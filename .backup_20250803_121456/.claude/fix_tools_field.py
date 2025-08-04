#!/usr/bin/env python3
"""
Script to fix tools: -> allowed-tools: in command YAML frontmatter
"""
import os
import re

def fix_tools_field(file_path):
    """Fix tools: field to allowed-tools: in a markdown file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Replace tools: with allowed-tools: in YAML frontmatter only
        # Look for the pattern at the start of a line
        updated_content = re.sub(r'^tools:', 'allowed-tools:', content, flags=re.MULTILINE)
        
        if content != updated_content:
            with open(file_path, 'w') as f:
                f.write(updated_content)
            print(f"Fixed: {file_path}")
            return True
        else:
            print(f"No changes needed: {file_path}")
            return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Fix all core commands"""
    core_dir = '.claude/commands/core'
    fixed_count = 0
    
    if not os.path.exists(core_dir):
        print(f"Directory {core_dir} not found")
        return
    
    for filename in os.listdir(core_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(core_dir, filename)
            if fix_tools_field(file_path):
                fixed_count += 1
    
    print(f"\nFixed {fixed_count} files in {core_dir}")

if __name__ == "__main__":
    main()