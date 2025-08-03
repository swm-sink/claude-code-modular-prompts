#!/usr/bin/env python3
"""
Test Claude Code compatibility for all command files (Fixed Version)
"""
import os
import re
import yaml

def test_command_compatibility(file_path):
    """Test Claude Code compatibility for a command file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        compatibility_issues = []
        
        # 1. YAML Frontmatter Structure Test
        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not yaml_match:
            compatibility_issues.append("Missing YAML frontmatter")
            return False, compatibility_issues
        
        yaml_content = yaml_match.group(1)
        
        # 2. YAML Parsing Test
        try:
            parsed_yaml = yaml.safe_load(yaml_content)
        except yaml.YAMLError as e:
            compatibility_issues.append(f"YAML parsing error: {e}")
            return False, compatibility_issues
        
        # 3. Required Fields Test
        required_fields = ['name', 'description', 'allowed-tools']
        for field in required_fields:
            if field not in parsed_yaml:
                compatibility_issues.append(f"Missing required field: {field}")
        
        # 4. Command Name Format Test
        if 'name' in parsed_yaml:
            name = parsed_yaml['name']
            if not name.startswith('/'):
                compatibility_issues.append("Command name must start with '/'")
            if ' ' in name:
                compatibility_issues.append("Command name cannot contain spaces")
            if not re.match(r'^/[a-zA-Z0-9\-_]+$', name):
                compatibility_issues.append("Command name contains invalid characters")
        
        # 5. Tools Field Test (Claude Code Compatibility)
        if 'allowed-tools' in parsed_yaml:
            tools_str = parsed_yaml['allowed-tools']
            if isinstance(tools_str, str):
                tools = [tool.strip() for tool in tools_str.split(',')]
                # Valid Claude Code tools
                valid_tools = {
                    'Read', 'Write', 'Edit', 'MultiEdit', 'Bash', 'Grep', 'Glob', 'LS',
                    'Task', 'TodoWrite', 'WebSearch', 'WebFetch', 'NotebookRead', 'NotebookEdit'
                }
                invalid_tools = [tool for tool in tools if tool not in valid_tools]
                if invalid_tools:
                    compatibility_issues.append(f"Invalid tools: {invalid_tools}")
            else:
                compatibility_issues.append("allowed-tools must be a string")
        
        # 6. Description Test
        if 'description' in parsed_yaml:
            desc = parsed_yaml['description']
            if not isinstance(desc, str) or not desc.strip():
                compatibility_issues.append("Description must be a non-empty string")
        
        # 7. Usage Field Test (if present)
        if 'usage' in parsed_yaml:
            usage = parsed_yaml['usage']
            if not isinstance(usage, str):
                compatibility_issues.append("Usage must be a string")
        
        # 8. Markdown Content Test
        markdown_content = content[yaml_match.end():]
        if not markdown_content.strip():
            compatibility_issues.append("Command has no content after YAML frontmatter")
        
        # 9. Test for old format issues in YAML ONLY (not in content)
        yaml_lines = yaml_content.split('\n')
        for line in yaml_lines:
            if line.strip().startswith('tools:'):
                compatibility_issues.append("Found old 'tools:' field in YAML - should be 'allowed-tools:'")
                break
        
        # 10. Character encoding test
        try:
            content.encode('utf-8')
        except UnicodeEncodeError:
            compatibility_issues.append("File contains non-UTF-8 characters")
        
        if compatibility_issues:
            return False, compatibility_issues
        
        return True, []
        
    except Exception as e:
        return False, [f"Error reading file: {e}"]

def main():
    """Test Claude Code compatibility for all commands"""
    commands_dir = '.claude/commands'
    total_files = 0
    compatible_files = 0
    issues = []
    
    print("🧪 Claude Code Compatibility Testing (Fixed)")
    print("=" * 50)
    
    for root, dirs, files in os.walk(commands_dir):
        for filename in files:
            if filename.endswith('.md'):
                total_files += 1
                file_path = os.path.join(root, filename)
                is_compatible, file_issues = test_command_compatibility(file_path)
                
                if is_compatible:
                    compatible_files += 1
                    print(f"✅ {file_path}")
                else:
                    issues.append((file_path, file_issues))
                    print(f"❌ {file_path}")
                    for issue in file_issues:
                        print(f"   • {issue}")
    
    print("\n" + "=" * 50)
    print(f"📊 COMPATIBILITY TEST SUMMARY")
    print(f"Total commands tested: {total_files}")
    print(f"Compatible commands: {compatible_files}")
    print(f"Commands with issues: {len(issues)}")
    print(f"Compatibility rate: {(compatible_files/total_files*100):.1f}%")
    
    if issues:
        print(f"\n❌ COMPATIBILITY ISSUES FOUND ({len(issues)} files):")
        for file_path, file_issues in issues:
            print(f"\n{file_path}:")
            for issue in file_issues:
                print(f"   • {issue}")
        return False
    else:
        print(f"\n🎉 ALL {total_files} COMMANDS ARE CLAUDE CODE COMPATIBLE!")
        return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)