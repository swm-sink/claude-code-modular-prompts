#!/usr/bin/env python3
"""Framework validation tool - detects and reports common issues."""

import os
import re
import sys
from pathlib import Path

def check_command_delegation(filepath):
    """Check if command has proper delegation block."""
    # Commands that orchestrate don't need delegation blocks
    orchestrator_commands = ['auto.md', 'query.md', 'swarm.md', 'task.md', 'docs.md']
    if filepath.name in orchestrator_commands:
        return None
        
    with open(filepath, 'r') as f:
        content = f.read()
    if '<delegation' not in content:
        return f"Missing delegation block in {filepath}"
    return None

def check_module_references():
    """Check for broken module references."""
    issues = []
    modules_dir = Path('.claude/modules')
    
    for cmd_file in Path('.claude/commands').glob('*.md'):
        with open(cmd_file, 'r') as f:
            content = f.read()
        module_refs = re.findall(r'modules/([^/]+/[^.]+\.md)', content)
        
        for ref in module_refs:
            if not (modules_dir / ref).exists():
                issues.append(f"Broken reference in {cmd_file.name}: {ref}")
    
    return issues

def check_version_headers():
    """Check for missing version headers in modules."""
    issues = []
    
    for module_file in Path('.claude/modules').rglob('*.md'):
        with open(module_file, 'r') as f:
            content = f.read()
        
        # Check for version in frontmatter, header, or metadata
        has_version = False
        
        # Check frontmatter
        if 'version:' in content[:200]:
            has_version = True
        
        # Check header
        lines = content.split('\n')
        for line in lines[:10]:
            if line.startswith('# ') and 'v' in line.lower():
                has_version = True
                break
        
        # Check metadata tags
        if '<version>' in content[:500]:
            has_version = True
        
        if not has_version:
            issues.append(f"Missing version in {module_file}")
    
    return issues

def check_file_locations():
    """Check for files in wrong locations."""
    issues = []
    
    # Check for non-md files in .claude
    for file in Path('.claude').rglob('*'):
        if file.is_file() and not file.suffix == '.md' and file.name != '.DS_Store':
            issues.append(f"Non-markdown file in .claude: {file}")
    
    # Check for orphaned test files
    for test_file in Path('tests').rglob('test_*.py'):
        module_name = test_file.stem.replace('test_', '')
        if not Path(f'src/framework/{module_name}.py').exists():
            issues.append(f"Orphaned test file: {test_file}")
    
    return issues

def main():
    """Run all validation checks."""
    print("🔍 Framework Validation Tool v1.0.0\n")
    
    all_issues = []
    
    # Check commands
    for cmd_file in Path('.claude/commands').glob('*.md'):
        issue = check_command_delegation(cmd_file)
        if issue:
            all_issues.append(issue)
    
    # Check module references
    all_issues.extend(check_module_references())
    
    # Check version headers
    all_issues.extend(check_version_headers())
    
    # Check file locations
    all_issues.extend(check_file_locations())
    
    if all_issues:
        print(f"❌ Found {len(all_issues)} issues:\n")
        for issue in all_issues:
            print(f"  • {issue}")
        sys.exit(1)
    else:
        print("✅ All validation checks passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()