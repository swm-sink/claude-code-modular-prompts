#!/usr/bin/env python3
"""Detailed analysis of imports to identify true external dependencies."""

import ast
import os
import sys
from pathlib import Path
from collections import defaultdict
import json

# Complete standard library modules for Python 3.8+
STDLIB_MODULES = {
    'abc', 'argparse', 'ast', 'asyncio', 'base64', 'bdb', 'binascii', 'bisect',
    'builtins', 'bz2', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmd', 'code', 
    'codecs', 'collections', 'colorsys', 'compileall', 'concurrent', 'configparser',
    'contextlib', 'contextvars', 'copy', 'copyreg', 'crypt', 'csv', 'ctypes',
    'curses', 'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis',
    'doctest', 'email', 'encodings', 'enum', 'errno', 'faulthandler', 'fcntl',
    'filecmp', 'fileinput', 'fnmatch', 'fractions', 'ftplib', 'functools',
    'gc', 'getopt', 'getpass', 'gettext', 'glob', 'grp', 'gzip', 'hashlib',
    'heapq', 'hmac', 'html', 'http', 'imaplib', 'imghdr', 'imp', 'importlib',
    'inspect', 'io', 'ipaddress', 'itertools', 'json', 'keyword', 'lib2to3',
    'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap', 'marshal',
    'math', 'mimetypes', 'mmap', 'modulefinder', 'multiprocessing', 'netrc',
    'nis', 'nntplib', 'numbers', 'operator', 'optparse', 'os', 'pathlib', 'pdb',
    'pickle', 'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib', 'poplib',
    'posix', 'pprint', 'profile', 'pstats', 'pty', 'pwd', 'py_compile', 'pyclbr',
    'pydoc', 'queue', 'quopri', 'random', 're', 'readline', 'reprlib', 'resource',
    'rlcompleter', 'runpy', 'sched', 'secrets', 'select', 'selectors', 'shelve',
    'shlex', 'shutil', 'signal', 'site', 'smtpd', 'smtplib', 'sndhdr', 'socket',
    'socketserver', 'spwd', 'sqlite3', 'ssl', 'stat', 'statistics', 'string',
    'stringprep', 'struct', 'subprocess', 'sunau', 'symbol', 'symtable', 'sys',
    'sysconfig', 'syslog', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile',
    'termios', 'test', 'textwrap', 'threading', 'time', 'timeit', 'token',
    'tokenize', 'trace', 'traceback', 'tracemalloc', 'tty', 'turtle', 'types',
    'typing', 'unicodedata', 'unittest', 'urllib', 'uu', 'uuid', 'venv',
    'warnings', 'wave', 'weakref', 'webbrowser', 'winreg', 'winsound', 'wsgiref',
    'xdrlib', 'xml', 'xmlrpc', 'zipapp', 'zipfile', 'zipimport', 'zlib'
}

