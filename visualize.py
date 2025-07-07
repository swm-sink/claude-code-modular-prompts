#!/usr/bin/env python3
"""Framework visualization tool - generates visual representations."""

import os
from pathlib import Path
from collections import defaultdict

def generate_command_tree():
    """Generate command-module relationship tree."""
    tree = defaultdict(list)
    
    for cmd_file in Path('.claude/commands').glob('*.md'):
        with open(cmd_file, 'r') as f:
            content = f.read()
        
        # Extract module references
        modules = []
        for line in content.split('\n'):
            if 'modules/' in line and '.md' in line:
                start = line.find('modules/')
                end = line.find('.md', start) + 3
                if end > start:
                    modules.append(line[start:end])
        
        tree[cmd_file.stem] = modules
    
    return tree

def generate_category_breakdown():
    """Generate module category breakdown."""
    categories = defaultdict(int)
    
    for category_dir in Path('.claude/modules').iterdir():
        if category_dir.is_dir():
            module_count = len(list(category_dir.glob('*.md')))
            categories[category_dir.name] = module_count
    
    return dict(categories)

def create_ascii_tree(tree):
    """Create ASCII representation of command-module tree."""
    output = ["Framework Structure", "=" * 50, ""]
    
    for cmd, modules in sorted(tree.items()):
        output.append(f"/{cmd}")
        for i, module in enumerate(modules):
            prefix = "└── " if i == len(modules) - 1 else "├── "
            output.append(f"    {prefix}{Path(module).name}")
        output.append("")
    
    return "\n".join(output)

def create_category_chart(categories):
    """Create ASCII bar chart of categories."""
    output = ["Module Categories", "=" * 50, ""]
    
    max_count = max(categories.values()) if categories else 1
    
    for category, count in sorted(categories.items()):
        bar_length = int((count / max_count) * 30)
        bar = "█" * bar_length
        output.append(f"{category:15} {bar} {count}")
    
    return "\n".join(output)

def create_architecture_diagram():
    """Create simple architecture diagram."""
    return """
Framework Architecture
====================

    User Input
        │
        ▼
    ╔═══════════╗
    ║ Commands  ║ ──delegates──> ╔═══════════╗
    ╚═══════════╝                ║  Modules  ║
        │                        ╚═══════════╝
        │                             │
        ▼                             ▼
    ┌─────────┐                 ┌──────────┐
    │ /auto   │                 │ security │
    │ /task   │                 │ quality  │
    │ /feature│                 │ patterns │
    │ /swarm  │                 │ planning │
    │ ...     │                 │ ...      │
    └─────────┘                 └──────────┘
"""

def main():
    """Generate framework visualization."""
    print("🎨 Framework Visualizer v1.0.0\n")
    
    # Generate data
    tree = generate_command_tree()
    categories = generate_category_breakdown()
    
    # Create visualizations
    print(create_ascii_tree(tree))
    print("\n")
    print(create_category_chart(categories))
    print("\n")
    print(create_architecture_diagram())
    
    # Summary stats
    total_commands = len(tree)
    total_modules = sum(len(modules) for modules in tree.values())
    
    print("\nSummary Statistics")
    print("=" * 50)
    print(f"Total Commands: {total_commands}")
    print(f"Total Module References: {total_modules}")
    print(f"Average Modules/Command: {total_modules / max(total_commands, 1):.1f}")

if __name__ == "__main__":
    main()