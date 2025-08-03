#!/usr/bin/env python3
"""
Comprehensive YAML frontmatter validation for Claude Code commands
"""
import os
import re
import yaml

def validate_yaml_frontmatter(file_path):
    """Validate YAML frontmatter in a markdown file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not yaml_match:
            return False, "No YAML frontmatter found"
        
        yaml_content = yaml_match.group(1)
        
        # Try to parse YAML
        try:
            parsed_yaml = yaml.safe_load(yaml_content)
            if not isinstance(parsed_yaml, dict):
                return False, f"YAML is not a dictionary: {type(parsed_yaml)}"
        except yaml.YAMLError as e:
            return False, f"YAML parsing error: {e}"
        
        # Check required fields
        required_fields = ['name', 'description', 'allowed-tools']
        missing_fields = [field for field in required_fields if field not in parsed_yaml]
        if missing_fields:
            return False, f"Missing required fields: {missing_fields}"
        
        # Validate field types and formats
        validation_errors = []
        
        # name field should start with /
        if not parsed_yaml['name'].startswith('/'):
            validation_errors.append("name field should start with '/'")
        
        # description should be a non-empty string
        if not isinstance(parsed_yaml['description'], str) or not parsed_yaml['description'].strip():
            validation_errors.append("description should be a non-empty string")
        
        # allowed-tools should be a string with comma-separated tools
        if 'allowed-tools' in parsed_yaml:
            tools = parsed_yaml['allowed-tools']
            if not isinstance(tools, str) or not tools.strip():
                validation_errors.append("allowed-tools should be a non-empty string")
            else:
                # Check for valid tool names
                valid_tools = {'Read', 'Write', 'Edit', 'MultiEdit', 'Bash', 'Grep', 'Glob', 'LS', 'Task', 'TodoWrite', 'WebSearch', 'WebFetch', 'NotebookRead', 'NotebookEdit'}
                tool_list = [tool.strip() for tool in tools.split(',')]
                invalid_tools = [tool for tool in tool_list if tool not in valid_tools]
                if invalid_tools:
                    validation_errors.append(f"Invalid tools found: {invalid_tools}")
        
        # Optional fields validation
        if 'usage' in parsed_yaml:
            if not isinstance(parsed_yaml['usage'], str):
                validation_errors.append("usage should be a string")
        
        if 'category' in parsed_yaml:
            if not isinstance(parsed_yaml['category'], str):
                validation_errors.append("category should be a string")
        
        if validation_errors:
            return False, "; ".join(validation_errors)
        
        return True, "Valid"
        
    except Exception as e:
        return False, f"Error reading file: {e}"

def main():
    """Validate all command files"""
    commands_dir = '.claude/commands'
    total_files = 0
    valid_files = 0
    errors = []
    
    print("🔍 Comprehensive YAML Frontmatter Validation")
    print("=" * 50)
    
    for root, dirs, files in os.walk(commands_dir):
        for filename in files:
            if filename.endswith('.md'):
                total_files += 1
                file_path = os.path.join(root, filename)
                is_valid, message = validate_yaml_frontmatter(file_path)
                
                if is_valid:
                    valid_files += 1
                    print(f"✅ {file_path}")
                else:
                    errors.append((file_path, message))
                    print(f"❌ {file_path}: {message}")
    
    print("\n" + "=" * 50)
    print(f"📊 VALIDATION SUMMARY")
    print(f"Total files processed: {total_files}")
    print(f"Valid files: {valid_files}")
    print(f"Files with errors: {len(errors)}")
    print(f"Success rate: {(valid_files/total_files*100):.1f}%")
    
    if errors:
        print(f"\n❌ ERRORS FOUND ({len(errors)} files):")
        for file_path, error in errors:
            print(f"  {file_path}: {error}")
        return False
    else:
        print(f"\n🎉 ALL {total_files} COMMANDS PASS YAML VALIDATION!")
        return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)