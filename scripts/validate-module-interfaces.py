#!/usr/bin/env python3
"""
Agent V14: Module Interface Validator
Validates that all modules follow proper interface contracts and patterns.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class ModuleInterfaceValidator:
    def __init__(self, modules_dir: str):
        self.modules_dir = Path(modules_dir)
        self.validation_results = {
            "total_modules": 0,
            "valid_modules": 0,
            "invalid_modules": 0,
            "missing_sections": {},
            "category_mismatches": [],
            "thinking_pattern_issues": [],
            "interface_contract_issues": [],
            "error_handling_issues": [],
            "version_issues": []
        }
        
    def validate_all_modules(self) -> Dict:
        """Validate all modules in the framework."""
        module_files = list(self.modules_dir.rglob("*.md"))
        module_files = [f for f in module_files if f.name != "README.md"]
        
        self.validation_results["total_modules"] = len(module_files)
        
        for module_file in module_files:
            self.validate_module(module_file)
            
        self.validation_results["valid_modules"] = (
            self.validation_results["total_modules"] - 
            self.validation_results["invalid_modules"]
        )
        
        return self.validation_results
    
    def validate_module(self, module_path: Path):
        """Validate a single module."""
        relative_path = module_path.relative_to(self.modules_dir)
        
        try:
            with open(module_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.validation_results["invalid_modules"] += 1
            return
        
        # Check required sections
        issues = []
        
        # 1. Version header
        if not self._has_version_header(content):
            issues.append("version_header")
            self.validation_results["version_issues"].append(str(relative_path))
        
        # 2. Purpose statement
        if not self._has_purpose_statement(content):
            issues.append("purpose_statement")
        
        # 3. Interface/API definition
        if not self._has_interface_definition(content):
            issues.append("interface_definition")
            self.validation_results["interface_contract_issues"].append(str(relative_path))
        
        # 4. Dependencies declaration
        if not self._has_dependencies_declaration(content):
            issues.append("dependencies_declaration")
        
        # 5. Usage examples
        if not self._has_usage_examples(content):
            issues.append("usage_examples")
        
        # 6. Check thinking patterns where required
        if self._requires_thinking_pattern(relative_path) and not self._has_thinking_pattern(content):
            self.validation_results["thinking_pattern_issues"].append(str(relative_path))
            issues.append("thinking_pattern")
        
        # 7. Check error handling patterns
        if not self._has_error_handling(content):
            self.validation_results["error_handling_issues"].append(str(relative_path))
            issues.append("error_handling")
        
        # 8. Validate category matches functionality
        if not self._validate_category_match(relative_path, content):
            self.validation_results["category_mismatches"].append(str(relative_path))
        
        # Record issues
        if issues:
            self.validation_results["invalid_modules"] += 1
            self.validation_results["missing_sections"][str(relative_path)] = issues
    
    def _has_version_header(self, content: str) -> bool:
        """Check if module has proper version header."""
        version_patterns = [
            r'\| version \| last_updated \| status \|',
            r'<version>.*?</version>',
            r'version:\s*\d+\.\d+\.\d+'
        ]
        return any(re.search(pattern, content, re.IGNORECASE | re.DOTALL) for pattern in version_patterns)
    
    def _has_purpose_statement(self, content: str) -> bool:
        """Check if module has purpose statement."""
        purpose_patterns = [
            r'<purpose>.*?</purpose>',
            r'## Purpose\s*\n',
            r'# .*? Module\s*\n'  # Module title often serves as purpose
        ]
        return any(re.search(pattern, content, re.IGNORECASE | re.DOTALL) for pattern in purpose_patterns)
    
    def _has_interface_definition(self, content: str) -> bool:
        """Check if module has interface/API definition."""
        interface_patterns = [
            r'<interface_contract>.*?</interface_contract>',
            r'<inputs>.*?</inputs>',
            r'<outputs>.*?</outputs>',
            r'## Interface\s*\n',
            r'## API\s*\n'
        ]
        return any(re.search(pattern, content, re.IGNORECASE | re.DOTALL) for pattern in interface_patterns)
    
    def _has_dependencies_declaration(self, content: str) -> bool:
        """Check if module has dependencies declaration."""
        dependency_patterns = [
            r'<depends_on>.*?</depends_on>',
            r'<dependencies>.*?</dependencies>',
            r'## Dependencies\s*\n',
            r'<integration_points>.*?</integration_points>'
        ]
        return any(re.search(pattern, content, re.IGNORECASE | re.DOTALL) for pattern in dependency_patterns)
    
    def _has_usage_examples(self, content: str) -> bool:
        """Check if module has usage examples."""
        example_patterns = [
            r'<usage_examples>.*?</usage_examples>',
            r'<examples>.*?</examples>',
            r'## Usage\s*\n',
            r'## Examples?\s*\n',
            r'<pattern_usage>.*?</pattern_usage>'
        ]
        return any(re.search(pattern, content, re.IGNORECASE | re.DOTALL) for pattern in example_patterns)
    
    def _has_thinking_pattern(self, content: str) -> bool:
        """Check if module has thinking patterns."""
        thinking_patterns = [
            r'<thinking_pattern>.*?</thinking_pattern>',
            r'<critical_thinking>.*?</critical_thinking>',
            r'<interleaved_thinking>.*?</interleaved_thinking>',
            r'thinking_mode='
        ]
        return any(re.search(pattern, content, re.IGNORECASE | re.DOTALL) for pattern in thinking_patterns)
    
    def _has_error_handling(self, content: str) -> bool:
        """Check if module has error handling patterns."""
        error_patterns = [
            r'<error_handling>.*?</error_handling>',
            r'<failure>.*?</failure>',
            r'<recovery>.*?</recovery>',
            r'<blocking_conditions>.*?</blocking_conditions>',
            r'## Error Handling\s*\n'
        ]
        return any(re.search(pattern, content, re.IGNORECASE | re.DOTALL) for pattern in error_patterns)
    
    def _requires_thinking_pattern(self, relative_path: Path) -> bool:
        """Determine if module requires thinking patterns."""
        # Modules that typically require thinking patterns
        thinking_required = [
            'patterns/critical-thinking-pattern.md',
            'patterns/thinking-pattern-template.md',
            'quality/',  # Quality modules often need thinking patterns
            'meta/',     # Meta modules often need advanced thinking
            'routing',   # Routing decisions need thinking
            'analysis'   # Analysis modules need thinking
        ]
        
        path_str = str(relative_path)
        return any(req in path_str for req in thinking_required)
    
    def _validate_category_match(self, relative_path: Path, content: str) -> bool:
        """Validate module category matches its functionality."""
        # Extract category from path
        path_parts = relative_path.parts
        if len(path_parts) < 2:
            return True  # Can't validate root-level files
        
        path_category = path_parts[0]
        
        # Extract category from content
        category_match = re.search(r'<module.*?category="([^"]+)"', content)
        if not category_match:
            return True  # No explicit category in content
        
        content_category = category_match.group(1)
        
        # Map path categories to content categories
        category_map = {
            'patterns': 'patterns',
            'quality': 'quality',
            'security': 'security',
            'development': 'development',
            'meta': 'meta'
        }
        
        expected_category = category_map.get(path_category, path_category)
        return content_category == expected_category
    
    def generate_report(self) -> str:
        """Generate validation report."""
        report = []
        report.append("# Module Interface Validation Report\n")
        report.append(f"**Total Modules:** {self.validation_results['total_modules']}")
        report.append(f"**Valid Modules:** {self.validation_results['valid_modules']}")
        report.append(f"**Invalid Modules:** {self.validation_results['invalid_modules']}\n")
        
        # Missing sections
        if self.validation_results["missing_sections"]:
            report.append("## Modules with Missing Sections\n")
            for module, sections in self.validation_results["missing_sections"].items():
                report.append(f"### {module}")
                report.append(f"Missing: {', '.join(sections)}\n")
        
        # Version issues
        if self.validation_results["version_issues"]:
            report.append("## Modules with Version Header Issues\n")
            for module in self.validation_results["version_issues"]:
                report.append(f"- {module}")
            report.append("")
        
        # Interface contract issues
        if self.validation_results["interface_contract_issues"]:
            report.append("## Modules with Interface Contract Issues\n")
            for module in self.validation_results["interface_contract_issues"]:
                report.append(f"- {module}")
            report.append("")
        
        # Thinking pattern issues
        if self.validation_results["thinking_pattern_issues"]:
            report.append("## Modules Missing Required Thinking Patterns\n")
            for module in self.validation_results["thinking_pattern_issues"]:
                report.append(f"- {module}")
            report.append("")
        
        # Error handling issues
        if self.validation_results["error_handling_issues"]:
            report.append("## Modules with Error Handling Issues\n")
            for module in self.validation_results["error_handling_issues"]:
                report.append(f"- {module}")
            report.append("")
        
        # Category mismatches
        if self.validation_results["category_mismatches"]:
            report.append("## Modules with Category Mismatches\n")
            for module in self.validation_results["category_mismatches"]:
                report.append(f"- {module}")
            report.append("")
        
        # Summary
        report.append("## Summary\n")
        report.append(f"- **Compliance Rate:** {self.validation_results['valid_modules'] / self.validation_results['total_modules'] * 100:.1f}%")
        report.append(f"- **Most Common Issue:** {self._get_most_common_issue()}")
        report.append(f"- **Critical Issues:** {len(self.validation_results['interface_contract_issues'])} modules lack proper interface contracts")
        
        return "\n".join(report)
    
    def _get_most_common_issue(self) -> str:
        """Identify most common issue type."""
        issue_counts = {}
        for sections in self.validation_results["missing_sections"].values():
            for section in sections:
                issue_counts[section] = issue_counts.get(section, 0) + 1
        
        if not issue_counts:
            return "None"
        
        return max(issue_counts, key=issue_counts.get)


def main():
    modules_dir = "/Users/smenssink/Documents/Github/claude-code-modular-prompts/.claude/modules"
    validator = ModuleInterfaceValidator(modules_dir)
    
    print("Validating module interfaces...")
    results = validator.validate_all_modules()
    
    # Generate report
    report = validator.generate_report()
    
    # Save report
    report_path = "/Users/smenssink/Documents/Github/claude-code-modular-prompts/internal/reports/agents/V14_INTERFACE_VALIDATION_REPORT.md"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Save raw results
    results_path = "/Users/smenssink/Documents/Github/claude-code-modular-prompts/internal/data/v14-validation-results.json"
    os.makedirs(os.path.dirname(results_path), exist_ok=True)
    
    with open(results_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nValidation complete!")
    print(f"Report saved to: {report_path}")
    print(f"Raw results saved to: {results_path}")
    print(f"\nSummary:")
    print(f"- Total Modules: {results['total_modules']}")
    print(f"- Valid Modules: {results['valid_modules']}")
    print(f"- Invalid Modules: {results['invalid_modules']}")
    print(f"- Compliance Rate: {results['valid_modules'] / results['total_modules'] * 100:.1f}%")


if __name__ == "__main__":
    main()