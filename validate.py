#!/usr/bin/env python3
"""Framework validation tool - detects and reports common issues.
Version 2.0.0 - Updated for Framework 3.0 format validation."""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

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

def check_version_table():
    """Check for proper version table format in modules and commands."""
    issues = []
    
    # Check both modules and commands
    for directory in ['.claude/modules', '.claude/commands']:
        for file_path in Path(directory).rglob('*.md'):
            with open(file_path, 'r') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Check if version table exists at the beginning
            if len(lines) < 3:
                issues.append(f"Missing version table in {file_path}")
                continue
            
            # Also check if it's not a version table at all
            if not lines[0].strip().startswith('|'):
                issues.append(f"Missing version table in {file_path}")
                continue
            
            # Check table format
            if not (lines[0].startswith('| version') and 
                    lines[1].startswith('|---') and 
                    lines[2].startswith('|')):
                # Check for other malformed tables
                if lines[0].startswith('|') and not lines[0].startswith('| version'):
                    issues.append(f"Invalid version table format in {file_path}")
                else:
                    issues.append(f"Invalid version table format in {file_path}")
                continue
            
            # Also check if separator line is malformed
            if '|' in lines[1] and lines[1].count('|') < 3:
                issues.append(f"Invalid version table format in {file_path} - malformed separator line")
                continue
            
            # Check version table content
            try:
                version_line = lines[2]
                parts = [p.strip() for p in version_line.split('|')]
                if len(parts) < 4:  # Empty | version | date | status | empty
                    issues.append(f"Incomplete version table in {file_path}")
                    continue
                
                # Validate version format (e.g., 1.0.0)
                version = parts[1]
                if not re.match(r'^\d+\.\d+\.\d+$', version):
                    issues.append(f"Invalid version format '{version}' in {file_path} (expected X.Y.Z)")
                
                # Validate date format (YYYY-MM-DD) and enforce July 2025
                date = parts[2]
                try:
                    parsed_date = datetime.strptime(date, '%Y-%m-%d')
                    # Enforce July 2025 temporal standards
                    if not (parsed_date.year == 2025 and parsed_date.month == 7):
                        issues.append(f"Non-compliant timestamp '{date}' in {file_path} (must be July 2025: 2025-07-XX)")
                except ValueError:
                    issues.append(f"Invalid date format '{date}' in {file_path} (expected YYYY-MM-DD)")
                
                # Validate status
                status = parts[3]
                valid_statuses = ['stable', 'beta', 'experimental', 'deprecated', 'minimal']
                if status not in valid_statuses:
                    issues.append(f"Invalid status '{status}' in {file_path} (expected one of: {', '.join(valid_statuses)})")
                    
            except Exception as e:
                issues.append(f"Error parsing version table in {file_path}: {str(e)}")
    
    return issues

def check_horizontal_separators():
    """Check for proper horizontal separator lines (80 chars)."""
    issues = []
    separator = '─' * 80
    
    for directory in ['.claude/modules', '.claude/commands']:
        for file_path in Path(directory).rglob('*.md'):
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Check if separator exists after header
            lines = content.split('\n')
            
            # Find the main header (should be after version table)
            header_found = False
            separator_found = False
            
            for i, line in enumerate(lines):
                if line.startswith('# ') and i > 3:  # After version table
                    header_found = True
                    # Check if next non-empty line is separator
                    for j in range(i+1, min(i+3, len(lines))):
                        if lines[j].strip():
                            if lines[j] == separator:
                                separator_found = True
                            break
                    break
            
            if header_found and not separator_found:
                issues.append(f"Missing horizontal separator after header in {file_path}")
    
    return issues

