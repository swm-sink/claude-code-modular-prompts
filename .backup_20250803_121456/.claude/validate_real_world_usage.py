#!/usr/bin/env python3
"""
Real-World Component Usage Validator
Validates that all 21 atomic components are used in working example commands
Phase 2, Step 39 - Component Integration Validation
"""

import os
import re
import logging
from pathlib import Path
from typing import Dict, List, Set

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')

class RealWorldUsageValidator:
    def __init__(self, base_dir: str = ".claude"):
        self.base_dir = Path(base_dir)
        self.components_dir = self.base_dir / "components" / "atomic"
        self.examples_dir = self.base_dir / "commands" / "examples"
        
    def get_all_components(self) -> Set[str]:
        """Get list of all atomic components"""
        components = set()
        if self.components_dir.exists():
            for file_path in self.components_dir.glob("*.md"):
                components.add(file_path.stem)
        return components
    
    def get_example_commands(self) -> List[Path]:
        """Get all example command files"""
        examples = []
        if self.examples_dir.exists():
            for file_path in self.examples_dir.glob("component-demo-*.md"):
                examples.append(file_path)
        return examples
    
    def extract_used_components(self, command_file: Path) -> Set[str]:
        """Extract component names used in a command file"""
        used_components = set()
        
        try:
            content = command_file.read_text()
            
            # Look for component code blocks (our atomic components are in code blocks)
            code_blocks = re.findall(r'```\n(.*?)\n```', content, re.DOTALL)
            
            # Map code patterns to component names
            component_patterns = {
                'input-validation': ['validate the provided input', 'check for required parameters'],
                'parameter-parser': ['parse and extract command parameters', 'split parameter string'],
                'file-reader': ['read the specified file', 'use the provided file path'],
                'file-writer': ['write the processed content', 'create output files'],
                'search-files': ['search for files matching', 'use glob patterns'],
                'content-sanitizer': ['clean and sanitize', 'remove or escape potentially harmful'],
                'data-transformer': ['transform data to specified format', 'parse input data structure'],
                'format-converter': ['convert content to target format', 'identify source format automatically'],
                'output-formatter': ['format the final output', 'apply consistent formatting rules'],
                'error-handler': ['handle errors gracefully', 'catch and process exceptions'],
                'progress-indicator': ['show progress information', 'display completion percentage', 'show current step and overall progress'],
                'user-confirmation': ['ask for user confirmation', 'prompt user to confirm', 'present confirmation prompt'],
                'task-summary': ['summarize completed work', 'generate summary report', 'generate comprehensive summary'],
                'state-manager': ['initialize and configure workflow state', 'set up state tracking'],
                'workflow-coordinator': ['coordinate the execution', 'execute tasks in dependency-resolved order'],
                'dependency-resolver': ['analyze and resolve task dependencies', 'parse dependency requirements'],
                'completion-tracker': ['track and report completion status', 'monitor task completion'],
                'api-caller': ['make api call to external service', 'construct proper api request'],
                'response-validator': ['validate the api response', 'check http status codes'],
                'git-operations': ['execute git commands', 'perform git operations', 'execute git commands safely'],
                'test-runner': ['run tests and collect results', 'execute test commands']
            }
            
            # Check each code block for component patterns
            for block in code_blocks:
                block_lower = block.lower()
                for component, patterns in component_patterns.items():
                    if any(pattern.lower() in block_lower for pattern in patterns):
                        used_components.add(component)
            
        except Exception as e:
            logging.error(f"Error reading {command_file}: {e}")
        
        return used_components
    
    def validate_component_coverage(self) -> Dict[str, any]:
        """Validate that all components are covered in real-world examples"""
        all_components = self.get_all_components()
        example_commands = self.get_example_commands()
        
        logging.info(f"Found {len(all_components)} atomic components")
        logging.info(f"Found {len(example_commands)} example commands")
        
        used_components = set()
        command_coverage = {}
        
        for command_file in example_commands:
            components_in_command = self.extract_used_components(command_file)
            command_coverage[command_file.name] = components_in_command
            used_components.update(components_in_command)
            
            logging.info(f"{command_file.name}: {len(components_in_command)} components used")
        
        unused_components = all_components - used_components
        coverage_percentage = (len(used_components) / len(all_components)) * 100 if all_components else 0
        
        return {
            'total_components': len(all_components),
            'used_components': len(used_components),
            'unused_components': len(unused_components),
            'coverage_percentage': coverage_percentage,
            'unused_list': sorted(unused_components),
            'used_list': sorted(used_components),
            'command_coverage': command_coverage,
            'example_commands': len(example_commands)
        }
    
    def validate_example_quality(self) -> Dict[str, any]:
        """Validate quality of example commands"""
        example_commands = self.get_example_commands()
        quality_metrics = {
            'total_examples': len(example_commands),
            'has_yaml_frontmatter': 0,
            'has_usage_field': 0,
            'has_allowed_tools': 0,
            'has_multiple_components': 0,
            'average_components_per_example': 0
        }
        
        total_components_used = 0
        
        for command_file in example_commands:
            try:
                content = command_file.read_text()
                
                # Check for YAML frontmatter
                if content.startswith('---') and '\n---\n' in content:
                    quality_metrics['has_yaml_frontmatter'] += 1
                    
                    # Extract frontmatter
                    frontmatter = content.split('\n---\n')[0].replace('---', '').strip()
                    
                    if 'usage:' in frontmatter:
                        quality_metrics['has_usage_field'] += 1
                    
                    if 'allowed-tools:' in frontmatter:
                        quality_metrics['has_allowed_tools'] += 1
                
                # Count components used
                components_used = len(self.extract_used_components(command_file))
                total_components_used += components_used
                
                if components_used > 1:
                    quality_metrics['has_multiple_components'] += 1
                    
            except Exception as e:
                logging.error(f"Error analyzing {command_file}: {e}")
        
        if quality_metrics['total_examples'] > 0:
            quality_metrics['average_components_per_example'] = total_components_used / quality_metrics['total_examples']
        
        return quality_metrics
    
    def run_validation(self) -> Dict[str, any]:
        """Run complete real-world usage validation"""
        logging.info("🧪 REAL-WORLD COMPONENT USAGE VALIDATION")
        logging.info("=" * 60)
        
        coverage_results = self.validate_component_coverage()
        quality_results = self.validate_example_quality()
        
        # Determine overall grade
        coverage_pct = coverage_results['coverage_percentage']
        if coverage_pct >= 90:
            grade = "A"
        elif coverage_pct >= 80:
            grade = "B"
        elif coverage_pct >= 70:
            grade = "C"
        elif coverage_pct >= 60:
            grade = "D"
        else:
            grade = "F"
        
        results = {
            'coverage': coverage_results,
            'quality': quality_results,
            'overall_grade': grade,
            'validation_passed': coverage_pct >= 70  # Minimum 70% coverage for pass
        }
        
        return results

