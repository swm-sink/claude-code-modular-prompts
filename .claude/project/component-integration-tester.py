#!/usr/bin/env python3
"""
Atomic Component Integration Testing Framework

Tests combinations of atomic components to validate they work together
effectively without conflicts. Tests logical pairs and workflow sequences.

Usage:
    python3 component-integration-tester.py
    python3 component-integration-tester.py --pair file-reader content-sanitizer
"""

import os
import re
import argparse
from typing import Tuple, List, Dict, Any
from pathlib import Path
from itertools import combinations

class ComponentIntegrationTester:
    def __init__(self):
        self.components_dir = Path('.claude/components/atomic')
        self.logical_pairs = [
            ('file-reader', 'content-sanitizer'),
            ('input-validation', 'parameter-parser'),
            ('data-transformer', 'format-converter'),
            ('error-handler', 'progress-indicator'),
            ('file-reader', 'file-writer'),
            ('state-manager', 'workflow-coordinator'),
            ('dependency-resolver', 'completion-tracker'),
            ('api-caller', 'response-validator'),
            ('test-runner', 'git-operations'),
            ('search-files', 'file-reader')
        ]
        
        self.workflow_sequences = [
            ['input-validation', 'parameter-parser', 'file-reader'],
            ['file-reader', 'content-sanitizer', 'data-transformer', 'output-formatter'],
            ['dependency-resolver', 'state-manager', 'workflow-coordinator', 'completion-tracker'],
            ['search-files', 'file-reader', 'format-converter', 'file-writer'],
            ['api-caller', 'response-validator', 'data-transformer', 'output-formatter']
        ]
    
    def _load_component(self, component_name: str) -> str:
        """Load component content from file"""
        component_file = self.components_dir / f"{component_name}.md"
        if not component_file.exists():
            return ""
        
        with open(component_file, 'r') as f:
            return f.read()
    
    def _extract_code_block(self, content: str) -> str:
        """Extract code block content from component"""
        match = re.search(r'```\n(.*?)\n```', content, re.DOTALL)
        return match.group(1) if match else ""
    
    def _get_component_actions(self, content: str) -> List[str]:
        """Extract action verbs from component"""
        code_block = self._extract_code_block(content)
        if not code_block:
            return []
        
        # Extract bullet points
        bullets = [line.strip() for line in code_block.split('\n') if line.strip().startswith('-')]
        actions = []
        
        for bullet in bullets:
            # Extract first verb from each bullet point
            words = bullet.replace('-', '').strip().split()
            if words:
                actions.append(words[0].lower())
        
        return actions
    
    def _test_pair_compatibility(self, component1: str, component2: str) -> Tuple[bool, Dict[str, Any]]:
        """Test if two components are compatible when used together"""
        content1 = self._load_component(component1)
        content2 = self._load_component(component2)
        
        if not content1 or not content2:
            return False, {"error": "Component not found"}
        
        actions1 = self._get_component_actions(content1)
        actions2 = self._get_component_actions(content2)
        
        # Test for conflicts
        conflicting_actions = set(actions1) & set(actions2)
        has_conflicts = len(conflicting_actions) > 0
        
        # Test for complementary actions
        input_actions = ['accept', 'receive', 'parse', 'read', 'extract', 'validate']
        output_actions = ['generate', 'create', 'format', 'write', 'provide', 'return']
        
        comp1_has_input = any(action in actions1 for action in input_actions)
        comp1_has_output = any(action in actions1 for action in output_actions)
        comp2_has_input = any(action in actions2 for action in input_actions)
        comp2_has_output = any(action in actions2 for action in output_actions)
        
        # Good pairing: output of one feeds input of another
        complementary = (comp1_has_output and comp2_has_input) or (comp2_has_output and comp1_has_input)
        
        # Check for interface compatibility
        code1 = self._extract_code_block(content1)
        code2 = self._extract_code_block(content2)
        
        # Look for compatible data types/formats
        data_formats = ['json', 'yaml', 'csv', 'xml', 'text', 'file', 'content', 'data']
        formats1 = [fmt for fmt in data_formats if fmt in code1.lower()]
        formats2 = [fmt for fmt in data_formats if fmt in code2.lower()]
        shared_formats = set(formats1) & set(formats2)
        
        compatibility_score = 0
        if not has_conflicts:
            compatibility_score += 3
        if complementary:
            compatibility_score += 2
        if shared_formats:
            compatibility_score += 2
        if len(actions1) > 2 and len(actions2) > 2:  # Both have sufficient functionality
            compatibility_score += 1
        
        is_compatible = compatibility_score >= 5
        
        return is_compatible, {
            "score": compatibility_score,
            "max_score": 8,
            "conflicts": list(conflicting_actions),
            "complementary": complementary,
            "shared_formats": list(shared_formats),
            "actions1": actions1,
            "actions2": actions2
        }
    
    def _test_workflow_sequence(self, sequence: List[str]) -> Tuple[bool, Dict[str, Any]]:
        """Test if a sequence of components forms a valid workflow"""
        if len(sequence) < 2:
            return False, {"error": "Sequence too short"}
        
        workflow_score = 0
        max_score = (len(sequence) - 1) * 3  # 3 points per adjacent pair
        pair_results = []
        
        # Test each adjacent pair in the sequence
        for i in range(len(sequence) - 1):
            comp1, comp2 = sequence[i], sequence[i + 1]
            is_compatible, details = self._test_pair_compatibility(comp1, comp2)
            
            pair_results.append({
                "pair": f"{comp1} → {comp2}",
                "compatible": is_compatible,
                "score": details.get("score", 0)
            })
            
            workflow_score += details.get("score", 0)
        
        # Check for overall workflow coherence
        first_component = self._load_component(sequence[0])
        last_component = self._load_component(sequence[-1])
        
        first_actions = self._get_component_actions(first_component)
        last_actions = self._get_component_actions(last_component)
        
        # Good workflow: starts with input actions, ends with output actions
        input_actions = ['accept', 'receive', 'parse', 'read', 'extract', 'validate']
        output_actions = ['generate', 'create', 'format', 'write', 'provide', 'return']
        
        starts_with_input = any(action in first_actions for action in input_actions)
        ends_with_output = any(action in last_actions for action in output_actions)
        
        if starts_with_input:
            workflow_score += 2
            max_score += 2
        if ends_with_output:
            workflow_score += 2
            max_score += 2
        
        is_valid_workflow = workflow_score >= (max_score * 0.6)  # 60% threshold
        
        return is_valid_workflow, {
            "score": workflow_score,
            "max_score": max_score,
            "percentage": (workflow_score / max_score * 100) if max_score > 0 else 0,
            "pair_results": pair_results,
            "starts_with_input": starts_with_input,
            "ends_with_output": ends_with_output,
            "sequence": " → ".join(sequence)
        }
    
    def test_logical_pairs(self) -> Dict[str, Any]:
        """Test all predefined logical component pairs"""
        results = []
        passed = 0
        total = len(self.logical_pairs)
        
        print("🔗 TESTING LOGICAL COMPONENT PAIRS")
        print("=" * 50)
        
        for comp1, comp2 in self.logical_pairs:
            is_compatible, details = self._test_pair_compatibility(comp1, comp2)
            
            if is_compatible:
                passed += 1
                status = "✅"
            else:
                status = "❌"
            
            print(f"{status} {comp1} + {comp2}: {details['score']}/{details['max_score']} ({details['score']/details['max_score']*100:.1f}%)")
            
            results.append({
                "pair": f"{comp1} + {comp2}",
                "compatible": is_compatible,
                "details": details
            })
        
        pass_rate = (passed / total * 100) if total > 0 else 0
        print(f"\nLogical Pairs: {passed}/{total} compatible ({pass_rate:.1f}%)")
        
        return {
            "passed": passed,
            "total": total,
            "pass_rate": pass_rate,
            "results": results
        }
    
    def test_workflow_sequences(self) -> Dict[str, Any]:
        """Test all predefined workflow sequences"""
        results = []
        passed = 0
        total = len(self.workflow_sequences)
        
        print("\n🔄 TESTING WORKFLOW SEQUENCES")
        print("=" * 50)
        
        for sequence in self.workflow_sequences:
            is_valid, details = self._test_workflow_sequence(sequence)
            
            if is_valid:
                passed += 1
                status = "✅"
            else:
                status = "❌"
            
            print(f"{status} {details['sequence']}: {details['score']}/{details['max_score']} ({details['percentage']:.1f}%)")
            
            results.append({
                "sequence": details['sequence'],
                "valid": is_valid,
                "details": details
            })
        
        pass_rate = (passed / total * 100) if total > 0 else 0
        print(f"\nWorkflow Sequences: {passed}/{total} valid ({pass_rate:.1f}%)")
        
        return {
            "passed": passed,
            "total": total,
            "pass_rate": pass_rate,
            "results": results
        }
    
    def run_all_tests(self) -> Dict[str, Any]:
        """Run all integration tests"""
        print("🧪 ATOMIC COMPONENT INTEGRATION TESTING")
        print("=" * 60)
        
        pairs_results = self.test_logical_pairs()
        workflow_results = self.test_workflow_sequences()
        
        total_tests = pairs_results['total'] + workflow_results['total']
        total_passed = pairs_results['passed'] + workflow_results['passed']
        overall_pass_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n📊 OVERALL INTEGRATION RESULTS")
        print("=" * 50)
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {total_passed}")
        print(f"Overall Pass Rate: {overall_pass_rate:.1f}%")
        
        if overall_pass_rate >= 70:
            grade = "A" if overall_pass_rate >= 90 else "B"
            print(f"Grade: {grade} ✅")
        else:
            grade = "F" if overall_pass_rate < 50 else "D"
            print(f"Grade: {grade} ❌")
        
        return {
            "pairs": pairs_results,
            "workflows": workflow_results,
            "overall": {
                "total_tests": total_tests,
                "total_passed": total_passed,
                "pass_rate": overall_pass_rate,
                "grade": grade
            }
        }

def main():
    parser = argparse.ArgumentParser(description='Test atomic component integration')
    parser.add_argument('--pair', nargs=2, help='Test specific component pair')
    parser.add_argument('--workflow', nargs='+', help='Test specific workflow sequence')
    args = parser.parse_args()
    
    tester = ComponentIntegrationTester()
    
    if args.pair:
        comp1, comp2 = args.pair
        is_compatible, details = tester._test_pair_compatibility(comp1, comp2)
        print(f"Testing pair: {comp1} + {comp2}")
        print(f"Compatible: {is_compatible}")
        print(f"Score: {details['score']}/{details['max_score']}")
        print(f"Details: {details}")
    elif args.workflow:
        is_valid, details = tester._test_workflow_sequence(args.workflow)
        print(f"Testing workflow: {' → '.join(args.workflow)}")
        print(f"Valid: {is_valid}")
        print(f"Score: {details['score']}/{details['max_score']} ({details['percentage']:.1f}%)")
        print(f"Details: {details}")
    else:
        tester.run_all_tests()

if __name__ == "__main__":
    main()