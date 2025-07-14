#!/usr/bin/env python3
"""
Fix common XML validation errors in documentation.
Part of Agent V24: Example Validator.
"""

import json
import os
import re
from typing import List, Tuple, Dict

def fix_unclosed_xml_tags(content: str) -> Tuple[str, List[str]]:
    """Fix unclosed XML tags in content."""
    fixes = []
    lines = content.split('\n')
    in_code_block = False
    code_block_start = -1
    code_block_language = None
    
    for i, line in enumerate(lines):
        # Track code blocks
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_block_start = i
                # Extract language
                match = re.match(r'^```(\w*)', line)
                code_block_language = match.group(1) if match else None
            else:
                # Ending code block
                if code_block_language == 'xml' and code_block_start >= 0:
                    # Process XML block
                    block_content = '\n'.join(lines[code_block_start+1:i])
                    fixed_block, block_fixes = fix_xml_block(block_content)
                    
                    if block_fixes:
                        # Replace the block content
                        lines[code_block_start+1:i] = fixed_block.split('\n')
                        fixes.extend([f"Line {code_block_start+1}: {fix}" for fix in block_fixes])
                
                in_code_block = False
                code_block_start = -1
                code_block_language = None
    
    return '\n'.join(lines), fixes

def fix_xml_block(xml_content: str) -> Tuple[str, List[str]]:
    """Fix XML content by adding missing closing tags."""
    fixes = []
    
    # Find all tags
    tag_pattern = r'<([^/\s>]+)(?:\s[^>]*)?>|</([^>]+)>'
    stack = []
    tag_positions = []
    
    for match in re.finditer(tag_pattern, xml_content):
        opening_tag = match.group(1)
        closing_tag = match.group(2)
        
        if opening_tag:
            # Skip self-closing tags and special tags
            if match.group(0).endswith('/>') or opening_tag.startswith('!'):
                continue
            stack.append((opening_tag, match.end()))
            tag_positions.append((opening_tag, match.start(), match.end(), 'open'))
        elif closing_tag:
            if stack and stack[-1][0] == closing_tag:
                stack.pop()
            else:
                # Mismatched closing tag
                fixes.append(f"Removed mismatched closing tag: </{closing_tag}>")
                tag_positions.append((closing_tag, match.start(), match.end(), 'remove'))
    
    # Add missing closing tags
    if stack:
        # Add closing tags at the end
        lines = xml_content.split('\n')
        last_line_with_content = len(lines) - 1
        
        # Find the last line with actual content
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip():
                last_line_with_content = i
                break
        
        # Add closing tags in reverse order
        for tag, _ in reversed(stack):
            fixes.append(f"Added missing closing tag: </{tag}>")
            # Check if we need to add before the last ```
            if last_line_with_content < len(lines) - 1:
                lines.insert(last_line_with_content + 1, f"</{tag}>")
            else:
                lines.append(f"</{tag}>")
        
        xml_content = '\n'.join(lines)
    
    return xml_content, fixes

def fix_python_examples(content: str) -> Tuple[str, List[str]]:
    """Fix common Python syntax errors in examples."""
    fixes = []
    lines = content.split('\n')
    in_code_block = False
    code_block_start = -1
    code_block_language = None
    
    for i, line in enumerate(lines):
        # Track code blocks
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_block_start = i
                # Extract language
                match = re.match(r'^```(\w*)', line)
                code_block_language = match.group(1) if match else None
            else:
                # Ending code block
                if code_block_language == 'python' and code_block_start >= 0:
                    # Process Python block
                    block_lines = lines[code_block_start+1:i]
                    fixed_lines, block_fixes = fix_python_block(block_lines)
                    
                    if block_fixes:
                        lines[code_block_start+1:i] = fixed_lines
                        fixes.extend([f"Line {code_block_start+1+j}: {fix}" for j, fix in block_fixes])
                
                in_code_block = False
                code_block_start = -1
                code_block_language = None
    
    return '\n'.join(lines), fixes

