#!/usr/bin/env python3
"""Unified dependency visualization tool - creates various visual representations.

This tool consolidates functionality from:
- generate-dependency-graph.py
- utilities/create_dependency_graph.py
- utilities/visualize.py
"""

import argparse
import json
import sys
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Add the parent directory to the path so we can import from lib
sys.path.insert(0, str(Path(__file__).parent))

from lib.module_utils import ModuleAnalyzer


def create_ascii_graph(dependencies, title="Module Dependencies"):
    """Create an ASCII representation of dependencies."""
    output = []
    output.append("=" * 60)
    output.append(f"{title:^60}")
    output.append("=" * 60)
    output.append("")
    
    # Group by category
    categories = defaultdict(list)
    for module in dependencies:
        if '/' in module:
            category = module.split('/')[0]
            categories[category].append(module)
    
    # Display by category
    for category, modules in sorted(categories.items()):
        output.append(f"[{category.upper()}]")
        for module in sorted(modules):
            deps = dependencies[module]
            if deps:
                output.append(f"  └─ {module}")
                for i, dep in enumerate(sorted(deps)):
                    prefix = "    └─" if i == len(deps) - 1 else "    ├─"
                    output.append(f"{prefix} → {dep}")
            else:
                output.append(f"  └─ {module} (no dependencies)")
        output.append("")
    
    return "\n".join(output)


def create_mermaid_graph(dependencies, title="Module Dependencies"):
    """Create a Mermaid diagram for dependencies."""
    output = []
    output.append("```mermaid")
    output.append("graph TD")
    output.append(f"    title[{title}]")
    output.append("    style title fill:#f9f,stroke:#333,stroke-width:4px")
    output.append("")
    
    # Create node IDs mapping
    node_ids = {}
    for i, module in enumerate(sorted(set(dependencies.keys()) | 
                                    set(dep for deps in dependencies.values() for dep in deps))):
        safe_id = f"node{i}"
        node_ids[module] = safe_id
    
    # Add nodes with labels
    categories = defaultdict(list)
    for module, node_id in node_ids.items():
        if '/' in module:
            category = module.split('/')[0]
            categories[category].append((module, node_id))
    
    # Define category styles
    category_styles = {
        'modules': 'fill:#e1f5fe,stroke:#01579b',
        'patterns': 'fill:#f3e5f5,stroke:#4a148c',
        'quality': 'fill:#e8f5e9,stroke:#1b5e20',
        'development': 'fill:#fff3e0,stroke:#e65100',
        'security': 'fill:#ffebee,stroke:#b71c1c',
        'system': 'fill:#e0f2f1,stroke:#004d40',
        'meta': 'fill:#fce4ec,stroke:#880e4f'
    }
    
    # Add nodes by category
    for category, nodes in sorted(categories.items()):
        output.append(f"    subgraph {category}")
        for module, node_id in nodes:
            short_name = module.split('/')[-1].replace('.md', '')
            output.append(f'        {node_id}["{short_name}"]')
        output.append("    end")
    
    # Add edges
    output.append("")
    for module, deps in dependencies.items():
        if module in node_ids:
            for dep in deps:
                if dep in node_ids:
                    output.append(f"    {node_ids[module]} --> {node_ids[dep]}")
    
    # Apply styles
    output.append("")
    for category, style in category_styles.items():
        for module, node_id in categories.get(category, []):
            output.append(f"    style {node_id} {style}")
    
    output.append("```")
    return "\n".join(output)


def create_dot_graph(dependencies, output_file="dependency_graph"):
    """Create a Graphviz DOT file and optionally render it."""
    dot_content = []
    dot_content.append('digraph "Module Dependencies" {')
    dot_content.append('    rankdir=TB;')
    dot_content.append('    node [shape=box, style=rounded];')
    dot_content.append('')
    
    # Group by category for clustering
    categories = defaultdict(list)
    for module in set(dependencies.keys()) | set(dep for deps in dependencies.values() for dep in deps):
        if '/' in module:
            category = module.split('/')[0]
            categories[category].append(module)
    
    # Define category colors
    category_colors = {
        'modules': '#e1f5fe',
        'patterns': '#f3e5f5',
        'quality': '#e8f5e9',
        'development': '#fff3e0',
        'security': '#ffebee',
        'system': '#e0f2f1',
        'meta': '#fce4ec'
    }
    
    # Create subgraphs for categories
    for category, modules in sorted(categories.items()):
        color = category_colors.get(category, '#f0f0f0')
        dot_content.append(f'    subgraph "cluster_{category}" {{')
        dot_content.append(f'        label="{category.upper()}";')
        dot_content.append(f'        style=filled;')
        dot_content.append(f'        fillcolor="{color}";')
        dot_content.append(f'        node [fillcolor=white];')
        
        for module in sorted(modules):
            short_name = module.split('/')[-1].replace('.md', '')
            dot_content.append(f'        "{module}" [label="{short_name}"];')
        
        dot_content.append('    }')
        dot_content.append('')
    
    # Add edges
    for module, deps in dependencies.items():
        for dep in sorted(deps):
            dot_content.append(f'    "{module}" -> "{dep}";')
    
    dot_content.append('}')
    
    # Write DOT file
    dot_file = f"{output_file}.dot"
    with open(dot_file, 'w') as f:
        f.write('\n'.join(dot_content))
    
    print(f"✅ DOT file created: {dot_file}")
    
    # Try to render with graphviz if available
    try:
        import subprocess
        formats = ['png', 'svg']
        for fmt in formats:
            output_path = f"{output_file}.{fmt}"
            subprocess.run(['dot', '-T', fmt, dot_file, '-o', output_path], 
                         check=True, capture_output=True)
            print(f"✅ Rendered {fmt.upper()}: {output_path}")
    except (ImportError, subprocess.CalledProcessError, FileNotFoundError):
        print("ℹ️  Install graphviz to render the graph: brew install graphviz")
    
    return dot_file


