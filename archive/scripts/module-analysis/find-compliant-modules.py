#!/usr/bin/env python3
import json
from pathlib import Path

with open('/Users/smenssink/Documents/Github/claude-code-modular-prompts/internal/data/v14-validation-results.json', 'r') as f:
    data = json.load(f)
    total = data['total_modules']
    missing = data['missing_sections']
    
    print(f'Total modules: {total}')
    print(f'Modules with issues: {len(missing)}')
    print(f'\nCompliant modules:')
    
    # Find modules not in missing_sections
    modules_dir = Path('/Users/smenssink/Documents/Github/claude-code-modular-prompts/.claude/modules')
    all_modules = list(modules_dir.rglob('*.md'))
    all_modules = [f for f in all_modules if f.name != 'README.md']
    
    compliant_count = 0
    for module in all_modules:
        rel_path = module.relative_to(modules_dir)
        if str(rel_path) not in missing:
            print(f'  - {rel_path}')
            compliant_count += 1
    
    print(f'\nTotal compliant: {compliant_count}')