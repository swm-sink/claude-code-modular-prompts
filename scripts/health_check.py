#!/usr/bin/env python3
"""
Framework Health Check Script

Comprehensive health monitoring for the Claude Code Modular Framework.
Provides a single command to verify framework integrity and identify issues.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

class HealthCheck:
    def __init__(self):
        self.root = Path(__file__).parent.parent
        self.results = {
            'timestamp': datetime.utcnow().isoformat(),
            'checks': {},
            'metrics': {},
            'recommendations': []
        }
        
    def run_validation(self) -> Tuple[bool, int, List[str]]:
        """Run framework validation and parse results."""
        try:
            result = subprocess.run(
                [sys.executable, 'scripts/validate.py'],
                capture_output=True,
                text=True,
                cwd=self.root
            )
            
            # Parse output for quality score and issues
            output = result.stdout
            quality_score = 0
            issues = []
            
            for line in output.split('\n'):
                if 'Quality Score:' in line:
                    score_part = line.split(':')[1].split('/')[0].strip()
                    quality_score = int(float(score_part))
                elif line.strip().startswith('•'):
                    issues.append(line.strip())
                    
            passed = result.returncode == 0 or len(issues) <= 2  # Allow minor issues
            return passed, quality_score, issues
        except Exception as e:
            return False, 0, [f"Validation error: {str(e)}"]
    
    def run_tests(self) -> Tuple[bool, int, int]:
        """Run framework tests and get pass/fail counts."""
        try:
            result = subprocess.run(
                [sys.executable, '-m', 'pytest', 'tests/framework/', '-v', '--tb=short'],
                capture_output=True,
                text=True,
                cwd=self.root
            )
            
            # Parse test results
            output = result.stdout
            passed = failed = 0
            
            for line in output.split('\n'):
                if ' PASSED' in line:
                    passed += 1
                elif ' FAILED' in line:
                    failed += 1
                    
            return result.returncode == 0, passed, failed
        except Exception as e:
            return False, 0, 0
    
    def check_file_structure(self) -> Tuple[bool, List[str]]:
        """Verify expected directory structure exists."""
        expected_dirs = [
            '.claude/commands',
            '.claude/modules',
            'scripts',
            'tests/framework',
            'docs'
        ]
        
        missing = []
        for dir_path in expected_dirs:
            if not (self.root / dir_path).exists():
                missing.append(dir_path)
                
        return len(missing) == 0, missing
    
    def analyze_module_complexity(self) -> Dict[str, int]:
        """Analyze module sizes and complexity."""
        modules_dir = self.root / '.claude' / 'modules'
        complexity = {}
        
        for module_file in modules_dir.rglob('*.md'):
            content = module_file.read_text()
            # Simple complexity: character count
            complexity[str(module_file.relative_to(modules_dir))] = len(content)
            
        return complexity
    
    def check_dependencies(self) -> Tuple[bool, List[str]]:
        """Check for missing module dependencies."""
        issues = []
        modules_dir = self.root / '.claude' / 'modules'
        
        for module_file in modules_dir.rglob('*.md'):
            content = module_file.read_text()
            # Look for module references
            for line in content.split('\n'):
                if 'modules/' in line and '.md' in line:
                    # Extract module path
                    start = line.find('modules/')
                    end = line.find('.md', start) + 3
                    if start != -1 and end > start:
                        ref_path = line[start:end]
                        full_path = self.root / '.claude' / ref_path
                        if not full_path.exists():
                            issues.append(f"{module_file.name} → {ref_path}")
                            
        return len(issues) == 0, issues
    
    def generate_report(self):
        """Generate and display the health check report."""
        print(f"\n{Colors.BOLD}🏥 Framework Health Check v1.0.0{Colors.RESET}")
        print("=" * 50)
        
        # Run validation
        val_passed, quality_score, val_issues = self.run_validation()
        self.results['checks']['validation'] = val_passed
        self.results['metrics']['quality_score'] = quality_score
        
        if val_passed:
            print(f"{Colors.GREEN}✅ Validation: PASSED{Colors.RESET} ({len(val_issues)} minor issues)")
        else:
            print(f"{Colors.RED}❌ Validation: FAILED{Colors.RESET}")
            
        # Run tests
        tests_passed, test_pass, test_fail = self.run_tests()
        self.results['checks']['tests'] = tests_passed
        self.results['metrics']['tests_passed'] = test_pass
        self.results['metrics']['tests_failed'] = test_fail
        
        if tests_passed:
            print(f"{Colors.GREEN}✅ Tests: {test_pass}/{test_pass + test_fail} passing{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Tests: {test_pass}/{test_pass + test_fail} passing{Colors.RESET}")
            
        # Check quality score
        if quality_score >= 90:
            print(f"{Colors.GREEN}✅ Quality Score: {quality_score}/100{Colors.RESET}")
        elif quality_score >= 80:
            print(f"{Colors.YELLOW}⚠️  Quality Score: {quality_score}/100{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Quality Score: {quality_score}/100{Colors.RESET}")
            
        # Check file structure
        structure_ok, missing_dirs = self.check_file_structure()
        self.results['checks']['structure'] = structure_ok
        
        if structure_ok:
            print(f"{Colors.GREEN}✅ File Structure: OK{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ File Structure: Missing {len(missing_dirs)} directories{Colors.RESET}")
            
        # Check dependencies
        deps_ok, dep_issues = self.check_dependencies()
        self.results['checks']['dependencies'] = deps_ok
        
        if deps_ok:
            print(f"{Colors.GREEN}✅ Dependencies: All resolved{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}⚠️  Dependencies: {len(dep_issues)} broken references{Colors.RESET}")
            
        # Module complexity
        print(f"\n{Colors.BOLD}📊 Module Metrics:{Colors.RESET}")
        complexity = self.analyze_module_complexity()
        self.results['metrics']['module_sizes'] = complexity
        
        # Find largest modules
        sorted_modules = sorted(complexity.items(), key=lambda x: x[1], reverse=True)[:3]
        for module, size in sorted_modules:
            size_kb = size / 1024
            if size_kb > 40:
                print(f"  {Colors.RED}⚠️  {module}: {size_kb:.1f}KB (over limit){Colors.RESET}")
            else:
                print(f"  {Colors.BLUE}📄 {module}: {size_kb:.1f}KB{Colors.RESET}")
                
        # Recommendations
        print(f"\n{Colors.BOLD}🎯 Recommendations:{Colors.RESET}")
        
        if not val_passed:
            self.results['recommendations'].append("Fix validation errors urgently")
            print(f"  1. {Colors.RED}Fix validation errors urgently{Colors.RESET}")
            
        if not tests_passed:
            self.results['recommendations'].append("Fix failing tests")
            print(f"  2. {Colors.RED}Fix failing tests{Colors.RESET}")
            
        if quality_score < 90:
            self.results['recommendations'].append("Improve quality score to 90+")
            print(f"  3. {Colors.YELLOW}Improve quality score to 90+{Colors.RESET}")
            
        if not deps_ok:
            self.results['recommendations'].append("Fix broken module references")
            print(f"  4. {Colors.YELLOW}Fix broken module references{Colors.RESET}")
            
        large_modules = [m for m, s in complexity.items() if s > 40000]
        if large_modules:
            self.results['recommendations'].append(f"Reduce size of {len(large_modules)} large modules")
            print(f"  5. {Colors.YELLOW}Reduce size of {len(large_modules)} large modules{Colors.RESET}")
            
        if len(self.results['recommendations']) == 0:
            self.results['recommendations'].append("Framework is healthy - consider adding more tests")
            print(f"  {Colors.GREEN}✨ Framework is healthy!{Colors.RESET}")
            
        # Save detailed report
        report_path = self.root / '.claude' / 'analytics' / f'health-check-{datetime.now().strftime("%Y-%m-%d-%H%M%S")}.json'
        report_path.parent.mkdir(exist_ok=True)
        
        with open(report_path, 'w') as f:
            json.dump(self.results, f, indent=2)
            
        print(f"\n{Colors.BLUE}Full report: {report_path}{Colors.RESET}")
        
        # Overall health status
        all_passed = all([
            val_passed,
            tests_passed,
            quality_score >= 80,
            structure_ok,
            deps_ok
        ])
        
        if all_passed:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✅ OVERALL HEALTH: GOOD{Colors.RESET}")
            return 0
        else:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠️  OVERALL HEALTH: NEEDS ATTENTION{Colors.RESET}")
            return 1

def main():
    """Run the health check."""
    checker = HealthCheck()
    return checker.generate_report()

if __name__ == "__main__":
    sys.exit(main())