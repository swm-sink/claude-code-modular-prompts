#!/usr/bin/env python3
"""
Script to standardize YAML fields to Claude Code specification
"""
import os
import re

def standardize_yaml_fields(file_path):
    """Standardize YAML frontmatter fields in a markdown file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Extract YAML frontmatter and content
        yaml_match = re.match(r'^(---\n)(.*?)\n(---)(.*)', content, re.DOTALL)
        if not yaml_match:
            return False, "No YAML frontmatter found"
        
        yaml_start = yaml_match.group(1)
        yaml_content = yaml_match.group(2)
        yaml_end = yaml_match.group(3)
        markdown_content = yaml_match.group(4)
        
        # Parse YAML lines and keep only standard fields
        yaml_lines = yaml_content.strip().split('\n')
        
        # Standard Claude Code fields in preferred order
        standard_fields = ['name', 'description', 'usage', 'category', 'allowed-tools', 'security']
        
        # Dictionary to store field values
        field_values = {}
        
        for line in yaml_lines:
            if ':' in line and not line.strip().startswith('-'):
                field, value = line.split(':', 1)
                field = field.strip()
                value = value.strip()
                
                if field in standard_fields:
                    field_values[field] = value
        
        # Rebuild YAML in standard order
        new_yaml_lines = []
        for field in standard_fields:
            if field in field_values:
                new_yaml_lines.append(f"{field}: {field_values[field]}")
        
        # Reconstruct the file content
        new_yaml_content = '\n'.join(new_yaml_lines)
        new_content = f"{yaml_start}{new_yaml_content}\n{yaml_end}{markdown_content}"
        
        # Only write if content changed
        if content != new_content:
            with open(file_path, 'w') as f:
                f.write(new_content)
            return True, "Standardized"
        else:
            return False, "Already standard"
            
    except Exception as e:
        return False, f"Error: {e}"

def main():
    """Standardize all command files"""
    commands_dir = '.claude/commands'
    standardized_count = 0
    files_processed = []
    
    for root, dirs, files in os.walk(commands_dir):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                changed, message = standardize_yaml_fields(file_path)
                
                if changed:
                    standardized_count += 1
                    files_processed.append(file_path)
                    print(f"Standardized: {file_path}")
                elif "Error" in message:
                    print(f"Error in {file_path}: {message}")
    
    print(f"\n=== SUMMARY ===")
    print(f"Files standardized: {standardized_count}")
    
    if files_processed:
        print("\nFiles that were standardized:")
        for file_path in files_processed:
            print(f"  {file_path}")

if __name__ == "__main__":
    main()