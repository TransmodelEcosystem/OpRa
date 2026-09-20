#!/usr/bin/env python3
"""
Extract class diagrams from OpRa Part 8 EA model.
Queries SQLite database (.qea) to extract classes, packages, inheritance, and attributes.
"""

import sqlite3
import json
from collections import defaultdict
from pathlib import Path

# Database path
DB_PATH = "/Users/andrejt/Research/ITS/CEN_TC_278_WG3/SG4-Transmodel/Model/TransmodelEcoSystem2024-EAv16-nk84_OpRa-v13.qea"

def get_db_connection():
    """Create and return database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def get_all_subpackages(conn, parent_package_id):
    """Recursively get all package IDs under a parent package."""
    package_ids = {parent_package_id}
    to_process = [parent_package_id]
    
    while to_process:
        current_id = to_process.pop(0)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Package_ID FROM t_package 
            WHERE Parent_ID = ?
        """, (current_id,))
        
        for row in cursor.fetchall():
            pkg_id = row[0]
            if pkg_id not in package_ids:
                package_ids.add(pkg_id)
                to_process.append(pkg_id)
    
    return package_ids

def get_package_info(conn, package_id):
    """Get package name and details."""
    cursor = conn.cursor()
    cursor.execute("SELECT Package_ID, Name, Parent_ID FROM t_package WHERE Package_ID = ?", (package_id,))
    result = cursor.fetchone()
    return dict(result) if result else None

