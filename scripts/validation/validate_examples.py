#!/usr/bin/env python3
"""
Validate code examples in documentation.
Run this script regularly to ensure examples remain valid.
"""

import subprocess
import sys
import os

def main():
    """Run example validation pipeline."""
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=== Code Example Validation ===")
    print()
    
    # Step 1: Extract examples
    print("Step 1: Extracting code examples from documentation...")
    result = subprocess.run([
        sys.executable,
        os.path.join(scripts_dir, 'extract_code_examples.py')
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error extracting examples: {result.stderr}")
        return 1
    
    # Step 2: Validate examples
    print("\nStep 2: Validating code examples...")
    result = subprocess.run([
        sys.executable,
        os.path.join(scripts_dir, 'validate_code_examples.py')
    ], capture_output=True, text=True)
    
    # Show results regardless of return code
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    # Step 3: Generate report
    print("\nStep 3: Generating validation report...")
    result = subprocess.run([
        sys.executable,
        os.path.join(scripts_dir, 'mark_broken_examples.py')
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Validation complete! Check example_fixes_needed.md for details.")
    else:
        print(f"Error generating report: {result.stderr}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
