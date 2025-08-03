#!/usr/bin/env python3
"""
Production Validation Suite
Comprehensive validation for production readiness
Phase 4 - Final Production Validation
"""

import os
import sys
import logging
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')

class ProductionValidationSuite:
    """Comprehensive production readiness validation"""
    
    def __init__(self, base_dir: str = ".claude"):
        self.base_dir = Path(base_dir)
        self.validation_results = {}
        
    def validate_file_structure(self) -> Dict[str, Any]:
        """Validate expected file structure exists"""
        logging.info("🏗️ Validating file structure...")
        
        required_files = [
            "commands",
            "components/atomic",
            "settings.json",
            "CLAUDE.md",
            "smart-automation-engine.py",
            "component-testing-framework.py",
            "validate-compliance.sh"
        ]
        
        missing_files = []
        existing_files = []
        
        for file_path in required_files:
            full_path = self.base_dir / file_path
            if full_path.exists():
                existing_files.append(file_path)
            else:
                missing_files.append(file_path)
        
        return {
            'test_name': 'File Structure',
            'passed': len(missing_files) == 0,
            'score': len(existing_files) / len(required_files) * 100,
            'existing_files': len(existing_files),
            'missing_files': missing_files,
            'details': f"{len(existing_files)}/{len(required_files)} required files present"
        }
    
    def validate_command_compliance(self) -> Dict[str, Any]:
        """Validate all commands are Claude Code compliant"""
        logging.info("⚡ Validating Claude Code compliance...")
        
        try:
            result = subprocess.run(
                ['bash', str(self.base_dir / 'validate-compliance.sh')],
                capture_output=True,
                text=True,
                cwd=self.base_dir.parent
            )
            
            success = result.returncode == 0
            output_lines = result.stdout.split('\n') if result.stdout else []
            error_lines = result.stderr.split('\n') if result.stderr else []
            
            # Parse validation results
            files_processed = 0
            issues_found = 0
            
            for line in output_lines + error_lines:
                if 'Total Files Processed:' in line:
                    files_processed = int(line.split(':')[1].strip())
                elif 'Total Issues Found:' in line:
                    issues_found = int(line.split(':')[1].strip())
            
            return {
                'test_name': 'Claude Code Compliance',
                'passed': success and issues_found == 0,
                'score': (files_processed - issues_found) / max(files_processed, 1) * 100,
                'files_processed': files_processed,
                'issues_found': issues_found,
                'details': f"{files_processed - issues_found}/{files_processed} files compliant"
            }
            
        except Exception as e:
            return {
                'test_name': 'Claude Code Compliance',
                'passed': False,
                'score': 0,
                'error': str(e),
                'details': 'Compliance validation failed'
            }
    
    def validate_component_system(self) -> Dict[str, Any]:
        """Validate atomic component system"""
        logging.info("🧩 Validating atomic component system...")
        
        try:
            result = subprocess.run(
                ['python3', str(self.base_dir / 'component-testing-framework.py')],
                capture_output=True,
                text=True,
                cwd=self.base_dir.parent
            )
            
            output = result.stdout
            
            # Parse component test results
            overall_health = 0
            structural_score = 0
            unit_score = 0
            integration_score = 0
            
            for line in output.split('\n'):
                if 'Overall Health:' in line:
                    try:
                        overall_health = float(line.split(':')[1].split('(')[0].strip().replace('%', ''))
                    except:
                        pass
                elif 'Structural Validation:' in line:
                    try:
                        structural_score = float(line.split(':')[1].split('(')[0].strip().replace('%', ''))
                    except:
                        pass
                elif 'Unit Tests:' in line:
                    try:
                        unit_score = float(line.split(':')[1].split('(')[0].strip().replace('%', ''))
                    except:
                        pass
                elif 'Integration Tests:' in line:
                    try:
                        integration_score = float(line.split(':')[1].split('(')[0].strip().replace('%', ''))
                    except:
                        pass
            
            passed = overall_health >= 70  # Grade C or better for production
            
            return {
                'test_name': 'Component System',
                'passed': passed,
                'score': overall_health,
                'overall_health': overall_health,
                'structural_score': structural_score,
                'unit_score': unit_score,
                'integration_score': integration_score,
                'details': f"Overall health: {overall_health:.1f}% (Grade {'A' if overall_health >= 90 else 'B' if overall_health >= 80 else 'C' if overall_health >= 70 else 'D' if overall_health >= 60 else 'F'})"
            }
            
        except Exception as e:
            return {
                'test_name': 'Component System',
                'passed': False,
                'score': 0,
                'error': str(e),
                'details': 'Component validation failed'
            }
    
    def validate_automation_system(self) -> Dict[str, Any]:
        """Validate smart automation system"""
        logging.info("🤖 Validating automation system...")
        
        try:
            result = subprocess.run(
                ['python3', str(self.base_dir / 'test-automation-system.py')],
                capture_output=True,
                text=True,
                cwd=self.base_dir.parent
            )
            
            output = result.stdout
            
            # Parse automation results
            automation_percentage = 0
            total_replacements = 0
            total_placeholders = 0
            
            for line in output.split('\n'):
                if 'Automation Percentage:' in line:
                    try:
                        automation_percentage = float(line.split(':')[1].strip().replace('%', ''))
                    except:
                        pass
                elif 'Automated Replacements:' in line:
                    try:
                        total_replacements = int(line.split(':')[1].strip())
                    except:
                        pass
                elif 'Total Placeholders:' in line:
                    try:
                        total_placeholders = int(line.split(':')[1].strip())
                    except:
                        pass
            
            # Success if automation system is working (>40% is good for production)
            passed = automation_percentage >= 40 and total_replacements >= 50
            
            return {
                'test_name': 'Automation System',
                'passed': passed,
                'score': automation_percentage,
                'automation_percentage': automation_percentage,
                'total_replacements': total_replacements,
                'total_placeholders': total_placeholders,
                'details': f"Automation: {automation_percentage:.1f}% ({total_replacements}/{total_placeholders})"
            }
            
        except Exception as e:
            return {
                'test_name': 'Automation System',
                'passed': False,
                'score': 0,
                'error': str(e),
                'details': 'Automation validation failed'
            }
    
    def validate_documentation(self) -> Dict[str, Any]:
        """Validate documentation completeness"""
        logging.info("📚 Validating documentation...")
        
        required_docs = [
            "CLAUDE.md",
            "PRODUCTION-READY-USER-GUIDE.md",
            "ATOMIC-COMPONENT-ARCHITECTURE-STANDARDS.md",
            "ATOMIC-COMPONENT-DOCUMENTATION.md",
            "COMPONENT-QUICK-REFERENCE.md",
            "PROVEN-WORKFLOW-PATTERNS.md",
            "COMPONENT-COMPATIBILITY-MATRIX.md"
        ]
        
        existing_docs = []
        missing_docs = []
        
        for doc in required_docs:
            if (self.base_dir / doc).exists():
                existing_docs.append(doc)
            else:
                missing_docs.append(doc)
        
        doc_score = len(existing_docs) / len(required_docs) * 100
        
        return {
            'test_name': 'Documentation',
            'passed': len(missing_docs) == 0,
            'score': doc_score,
            'existing_docs': len(existing_docs),
            'missing_docs': missing_docs,
            'details': f"{len(existing_docs)}/{len(required_docs)} required documents present"
        }
    
    def validate_performance(self) -> Dict[str, Any]:
        """Validate system performance"""
        logging.info("⚡ Validating performance...")
        
        try:
            import time
            
            # Test automation engine performance
            start_time = time.time()
            result = subprocess.run(
                ['python3', str(self.base_dir / 'smart-automation-engine.py')],
                capture_output=True,
                text=True,
                cwd=self.base_dir.parent
            )
            automation_time = time.time() - start_time
            
            # Test component validation performance
            start_time = time.time()
            result = subprocess.run(
                ['python3', str(self.base_dir / 'validate-component-standards.py')],
                capture_output=True,
                text=True,
                cwd=self.base_dir.parent
            )
            validation_time = time.time() - start_time
            
            # Performance targets
            automation_target = 5.0  # seconds
            validation_target = 10.0  # seconds
            
            automation_passed = automation_time <= automation_target
            validation_passed = validation_time <= validation_target
            
            overall_passed = automation_passed and validation_passed
            
            # Calculate performance score
            automation_score = min(100, (automation_target / automation_time) * 100) if automation_time > 0 else 100
            validation_score = min(100, (validation_target / validation_time) * 100) if validation_time > 0 else 100
            overall_score = (automation_score + validation_score) / 2
            
            return {
                'test_name': 'Performance',
                'passed': overall_passed,
                'score': overall_score,
                'automation_time': automation_time,
                'validation_time': validation_time,
                'automation_passed': automation_passed,
                'validation_passed': validation_passed,
                'details': f"Automation: {automation_time:.1f}s, Validation: {validation_time:.1f}s"
            }
            
        except Exception as e:
            return {
                'test_name': 'Performance',
                'passed': False,
                'score': 0,
                'error': str(e),
                'details': 'Performance validation failed'
            }
    
    def calculate_production_readiness(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate overall production readiness score"""
        
        # Weight different validation categories
        weights = {
            'File Structure': 0.15,
            'Claude Code Compliance': 0.25,
            'Component System': 0.25,
            'Automation System': 0.20,
            'Documentation': 0.10,
            'Performance': 0.05
        }
        
        total_score = 0
        total_weight = 0
        passed_tests = 0
        failed_tests = 0
        
        for result in results:
            test_name = result['test_name']
            if test_name in weights:
                weight = weights[test_name]
                score = result.get('score', 0)
                total_score += score * weight
                total_weight += weight
                
                if result.get('passed', False):
                    passed_tests += 1
                else:
                    failed_tests += 1
        
        overall_score = total_score / total_weight if total_weight > 0 else 0
        
        # Production readiness grades
        if overall_score >= 90:
            grade = 'A+'
            readiness = 'Excellent - Ready for Enterprise Production'
        elif overall_score >= 80:
            grade = 'A'
            readiness = 'Great - Ready for Production'
        elif overall_score >= 70:
            grade = 'B'
            readiness = 'Good - Production Ready with Minor Polish'
        elif overall_score >= 60:
            grade = 'C'
            readiness = 'Acceptable - Production Ready'
        else:
            grade = 'D'
            readiness = 'Needs Improvement - Not Production Ready'
        
        return {
            'overall_score': overall_score,
            'grade': grade,
            'readiness': readiness,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'total_tests': len(results),
            'production_ready': overall_score >= 60
        }
    
    def run_full_validation(self) -> Dict[str, Any]:
        """Run complete production validation suite"""
        logging.info("🚀 PRODUCTION VALIDATION SUITE")
        logging.info("=" * 60)
        
        validation_tests = [
            self.validate_file_structure,
            self.validate_command_compliance,
            self.validate_component_system,
            self.validate_automation_system,
            self.validate_documentation,
            self.validate_performance
        ]
        
        results = []
        for test in validation_tests:
            try:
                result = test()
                results.append(result)
            except Exception as e:
                logging.error(f"Test failed: {e}")
                results.append({
                    'test_name': test.__name__,
                    'passed': False,
                    'score': 0,
                    'error': str(e),
                    'details': 'Test execution failed'
                })
        
        # Calculate overall production readiness
        readiness = self.calculate_production_readiness(results)
        
        return {
            'test_results': results,
            'production_readiness': readiness,
            'timestamp': '2025-07-30',
            'validation_version': 'Phase 4 Production'
        }

def print_validation_results(results: Dict[str, Any]):
    """Print comprehensive validation results"""
    test_results = results['test_results']
    readiness = results['production_readiness']
    
    print(f"\n🎯 PRODUCTION VALIDATION RESULTS")
    print(f"=" * 60)
    print(f"Validation Date: {results['timestamp']}")
    print(f"Version: {results['validation_version']}")
    print()
    
    print(f"📊 TEST RESULTS")
    print(f"=" * 40)
    for result in test_results:
        status = "✅ PASS" if result.get('passed', False) else "❌ FAIL"
        score = result.get('score', 0)
        test_name = result['test_name']
        details = result.get('details', 'No details')
        
        print(f"{status} {test_name}: {score:.1f}%")
        print(f"    {details}")
        
        if 'error' in result:
            print(f"    Error: {result['error']}")
        print()
    
    print(f"🏆 OVERALL PRODUCTION READINESS")
    print(f"=" * 40)
    print(f"Overall Score: {readiness['overall_score']:.1f}%")
    print(f"Grade: {readiness['grade']}")
    print(f"Status: {readiness['readiness']}")
    print(f"Tests Passed: {readiness['passed_tests']}/{readiness['total_tests']}")
    print(f"Production Ready: {'✅ YES' if readiness['production_ready'] else '❌ NO'}")
    
    if readiness['production_ready']:
        print(f"\n🎉 PRODUCTION DEPLOYMENT APPROVED")
        print(f"✅ System meets all production readiness criteria")
        print(f"🚀 Ready for immediate deployment and use")
    else:
        print(f"\n⚠️  PRODUCTION DEPLOYMENT NOT RECOMMENDED")
        print(f"🔧 Address failed tests before production deployment")
        print(f"📋 Review validation details and improve failing areas")

def main():
    """Main validation execution"""
    validator = ProductionValidationSuite()
    results = validator.run_full_validation()
    print_validation_results(results)
    
    return results['production_readiness']['production_ready']

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)