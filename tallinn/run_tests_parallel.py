#!/usr/bin/env python3
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
