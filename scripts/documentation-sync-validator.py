#!/usr/bin/env python3
"""
Documentation Sync Validator
TDD approach: Test documentation accuracy against implementation, then automate sync
Target: 100% documentation accuracy with automated validation
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import yaml

class DocumentationSyncValidator:
    """Validates and synchronizes documentation with implementation"""
    
    def __init__(self):
        self.validation_results = {
            'total_checks': 0,
            'passed_checks': 0,
            'failed_checks': 0,
            'accuracy_percentage': 0,
            'sync_issues': []
        }
        
        # Documentation validation rules
        self.doc_patterns = {
            'command_count': r'(\d+)\s*command[s]?\s*template[s]?',
            'component_count': r'(\d+)\s*component[s]?',
            'file_count': r'(\d+)\s*(?:files?|\.md)',
            'installation_time': r'(\d+)[-\s]*second[s]?',
            'performance_claims': r'<(\d+(?:\.\d+)?)(?:ms|millisecond[s]?)'
        }
    
    def count_actual_commands(self) -> int:
        """Count actual command files in the project"""
        command_files = list(Path('.claude/commands').rglob('*.md'))
        return len(command_files)
    
    def count_actual_components(self) -> int:
        """Count actual component files in the project"""
        component_files = list(Path('.claude/components').rglob('*.md'))
        # Exclude documentation files
        return len([f for f in component_files if not f.name.startswith('README') and not f.name.startswith('COMPONENT-LIBRARY-INDEX')])
    
    def count_actual_markdown_files(self) -> int:
        """Count total markdown files in project"""
        md_files = list(Path('.').rglob('*.md'))
        return len(md_files)
    
    def measure_actual_performance(self) -> float:
        """Measure actual validation performance"""
        import time
        
        # Simple performance measurement using existing validation
        command_files = list(Path('.claude/commands').rglob('*.md'))
        total_time = 0
        
        for file_path in command_files[:10]:  # Sample 10 files for performance
            start_time = time.perf_counter()
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Simple YAML validation
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        yaml.safe_load(parts[1])
            except:
                pass
            end_time = time.perf_counter()
            total_time += (end_time - start_time)
        
        avg_time = total_time / 10 if total_time > 0 else 0.001
        return avg_time * 1000  # Convert to ms
    
    def validate_readme_accuracy(self) -> Dict:
        """Validate README.md claims against actual implementation"""
        issues = []
        
        try:
            with open('README.md', 'r', encoding='utf-8') as f:
                readme_content = f.read()
        except FileNotFoundError:
            return {'valid': False, 'issues': ['README.md not found']}
        
        # Check command count claims
        actual_commands = self.count_actual_commands()
        command_matches = re.findall(self.doc_patterns['command_count'], readme_content, re.IGNORECASE)
        
        for match in command_matches:
            claimed_count = int(match)
            if claimed_count != actual_commands:
                issues.append(f"Command count mismatch: README claims {claimed_count}, actual is {actual_commands}")
        
        # Check performance claims
        actual_performance = self.measure_actual_performance()
        perf_matches = re.findall(self.doc_patterns['performance_claims'], readme_content, re.IGNORECASE)
        
        for match in perf_matches:
            claimed_perf = float(match)
            if actual_performance > claimed_perf:
                issues.append(f"Performance claim unmet: README claims <{claimed_perf}ms, actual is {actual_performance:.2f}ms")
        
        # Check installation time claims (harder to validate automatically, but we can check for consistency)
        install_matches = re.findall(self.doc_patterns['installation_time'], readme_content, re.IGNORECASE)
        if install_matches:
            claimed_times = [int(match) for match in install_matches]
            if len(set(claimed_times)) > 1:
                issues.append(f"Inconsistent installation time claims: {claimed_times}")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'checks_performed': len(command_matches) + len(perf_matches) + len(install_matches),
            'actual_commands': actual_commands,
            'actual_performance': actual_performance
        }
    
    def validate_claude_md_accuracy(self) -> Dict:
        """Validate CLAUDE.md accuracy against implementation"""
        issues = []
        
        try:
            with open('CLAUDE.md', 'r', encoding='utf-8') as f:
                claude_content = f.read()
        except FileNotFoundError:
            return {'valid': False, 'issues': ['CLAUDE.md not found']}
        
        # Check command count in CLAUDE.md
        actual_commands = self.count_actual_commands()
        actual_components = self.count_actual_components()
        
        command_matches = re.findall(self.doc_patterns['command_count'], claude_content, re.IGNORECASE)
        for match in command_matches:
            claimed_count = int(match)
            if claimed_count != actual_commands:
                issues.append(f"CLAUDE.md command count mismatch: claims {claimed_count}, actual is {actual_commands}")
        
        component_matches = re.findall(self.doc_patterns['component_count'], claude_content, re.IGNORECASE)
        for match in component_matches:
            claimed_count = int(match)
            if claimed_count != actual_components:
                issues.append(f"CLAUDE.md component count mismatch: claims {claimed_count}, actual is {actual_components}")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'checks_performed': len(command_matches) + len(component_matches),
            'actual_commands': actual_commands,
            'actual_components': actual_components
        }
    
    def validate_documentation_consistency(self) -> Dict:
        """Validate consistency across all documentation files"""
        issues = []
        doc_files = [
            'README.md',
            'CLAUDE.md', 
            'USAGE.md',
            'FAQ.md',
            '.claude/components/COMPONENT-LIBRARY-INDEX.md'
        ]
        
        # Extract claims from all documentation files
        all_claims = {}
        
        for doc_file in doc_files:
            if os.path.exists(doc_file):
                try:
                    with open(doc_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract command counts
                    command_counts = re.findall(self.doc_patterns['command_count'], content, re.IGNORECASE)
                    if command_counts:
                        all_claims[doc_file + '_commands'] = [int(c) for c in command_counts]
                    
                    # Extract component counts
                    component_counts = re.findall(self.doc_patterns['component_count'], content, re.IGNORECASE)
                    if component_counts:
                        all_claims[doc_file + '_components'] = [int(c) for c in component_counts]
                        
                except Exception as e:
                    issues.append(f"Error reading {doc_file}: {e}")
        
        # Check for inconsistencies
        actual_commands = self.count_actual_commands()
        actual_components = self.count_actual_components()
        
        for claim_key, claim_values in all_claims.items():
            if 'commands' in claim_key:
                for value in claim_values:
                    if value != actual_commands:
                        issues.append(f"Inconsistent command count in {claim_key}: {value} vs actual {actual_commands}")
            elif 'components' in claim_key:
                for value in claim_values:
                    if value != actual_components:
                        issues.append(f"Inconsistent component count in {claim_key}: {value} vs actual {actual_components}")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'claims_found': all_claims,
            'actual_commands': actual_commands,
            'actual_components': actual_components
        }
    
    def generate_sync_report(self) -> Dict:
        """Generate comprehensive documentation sync report"""
        print("🔍 DOCUMENTATION SYNC VALIDATION")
        print("=" * 50)
        
        # Validate README.md
        print("📖 Validating README.md accuracy...")
        readme_result = self.validate_readme_accuracy()
        
        # Validate CLAUDE.md  
        print("📋 Validating CLAUDE.md accuracy...")
        claude_result = self.validate_claude_md_accuracy()
        
        # Validate overall consistency
        print("🔄 Validating documentation consistency...")
        consistency_result = self.validate_documentation_consistency()
        
        # Compile overall results
        all_issues = (readme_result.get('issues', []) + 
                     claude_result.get('issues', []) + 
                     consistency_result.get('issues', []))
        
        total_checks = (readme_result.get('checks_performed', 0) + 
                       claude_result.get('checks_performed', 0) + 
                       len(consistency_result.get('claims_found', {})))
        
        passed_checks = total_checks - len(all_issues)
        accuracy_percentage = (passed_checks / total_checks * 100) if total_checks > 0 else 0
        
        # Update validation results
        self.validation_results.update({
            'total_checks': total_checks,
            'passed_checks': passed_checks,
            'failed_checks': len(all_issues),
            'accuracy_percentage': accuracy_percentage,
            'sync_issues': all_issues
        })
        
        # Print results
        print(f"\n📊 DOCUMENTATION ACCURACY RESULTS:")
        print(f"    Total checks performed: {total_checks}")
        print(f"    Checks passed: {passed_checks}")
        print(f"    Checks failed: {len(all_issues)}")
        print(f"    Accuracy percentage: {accuracy_percentage:.1f}%")
        
        if all_issues:
            print(f"\n❌ SYNC ISSUES FOUND:")
            for i, issue in enumerate(all_issues, 1):
                print(f"    {i}. {issue}")
        else:
            print(f"\n✅ PERFECT SYNC: All documentation is accurate!")
        
        return {
            'overall_accuracy': accuracy_percentage,
            'total_issues': len(all_issues),
            'readme_result': readme_result,
            'claude_result': claude_result,
            'consistency_result': consistency_result,
            'actual_metrics': {
                'commands': consistency_result['actual_commands'],
                'components': consistency_result['actual_components'],
                'performance_ms': readme_result.get('actual_performance', 0)
            }
        }
    
    def auto_fix_documentation(self, dry_run=True) -> Dict:
        """Automatically fix documentation sync issues"""
        print(f"\n🔧 AUTO-FIX DOCUMENTATION {'(DRY RUN)' if dry_run else '(LIVE)'}")
        print("=" * 50)
        
        fixes_applied = []
        actual_commands = self.count_actual_commands()
        actual_components = self.count_actual_components()
        actual_performance = self.measure_actual_performance()
        
        # Fix README.md
        if os.path.exists('README.md'):
            try:
                with open('README.md', 'r', encoding='utf-8') as f:
                    readme_content = f.read()
                
                original_content = readme_content
                
                # Fix command count references
                readme_content = re.sub(
                    r'(\d+)\s*command[s]?\s*template[s]?',
                    f'{actual_commands} command templates',
                    readme_content,
                    flags=re.IGNORECASE
                )
                
                if readme_content != original_content:
                    fixes_applied.append(f"Updated command count to {actual_commands} in README.md")
                    
                    if not dry_run:
                        with open('README.md', 'w', encoding='utf-8') as f:
                            f.write(readme_content)
                
            except Exception as e:
                fixes_applied.append(f"Error fixing README.md: {e}")
        
        # Fix CLAUDE.md
        if os.path.exists('CLAUDE.md'):
            try:
                with open('CLAUDE.md', 'r', encoding='utf-8') as f:
                    claude_content = f.read()
                
                original_content = claude_content
                
                # Fix command count references
                claude_content = re.sub(
                    r'(\d+)\s*command[s]?\s*template[s]?',
                    f'{actual_commands} command templates',
                    claude_content,
                    flags=re.IGNORECASE
                )
                
                # Fix component count references  
                claude_content = re.sub(
                    r'(\d+)\s*component[s]?',
                    f'{actual_components} components',
                    claude_content,
                    flags=re.IGNORECASE
                )
                
                if claude_content != original_content:
                    fixes_applied.append(f"Updated counts to {actual_commands} commands, {actual_components} components in CLAUDE.md")
                    
                    if not dry_run:
                        with open('CLAUDE.md', 'w', encoding='utf-8') as f:
                            f.write(claude_content)
                
            except Exception as e:
                fixes_applied.append(f"Error fixing CLAUDE.md: {e}")
        
        print(f"🔧 FIXES {'WOULD BE APPLIED' if dry_run else 'APPLIED'}:")
        for fix in fixes_applied:
            print(f"    ✅ {fix}")
        
        if not fixes_applied:
            print("    ✅ No fixes needed - documentation is already accurate!")
        
        return {
            'fixes_applied': len(fixes_applied),
            'fixes_list': fixes_applied,
            'dry_run': dry_run
        }
    
    def run_live_auto_fix(self):
        """Run auto-fix in live mode to actually update files"""
        print(f"\n🚀 RUNNING LIVE AUTO-FIX")
        print("=" * 50)
        
        result = self.auto_fix_documentation(dry_run=False)
        
        if result['fixes_applied'] > 0:
            print(f"\n✅ SUCCESS: {result['fixes_applied']} fixes applied to documentation")
            print("📝 Files updated:")
            for fix in result['fixes_list']:
                print(f"    • {fix}")
        else:
            print(f"\n✅ NO FIXES NEEDED: Documentation already accurate")
        
        return result

def run_documentation_sync_test():
    """Run comprehensive documentation sync validation"""
    validator = DocumentationSyncValidator()
    
    # Generate sync report
    sync_report = validator.generate_sync_report()
    
    # Run auto-fix in dry-run mode first
    auto_fix_report = validator.auto_fix_documentation(dry_run=True)
    
    print(f"\n🎯 DOCUMENTATION SYNC SUMMARY:")
    print(f"    Current accuracy: {sync_report['overall_accuracy']:.1f}%")
    print(f"    Issues found: {sync_report['total_issues']}")
    print(f"    Auto-fixes available: {auto_fix_report['fixes_applied']}")
    
    if sync_report['overall_accuracy'] >= 100.0:
        print(f"\n🏆 SUCCESS: 100% documentation accuracy achieved!")
    else:
        print(f"\n⚠️  IMPROVEMENT NEEDED: {100 - sync_report['overall_accuracy']:.1f}% accuracy gap")
    
    return sync_report, auto_fix_report

if __name__ == "__main__":
    run_documentation_sync_test()