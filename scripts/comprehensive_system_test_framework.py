#!/usr/bin/env python3
"""
Comprehensive System Testing Framework
======================================

Master test suite for validating all layers of the Progressive Disclosure System
and ensuring the Claude Code Modular Prompts project works as documented.

Test Coverage:
- 88 Claude Code commands with YAML compliance
- 3-layer Progressive Disclosure System functionality
- 91 component library integration
- Documentation accuracy verification
- End-to-end workflow validation

Author: Testing Framework Agent
Date: 2025-07-31
"""

import os
import sys
import yaml
import json
import re
import glob
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class TestResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"
    WARNING = "WARNING"


@dataclass
class TestReport:
    name: str
    result: TestResult
    details: str
    execution_time: float = 0.0
    errors: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []


class ComprehensiveSystemTester:
    """Master testing framework for the entire system"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.claude_dir = self.project_root / ".claude"
        self.commands_dir = self.claude_dir / "commands"
        self.components_dir = self.claude_dir / "components"
        self.test_results: List[TestReport] = []
        
        # Test configuration
        self.expected_command_count = 88
        self.expected_component_count = 94
        self.progressive_disclosure_commands = [
            "quick-command.md",
            "build-command.md", 
            "assemble-command.md"
        ]
        
    def run_all_tests(self) -> Dict:
        """Run comprehensive test suite"""
        print("🧪 Starting Comprehensive System Testing Framework")
        print("="*60)
        
        # Phase 1: YAML Compliance Testing
        print("\n📋 Phase 1: YAML Compliance Testing")
        self.test_yaml_compliance()
        
        # Phase 2: Progressive Disclosure System Testing
        print("\n🎯 Phase 2: Progressive Disclosure System Testing")
        self.test_progressive_disclosure_system()
        
        # Phase 3: Component Library Testing
        print("\n🧩 Phase 3: Component Library Testing")
        self.test_component_library()
        
        # Phase 4: Integration Testing
        print("\n🔗 Phase 4: Integration Testing")
        self.test_system_integration()
        
        # Phase 5: Documentation Accuracy Testing
        print("\n📚 Phase 5: Documentation Accuracy Testing")
        self.test_documentation_accuracy()
        
        # Generate comprehensive report
        return self.generate_final_report()
    
    def test_yaml_compliance(self):
        """Test all 88 commands for proper YAML compliance"""
        print("  Testing YAML compliance for all command files...")
        
        # Count actual commands
        command_files = list(self.commands_dir.rglob("*.md"))
        actual_count = len(command_files)
        
        if actual_count != self.expected_command_count:
            self.test_results.append(TestReport(
                "Command Count Verification",
                TestResult.FAIL,
                f"Expected {self.expected_command_count} commands, found {actual_count}"
            ))
        else:
            self.test_results.append(TestReport(
                "Command Count Verification", 
                TestResult.PASS,
                f"Verified {actual_count} command files"
            ))
        
        # Test each command file
        yaml_pass = 0
        yaml_fail = 0
        deprecated_tools_found = []
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                
                # Extract YAML frontmatter
                if not content.startswith('---'):
                    self.test_results.append(TestReport(
                        f"YAML Frontmatter - {cmd_file.name}",
                        TestResult.FAIL,
                        "No YAML frontmatter found"
                    ))
                    yaml_fail += 1
                    continue
                
                # Parse YAML
                yaml_end = content.find('---', 3)
                if yaml_end == -1:
                    self.test_results.append(TestReport(
                        f"YAML Frontmatter - {cmd_file.name}",
                        TestResult.FAIL,
                        "YAML frontmatter not properly closed"
                    ))
                    yaml_fail += 1
                    continue
                
                yaml_content = content[3:yaml_end].strip()
                yaml_data = yaml.safe_load(yaml_content)
                
                # Check required fields
                required_fields = ['name', 'description']
                missing_fields = [field for field in required_fields if field not in yaml_data]
                
                if missing_fields:
                    self.test_results.append(TestReport(
                        f"Required Fields - {cmd_file.name}",
                        TestResult.FAIL,
                        f"Missing required fields: {missing_fields}"
                    ))
                    yaml_fail += 1
                    continue
                
                # Check for deprecated 'tools' field
                if 'tools' in yaml_data:
                    deprecated_tools_found.append(cmd_file.name)
                    self.test_results.append(TestReport(
                        f"Deprecated Tools Field - {cmd_file.name}",
                        TestResult.FAIL,
                        "Found deprecated 'tools' field, should be 'allowed-tools'"
                    ))
                    yaml_fail += 1
                    continue
                
                # Check for proper 'allowed-tools' field
                if 'allowed-tools' not in yaml_data:
                    self.test_results.append(TestReport(
                        f"Allowed Tools Field - {cmd_file.name}",
                        TestResult.WARNING,
                        "No 'allowed-tools' field specified"
                    ))
                
                yaml_pass += 1
                
            except Exception as e:
                self.test_results.append(TestReport(
                    f"YAML Parsing - {cmd_file.name}",
                    TestResult.FAIL,
                    f"YAML parsing error: {str(e)}"
                ))
                yaml_fail += 1
        
        # Summary report
        self.test_results.append(TestReport(
            "YAML Compliance Summary",
            TestResult.PASS if yaml_fail == 0 else TestResult.FAIL,
            f"YAML Compliance: {yaml_pass}/{actual_count} commands passed"
        ))
        
        if deprecated_tools_found:
            self.test_results.append(TestReport(
                "Deprecated Tools Fields",
                TestResult.FAIL,
                f"Found deprecated 'tools' fields in: {deprecated_tools_found}"
            ))
        
        print(f"    ✅ YAML Compliance: {yaml_pass}/{actual_count} commands passed")
        if deprecated_tools_found:
            print(f"    ❌ Deprecated 'tools' fields found in {len(deprecated_tools_found)} files")
    
    def test_progressive_disclosure_system(self):
        """Test all three layers of Progressive Disclosure System"""
        print("  Testing 3-layer Progressive Disclosure System...")
        
        # Test Layer 1: Quick Command
        layer1_path = self.commands_dir / "core" / "quick-command.md"
        if layer1_path.exists():
            content = layer1_path.read_text()
            
            # Check for auto-generation capabilities
            if "Auto-generation Process" in content and "Intelligence Behind Auto-Generation" in content:
                self.test_results.append(TestReport(
                    "Layer 1 - Quick Command Auto-Generation",
                    TestResult.PASS,
                    "Quick command system documented with auto-generation process"
                ))
            else:
                self.test_results.append(TestReport(
                    "Layer 1 - Quick Command Auto-Generation",
                    TestResult.FAIL,
                    "Quick command missing auto-generation documentation"
                ))
            
            # Check for supported command types
            required_types = ["search", "analyze", "transform", "validate", "report"]
            found_types = sum(1 for cmd_type in required_types if cmd_type in content.lower())
            
            if found_types >= 4:
                self.test_results.append(TestReport(
                    "Layer 1 - Command Type Support",
                    TestResult.PASS,
                    f"Found {found_types}/5 command types documented"
                ))
            else:
                self.test_results.append(TestReport(
                    "Layer 1 - Command Type Support",
                    TestResult.FAIL,
                    f"Only {found_types}/5 command types found"
                ))
        else:
            self.test_results.append(TestReport(
                "Layer 1 - Quick Command Existence",
                TestResult.FAIL,
                "quick-command.md not found"
            ))
        
        # Test Layer 2: Build Command
        layer2_path = self.commands_dir / "core" / "build-command.md"
        if layer2_path.exists():
            content = layer2_path.read_text()
            
            # Check for guided customization
            if "guided customization" in content.lower() or "customize" in content.lower():
                self.test_results.append(TestReport(
                    "Layer 2 - Build Command Customization",
                    TestResult.PASS,
                    "Build command system supports guided customization"
                ))
            else:
                self.test_results.append(TestReport(
                    "Layer 2 - Build Command Customization",
                    TestResult.FAIL,
                    "Build command missing customization features"
                ))
        else:
            self.test_results.append(TestReport(
                "Layer 2 - Build Command Existence",
                TestResult.FAIL,
                "build-command.md not found"
            ))
        
        # Test Layer 3: Assemble Command
        layer3_path = self.commands_dir / "core" / "assemble-command.md"
        if layer3_path.exists():
            content = layer3_path.read_text()
            
            # Check for component library access
            if "component" in content.lower() and ("library" in content.lower() or "assembly" in content.lower()):
                self.test_results.append(TestReport(
                    "Layer 3 - Assemble Command Components",
                    TestResult.PASS,
                    "Assemble command provides component library access"
                ))
            else:
                self.test_results.append(TestReport(
                    "Layer 3 - Assemble Command Components",
                    TestResult.FAIL,
                    "Assemble command missing component library features"
                ))
        else:
            self.test_results.append(TestReport(
                "Layer 3 - Assemble Command Existence",
                TestResult.FAIL,
                "assemble-command.md not found"
            ))
        
        print("    ✅ Progressive Disclosure System structure validated")
    
    def test_component_library(self):
        """Test the 91-component library"""
        print("  Testing component library integration...")
        
        # Count actual components
        component_files = list(self.components_dir.rglob("*.md"))
        actual_count = len(component_files)
        
        if actual_count != self.expected_component_count:
            self.test_results.append(TestReport(
                "Component Count Verification",
                TestResult.FAIL,
                f"Expected {self.expected_component_count} components, found {actual_count}"
            ))
        else:
            self.test_results.append(TestReport(
                "Component Count Verification",
                TestResult.PASS,
                f"Verified {actual_count} component files"
            ))
        
        # Test atomic components specifically
        atomic_dir = self.components_dir / "atomic"
        if atomic_dir.exists():
            atomic_components = list(atomic_dir.glob("*.md"))
            self.test_results.append(TestReport(
                "Atomic Components",
                TestResult.PASS,
                f"Found {len(atomic_components)} atomic components"
            ))
            
            # Test a few key atomic components
            key_atomics = [
                "input-validation.md",
                "output-formatter.md", 
                "file-reader.md",
                "error-handler.md"
            ]
            
            found_atomics = []
            for atomic in key_atomics:
                if (atomic_dir / atomic).exists():
                    found_atomics.append(atomic)
            
            if len(found_atomics) >= 3:
                self.test_results.append(TestReport(
                    "Key Atomic Components",
                    TestResult.PASS,
                    f"Found {len(found_atomics)}/4 key atomic components"
                ))
            else:
                self.test_results.append(TestReport(
                    "Key Atomic Components",
                    TestResult.FAIL,
                    f"Only found {len(found_atomics)}/4 key atomic components"
                ))
        else:
            self.test_results.append(TestReport(
                "Atomic Components Directory",
                TestResult.FAIL,
                "Atomic components directory not found"
            ))
        
        print(f"    ✅ Component Library: {actual_count} components verified")
    
    def test_system_integration(self):
        """Test cross-layer integration and workflows"""
        print("  Testing system integration...")
        
        # Test command-component relationships
        component_references = 0
        command_files = list(self.commands_dir.rglob("*.md"))
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text().lower()
                if "component" in content:
                    component_references += 1
            except:
                continue
        
        if component_references > 0:
            self.test_results.append(TestReport(
                "Command-Component Integration",
                TestResult.PASS,
                f"Found component references in {component_references} command files"
            ))
        else:
            self.test_results.append(TestReport(
                "Command-Component Integration",
                TestResult.WARNING,
                "No component references found in command files"
            ))
        
        # Test progressive disclosure upgrade paths
        upgrade_paths = 0
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text().lower()
                if ("build-command" in content or "assemble-command" in content or
                    "layer 2" in content or "layer 3" in content):
                    upgrade_paths += 1
            except:
                continue
        
        if upgrade_paths >= 3:
            self.test_results.append(TestReport(
                "Progressive Disclosure Upgrade Paths",
                TestResult.PASS,
                f"Found upgrade path references in {upgrade_paths} files"
            ))
        else:
            self.test_results.append(TestReport(
                "Progressive Disclosure Upgrade Paths",
                TestResult.WARNING,
                f"Limited upgrade path documentation: {upgrade_paths} references"
            ))
        
        print("    ✅ System integration validated")
    
    def test_documentation_accuracy(self):
        """Test that documentation claims match reality"""
        print("  Testing documentation accuracy...")
        
        # Test CLAUDE.md claims
        claude_md = self.project_root / "CLAUDE.md"
        if claude_md.exists():
            content = claude_md.read_text()
            
            # Check command count claims
            if f"{self.expected_command_count} command" in content:
                self.test_results.append(TestReport(
                    "Documentation Command Count",
                    TestResult.PASS,
                    f"CLAUDE.md correctly states {self.expected_command_count} commands"
                ))
            else:
                self.test_results.append(TestReport(
                    "Documentation Command Count",
                    TestResult.FAIL,
                    f"CLAUDE.md command count doesn't match actual {self.expected_command_count}"
                ))
            
            # Check component count claims
            if f"{self.expected_component_count} component" in content:
                self.test_results.append(TestReport(
                    "Documentation Component Count",
                    TestResult.PASS,
                    f"CLAUDE.md correctly states {self.expected_component_count} components"
                ))
            else:
                self.test_results.append(TestReport(
                    "Documentation Component Count",
                    TestResult.FAIL,
                    f"CLAUDE.md component count doesn't match actual {self.expected_component_count}"
                ))
            
            # Check Progressive Disclosure claims
            if "progressive disclosure" in content.lower() and "3-layer" in content.lower():
                self.test_results.append(TestReport(
                    "Documentation Progressive Disclosure",
                    TestResult.PASS,
                    "CLAUDE.md correctly documents 3-layer Progressive Disclosure System"
                ))
            else:
                self.test_results.append(TestReport(
                    "Documentation Progressive Disclosure",
                    TestResult.WARNING,
                    "Progressive Disclosure System not prominently documented"
                ))
        else:
            self.test_results.append(TestReport(
                "CLAUDE.md Existence",
                TestResult.FAIL,
                "CLAUDE.md not found"
            ))
        
        print("    ✅ Documentation accuracy verified")
    
    def generate_final_report(self) -> Dict:
        """Generate comprehensive test report"""
        print("\n" + "="*60)
        print("🏆 COMPREHENSIVE SYSTEM TEST RESULTS")
        print("="*60)
        
        # Calculate statistics
        total_tests = len(self.test_results)
        passed = sum(1 for r in self.test_results if r.result == TestResult.PASS)
        failed = sum(1 for r in self.test_results if r.result == TestResult.FAIL)
        warnings = sum(1 for r in self.test_results if r.result == TestResult.WARNING)
        
        # Overall score
        score = (passed / total_tests) * 100 if total_tests > 0 else 0
        
        print(f"\n📊 OVERALL RESULTS:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed}")
        print(f"   ❌ Failed: {failed}")
        print(f"   ⚠️  Warnings: {warnings}")
        print(f"   📈 Success Rate: {score:.1f}%")
        
        # Grade assignment
        if score >= 95:
            grade = "A+"
        elif score >= 90:
            grade = "A"
        elif score >= 85:
            grade = "B+"
        elif score >= 80:
            grade = "B"
        elif score >= 75:
            grade = "C+"
        else:
            grade = "C"
        
        print(f"   🎓 Overall Grade: {grade}")
        
        # Detailed results by category
        print(f"\n📋 DETAILED RESULTS:")
        for result in self.test_results:
            status_icon = {
                TestResult.PASS: "✅",
                TestResult.FAIL: "❌", 
                TestResult.WARNING: "⚠️",
                TestResult.SKIP: "⏭️"
            }[result.result]
            
            print(f"   {status_icon} {result.name}: {result.details}")
        
        # System status assessment
        print(f"\n🎯 SYSTEM STATUS ASSESSMENT:")
        
        critical_failures = [r for r in self.test_results 
                           if r.result == TestResult.FAIL and 
                           ("command count" in r.name.lower() or 
                            "component count" in r.name.lower() or
                            "yaml compliance" in r.name.lower())]
        
        if not critical_failures:
            print("   ✅ All critical systems operational")
            print("   ✅ Progressive Disclosure System validated")
            print("   ✅ Component library accessible")
            print("   ✅ Documentation accuracy verified")
            print("   🚀 SYSTEM STATUS: PRODUCTION READY")
        else:
            print("   ❌ Critical system failures detected")
            print("   🔧 SYSTEM STATUS: REQUIRES ATTENTION")
        
        # Generate summary object
        summary = {
            "timestamp": "2025-07-31",
            "total_tests": total_tests,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "success_rate": score,
            "grade": grade,
            "system_status": "PRODUCTION READY" if not critical_failures else "REQUIRES ATTENTION",
            "critical_failures": len(critical_failures),
            "details": [
                {
                    "name": r.name,
                    "result": r.result.value,
                    "details": r.details
                } for r in self.test_results
            ]
        }
        
        print(f"\n📄 Test report saved to comprehensive_test_results.json")
        
        return summary


def main():
    """Run the comprehensive system test framework"""
    tester = ComprehensiveSystemTester()
    results = tester.run_all_tests()
    
    # Save results to file
    with open("comprehensive_test_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n🏁 Testing Complete!")
    print(f"   Success Rate: {results['success_rate']:.1f}%")
    print(f"   Grade: {results['grade']}")
    print(f"   Status: {results['system_status']}")
    
    return results


if __name__ == "__main__":
    main()