def check_xml_blocks():
    """Check that XML blocks are properly wrapped in ```xml."""
    issues = []
    
    for directory in ['.claude/modules', '.claude/commands']:
        for file_path in Path(directory).rglob('*.md'):
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Check for XML content
            if '<module' in content or '<command' in content or '<delegation' in content:
                # Check if wrapped in ```xml
                if '```xml' not in content:
                    issues.append(f"XML content not wrapped in ```xml blocks in {file_path}")
                else:
                    # More accurate check for matching blocks
                    lines = content.split('\n')
                    xml_block_count = 0
                    closing_block_count = 0
                    
                    for i, line in enumerate(lines):
                        if line.strip() == '```xml':
                            xml_block_count += 1
                        elif line.strip() == '```':
                            # Check if this is a closing block (follows content, not language specifier)
                            if i > 0 and not lines[i-1].strip().startswith('```'):
                                closing_block_count += 1
                    
                    if xml_block_count > closing_block_count:
                        issues.append(f"Unclosed ```xml block in {file_path} (found {xml_block_count} opening, {closing_block_count} closing)")
    
    return issues

def check_file_locations():
    """Check for files in wrong locations."""
    issues = []
    
    # Check for non-md files in .claude
    allowed_files = ['.DS_Store', 'settings.local.json']
    for file in Path('.claude').rglob('*'):
        if file.is_file() and not file.suffix == '.md' and file.name not in allowed_files:
            issues.append(f"Non-markdown file in .claude: {file}")
    
    # Check for orphaned test files
    if Path('tests').exists():
        for test_file in Path('tests').rglob('test_*.py'):
            module_name = test_file.stem.replace('test_', '')
            # Check if it's testing a script in the root directory
            if module_name == 'validate' and Path('validate.py').exists():
                continue
            # Check if it's testing a framework module
            if not Path(f'src/framework/{module_name}.py').exists():
                # Not an error if the test is for framework functionality
                if 'framework' not in str(test_file):
                    issues.append(f"Orphaned test file: {test_file}")
    
    return issues

def check_format_consistency():
    """Check overall format consistency across files."""
    issues = []
    
    # Check that all module/command files follow the same structure
    for directory in ['.claude/modules', '.claude/commands']:
        if not Path(directory).exists():
            continue
        for file_path in Path(directory).rglob('*.md'):
            with open(file_path, 'r') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Basic structure checks
            if len(lines) < 6:  # Minimum: version table (3 lines) + empty + header + separator
                issues.append(f"File too short, likely incomplete: {file_path}")
                continue
            
            # Check for empty line after version table (but only if we have a valid table)
            if len(lines) > 3 and lines[0].startswith('| version'):
                if lines[3].strip() != '':
                    issues.append(f"Missing empty line after version table in {file_path}")
            
            # Check for empty line after separator
            separator = '─' * 80
            for i, line in enumerate(lines):
                if line == separator and i+1 < len(lines):
                    if lines[i+1].strip() != '':
                        issues.append(f"Missing empty line after separator in {file_path} at line {i+1}")
    
    return issues

def check_file_limits():
    """Check framework file limits per CLAUDE.md rules."""
    issues = []
    
    # Read limits from CLAUDE.md
    limits = {}
    try:
        with open('CLAUDE.md', 'r') as f:
            content = f.read()
        # Parse limits line: <limits patterns="6" quality="4" ... />
        limits_match = re.search(r'<limits\s+([^>]+)/>', content)
        if limits_match:
            limits_str = limits_match.group(1)
            for match in re.finditer(r'(\w+)="(\d+)"', limits_str):
                limits[match.group(1)] = int(match.group(2))
    except:
        # Fallback to default limit of 3 if CLAUDE.md not readable
        pass
    
    # Count modules per category using actual limits
    modules_dir = Path('.claude/modules')
    if modules_dir.exists():
        for category_dir in modules_dir.iterdir():
            if category_dir.is_dir() and category_dir.name not in ['.DS_Store']:
                module_count = len(list(category_dir.glob('*.md')))
                limit = limits.get(category_dir.name, 3)  # Default to 3 if not specified
                if module_count > limit:
                    issues.append(f"Module limit exceeded in {category_dir.name}: {module_count}/{limit} modules")
    
    # Count reports (limit: 5)
    report_count = len(list(Path('.').glob('*REPORT*.md')))
    if report_count > 5:
        issues.append(f"Report limit exceeded: {report_count}/5 reports")
    
    # Count docs per directory (limit: 20)
    docs_dir = Path('docs')
    if docs_dir.exists():
        for subdir in docs_dir.iterdir():
            if subdir.is_dir():
                doc_count = len(list(subdir.glob('*.md')))
                if doc_count > 20:
                    issues.append(f"Docs limit exceeded in {subdir.name}: {doc_count}/20 files")
    
    return issues

