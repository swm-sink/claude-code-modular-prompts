#!/usr/bin/env python3
"""
Test script for /prompt command functionality
Tests command structure, delegation pattern, and parameter parsing
"""

import json
import os
import xml.etree.ElementTree as ET
from pathlib import Path


class PromptCommandTester:
    """Test harness for /prompt command validation"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.command_path = self.base_path / "commands" / "prompt.md"
        self.module_path = self.base_path / "modules" / "development" / "prompt-engineering.md"
        self.results = {"passed": 0, "failed": 0, "errors": []}
    
    def run_all_tests(self):
        """Execute all test cases"""
        print("🧪 Testing /prompt Command Implementation\n")
        
        # Test 1: Command file exists
        self.test_command_file_exists()
        
        # Test 2: Module file exists
        self.test_module_file_exists()
        
        # Test 3: Command follows delegation pattern
        self.test_delegation_pattern()
        
        # Test 4: Command structure validity
        self.test_command_structure()
        
        # Test 5: Module structure validity
        self.test_module_structure()
        
        # Test 6: Subcommands defined
        self.test_subcommands()
        
        # Test 7: Parameter definitions
        self.test_parameters()
        
        # Test 8: Integration hooks
        self.test_integration_hooks()
        
        # Test 9: Error handling
        self.test_error_handling()
        
        # Test 10: End-to-end workflow
        self.test_end_to_end_workflow()
        
        self.print_results()
    
    def test_command_file_exists(self):
        """Test 1: Verify command file exists"""
        try:
            assert self.command_path.exists(), f"Command file not found: {self.command_path}"
            self.results["passed"] += 1
            print("✅ Test 1: Command file exists")
        except AssertionError as e:
            self.results["failed"] += 1
            self.results["errors"].append(str(e))
            print(f"❌ Test 1: {e}")
    
    def test_module_file_exists(self):
        """Test 2: Verify module file exists"""
        try:
            assert self.module_path.exists(), f"Module file not found: {self.module_path}"
            self.results["passed"] += 1
            print("✅ Test 2: Module file exists")
        except AssertionError as e:
            self.results["failed"] += 1
            self.results["errors"].append(str(e))
            print(f"❌ Test 2: {e}")
    
    def test_delegation_pattern(self):
        """Test 3: Verify command follows delegation pattern"""
        try:
            content = self.command_path.read_text()
            # Check for delegation tag
            assert "<delegation target=" in content, "Missing delegation tag"
            assert "modules/development/prompt-engineering.md" in content, "Incorrect delegation target"
            # Verify no implementation in command
            assert "def " not in content, "Command contains implementation (should only delegate)"
            assert "class " not in content, "Command contains implementation (should only delegate)"
            self.results["passed"] += 1
            print("✅ Test 3: Command follows delegation pattern")
        except AssertionError as e:
            self.results["failed"] += 1
            self.results["errors"].append(str(e))
            print(f"❌ Test 3: {e}")
    
    def test_command_structure(self):
        """Test 4: Validate command XML structure"""
        try:
            content = self.command_path.read_text()
            # Parse as XML
            root = ET.fromstring(content)
            
            # Check required elements
            assert root.tag == "command", "Root element must be 'command'"
            assert root.get("purpose"), "Command must have purpose attribute"
            
            # Check for required sections
            required_sections = ["delegation", "module_integration", "subcommands", 
                               "usage_examples", "parameters", "reference"]
            for section in required_sections:
                elements = root.findall(f".//{section}")
                assert elements, f"Missing required section: {section}"
            
            self.results["passed"] += 1
            print("✅ Test 4: Command structure valid")
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Command structure error: {e}")
            print(f"❌ Test 4: Command structure error: {e}")
    
    def test_module_structure(self):
        """Test 5: Validate module XML structure"""
        try:
            content = self.module_path.read_text()
            # Parse as XML
            root = ET.fromstring(content)
            
            # Check required elements
            assert root.tag == "module", "Root element must be 'module'"
            assert root.get("name") == "prompt-engineering", "Module name mismatch"
            assert root.get("version"), "Module must have version"
            
            # Check for implementation section
            impl = root.find(".//implementation")
            assert impl is not None, "Missing implementation section"
            
            self.results["passed"] += 1
            print("✅ Test 5: Module structure valid")
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Module structure error: {e}")
            print(f"❌ Test 5: Module structure error: {e}")
    
    def test_subcommands(self):
        """Test 6: Verify all subcommands are defined"""
        try:
            content = self.command_path.read_text()
            root = ET.fromstring(content)
            
            # Find all subcommands
            subcommands = root.findall(".//subcommand")
            subcommand_names = [sc.get("name") for sc in subcommands]
            
            # Verify required subcommands
            required = ["create", "evaluate", "test", "improve"]
            for req in required:
                assert req in subcommand_names, f"Missing subcommand: {req}"
            
            self.results["passed"] += 1
            print("✅ Test 6: All subcommands defined")
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Subcommand error: {e}")
            print(f"❌ Test 6: Subcommand error: {e}")
    
    def test_parameters(self):
        """Test 7: Verify parameter definitions"""
        try:
            content = self.command_path.read_text()
            root = ET.fromstring(content)
            
            # Find all parameters
            parameters = root.findall(".//parameter")
            param_names = [p.get("name") for p in parameters]
            
            # Verify key parameters
            expected_params = ["--type", "--framework", "--style", "--metrics"]
            for param in expected_params:
                assert param in param_names, f"Missing parameter: {param}"
            
            # Check parameter attributes
            for param in parameters:
                assert param.get("values") or param.get("default"), f"Parameter {param.get('name')} missing values or default"
            
            self.results["passed"] += 1
            print("✅ Test 7: Parameters properly defined")
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Parameter error: {e}")
            print(f"❌ Test 7: Parameter error: {e}")
    
    def test_integration_hooks(self):
        """Test 8: Verify integration hooks"""
        try:
            content = self.command_path.read_text()
            root = ET.fromstring(content)
            
            # Find integration hooks
            hooks = root.findall(".//hook")
            hook_types = [h.get("type") for h in hooks]
            
            # Verify key hooks
            expected_hooks = ["pre_create", "post_create", "pre_test", "post_test"]
            for hook in expected_hooks:
                assert hook in hook_types, f"Missing integration hook: {hook}"
            
            self.results["passed"] += 1
            print("✅ Test 8: Integration hooks defined")
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Integration hook error: {e}")
            print(f"❌ Test 8: Integration hook error: {e}")
    
    def test_error_handling(self):
        """Test 9: Verify error handling definitions"""
        try:
            content = self.module_path.read_text()
            root = ET.fromstring(content)
            
            # Find error handling section
            error_section = root.find(".//error_handling")
            assert error_section is not None, "Missing error handling section"
            
            # Check for error types
            errors = error_section.findall(".//error")
            error_types = [e.get("type") for e in errors]
            
            expected_errors = ["invalid_subcommand", "missing_parameters", "file_not_found"]
            for err in expected_errors:
                assert err in error_types, f"Missing error handling for: {err}"
            
            self.results["passed"] += 1
            print("✅ Test 9: Error handling implemented")
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Error handling error: {e}")
            print(f"❌ Test 9: Error handling error: {e}")
    
    def test_end_to_end_workflow(self):
        """Test 10: Verify end-to-end workflow completeness"""
        try:
            content = self.module_path.read_text()
            root = ET.fromstring(content)
            
            # Find workflow phases
            phases = root.findall(".//phase")
            phase_names = [p.get("name") for p in phases]
            
            # Verify all workflow phases
            expected_phases = ["initialization", "create", "evaluate", "test", "improve"]
            for phase in expected_phases:
                assert phase in phase_names, f"Missing workflow phase: {phase}"
            
            # Check phase order
            phase_orders = [(p.get("name"), int(p.get("order", 0))) for p in phases]
            phase_orders.sort(key=lambda x: x[1])
            
            assert phase_orders[0][0] == "initialization", "Initialization must be first phase"
            
            self.results["passed"] += 1
            print("✅ Test 10: End-to-end workflow complete")
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Workflow error: {e}")
            print(f"❌ Test 10: Workflow error: {e}")
    
    def print_results(self):
        """Print test summary"""
        total = self.results["passed"] + self.results["failed"]
        print(f"\n{'='*50}")
        print(f"Test Results: {self.results['passed']}/{total} passed")
        print(f"{'='*50}")
        
        if self.results["failed"] > 0:
            print("\n❌ Failed Tests:")
            for error in self.results["errors"]:
                print(f"  - {error}")
        else:
            print("\n✅ All tests passed! /prompt command is ready for use.")
        
        # Save results
        results_file = self.base_path / "tests" / "prompt_command_test_results.json"
        with open(results_file, "w") as f:
            json.dump(self.results, f, indent=2)
        print(f"\nResults saved to: {results_file}")


if __name__ == "__main__":
    tester = PromptCommandTester()
    tester.run_all_tests()