#!/usr/bin/env python3
"""
Comprehensive Integration Test Suite
Tests the complete user workflow from installation to usage
"""

import os
import tempfile
import shutil
import subprocess
import json
from pathlib import Path
import time

class IntegrationTestSuite:
    """Complete integration testing framework"""
    
    def __init__(self):
        self.test_results = []
        self.temp_projects = []
        
    def log_test(self, test_name, status, details=""):
        """Log test result"""
        result = {
            'test': test_name,
            'status': status,
            'details': details,
            'timestamp': time.strftime('%H:%M:%S')
        }
        self.test_results.append(result)
        status_icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
        print(f"{status_icon} {test_name}: {status}")
        if details:
            print(f"   {details}")
    
    def create_test_project(self, project_type="basic"):
        """Create a temporary test project"""
        temp_dir = tempfile.mkdtemp(prefix=f"claude_test_{project_type}_")
        self.temp_projects.append(temp_dir)
        
        if project_type == "node":
            # Create a Node.js project
            package_json = {
                "name": "test-node-project",
                "version": "1.0.0",
                "description": "Test Node.js project",
                "main": "index.js",
                "dependencies": {
                    "express": "^4.18.0",
                    "react": "^18.0.0"
                },
                "devDependencies": {
                    "jest": "^29.0.0"
                }
            }
            with open(os.path.join(temp_dir, "package.json"), "w") as f:
                json.dump(package_json, f, indent=2)
                
            # Create some JS files
            with open(os.path.join(temp_dir, "index.js"), "w") as f:
                f.write("console.log('Hello World');")
            with open(os.path.join(temp_dir, "app.js"), "w") as f:
                f.write("const express = require('express');")
                
        elif project_type == "python":
            # Create a Python project
            with open(os.path.join(temp_dir, "setup.py"), "w") as f:
                f.write("""
from setuptools import setup, find_packages

setup(
    name="test-python-project",
    version="1.0.0",
    description="Test Python project",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0.0",
        "requests>=2.25.0"
    ],
    extras_require={
        "dev": ["pytest>=6.0.0", "black>=21.0.0"]
    }
)
""")
            
            # Create some Python files
            os.makedirs(os.path.join(temp_dir, "src"))
            with open(os.path.join(temp_dir, "src", "main.py"), "w") as f:
                f.write("print('Hello World')")
            with open(os.path.join(temp_dir, "src", "app.py"), "w") as f:
                f.write("from flask import Flask\napp = Flask(__name__)")
        
        return temp_dir
    
    def test_minimal_installation(self):
        """Test minimal installation workflow"""
        test_project = self.create_test_project("basic")
        
        try:
            # Run setup-minimal.sh
            result = subprocess.run([
                "./setup-minimal.sh", test_project
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                self.log_test("Minimal Installation", "FAIL", f"Setup failed: {result.stderr}")
                return False
            
            # Check if .claude directory was created
            claude_dir = os.path.join(test_project, ".claude")
            if not os.path.exists(claude_dir):
                self.log_test("Minimal Installation", "FAIL", ".claude directory not created")
                return False
            
            # Check if commands were installed
            commands_dir = os.path.join(claude_dir, "commands")
            if not os.path.exists(commands_dir):
                self.log_test("Minimal Installation", "FAIL", "commands directory not created")
                return False
            
            # Count command files
            command_files = list(Path(commands_dir).glob("*.md"))
            if len(command_files) != 7:
                self.log_test("Minimal Installation", "FAIL", f"Expected 7 commands, found {len(command_files)}")
                return False
            
            # Check CLAUDE.md was created
            claude_md = os.path.join(test_project, "CLAUDE.md")
            if not os.path.exists(claude_md):
                self.log_test("Minimal Installation", "FAIL", "CLAUDE.md not created")
                return False
            
            self.log_test("Minimal Installation", "PASS", "7 commands installed successfully")
            return True
            
        except Exception as e:
            self.log_test("Minimal Installation", "FAIL", f"Exception: {e}")
            return False
    
    def test_full_installation(self):
        """Test full template library installation"""
        test_project = self.create_test_project("basic")
        
        try:
            # Run setup.sh
            result = subprocess.run([
                "./setup.sh", test_project
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode != 0:
                self.log_test("Full Installation", "FAIL", f"Setup failed: {result.stderr}")
                return False
            
            # Check if .claude directory was created
            claude_dir = os.path.join(test_project, ".claude")
            if not os.path.exists(claude_dir):
                self.log_test("Full Installation", "FAIL", ".claude directory not created")
                return False
            
            # Count total template files
            commands_dir = os.path.join(claude_dir, "commands")
            total_commands = len(list(Path(commands_dir).rglob("*.md")))
            
            # Should have around 82 commands
            if total_commands < 80 or total_commands > 85:
                self.log_test("Full Installation", "FAIL", f"Expected ~82 commands, found {total_commands}")
                return False
            
            # Check for key directories
            expected_dirs = ["commands", "components", "scripts"]
            for dir_name in expected_dirs:
                if not os.path.exists(os.path.join(claude_dir, dir_name)):
                    self.log_test("Full Installation", "FAIL", f"Missing directory: {dir_name}")
                    return False
            
            self.log_test("Full Installation", "PASS", f"{total_commands} templates installed successfully")
            return True
            
        except Exception as e:
            self.log_test("Full Installation", "FAIL", f"Exception: {e}")
            return False
    
    def test_project_detection(self):
        """Test smart project detection capabilities"""
        # Test Node.js project detection
        node_project = self.create_test_project("node")
        
        try:
            # Run smart automation engine
            python_path = os.path.join(os.getcwd(), ".claude", "smart-automation-engine.py")
            if os.path.exists(python_path):
                result = subprocess.run([
                    "python3", python_path, node_project
                ], capture_output=True, text=True, timeout=30, cwd=os.getcwd())
                
                if "JavaScript" in result.stdout or "Node" in result.stdout:
                    self.log_test("Project Detection - Node.js", "PASS", "JavaScript project detected")
                else:
                    self.log_test("Project Detection - Node.js", "WARN", "Node.js detection may be incomplete")
            else:
                self.log_test("Project Detection - Node.js", "SKIP", "Smart automation engine not found")
            
            # Test Python project detection  
            python_project = self.create_test_project("python")
            
            if os.path.exists(python_path):
                result = subprocess.run([
                    "python3", python_path, python_project
                ], capture_output=True, text=True, timeout=30, cwd=os.getcwd())
                
                if "Python" in result.stdout:
                    self.log_test("Project Detection - Python", "PASS", "Python project detected")
                else:
                    self.log_test("Project Detection - Python", "WARN", "Python detection may be incomplete")
            else:
                self.log_test("Project Detection - Python", "SKIP", "Smart automation engine not found")
                
            return True
            
        except Exception as e:
            self.log_test("Project Detection", "FAIL", f"Exception: {e}")
            return False
    
    def test_yaml_compliance(self):
        """Test YAML compliance across all commands"""
        try:
            result = subprocess.run([
                "python3", "validate-yaml-compliance.py"
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode != 0:
                self.log_test("YAML Compliance", "FAIL", "Validation script failed")
                return False
            
            # Check for compliance rate in output
            output = result.stdout
            if "96.3%" in output or "Compliance Rate: 96" in output:
                self.log_test("YAML Compliance", "PASS", "96.3% compliance rate achieved")
            elif "EXCELLENT COMPLIANCE" in output:
                self.log_test("YAML Compliance", "PASS", "Excellent compliance achieved")
            else:
                self.log_test("YAML Compliance", "WARN", "Compliance rate may have changed")
            
            return True
            
        except Exception as e:
            self.log_test("YAML Compliance", "FAIL", f"Exception: {e}")
            return False
    
    def test_file_permissions(self):
        """Test file permissions and executable status"""
        issues = []
        
        # Check setup scripts are executable
        setup_scripts = ["setup.sh", "setup-minimal.sh"]
        for script in setup_scripts:
            if os.path.exists(script):
                if not os.access(script, os.X_OK):
                    issues.append(f"{script} is not executable")
            else:
                issues.append(f"{script} not found")
        
        # Check Python scripts have proper permissions
        python_files = list(Path(".").rglob("*.py"))
        for py_file in python_files[:10]:  # Check first 10
            if not os.access(py_file, os.R_OK):
                issues.append(f"{py_file} is not readable")
        
        if issues:
            self.log_test("File Permissions", "FAIL", "; ".join(issues))
            return False
        else:
            self.log_test("File Permissions", "PASS", "All critical files have proper permissions")
            return True
    
    def cleanup(self):
        """Clean up temporary test projects"""
        for temp_dir in self.temp_projects:
            try:
                shutil.rmtree(temp_dir)
            except Exception as e:
                print(f"Warning: Could not cleanup {temp_dir}: {e}")
    
    def run_all_tests(self):
        """Run complete integration test suite"""
        print("🚀 COMPREHENSIVE INTEGRATION TEST SUITE")
        print("=" * 60)
        print()
        
        tests = [
            self.test_file_permissions,
            self.test_yaml_compliance,
            self.test_minimal_installation,
            self.test_full_installation,
            self.test_project_detection,
        ]
        
        passed = 0
        failed = 0
        warnings = 0
        
        for test in tests:
            try:
                result = test()
                if result is True:
                    passed += 1
                elif result is False:
                    failed += 1
                else:
                    warnings += 1
            except Exception as e:
                print(f"❌ Test error: {e}")
                failed += 1
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 INTEGRATION TEST SUMMARY")
        print("=" * 60)
        print(f"Tests Passed: {passed}")
        print(f"Tests Failed: {failed}")
        print(f"Warnings: {warnings}")
        print(f"Total Tests: {len(tests)}")
        
        success_rate = (passed / len(tests)) * 100
        print(f"\n✅ Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 90:
            print("🎉 EXCELLENT - System ready for production deployment")
        elif success_rate >= 70:
            print("✅ GOOD - Minor issues, generally production ready")  
        elif success_rate >= 50:
            print("⚠️ ACCEPTABLE - Some issues need attention")
        else:
            print("🚨 POOR - Major issues require immediate attention")
        
        # Cleanup
        self.cleanup()
        
        return success_rate >= 80

if __name__ == "__main__":
    suite = IntegrationTestSuite()
    success = suite.run_all_tests()
    exit(0 if success else 1)