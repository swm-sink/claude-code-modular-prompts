#!/usr/bin/env python3
"""
Code Complexity Analyzer
Identifies the most complex functions for refactoring.
"""

import ast
import os
import sys
from pathlib import Path
from typing import List, Dict, Tuple
from collections import namedtuple
from dataclasses import dataclass

@dataclass
class FunctionComplexity:
    """Data class for function complexity metrics."""
    name: str
    file_path: str
    start_line: int
    end_line: int
    line_count: int
    cyclomatic_complexity: int
    nesting_depth: int
    parameter_count: int
    complexity_score: float
    reasons: List[str]

class ComplexityAnalyzer(ast.NodeVisitor):
    """AST visitor to analyze function complexity."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.functions = []
        self.current_depth = 0
        self.max_depth = 0
        
    def visit_FunctionDef(self, node):
        """Visit function definition and analyze complexity."""
        complexity_visitor = FunctionAnalyzer(self.file_path, node.name)
        complexity_visitor.visit(node)
        
        function_complexity = complexity_visitor.get_complexity()
        if function_complexity.line_count > 10:  # Only consider functions with >10 lines
            self.functions.append(function_complexity)
        
        self.generic_visit(node)
    
    def visit_AsyncFunctionDef(self, node):
        """Visit async function definition."""
        self.visit_FunctionDef(node)

class FunctionAnalyzer(ast.NodeVisitor):
    """Analyzer for individual function complexity."""
    
    def __init__(self, file_path: str, function_name: str):
        self.file_path = file_path
        self.function_name = function_name
        self.cyclomatic_complexity = 1  # Base complexity
        self.nesting_depth = 0
        self.max_nesting_depth = 0
        self.current_depth = 0
        self.parameter_count = 0
        self.start_line = 0
        self.end_line = 0
        self.reasons = []
        
    def visit_FunctionDef(self, node):
        """Visit function definition to collect metrics."""
        if hasattr(node, 'lineno'):
            self.start_line = node.lineno
            
        # Count parameters
        self.parameter_count = len(node.args.args)
        if node.args.vararg:
            self.parameter_count += 1
        if node.args.kwarg:
            self.parameter_count += 1
        if hasattr(node.args, 'kwonlyargs'):
            self.parameter_count += len(node.args.kwonlyargs)
            
        # Visit function body
        for stmt in node.body:
            self._find_end_line(stmt)
            self.visit(stmt)
            
        if self.parameter_count > 5:
            self.reasons.append(f"High parameter count ({self.parameter_count})")
        if self.max_nesting_depth > 4:
            self.reasons.append(f"Deep nesting ({self.max_nesting_depth} levels)")
        if self.cyclomatic_complexity > 10:
            self.reasons.append(f"High cyclomatic complexity ({self.cyclomatic_complexity})")
    
    def _find_end_line(self, node):
        """Find the ending line of a node."""
        if hasattr(node, 'lineno'):
            self.end_line = max(self.end_line, node.lineno)
        if hasattr(node, 'body'):
            for child in node.body:
                self._find_end_line(child)
        if hasattr(node, 'orelse'):
            for child in node.orelse:
                self._find_end_line(child)
    
    def visit_If(self, node):
        """Visit if statement."""
        self.cyclomatic_complexity += 1
        self._visit_nested_block(node)
    
    def visit_While(self, node):
        """Visit while loop."""
        self.cyclomatic_complexity += 1
        self._visit_nested_block(node)
    
    def visit_For(self, node):
        """Visit for loop."""
        self.cyclomatic_complexity += 1
        self._visit_nested_block(node)
    
    def visit_Try(self, node):
        """Visit try statement."""
        self.cyclomatic_complexity += len(node.handlers)
        if node.orelse:
            self.cyclomatic_complexity += 1
        if node.finalbody:
            self.cyclomatic_complexity += 1
        self._visit_nested_block(node)
    
    def visit_With(self, node):
        """Visit with statement."""
        self._visit_nested_block(node)
    
    def visit_BoolOp(self, node):
        """Visit boolean operation (and/or)."""
        if isinstance(node.op, (ast.And, ast.Or)):
            self.cyclomatic_complexity += len(node.values) - 1
        self.generic_visit(node)
    
    def _visit_nested_block(self, node):
        """Visit a nested block and track nesting depth."""
        self.current_depth += 1
        self.max_nesting_depth = max(self.max_nesting_depth, self.current_depth)
        
        # Visit body
        if hasattr(node, 'body'):
            for stmt in node.body:
                self.visit(stmt)
        
        # Visit else clause
        if hasattr(node, 'orelse'):
            for stmt in node.orelse:
                self.visit(stmt)
        
        # Visit exception handlers
        if hasattr(node, 'handlers'):
            for handler in node.handlers:
                for stmt in handler.body:
                    self.visit(stmt)
        
        # Visit finally clause
        if hasattr(node, 'finalbody'):
            for stmt in node.finalbody:
                self.visit(stmt)
        
        self.current_depth -= 1
    
    def get_complexity(self) -> FunctionComplexity:
        """Get the complexity metrics for this function."""
        line_count = max(1, self.end_line - self.start_line + 1)
        
        # Calculate composite complexity score
        complexity_score = (
            (self.cyclomatic_complexity * 2) +
            (self.max_nesting_depth * 3) +
            (self.parameter_count * 1) +
            (line_count * 0.1)
        )
        
        if line_count > 50:
            self.reasons.append(f"Long function ({line_count} lines)")
        
        return FunctionComplexity(
            name=self.function_name,
            file_path=self.file_path,
            start_line=self.start_line,
            end_line=self.end_line,
            line_count=line_count,
            cyclomatic_complexity=self.cyclomatic_complexity,
            nesting_depth=self.max_nesting_depth,
            parameter_count=self.parameter_count,
            complexity_score=complexity_score,
            reasons=self.reasons
        )

def analyze_file(file_path: Path) -> List[FunctionComplexity]:
    """Analyze complexity of all functions in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        analyzer = ComplexityAnalyzer(str(file_path))
        analyzer.visit(tree)
        
        return analyzer.functions
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return []

