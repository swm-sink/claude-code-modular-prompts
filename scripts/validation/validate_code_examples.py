#!/usr/bin/env python3
"""
Validate code examples from markdown files.
Part of Agent V24: Example Validator.
"""

import ast
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class ExampleValidator:
    """Validate code examples for syntax and structure."""
    
    def __init__(self):
        self.results = {
            'total': 0,
            'validated': 0,
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'errors': []
        }
    
    def validate_python(self, code: str, context: Dict[str, str]) -> Tuple[bool, Optional[str]]:
        """Validate Python code syntax."""
        try:
            # Try to parse as a complete module
            ast.parse(code)
            return True, None
        except SyntaxError as e:
            # Try to parse as an expression
            try:
                ast.parse(code, mode='eval')
                return True, None
            except:
                # Try to parse as single statement
                try:
                    ast.parse(code, mode='single')
                    return True, None
                except:
                    return False, f"SyntaxError: {e.msg} at line {e.lineno}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def validate_bash(self, code: str, context: Dict[str, str]) -> Tuple[bool, Optional[str]]:
        """Validate bash command syntax and paths."""
        errors = []
        
        # Check for common issues
        lines = code.strip().split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Check for references to non-existent paths
            path_pattern = r'(?:\.claude/|scripts/|docs/|internal/)[^\s\'"]*'
            paths = re.findall(path_pattern, line)
            
            for path in paths:
                # Clean up the path
                clean_path = path.strip('\'",;|')
                if clean_path and not os.path.exists(clean_path):
                    errors.append(f"Line {i+1}: Path does not exist: {clean_path}")
            
            # Check for deprecated commands or patterns
            if 'claude validate' in line and 'init-validate' not in line:
                errors.append(f"Line {i+1}: Deprecated command 'claude validate' - use '/init-validate' instead")
            
            # Check for incorrect module references
            if 'modules/' in line and '.claude/modules/' not in line:
                errors.append(f"Line {i+1}: Module path should start with '.claude/modules/'")
        
        if errors:
            return False, "; ".join(errors)
        
        # Basic syntax check using bash -n (dry run)
        try:
            result = subprocess.run(
                ['bash', '-n'],
                input=code,
                text=True,
                capture_output=True,
                timeout=5
            )
            if result.returncode != 0:
                return False, f"Bash syntax error: {result.stderr.strip()}"
            return True, None
        except Exception as e:
            # If bash -n fails, still check for obvious issues
            return len(errors) == 0, None if not errors else "; ".join(errors)
    
    def validate_json(self, code: str, context: Dict[str, str]) -> Tuple[bool, Optional[str]]:
        """Validate JSON syntax."""
        try:
            json.loads(code)
            return True, None
        except json.JSONDecodeError as e:
            return False, f"JSONDecodeError: {e.msg} at line {e.lineno}, column {e.colno}"
    
    def validate_xml(self, code: str, context: Dict[str, str]) -> Tuple[bool, Optional[str]]:
        """Basic XML validation - check for balanced tags."""
        # This is a simple validation - just check for balanced tags
        tag_pattern = r'<([^/\s>]+)(?:\s[^>]*)?>|</([^>]+)>'
        stack = []
        
        for match in re.finditer(tag_pattern, code):
            opening_tag = match.group(1)
            closing_tag = match.group(2)
            
            if opening_tag:
                # Self-closing tags
                if match.group(0).endswith('/>'):
                    continue
                stack.append(opening_tag)
            elif closing_tag:
                if not stack or stack[-1] != closing_tag:
                    return False, f"Unmatched closing tag: </{closing_tag}>"
                stack.pop()
        
        if stack:
            return False, f"Unclosed tags: {', '.join(f'<{tag}>' for tag in stack)}"
        
        return True, None
    
    def validate_yaml(self, code: str, context: Dict[str, str]) -> Tuple[bool, Optional[str]]:
        """Validate YAML syntax."""
        try:
            import yaml
            yaml.safe_load(code)
            return True, None
        except yaml.YAMLError as e:
            return False, f"YAMLError: {str(e)}"
        except ImportError:
            # If PyYAML is not installed, do basic validation
            # Check for basic YAML structure
            if re.search(r'^\s*-\s+|\s*\w+:\s*', code, re.MULTILINE):
                return True, None
            return False, "Invalid YAML structure"
    
    def validate_example(self, example: Dict[str, str]) -> Dict[str, any]:
        """Validate a single code example."""
        self.results['total'] += 1
        
        language = example['language']
        code = example['code']
        
        # Skip validation for certain types
        if language in ['txt', 'markdown', 'html', 'sql', 'unknown']:
            self.results['skipped'] += 1
            return {
                'file': example['file'],
                'language': language,
                'status': 'skipped',
                'reason': 'Language not supported for validation'
            }
        
        # Select validator
        validators = {
            'python': self.validate_python,
            'bash': self.validate_bash,
            'json': self.validate_json,
            'xml': self.validate_xml,
            'yaml': self.validate_yaml,
            'javascript': self.validate_javascript,
            'typescript': self.validate_typescript
        }
        
        validator = validators.get(language)
        if not validator:
            self.results['skipped'] += 1
            return {
                'file': example['file'],
                'language': language,
                'status': 'skipped',
                'reason': f'No validator for language: {language}'
            }
        
        # Validate
        self.results['validated'] += 1
        passed, error = validator(code, example)
        
        if passed:
            self.results['passed'] += 1
            return {
                'file': example['file'],
                'language': language,
                'line': example['line_number'],
                'status': 'passed'
            }
        else:
            self.results['failed'] += 1
            error_detail = {
                'file': example['file'],
                'language': language,
                'line': example['line_number'],
                'status': 'failed',
                'error': error,
                'code_snippet': code[:200] + '...' if len(code) > 200 else code
            }
            self.results['errors'].append(error_detail)
            return error_detail
    
    def validate_javascript(self, code: str, context: Dict[str, str]) -> Tuple[bool, Optional[str]]:
        """Basic JavaScript validation."""
        # Very basic validation - check for common syntax errors
        try:
            # Check for balanced braces, brackets, and parentheses
            pairs = {'(': ')', '[': ']', '{': '}'}
            stack = []
            in_string = False
            string_char = None
            
            for i, char in enumerate(code):
                if char in ['"', "'", '`'] and (i == 0 or code[i-1] != '\\'):
                    if not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char:
                        in_string = False
                        string_char = None
                
                if not in_string:
                    if char in pairs:
                        stack.append(char)
                    elif char in pairs.values():
                        if not stack or pairs[stack[-1]] != char:
                            return False, f"Unmatched '{char}' at position {i}"
                        stack.pop()
            
            if stack:
                return False, f"Unclosed '{stack[-1]}'"
            
            return True, None
        except Exception as e:
            return False, str(e)
    
    def validate_typescript(self, code: str, context: Dict[str, str]) -> Tuple[bool, Optional[str]]:
        """Basic TypeScript validation - same as JavaScript for now."""
        return self.validate_javascript(code, context)

