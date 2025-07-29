#!/usr/bin/env python3
"""
Development Command Consolidation Validation Script

This script validates that the unified /dev command preserves all functionality
from the original individual development commands.

Usage: python dev-consolidation-validation.py
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

class DevConsolidationValidator:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.deprecated_commands = [
            "development/code/code-format.md",
            "development/code/code-lint.md", 
            "development/code/debug.md",
            "development/code/dev-refactor.md",
            "development/code/feature.md",
            "development/code/new.md",
            "development/code/existing.md",
            "development/project/deps-update.md"
        ]
        self.unified_command = "development/dev.md"
        
    def extract_functionality(self, command_file: str) -> Dict:
        """Extract key functionality from a command file."""
        file_path = self.base_path / command_file
        if not file_path.exists():
            return {}
            
        content = file_path.read_text()
        
        # Extract metadata
        metadata = {}
        if '---' in content:
            yaml_section = content.split('---')[1]
            for line in yaml_section.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip().strip('"')
        
        # Extract usage patterns
        usage_patterns = re.findall(r'```bash\n(.*?)\n```', content, re.DOTALL)
        
        # Extract arguments
        arguments = re.findall(r'<argument name="([^"]*)"[^>]*>', content)
        
        # Extract examples
        examples = re.findall(r'<usage>(.*?)</usage>', content)
        
        return {
            'metadata': metadata,
            'usage_patterns': usage_patterns,
            'arguments': arguments,
            'examples': examples,
            'file_path': command_file
        }
    
    def validate_mode_mapping(self) -> List[str]:
        """Validate that all deprecated commands map to appropriate modes."""
        issues = []
        
        mode_mappings = {
            'code-format.md': 'format',
            'code-lint.md': 'lint',
            'debug.md': 'debug', 
            'dev-refactor.md': 'refactor',
            'feature.md': 'feature',
            'new.md': 'init',
            'existing.md': 'analyze',
            'deps-update.md': 'deps'
        }
        
        # Read unified command
        unified_path = self.base_path / self.unified_command
        unified_content = unified_path.read_text()
        
        for cmd_file, expected_mode in mode_mappings.items():
            if expected_mode not in unified_content:
                issues.append(f"Mode '{expected_mode}' not found in unified command (expected from {cmd_file})")
        
        return issues
    
    def validate_functionality_preservation(self) -> List[str]:
        """Validate that all key functionality is preserved."""
        issues = []
        
        # Extract functionality from all deprecated commands
        deprecated_functionality = {}
        for cmd_file in self.deprecated_commands:
            cmd_name = Path(cmd_file).stem
            deprecated_functionality[cmd_name] = self.extract_functionality(cmd_file)
        
        # Extract functionality from unified command
        unified_functionality = self.extract_functionality(self.unified_command)
        
        # Validate arguments preservation
        for cmd_name, func_data in deprecated_functionality.items():
            for arg in func_data.get('arguments', []):
                if arg not in str(unified_functionality.get('arguments', [])):
                    # Check if argument is mapped to a different name in unified command
                    unified_content = (self.base_path / self.unified_command).read_text()
                    if arg not in unified_content:
                        issues.append(f"Argument '{arg}' from {cmd_name} not preserved in unified command")
        
        return issues
    
    def validate_deprecation_notices(self) -> List[str]:
        """Validate that all deprecated commands have proper deprecation notices."""
        issues = []
        
        required_fields = ['deprecated', 'deprecation_date', 'replacement', 'removal_date']
        
        for cmd_file in self.deprecated_commands:
            func_data = self.extract_functionality(cmd_file)
            metadata = func_data.get('metadata', {})
            
            for field in required_fields:
                if field not in metadata:
                    issues.append(f"Missing deprecation field '{field}' in {cmd_file}")
            
            # Check for deprecation notice in content
            file_path = self.base_path / cmd_file
            content = file_path.read_text()
            if "DEPRECATION NOTICE" not in content:
                issues.append(f"Missing deprecation notice in content of {cmd_file}")
        
        return issues
    
    def validate_unified_command_completeness(self) -> List[str]:
        """Validate that the unified command is complete and well-structured."""
        issues = []
        
        unified_path = self.base_path / self.unified_command
        content = unified_path.read_text()
        
        # Check for required modes
        required_modes = ['format', 'lint', 'refactor', 'debug', 'feature', 'init', 'analyze', 'deps']
        for mode in required_modes:
            if f'<{mode}_mode>' not in content:
                issues.append(f"Missing mode section '{mode}_mode' in unified command")
        
        # Check for proper argument definitions
        if '<arguments>' not in content:
            issues.append("Missing arguments section in unified command")
        
        # Check for examples
        if '<examples>' not in content:
            issues.append("Missing examples section in unified command")
        
        # Check for proper dependencies
        if '<dependencies>' not in content:
            issues.append("Missing dependencies section in unified command")
        
        return issues
    
    def run_validation(self) -> Dict[str, List[str]]:
        """Run complete validation and return results."""
        results = {
            'mode_mapping': self.validate_mode_mapping(),
            'functionality_preservation': self.validate_functionality_preservation(), 
            'deprecation_notices': self.validate_deprecation_notices(),
            'unified_completeness': self.validate_unified_command_completeness()
        }
        
        return results
    
    def generate_report(self) -> str:
        """Generate a comprehensive validation report."""
        results = self.run_validation()
        
        report = "# Development Command Consolidation Validation Report\n\n"
        
        total_issues = sum(len(issues) for issues in results.values())
        
        if total_issues == 0:
            report += "✅ **VALIDATION PASSED** - All checks completed successfully!\n\n"
        else:
            report += f"❌ **VALIDATION FAILED** - {total_issues} issues found\n\n"
        
        for category, issues in results.items():
            report += f"## {category.replace('_', ' ').title()}\n\n"
            
            if not issues:
                report += "✅ All checks passed\n\n"
            else:
                report += f"❌ {len(issues)} issues found:\n\n"
                for issue in issues:
                    report += f"- {issue}\n"
                report += "\n"
        
        # Add summary statistics
        report += "## Summary Statistics\n\n"
        report += f"- Deprecated commands validated: {len(self.deprecated_commands)}\n"
        report += f"- Total validation categories: {len(results.keys())}\n"
        report += f"- Issues found: {total_issues}\n"
        successful_categories = len([category for category, issues in results.items() if not issues])
        report += f"- Success rate: {((successful_categories / len(results.keys())) * 100):.1f}%\n"
        
        return report

def main():
    """Main validation function."""
    validator = DevConsolidationValidator()
    report = validator.generate_report()
    
    # Save report
    report_path = Path(__file__).parent / "DEV-CONSOLIDATION-VALIDATION-REPORT.md"
    report_path.write_text(report)
    
    print(f"Validation complete. Report saved to: {report_path}")
    print("\n" + "="*60)
    print(report)

if __name__ == "__main__":
    main()