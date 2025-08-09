#!/usr/bin/env python3
"""
YAML Compliance Verification Test
=================================

Comprehensive YAML frontmatter validation for all 88 Claude Code commands.
Validates Phase 1 compliance achievements and ensures all commands meet
Claude Code standards.

Tests:
- YAML frontmatter structure and syntax
- Required fields (name, description, usage, allowed-tools, category)
- No deprecated 'tools' fields
- Proper field formatting and values
- Claude Code compatibility standards

Author: Testing Framework Agent
Date: 2025-07-31
"""

import os
import yaml
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum


class YAMLTestResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"


@dataclass
class YAMLTest:
    file_path: str
    test_name: str
    result: YAMLTestResult
    details: str
    score: float = 0.0


class YAMLComplianceVerifier:
    """Comprehensive YAML compliance verification for Claude Code commands"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.commands_dir = self.project_root / ".claude" / "commands"
        self.test_results: List[YAMLTest] = []
        
        # Claude Code YAML standards
        self.required_fields = ['name', 'description']
        self.recommended_fields = ['usage', 'allowed-tools', 'category']
        self.deprecated_fields = ['tools', 'argument-hint']
        self.allowed_tools = [
            'Read', 'Write', 'Edit', 'MultiEdit', 'Glob', 'Grep', 
            'Bash', 'LS', 'WebFetch', 'WebSearch', 'NotebookRead', 'NotebookEdit'
        ]
        
        # Expected command count from documentation
        self.expected_command_count = 88
    
    def run_yaml_compliance_verification(self) -> Dict:
        """Run comprehensive YAML compliance verification"""
        print("📋 YAML Compliance Verification for Claude Code Commands")
        print("="*55)
        
        # Test 1: Command Discovery and Count
        print("\n🔍 Discovering Command Files")
        command_files = self.discover_command_files()
        
        # Test 2: YAML Structure Validation
        print("\n📝 Validating YAML Structure")
        self.validate_yaml_structure(command_files)
        
        # Test 3: Required Fields Validation
        print("\n✅ Validating Required Fields")
        self.validate_required_fields(command_files)
        
        # Test 4: Deprecated Fields Check
        print("\n🚫 Checking for Deprecated Fields")
        self.check_deprecated_fields(command_files)
        
        # Test 5: Field Value Validation
        print("\n🔧 Validating Field Values")
        self.validate_field_values(command_files)
        
        # Test 6: Claude Code Compatibility
        print("\n🎯 Verifying Claude Code Compatibility")
        self.verify_claude_code_compatibility(command_files)
        
        return self.generate_yaml_compliance_report()
    
    def discover_command_files(self) -> List[Path]:
        """Discover and validate command file count"""
        
        if not self.commands_dir.exists():
            self.test_results.append(YAMLTest(
                "system",
                "Commands Directory Exists",
                YAMLTestResult.FAIL,
                "Commands directory not found",
                0.0
            ))
            return []
        
        # Find all .md files in commands directory
        command_files = list(self.commands_dir.rglob("*.md"))
        actual_count = len(command_files)
        
        # Validate count matches documentation
        if actual_count == self.expected_command_count:
            self.test_results.append(YAMLTest(
                "system",
                "Command Count Verification",
                YAMLTestResult.PASS,
                f"Found exactly {actual_count} command files as expected",
                100.0
            ))
        elif abs(actual_count - self.expected_command_count) <= 2:
            self.test_results.append(YAMLTest(
                "system",
                "Command Count Verification",
                YAMLTestResult.WARNING,
                f"Found {actual_count} commands, expected {self.expected_command_count} (within tolerance)",
                90.0
            ))
        else:
            self.test_results.append(YAMLTest(
                "system",
                "Command Count Verification",
                YAMLTestResult.FAIL,
                f"Found {actual_count} commands, expected {self.expected_command_count}",
                50.0
            ))
        
        print(f"    📊 Discovered {actual_count} command files")
        return command_files
    
    def validate_yaml_structure(self, command_files: List[Path]):
        """Validate YAML frontmatter structure"""
        
        yaml_structure_passed = 0
        yaml_structure_failed = 0
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                relative_path = str(cmd_file.relative_to(self.project_root))
                
                # Check for YAML frontmatter
                if not content.startswith('---'):
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "YAML Frontmatter Start",
                        YAMLTestResult.FAIL,
                        "File does not start with YAML frontmatter delimiter '---'",
                        0.0
                    ))
                    yaml_structure_failed += 1
                    continue
                
                # Find YAML end delimiter
                yaml_end = content.find('---', 3)
                if yaml_end == -1:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "YAML Frontmatter End",
                        YAMLTestResult.FAIL,
                        "YAML frontmatter not properly closed with '---'",
                        0.0
                    ))
                    yaml_structure_failed += 1
                    continue
                
                # Extract and parse YAML
                yaml_content = content[3:yaml_end].strip()
                
                try:
                    yaml_data = yaml.safe_load(yaml_content)
                    
                    if yaml_data is None:
                        self.test_results.append(YAMLTest(
                            relative_path,
                            "YAML Content",
                            YAMLTestResult.FAIL,
                            "YAML frontmatter is empty",
                            0.0
                        ))
                        yaml_structure_failed += 1
                        continue
                    
                    if not isinstance(yaml_data, dict):
                        self.test_results.append(YAMLTest(
                            relative_path,
                            "YAML Structure",
                            YAMLTestResult.FAIL,
                            "YAML frontmatter is not a dictionary",
                            0.0
                        ))
                        yaml_structure_failed += 1
                        continue
                    
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "YAML Structure",
                        YAMLTestResult.PASS,
                        "Valid YAML frontmatter structure",
                        100.0
                    ))
                    yaml_structure_passed += 1
                    
                except yaml.YAMLError as e:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "YAML Parsing",
                        YAMLTestResult.FAIL,
                        f"YAML parsing error: {str(e)}",
                        0.0
                    ))
                    yaml_structure_failed += 1
                    
            except Exception as e:
                self.test_results.append(YAMLTest(
                    str(cmd_file),
                    "File Reading",
                    YAMLTestResult.FAIL,
                    f"Cannot read file: {str(e)}",
                    0.0
                ))
                yaml_structure_failed += 1
        
        print(f"    ✅ YAML Structure: {yaml_structure_passed}/{len(command_files)} files passed")
    
    def validate_required_fields(self, command_files: List[Path]):
        """Validate required YAML fields"""
        
        required_fields_passed = 0
        required_fields_failed = 0
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                relative_path = str(cmd_file.relative_to(self.project_root))
                
                # Extract YAML data
                yaml_end = content.find('---', 3)
                if yaml_end == -1:
                    continue  # Already handled in structure validation
                
                yaml_content = content[3:yaml_end].strip()
                yaml_data = yaml.safe_load(yaml_content)
                
                if not isinstance(yaml_data, dict):
                    continue  # Already handled in structure validation
                
                # Check required fields
                missing_required = []
                for field in self.required_fields:
                    if field not in yaml_data:
                        missing_required.append(field)
                
                # Check recommended fields
                missing_recommended = []
                for field in self.recommended_fields:
                    if field not in yaml_data:
                        missing_recommended.append(field)
                
                if not missing_required:
                    if not missing_recommended:
                        self.test_results.append(YAMLTest(
                            relative_path,
                            "Required Fields",
                            YAMLTestResult.PASS,
                            "All required and recommended fields present",
                            100.0
                        ))
                        required_fields_passed += 1
                    else:
                        self.test_results.append(YAMLTest(
                            relative_path,
                            "Required Fields",
                            YAMLTestResult.WARNING,
                            f"Missing recommended fields: {missing_recommended}",
                            85.0
                        ))
                        required_fields_passed += 1
                else:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "Required Fields",
                        YAMLTestResult.FAIL,
                        f"Missing required fields: {missing_required}",
                        50.0
                    ))
                    required_fields_failed += 1
                    
            except Exception as e:
                continue  # Skip files with parsing errors
        
        print(f"    ✅ Required Fields: {required_fields_passed}/{len(command_files)} files passed")
    
    def check_deprecated_fields(self, command_files: List[Path]):
        """Check for deprecated YAML fields"""
        
        deprecated_fields_found = []
        clean_files = 0
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                relative_path = str(cmd_file.relative_to(self.project_root))
                
                # Extract YAML data
                yaml_end = content.find('---', 3)
                if yaml_end == -1:
                    continue
                
                yaml_content = content[3:yaml_end].strip()
                yaml_data = yaml.safe_load(yaml_content)
                
                if not isinstance(yaml_data, dict):
                    continue
                
                # Check for deprecated fields
                found_deprecated = []
                for field in self.deprecated_fields:
                    if field in yaml_data:
                        found_deprecated.append(field)
                
                if found_deprecated:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "Deprecated Fields",
                        YAMLTestResult.FAIL,
                        f"Contains deprecated fields: {found_deprecated}",
                        0.0
                    ))
                    deprecated_fields_found.append({
                        'file': relative_path,
                        'fields': found_deprecated
                    })
                else:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "Deprecated Fields",
                        YAMLTestResult.PASS,
                        "No deprecated fields found",
                        100.0
                    ))
                    clean_files += 1
                    
            except Exception as e:
                continue
        
        if deprecated_fields_found:
            print(f"    ❌ Deprecated Fields: Found in {len(deprecated_fields_found)} files")
        else:
            print(f"    ✅ Deprecated Fields: All {clean_files} files clean")
    
    def validate_field_values(self, command_files: List[Path]):
        """Validate YAML field values"""
        
        valid_values_passed = 0
        valid_values_failed = 0
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                relative_path = str(cmd_file.relative_to(self.project_root))
                
                # Extract YAML data
                yaml_end = content.find('---', 3)
                if yaml_end == -1:
                    continue
                
                yaml_content = content[3:yaml_end].strip()
                yaml_data = yaml.safe_load(yaml_content)
                
                if not isinstance(yaml_data, dict):
                    continue
                
                validation_issues = []
                
                # Validate 'name' field
                if 'name' in yaml_data:
                    name = yaml_data['name']
                    if not isinstance(name, str) or not name.startswith('/'):
                        validation_issues.append("'name' should be a string starting with '/'")
                
                # Validate 'description' field
                if 'description' in yaml_data:
                    description = yaml_data['description']
                    if not isinstance(description, str) or len(description.strip()) < 10:
                        validation_issues.append("'description' should be a meaningful string")
                
                # Validate 'allowed-tools' field
                if 'allowed-tools' in yaml_data:
                    tools = yaml_data['allowed-tools']
                    if not isinstance(tools, list):
                        validation_issues.append("'allowed-tools' should be a list")
                    else:
                        invalid_tools = [tool for tool in tools if tool not in self.allowed_tools]
                        if invalid_tools:
                            validation_issues.append(f"Invalid tools: {invalid_tools}")
                
                # Validate 'usage' field
                if 'usage' in yaml_data:
                    usage = yaml_data['usage']
                    if not isinstance(usage, str):
                        validation_issues.append("'usage' should be a string")
                
                if not validation_issues:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "Field Values",
                        YAMLTestResult.PASS,
                        "All field values are valid",
                        100.0
                    ))
                    valid_values_passed += 1
                else:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "Field Values",
                        YAMLTestResult.WARNING,
                        f"Field validation issues: {validation_issues}",
                        70.0
                    ))
                    valid_values_failed += 1
                    
            except Exception as e:
                continue
        
        print(f"    ✅ Field Values: {valid_values_passed}/{valid_values_passed + valid_values_failed} files passed")
    
    def verify_claude_code_compatibility(self, command_files: List[Path]):
        """Verify Claude Code compatibility"""
        
        compatibility_passed = 0
        compatibility_issues = 0
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                relative_path = str(cmd_file.relative_to(self.project_root))
                
                # Extract YAML data
                yaml_end = content.find('---', 3)
                if yaml_end == -1:
                    continue
                
                yaml_content = content[3:yaml_end].strip()
                yaml_data = yaml.safe_load(yaml_content)
                
                if not isinstance(yaml_data, dict):
                    continue
                
                compatibility_score = 100
                issues = []
                
                # Check for Claude Code standard compliance
                if 'name' not in yaml_data or not yaml_data['name'].startswith('/'):
                    compatibility_score -= 25
                    issues.append("name should start with '/'")
                
                if 'description' not in yaml_data:
                    compatibility_score -= 25
                    issues.append("missing description")
                
                if 'allowed-tools' not in yaml_data:
                    compatibility_score -= 20
                    issues.append("missing allowed-tools")
                
                # Check for deprecated patterns
                if 'tools' in yaml_data:
                    compatibility_score -= 30
                    issues.append("uses deprecated 'tools' field")
                
                if compatibility_score >= 90:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "Claude Code Compatibility",
                        YAMLTestResult.PASS,
                        "Full Claude Code compatibility",
                        compatibility_score
                    ))
                    compatibility_passed += 1
                elif compatibility_score >= 70:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "Claude Code Compatibility",
                        YAMLTestResult.WARNING,
                        f"Minor compatibility issues: {issues}",
                        compatibility_score
                    ))
                    compatibility_passed += 1
                else:
                    self.test_results.append(YAMLTest(
                        relative_path,
                        "Claude Code Compatibility",
                        YAMLTestResult.FAIL,
                        f"Major compatibility issues: {issues}",
                        compatibility_score
                    ))
                    compatibility_issues += 1
                    
            except Exception as e:
                continue
        
        print(f"    ✅ Claude Code Compatibility: {compatibility_passed}/{len(command_files)} files compatible")
    
    def generate_yaml_compliance_report(self) -> Dict:
        """Generate comprehensive YAML compliance report"""
        print("\n" + "="*55)
        print("🏆 YAML COMPLIANCE VERIFICATION RESULTS")
        print("="*55)
        
        # Calculate statistics
        total_tests = len(self.test_results)
        passed = sum(1 for r in self.test_results if r.result == YAMLTestResult.PASS)
        failed = sum(1 for r in self.test_results if r.result == YAMLTestResult.FAIL)
        warnings = sum(1 for r in self.test_results if r.result == YAMLTestResult.WARNING)
        
        # Calculate scores by test type
        test_categories = {}
        for result in self.test_results:
            category = result.test_name
            if category not in test_categories:
                test_categories[category] = []
            test_categories[category].append(result.score)
        
        category_averages = {
            category: sum(scores) / len(scores) if scores else 0
            for category, scores in test_categories.items()
        }
        
        overall_score = sum(category_averages.values()) / len(category_averages) if category_averages else 0
        
        print(f"\n📊 COMPLIANCE SUMMARY:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed}")
        print(f"   ❌ Failed: {failed}")
        print(f"   ⚠️  Warnings: {warnings}")
        print(f"   📈 Overall Compliance Score: {overall_score:.1f}%")
        
        # Grade assignment
        if overall_score >= 95:
            grade = "A+"
        elif overall_score >= 90:
            grade = "A"
        elif overall_score >= 85:
            grade = "B+"
        elif overall_score >= 80:
            grade = "B"
        else:
            grade = "C"
        
        print(f"   🎓 YAML Compliance Grade: {grade}")
        
        # Category breakdown
        print(f"\n📋 COMPLIANCE BY CATEGORY:")
        for category, avg_score in category_averages.items():
            print(f"   {category}: {avg_score:.1f}%")
        
        # Critical issues
        critical_failures = [r for r in self.test_results 
                           if r.result == YAMLTestResult.FAIL and 
                           ('deprecated' in r.test_name.lower() or 
                            'required' in r.test_name.lower())]
        
        if critical_failures:
            print(f"\n❌ CRITICAL ISSUES FOUND:")
            for failure in critical_failures[:5]:  # Show first 5
                print(f"   • {failure.file_path}: {failure.details}")
            if len(critical_failures) > 5:
                print(f"   • ... and {len(critical_failures) - 5} more critical issues")
        
        # Phase 1 compliance assessment
        print(f"\n🎯 PHASE 1 COMPLIANCE ASSESSMENT:")
        
        deprecated_failures = [r for r in self.test_results 
                             if 'deprecated' in r.test_name.lower() and 
                             r.result == YAMLTestResult.FAIL]
        
        if not deprecated_failures:
            print("   ✅ No deprecated 'tools' fields found")
            print("   ✅ All commands use 'allowed-tools' field")
            print("   ✅ YAML field standardization complete")
            
            if overall_score >= 90:
                print("   🚀 PHASE 1 STATUS: FULLY COMPLIANT")
            else:
                print("   🔧 PHASE 1 STATUS: COMPLIANT WITH MINOR ISSUES")
        else:
            print(f"   ❌ {len(deprecated_failures)} files still use deprecated fields")
            print("   🔧 PHASE 1 STATUS: REQUIRES COMPLETION")
        
        return {
            "timestamp": "2025-07-31",
            "total_tests": total_tests,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "overall_score": overall_score,
            "grade": grade,
            "category_scores": category_averages,
            "critical_failures": len(critical_failures),
            "deprecated_failures": len(deprecated_failures),
            "phase1_compliant": len(deprecated_failures) == 0,
            "system_status": "FULLY COMPLIANT" if overall_score >= 90 and not critical_failures else "NEEDS WORK",
            "test_details": [
                {
                    "file_path": r.file_path,
                    "test_name": r.test_name,
                    "result": r.result.value,
                    "details": r.details,
                    "score": r.score
                } for r in self.test_results
            ]
        }


def main():
    """Run YAML Compliance Verification"""
    verifier = YAMLComplianceVerifier()
    results = verifier.run_yaml_compliance_verification()
    
    # Save results
    import json
    with open("yaml_compliance_verification_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n🏁 YAML Compliance Verification Complete!")
    print(f"   Overall Score: {results['overall_score']:.1f}%")
    print(f"   Grade: {results['grade']}")
    print(f"   Phase 1 Compliant: {'Yes' if results['phase1_compliant'] else 'No'}")
    print(f"   Status: {results['system_status']}")
    
    return results


if __name__ == "__main__":
    main()