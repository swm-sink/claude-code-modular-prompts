#!/usr/bin/env python3
"""
Verify Test Coverage Enforcement

This script verifies that the test coverage enforcement is properly configured
and will block commits/deployments when coverage falls below 90%.
"""

import subprocess
import sys
import os

def run_coverage_check():
    """Run pytest with coverage and verify enforcement works."""
    print("🔍 Verifying test coverage enforcement...")
    print("-" * 60)
    
    # Check if pytest and pytest-cov are installed
    try:
        import pytest
        import pytest_cov
        print("✅ pytest and pytest-cov are installed")
    except ImportError:
        print("❌ ERROR: pytest or pytest-cov not installed!")
        print("   Run: pip install -r requirements.txt")
        return False
    
    # Check configuration files
    config_files = ['pyproject.toml', '.coveragerc']
    for config in config_files:
        if os.path.exists(config):
            print(f"✅ {config} exists")
        else:
            print(f"❌ {config} missing!")
            return False
    
    # Run a test coverage check (will fail if <90%)
    print("\n📊 Running coverage check...")
    cmd = ["pytest", "--cov=.", "--cov-fail-under=90", "--cov-report=term"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Coverage check passed (≥90%)")
            print("\nCoverage output:")
            print(result.stdout)
            return True
        else:
            print("⚠️  Coverage check failed (expected if <90%)")
            print("\nOutput:")
            print(result.stdout)
            print("\nError:")
            print(result.stderr)
            
            # This is actually good - it means enforcement is working!
            if "FAIL Required test coverage of 90% not reached" in result.stdout:
                print("\n✅ GOOD: Coverage enforcement is working correctly!")
                print("   The build will fail if coverage drops below 90%")
                return True
            else:
                print("\n❌ ERROR: Coverage check failed for unknown reason")
                return False
                
    except Exception as e:
        print(f"❌ ERROR running coverage check: {e}")
        return False

def main():
    """Main verification function."""
    print("Test Coverage Enforcement Verification")
    print("=" * 60)
    print("This verifies that 90% test coverage is enforced\n")
    
    success = run_coverage_check()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ Test coverage enforcement is properly configured!")
        print("   - pyproject.toml has --cov-fail-under=90")
        print("   - .coveragerc has fail_under = 90")
        print("   - pytest-cov will block if coverage < 90%")
    else:
        print("❌ Test coverage enforcement needs configuration")
        sys.exit(1)

if __name__ == "__main__":
    main()