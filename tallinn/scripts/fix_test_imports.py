#!/usr/bin/env python3
"""
Fix test import issues by adding __init__.py files and updating sys.path in tests.
"""

import os
from pathlib import Path

def create_init_files():
    """Create __init__.py files in necessary directories."""
    project_root = Path(__file__).parent.parent
    
    # Directories that need __init__.py
    dirs_needing_init = [
        project_root,
        project_root / "security",
        project_root / "performance",
        project_root / "scripts",
        project_root / "tests",
        project_root / "tests" / "unit",
        project_root / "tests" / "integration",
        project_root / "tests" / "e2e",
    ]
    
    for dir_path in dirs_needing_init:
        if dir_path.exists() and dir_path.is_dir():
            init_file = dir_path / "__init__.py"
            if not init_file.exists():
                init_file.write_text("# This file makes the directory a Python package\n")
                print(f"Created: {init_file}")

def main():
    """Main execution."""
    print("Fixing test import issues...")
    create_init_files()
    print("Done!")

if __name__ == "__main__":
    main()