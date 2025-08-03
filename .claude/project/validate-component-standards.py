#!/usr/bin/env python3
"""
Atomic Component Standards Validation Script

Tests components against the architectural standards defined in
ATOMIC-COMPONENT-ARCHITECTURE-STANDARDS.md

Usage:
    python3 validate-component-standards.py [component_file]
    python3 validate-component-standards.py --all
"""

import os
import re
import argparse
from typing import Tuple, List, Dict
from pathlib import Path

class ComponentValidator:
    def __init__(self):
        self.standards = {
            'length_min': 5,
            'length_max': 10,
            'required_structure': True,
            'clear_purpose': True,
            'independence': True,
            'naming_convention': True
        }
    
    def validate_component(self, file_path: str) -> Tuple[bool, Dict[str, any]]:
        """Validate a component against architecture standards"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return False, {'error': f"Could not read file: {e}"}
        
        results = {
            'file': file_path,
            'valid': True,
            'checks': {},
            'score': 0,
            'total_checks': 8
        }
        
        # Check 1: File naming convention
        filename = Path(file_path).name
        kebab_case_pattern = r'^[a-z]+(-[a-z]+)*\.md$'
        naming_valid = re.match(kebab_case_pattern, filename) is not None
        results['checks']['naming_convention'] = {
            'pass': naming_valid,
            'details': f"Filename follows kebab-case pattern: {filename}"
        }
        if naming_valid:
            results['score'] += 1
        
        # Check 2: Title format
        title_match = re.search(r'^# (.+) Component\s*$', content, re.MULTILINE)
        title_valid = title_match is not None
        results['checks']['title_format'] = {
            'pass': title_valid,
            'details': f"Has proper '# [Name] Component' title format"
        }
        if title_valid:
            results['score'] += 1
        
        # Check 3: Code block structure
        code_block_pattern = r'```\n(.*?)\n```'
        code_blocks = re.findall(code_block_pattern, content, re.DOTALL)
        has_code_block = len(code_blocks) > 0
        results['checks']['code_block_structure'] = {
            'pass': has_code_block,
            'details': f"Contains proper code block structure: {len(code_blocks)} blocks found"
        }
        if has_code_block:
            results['score'] += 1
        
        # Check 4: Content length (bullet points)
        if code_blocks:
            main_content = code_blocks[0]
            bullet_lines = [line.strip() for line in main_content.split('\n') 
                           if line.strip().startswith('-')]
            content_length = len(bullet_lines)
            length_valid = self.standards['length_min'] <= content_length <= self.standards['length_max']
            results['checks']['content_length'] = {
                'pass': length_valid,
                'details': f"Content length: {content_length} lines (target: {self.standards['length_min']}-{self.standards['length_max']})"
            }
            if length_valid:
                results['score'] += 1
        else:
            results['checks']['content_length'] = {
                'pass': False,
                'details': "No code block found to measure content length"
            }
        
        # Check 5: Clear action items
        if code_blocks:
            main_content = code_blocks[0]
            has_action_items = '-' in main_content
            results['checks']['clear_actions'] = {
                'pass': has_action_items,
                'details': f"Contains clear action items (bullet points)"
            }
            if has_action_items:
                results['score'] += 1
        else:
            results['checks']['clear_actions'] = {
                'pass': False,
                'details': "No content to evaluate for action items"
            }
        
        # Check 6: Single responsibility
        if title_match:
            title = title_match.group(1)
            # Simple heuristic: title should describe one clear purpose
            single_purpose = len(title.split(' and ')) == 1 and len(title.split('/')) == 1
            results['checks']['single_responsibility'] = {
                'pass': single_purpose,
                'details': f"Title suggests single responsibility: '{title}'"
            }
            if single_purpose:
                results['score'] += 1
        else:
            results['checks']['single_responsibility'] = {
                'pass': False,
                'details': "Cannot evaluate responsibility from title"
            }
        
        # Check 7: No external dependencies  
        # Look for actual dependency patterns, not just keywords
        dependency_patterns = [
            r'\bimport\s+\w+',
            r'\brequire\s*\(',
            r'\binclude\s+["\']',
            r'\bfrom\s+[\.\/]',
            r'\bcall\s+\w+\('
        ]
        has_dependencies = any(re.search(pattern, content, re.IGNORECASE) for pattern in dependency_patterns)
        results['checks']['independence'] = {
            'pass': not has_dependencies,
            'details': f"Dependencies detected: {has_dependencies}" if has_dependencies else "No external dependencies detected"
        }
        if not has_dependencies:
            results['score'] += 1
        
        # Check 8: Reasonable token efficiency
        token_count = len(content.split())
        efficient = token_count < 100  # Reasonable threshold
        results['checks']['token_efficiency'] = {
            'pass': efficient,
            'details': f"Token count: {token_count} (efficient: <100)"
        }
        if efficient:
            results['score'] += 1
        
        # Overall validation
        results['valid'] = results['score'] >= 6  # Must pass at least 75% of checks
        results['percentage'] = (results['score'] / results['total_checks']) * 100
        
        return results['valid'], results
    
    def validate_all_components(self, components_dir: str = '.claude/components/atomic') -> Dict[str, any]:
        """Validate all components in the atomic directory"""
        if not os.path.exists(components_dir):
            return {'error': f"Components directory not found: {components_dir}"}
        
        results = {
            'directory': components_dir,
            'total_components': 0,
            'valid_components': 0,
            'components': {},
            'summary': {}
        }
        
        for filename in os.listdir(components_dir):
            if filename.endswith('.md'):
                file_path = os.path.join(components_dir, filename)
                results['total_components'] += 1
                
                is_valid, component_results = self.validate_component(file_path)
                results['components'][filename] = component_results
                
                if is_valid:
                    results['valid_components'] += 1
        
        if results['total_components'] > 0:
            results['summary'] = {
                'compliance_rate': (results['valid_components'] / results['total_components']) * 100,
                'total_score': sum(comp['score'] for comp in results['components'].values()),
                'max_possible_score': results['total_components'] * 8,
                'average_score': sum(comp['score'] for comp in results['components'].values()) / results['total_components']
            }
        
        return results
    
    def print_results(self, results: Dict[str, any]):
        """Print formatted validation results"""
        if 'error' in results:
            print(f"❌ Error: {results['error']}")
            return
        
        print("🧪 ATOMIC COMPONENT STANDARDS VALIDATION")
        print("=" * 50)
        print(f"Directory: {results['directory']}")
        print(f"Components Found: {results['total_components']}")
        print(f"Valid Components: {results['valid_components']}")
        print(f"Compliance Rate: {results['summary'].get('compliance_rate', 0):.1f}%")
        print()
        
        for filename, component in results['components'].items():
            status = "✅" if component['valid'] else "❌"
            print(f"{status} {filename} - {component['score']}/{component['total_checks']} ({component['percentage']:.1f}%)")
            
            if not component['valid']:
                print("   Failed checks:")
                for check_name, check_result in component['checks'].items():
                    if not check_result['pass']:
                        print(f"   • {check_name}: {check_result['details']}")
                print()

def main():
    parser = argparse.ArgumentParser(description="Validate atomic components against architecture standards")
    parser.add_argument('component', nargs='?', help='Specific component file to validate')
    parser.add_argument('--all', action='store_true', help='Validate all components')
    
    args = parser.parse_args()
    
    validator = ComponentValidator()
    
    if args.all or args.component is None:
        results = validator.validate_all_components()
        validator.print_results(results)
    else:
        if not os.path.exists(args.component):
            print(f"❌ Component file not found: {args.component}")
            return 1
        
        is_valid, results = validator.validate_component(args.component)
        
        status = "✅" if is_valid else "❌"
        print(f"{status} {results['file']} - {results['score']}/{results['total_checks']} ({results['percentage']:.1f}%)")
        print()
        
        for check_name, check_result in results['checks'].items():
            status = "✅" if check_result['pass'] else "❌"
            print(f"{status} {check_name}: {check_result['details']}")
        
        return 0 if is_valid else 1

if __name__ == "__main__":
    exit(main())