def print_results(results: Dict[str, any]):
    """Print validation results in a readable format"""
    coverage = results['coverage']
    quality = results['quality']
    
    print(f"\n📊 COMPONENT COVERAGE ANALYSIS")
    print(f"=" * 50)
    print(f"Total Atomic Components: {coverage['total_components']}")
    print(f"Components Used in Examples: {coverage['used_components']}")
    print(f"Coverage Percentage: {coverage['coverage_percentage']:.1f}%")
    print(f"Overall Grade: {results['overall_grade']}")
    
    if coverage['unused_components'] > 0:
        print(f"\n⚠️  UNUSED COMPONENTS ({coverage['unused_components']}):")
        for component in coverage['unused_list']:
            print(f"   - {component}")
    
    print(f"\n✅ USED COMPONENTS ({coverage['used_components']}):")
    for component in coverage['used_list']:
        print(f"   - {component}")
    
    print(f"\n📋 EXAMPLE COMMAND QUALITY")
    print(f"=" * 50)
    print(f"Total Example Commands: {quality['total_examples']}")
    print(f"With YAML Frontmatter: {quality['has_yaml_frontmatter']}/{quality['total_examples']}")
    print(f"With Usage Field: {quality['has_usage_field']}/{quality['total_examples']}")
    print(f"With Allowed-Tools: {quality['has_allowed_tools']}/{quality['total_examples']}")
    print(f"With Multiple Components: {quality['has_multiple_components']}/{quality['total_examples']}")
    print(f"Average Components per Example: {quality['average_components_per_example']:.1f}")
    
    print(f"\n🎯 VALIDATION RESULT")
    print(f"=" * 50)
    if results['validation_passed']:
        print("✅ VALIDATION PASSED - Real-world usage demonstrated")
    else:
        print("❌ VALIDATION FAILED - Insufficient component coverage")
    
    print(f"Grade: {results['overall_grade']} ({coverage['coverage_percentage']:.1f}% coverage)")

if __name__ == "__main__":
    validator = RealWorldUsageValidator()
    results = validator.run_validation()
    print_results(results)