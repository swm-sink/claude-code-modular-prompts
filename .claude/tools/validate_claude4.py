#!/usr/bin/env python3
"""
Claude 4 Feature Validation Script for Claude Framework
Validates Claude 4 specific optimizations and patterns
"""

from pathlib import Path
from typing import Dict, List, Set, Tuple
import re
import json

class Claude4Validator:
    def __init__(self, framework_root: str):
        self.framework_root = Path(framework_root)
        
    def validate_xml_structure(self) -> Dict:
        """Validate XML structure implementation across framework"""
        results = {
            'files_with_xml': 0,
            'total_files': 0,
            'xml_coverage': 0.0,
            'issues': []
        }
        
        md_files = list(self.framework_root.rglob("*.md"))
        results['total_files'] = len(md_files)
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                
                # Check for XML tags
                if re.search(r'<\w+[^>]*>', content):
                    results['files_with_xml'] += 1
                    
                    # Check for proper XML structure
                    if not re.search(r'<module[^>]*>', content) and not re.search(r'<command[^>]*>', content):
                        if 'README' not in file_path.name and 'PERMISSION' not in file_path.name:
                            results['issues'].append(f"{file_path.relative_to(self.framework_root)}: Missing root XML structure")
                            
            except Exception as e:
                results['issues'].append(f"{file_path.relative_to(self.framework_root)}: Error reading file: {e}")
        
        results['xml_coverage'] = (results['files_with_xml'] / results['total_files']) * 100
        
        return results
    
    def validate_enforcement_patterns(self) -> Dict:
        """Validate strict enforcement patterns"""
        results = {
            'enforcement_attributes': 0,
            'strict_enforcement_tags': 0,
            'valid_enforcement_values': 0,
            'invalid_enforcement_values': [],
            'files_with_enforcement': []
        }
        
        valid_enforcement_values = {'mandatory', 'strict', 'absolute', 'automatic'}
        
        md_files = list(self.framework_root.rglob("*.md"))
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                
                # Count enforcement attributes
                enforcement_attrs = re.findall(r'enforcement="([^"]*)"', content)
                if enforcement_attrs:
                    results['files_with_enforcement'].append(str(file_path.relative_to(self.framework_root)))
                    results['enforcement_attributes'] += len(enforcement_attrs)
                    
                    for value in enforcement_attrs:
                        if value in valid_enforcement_values:
                            results['valid_enforcement_values'] += 1
                        else:
                            results['invalid_enforcement_values'].append({
                                'file': str(file_path.relative_to(self.framework_root)),
                                'value': value
                            })
                
                # Count strict_enforcement tags
                if '<strict_enforcement' in content:
                    results['strict_enforcement_tags'] += 1
                    
            except Exception as e:
                pass
        
        return results
    
    def validate_emphasis_techniques(self) -> Dict:
        """Validate multiple emphasis techniques"""
        results = {
            'caps_emphasis': 0,
            'bold_emphasis': 0,
            'xml_emphasis': 0,
            'repetition_emphasis': 0,
            'files_analyzed': 0
        }
        
        md_files = list(self.framework_root.rglob("*.md"))
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                results['files_analyzed'] += 1
                
                # Count different emphasis types
                results['caps_emphasis'] += len(re.findall(r'\b[A-Z]{3,}\b', content))
                results['bold_emphasis'] += len(re.findall(r'\*\*[^*]+\*\*', content))
                results['xml_emphasis'] += len(re.findall(r'<\w+[^>]*enforcement=', content))
                
                # Check for repetition (same key phrase multiple times)
                lines = content.split('\n')
                key_phrases = ['MUST', 'ALWAYS', 'NEVER', 'mandatory', 'strict', 'absolute']
                for phrase in key_phrases:
                    count = sum(1 for line in lines if phrase in line)
                    if count > 2:
                        results['repetition_emphasis'] += 1
                        
            except Exception as e:
                pass
        
        return results
    
    def validate_deterministic_execution(self) -> Dict:
        """Validate deterministic execution features"""
        results = {
            'structured_workflows': 0,
            'ordered_phases': 0,
            'validation_checkpoints': 0,
            'quality_gates': 0,
            'files_with_structure': []
        }
        
        md_files = list(self.framework_root.rglob("*.md"))
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                has_structure = False
                
                # Count structured elements
                if re.search(r'<phase[^>]*order=', content):
                    results['ordered_phases'] += len(re.findall(r'<phase[^>]*order=', content))
                    has_structure = True
                
                if '<validation>' in content:
                    results['validation_checkpoints'] += len(re.findall(r'<validation>', content))
                    has_structure = True
                
                if '<quality_gates' in content:
                    results['quality_gates'] += 1
                    has_structure = True
                
                if '<workflow>' in content or '<implementation>' in content:
                    results['structured_workflows'] += 1
                    has_structure = True
                
                if has_structure:
                    results['files_with_structure'].append(str(file_path.relative_to(self.framework_root)))
                    
            except Exception as e:
                pass
        
        return results
    
    def validate_claude4_optimizations(self) -> Dict:
        """Validate Claude 4 specific optimizations"""
        results = {
            'context_provided': 0,
            'motivation_explained': 0,
            'enforcement_targets': 0,
            'comprehensive_coverage': 0,
            'files_optimized': []
        }
        
        md_files = list(self.framework_root.rglob("*.md"))
        
        for file_path in md_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                optimized = False
                
                # Check for context provision
                context_patterns = [
                    r'<context>',
                    r'<motivation>',
                    r'enforcement="[^"]*".*context',
                    r'This.*ensures.*',
                    r'Prevents.*by.*'
                ]
                
                for pattern in context_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        results['context_provided'] += 1
                        optimized = True
                        break
                
                # Check for motivation explanation
                motivation_patterns = [
                    r'<motivation>',
                    r'prevents.*errors',
                    r'ensures.*quality',
                    r'improves.*by.*',
                    r'reduces.*time'
                ]
                
                for pattern in motivation_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        results['motivation_explained'] += 1
                        optimized = True
                        break
                
                # Check for enforcement targets
                if re.search(r'target="[^"]*"', content) or re.search(r'enforcement="[^"]*"', content):
                    results['enforcement_targets'] += 1
                    optimized = True
                
                # Check for comprehensive coverage
                coverage_indicators = [
                    r'<trigger_conditions>',
                    r'<implementation>',
                    r'<validation>',
                    r'<quality_gates>',
                    r'<integration_points>'
                ]
                
                coverage_count = sum(1 for pattern in coverage_indicators if re.search(pattern, content))
                if coverage_count >= 3:
                    results['comprehensive_coverage'] += 1
                    optimized = True
                
                if optimized:
                    results['files_optimized'].append(str(file_path.relative_to(self.framework_root)))
                    
            except Exception as e:
                pass
        
        return results
    
    def validate_all(self) -> Dict:
        """Run complete Claude 4 validation"""
        results = {
            'xml_structure': self.validate_xml_structure(),
            'enforcement_patterns': self.validate_enforcement_patterns(),
            'emphasis_techniques': self.validate_emphasis_techniques(),
            'deterministic_execution': self.validate_deterministic_execution(),
            'claude4_optimizations': self.validate_claude4_optimizations()
        }
        
        return results
    
    def generate_report(self, results: Dict) -> str:
        """Generate comprehensive Claude 4 validation report"""
        report = []
        report.append("=" * 80)
        report.append("CLAUDE 4 FEATURE VALIDATION REPORT")
        report.append("=" * 80)
        report.append("")
        
        # XML Structure validation
        xml_results = results['xml_structure']
        report.append("XML STRUCTURE IMPLEMENTATION:")
        report.append("-" * 40)
        report.append(f"✅ Files with XML: {xml_results['files_with_xml']}/{xml_results['total_files']}")
        report.append(f"✅ XML Coverage: {xml_results['xml_coverage']:.1f}%")
        
        if xml_results['issues']:
            report.append("Issues found:")
            for issue in xml_results['issues']:
                report.append(f"  ⚠️  {issue}")
        else:
            report.append("✅ No XML structure issues found")
        
        report.append("")
        
        # Enforcement patterns
        enf_results = results['enforcement_patterns']
        report.append("STRICT ENFORCEMENT PATTERNS:")
        report.append("-" * 40)
        report.append(f"✅ Enforcement attributes: {enf_results['enforcement_attributes']}")
        report.append(f"✅ Strict enforcement tags: {enf_results['strict_enforcement_tags']}")
        report.append(f"✅ Valid enforcement values: {enf_results['valid_enforcement_values']}")
        report.append(f"✅ Files with enforcement: {len(enf_results['files_with_enforcement'])}")
        
        if enf_results['invalid_enforcement_values']:
            report.append("Invalid enforcement values:")
            for invalid in enf_results['invalid_enforcement_values']:
                report.append(f"  ❌ {invalid['file']}: {invalid['value']}")
        
        report.append("")
        
        # Emphasis techniques
        emp_results = results['emphasis_techniques']
        report.append("MULTIPLE EMPHASIS TECHNIQUES:")
        report.append("-" * 40)
        report.append(f"✅ CAPS emphasis: {emp_results['caps_emphasis']} instances")
        report.append(f"✅ Bold emphasis: {emp_results['bold_emphasis']} instances")
        report.append(f"✅ XML emphasis: {emp_results['xml_emphasis']} instances")
        report.append(f"✅ Repetition emphasis: {emp_results['repetition_emphasis']} instances")
        report.append("")
        
        # Deterministic execution
        det_results = results['deterministic_execution']
        report.append("DETERMINISTIC EXECUTION FEATURES:")
        report.append("-" * 40)
        report.append(f"✅ Structured workflows: {det_results['structured_workflows']}")
        report.append(f"✅ Ordered phases: {det_results['ordered_phases']}")
        report.append(f"✅ Validation checkpoints: {det_results['validation_checkpoints']}")
        report.append(f"✅ Quality gates: {det_results['quality_gates']}")
        report.append(f"✅ Files with structure: {len(det_results['files_with_structure'])}")
        report.append("")
        
        # Claude 4 optimizations
        opt_results = results['claude4_optimizations']
        report.append("CLAUDE 4 SPECIFIC OPTIMIZATIONS:")
        report.append("-" * 40)
        report.append(f"✅ Context provided: {opt_results['context_provided']} instances")
        report.append(f"✅ Motivation explained: {opt_results['motivation_explained']} instances")
        report.append(f"✅ Enforcement targets: {opt_results['enforcement_targets']} instances")
        report.append(f"✅ Comprehensive coverage: {opt_results['comprehensive_coverage']} files")
        report.append(f"✅ Files optimized: {len(opt_results['files_optimized'])}")
        report.append("")
        
        # Overall assessment
        report.append("OVERALL CLAUDE 4 COMPLIANCE:")
        report.append("-" * 40)
        
        compliance_score = 0
        total_checks = 5
        
        if xml_results['xml_coverage'] > 80:
            compliance_score += 1
            report.append("✅ XML structure implementation: COMPLIANT")
        else:
            report.append("❌ XML structure implementation: NEEDS IMPROVEMENT")
        
        if enf_results['enforcement_attributes'] > 5:
            compliance_score += 1
            report.append("✅ Enforcement patterns: COMPLIANT")
        else:
            report.append("❌ Enforcement patterns: NEEDS IMPROVEMENT")
        
        if (emp_results['caps_emphasis'] + emp_results['bold_emphasis'] + emp_results['xml_emphasis']) > 20:
            compliance_score += 1
            report.append("✅ Multiple emphasis techniques: COMPLIANT")
        else:
            report.append("❌ Multiple emphasis techniques: NEEDS IMPROVEMENT")
        
        if det_results['ordered_phases'] > 10:
            compliance_score += 1
            report.append("✅ Deterministic execution: COMPLIANT")
        else:
            report.append("❌ Deterministic execution: NEEDS IMPROVEMENT")
        
        if opt_results['comprehensive_coverage'] > 10:
            compliance_score += 1
            report.append("✅ Claude 4 optimizations: COMPLIANT")
        else:
            report.append("❌ Claude 4 optimizations: NEEDS IMPROVEMENT")
        
        report.append("")
        report.append(f"COMPLIANCE SCORE: {compliance_score}/{total_checks} ({(compliance_score/total_checks)*100:.0f}%)")
        
        if compliance_score == total_checks:
            report.append("🎉 FULL CLAUDE 4 COMPLIANCE ACHIEVED!")
        elif compliance_score >= total_checks * 0.8:
            report.append("👍 STRONG CLAUDE 4 COMPLIANCE")
        else:
            report.append("⚠️  CLAUDE 4 COMPLIANCE NEEDS IMPROVEMENT")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)

def main():
    framework_root = "/Users/smenssink/Documents/Github personal projects/claude-code-modular-agents/.claude"
    
    validator = Claude4Validator(framework_root)
    results = validator.validate_all()
    report = validator.generate_report(results)
    
    print(report)
    
    # Save detailed results
    results_file = Path(framework_root) / "claude4_validation.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Save report
    report_file = Path(framework_root) / "claude4_report.txt"
    report_file.write_text(report)
    
    print(f"\nDetailed results saved to: {results_file}")
    print(f"Report saved to: {report_file}")
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())