def find_most_complex_functions(project_root: str, limit: int = 10) -> List[FunctionComplexity]:
    """Find the most complex functions in the project."""
    all_functions = []
    
    # Focus on key directories
    focus_patterns = [
        "*.py",
        "scripts/*.py", 
        "security/*.py",
        "performance/*.py",
        "command_processing/*.py"
    ]
    
    project_path = Path(project_root)
    
    # Get all Python files
    python_files = []
    for pattern in focus_patterns:
        python_files.extend(project_path.glob(pattern))
    
    # Also get files from subdirectories
    for py_file in project_path.rglob("*.py"):
        if py_file not in python_files and not any(part.startswith('.') for part in py_file.parts):
            python_files.append(py_file)
    
    for py_file in python_files:
        if py_file.name.startswith('test_') or 'test' in py_file.name:
            continue  # Skip test files for now
        
        functions = analyze_file(py_file)
        all_functions.extend(functions)
    
    # Sort by complexity score
    all_functions.sort(key=lambda f: f.complexity_score, reverse=True)
    
    return all_functions[:limit]

def generate_refactoring_report(complex_functions: List[FunctionComplexity]) -> str:
    """Generate a refactoring report."""
    report = f"""# Top {len(complex_functions)} Most Complex Functions - Refactoring Analysis

Generated: {os.popen('date').read().strip()}

## Summary

The following functions have been identified as the most complex in the codebase and are candidates for refactoring to improve testability, maintainability, and readability.

## Complexity Analysis

"""
    
    for i, func in enumerate(complex_functions, 1):
        relative_path = Path(func.file_path).name
        
        report += f"""### {i}. `{func.name}()` 
**File**: `{relative_path}` (lines {func.start_line}-{func.end_line})  
**Complexity Score**: {func.complexity_score:.1f}  
**Lines**: {func.line_count} | **Cyclomatic**: {func.cyclomatic_complexity} | **Nesting**: {func.nesting_depth} | **Parameters**: {func.parameter_count}

**Complexity Issues**:
"""
        for reason in func.reasons:
            report += f"- {reason}\n"
        
        report += f"""
**Refactoring Strategy**:
- Extract helper methods to reduce line count
- Simplify conditional logic to reduce cyclomatic complexity
- Reduce nesting depth through early returns
- Consider parameter objects for functions with many parameters
- Apply Single Responsibility Principle

---

"""
    
    return report

def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = Path(__file__).parent.parent
    
    print("🔍 Analyzing code complexity...")
    complex_functions = find_most_complex_functions(project_root, 15)
    
    print(f"\n📊 Found {len(complex_functions)} complex functions:")
    for i, func in enumerate(complex_functions[:10], 1):
        relative_path = Path(func.file_path).relative_to(project_root)
        print(f"{i:2d}. {func.name}() in {relative_path} (score: {func.complexity_score:.1f})")
    
    # Generate report
    report = generate_refactoring_report(complex_functions[:10])
    
    # Save report
    report_path = Path(project_root) / "complexity_analysis.md"
    with open(report_path, 'w') as f:
        f.write(report)
    
    print(f"\n📋 Detailed analysis saved to: {report_path}")
    
    return complex_functions[:10]

if __name__ == "__main__":
    main()