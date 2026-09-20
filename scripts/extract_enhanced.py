#!/usr/bin/env python3
"""
Enhanced extraction with proper inheritance detection.
Generates comprehensive class hierarchy and attribute documentation.
"""

import sqlite3
import json
from pathlib import Path
from collections import defaultdict

DB_PATH = "/Users/andrejt/Research/ITS/CEN_TC_278_WG3/SG4-Transmodel/Model/TransmodelEcoSystem2024-EAv16-nk84_OpRa-v13.qea"

def query_db():
    """Extract classes with proper inheritance relationships."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get all classes
    cursor.execute("""
        SELECT Object_ID, Name, Object_Type, Abstract, Stereotype, Package_ID
        FROM t_object
        WHERE Object_ID IN (
            SELECT DISTINCT Object_ID FROM t_object 
            WHERE Package_ID IN (
                WITH RECURSIVE pkg_tree AS (
                    SELECT Package_ID FROM t_package WHERE Package_ID = 1319
                    UNION ALL
                    SELECT p.Package_ID FROM t_package p 
                    JOIN pkg_tree ON p.Parent_ID = pkg_tree.Package_ID
                )
                SELECT Package_ID FROM pkg_tree
            )
            AND Object_Type = 'Class'
        )
        ORDER BY Name
    """)
    
    classes = {}
    for row in cursor.fetchall():
        classes[row['Object_ID']] = dict(row)
    
    # Get inheritance relationships (generalization connectors)
    cursor.execute("""
        SELECT Start_Object_ID, End_Object_ID, Name
        FROM t_connector
        WHERE Connector_Type = 'Generalization'
    """)
    
    generalization_map = {}  # Maps child_id -> parent_id
    for row in cursor.fetchall():
        child_id = row[0]
        parent_id = row[1]
        generalization_map[child_id] = parent_id
    
    # Add inheritance info to classes
    for obj_id in classes:
        parent_id = generalization_map.get(obj_id)
        if parent_id and parent_id in classes:
            classes[obj_id]['parent_class_name'] = classes[parent_id]['Name']
            classes[obj_id]['parent_class_id'] = parent_id
        else:
            classes[obj_id]['parent_class_name'] = None
            classes[obj_id]['parent_class_id'] = None
    
    # Get attributes for each class
    cursor.execute("""
        SELECT Object_ID, Name, Type
        FROM t_attribute
        WHERE Object_ID IN ({})
        ORDER BY Pos
    """.format(','.join('?' * len(classes))), list(classes.keys()))
    
    attributes_by_class = defaultdict(list)
    for row in cursor.fetchall():
        attributes_by_class[row[0]].append({
            'name': row[1],
            'type': row[2]
        })
    
    conn.close()
    return classes, generalization_map, attributes_by_class

def generate_hierarchy():
    """Generate class hierarchy visualization."""
    classes, gen_map, attrs = query_db()
    
    # Build parent-child relationships
    hierarchy = defaultdict(list)
    for child_id, parent_id in gen_map.items():
        if child_id in classes and parent_id in classes:
            parent_name = classes[parent_id]['Name']
            child_name = classes[child_id]['Name']
            hierarchy[parent_name].append(child_name)
    
    return {
        'classes': classes,
        'hierarchy': hierarchy,
        'attributes': attrs,
        'gen_map': gen_map
    }

def format_report(data):
    """Generate markdown report."""
    classes = data['classes']
    hierarchy = data['hierarchy']
    attributes = data['attributes']
    
    report = []
    report.append("# OpRa Part 8 - Enhanced Class Extraction\n")
    report.append(f"**Total Classes:** {len(classes)}")
    report.append(f"**Classes with Inheritance:** {sum(1 for c in classes.values() if c['parent_class_name'])}")
    report.append(f"**Total Attributes:** {sum(len(attrs) for attrs in attributes.values())}\n")
    
    # Inheritance hierarchies
    if hierarchy:
        report.append("## Class Hierarchies\n")
        for parent in sorted(hierarchy.keys()):
            children = hierarchy[parent]
            report.append(f"### {parent}")
            for child in sorted(children):
                attrs_info = f" ({len(attributes.get(next((id for id, c in classes.items() if c['Name'] == child), None), []))} attrs)" if any(c['Name'] == child for c in classes.values()) else ""
                report.append(f"  - {child}{attrs_info}")
            report.append("")
    
    # All classes with details
    report.append("## All Classes (Detailed)\n")
    report.append("| Class | Parent | Abstract | # Attributes |")
    report.append("|-------|--------|----------|--------------|")
    
    for obj_id in sorted(classes.keys(), key=lambda x: classes[x]['Name']):
        cls = classes[obj_id]
        parent = cls['parent_class_name'] or "—"
        abstract = "✓" if cls['Abstract'] == '1' else ""
        attr_count = len(attributes.get(obj_id, []))
        report.append(f"| {cls['Name']} | {parent} | {abstract} | {attr_count} |")
    
    return "\n".join(report)

if __name__ == "__main__":
    data = generate_hierarchy()
    report = format_report(data)
    
    output_path = Path("/Users/andrejt/Research/repositories/git/OpRa/scripts/opra_part8_enhanced.md")
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(report)
    print(f"\n✅ Enhanced report saved to {output_path}")
