#!/usr/bin/env python3
"""
Atomic Component Unit Testing Framework

Tests individual components for functionality, clarity, edge cases,
and real-world usability scenarios. Validates prompt effectiveness
beyond just structural compliance.

Usage:
    python3 component-unit-tester.py [component_file]
    python3 component-unit-tester.py --all
"""

import os
import re
import argparse
from typing import Tuple, List, Dict, Any
from pathlib import Path

class ComponentUnitTester:
    def __init__(self):
        self.test_scenarios = {
            'clarity': self._test_clarity,
            'completeness': self._test_completeness,
            'edge_cases': self._test_edge_cases,
            'usability': self._test_usability,
            'specificity': self._test_specificity,
            'actionability': self._test_actionability
        }
    
    def _test_clarity(self, content: str, title: str) -> Tuple[bool, str]:
        """Test if component instructions are clear and unambiguous"""
        code_block = self._extract_code_block(content)
        if not code_block:
            return False, "No code block found"
        
        # Check for clear action verbs
        action_verbs = ['check', 'verify', 'validate', 'ensure', 'handle', 'provide', 'generate', 'parse', 'execute', 'manage', 'track', 'resolve', 'coordinate', 'transform', 'convert', 'sanitize', 'format']
        has_action_verbs = any(verb in code_block.lower() for verb in action_verbs)
        
        # Check for vague terms that reduce clarity
        vague_terms = ['somehow', 'appropriately', 'properly', 'correctly', 'as needed', 'if necessary']
        has_vague_terms = any(term in code_block.lower() for term in vague_terms)
        
        # Check for specific instructions
        bullet_points = [line.strip() for line in code_block.split('\n') if line.strip().startswith('-')]
        specific_instructions = len(bullet_points) >= 3
        
        clarity_score = sum([has_action_verbs, not has_vague_terms, specific_instructions])
        is_clear = clarity_score >= 2
        
        details = f"Action verbs: {has_action_verbs}, Avoids vague terms: {not has_vague_terms}, Specific instructions: {specific_instructions}"
        return is_clear, details
    
    def _test_completeness(self, content: str, title: str) -> Tuple[bool, str]:
        """Test if component covers complete workflow for its purpose"""
        code_block = self._extract_code_block(content)
        if not code_block:
            return False, "No code block found"
        
        # Check for input handling
        has_input_handling = any(term in code_block.lower() for term in ['input', 'parameter', 'data', 'content', 'request'])
        
        # Check for processing/operation
        has_processing = any(term in code_block.lower() for term in ['process', 'execute', 'run', 'perform', 'apply', 'transform', 'parse', 'analyze'])
        
        # Check for output/result handling
        has_output_handling = any(term in code_block.lower() for term in ['output', 'result', 'response', 'report', 'generate', 'provide', 'return'])
        
        # Check for error handling
        has_error_handling = any(term in code_block.lower() for term in ['error', 'fail', 'exception', 'issue', 'problem'])
        
        completeness_score = sum([has_input_handling, has_processing, has_output_handling, has_error_handling])
        is_complete = completeness_score >= 3
        
        details = f"Input: {has_input_handling}, Processing: {has_processing}, Output: {has_output_handling}, Errors: {has_error_handling}"
        return is_complete, details
    
    def _test_edge_cases(self, content: str, title: str) -> Tuple[bool, str]:
        """Test if component addresses edge cases and error conditions"""
        code_block = self._extract_code_block(content)
        if not code_block:
            return False, "No code block found"
        
        # Look for edge case handling patterns
        edge_case_indicators = [
            'if', 'when', 'handle', 'fail', 'error', 'exception', 'missing', 'invalid', 
            'empty', 'null', 'conflict', 'timeout', 'retry', 'fallback', 'recovery'
        ]
        
        edge_case_count = sum(1 for indicator in edge_case_indicators if indicator in code_block.lower())
        handles_edge_cases = edge_case_count >= 2
        
        # Check for validation steps
        validation_terms = ['validate', 'verify', 'check', 'ensure', 'confirm']
        has_validation = any(term in code_block.lower() for term in validation_terms)
        
        # Check for error handling
        error_handling = any(term in code_block.lower() for term in ['error', 'fail', 'exception'])
        
        edge_case_score = sum([handles_edge_cases, has_validation, error_handling])
        handles_edges = edge_case_score >= 2
        
        details = f"Edge indicators: {edge_case_count}, Validation: {has_validation}, Error handling: {error_handling}"
        return handles_edges, details
    
    def _test_usability(self, content: str, title: str) -> Tuple[bool, str]:
        """Test if component is practical for real-world usage"""
        code_block = self._extract_code_block(content)
        if not code_block:
            return False, "No code block found"
        
        # Check instruction length (not too short, not too long)
        lines = [line.strip() for line in code_block.split('\n') if line.strip()]
        instruction_lines = [line for line in lines if line.startswith('-')]
        appropriate_length = 3 <= len(instruction_lines) <= 10
        
        # Check for implementation guidance
        implementation_terms = ['use', 'apply', 'implement', 'execute', 'run', 'perform']
        has_implementation = any(term in code_block.lower() for term in implementation_terms)
        
        # Check for result expectations
        result_terms = ['result', 'output', 'response', 'generate', 'produce', 'create']
        has_result_clarity = any(term in code_block.lower() for term in result_terms)
        
        usability_score = sum([appropriate_length, has_implementation, has_result_clarity])
        is_usable = usability_score >= 2
        
        details = f"Length: {len(instruction_lines)} lines, Implementation: {has_implementation}, Results: {has_result_clarity}"
        return is_usable, details
    
    def _test_specificity(self, content: str, title: str) -> Tuple[bool, str]:
        """Test if component provides specific, actionable instructions"""
        code_block = self._extract_code_block(content)
        if not code_block:
            return False, "No code block found"
        
        # Count specific action words
        specific_actions = [
            'check', 'verify', 'validate', 'parse', 'extract', 'transform', 'convert', 
            'generate', 'create', 'update', 'remove', 'add', 'replace', 'format'
        ]
        action_count = sum(1 for action in specific_actions if action in code_block.lower())
        
        # Avoid generic terms
        generic_terms = ['handle', 'manage', 'deal with', 'work with', 'process']
        generic_count = sum(1 for term in generic_terms if term in code_block.lower())
        
        # Check for measurable criteria
        measurable_terms = ['all', 'each', 'every', 'complete', 'successful', 'valid', 'correct']
        has_measurable = any(term in code_block.lower() for term in measurable_terms)
        
        specificity_score = action_count - generic_count + (1 if has_measurable else 0)
        is_specific = specificity_score >= 2
        
        details = f"Specific actions: {action_count}, Generic terms: {generic_count}, Measurable: {has_measurable}"
        return is_specific, details
    
    def _test_actionability(self, content: str, title: str) -> Tuple[bool, str]:
        """Test if component provides actionable instructions"""
        code_block = self._extract_code_block(content)
        if not code_block:
            return False, "No code block found"
        
        # Check for imperative mood (commands/instructions)
        lines = [line.strip() for line in code_block.split('\n') if line.strip().startswith('-')]
        
        # Count lines that start with action verbs
        action_starters = 0
        for line in lines:
            line_text = line.replace('-', '').strip().lower()
            if any(line_text.startswith(verb) for verb in ['check', 'verify', 'validate', 'ensure', 'handle', 'provide', 'generate', 'parse', 'execute', 'manage', 'track', 'resolve', 'coordinate', 'transform', 'convert', 'sanitize', 'format', 'create', 'update', 'remove', 'add', 'replace']):
                action_starters += 1
        
        actionable_ratio = action_starters / max(len(lines), 1)
        is_actionable = actionable_ratio >= 0.6  # At least 60% actionable instructions
        
        details = f"Actionable instructions: {action_starters}/{len(lines)} ({actionable_ratio:.1%})"
        return is_actionable, details
    
    def _extract_code_block(self, content: str) -> str:
        """Extract the main code block from component content"""
        code_block_match = re.search(r'```\n(.*?)\n```', content, re.DOTALL)
        return code_block_match.group(1) if code_block_match else ""
    
    def test_component(self, file_path: str) -> Dict[str, Any]:
        """Run all unit tests on a component"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {'error': f"Could not read file: {e}"}
        
        # Extract title
        title_match = re.search(r'^# (.+) Component\s*$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Unknown"
        
        results = {
            'file': file_path,
            'title': title,
            'tests': {},
            'passed': 0,
            'total': len(self.test_scenarios),
            'score': 0,
            'grade': 'F'
        }
        
        # Run all tests
        for test_name, test_func in self.test_scenarios.items():
            passed, details = test_func(content, title)
            results['tests'][test_name] = {
                'passed': passed,
                'details': details
            }
            if passed:
                results['passed'] += 1
        
        # Calculate score and grade
        results['score'] = (results['passed'] / results['total']) * 100
        
        if results['score'] >= 90:
            results['grade'] = 'A'
        elif results['score'] >= 80:
            results['grade'] = 'B'
        elif results['score'] >= 70:
            results['grade'] = 'C'
        elif results['score'] >= 60:
            results['grade'] = 'D'
        else:
            results['grade'] = 'F'
        
        return results
    
    def test_all_components(self, components_dir: str = '.claude/components/atomic') -> Dict[str, Any]:
        """Test all components in the atomic directory"""
        if not os.path.exists(components_dir):
            return {'error': f"Components directory not found: {components_dir}"}
        
        results = {
            'directory': components_dir,
            'total_components': 0,
            'components': {},
            'summary': {
                'grades': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0},
                'average_score': 0,
                'pass_rate': 0
            }
        }
        
        for filename in os.listdir(components_dir):
            if filename.endswith('.md'):
                file_path = os.path.join(components_dir, filename)
                results['total_components'] += 1
                
                component_results = self.test_component(file_path)
                results['components'][filename] = component_results
                
                if 'grade' in component_results:
                    results['summary']['grades'][component_results['grade']] += 1
        
        if results['total_components'] > 0:
            total_score = sum(comp.get('score', 0) for comp in results['components'].values() if 'score' in comp)
            results['summary']['average_score'] = total_score / results['total_components']
            
            passing_components = sum(1 for comp in results['components'].values() if comp.get('score', 0) >= 70)
            results['summary']['pass_rate'] = (passing_components / results['total_components']) * 100
        
        return results
    
    def print_results(self, results: Dict[str, Any]):
        """Print formatted unit test results"""
        if 'error' in results:
            print(f"❌ Error: {results['error']}")
            return
        
        if 'total_components' in results:
            # Multiple components
            print("🧪 ATOMIC COMPONENT UNIT TESTING")
            print("=" * 50)
            print(f"Directory: {results['directory']}")
            print(f"Components Tested: {results['total_components']}")
            print(f"Average Score: {results['summary']['average_score']:.1f}%")
            print(f"Pass Rate (≥70%): {results['summary']['pass_rate']:.1f}%")
            print()
            
            print("Grade Distribution:")
            for grade, count in results['summary']['grades'].items():
                percentage = (count / results['total_components']) * 100 if results['total_components'] > 0 else 0
                print(f"  {grade}: {count} components ({percentage:.1f}%)")
            print()
            
            print("Component Results:")
            for filename, component in results['components'].items():
                if 'error' in component:
                    print(f"❌ {filename}: {component['error']}")
                else:
                    status = "✅" if component['score'] >= 70 else "❌"
                    print(f"{status} {filename}: {component['score']:.1f}% (Grade: {component['grade']})")
        else:
            # Single component
            if 'error' in results:
                print(f"❌ {results['file']}: {results['error']}")
            else:
                status = "✅" if results['score'] >= 70 else "❌"
                print(f"{status} {results['title']} ({Path(results['file']).name})")
                print(f"Score: {results['score']:.1f}% (Grade: {results['grade']})")
                print(f"Passed: {results['passed']}/{results['total']} tests")
                print()
                
                for test_name, test_result in results['tests'].items():
                    status = "✅" if test_result['passed'] else "❌"
                    print(f"{status} {test_name}: {test_result['details']}")

def main():
    parser = argparse.ArgumentParser(description="Unit test atomic components for functionality and usability")
    parser.add_argument('component', nargs='?', help='Specific component file to test')
    parser.add_argument('--all', action='store_true', help='Test all components')
    
    args = parser.parse_args()
    
    tester = ComponentUnitTester()
    
    if args.all or args.component is None:
        results = tester.test_all_components()
        tester.print_results(results)
    else:
        if not os.path.exists(args.component):
            print(f"❌ Component file not found: {args.component}")
            return 1
        
        results = tester.test_component(args.component)
        tester.print_results(results)
        
        return 0 if results.get('score', 0) >= 70 else 1

if __name__ == "__main__":
    exit(main())