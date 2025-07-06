#!/usr/bin/env python3
"""
Delegation Pattern Validation Script for Claude Framework
Validates that commands contain only delegation and modules contain full implementation
"""

from pathlib import Path
from typing import Dict, List, Set, Tuple
import re

class DelegationValidator:
    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        self.violations = []
        self.warnings = []
        
    def analyze_command_file(self, file_path: Path) -> Dict:
        """Analyze a command file for delegation compliance"""
        try:
            content = file_path.read_text(encoding='utf-8')
            violations = []
            
            # Check for implementation details in commands (should only delegate)
            implementation_indicators = [
                r'<implementation>',  # Should not have detailed implementation
                r'<actions>',         # Should not have specific actions
                r'<validation>',      # Should not have validation details
                r'def\s+\w+\(',       # Should not have function definitions
                r'class\s+\w+',       # Should not have class definitions
                r'import\s+\w+',      # Should not have imports
                r'from\s+\w+',        # Should not have imports
            ]
            
            for pattern in implementation_indicators:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    violations.append(f"Contains implementation details: {pattern} ({len(matches)} occurrences)")
            
            # Check for required delegation elements
            required_delegation = [
                r'delegates_to=',          # Should reference modules
                r'reference.*modules/',    # Should reference module files
                r'See.*modules/',          # Should see module files
            ]
            
            delegation_found = False
            for pattern in required_delegation:
                if re.search(pattern, content, re.IGNORECASE):
                    delegation_found = True
                    break
            
            if not delegation_found:
                violations.append("Missing delegation references to modules")
            
            return {
                'file': str(file_path.relative_to(self.framework_root)),
                'type': 'command',
                'violations': violations,
                'compliant': len(violations) == 0
            }
            
        except Exception as e:
            return {
                'file': str(file_path.relative_to(self.framework_root)),
                'type': 'command',
                'violations': [f"Error analyzing file: {str(e)}"],
                'compliant': False
            }
    
    def analyze_module_file(self, file_path: Path) -> Dict:
        """Analyze a module file for implementation completeness"""
        try:
            content = file_path.read_text(encoding='utf-8')
            violations = []
            
            # Check for required implementation elements in modules
            required_elements = [
                (r'<purpose>', "Missing purpose definition"),
                (r'<trigger_conditions>', "Missing trigger conditions"),
                (r'<implementation[^>]*>', "Missing implementation section"),
            ]
            
            for pattern, error_msg in required_elements:
                if not re.search(pattern, content, re.IGNORECASE):
                    violations.append(error_msg)
            
            # Check that modules don't just delegate (should have implementation)
            delegation_only_indicators = [
                r'^.*delegates to.*modules/.*$',  # Lines that only delegate
                r'^.*See modules/.*for.*$',       # Lines that only reference
            ]
            
            lines = content.split('\n')
            implementation_lines = 0
            delegation_lines = 0
            
            for line in lines:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                    
                is_delegation = False
                for pattern in delegation_only_indicators:
                    if re.match(pattern, line, re.IGNORECASE):
                        delegation_lines += 1
                        is_delegation = True
                        break
                
                if not is_delegation and len(line) > 20:  # Meaningful content
                    implementation_lines += 1
            
            if delegation_lines > implementation_lines:
                violations.append("Module appears to delegate more than implement")
            
            return {
                'file': str(file_path.relative_to(self.framework_root)),
                'type': 'module',
                'violations': violations,
                'compliant': len(violations) == 0,
                'implementation_lines': implementation_lines,
                'delegation_lines': delegation_lines
            }
            
        except Exception as e:
            return {
                'file': str(file_path.relative_to(self.framework_root)),
                'type': 'module',
                'violations': [f"Error analyzing file: {str(e)}"],
                'compliant': False
            }
    
    def check_reference_accuracy(self) -> List[Dict]:
        """Check that all module references in commands point to existing files"""
        violations = []
        
        # Find all command files
        command_files = list((self.framework_root / "commands").glob("*.md"))
        
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                
                # Find module references
                module_refs = re.findall(r'modules/([^.\s]+\.md)', content)
                
                for ref in module_refs:
                    module_path = self.framework_root / "modules" / ref
                    if not module_path.exists():
                        violations.append({
                            'file': str(cmd_file.relative_to(self.framework_root)),
                            'violation': f"References non-existent module: modules/{ref}",
                            'type': 'broken_reference'
                        })
                        
            except Exception as e:
                violations.append({
                    'file': str(cmd_file.relative_to(self.framework_root)),
                    'violation': f"Error checking references: {str(e)}",
                    'type': 'error'
                })
        
        return violations
    
    def check_content_redundancy(self) -> List[Dict]:
        """Check for redundant content between commands and modules"""
        redundancy_issues = []
        
        # Get all file contents
        all_files = {}
        
        # Read command files
        for cmd_file in (self.framework_root / "commands").glob("*.md"):
            content = cmd_file.read_text(encoding='utf-8')
            all_files[f"commands/{cmd_file.name}"] = content
        
        # Read module files
        for module_file in (self.framework_root / "modules").rglob("*.md"):
            rel_path = module_file.relative_to(self.framework_root)
            content = module_file.read_text(encoding='utf-8')
            all_files[str(rel_path)] = content
        
        # Look for similar content blocks (simplified check)
        checked_pairs = set()
        
        for file1, content1 in all_files.items():
            for file2, content2 in all_files.items():
                if file1 >= file2:  # Avoid duplicate comparisons
                    continue
                
                pair = tuple(sorted([file1, file2]))
                if pair in checked_pairs:
                    continue
                checked_pairs.add(pair)
                
                # Find common lines (>10 words each)
                lines1 = [line.strip() for line in content1.split('\n') if len(line.split()) > 10]
                lines2 = [line.strip() for line in content2.split('\n') if len(line.split()) > 10]
                
                common_lines = set(lines1) & set(lines2)
                
                if len(common_lines) > 2:  # Threshold for redundancy
                    redundancy_issues.append({
                        'file1': file1,
                        'file2': file2,
                        'common_lines': len(common_lines),
                        'sample_redundancy': list(common_lines)[:3]
                    })
        
        return redundancy_issues
    
    def validate_all(self) -> Dict:
        """Run complete delegation pattern validation"""
        results = {
            'command_analysis': [],
            'module_analysis': [],
            'reference_accuracy': [],
            'redundancy_check': [],
            'summary': {
                'total_commands': 0,
                'compliant_commands': 0,
                'total_modules': 0,
                'compliant_modules': 0,
                'broken_references': 0,
                'redundancy_issues': 0
            }
        }
        
        # Analyze command files
        command_files = list((self.framework_root / "commands").glob("*.md"))
        for cmd_file in command_files:
            analysis = self.analyze_command_file(cmd_file)
            results['command_analysis'].append(analysis)
            results['summary']['total_commands'] += 1
            if analysis['compliant']:
                results['summary']['compliant_commands'] += 1
        
        # Analyze module files
        module_files = list((self.framework_root / "modules").rglob("*.md"))
        for mod_file in module_files:
            analysis = self.analyze_module_file(mod_file)
            results['module_analysis'].append(analysis)
            results['summary']['total_modules'] += 1
            if analysis['compliant']:
                results['summary']['compliant_modules'] += 1
        
        # Check reference accuracy
        ref_violations = self.check_reference_accuracy()
        results['reference_accuracy'] = ref_violations
        results['summary']['broken_references'] = len(ref_violations)
        
        # Check redundancy
        redundancy = self.check_content_redundancy()
        results['redundancy_check'] = redundancy
        results['summary']['redundancy_issues'] = len(redundancy)
        
        return results
    
    def generate_report(self, results: Dict) -> str:
        """Generate comprehensive delegation validation report"""
        report = []
        report.append("=" * 80)
        report.append("CLAUDE FRAMEWORK DELEGATION PATTERN VALIDATION REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Summary
        summary = results['summary']
        report.append("SUMMARY STATISTICS:")
        report.append(f"- Command files analyzed: {summary['total_commands']}")
        report.append(f"- Command files compliant: {summary['compliant_commands']}")
        report.append(f"- Module files analyzed: {summary['total_modules']}")
        report.append(f"- Module files compliant: {summary['compliant_modules']}")
        report.append(f"- Broken references found: {summary['broken_references']}")
        report.append(f"- Redundancy issues found: {summary['redundancy_issues']}")
        report.append("")
        
        # Command violations
        command_violations = [r for r in results['command_analysis'] if not r['compliant']]
        if command_violations:
            report.append("COMMAND DELEGATION VIOLATIONS:")
            report.append("-" * 40)
            for violation in command_violations:
                report.append(f"\n{violation['file']}:")
                for v in violation['violations']:
                    report.append(f"  ❌ {v}")
        else:
            report.append("✅ ALL COMMANDS PROPERLY DELEGATE")
        
        report.append("")
        
        # Module violations
        module_violations = [r for r in results['module_analysis'] if not r['compliant']]
        if module_violations:
            report.append("MODULE IMPLEMENTATION VIOLATIONS:")
            report.append("-" * 40)
            for violation in module_violations:
                report.append(f"\n{violation['file']}:")
                for v in violation['violations']:
                    report.append(f"  ❌ {v}")
        else:
            report.append("✅ ALL MODULES PROPERLY IMPLEMENT")
        
        report.append("")
        
        # Reference accuracy
        if results['reference_accuracy']:
            report.append("BROKEN REFERENCES:")
            report.append("-" * 40)
            for ref_issue in results['reference_accuracy']:
                report.append(f"  ❌ {ref_issue['file']}: {ref_issue['violation']}")
        else:
            report.append("✅ ALL MODULE REFERENCES ACCURATE")
        
        report.append("")
        
        # Redundancy
        if results['redundancy_check']:
            report.append("CONTENT REDUNDANCY ISSUES:")
            report.append("-" * 40)
            for redundancy in results['redundancy_check']:
                report.append(f"  ⚠️  {redundancy['file1']} ↔ {redundancy['file2']}: {redundancy['common_lines']} common lines")
        else:
            report.append("✅ NO SIGNIFICANT CONTENT REDUNDANCY")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)

def main():
    framework_root = "/Users/smenssink/Documents/Github personal projects/claude-code-modular-agents/.claude"
    
    validator = DelegationValidator(framework_root)
    results = validator.validate_all()
    report = validator.generate_report(results)
    
    print(report)
    
    # Save report
    report_file = Path(framework_root) / "delegation_report.txt"
    report_file.write_text(report)
    print(f"\nReport saved to: {report_file}")
    
    # Return exit code based on violations
    total_violations = (
        len([r for r in results['command_analysis'] if not r['compliant']]) +
        len([r for r in results['module_analysis'] if not r['compliant']]) +
        len(results['reference_accuracy'])
    )
    
    return 1 if total_violations > 0 else 0

if __name__ == "__main__":
    import sys
    sys.exit(main())