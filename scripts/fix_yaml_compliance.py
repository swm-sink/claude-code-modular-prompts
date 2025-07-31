#!/usr/bin/env python3
"""
YAML Frontmatter Compliance Fixer
Fixes YAML formatting issues in all command files
"""

import os
import re
import glob
import yaml
from pathlib import Path

def fix_yaml_frontmatter(file_path):
    """Fix YAML frontmatter formatting in a markdown file"""
    changes_made = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return changes_made
        
        # Split into YAML and content parts
        parts = content.split('---', 2)
        if len(parts) < 3:
            return changes_made
        
        yaml_content = parts[1]
        markdown_content = parts[2]
        
        # Parse existing YAML
        try:
            yaml_data = yaml.safe_load(yaml_content)
        except yaml.YAMLError:
            return changes_made
        
        if not isinstance(yaml_data, dict):
            return changes_made
        
        modified = False
        
        # Fix allowed-tools format (string to list)
        if 'allowed-tools' in yaml_data:
            tools = yaml_data['allowed-tools']
            if isinstance(tools, str):
                # Parse string format like "Read, Write, Edit" to list
                if ',' in tools:
                    tool_list = [tool.strip() for tool in tools.split(',')]
                else:
                    # Handle space-separated format
                    tool_list = tools.split()
                
                yaml_data['allowed-tools'] = tool_list
                changes_made.append(f"Converted allowed-tools from string to list: {tool_list}")
                modified = True
        
        # Add missing category if possible to infer from path
        if 'category' not in yaml_data:
            # Try to infer category from file path
            path_parts = Path(file_path).parts
            if 'commands' in path_parts:
                commands_idx = path_parts.index('commands')
                if commands_idx + 1 < len(path_parts):
                    category = path_parts[commands_idx + 1]
                    if category not in ['examples']:  # Skip generic directories
                        yaml_data['category'] = category
                        changes_made.append(f"Added inferred category: {category}")
                        modified = True
        
        # Ensure name starts with /
        if 'name' in yaml_data:
            name = yaml_data['name']
            if isinstance(name, str) and not name.startswith('/'):
                yaml_data['name'] = '/' + name
                changes_made.append(f"Added '/' prefix to name: {yaml_data['name']}")
                modified = True
        
        # Write back if modified
        if modified:
            # Generate clean YAML
            new_yaml = yaml.dump(yaml_data, default_flow_style=False, sort_keys=False)
            new_content = f"---\n{new_yaml}---{markdown_content}"
            
            # Backup original
            backup_path = file_path + '.backup'
            if not os.path.exists(backup_path):
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            # Write fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        
    except Exception as e:
        changes_made.append(f"ERROR: {e}")
    
    return changes_made

def main():
    """Main fixing function"""
    print("🔧 YAML Frontmatter Compliance Fixer")
    print("=" * 50)
    
    # Find all command files
    commands_dir = ".claude/commands"
    if not os.path.exists(commands_dir):
        print(f"❌ Commands directory not found: {commands_dir}")
        return
    
    pattern = os.path.join(commands_dir, "**/*.md")
    command_files = glob.glob(pattern, recursive=True)
    
    if not command_files:
        print(f"⚠️  No command files found in {commands_dir}")
        return
    
    print(f"📊 Found {len(command_files)} command files to fix")
    print()
    
    # Fix each file
    total_fixes = 0
    files_fixed = 0
    
    for file_path in sorted(command_files):
        rel_path = os.path.relpath(file_path)
        changes = fix_yaml_frontmatter(file_path)
        
        if changes:
            files_fixed += 1
            total_fixes += len(changes)
            print(f"🔧 {rel_path}")
            for change in changes:
                if change.startswith("ERROR"):
                    print(f"   ❌ {change}")
                else:
                    print(f"   ✅ {change}")
        else:
            print(f"✨ {rel_path} (no changes needed)")
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 FIXING SUMMARY")
    print("=" * 50)
    print(f"Total Files: {len(command_files)}")
    print(f"Files Fixed: {files_fixed}")
    print(f"Total Changes: {total_fixes}")
    print(f"\n💾 Backup files created with .backup extension")
    print(f"🚀 Run 'python3 validate-yaml-compliance.py' to verify fixes")

if __name__ == "__main__":
    main()