def check_pattern_usage():
    """Check for proper pattern usage declarations."""
    issues = []
    
    if not Path('.claude/modules').exists():
        return issues
        
    for module_file in Path('.claude/modules').rglob('*.md'):
        with open(module_file, 'r') as f:
            content = f.read()
        
        # Check if module uses patterns
        if '<uses_pattern' in content:
            # Extract pattern references
            pattern_refs = re.findall(r'<uses_pattern from="([^"]+)">(\w+)</uses_pattern>', content)
            
            for pattern_file, pattern_name in pattern_refs:
                # Verify pattern file exists
                pattern_path = Path('.claude/modules') / pattern_file
                if not pattern_path.exists():
                    issues.append(f"Broken pattern reference in {module_file.name}: {pattern_file}")
                else:
                    # Verify pattern exists in file
                    with open(pattern_path, 'r') as pf:
                        pattern_content = pf.read()
                    if pattern_name not in pattern_content:
                        issues.append(f"Pattern '{pattern_name}' not found in {pattern_file} (referenced by {module_file.name})")
    
    return issues

def check_dependency_declarations():
    """Check for proper dependency declarations."""
    issues = []
    
    if not Path('.claude').exists():
        return issues
        
    for file_path in Path('.claude').rglob('*.md'):
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for depends_on declarations
        if '<depends_on>' in content:
            # Extract dependency references
            dep_refs = re.findall(r'([\w/\-]+\.md)', content[content.find('<depends_on>'):content.find('</depends_on>') if '</depends_on>' in content else len(content)])
            
            for dep_ref in dep_refs:
                # Verify dependency exists
                if dep_ref.startswith('modules/'):
                    dep_path = Path('.claude') / dep_ref
                elif dep_ref.startswith('commands/'):
                    dep_path = Path('.claude') / dep_ref
                elif dep_ref.startswith('docs/'):
                    dep_path = Path(dep_ref)
                else:
                    # Assume it's a module reference
                    dep_path = Path('.claude/modules') / dep_ref
                
                if not dep_path.exists():
                    issues.append(f"Broken dependency in {file_path.name}: {dep_ref}")
    
    return issues

def check_timestamp_compliance():
    """Check for comprehensive timestamp compliance across the entire codebase."""
    issues = []
    
    # Check all markdown files for non-July 2025 timestamps
    for file_path in Path('.').rglob('*.md'):
        # Skip hidden directories and files
        if any(part.startswith('.') for part in file_path.parts[:-1]):
            continue
            
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Look for complete date patterns that are not July 2025
        # Check for years 2010-2024 (complete dates)
        old_year_matches = re.findall(r'20(1[0-9]|2[0-4])-[0-9]{2}-[0-9]{2}', content)
        for match in old_year_matches:
            issues.append(f"Non-compliant timestamp '20{match}' in {file_path}")
        
        # Check for 2025 non-July dates (complete dates only)
        non_july_2025_matches = re.findall(r'2025-(0[1-6]|08|09|1[0-2])-[0-9]{2}', content)
        for match in non_july_2025_matches:
            issues.append(f"Non-compliant timestamp '2025-{match}' in {file_path}")
        
        # Special check for January 2025 dates (most common issue)
        jan_2025_matches = re.findall(r'2025-01-[0-9]{2}', content)
        for match in jan_2025_matches:
            issues.append(f"January 2025 timestamp '{match}' must be updated to July 2025 in {file_path}")
    
    return issues

