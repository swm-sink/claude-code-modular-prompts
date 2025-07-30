#!/usr/bin/env python3
"""
Comprehensive YAML Frontmatter Compliance Validator
Validates all command files for proper Claude Code YAML structure
"""

import os
import yaml
import glob
from pathlib import Path

def validate_yaml_frontmatter(file_path):
    """Validate YAML frontmatter in a markdown file"""
    issues = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file starts with YAML frontmatter
        if not content.startswith('---'):
            issues.append("Missing YAML frontmatter (must start with '---')")
            return issues
        
        # Extract YAML frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            issues.append("Invalid YAML frontmatter structure")
            return issues
        
        yaml_content = parts[1]
        
        # Parse YAML
        try:
            yaml_data = yaml.safe_load(yaml_content)
        except yaml.YAMLError as e:
            issues.append(f"Invalid YAML syntax: {e}")
            return issues
        
        if not isinstance(yaml_data, dict):
            issues.append("YAML frontmatter must be a dictionary")
            return issues
        
        # Check required fields
        required_fields = ['name', 'description']
        for field in required_fields:
            if field not in yaml_data:
                issues.append(f"Missing required field: '{field}'")
        
        # Check recommended fields
        recommended_fields = ['usage', 'allowed-tools', 'category']
        for field in recommended_fields:
            if field not in yaml_data:
                issues.append(f"Missing recommended field: '{field}' (warning)")
        
        # Check deprecated fields
        deprecated_fields = ['tools']
        for field in deprecated_fields:
            if field in yaml_data:
                issues.append(f"Deprecated field found: '{field}' (should be 'allowed-tools')")
        
        # Validate field formats
        if 'name' in yaml_data:
            name = yaml_data['name']
            if not isinstance(name, str):
                issues.append("Field 'name' must be a string")
            elif not name.startswith('/'):
                issues.append("Field 'name' should start with '/' (e.g., '/task')")
        
        if 'allowed-tools' in yaml_data:
            tools = yaml_data['allowed-tools']
            if not isinstance(tools, list):
                issues.append("Field 'allowed-tools' must be a list")
            else:
                valid_tools = [
                    'Read', 'Write', 'Edit', 'MultiEdit', 'Bash', 'Glob', 'Grep', 
                    'LS', 'Task', 'WebFetch', 'WebSearch', 'NotebookRead', 'NotebookEdit',
                    'TodoWrite', 'ExitPlanMode'
                ]
                for tool in tools:
                    if tool not in valid_tools:
                        issues.append(f"Unknown tool in allowed-tools: '{tool}'")
        
    except Exception as e:
        issues.append(f"Error reading file: {e}")
    
    return issues

def main():
    """Main validation function"""
    print("🔍 YAML Frontmatter Compliance Validator")
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
    
    print(f"📊 Found {len(command_files)} command files to validate")
    print()
    
    # Validation results
    total_files = len(command_files)
    files_with_issues = 0
    total_issues = 0
    critical_issues = 0
    warnings = 0
    
    # Validate each file
    for file_path in sorted(command_files):
        rel_path = os.path.relpath(file_path)
        issues = validate_yaml_frontmatter(file_path)
        
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            
            print(f"❌ {rel_path}")
            for issue in issues:
                if "warning" in issue.lower():
                    warnings += 1
                    print(f"   ⚠️  {issue}")
                else:
                    critical_issues += 1
                    print(f"   🚨 {issue}")
            print()
        else:
            print(f"✅ {rel_path}")
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 VALIDATION SUMMARY")
    print("=" * 50)
    print(f"Total Files: {total_files}")
    print(f"Files with Issues: {files_with_issues}")
    print(f"Files Passing: {total_files - files_with_issues}")
    print(f"Total Issues: {total_issues}")
    print(f"Critical Issues: {critical_issues}")
    print(f"Warnings: {warnings}")
    
    # Calculate compliance percentage
    compliance_rate = ((total_files - files_with_issues) / total_files) * 100
    print(f"\n📊 Compliance Rate: {compliance_rate:.1f}%")
    
    if compliance_rate == 100:
        print("🎉 PERFECT COMPLIANCE - All files pass validation!")
    elif compliance_rate >= 90:
        print("✅ EXCELLENT COMPLIANCE - Minor issues to address")
    elif compliance_rate >= 70:
        print("⚠️  GOOD COMPLIANCE - Some issues need attention")
    else:
        print("🚨 POOR COMPLIANCE - Major issues require immediate attention")
    
    return compliance_rate >= 90

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)