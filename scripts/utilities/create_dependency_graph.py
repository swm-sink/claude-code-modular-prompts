#!/usr/bin/env python3
"""
Create a visual dependency graph for the module framework.
Generates both text-based and graphviz representations.
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import subprocess

def load_analysis_data():
    """Load the module dependency analysis data."""
    with open('module_dependency_analysis.json', 'r') as f:
        return json.load(f)

def create_text_dependency_map(data):
    """Create a text-based dependency map."""
    output = []
    output.append("# Module Dependency Map\n")
    output.append("## Summary\n")
    
    summary = data['summary']
    output.append(f"- Total Modules: {summary['total_modules']}")
    output.append(f"- Total References: {summary['total_references']}")
    output.append(f"- Broken References: {summary['total_broken_references']} ({summary['broken_percentage']:.1f}%)")
    output.append(f"- Circular Dependencies: {summary['circular_dependencies_count']}")
    
    # Broken references section
    output.append("\n## Broken References by Module\n")
    if data.get('broken_references'):
        for module, refs in sorted(data['broken_references'].items()):
            output.append(f"\n**{module}** ({len(refs)} broken)")
            for ref in refs:
                output.append(f"  ❌ → {ref}")
    
    # Valid references section
    output.append("\n## Valid References by Module\n")
    if data.get('valid_references'):
        for module, refs in sorted(data['valid_references'].items()):
            output.append(f"\n**{module}** ({len(refs)} valid)")
            for ref in refs:
                output.append(f"  ✅ → {ref}")
    
    # Circular dependencies section
    output.append("\n## Circular Dependencies\n")
    if data.get('circular_dependencies'):
        for cycle in data['circular_dependencies']:
            output.append(f"- {' ↔ '.join(cycle)}")
    else:
        output.append("No circular dependencies found.")
    
    # Critical missing modules
    output.append("\n## Critical Missing Modules\n")
    if data.get('critical_missing_modules'):
        for module in data['critical_missing_modules']:
            output.append(f"- {module}")
    
    return '\n'.join(output)

def create_graphviz_dot(data):
    """Create a Graphviz DOT file for visualization."""
    dot_lines = []
    dot_lines.append('digraph ModuleDependencies {')
    dot_lines.append('  rankdir=TB;')
    dot_lines.append('  node [shape=box, style=rounded];')
    dot_lines.append('  edge [color=gray];')
    
    # Collect all modules
    all_modules = set()
    if data.get('broken_references'):
        all_modules.update(data['broken_references'].keys())
        for refs in data['broken_references'].values():
            all_modules.update(refs)
    if data.get('valid_references'):
        all_modules.update(data['valid_references'].keys())
        for refs in data['valid_references'].values():
            all_modules.update(refs)
    
    # Define node colors based on status
    for module in all_modules:
        name = os.path.basename(module).replace('.md', '')
        if module in data.get('broken_references', {}):
            num_broken = len(data['broken_references'][module])
            color = "red" if num_broken > 5 else "orange"
            dot_lines.append(f'  "{name}" [color={color}, fontcolor={color}];')
        else:
            dot_lines.append(f'  "{name}" [color=green];')
    
    # Add edges for valid dependencies
    seen_edges = set()
    if data.get('valid_references'):
        for source_file, refs in data['valid_references'].items():
            source = os.path.basename(source_file).replace('.md', '')
            for ref in refs:
                target = os.path.basename(ref).replace('.md', '')
                edge = (source, target)
                if edge not in seen_edges:
                    seen_edges.add(edge)
                    dot_lines.append(f'  "{source}" -> "{target}";')
    
    # Highlight circular dependencies
    if data.get('circular_dependencies'):
        for cycle in data['circular_dependencies']:
            for i in range(len(cycle)):
                source = os.path.basename(cycle[i]).replace('.md', '')
                target = os.path.basename(cycle[(i + 1) % len(cycle)]).replace('.md', '')
                dot_lines.append(f'  "{source}" -> "{target}" [color=red, penwidth=2];')
    
    dot_lines.append('}')
    return '\n'.join(dot_lines)

def main():
    """Generate dependency maps."""
    # Load analysis data
    data = load_analysis_data()
    
    # Create text-based map
    text_map = create_text_dependency_map(data)
    with open('module_dependency_map.md', 'w') as f:
        f.write(text_map)
    print("✅ Created module_dependency_map.md")
    
    # Create Graphviz DOT file
    dot_content = create_graphviz_dot(data)
    with open('module_dependencies.dot', 'w') as f:
        f.write(dot_content)
    print("✅ Created module_dependencies.dot")
    
    # Try to generate PNG if graphviz is installed
    try:
        subprocess.run(['dot', '-Tpng', 'module_dependencies.dot', '-o', 'module_dependencies.png'], 
                      check=True, capture_output=True)
        print("✅ Created module_dependencies.png")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ℹ️  Graphviz not available - skipping PNG generation")
        print("   Install with: brew install graphviz (macOS) or apt-get install graphviz (Ubuntu)")

if __name__ == "__main__":
    main()