def main():
    """Run all validation checks."""
    print("🔍 Framework Validation Tool v2.1.0\n")
    print("Validating Framework 3.0 format compliance...\n")
    
    all_issues = []
    check_count = 0
    
    # Check commands
    print("[✓] Checking command delegation...")
    if Path('.claude/commands').exists():
        for cmd_file in Path('.claude/commands').glob('*.md'):
            issue = check_command_delegation(cmd_file)
            if issue:
                all_issues.append(issue)
    check_count += 1
    
    # Check module references
    print("[✓] Checking module references...")
    all_issues.extend(check_module_references())
    check_count += 1
    
    # Check version tables (replaces version headers)
    print("[✓] Checking version tables and format compliance...")
    all_issues.extend(check_version_table())
    check_count += 1
    
    # Check horizontal separators
    print("[✓] Checking visual separators...")
    all_issues.extend(check_horizontal_separators())
    check_count += 1
    
    # Check XML blocks
    print("[✓] Checking XML code blocks...")
    all_issues.extend(check_xml_blocks())
    check_count += 1
    
    # Check file locations
    print("[✓] Checking file locations...")
    all_issues.extend(check_file_locations())
    check_count += 1
    
    # Check file limits
    print("[✓] Checking framework file limits...")
    all_issues.extend(check_file_limits())
    check_count += 1
    
    # Check pattern usage
    print("[✓] Checking pattern usage declarations...")
    all_issues.extend(check_pattern_usage())
    check_count += 1
    
    # Check dependency declarations
    print("[✓] Checking dependency declarations...")
    all_issues.extend(check_dependency_declarations())
    check_count += 1
    
    # Check format consistency
    print("[✓] Checking format consistency...")
    all_issues.extend(check_format_consistency())
    check_count += 1
    
    # Check timestamp compliance (July 2025 enforcement)
    print("[✓] Checking timestamp compliance (July 2025 enforcement)...")
    all_issues.extend(check_timestamp_compliance())
    check_count += 1
    
    print("\n" + "="*60 + "\n")
    print(f"Completed {check_count} validation checks.\n")
    
    if all_issues:
        print(f"❌ Found {len(all_issues)} issues:\n")
        # Group issues by type
        format_issues = [i for i in all_issues if 'format' in i.lower() or 'table' in i.lower() or 'separator' in i.lower()]
        reference_issues = [i for i in all_issues if 'reference' in i.lower() or 'dependency' in i.lower() or 'broken' in i.lower()]
        limit_issues = [i for i in all_issues if 'limit' in i.lower() or 'exceeded' in i.lower()]
        timestamp_issues = [i for i in all_issues if 'timestamp' in i.lower() or 'january' in i.lower() or 'non-compliant' in i.lower()]
        other_issues = [i for i in all_issues if i not in format_issues + reference_issues + limit_issues + timestamp_issues]
        
        if format_issues:
            print("Format Issues:")
            for issue in format_issues:
                print(f"  • {issue}")
            print()
        
        if reference_issues:
            print("Reference/Dependency Issues:")
            for issue in reference_issues:
                print(f"  • {issue}")
            print()
        
        if limit_issues:
            print("Limit Violations:")
            for issue in limit_issues:
                print(f"  • {issue}")
            print()
        
        if timestamp_issues:
            print("Timestamp Compliance Issues:")
            for issue in timestamp_issues:
                print(f"  • {issue}")
            print()
        
        if other_issues:
            print("Other Issues:")
            for issue in other_issues:
                print(f"  • {issue}")
            print()
        
        print("Please fix these issues to ensure framework compliance.")
        sys.exit(1)
    else:
        print("✅ All validation checks passed!")
        print("Framework is compliant with version 3.0 format.")
        sys.exit(0)

if __name__ == "__main__":
    main()