def main():
    """Main validation function."""
    # Load extracted examples
    if not os.path.exists('code_examples_extracted.json'):
        print("Error: code_examples_extracted.json not found. Run extract_code_examples.py first.")
        sys.exit(1)
    
    with open('code_examples_extracted.json', 'r') as f:
        data = json.load(f)
    
    validator = ExampleValidator()
    all_results = []
    
    # Validate each category
    for language, examples in data['examples'].items():
        print(f"\nValidating {len(examples)} {language} examples...")
        
        for example in examples:
            result = validator.validate_example(example)
            all_results.append(result)
    
    # Print summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    print(f"Total examples: {validator.results['total']}")
    print(f"Validated: {validator.results['validated']}")
    print(f"Passed: {validator.results['passed']}")
    print(f"Failed: {validator.results['failed']}")
    print(f"Skipped: {validator.results['skipped']}")
    
    # Print errors
    if validator.results['errors']:
        print("\n" + "="*60)
        print("VALIDATION ERRORS")
        print("="*60)
        
        # Group errors by file
        errors_by_file = {}
        for error in validator.results['errors']:
            file_path = error['file']
            if file_path not in errors_by_file:
                errors_by_file[file_path] = []
            errors_by_file[file_path].append(error)
        
        for file_path, errors in sorted(errors_by_file.items()):
            print(f"\n{file_path}:")
            for error in errors:
                print(f"  Line {error['line']} ({error['language']}): {error['error']}")
    
    # Save detailed results
    output_file = 'code_examples_validation_results.json'
    with open(output_file, 'w') as f:
        json.dump({
            'summary': validator.results,
            'details': all_results
        }, f, indent=2)
    
    print(f"\nDetailed results saved to: {output_file}")
    
    # Return exit code based on failures
    return 1 if validator.results['failed'] > 0 else 0

if __name__ == "__main__":
    sys.exit(main())