"""Shared import analysis utilities for dependency management."""

import ast
import os
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set, List, Tuple, Optional

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

# Known local module patterns for this project
LOCAL_MODULE_PATTERNS = [
    'config', 'framework', 'loader', 'validator', 'metrics', 
    'template_resolver', 'xml_utils', 'monitoring', 'optimization',
    'validation', 'deployment', 'utilities', 'testing', 'scripts'
]


class ImportAnalyzer:
    """Unified import analyzer with multiple analysis modes."""
    
    def __init__(self, detailed_mode=False):
        self.detailed_mode = detailed_mode
        self.imports_by_file = defaultdict(lambda: {
            'stdlib': set(),
            'external': set(),
            'local': set(),
            'relative': set()
        })
        self.all_imports = defaultdict(set)
        self.external_deps = defaultdict(set)
        self.errors = []
        self.conflicts = []
        
    def is_stdlib(self, module_name: str) -> bool:
        """Check if a module is part of the standard library."""
        base_module = module_name.split('.')[0]
        return base_module in STDLIB_MODULES
    
    def is_local(self, module_name: str) -> bool:
        """Check if a module appears to be a local import."""
        base_module = module_name.split('.')[0]
        return (base_module in LOCAL_MODULE_PATTERNS or 
                module_name.startswith('.') or
                any(module_name.startswith(f'{pattern}.') for pattern in LOCAL_MODULE_PATTERNS))
    
    def classify_import(self, filepath: str, module_name: str) -> str:
        """Classify an import as stdlib, external, local, or relative."""
        if module_name.startswith('.'):
            self.imports_by_file[filepath]['relative'].add(module_name)
            return 'relative'
        elif self.is_stdlib(module_name):
            self.imports_by_file[filepath]['stdlib'].add(module_name)
            return 'stdlib'
        elif self.is_local(module_name):
            self.imports_by_file[filepath]['local'].add(module_name)
            return 'local'
        else:
            self.imports_by_file[filepath]['external'].add(module_name)
            base_module = module_name.split('.')[0]
            self.external_deps[base_module].add(filepath)
            return 'external'
    
    def analyze_file(self, filepath: str) -> None:
        """Analyze imports in a single Python file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.classify_import(filepath, alias.name)
                        self.all_imports[alias.name].add(filepath)
                elif isinstance(node, ast.ImportFrom):
                    if node.level > 0:
                        # Relative import
                        module = '.' * node.level + (node.module or '')
                        self.classify_import(filepath, module)
                    elif node.module:
                        self.classify_import(filepath, node.module)
                        self.all_imports[node.module].add(filepath)
                        
        except Exception as e:
            self.errors.append(f"Error analyzing {filepath}: {e}")
    
    def analyze_directory(self, directory: str) -> None:
        """Analyze all Python files in a directory recursively."""
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    self.analyze_file(filepath)
    
    def find_conflicts(self) -> List[Tuple[str, List[str]]]:
        """Find potential import conflicts or duplications."""
        conflicts = []
        
        # Check for multiple versions of the same external dependency
        for module, files in self.external_deps.items():
            if len(files) > 1:
                # Check if different files might be importing different versions
                file_list = list(files)
                if any('test' in f for f in file_list) and any('test' not in f for f in file_list):
                    conflicts.append((module, file_list))
        
        return conflicts
    
    def get_dependency_graph(self) -> Dict[str, Set[str]]:
        """Generate a dependency graph showing which files depend on which modules."""
        graph = {}
        for filepath, imports in self.imports_by_file.items():
            all_deps = (imports['external'] | imports['local'] | imports['relative'])
            if all_deps:
                graph[filepath] = all_deps
        return graph
    
    def generate_requirements(self) -> Dict[str, str]:
        """Generate requirements.txt content with known versions."""
        pkg_versions = {
            'pytest': '>=7.0.0',
            'pytest-cov': '>=4.0.0',
            'pandas': '>=1.5.0',
            'numpy': '>=1.21.0',
            'matplotlib': '>=3.5.0',
            'networkx': '>=2.8.0',
            'graphviz': '>=0.20',
            'pyyaml': '>=6.0',
            'lxml': '>=4.9.0',
            'black': '>=22.0.0',
            'flake8': '>=5.0.0',
            'mypy': '>=1.0.0',
            'coverage': '>=7.0.0',
            'psutil': '>=5.9.0',
            'defusedxml': '>=0.7.1',
            'schedule': '>=1.2.0',
            'requests': '>=2.28.0'
        }
        
        requirements = {}
        for dep in sorted(self.external_deps.keys()):
            if dep not in ['validate']:  # Skip known problematic imports
                version = pkg_versions.get(dep, '')
                requirements[dep] = f"{dep}{version}"
        
        return requirements
    
    def get_summary(self) -> Dict[str, any]:
        """Get a summary of the analysis."""
        return {
            'total_files': len(self.imports_by_file),
            'external_dependencies': len(self.external_deps),
            'total_imports': len(self.all_imports),
            'errors': len(self.errors),
            'conflicts': len(self.find_conflicts()),
            'files_with_external_deps': sum(1 for f, i in self.imports_by_file.items() if i['external'])
        }


def analyze_project_dependencies(directories: List[str], detailed: bool = False) -> Dict[str, any]:
    """Analyze dependencies across multiple directories."""
    analyzer = ImportAnalyzer(detailed_mode=detailed)
    
    for directory in directories:
        if os.path.exists(directory):
            analyzer.analyze_directory(directory)
    
    return {
        'summary': analyzer.get_summary(),
        'external_deps': dict(analyzer.external_deps),
        'conflicts': analyzer.find_conflicts(),
        'errors': analyzer.errors,
        'requirements': analyzer.generate_requirements(),
        'dependency_graph': analyzer.get_dependency_graph() if detailed else None
    }