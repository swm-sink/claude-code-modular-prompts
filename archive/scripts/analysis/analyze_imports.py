#!/usr/bin/env python3
"""Analyze imports across all Python scripts to identify dependencies."""

import ast
import os
import sys
from pathlib import Path
from collections import defaultdict
import json

# Standard library modules (Python 3.x)
STDLIB_MODULES = {
    'abc', 'argparse', 'ast', 'asyncio', 'base64', 'collections', 'concurrent',
    'copy', 'csv', 'dataclasses', 'datetime', 'decimal', 'difflib', 'email',
    'enum', 'functools', 'glob', 'hashlib', 'http', 'importlib', 'inspect',
    'io', 'itertools', 'json', 'logging', 'math', 'multiprocessing', 'os',
    'pathlib', 'pickle', 'platform', 'pprint', 'queue', 'random', 're',
    'shutil', 'signal', 'smtplib', 'socket', 'socketserver', 'sqlite3',
    'statistics', 'string', 'subprocess', 'sys', 'tempfile', 'textwrap',
    'threading', 'time', 'timeit', 'traceback', 'typing', 'unittest',
    'urllib', 'uuid', 'warnings', 'webbrowser', 'xml', 'zipfile'
}

class ImportAnalyzer:
    def __init__(self):
        self.imports_by_file = defaultdict(set)
        self.external_deps = defaultdict(int)
        self.stdlib_deps = defaultdict(int)
        self.local_imports = defaultdict(int)
        self.errors = []

    def is_stdlib(self, module_name):
        """Check if a module is part of the standard library."""
        # Handle submodules (e.g., xml.etree.ElementTree)
        base_module = module_name.split('.')[0]
        return base_module in STDLIB_MODULES

    def is_local(self, module_name):
        """Check if a module appears to be a local import."""
        local_prefixes = ['.', 'scripts.', 'config.', 'monitoring.', 
                         'optimization.', 'validation.', 'deployment.',
                         'utilities.', 'testing.']
        return any(module_name.startswith(prefix) for prefix in local_prefixes)

    def analyze_file(self, filepath):
        """Analyze imports in a single Python file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.process_import(filepath, alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        # Handle 'from module import ...'
                        self.process_import(filepath, node.module)
                    elif node.level > 0:
                        # Handle relative imports like 'from . import ...'
                        self.process_import(filepath, '.' * node.level)
                        
        except Exception as e:
            self.errors.append(f"Error analyzing {filepath}: {e}")

    def process_import(self, filepath, module_name):
        """Process a single import statement."""
        self.imports_by_file[filepath].add(module_name)
        
        if self.is_local(module_name):
            self.local_imports[module_name] += 1
        elif self.is_stdlib(module_name):
            self.stdlib_deps[module_name] += 1
        else:
            # External dependency
            base_module = module_name.split('.')[0]
            self.external_deps[base_module] += 1

    def analyze_directory(self, directory):
        """Analyze all Python files in a directory."""
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    self.analyze_file(filepath)

    def generate_report(self):
        """Generate a comprehensive dependency report."""
        report = {
            'total_files': len(self.imports_by_file),
            'external_dependencies': dict(sorted(self.external_deps.items())),
            'stdlib_usage': dict(sorted(self.stdlib_deps.items(), key=lambda x: x[1], reverse=True)[:20]),
            'local_imports': dict(sorted(self.local_imports.items())),
            'errors': self.errors,
            'files_with_external_deps': {}
        }
        
        # Map external dependencies to files that use them
        for filepath, imports in self.imports_by_file.items():
            external_in_file = []
            for imp in imports:
                if not self.is_stdlib(imp) and not self.is_local(imp):
                    base_module = imp.split('.')[0]
                    external_in_file.append(base_module)
            
            if external_in_file:
                report['files_with_external_deps'][filepath] = list(set(external_in_file))
        
        return report

def main():
    analyzer = ImportAnalyzer()
    
    # Analyze all script directories
    script_dirs = ['./scripts', './.claude/scripts']
    
    for dir_path in script_dirs:
        if os.path.exists(dir_path):
            print(f"Analyzing {dir_path}...")
            analyzer.analyze_directory(dir_path)
    
    # Generate report
    report = analyzer.generate_report()
    
    # Print summary
    print(f"\n📊 Import Analysis Summary")
    print(f"{'='*50}")
    print(f"Total Python files analyzed: {report['total_files']}")
    print(f"External dependencies found: {len(report['external_dependencies'])}")
    print(f"Errors encountered: {len(report['errors'])}")
    
    print(f"\n📦 External Dependencies (pip packages):")
    print(f"{'-'*50}")
    for dep, count in sorted(report['external_dependencies'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {dep:20} used in {count} files")
    
    print(f"\n📁 Files requiring external dependencies:")
    print(f"{'-'*50}")
    for filepath, deps in sorted(report['files_with_external_deps'].items()):
        print(f"  {filepath}")
        for dep in deps:
            print(f"    - {dep}")
    
    # Save detailed report
    with open('dependency_analysis.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✅ Detailed report saved to dependency_analysis.json")
    
    # Generate requirements.txt
    if report['external_dependencies']:
        with open('requirements.txt', 'w') as f:
            f.write("# Auto-generated requirements from dependency analysis\n")
            f.write("# Generated on: 2025-07-13\n\n")
            for dep in sorted(report['external_dependencies'].keys()):
                # Add common version constraints where known
                if dep == 'pytest':
                    f.write("pytest>=7.0.0\n")
                elif dep == 'pandas':
                    f.write("pandas>=1.5.0\n")
                elif dep == 'numpy':
                    f.write("numpy>=1.21.0\n")
                elif dep == 'matplotlib':
                    f.write("matplotlib>=3.5.0\n")
                elif dep == 'networkx':
                    f.write("networkx>=2.8.0\n")
                elif dep == 'graphviz':
                    f.write("graphviz>=0.20\n")
                elif dep == 'pyyaml':
                    f.write("pyyaml>=6.0\n")
                elif dep == 'lxml':
                    f.write("lxml>=4.9.0\n")
                elif dep == 'black':
                    f.write("black>=22.0.0\n")
                elif dep == 'flake8':
                    f.write("flake8>=5.0.0\n")
                elif dep == 'mypy':
                    f.write("mypy>=1.0.0\n")
                elif dep == 'coverage':
                    f.write("coverage>=7.0.0\n")
                elif dep == 'pytest-cov':
                    f.write("pytest-cov>=4.0.0\n")
                else:
                    f.write(f"{dep}\n")
        
        print(f"📄 requirements.txt generated with {len(report['external_dependencies'])} dependencies")
    
    return report

if __name__ == "__main__":
    main()