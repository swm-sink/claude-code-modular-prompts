#!/usr/bin/env python3
"""
XML Structure Fix Script for Claude Framework
Automatically fixes common XML issues in framework files
"""

import re
from pathlib import Path

def fix_gate_tags(content: str) -> str:
    """Fix unclosed gate tags by converting them to self-closing tags"""
    # Pattern to match gate tags that should be self-closing
    gate_pattern = r'<gate\s+([^>]*?)\/?\s*>'
    
    # Find all gate tags and make them self-closing
    def replace_gate(match):
        attributes = match.group(1)
        return f'<gate {attributes}/>'
    
    return re.sub(gate_pattern, replace_gate, content)

def fix_enforcement_values(content: str) -> str:
    """Fix invalid enforcement values"""
    # Replace invalid enforcement values
    content = content.replace('enforcement="blocking"', 'enforcement="mandatory"')
    return content

def fix_xml_file(file_path: Path) -> bool:
    """Fix XML issues in a single file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        # Apply fixes
        content = fix_gate_tags(content)
        content = fix_enforcement_values(content)
        
        # Only write if changes were made
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            print(f"Fixed: {file_path.relative_to(file_path.parents[1])}")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    framework_root = Path("/Users/smenssink/Documents/Github personal projects/claude-code-modular-agents/.claude")
    
    # Find all markdown files
    md_files = list(framework_root.rglob("*.md"))
    
    files_fixed = 0
    
    for file_path in md_files:
        if fix_xml_file(file_path):
            files_fixed += 1
    
    print(f"\nFixed {files_fixed} files")

if __name__ == "__main__":
    main()