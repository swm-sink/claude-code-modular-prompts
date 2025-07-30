#!/usr/bin/env python3
"""
Comprehensive System Integration Test Framework
Step 81 of 100-Step Finalization Plan

PURPOSE: End-to-end validation of entire Claude Code template library system
SCOPE: All commands, components, documentation, and workflows
"""

import os
import sys
import yaml
import json
import time
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class IntegrationTestResult:
    test_name: str
    status: str  # PASS, FAIL, SKIP, ERROR
    execution_time: float
    message: str
    details: Optional[Dict[str, Any]] = None

class ComprehensiveSystemIntegrationTester:
    """End-to-end system integration testing framework"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.results: List[IntegrationTestResult] = []
        self.start_time = time.time()
        
        # Core paths
        self.claude_dir = project_root / ".claude"
        self.commands_dir = self.claude_dir / "commands"
        self.components_dir = self.claude_dir / "components"
        self.docs_dir = project_root / "docs"
        
    def run_comprehensive_integration_tests(self) -> Dict[str, Any]:
        """Execute all integration tests"""
        print("🚀 COMPREHENSIVE SYSTEM INTEGRATION TESTING")
        print("=" * 60)
        
        # Test Categories
        test_categories = [
            ("File System Integration", self._test_file_system_integration),
            ("Command Template Integration", self._test_command_integration),
            ("Component System Integration", self._test_component_integration),
            ("Documentation Integration", self._test_documentation_integration),
            ("YAML Compliance Integration", self._test_yaml_integration),
            ("Cross-System Compatibility", self._test_cross_system_compatibility),
            ("Workflow Integration", self._test_workflow_integration),
            ("Security Integration", self._test_security_integration)
        ]
        
        for category_name, test_method in test_categories:
            print(f"\n🧪 Testing: {category_name}")
            try:
                test_method()
            except Exception as e:
                self._add_result(f"{category_name} - Critical Error", 
                               "ERROR", 0, f"Unexpected error: {str(e)}")
        
        return self._generate_comprehensive_report()
    
    def _test_file_system_integration(self):
        """Test file system structure and accessibility"""
        start = time.time()
        
        # Test core directory structure
        required_dirs = [
            self.claude_dir,
            self.commands_dir,
            self.components_dir,
            self.claude_dir / "context",
            self.claude_dir / "config"
        ]
        
        missing_dirs = [d for d in required_dirs if not d.exists()]
        if missing_dirs:
            self._add_result("File System Structure", "FAIL", time.time() - start,
                           f"Missing directories: {[str(d) for d in missing_dirs]}")
            return
        
        # Test file accessibility
        try:
            # Count files in each directory
            command_count = len(list(self.commands_dir.rglob("*.md")))
            component_count = len(list(self.components_dir.rglob("*.md")))
            
            self._add_result("File System Structure", "PASS", time.time() - start,
                           f"All directories accessible. Commands: {command_count}, Components: {component_count}")
        except Exception as e:
            self._add_result("File System Structure", "FAIL", time.time() - start,
                           f"File access error: {str(e)}")
    
    def _test_command_integration(self):
        """Test command template integration and functionality"""
        start = time.time()
        
        command_files = list(self.commands_dir.rglob("*.md"))
        if not command_files:
            self._add_result("Command Integration", "FAIL", time.time() - start,
                           "No command files found")
            return
        
        valid_commands = 0
        invalid_commands = []
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                
                # Check for YAML frontmatter
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end > 0:
                        yaml_content = content[3:yaml_end]
                        yaml_data = yaml.safe_load(yaml_content)
                        
                        # Validate required fields
                        required_fields = ['name', 'description']
                        if all(field in yaml_data for field in required_fields):
                            valid_commands += 1
                        else:
                            invalid_commands.append(f"{cmd_file.name}: Missing required fields")
                    else:
                        invalid_commands.append(f"{cmd_file.name}: Invalid YAML frontmatter")
                else:
                    invalid_commands.append(f"{cmd_file.name}: No YAML frontmatter")
            except Exception as e:
                invalid_commands.append(f"{cmd_file.name}: {str(e)}")
        
        success_rate = (valid_commands / len(command_files)) * 100
        status = "PASS" if success_rate >= 95 else "FAIL"
        
        message = f"Commands tested: {len(command_files)}, Valid: {valid_commands} ({success_rate:.1f}%)"
        if invalid_commands:
            message += f", Issues: {len(invalid_commands)}"
        
        self._add_result("Command Integration", status, time.time() - start, message,
                        {"invalid_commands": invalid_commands[:5]})  # Limit to first 5
    
    def _test_component_integration(self):
        """Test component system integration"""
        start = time.time()
        
        component_files = list(self.components_dir.rglob("*.md"))
        if not component_files:
            self._add_result("Component Integration", "FAIL", time.time() - start,
                           "No component files found")
            return
        
        # Test different component types
        atomic_components = [f for f in component_files if 'atomic' in str(f)]
        regular_components = [f for f in component_files if 'atomic' not in str(f)]
        
        # Validate atomic components (should be simple)
        valid_atomic = 0
        for comp in atomic_components:
            try:
                content = comp.read_text(encoding='utf-8')
                # Atomic components should be concise (< 20 lines)
                if len(content.split('\n')) <= 20:
                    valid_atomic += 1
            except:
                pass
        
        atomic_success = (valid_atomic / len(atomic_components)) * 100 if atomic_components else 100
        
        message = f"Components: {len(component_files)} (Atomic: {len(atomic_components)}, Regular: {len(regular_components)})"
        message += f", Atomic compliance: {atomic_success:.1f}%"
        
        status = "PASS" if atomic_success >= 80 else "FAIL"
        self._add_result("Component Integration", status, time.time() - start, message)
    
    def _test_documentation_integration(self):
        """Test documentation system integration"""
        start = time.time()
        
        # Key documentation files
        key_docs = [
            self.project_root / "README.md",
            self.project_root / "CLAUDE.md",
            self.project_root / "100-STEP-FINALIZATION-PLAN.md"
        ]
        
        existing_docs = [doc for doc in key_docs if doc.exists()]
        
        # Test README accuracy
        readme_accurate = True
        if (self.project_root / "README.md").exists():
            readme_content = (self.project_root / "README.md").read_text()
            # Check if command count in README matches reality
            command_count = len(list(self.commands_dir.rglob("*.md")))
            # Simple heuristic: if README mentions command counts, they should be reasonably accurate
            if "command" in readme_content.lower() and str(command_count) not in readme_content:
                readme_accurate = False
        
        status = "PASS" if len(existing_docs) >= 2 and readme_accurate else "FAIL"
        message = f"Key docs found: {len(existing_docs)}/{len(key_docs)}, README accurate: {readme_accurate}"
        
        self._add_result("Documentation Integration", status, time.time() - start, message,
                        {"existing_docs": [str(doc.name) for doc in existing_docs]})
    
    def _test_yaml_integration(self):
        """Test YAML system integration"""
        start = time.time()
        
        # Find all YAML frontmatter in commands
        command_files = list(self.commands_dir.rglob("*.md"))
        yaml_valid = 0
        yaml_errors = []
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end > 0:
                        yaml_content = content[3:yaml_end]
                        yaml_data = yaml.safe_load(yaml_content)
                        
                        # Check for Claude Code compliance
                        if 'allowed-tools' in yaml_data or 'tools' not in yaml_data:
                            yaml_valid += 1
                        else:
                            yaml_errors.append(f"{cmd_file.name}: Uses deprecated 'tools' field")
                    else:
                        yaml_errors.append(f"{cmd_file.name}: Invalid YAML structure")
                else:
                    yaml_errors.append(f"{cmd_file.name}: No YAML frontmatter")
            except Exception as e:
                yaml_errors.append(f"{cmd_file.name}: {str(e)}")
        
        success_rate = (yaml_valid / len(command_files)) * 100 if command_files else 0
        status = "PASS" if success_rate >= 95 else "FAIL"
        
        message = f"YAML compliance: {yaml_valid}/{len(command_files)} ({success_rate:.1f}%)"
        
        self._add_result("YAML Integration", status, time.time() - start, message,
                        {"yaml_errors": yaml_errors[:3]})
    
    def _test_cross_system_compatibility(self):
        """Test cross-system compatibility"""
        start = time.time()
        
        # Test file encoding consistency
        encoding_issues = []
        for file_path in self.project_root.rglob("*.md"):
            try:
                file_path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                encoding_issues.append(str(file_path))
        
        # Test path compatibility (no spaces, special chars in critical paths)
        path_issues = []
        for path in [self.claude_dir, self.commands_dir, self.components_dir]:
            if ' ' in str(path):
                path_issues.append(f"Space in path: {path}")
        
        status = "PASS" if not encoding_issues and not path_issues else "FAIL"
        message = f"Encoding issues: {len(encoding_issues)}, Path issues: {len(path_issues)}"
        
        self._add_result("Cross-System Compatibility", status, time.time() - start, message)
    
    def _test_workflow_integration(self):
        """Test workflow integration"""
        start = time.time()
        
        # Test script executability
        script_files = list(self.project_root.rglob("*.py"))
        executable_scripts = []
        
        for script in script_files:
            if script.name.startswith(('test', 'validate', 'enhanced')):
                try:
                    # Simple syntax check
                    subprocess.run([sys.executable, '-m', 'py_compile', str(script)], 
                                 capture_output=True, check=True, timeout=10)
                    executable_scripts.append(script.name)
                except:
                    pass
        
        status = "PASS" if len(executable_scripts) >= 3 else "FAIL"
        message = f"Executable scripts found: {len(executable_scripts)}"
        
        self._add_result("Workflow Integration", status, time.time() - start, message,
                        {"executable_scripts": executable_scripts})
    
    def _test_security_integration(self):
        """Test security integration"""
        start = time.time()
        
        security_issues = []
        
        # Check for potential security issues in files
        for file_path in self.project_root.rglob("*"):
            if file_path.is_file() and file_path.suffix in ['.py', '.sh', '.md']:
                try:
                    content = file_path.read_text(encoding='utf-8').lower()
                    
                    # Look for potential security concerns
                    if 'password' in content and '=' in content:
                        security_issues.append(f"Potential password in {file_path.name}")
                    if 'secret' in content and '=' in content:
                        security_issues.append(f"Potential secret in {file_path.name}")
                    if 'token' in content and '=' in content:
                        security_issues.append(f"Potential token in {file_path.name}")
                except:
                    pass
        
        # Limit security issue reporting
        security_issues = security_issues[:5]
        
        status = "PASS" if len(security_issues) == 0 else "FAIL"
        message = f"Security issues found: {len(security_issues)}"
        
        self._add_result("Security Integration", status, time.time() - start, message,
                        {"security_issues": security_issues})
    
    def _add_result(self, test_name: str, status: str, execution_time: float, 
                   message: str, details: Optional[Dict[str, Any]] = None):
        """Add test result"""
        self.results.append(IntegrationTestResult(
            test_name=test_name,
            status=status,
            execution_time=execution_time,
            message=message,
            details=details
        ))
        
        # Real-time feedback
        status_emoji = {"PASS": "✅", "FAIL": "❌", "SKIP": "⏭️", "ERROR": "💥"}
        print(f"  {status_emoji.get(status, '❓')} {test_name}: {message}")
    
    def _generate_comprehensive_report(self) -> Dict[str, Any]:
        """Generate comprehensive integration test report"""
        total_time = time.time() - self.start_time
        
        # Calculate statistics
        total_tests = len(self.results)
        passed_tests = len([r for r in self.results if r.status == "PASS"])
        failed_tests = len([r for r in self.results if r.status == "FAIL"])
        error_tests = len([r for r in self.results if r.status == "ERROR"])
        
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        # Overall grade
        if success_rate >= 95:
            grade = "A+ (Exceptional)"
        elif success_rate >= 90:
            grade = "A (Excellent)"
        elif success_rate >= 85:
            grade = "B+ (Very Good)"
        elif success_rate >= 80:
            grade = "B (Good)"
        elif success_rate >= 75:
            grade = "C+ (Acceptable)"
        elif success_rate >= 70:
            grade = "C (Needs Work)"
        else:
            grade = "F (Critical Issues)"
        
        report = {
            "test_summary": {
                "total_tests": total_tests,
                "passed": passed_tests,
                "failed": failed_tests,
                "errors": error_tests,
                "success_rate": f"{success_rate:.1f}%",
                "grade": grade,
                "total_execution_time": f"{total_time:.2f}s"
            },
            "detailed_results": [
                {
                    "test": r.test_name,
                    "status": r.status,
                    "time": f"{r.execution_time:.3f}s",
                    "message": r.message,
                    "details": r.details
                }
                for r in self.results
            ],
            "recommendations": self._generate_recommendations()
        }
        
        return report
    
    def _generate_recommendations(self) -> List[str]:
        """Generate improvement recommendations based on test results"""
        recommendations = []
        
        failed_tests = [r for r in self.results if r.status == "FAIL"]
        error_tests = [r for r in self.results if r.status == "ERROR"]
        
        if failed_tests:
            recommendations.append(f"Fix {len(failed_tests)} failed integration tests")
        
        if error_tests:
            recommendations.append(f"Resolve {len(error_tests)} critical errors")
        
        # Specific recommendations based on test results
        yaml_failures = [r for r in failed_tests if "YAML" in r.test_name]
        if yaml_failures:
            recommendations.append("Update YAML frontmatter to Claude Code compliance")
        
        security_failures = [r for r in failed_tests if "Security" in r.test_name]
        if security_failures:
            recommendations.append("Address security concerns in codebase")
        
        if not recommendations:
            recommendations.append("System integration is excellent - ready for production")
        
        return recommendations

def main():
    """Run comprehensive system integration tests"""
    project_root = Path.cwd()
    
    print(f"🔍 Project root: {project_root}")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    tester = ComprehensiveSystemIntegrationTester(project_root)
    report = tester.run_comprehensive_integration_tests()
    
    # Display summary
    print("\n" + "="*60)
    print("📊 COMPREHENSIVE INTEGRATION TEST SUMMARY")
    print("="*60)
    
    summary = report["test_summary"]
    print(f"Total Tests: {summary['total_tests']}")
    print(f"Passed: {summary['passed']} | Failed: {summary['failed']} | Errors: {summary['errors']}")
    print(f"Success Rate: {summary['success_rate']}")
    print(f"Grade: {summary['grade']}")
    print(f"Execution Time: {summary['total_execution_time']}")
    
    if report["recommendations"]:
        print(f"\n🎯 RECOMMENDATIONS:")
        for i, rec in enumerate(report["recommendations"], 1):
            print(f"{i}. {rec}")
    
    # Save detailed report
    report_file = project_root / "STEP-81-COMPREHENSIVE-INTEGRATION-TEST-RESULTS.md"
    with open(report_file, 'w') as f:
        f.write("# Step 81: Comprehensive System Integration Test Results\n\n")
        f.write(f"**Executed**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Grade**: {summary['grade']}\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- **Total Tests**: {summary['total_tests']}\n")
        f.write(f"- **Success Rate**: {summary['success_rate']}\n")
        f.write(f"- **Execution Time**: {summary['total_execution_time']}\n\n")
        
        f.write("## Detailed Results\n\n")
        for result in report["detailed_results"]:
            status_emoji = {"PASS": "✅", "FAIL": "❌", "SKIP": "⏭️", "ERROR": "💥"}
            f.write(f"### {status_emoji.get(result['status'], '❓')} {result['test']}\n")
            f.write(f"**Status**: {result['status']} | **Time**: {result['time']}\n")
            f.write(f"**Message**: {result['message']}\n\n")
            if result['details']:
                f.write(f"**Details**: {json.dumps(result['details'], indent=2)}\n\n")
        
        f.write("## Recommendations\n\n")
        for i, rec in enumerate(report["recommendations"], 1):
            f.write(f"{i}. {rec}\n")
    
    print(f"\n📄 Detailed report saved: {report_file}")
    
    return float(summary['success_rate'].rstrip('%')) >= 80  # Return success boolean

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)