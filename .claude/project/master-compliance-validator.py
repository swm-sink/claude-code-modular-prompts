#!/usr/bin/env python3
"""
Master Claude Code Compliance Validation Script

This script performs comprehensive validation of all command files to ensure
ongoing Claude Code compliance. It combines all validation checks into a
single automated test that can be run in CI/CD pipelines.

Usage:
    python3 master-compliance-validator.py [--verbose] [--fix-issues]
    
Exit codes:
    0: All validations passed
    1: Validation failures found
    2: Script error
"""

import os
import re
import yaml
import argparse
import sys
from datetime import datetime
from typing import List, Tuple, Dict, Any

class ComplianceValidator:
    def __init__(self, verbose: bool = False, fix_issues: bool = False):
        self.verbose = verbose
        self.fix_issues = fix_issues
        self.commands_dir = '.claude/commands'
        self.total_files = 0
        self.issues = []
        
    def log(self, message: str, level: str = "INFO"):
        """Log message if verbose mode is enabled"""
        if self.verbose or level == "ERROR":
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] {level}: {message}")
    
    def validate_file_structure(self) -> bool:
        """Validate that only .md files exist in commands directory"""
        self.log("Validating file structure...")
        structure_valid = True
        
        for root, dirs, files in os.walk(self.commands_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                if not filename.endswith('.md'):
                    self.issues.append({
                        'type': 'STRUCTURE',
                        'file': file_path,
                        'issue': f"Non-markdown file in commands directory: {filename}",
                        'severity': 'ERROR'
                    })
                    structure_valid = False
                    
        return structure_valid
    
    def validate_yaml_frontmatter(self, file_path: str) -> Tuple[bool, List[str]]:
        """Validate YAML frontmatter for a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return False, [f"Error reading file: {e}"]
        
        issues = []
        
        # Check for YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not yaml_match:
            return False, ["No YAML frontmatter found"]
        
        yaml_content = yaml_match.group(1)
        
        # Parse YAML
        try:
            parsed_yaml = yaml.safe_load(yaml_content)
            if not isinstance(parsed_yaml, dict):
                return False, [f"YAML is not a dictionary: {type(parsed_yaml)}"]
        except yaml.YAMLError as e:
            return False, [f"YAML parsing error: {e}"]
        
        # Check required fields
        required_fields = ['name', 'description', 'allowed-tools']
        for field in required_fields:
            if field not in parsed_yaml:
                issues.append(f"Missing required field: {field}")
        
        # Validate field formats
        if 'name' in parsed_yaml:
            name = parsed_yaml['name']
            if not name.startswith('/'):
                issues.append("Command name must start with '/'")
            if not re.match(r'^/[a-zA-Z0-9\-_]+$', name):
                issues.append("Command name contains invalid characters")
        
        if 'description' in parsed_yaml:
            if not isinstance(parsed_yaml['description'], str) or not parsed_yaml['description'].strip():
                issues.append("Description must be a non-empty string")
        
        if 'allowed-tools' in parsed_yaml:
            tools_str = parsed_yaml['allowed-tools']
            if isinstance(tools_str, str):
                tools = [tool.strip() for tool in tools_str.split(',')]
                valid_tools = {
                    'Read', 'Write', 'Edit', 'MultiEdit', 'Bash', 'Grep', 'Glob', 'LS',
                    'Task', 'TodoWrite', 'WebSearch', 'WebFetch', 'NotebookRead', 'NotebookEdit'
                }
                invalid_tools = [tool for tool in tools if tool not in valid_tools]
                if invalid_tools:
                    issues.append(f"Invalid tools: {invalid_tools}")
            else:
                issues.append("allowed-tools must be a string")
        
        # Check for old format fields
        yaml_lines = yaml_content.split('\n')
        for line in yaml_lines:
            if line.strip().startswith('tools:'):
                issues.append("Found old 'tools:' field - should be 'allowed-tools:'")
            if line.strip().startswith('argument-hint:'):
                issues.append("Found old 'argument-hint:' field - should be 'usage:'")
        
        # Check for non-standard fields
        standard_fields = {'name', 'description', 'usage', 'category', 'allowed-tools', 'security'}
        for field in parsed_yaml.keys():
            if field not in standard_fields:
                issues.append(f"Non-standard field found: {field}")
        
        return len(issues) == 0, issues
    
    def validate_command_file(self, file_path: str) -> bool:
        """Validate a single command file"""
        self.total_files += 1
        self.log(f"Validating {file_path}...")
        
        file_valid = True
        
        # YAML frontmatter validation
        yaml_valid, yaml_issues = self.validate_yaml_frontmatter(file_path)
        if not yaml_valid:
            file_valid = False
            for issue in yaml_issues:
                self.issues.append({
                    'type': 'YAML',
                    'file': file_path,
                    'issue': issue,
                    'severity': 'ERROR'
                })
        
        # Check file encoding
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                content.encode('utf-8')
        except UnicodeError:
            file_valid = False
            self.issues.append({
                'type': 'ENCODING',
                'file': file_path,
                'issue': "File contains non-UTF-8 characters",
                'severity': 'ERROR'
            })
        
        return file_valid
    
    def check_duplicate_commands(self) -> bool:
        """Check for duplicate command names"""
        self.log("Checking for duplicate command names...")
        command_names = {}
        duplicates_found = False
        
        for root, dirs, files in os.walk(self.commands_dir):
            for filename in files:
                if filename.endswith('.md'):
                    file_path = os.path.join(root, filename)
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read()
                        
                        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                        if yaml_match:
                            yaml_content = yaml_match.group(1)
                            parsed_yaml = yaml.safe_load(yaml_content)
                            
                            if isinstance(parsed_yaml, dict) and 'name' in parsed_yaml:
                                cmd_name = parsed_yaml['name']
                                if cmd_name in command_names:
                                    duplicates_found = True
                                    self.issues.append({
                                        'type': 'DUPLICATE',
                                        'file': file_path,
                                        'issue': f"Duplicate command name '{cmd_name}' (also in {command_names[cmd_name]})",
                                        'severity': 'ERROR'
                                    })
                                else:
                                    command_names[cmd_name] = file_path
                    
                    except Exception as e:
                        self.log(f"Error processing {file_path}: {e}", "ERROR")
        
        return not duplicates_found
    
    def validate_documentation_accuracy(self) -> bool:
        """Validate that documentation reflects actual command count"""
        self.log("Validating documentation accuracy...")
        
        # Count actual command files
        actual_count = 0
        for root, dirs, files in os.walk(self.commands_dir):
            for filename in files:
                if filename.endswith('.md'):
                    actual_count += 1
        
        # Check CLAUDE.md for accurate count references
        try:
            with open('CLAUDE.md', 'r') as f:
                claude_content = f.read()
            
            # Look for command count references
            count_references = re.findall(r'(\d+)\s+(?:command|commands)', claude_content, re.IGNORECASE)
            
            for count in count_references:
                if int(count) != actual_count:
                    self.issues.append({
                        'type': 'DOCUMENTATION',
                        'file': 'CLAUDE.md',
                        'issue': f"Inaccurate command count: {count} (should be {actual_count})",
                        'severity': 'WARNING'
                    })
                    return False
                    
        except FileNotFoundError:
            self.issues.append({
                'type': 'DOCUMENTATION',
                'file': 'CLAUDE.md',
                'issue': "CLAUDE.md file not found",
                'severity': 'ERROR'
            })
            return False
        
        return True
    
    def run_validation(self) -> bool:
        """Run all validation checks"""
        self.log("🔍 Starting Master Compliance Validation")
        self.log("=" * 50)
        
        all_valid = True
        
        # 1. File structure validation
        if not self.validate_file_structure():
            all_valid = False
        
        # 2. Individual file validation
        for root, dirs, files in os.walk(self.commands_dir):
            for filename in files:
                if filename.endswith('.md'):
                    file_path = os.path.join(root, filename)
                    if not self.validate_command_file(file_path):
                        all_valid = False
        
        # 3. Duplicate command check
        if not self.check_duplicate_commands():
            all_valid = False
        
        # 4. Documentation accuracy check
        if not self.validate_documentation_accuracy():
            all_valid = False
        
        return all_valid
    
    def generate_report(self) -> str:
        """Generate validation report"""
        report = []
        report.append("🔍 CLAUDE CODE COMPLIANCE VALIDATION REPORT")
        report.append("=" * 50)
        report.append(f"Validation Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Files Processed: {self.total_files}")
        report.append(f"Total Issues Found: {len(self.issues)}")
        report.append("")
        
        if not self.issues:
            report.append("🎉 ALL VALIDATIONS PASSED!")
            report.append("✅ 100% Claude Code Compliance Maintained")
        else:
            # Group issues by type
            by_type = {}
            for issue in self.issues:
                issue_type = issue['type']
                if issue_type not in by_type:
                    by_type[issue_type] = []
                by_type[issue_type].append(issue)
            
            for issue_type, issues in by_type.items():
                report.append(f"❌ {issue_type} ISSUES ({len(issues)}):")
                for issue in issues:
                    severity_icon = "🔴" if issue['severity'] == 'ERROR' else "🟡"
                    report.append(f"  {severity_icon} {issue['file']}: {issue['issue']}")
                report.append("")
        
        report.append("=" * 50)
        return "\n".join(report)
    
    def test_validation_detection(self) -> bool:
        """Test that the validator can detect intentionally broken commands"""
        self.log("Testing validation detection capability...")
        
        # Create a temporary broken command file
        test_file = os.path.join(self.commands_dir, 'test-broken-command.md')
        broken_content = """---
name: /test-broken
description: 
tools: Read, Write
---

# Test broken command
This is intentionally broken for testing.
"""
        
        try:
            with open(test_file, 'w') as f:
                f.write(broken_content)
            
            # Validate the broken file
            is_valid, issues = self.validate_yaml_frontmatter(test_file)
            
            # Clean up
            os.remove(test_file)
            
            # Should detect issues
            if is_valid:
                self.log("ERROR: Failed to detect intentionally broken command", "ERROR")
                return False
            else:
                self.log(f"✅ Successfully detected {len(issues)} issues in broken command")
                return True
                
        except Exception as e:
            self.log(f"Error during detection test: {e}", "ERROR")
            return False

def main():
    parser = argparse.ArgumentParser(description="Master Claude Code Compliance Validator")
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--fix-issues', action='store_true', help='Attempt to fix issues automatically')
    parser.add_argument('--test-detection', action='store_true', help='Test validation detection capability')
    
    args = parser.parse_args()
    
    validator = ComplianceValidator(verbose=args.verbose, fix_issues=args.fix_issues)
    
    try:
        # Test detection capability if requested
        if args.test_detection:
            if not validator.test_validation_detection():
                print("❌ Validation detection test failed")
                return 2
            print("✅ Validation detection test passed")
            return 0
        
        # Run full validation
        is_valid = validator.run_validation()
        
        # Generate and display report
        report = validator.generate_report()
        print(report)
        
        # Save report to file
        with open('.claude/compliance-validation-report.txt', 'w') as f:
            f.write(report)
        
        return 0 if is_valid else 1
        
    except Exception as e:
        print(f"❌ Script error: {e}")
        return 2

if __name__ == "__main__":
    sys.exit(main())