def get_all_classes(conn, package_ids):
    """Get all classes in the given packages."""
    if not package_ids:
        return []
    
    placeholders = ','.join('?' * len(package_ids))
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT Object_ID, Name, Package_ID, Stereotype, Object_Type, Abstract, ParentID 
        FROM t_object 
        WHERE Package_ID IN ({placeholders})
        AND Object_Type = 'Class'
        ORDER BY Name
    """, list(package_ids))
    
    classes = []
    for row in cursor.fetchall():
        classes.append(dict(row))
    
    return classes

def get_class_attributes(conn, object_id):
    """Get attributes for a class."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ID, Name, Type, Stereotype, `Default`
        FROM t_attribute
        WHERE Object_ID = ?
        ORDER BY Pos
    """, (object_id,))
    
    attributes = []
    for row in cursor.fetchall():
        attributes.append(dict(row))
    
    return attributes

def get_class_inheritance(conn, object_id):
    """Get parent class (inheritance) for a class."""
    cursor = conn.cursor()
    # Check t_xref for generalization relationships
    # In EA, Client is usually the subclass and Supplier is the superclass for generalization
    cursor.execute("""
        SELECT DISTINCT t_object.Object_ID, t_object.Name
        FROM t_xref
        JOIN t_object ON t_xref.Supplier = t_object.Name
        WHERE t_xref.Client = (SELECT Name FROM t_object WHERE Object_ID = ?)
        AND t_xref.Type = 'Generalization'
        LIMIT 1
    """, (object_id,))
    
    result = cursor.fetchone()
    return dict(result) if result else None

def get_class_relationships(conn, object_id):
    """Get key relationships/associations for a class."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Connector_ID, Name, Connector_Type, Start_Object_ID, End_Object_ID
        FROM t_connector
        WHERE Start_Object_ID = ? OR End_Object_ID = ?
        LIMIT 5
    """, (object_id, object_id))
    
    relationships = []
    for row in cursor.fetchall():
        relationships.append(dict(row))
    
    return relationships

def get_package_tree(conn, package_id, depth=0, tree=None):
    """Build a tree structure of packages."""
    if tree is None:
        tree = {}
    
    info = get_package_info(conn, package_id)
    if not info:
        return tree
    
    cursor = conn.cursor()
    cursor.execute("SELECT Package_ID, Name FROM t_package WHERE Parent_ID = ?", (package_id,))
    
    children = {}
    for row in cursor.fetchall():
        child_id = row[0]
        child_name = row[1]
        children[child_name] = get_package_tree(conn, child_id, depth + 1)
    
    tree[info['Name']] = children if children else None
    return tree

def extract_part8_data():
    """Main extraction function."""
    conn = get_db_connection()
    
    try:
        # Part 8 root package ID
        part8_id = 1319
        
        print("🔍 Querying OpRa Part 8 EA Model...")
        print(f"   Root Package ID: {part8_id}")
        
        # Get all subpackages
        package_ids = get_all_subpackages(conn, part8_id)
        print(f"   Found {len(package_ids)} packages (including root)")
        
        # Get all classes
        classes = get_all_classes(conn, package_ids)
        print(f"   Found {len(classes)} classes")
        
        # Build package tree for reference
        package_tree = get_package_tree(conn, part8_id)
        
        # Organize classes by package
        classes_by_package = defaultdict(list)
        for cls in classes:
            pkg_info = get_package_info(conn, cls['Package_ID'])
            if pkg_info:
                classes_by_package[pkg_info['Name']].append(cls)
        
        # Enrich class data with inheritance and attributes
        result = {
            "extraction_date": "2026-05-14",
            "model_file": Path(DB_PATH).name,
            "part8_root_id": part8_id,
            "total_packages": len(package_ids),
            "total_classes": len(classes),
            "package_tree": package_tree,
            "classes_by_package": {}
        }
        
        for pkg_name in sorted(classes_by_package.keys()):
            pkg_classes = classes_by_package[pkg_name]
            enriched_classes = []
            
            for cls in sorted(pkg_classes, key=lambda x: x['Name']):
                parent = get_class_inheritance(conn, cls['Object_ID'])
                attributes = get_class_attributes(conn, cls['Object_ID'])
                relationships = get_class_relationships(conn, cls['Object_ID'])
                
                enriched = {
                    "object_id": cls['Object_ID'],
                    "name": cls['Name'],
                    "stereotype": cls['Stereotype'],
                    "object_type": cls['Object_Type'],
                    "is_abstract": cls['Abstract'],
                    "parent_class": parent['Name'] if parent else None,
                    "attributes": [
                        {
                            "name": attr['Name'],
                            "type": attr['Type'],
                            "stereotype": attr['Stereotype']
                        }
                        for attr in attributes[:3]  # Top 3 attributes
                    ],
                    "relationships": [
                        {
                            "name": rel['Name'],
                            "type": rel['Connector_Type']
                        }
                        for rel in relationships[:3]  # Top 3 relationships
                    ]
                }
                enriched_classes.append(enriched)
            
            result["classes_by_package"][pkg_name] = enriched_classes
        
        return result
        
    finally:
        conn.close()

def print_markdown_table(data):
    """Print results as markdown table."""
    output = []
    output.append("# OpRa Part 8 Class Extraction\n")
    output.append(f"**Extraction Date:** {data['extraction_date']}")
    output.append(f"**Model File:** {data['model_file']}")
    output.append(f"**Total Packages:** {data['total_packages']}")
    output.append(f"**Total Classes:** {data['total_classes']}\n")
    
    output.append("## Package Tree")
    output.append("```")
    import json
    output.append(json.dumps(data['package_tree'], indent=2))
    output.append("```\n")
    
    output.append("## Classes by Package\n")
    
    for pkg_name, classes in data['classes_by_package'].items():
        output.append(f"### {pkg_name} ({len(classes)} classes)\n")
        
        # Table header
        output.append("| Class | Parent | Abstract | Key Attributes | Relationships |")
        output.append("|-------|--------|----------|----------------|----------------|")
        
        for cls in classes:
            attrs = ", ".join([f"{a['name']}: {a['type']}" for a in cls['attributes']])
            rels = ", ".join([f"{r['name']} ({r['type']})" for r in cls['relationships']])
            parent = cls['parent_class'] or "-"
            abstract = "✓" if cls['is_abstract'] else ""
            
            output.append(f"| {cls['name']} | {parent} | {abstract} | {attrs} | {rels} |")
        
        output.append("")
    
    return "\n".join(output)

if __name__ == "__main__":
    # Extract data
    data = extract_part8_data()
    
    # Save as JSON
    json_output = Path("/Users/andrejt/Research/repositories/git/OpRa/scripts/opra_part8_classes.json")
    with open(json_output, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"\n✅ JSON output saved to: {json_output}")
    
    # Save as Markdown
    md_output = Path("/Users/andrejt/Research/repositories/git/OpRa/scripts/opra_part8_classes.md")
    with open(md_output, 'w') as f:
        f.write(print_markdown_table(data))
    print(f"✅ Markdown output saved to: {md_output}")
    
    # Print summary
    print("\n" + "="*60)
    print(print_markdown_table(data))
