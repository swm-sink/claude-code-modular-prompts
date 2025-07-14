#!/usr/bin/env python3
"""
Generate comprehensive module guide from module inventory
"""

import os
import json
from pathlib import Path
import re

def extract_module_info(file_path):
    """Extract purpose and key info from module"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract purpose
    purpose_match = re.search(r'<purpose>\s*(.+?)\s*</purpose>', content, re.DOTALL)
    purpose = purpose_match.group(1).strip() if purpose_match else "No purpose documented"
    
    # Extract version
    version_match = re.search(r'\| version \| last_updated \| status \|.*?\n\|.*?\|\s*(\d+\.\d+\.\d+)', content, re.DOTALL)
    version = version_match.group(1) if version_match else "Unknown"
    
    # Check for critical patterns
    critical_patterns = ['tdd', 'routing', 'quality', 'session', 'thinking', 'module-composition']
    is_critical = any(pattern in str(file_path).lower() for pattern in critical_patterns)
    
    # Extract interface info
    has_interface = '<interface_contract>' in content
    
    return {
        'purpose': purpose.replace('\n', ' '),
        'version': version,
        'is_critical': is_critical,
        'has_interface': has_interface,
        'file_name': file_path.name
    }

def generate_module_guide():
    """Generate comprehensive module guide"""
    base_path = Path('.claude')
    categories = {
        'development': {
            'modules': [],
            'description': 'Core development workflow modules'
        },
        'patterns': {
            'modules': [],
            'description': 'Reusable pattern modules for consistent behavior'
        },
        'meta': {
            'modules': [],
            'description': 'Meta-framework modules for self-improvement and governance'
        },
        'frameworks': {
            'modules': [],
            'description': 'Prompt engineering frameworks'
        },
        'personas': {
            'modules': [],
            'description': 'Specialized engineering personas'
        }
    }
    
    # Find all modules
    for pattern in ['modules/**/*.md', 'prompt_eng/**/*.md']:
        for path in base_path.glob(pattern):
            if path.name != 'README.md' and 'STRUCTURE' not in path.name:
                info = extract_module_info(path)
                info['path'] = str(path.relative_to(base_path))
                
                # Categorize
                if 'modules/development' in str(path):
                    categories['development']['modules'].append(info)
                elif 'modules/patterns' in str(path):
                    categories['patterns']['modules'].append(info)
                elif 'modules/meta' in str(path):
                    categories['meta']['modules'].append(info)
                elif 'prompt_eng/frameworks' in str(path):
                    categories['frameworks']['modules'].append(info)
                elif 'prompt_eng/personas' in str(path):
                    categories['personas']['modules'].append(info)
    
    # Generate guide
    guide = []
    guide.append("# Claude Code Modular Framework - Master Module Guide")
    guide.append("\n**Generated**: $(date '+%Y-%m-%d')")
    guide.append(f"**Total Modules**: {sum(len(cat['modules']) for cat in categories.values())}")
    guide.append("\n## Overview")
    guide.append("\nThis guide provides a comprehensive listing of all modules in the Claude Code Modular Framework.")
    guide.append("Modules are organized by category and include their purpose, version, and critical status.")
    
    # Table of Contents
    guide.append("\n## Table of Contents\n")
    for category, data in categories.items():
        if data['modules']:
            guide.append(f"- [{category.title()}](#{category}) ({len(data['modules'])} modules)")
    
    # Critical Modules Section
    guide.append("\n## Critical Modules")
    guide.append("\nThese modules are essential for core framework functionality:\n")
    
    critical_modules = []
    for category, data in categories.items():
        for module in data['modules']:
            if module['is_critical']:
                critical_modules.append((category, module))
    
    for category, module in sorted(critical_modules, key=lambda x: x[1]['file_name']):
        guide.append(f"- **{module['file_name']}** ({category})")
        guide.append(f"  - Purpose: {module['purpose'][:100]}...")
        guide.append(f"  - Path: `{module['path']}`")
    
    # Category Sections
    for category, data in categories.items():
        if not data['modules']:
            continue
            
        guide.append(f"\n## {category.title()}")
        guide.append(f"\n{data['description']}\n")
        
        # Sort modules by name
        for module in sorted(data['modules'], key=lambda x: x['file_name']):
            guide.append(f"### {module['file_name']}")
            guide.append(f"- **Version**: {module['version']}")
            guide.append(f"- **Path**: `{module['path']}`")
            guide.append(f"- **Critical**: {'Yes' if module['is_critical'] else 'No'}")
            guide.append(f"- **Has Interface**: {'Yes' if module['has_interface'] else 'No'}")
            guide.append(f"- **Purpose**: {module['purpose']}")
            guide.append("")
    
    # Usage Guide
    guide.append("\n## Module Usage Guide")
    guide.append("\n### Accessing Modules")
    guide.append("\nModules are accessed through commands or direct invocation:")
    guide.append("```bash")
    guide.append("# Through commands")
    guide.append("/task --help  # Uses development/task-management.md")
    guide.append("/auto --help  # Uses patterns/intelligent-routing.md")
    guide.append("```")
    
    guide.append("\n### Module Dependencies")
    guide.append("\nModules can depend on other modules. Always check dependencies before using:")
    guide.append("```xml")
    guide.append("<dependencies>")
    guide.append("  <module>patterns/thinking-pattern-template.md</module>")
    guide.append("  <module>quality/universal-quality-gates.md</module>")
    guide.append("</dependencies>")
    guide.append("```")
    
    guide.append("\n### Integration Patterns")
    guide.append("\nModules follow standard integration patterns:")
    guide.append("1. **Command Integration**: Commands delegate to modules")
    guide.append("2. **Module Composition**: Modules can compose other modules")
    guide.append("3. **Quality Gates**: All modules respect quality gates")
    guide.append("4. **Error Handling**: Standardized error recovery")
    
    # Module Statistics
    guide.append("\n## Module Statistics")
    
    total_modules = sum(len(cat['modules']) for cat in categories.values())
    critical_count = sum(1 for cat in categories.values() for m in cat['modules'] if m['is_critical'])
    interface_count = sum(1 for cat in categories.values() for m in cat['modules'] if m['has_interface'])
    
    guide.append(f"\n- **Total Modules**: {total_modules}")
    guide.append(f"- **Critical Modules**: {critical_count} ({critical_count/total_modules*100:.1f}%)")
    guide.append(f"- **With Interfaces**: {interface_count} ({interface_count/total_modules*100:.1f}%)")
    
    for category, data in categories.items():
        if data['modules']:
            guide.append(f"- **{category.title()}**: {len(data['modules'])} modules")
    
    return '\n'.join(guide)

if __name__ == "__main__":
    guide_content = generate_module_guide()
    
    # Write the guide
    with open('.claude/modules/MASTER_MODULE_GUIDE.md', 'w') as f:
        f.write(guide_content)
    
    print("Master Module Guide generated successfully!")
    print(f"Location: .claude/modules/MASTER_MODULE_GUIDE.md")