def analyze_dependency_metrics(dependencies):
    """Calculate dependency metrics and statistics."""
    metrics = {
        'total_modules': len(dependencies),
        'modules_with_deps': sum(1 for deps in dependencies.values() if deps),
        'total_dependencies': sum(len(deps) for deps in dependencies.values()),
        'avg_dependencies': 0,
        'max_dependencies': 0,
        'most_dependent': None,
        'most_depended_on': None,
        'categories': defaultdict(int)
    }
    
    if dependencies:
        dep_counts = {m: len(deps) for m, deps in dependencies.items() if deps}
        if dep_counts:
            metrics['avg_dependencies'] = sum(dep_counts.values()) / len(dep_counts)
            metrics['max_dependencies'] = max(dep_counts.values())
            metrics['most_dependent'] = max(dep_counts.items(), key=lambda x: x[1])
        
        # Find most depended-on modules
        depended_on = defaultdict(int)
        for deps in dependencies.values():
            for dep in deps:
                depended_on[dep] += 1
        
        if depended_on:
            metrics['most_depended_on'] = max(depended_on.items(), key=lambda x: x[1])
        
        # Category statistics
        for module in dependencies:
            if '/' in module:
                category = module.split('/')[0]
                metrics['categories'][category] += 1
    
    return metrics


def create_summary_report(dependencies, metrics):
    """Create a summary report of dependencies."""
    output = []
    output.append("# Dependency Analysis Summary")
    output.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append("")
    
    output.append("## Overview")
    output.append(f"- Total Modules: {metrics['total_modules']}")
    output.append(f"- Modules with Dependencies: {metrics['modules_with_deps']}")
    output.append(f"- Total Dependencies: {metrics['total_dependencies']}")
    output.append(f"- Average Dependencies per Module: {metrics['avg_dependencies']:.1f}")
    output.append("")
    
    if metrics['most_dependent']:
        output.append("## Key Modules")
        module, count = metrics['most_dependent']
        output.append(f"- Most Dependencies: {module} ({count} dependencies)")
        
        if metrics['most_depended_on']:
            module, count = metrics['most_depended_on']
            output.append(f"- Most Depended On: {module} ({count} modules depend on it)")
    
    output.append("")
    output.append("## Dependencies by Category")
    for category, count in sorted(metrics['categories'].items()):
        output.append(f"- {category}: {count} modules")
    
    return "\n".join(output)


def main():
    """Main entry point for the dependency visualizer."""
    parser = argparse.ArgumentParser(
        description="Visualize module dependencies in various formats"
    )
    parser.add_argument(
        '--format',
        choices=['ascii', 'mermaid', 'dot', 'all'],
        default='ascii',
        help='Output format for visualization'
    )
    parser.add_argument(
        '--input',
        help='Input JSON file with dependency data (from module_analyzer.py)'
    )
    parser.add_argument(
        '--output',
        default='dependency_visualization',
        help='Output file prefix'
    )
    parser.add_argument(
        '--base-path',
        default='.claude',
        help='Base path for module analysis'
    )
    parser.add_argument(
        '--summary',
        action='store_true',
        help='Include summary report'
    )
    
    args = parser.parse_args()
    
    # Load or generate dependency data
    if args.input and os.path.exists(args.input):
        print(f"Loading dependency data from {args.input}...")
        with open(args.input, 'r') as f:
            data = json.load(f)
        if 'dependency_graph' in data:
            dependencies = data['dependency_graph']
        else:
            dependencies = data.get('dependencies', {})
    else:
        print(f"Analyzing modules in {args.base_path}...")
        analyzer = ModuleAnalyzer(args.base_path)
        analyzer.find_modules()
        dependencies = analyzer.generate_dependency_graph()
    
    if not dependencies:
        print("No dependencies found!")
        sys.exit(1)
    
    # Calculate metrics
    metrics = analyze_dependency_metrics(dependencies)
    
    # Generate visualizations based on format
    if args.format in ['ascii', 'all']:
        ascii_output = create_ascii_graph(dependencies)
        if args.format == 'ascii':
            print(ascii_output)
        else:
            with open(f"{args.output}_ascii.txt", 'w') as f:
                f.write(ascii_output)
            print(f"✅ ASCII visualization saved to {args.output}_ascii.txt")
    
    if args.format in ['mermaid', 'all']:
        mermaid_output = create_mermaid_graph(dependencies)
        output_file = f"{args.output}_mermaid.md"
        with open(output_file, 'w') as f:
            f.write(mermaid_output)
        print(f"✅ Mermaid diagram saved to {output_file}")
    
    if args.format in ['dot', 'all']:
        create_dot_graph(dependencies, args.output)
    
    # Generate summary if requested
    if args.summary:
        summary = create_summary_report(dependencies, metrics)
        summary_file = f"{args.output}_summary.md"
        with open(summary_file, 'w') as f:
            f.write(summary)
        print(f"✅ Summary report saved to {summary_file}")
    
    print(f"\n📊 Visualization complete!")
    print(f"   Total modules: {metrics['total_modules']}")
    print(f"   Total dependencies: {metrics['total_dependencies']}")


if __name__ == "__main__":
    main()