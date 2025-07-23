#!/usr/bin/env python3
"""
Fix import errors in test files by analyzing and adding missing imports.

This script:
1. Identifies missing imports in test files
2. Adds the required imports
3. Ensures proper module path setup
"""

import os
import ast
import sys
from pathlib import Path
from typing import Set, List, Dict, Tuple

class ImportAnalyzer(ast.NodeVisitor):
    """Analyze Python files to find undefined names that need imports."""
    
    def __init__(self):
        self.undefined_names: Set[str] = set()
        self.defined_names: Set[str] = set()
        self.imported_names: Set[str] = set()
        
    def visit_Import(self, node):
        """Track regular imports."""
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self.imported_names.add(name.split('.')[0])
        self.generic_visit(node)
        
    def visit_ImportFrom(self, node):
        """Track from imports."""
        for alias in node.names:
            name = alias.asname if alias.asname else alias.name
            self.imported_names.add(name)
        self.generic_visit(node)
        
    def visit_FunctionDef(self, node):
        """Track function definitions."""
        self.defined_names.add(node.name)
        # Add function parameters as defined
        for arg in node.args.args:
            self.defined_names.add(arg.arg)
        self.generic_visit(node)
        
    def visit_ClassDef(self, node):
        """Track class definitions."""
        self.defined_names.add(node.name)
        self.generic_visit(node)
        
    def visit_Name(self, node):
        """Track name usage."""
        if isinstance(node.ctx, ast.Load):
            # This name is being used
            if node.id not in self.defined_names and node.id not in self.imported_names:
                # Check if it's a builtin
                if node.id not in dir(__builtins__):
                    self.undefined_names.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            # This name is being defined
            self.defined_names.add(node.id)
        self.generic_visit(node)
        
    def visit_Assign(self, node):
        """Track variable assignments."""
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.defined_names.add(target.id)
        self.generic_visit(node)


def analyze_file(file_path: Path) -> Tuple[Set[str], List[str]]:
    """Analyze a Python file for missing imports."""
    try:
        content = file_path.read_text()
        tree = ast.parse(content)
        
        analyzer = ImportAnalyzer()
        analyzer.visit(tree)
        
        # Get existing import lines
        lines = content.split('\n')
        import_lines = []
        for i, line in enumerate(lines):
            if line.strip().startswith(('import ', 'from ')):
                import_lines.append(i)
                
        return analyzer.undefined_names, lines
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return set(), []


def get_required_imports(undefined_names: Set[str]) -> Dict[str, str]:
    """Map undefined names to their required import statements."""
    import_map = {
        'os': 'import os',
        'sys': 'import sys',
        'json': 'import json',
        'asyncio': 'import asyncio',
        'unittest': 'import unittest',
        'shutil': 'import shutil',
        'subprocess': 'import subprocess',
        'threading': 'import threading',
        'time': 'import time',
        'uuid': 'import uuid',
        'random': 'import random',
        'hashlib': 'import hashlib',
        'base64': 'import base64',
        'collections': 'import collections',
        'itertools': 'import itertools',
        'functools': 'import functools',
        'contextlib': 'import contextlib',
        'io': 'import io',
        'tempfile': 'import tempfile',
        're': 'import re',
        'logging': 'import logging',
        'datetime': 'from datetime import datetime',
        'timedelta': 'from datetime import timedelta',
        'Path': 'from pathlib import Path',
        'Any': 'from typing import Any',
        'Dict': 'from typing import Dict',
        'List': 'from typing import List',
        'Optional': 'from typing import Optional',
        'Tuple': 'from typing import Tuple',
        'Union': 'from typing import Union',
        'Set': 'from typing import Set',
    }
    
    required_imports = {}
    for name in undefined_names:
        if name in import_map:
            required_imports[name] = import_map[name]
            
    return required_imports


def fix_imports_in_file(file_path: Path) -> bool:
    """Fix import errors in a single file."""
    undefined_names, lines = analyze_file(file_path)
    
    if not undefined_names:
        return True
        
    print(f"\nFixing {file_path}")
    print(f"  Undefined names: {undefined_names}")
    
    required_imports = get_required_imports(undefined_names)
    
    if not required_imports:
        print(f"  No automatic fixes available for: {undefined_names}")
        return False
        
    # Find where to insert imports (after existing imports or docstring)
    insert_position = 0
    in_docstring = False
    docstring_quotes = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Handle docstrings
        if not in_docstring and (stripped.startswith('"""') or stripped.startswith("'''")):
            docstring_quotes = '"""' if stripped.startswith('"""') else "'''"
            if stripped.count(docstring_quotes) == 2 and len(stripped) > 6:
                # Single-line docstring
                insert_position = i + 1
            else:
                in_docstring = True
        elif in_docstring and docstring_quotes in stripped:
            in_docstring = False
            insert_position = i + 1
        # Handle imports
        elif stripped.startswith(('import ', 'from ')) and not in_docstring:
            insert_position = i + 1
        elif not stripped and insert_position > 0:
            # Empty line after imports/docstring
            break
            
    # Check which imports are already present
    existing_content = '\n'.join(lines)
    imports_to_add = []
    
    for name, import_stmt in required_imports.items():
        # Check if this import already exists
        if import_stmt not in existing_content:
            # Also check for variations
            if f"import {name}" not in existing_content and f"from {name}" not in existing_content:
                imports_to_add.append(import_stmt)
                
    if imports_to_add:
        print(f"  Adding imports: {imports_to_add}")
        
        # Insert the new imports
        for imp in reversed(imports_to_add):
            lines.insert(insert_position, imp)
            
        # Write back the file
        file_path.write_text('\n'.join(lines))
        return True
    else:
        print("  All required imports already present")
        return True


def main():
    """Fix import errors in all test files."""
    project_root = Path(__file__).parent.parent
    test_dir = project_root / "tests"
    
    if not test_dir.exists():
        print(f"Test directory not found: {test_dir}")
        return
        
    print("Fixing import errors in test files...")
    
    # Find all test files
    test_files = list(test_dir.rglob("test_*.py"))
    
    fixed_count = 0
    failed_count = 0
    
    for test_file in test_files:
        if fix_imports_in_file(test_file):
            fixed_count += 1
        else:
            failed_count += 1
            
    print(f"\nSummary:")
    print(f"  Files processed: {len(test_files)}")
    print(f"  Files fixed: {fixed_count}")
    print(f"  Files with issues: {failed_count}")
    
    # Also ensure __init__.py files exist
    print("\nEnsuring __init__.py files exist...")
    init_dirs = [
        test_dir,
        test_dir / "unit",
        test_dir / "integration", 
        test_dir / "e2e",
    ]
    
    for dir_path in init_dirs:
        if dir_path.exists():
            init_file = dir_path / "__init__.py"
            if not init_file.exists():
                init_file.write_text("")
                print(f"  Created {init_file}")


if __name__ == "__main__":
    main()