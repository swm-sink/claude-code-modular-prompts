#!/usr/bin/env python3
"""
Environment Validation Script for Claude Code Modular Prompts Framework
Agent V28 - Environment Configuration Tester
Created: 2025-07-13
"""

import sys
import os
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class EnvironmentValidator:
    """Validates the development environment for the framework."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.successes = []
        self.framework_root = Path(__file__).parent.parent
        
    def run_command(self, cmd: List[str]) -> Tuple[bool, str]:
        """Run a command and return success status and output."""
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode == 0, result.stdout.strip()
        except FileNotFoundError:
            return False, f"Command not found: {cmd[0]}"
        except Exception as e:
            return False, str(e)
    
    def check_python(self) -> None:
        """Check Python installation and version."""
        success, output = self.run_command(["python3", "--version"])
        if success:
            version = output.split()[1]
            major, minor = map(int, version.split('.')[:2])
            if major >= 3 and minor >= 8:
                self.successes.append(f"✓ Python {version} installed")
            else:
                self.warnings.append(f"⚠ Python {version} found, recommend 3.8+")
        else:
            self.errors.append("✗ Python 3 not found")
    
    def check_git(self) -> None:
        """Check Git installation and configuration."""
        success, output = self.run_command(["git", "--version"])
        if success:
            self.successes.append(f"✓ {output}")
        else:
            self.errors.append("✗ Git not found")
            
        # Check git user configuration
        success, name = self.run_command(["git", "config", "user.name"])
        success2, email = self.run_command(["git", "config", "user.email"])
        if success and success2:
            self.successes.append(f"✓ Git configured: {name} <{email}>")
        else:
            self.warnings.append("⚠ Git user not fully configured")
    
    def check_claude_code(self) -> None:
        """Check Claude Code installation."""
        # First try direct command
        success, output = self.run_command(["claude", "--version"])
        if success:
            self.successes.append(f"✓ Claude Code installed: {output}")
            return
            
        # Check if it's an alias by trying through bash
        success, output = self.run_command(["bash", "-c", "claude --version 2>&1"])
        if success and "Claude Code" in output:
            self.successes.append(f"✓ Claude Code installed (alias): {output}")
            return
            
        # Check common installation paths
        common_paths = [
            Path.home() / ".claude" / "local" / "claude",
            Path("/usr/local/bin/claude"),
            Path("/opt/homebrew/bin/claude")
        ]
        
        for path in common_paths:
            if path.exists():
                self.successes.append(f"✓ Claude Code binary found at: {path}")
                return
                
        self.errors.append("✗ Claude Code not found")
    
    def check_python_packages(self) -> None:
        """Check required Python packages."""
        required_packages = ["pytest", "pytest-cov", "coverage"]
        
        for package in required_packages:
            success, output = self.run_command(["python3", "-m", "pip", "show", package])
            if success:
                version = [line.split(': ')[1] for line in output.split('\n') if line.startswith('Version:')][0]
                self.successes.append(f"✓ {package} {version} installed")
            else:
                self.warnings.append(f"⚠ {package} not installed")
    
    def check_framework_structure(self) -> None:
        """Check framework directory structure."""
        required_dirs = [
            ".claude",
            ".claude/commands",
            ".claude/modules",
            ".claude/system",
            ".claude/prompt_eng",
            ".claude/meta",
            ".claude/domain",
            "scripts",
            "tests",
            "docs"
        ]
        
        for dir_path in required_dirs:
            full_path = self.framework_root / dir_path
            if full_path.exists() and full_path.is_dir():
                self.successes.append(f"✓ Directory exists: {dir_path}")
            else:
                self.errors.append(f"✗ Missing directory: {dir_path}")
    
    def check_environment_variables(self) -> None:
        """Check environment variables."""
        claude_vars = [var for var in os.environ if var.startswith("CLAUDE")]
        
        if claude_vars:
            self.successes.append(f"✓ Found {len(claude_vars)} Claude environment variables")
            for var in claude_vars:
                self.successes.append(f"  • {var}: {os.environ[var][:50]}...")
        else:
            self.warnings.append("⚠ No Claude-specific environment variables found")
    
    def check_optional_tools(self) -> None:
        """Check optional but recommended tools."""
        optional_tools = {
            "node": "Node.js",
            "npm": "NPM",
            "rg": "ripgrep",
            "tree": "tree",
            "jq": "jq"
        }
        
        for cmd, name in optional_tools.items():
            success, output = self.run_command([cmd, "--version"])
            if success:
                self.successes.append(f"✓ {name} installed")
            else:
                self.warnings.append(f"⚠ {name} not found (optional)")
    
    def validate_all(self) -> Dict[str, List[str]]:
        """Run all validation checks."""
        print("🔍 Validating Claude Code Modular Prompts Framework Environment...\n")
        
        self.check_python()
        self.check_git()
        self.check_claude_code()
        self.check_python_packages()
        self.check_framework_structure()
        self.check_environment_variables()
        self.check_optional_tools()
        
        return {
            "errors": self.errors,
            "warnings": self.warnings,
            "successes": self.successes
        }
    
    def print_report(self, results: Dict[str, List[str]]) -> int:
        """Print validation report and return exit code."""
        print("\n📊 VALIDATION REPORT")
        print("=" * 50)
        
        # Print successes
        if results["successes"]:
            print(f"\n✅ PASSED ({len(results['successes'])} checks)")
            for success in results["successes"]:
                print(f"   {success}")
        
        # Print warnings
        if results["warnings"]:
            print(f"\n⚠️  WARNINGS ({len(results['warnings'])} issues)")
            for warning in results["warnings"]:
                print(f"   {warning}")
        
        # Print errors
        if results["errors"]:
            print(f"\n❌ ERRORS ({len(results['errors'])} issues)")
            for error in results["errors"]:
                print(f"   {error}")
        
        # Summary
        print("\n" + "=" * 50)
        total_checks = len(results["successes"]) + len(results["warnings"]) + len(results["errors"])
        success_rate = (len(results["successes"]) / total_checks * 100) if total_checks > 0 else 0
        
        if results["errors"]:
            print(f"❌ Environment validation FAILED ({success_rate:.1f}% success rate)")
            print("   Please fix the errors above before proceeding.")
            return 1
        elif results["warnings"]:
            print(f"⚠️  Environment validation PASSED with warnings ({success_rate:.1f}% success rate)")
            print("   Consider addressing the warnings for optimal functionality.")
            return 0
        else:
            print(f"✅ Environment validation PASSED ({success_rate:.1f}% success rate)")
            print("   Your environment is properly configured!")
            return 0


def main():
    """Main entry point."""
    validator = EnvironmentValidator()
    results = validator.validate_all()
    exit_code = validator.print_report(results)
    
    # Save results to JSON for programmatic access
    results_file = Path(__file__).parent / "environment-validation-results.json"
    with open(results_file, 'w') as f:
        json.dump({
            "timestamp": str(Path(__file__).stat().st_mtime),
            "results": results,
            "exit_code": exit_code
        }, f, indent=2)
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())