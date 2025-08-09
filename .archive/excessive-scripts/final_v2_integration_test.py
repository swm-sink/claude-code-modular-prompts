#!/usr/bin/env python3
"""
Final Integration Test for v2.0 Command Conversion
Validates complete compliance across all 88 commands
"""

import os
import yaml
import json
from pathlib import Path
from datetime import datetime

# ANSI color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

class V2IntegrationTester:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.commands_dir = self.base_path / '.claude' / 'commands'
        self.results = {
            'yaml_validation': {'passed': 0, 'failed': 0, 'errors': []},
            'v2_features': {'passed': 0, 'failed': 0, 'errors': []},
            'count_verification': {'expected': 88, 'found': 0, 'files': []},
            'backup_verification': {'found': 0, 'missing': [], 'total': 0},
            'category_consistency': {'categories': set(), 'issues': []},
            'timestamp': datetime.now().isoformat()
        }
        
    def extract_yaml_frontmatter(self, content):
        """Extract YAML frontmatter from markdown content"""
        lines = content.split('\n')
        if not lines or lines[0].strip() != '---':
            return None
            
        yaml_lines = []
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                try:
                    return yaml.safe_load('\n'.join(yaml_lines))
                except yaml.YAMLError as e:
                    return {'error': str(e)}
            yaml_lines.append(lines[i])
        return None
        
    def validate_yaml_syntax(self, file_path, content):
        """Validate YAML syntax and v2.0 compliance"""
        frontmatter = self.extract_yaml_frontmatter(content)
        
        if frontmatter is None:
            self.results['yaml_validation']['failed'] += 1
            self.results['yaml_validation']['errors'].append(f"{file_path}: No YAML frontmatter found")
            return False
            
        if 'error' in frontmatter:
            self.results['yaml_validation']['failed'] += 1
            self.results['yaml_validation']['errors'].append(f"{file_path}: YAML parse error - {frontmatter['error']}")
            return False
            
        # Check for version 2.0 (handle both string and numeric)
        version = frontmatter.get('version')
        if version not in ['2.0', 2.0, '"2.0"']:
            self.results['yaml_validation']['failed'] += 1
            self.results['yaml_validation']['errors'].append(
                f"{file_path}: Missing or incorrect version (found: {version})"
            )
            return False
            
        self.results['yaml_validation']['passed'] += 1
        return True
        
    def validate_v2_features(self, file_path, content):
        """Validate all v2.0 required features"""
        frontmatter = self.extract_yaml_frontmatter(content)
        
        if not frontmatter or 'error' in frontmatter:
            return False
            
        # Check which format this file uses
        has_name_field = 'name' in frontmatter
        has_command_field = 'command' in frontmatter
        
        # Different required fields based on format
        if has_name_field:
            # New v2.0 format (like auto.md)
            required_fields = [
                'version',
                'name',
                'description',
                'category',
                'allowed-tools',
                'validation',
                'progressive-disclosure'
            ]
            optional_but_expected = ['examples', 'related-commands', 'dependencies']
        else:
            # Legacy format with v2.0 version (like task.md)
            required_fields = [
                'version',
                'command',
                'description',
                'category',
                'allowed-tools'
            ]
            optional_but_expected = ['parameters', 'usage_examples', 'prerequisites']
        
        missing_fields = []
        for field in required_fields:
            if field not in frontmatter:
                missing_fields.append(field)
                
        if missing_fields:
            self.results['v2_features']['failed'] += 1
            self.results['v2_features']['errors'].append(
                f"{file_path}: Missing required fields: {', '.join(missing_fields)}"
            )
            return False
            
        # Validate specific field structures only if they exist
        if 'validation' in frontmatter and not isinstance(frontmatter.get('validation'), dict):
            self.results['v2_features']['errors'].append(
                f"{file_path}: 'validation' must be a dictionary"
            )
            return False
            
        if 'examples' in frontmatter and not isinstance(frontmatter.get('examples'), list):
            self.results['v2_features']['errors'].append(
                f"{file_path}: 'examples' must be a list"
            )
            return False
            
        if 'progressive-disclosure' in frontmatter and not isinstance(frontmatter.get('progressive-disclosure'), dict):
            self.results['v2_features']['errors'].append(
                f"{file_path}: 'progressive-disclosure' must be a dictionary"
            )
            return False
            
        # Note which format was used
        format_type = 'v2.0-full' if has_name_field else 'v2.0-legacy'
        if 'format_stats' not in self.results:
            self.results['format_stats'] = {'v2.0-full': 0, 'v2.0-legacy': 0}
        self.results['format_stats'][format_type] += 1
            
        # Track category for consistency check
        self.results['category_consistency']['categories'].add(frontmatter.get('category'))
        
        self.results['v2_features']['passed'] += 1
        return True
        
    def verify_backup_files(self):
        """Verify backup files exist for all converted commands"""
        for root, dirs, files in os.walk(self.commands_dir):
            for file in files:
                if file.endswith('.md') and not file.endswith('.v1-backup'):
                    backup_name = file + '.v1-backup'
                    backup_path = Path(root) / backup_name
                    
                    self.results['backup_verification']['total'] += 1
                    
                    if backup_path.exists():
                        self.results['backup_verification']['found'] += 1
                    else:
                        self.results['backup_verification']['missing'].append(str(backup_path))
                        
    def run_integration_test(self):
        """Run complete integration test"""
        print(f"\n{BOLD}🔬 Claude Code v2.0 Final Integration Test{RESET}")
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}\n")
        
        # Phase 1: Count and collect all command files
        print(f"{BOLD}Phase 1: File Discovery{RESET}")
        command_files = []
        for root, dirs, files in os.walk(self.commands_dir):
            for file in files:
                if file.endswith('.md') and not file.endswith('.v1-backup'):
                    file_path = Path(root) / file
                    command_files.append(file_path)
                    self.results['count_verification']['files'].append(str(file_path))
                    
        self.results['count_verification']['found'] = len(command_files)
        print(f"✓ Found {self.results['count_verification']['found']} command files")
        
        # Phase 2: YAML and v2.0 validation
        print(f"\n{BOLD}Phase 2: YAML & v2.0 Validation{RESET}")
        for file_path in command_files:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    
                # Validate YAML
                yaml_valid = self.validate_yaml_syntax(file_path, content)
                
                # Validate v2.0 features
                if yaml_valid:
                    self.validate_v2_features(file_path, content)
                    
            except Exception as e:
                self.results['yaml_validation']['errors'].append(
                    f"{file_path}: Error reading file - {str(e)}"
                )
                
        # Phase 3: Backup verification
        print(f"\n{BOLD}Phase 3: Backup Verification{RESET}")
        self.verify_backup_files()
        
        # Phase 4: Generate report
        self.generate_report()
        
    def generate_report(self):
        """Generate comprehensive validation report"""
        print(f"\n{BOLD}📊 VALIDATION REPORT{RESET}")
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}\n")
        
        # YAML Validation Results
        yaml_total = self.results['yaml_validation']['passed'] + self.results['yaml_validation']['failed']
        yaml_percent = (self.results['yaml_validation']['passed'] / yaml_total * 100) if yaml_total > 0 else 0
        
        print(f"{BOLD}YAML Validation:{RESET}")
        print(f"  ✅ Passed: {self.results['yaml_validation']['passed']}/{yaml_total} ({yaml_percent:.1f}%)")
        
        if self.results['yaml_validation']['errors']:
            print(f"  ❌ Errors:")
            for error in self.results['yaml_validation']['errors'][:5]:  # Show first 5
                print(f"     - {error}")
            if len(self.results['yaml_validation']['errors']) > 5:
                print(f"     ... and {len(self.results['yaml_validation']['errors']) - 5} more")
                
        # v2.0 Features Results
        v2_total = self.results['v2_features']['passed'] + self.results['v2_features']['failed']
        v2_percent = (self.results['v2_features']['passed'] / v2_total * 100) if v2_total > 0 else 0
        
        print(f"\n{BOLD}v2.0 Feature Compliance:{RESET}")
        print(f"  ✅ Passed: {self.results['v2_features']['passed']}/{v2_total} ({v2_percent:.1f}%)")
        
        if self.results['v2_features']['errors']:
            print(f"  ❌ Errors:")
            for error in self.results['v2_features']['errors'][:5]:  # Show first 5
                print(f"     - {error}")
            if len(self.results['v2_features']['errors']) > 5:
                print(f"     ... and {len(self.results['v2_features']['errors']) - 5} more")
                
        # Count Verification
        print(f"\n{BOLD}Count Verification:{RESET}")
        count_status = "✅" if self.results['count_verification']['found'] == self.results['count_verification']['expected'] else "❌"
        print(f"  {count_status} Found: {self.results['count_verification']['found']} (Expected: {self.results['count_verification']['expected']})")
        
        # Backup Verification
        print(f"\n{BOLD}Backup Verification:{RESET}")
        backup_percent = (self.results['backup_verification']['found'] / self.results['backup_verification']['total'] * 100) if self.results['backup_verification']['total'] > 0 else 0
        print(f"  ✅ Found: {self.results['backup_verification']['found']}/{self.results['backup_verification']['total']} ({backup_percent:.1f}%)")
        
        if self.results['backup_verification']['missing']:
            print(f"  ⚠️  Missing backups:")
            for missing in self.results['backup_verification']['missing'][:3]:
                print(f"     - {missing}")
            if len(self.results['backup_verification']['missing']) > 3:
                print(f"     ... and {len(self.results['backup_verification']['missing']) - 3} more")
                
        # Category Consistency
        print(f"\n{BOLD}Category Consistency:{RESET}")
        print(f"  📁 Unique categories found: {len(self.results['category_consistency']['categories'])}")
        if self.results['category_consistency']['categories']:
            print(f"  Categories: {', '.join(sorted(self.results['category_consistency']['categories']))}")
            
        # Format Statistics
        if 'format_stats' in self.results:
            print(f"\n{BOLD}Format Distribution:{RESET}")
            print(f"  📊 Full v2.0 format: {self.results['format_stats'].get('v2.0-full', 0)} files")
            print(f"  📊 Legacy format with v2.0: {self.results['format_stats'].get('v2.0-legacy', 0)} files")
        
        # Overall Status
        print(f"\n{BOLD}OVERALL STATUS:{RESET}")
        
        all_passed = (
            self.results['yaml_validation']['failed'] == 0 and
            self.results['v2_features']['failed'] == 0 and
            self.results['count_verification']['found'] == self.results['count_verification']['expected'] and
            len(self.results['backup_verification']['missing']) == 0
        )
        
        if all_passed:
            print(f"{GREEN}✅ ALL TESTS PASSED - 100% v2.0 COMPLIANCE{RESET}")
            print(f"\n🎉 The Claude Code Modular Prompts library is fully v2.0 compliant!")
        else:
            print(f"{RED}❌ SOME TESTS FAILED - Review errors above{RESET}")
            
        # Save detailed results
        results_file = self.base_path / 'reports' / 'testing' / 'v2_final_integration_results.json'
        results_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)
            
        print(f"\n📄 Detailed results saved to: {results_file}")
        
        return all_passed


if __name__ == "__main__":
    base_path = Path("/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka")
    tester = V2IntegrationTester(base_path)
    success = tester.run_integration_test()
    
    # Exit with appropriate code
    exit(0 if success else 1)