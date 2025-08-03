#!/usr/bin/env python3
"""
Script to check for non-standard YAML fields in command files
"""
import os
import re

def check_yaml_fields(file_path):
    """Check YAML frontmatter fields in a markdown file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not yaml_match:
            return f"No YAML frontmatter found in {file_path}"
        
        yaml_content = yaml_match.group(1)
        
        # Standard fields we expect
        standard_fields = {
            'name', 'description', 'usage', 'allowed-tools', 
            'category', 'security', 'tools'  # tools shouldn't exist but checking
        }
        
        non_standard = []
        found_fields = set()
        
        for line in yaml_content.strip().split('\n'):
            if ':' in line:
                field = line.split(':')[0].strip()
                found_fields.add(field)
                if field not in standard_fields:
                    non_standard.append(f"{field}: {line.strip()}")
        
        results = {
            'file': file_path,
            'found_fields': found_fields,
            'non_standard': non_standard,
            'has_tools': 'tools' in found_fields,
            'has_allowed_tools': 'allowed-tools' in found_fields,
            'yaml_content': yaml_content
        }
        
        return results
            
    except Exception as e:
        return f"Error processing {file_path}: {e}"

def main():
    """Check all command files for YAML field standardization"""
    commands_dir = '.claude/commands'
    issues_found = []
    
    for root, dirs, files in os.walk(commands_dir):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                result = check_yaml_fields(file_path)
                
                if isinstance(result, dict):
                    # Check for issues
                    if result['non_standard']:
                        issues_found.append(result)
                        print(f"\n{result['file']}:")
                        for issue in result['non_standard']:
                            print(f"  Non-standard field: {issue}")
                    
                    if result['has_tools']:
                        print(f"  WARNING: Still has 'tools' field")
                        
                elif isinstance(result, str):
                    print(f"ERROR: {result}")
    
    if not issues_found:
        print("✅ All YAML fields are standardized!")
    else:
        print(f"\n❌ Found {len(issues_found)} files with non-standard YAML fields")

if __name__ == "__main__":
    main()