class DetailedImportAnalyzer:
    def __init__(self):
        self.imports_by_file = defaultdict(lambda: {
            'stdlib': set(),
            'external': set(),
            'local': set(),
            'relative': set()
        })
        self.all_external_deps = defaultdict(set)
        self.errors = []
        self.suspicious_imports = []

    def is_stdlib(self, module_name):
        """Check if a module is part of the standard library."""
        base_module = module_name.split('.')[0]
        return base_module in STDLIB_MODULES

    def analyze_file(self, filepath):
        """Analyze imports in a single Python file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.classify_import(filepath, alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.level > 0:
                        # Relative import
                        module = '.' * node.level + (node.module or '')
                        self.imports_by_file[filepath]['relative'].add(module)
                    elif node.module:
                        self.classify_import(filepath, node.module)
                        
        except Exception as e:
            self.errors.append(f"Error analyzing {filepath}: {e}")

    def classify_import(self, filepath, module_name):
        """Classify an import as stdlib, external, or local."""
        if self.is_stdlib(module_name):
            self.imports_by_file[filepath]['stdlib'].add(module_name)
        else:
            # Check if it looks like a local import based on the file structure
            base_module = module_name.split('.')[0]
            
            # Common patterns for local imports in this project
            if base_module in ['config', 'framework', 'loader', 'validator', 
                              'metrics', 'template_resolver', 'xml_utils']:
                self.imports_by_file[filepath]['local'].add(module_name)
            elif base_module == 'validate':
                # This might be a typo - should check further
                self.suspicious_imports.append((filepath, module_name))
                self.imports_by_file[filepath]['external'].add(module_name)
            else:
                # True external dependency
                self.imports_by_file[filepath]['external'].add(module_name)
                self.all_external_deps[base_module].add(filepath)

    def analyze_all_scripts(self):
        """Analyze all Python scripts in the project."""
        script_dirs = ['./scripts', './.claude/scripts']
        
        for dir_path in script_dirs:
            if os.path.exists(dir_path):
                for root, _, files in os.walk(dir_path):
                    for file in files:
                        if file.endswith('.py'):
                            filepath = os.path.join(root, file)
                            self.analyze_file(filepath)

    def generate_report(self):
        """Generate comprehensive dependency report."""
        true_external_deps = {}
        
        # Filter out false positives
        for dep, files in self.all_external_deps.items():
            if dep not in ['loader', 'validator', 'metrics', 'template_resolver', 
                          'xml_utils', 'validate']:
                true_external_deps[dep] = list(files)
            elif dep == 'validate':
                # This might be a typo or missing module
                true_external_deps[dep] = list(files)
        
        report = {
            'total_files_analyzed': len(self.imports_by_file),
            'true_external_dependencies': true_external_deps,
            'suspicious_imports': self.suspicious_imports,
            'errors': self.errors,
            'stats': {
                'files_with_external_deps': len([f for f, i in self.imports_by_file.items() 
                                               if i['external']]),
                'total_external_packages': len(true_external_deps)
            }
        }
        
        return report

def main():
    analyzer = DetailedImportAnalyzer()
    analyzer.analyze_all_scripts()
    report = analyzer.generate_report()
    
    print("\n📊 Detailed Import Analysis")
    print("=" * 60)
    print(f"Total files analyzed: {report['total_files_analyzed']}")
    print(f"Files with external dependencies: {report['stats']['files_with_external_deps']}")
    print(f"True external packages found: {report['stats']['total_external_packages']}")
    
    print("\n📦 True External Dependencies (require pip install):")
    print("-" * 60)
    for dep, files in sorted(report['true_external_dependencies'].items()):
        print(f"\n{dep}:")
        for file in sorted(files):
            print(f"  - {file}")
    
    if report['suspicious_imports']:
        print("\n⚠️  Suspicious Imports (may be errors):")
        print("-" * 60)
        for file, imp in report['suspicious_imports']:
            print(f"  {file}: imports '{imp}'")
    
    # Generate clean requirements.txt
    with open('requirements_clean.txt', 'w') as f:
        f.write("# External dependencies for Claude Code Modular Prompts\n")
        f.write("# Generated on: 2025-07-13\n\n")
        
        # Known packages with versions
        pkg_versions = {
            'psutil': '>=5.9.0',
            'defusedxml': '>=0.7.1',
            'schedule': '>=1.2.0',
            'numpy': '>=1.21.0',
            'pandas': '>=1.5.0',
            'requests': '>=2.28.0'
        }
        
        for dep in sorted(report['true_external_dependencies'].keys()):
            if dep != 'validate':  # Skip suspicious import
                version = pkg_versions.get(dep, '')
                f.write(f"{dep}{version}\n")
    
    print(f"\n✅ Clean requirements.txt saved as requirements_clean.txt")
    
    # Save detailed report
    with open('dependency_report_detailed.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📄 Detailed report saved to dependency_report_detailed.json")
    
    # Check current pip environment
    print("\n🔍 Checking installed packages...")
    os.system("pip list | grep -E 'psutil|defusedxml|schedule|numpy|pandas|requests' || echo 'None of the required packages found'")

if __name__ == "__main__":
    main()