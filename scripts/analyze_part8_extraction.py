#!/usr/bin/env python3
"""
Analyze and create comprehensive summary of OpRa Part 8 classes.
Generates inheritance hierarchies and package statistics.
"""

import json
from pathlib import Path
from collections import defaultdict

JSON_PATH = "/Users/andrejt/Research/repositories/git/OpRa/scripts/opra_part8_classes.json"

def analyze_classes():
    """Load and analyze the extracted class data."""
    with open(JSON_PATH) as f:
        data = json.load(f)
    
    # Statistics
    print("📊 OpRa Part 8 CLASS EXTRACTION SUMMARY")
    print("=" * 70)
    print(f"✅ Extracted: {data['total_classes']} classes from {data['total_packages']} packages")
    print(f"📅 Date: {data['extraction_date']}")
    print()
    
    # Organize by package group (primary categories)
    package_groups = {
        "EF": [],  # Explicit Frames
        "ID": [],  # Indicators
        "RC": [],  # Reusable Components
        "QM": []   # Query Model
    }
    
    classes_by_pkg = data['classes_by_package']
    
    for pkg_name, classes in classes_by_pkg.items():
        # Determine group prefix
        if "Explicit Frame" in pkg_name or "EF" in pkg_name:
            group = "EF"
        elif "Indicator" in pkg_name and "Query" not in pkg_name:
            group = "ID"
        elif "Query" in pkg_name or "QM" in pkg_name:
            group = "QM"
        else:
            group = "RC"
        
        for cls in classes:
            package_groups[group].append({
                'name': cls['name'],
                'package': pkg_name,
                'parent': cls['parent_class'],
                'attributes': cls['attributes'],
                'is_abstract': cls['is_abstract'] == '1'
            })
    
    # Print by group
    print("📦 CLASSES BY CATEGORY:")
    print("-" * 70)
    for group in ["EF", "ID", "RC", "QM"]:
        count = len(package_groups[group])
        group_names = {
            "EF": "Explicit Frames",
            "ID": "Indicators", 
            "RC": "Reusable Components",
            "QM": "Query Model"
        }
        print(f"\n  {group} - {group_names[group]}: {count} classes")
        for cls in sorted(package_groups[group], key=lambda x: x['name']):
            abstract_marker = "(abstract)" if cls['is_abstract'] else ""
            parent_info = f"→ {cls['parent']}" if cls['parent'] else ""
            print(f"     • {cls['name']} {parent_info} {abstract_marker}")
    
    # Inheritance analysis
    print("\n\n🔗 INHERITANCE HIERARCHY:")
    print("-" * 70)
    
    all_classes = []
    for pkg_classes in classes_by_pkg.values():
        all_classes.extend(pkg_classes)
    
    # Find class hierarchies
    parent_child_map = defaultdict(list)
    orphan_classes = []
    
    for cls in all_classes:
        parent = cls['parent_class']
        if parent:
            parent_child_map[parent].append(cls['name'])
        else:
            orphan_classes.append(cls['name'])
    
    # Print hierarchies
    if parent_child_map:
        print("\nClasses with inheritance relationships:")
        for parent, children in sorted(parent_child_map.items()):
            print(f"  {parent}")
            for child in sorted(children):
                print(f"    └─ {child}")
    
    print(f"\nOrphan/Root classes (no parent): {len(orphan_classes)}")
    
    # Statistics
    print("\n\n📈 STATISTICS:")
    print("-" * 70)
    total_attrs = sum(len(cls['attributes']) for cls in all_classes)
    avg_attrs = total_attrs / len(all_classes) if all_classes else 0
    abstract_count = sum(1 for cls in all_classes if cls['is_abstract'])
    
    print(f"  Total classes: {len(all_classes)}")
    print(f"  Abstract classes: {abstract_count}")
    print(f"  Concrete classes: {len(all_classes) - abstract_count}")
    print(f"  Total attributes: {total_attrs}")
    print(f"  Avg attributes per class: {avg_attrs:.1f}")
    print(f"  Classes with inheritance: {len(parent_child_map)}")
    print(f"  Root classes (no parent): {len(orphan_classes)}")
    
    # Package distribution
    print("\n\n📍 PACKAGE DISTRIBUTION:")
    print("-" * 70)
    pkg_counts = defaultdict(int)
    for pkg_name, classes in classes_by_pkg.items():
        pkg_counts[pkg_name] = len(classes)
    
    for pkg_name in sorted(pkg_counts.keys(), key=lambda x: (-pkg_counts[x], x)):
        count = pkg_counts[pkg_name]
        bar = "█" * (count // 2) + ("▌" if count % 2 else "")
        print(f"  {count:2d} classes  {bar}  {pkg_name}")
    
    return data, package_groups

if __name__ == "__main__":
    data, groups = analyze_classes()
