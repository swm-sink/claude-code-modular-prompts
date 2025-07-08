#!/usr/bin/env python3
"""
Framework Health Monitoring Script
Monitors the Claude Code framework for potential issues that could cause maintenance failures.
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime

class FrameworkHealthMonitor:
    def __init__(self, root_path="."):
        self.root_path = Path(root_path)
        self.issues = []
        self.warnings = []
        
    def check_directory_structure(self):
        """Check required directories exist"""
        required_dirs = [
            ".claude",
            ".claude/commands",
            ".claude/modules",
            ".github/workflows",
            "tests",
            "scripts",
            "docs"
        ]
        
        for dir_path in required_dirs:
            full_path = self.root_path / dir_path
            if not full_path.exists():
                self.issues.append(f"Missing required directory: {dir_path}")
            elif not full_path.is_dir():
                self.issues.append(f"Path exists but is not a directory: {dir_path}")
                
    def check_framework_files(self):
        """Check critical framework files exist"""
        critical_files = [
            "CLAUDE.md",
            ".github/workflows/claude.yml",
            "scripts/validate.py",
            "scripts/health_check.py"
        ]
        
        for file_path in critical_files:
            full_path = self.root_path / file_path
            if not full_path.exists():
                self.issues.append(f"Missing critical file: {file_path}")
                
    def check_optional_directories(self):
        """Check optional directories and warn if missing"""
        optional_dirs = ["src", "lib", "bin"]
        
        for dir_path in optional_dirs:
            full_path = self.root_path / dir_path
            if not full_path.exists():
                self.warnings.append(f"Optional directory missing (may affect some tools): {dir_path}")
                
    def check_framework_version(self):
        """Verify framework version consistency"""
        claude_md = self.root_path / "CLAUDE.md"
        workflow = self.root_path / ".github/workflows/claude.yml"
        
        expected_version = "v7.0.0-EMPIRICAL-REALITY-ALIGNED"
        
        if claude_md.exists():
            with open(claude_md, 'r') as f:
                content = f.read()
                if expected_version not in content:
                    self.warnings.append(f"CLAUDE.md may not have current framework version: {expected_version}")
                    
        if workflow.exists():
            with open(workflow, 'r') as f:
                content = f.read()
                if expected_version not in content:
                    self.issues.append(f"Workflow has incorrect framework version, expected: {expected_version}")
                    
    def check_test_health(self):
        """Check if tests are runnable"""
        test_dir = self.root_path / "tests"
        if test_dir.exists():
            test_files = list(test_dir.rglob("test_*.py"))
            if not test_files:
                self.warnings.append("No test files found in tests directory")
            else:
                # Check for __init__.py files
                for subdir in test_dir.iterdir():
                    if subdir.is_dir() and not (subdir / "__init__.py").exists():
                        self.warnings.append(f"Missing __init__.py in test directory: {subdir.name}")
                        
    def generate_report(self):
        """Generate health monitoring report"""
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "framework_health": "HEALTHY" if not self.issues else "UNHEALTHY",
            "issues_count": len(self.issues),
            "warnings_count": len(self.warnings),
            "issues": self.issues,
            "warnings": self.warnings,
            "recommendations": []
        }
        
        # Add recommendations based on issues
        if self.issues:
            report["recommendations"].append("Fix critical issues before running maintenance workflow")
            
        if any("src/" in warning for warning in self.warnings):
            report["recommendations"].append("Consider creating src/ directory or updating security scan configuration")
            
        return report
        
    def run(self):
        """Run all health checks"""
        print("🔍 Running Framework Health Monitoring...")
        
        self.check_directory_structure()
        self.check_framework_files()
        self.check_optional_directories()
        self.check_framework_version()
        self.check_test_health()
        
        report = self.generate_report()
        
        # Display results
        print(f"\n📊 Health Status: {report['framework_health']}")
        print(f"Issues: {report['issues_count']}")
        print(f"Warnings: {report['warnings_count']}")
        
        if self.issues:
            print("\n❌ Critical Issues:")
            for issue in self.issues:
                print(f"  - {issue}")
                
        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"  - {warning}")
                
        if report["recommendations"]:
            print("\n💡 Recommendations:")
            for rec in report["recommendations"]:
                print(f"  - {rec}")
                
        # Save report
        report_path = self.root_path / f"framework-health-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
            
        print(f"\n📄 Full report saved to: {report_path}")
        
        # Exit with error if unhealthy
        if report['framework_health'] == "UNHEALTHY":
            sys.exit(1)
            
if __name__ == "__main__":
    monitor = FrameworkHealthMonitor()
    monitor.run()