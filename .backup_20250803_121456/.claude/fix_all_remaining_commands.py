#!/usr/bin/env python3
"""
Script to fix tools: -> allowed-tools: in all remaining command directories
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
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def fix_directory(directory_path):
    """Fix all markdown files in a directory"""
    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} not found")
        return 0
    
    fixed_count = 0
    files_processed = []
    
    # Handle nested directories
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                if fix_tools_field(file_path):
                    fixed_count += 1
                    files_processed.append(file_path)
    
    return fixed_count, files_processed

def main():
    """Fix all remaining command directories"""
    base_dir = '.claude/commands'
    
    # Directories to fix (excluding core and quality which are already done)
    directories_to_fix = [
        'specialized',
        'development', 
        'devops',
        'testing',
        'database',
        'data-science',
        'security',
        'monitoring',
        'web-dev',
        'meta'
    ]
    
    total_fixed = 0
    all_fixed_files = []
    
    for directory in directories_to_fix:
        dir_path = os.path.join(base_dir, directory)
        fixed_count, fixed_files = fix_directory(dir_path)
        if fixed_count > 0:
            print(f"\n{directory.upper()} commands:")
            for file_path in fixed_files:
                print(f"  Fixed: {file_path}")
            print(f"  Total fixed: {fixed_count}")
        else:
            print(f"\n{directory.upper()}: No files needed fixing")
        
        total_fixed += fixed_count
        all_fixed_files.extend(fixed_files)
    
    # Also check for files directly in commands directory
    commands_dir = base_dir
    for filename in os.listdir(commands_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(commands_dir, filename)
            if fix_tools_field(file_path):
                total_fixed += 1
                all_fixed_files.append(file_path)
                print(f"Fixed root command: {file_path}")
    
    print(f"\n=== SUMMARY ===")
    print(f"Total files fixed: {total_fixed}")
    print(f"All directories processed: {', '.join(directories_to_fix)}")

if __name__ == "__main__":
    main()