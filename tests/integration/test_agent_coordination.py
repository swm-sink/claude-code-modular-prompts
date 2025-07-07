#!/usr/bin/env python3
"""
Integration tests for coordinated agent work verification.
Tests the complete integration of all agent outputs.
"""

import json
import os
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

# Framework root directory
FRAMEWORK_ROOT = Path(__file__).parent.parent.parent


class IntegrationTestSuite:
    """Comprehensive integration testing for agent coordination."""
    
    def __init__(self):
        self.framework_root = FRAMEWORK_ROOT
        self.results = {
            "version_consistency": [],
            "module_dependencies": [],
            "pattern_integration": [],
            "error_recovery": [],
            "quality_gates": []
        }
    
    def test_version_consistency(self) -> Tuple[bool, List[str]]:
        """Test that all framework components have consistent versions."""
        errors = []
        expected_version = "2.3.0"
        
        # Check command versions
        command_dir = self.framework_root / ".claude" / "commands"
        for cmd_file in command_dir.glob("*.md"):
            with open(cmd_file, 'r') as f:
                content = f.read()
                # Extract version from table
                version_match = re.search(r'\| ([\d.]+)\s+\|', content)
                if version_match:
                    version = version_match.group(1)
                    if version != expected_version:
                        errors.append(f"{cmd_file.name}: Found version {version}, expected {expected_version}")
                else:
                    errors.append(f"{cmd_file.name}: No version found")
        
        # Check CLAUDE.md version
        claude_md = self.framework_root / "CLAUDE.md"
        with open(claude_md, 'r') as f:
            content = f.read()
            if f'version="{expected_version}"' not in content:
                errors.append(f"CLAUDE.md: Framework version mismatch")
        
        return len(errors) == 0, errors
    
    def test_module_dependencies(self) -> Tuple[bool, List[str]]:
        """Test that all module dependencies exist and are valid."""
        errors = []
        modules_dir = self.framework_root / ".claude" / "modules"
        
        for module_file in modules_dir.rglob("*.md"):
            with open(module_file, 'r') as f:
                content = f.read()
                
                # Extract dependencies
                depends_match = re.search(r'<depends_on>(.*?)</depends_on>', content, re.DOTALL)
                if depends_match:
                    dependencies = depends_match.group(1)
                    
                    # Check each dependency
                    for line in dependencies.split('\n'):
                        if '.md' in line:
                            # Extract module path
                            module_match = re.search(r'(\w+/[\w-]+\.md)', line)
                            if module_match:
                                dep_path = module_match.group(1)
                                full_dep_path = modules_dir / dep_path
                                if not full_dep_path.exists():
                                    errors.append(f"{module_file.name}: Missing dependency {dep_path}")
        
        return len(errors) == 0, errors
    
    def test_pattern_integration(self) -> Tuple[bool, List[str]]:
        """Test that pattern usage declarations match actual patterns."""
        errors = []
        pattern_lib = self.framework_root / ".claude" / "modules" / "patterns" / "pattern-library.md"
        
        # Load available patterns
        available_patterns = set()
        with open(pattern_lib, 'r') as f:
            content = f.read()
            pattern_matches = re.findall(r'<(\w+_\w+)>', content)
            available_patterns.update(pattern_matches)
        
        # Check pattern usage in modules
        modules_dir = self.framework_root / ".claude" / "modules"
        for module_file in modules_dir.rglob("*.md"):
            if module_file == pattern_lib:
                continue
                
            with open(module_file, 'r') as f:
                content = f.read()
                
                # Extract pattern usage
                usage_matches = re.findall(r'<uses_pattern[^>]*>(\w+)</uses_pattern>', content)
                for pattern in usage_matches:
                    if pattern not in available_patterns:
                        errors.append(f"{module_file.name}: Uses undefined pattern '{pattern}'")
        
        return len(errors) == 0, errors
    
    def test_error_recovery_integration(self) -> Tuple[bool, List[str]]:
        """Test error recovery module integration with other components."""
        errors = []
        error_recovery = self.framework_root / ".claude" / "modules" / "quality" / "error-recovery.md"
        
        if not error_recovery.exists():
            errors.append("Error recovery module not found")
            return False, errors
        
        with open(error_recovery, 'r') as f:
            content = f.read()
            
            # Check for required patterns
            required_patterns = [
                "four_tier_recovery_hierarchy",
                "native_fallback_library",
                "failure_detection_system",
                "recovery_tracking_system"
            ]
            
            for pattern in required_patterns:
                if f"<{pattern}>" not in content:
                    errors.append(f"Error recovery missing required pattern: {pattern}")
            
            # Check integration points
            if "<integration_points>" not in content:
                errors.append("Error recovery missing integration points")
        
        return len(errors) == 0, errors
    
    def test_quality_gates(self) -> Tuple[bool, List[str]]:
        """Test quality gate enforcement across the framework."""
        errors = []
        
        # Check production standards
        prod_standards = self.framework_root / ".claude" / "modules" / "quality" / "production-standards.md"
        if not prod_standards.exists():
            errors.append("Production standards module not found")
        
        # Check TDD module
        tdd_module = self.framework_root / ".claude" / "modules" / "quality" / "tdd.md"
        if not tdd_module.exists():
            errors.append("TDD module not found")
        
        # Verify quality module count (should be 4 or less)
        quality_dir = self.framework_root / ".claude" / "modules" / "quality"
        quality_modules = list(quality_dir.glob("*.md"))
        if len(quality_modules) > 4:
            errors.append(f"Quality module limit exceeded: {len(quality_modules)}/4")
        
        return len(errors) == 0, errors
    
    def run_all_tests(self) -> Dict[str, Tuple[bool, List[str]]]:
        """Run all integration tests and return results."""
        print("🔍 Running Integration Tests for Agent Coordination...")
        print("=" * 60)
        
        tests = {
            "Version Consistency": self.test_version_consistency,
            "Module Dependencies": self.test_module_dependencies,
            "Pattern Integration": self.test_pattern_integration,
            "Error Recovery": self.test_error_recovery_integration,
            "Quality Gates": self.test_quality_gates
        }
        
        results = {}
        total_passed = 0
        
        for test_name, test_func in tests.items():
            print(f"\n🧪 Testing {test_name}...")
            passed, errors = test_func()
            results[test_name] = (passed, errors)
            
            if passed:
                print(f"✅ {test_name}: PASSED")
                total_passed += 1
            else:
                print(f"❌ {test_name}: FAILED")
                for error in errors:
                    print(f"   - {error}")
        
        print("\n" + "=" * 60)
        print(f"📊 Test Summary: {total_passed}/{len(tests)} tests passed")
        
        return results


def main():
    """Main test execution."""
    suite = IntegrationTestSuite()
    results = suite.run_all_tests()
    
    # Generate test report
    report = {
        "test_execution": "Integration Testing - Agent Coordination",
        "total_tests": len(results),
        "passed": sum(1 for passed, _ in results.values() if passed),
        "failed": sum(1 for passed, _ in results.values() if not passed),
        "details": {
            name: {"passed": passed, "errors": errors}
            for name, (passed, errors) in results.items()
        }
    }
    
    # Save report
    report_path = FRAMEWORK_ROOT / "tests" / "integration" / "test_report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📄 Test report saved: {report_path}")
    
    # Exit with appropriate code
    exit_code = 0 if report["failed"] == 0 else 1
    exit(exit_code)


if __name__ == "__main__":
    main()