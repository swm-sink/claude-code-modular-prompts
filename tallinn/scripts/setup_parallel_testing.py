#!/usr/bin/env python3
"""
Setup parallel testing infrastructure for faster test execution.
"""

import subprocess
import sys
from pathlib import Path

def setup_parallel_testing():
    """Setup pytest-xdist for parallel test execution."""
    print("🚀 Setting up parallel testing infrastructure...")
    print("=" * 60)
    
    # Check if pytest-xdist is installed
    try:
        import pytest_xdist
        print("✅ pytest-xdist is already installed")
    except ImportError:
        print("📦 Installing pytest-xdist for parallel testing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest-xdist"])
            print("✅ pytest-xdist installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install pytest-xdist: {e}")
            return False
    
    # Update pytest.ini to include parallel testing options
    project_root = Path(__file__).parent.parent
    pytest_ini = project_root / "pytest.ini"
    
    if pytest_ini.exists():
        content = pytest_ini.read_text()
        
        # Check if parallel options already exist
        if "-n auto" not in content:
            print("\n📝 Updating pytest.ini with parallel testing options...")
            
            # Find the addopts line
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('addopts'):
                    # Check if we need to add -n auto
                    if '-n' not in line:
                        # Add parallel execution to existing addopts
                        if line.strip().endswith('='):
                            lines[i] = line + ' -n auto'
                        else:
                            lines[i] = line.rstrip() + ' -n auto'
                        print("✅ Added parallel execution flag to pytest.ini")
                        break
            
            # Write back
            pytest_ini.write_text('\n'.join(lines))
    
    # Create a parallel test runner script
    runner_script = project_root / "run_tests_parallel.py"
    runner_content = '''#!/usr/bin/env python3
"""
Run tests in parallel for faster execution.
"""

import subprocess
import sys
import argparse
from pathlib import Path

def run_tests(args):
    """Run tests with parallel execution."""
    cmd = [sys.executable, "-m", "pytest"]
    
    # Add parallel execution
    if args.workers:
        cmd.extend(["-n", str(args.workers)])
    else:
        cmd.extend(["-n", "auto"])
    
    # Add coverage if requested
    if args.coverage:
        cmd.extend(["--cov=.", "--cov-report=term-missing", "--cov-report=html"])
    
    # Add verbosity
    if args.verbose:
        cmd.append("-v")
    
    # Add test path if specified
    if args.path:
        cmd.append(args.path)
    
    # Add any additional pytest args
    if args.pytest_args:
        cmd.extend(args.pytest_args)
    
    print(f"Running: {' '.join(cmd)}")
    print("=" * 60)
    
    result = subprocess.run(cmd)
    return result.returncode

def main():
    parser = argparse.ArgumentParser(description="Run tests in parallel")
    parser.add_argument("-n", "--workers", type=int, help="Number of workers (default: auto)")
    parser.add_argument("-c", "--coverage", action="store_true", help="Run with coverage")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("path", nargs="?", help="Test path to run")
    parser.add_argument("pytest_args", nargs="*", help="Additional pytest arguments")
    
    args = parser.parse_args()
    
    return run_tests(args)

if __name__ == "__main__":
    sys.exit(main())
'''
    
    runner_script.write_text(runner_content)
    runner_script.chmod(0o755)
    print(f"\n✅ Created parallel test runner: {runner_script}")
    
    # Test the setup
    print("\n🧪 Testing parallel execution setup...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "--collect-only", "-q"],
            capture_output=True,
            text=True
        )
        test_count = len([line for line in result.stdout.split('\n') if 'test' in line and '::' in line])
        print(f"✅ Found {test_count} tests ready for parallel execution")
    except Exception as e:
        print(f"⚠️ Could not verify test collection: {e}")
    
    print("\n📊 Parallel testing setup complete!")
    print("\nUsage:")
    print("  - Run all tests in parallel: python3 run_tests_parallel.py")
    print("  - Run with coverage: python3 run_tests_parallel.py -c")
    print("  - Run specific tests: python3 run_tests_parallel.py tests/unit/")
    print("  - Specify workers: python3 run_tests_parallel.py -n 4")
    
    return True

if __name__ == "__main__":
    setup_parallel_testing()