def fix_python_block(block_lines: List[str]) -> Tuple[List[str], List[Tuple[int, str]]]:
    """Fix common Python syntax issues in a code block."""
    fixes = []
    fixed_lines = block_lines.copy()
    
    # Common fixes
    for i, line in enumerate(fixed_lines):
        # Fix missing colons
        if re.match(r'^\s*(if|elif|else|for|while|def|class|try|except|finally|with)\s+.*[^:]$', line):
            fixed_lines[i] = line + ':'
            fixes.append((i, "Added missing colon"))
        
        # Fix print statements (Python 2 to 3)
        if re.match(r'^\s*print\s+["\']', line) and 'print(' not in line:
            fixed_lines[i] = re.sub(r'print\s+(.+)$', r'print(\1)', line)
            fixes.append((i, "Fixed print statement for Python 3"))
    
    return fixed_lines, fixes

def fix_bash_examples(content: str) -> Tuple[str, List[str]]:
    """Fix common bash path errors in examples."""
    fixes = []
    lines = content.split('\n')
    in_code_block = False
    code_block_start = -1
    code_block_language = None
    
    for i, line in enumerate(lines):
        # Track code blocks
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_block_start = i
                # Extract language
                match = re.match(r'^```(\w*)', line)
                code_block_language = match.group(1) if match else None
            else:
                # Ending code block
                if code_block_language == 'bash' and code_block_start >= 0:
                    # Process bash block
                    block_lines = lines[code_block_start+1:i]
                    fixed_lines, block_fixes = fix_bash_block(block_lines)
                    
                    if block_fixes:
                        lines[code_block_start+1:i] = fixed_lines
                        fixes.extend([f"Line {code_block_start+1}: {fix}" for fix in block_fixes])
                
                in_code_block = False
                code_block_start = -1
                code_block_language = None
    
    return '\n'.join(lines), fixes

def fix_bash_block(block_lines: List[str]) -> Tuple[List[str], List[str]]:
    """Fix common bash path issues in a code block."""
    fixes = []
    fixed_lines = []
    
    for line in block_lines:
        fixed_line = line
        
        # Fix module paths missing .claude prefix
        if 'modules/' in line and '.claude/modules/' not in line:
            fixed_line = re.sub(r'\bmodules/', '.claude/modules/', fixed_line)
            fixes.append(f"Fixed module path: added .claude/ prefix")
        
        # Fix deprecated claude validate command
        if 'claude validate' in line and 'init-validate' not in line:
            fixed_line = fixed_line.replace('claude validate', 'claude init-validate')
            fixes.append(f"Updated deprecated 'claude validate' to 'claude init-validate'")
        
        fixed_lines.append(fixed_line)
    
    return fixed_lines, fixes

def main():
    """Main function to fix code examples."""
    # Load validation results
    if not os.path.exists('code_examples_validation_results.json'):
        print("Error: code_examples_validation_results.json not found. Run validate_code_examples.py first.")
        return 1
    
    with open('code_examples_validation_results.json', 'r') as f:
        results = json.load(f)
    
    # Group errors by file
    errors_by_file = {}
    for detail in results['details']:
        if detail.get('status') == 'failed':
            file_path = detail['file']
            if file_path not in errors_by_file:
                errors_by_file[file_path] = []
            errors_by_file[file_path].append(detail)
    
    total_fixes = 0
    files_fixed = []
    
    # Process each file with errors
    for file_path, errors in errors_by_file.items():
        print(f"\nProcessing {file_path}...")
        
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        all_fixes = []
        
        # Apply fixes based on error types
        has_xml_errors = any(e['language'] == 'xml' for e in errors)
        has_python_errors = any(e['language'] == 'python' for e in errors)
        has_bash_errors = any(e['language'] == 'bash' for e in errors)
        
        if has_xml_errors:
            content, fixes = fix_unclosed_xml_tags(content)
            all_fixes.extend(fixes)
        
        if has_python_errors:
            content, fixes = fix_python_examples(content)
            all_fixes.extend(fixes)
        
        if has_bash_errors:
            content, fixes = fix_bash_examples(content)
            all_fixes.extend(fixes)
        
        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            files_fixed.append(file_path)
            total_fixes += len(all_fixes)
            
            print(f"  Fixed {len(all_fixes)} issues:")
            for fix in all_fixes:
                print(f"    - {fix}")
    
    print("\n" + "="*60)
    print("FIX SUMMARY")
    print("="*60)
    print(f"Files processed: {len(errors_by_file)}")
    print(f"Files fixed: {len(files_fixed)}")
    print(f"Total fixes applied: {total_fixes}")
    
    if files_fixed:
        print("\nFiles modified:")
        for file_path in sorted(files_fixed):
            print(f"  - {file_path}")
    
    return 0

if __name__ == "__main__":
    exit(main())