#!/usr/bin/env python3
"""
Comprehensive Component Testing Framework

Automated testing and validation system for atomic components.
Combines unit testing, integration testing, and continuous validation
with comprehensive reporting and regression detection.

Usage:
    python3 component-testing-framework.py                    # Run all tests
    python3 component-testing-framework.py --unit             # Unit tests only
    python3 component-testing-framework.py --integration      # Integration tests only
    python3 component-testing-framework.py --continuous       # Continuous monitoring mode
    python3 component-testing-framework.py --report          # Generate detailed report
"""

import os
import sys
import json
import time
import argparse
import importlib.util
from datetime import datetime
from typing import Dict, List, Any, Tuple
from pathlib import Path

# Import our existing testing modules using importlib for files with hyphens
def import_module_from_path(module_name: str, file_path: str):
    """Import a module from a file path"""
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception:
        return None

# Try to import testing modules
current_dir = Path(__file__).parent
unit_tester_module = import_module_from_path("component_unit_tester", current_dir / "component-unit-tester.py")
integration_tester_module = import_module_from_path("component_integration_tester", current_dir / "component-integration-tester.py")
standards_validator_module = import_module_from_path("validate_component_standards", current_dir / "validate-component-standards.py")

# Extract classes if modules loaded successfully
ComponentUnitTester = getattr(unit_tester_module, 'ComponentUnitTester', None) if unit_tester_module else None
ComponentIntegrationTester = getattr(integration_tester_module, 'ComponentIntegrationTester', None) if integration_tester_module else None
ComponentValidator = getattr(standards_validator_module, 'ComponentValidator', None) if standards_validator_module else None

class ComponentTestingFramework:
    def __init__(self):
        self.components_dir = Path('.claude/components/atomic')
        self.reports_dir = Path('.claude/reports')
        self.reports_dir.mkdir(exist_ok=True)
        
        # Initialize sub-testers
        self.unit_tester = ComponentUnitTester() if ComponentUnitTester else None
        self.integration_tester = ComponentIntegrationTester() if ComponentIntegrationTester else None
        self.standards_validator = ComponentValidator() if ComponentValidator else None
        
        # Test configuration
        self.test_config = {
            'unit_test_threshold': 70.0,  # Minimum pass rate for unit tests
            'integration_test_threshold': 60.0,  # Minimum pass rate for integration tests
            'overall_health_threshold': 75.0,  # Minimum overall health score
            'critical_components': [  # Components that must always pass
                'file-reader', 'git-operations', 'dependency-resolver', 'state-manager'
            ]
        }
        
        # Test history tracking
        self.history_file = self.reports_dir / 'test-history.json'
    
    def discover_components(self) -> List[str]:
        """Discover all atomic components in the directory"""
        if not self.components_dir.exists():
            return []
        
        components = []
        for file_path in self.components_dir.glob('*.md'):
            components.append(file_path.stem)
        
        return sorted(components)
    
    def run_structural_validation(self) -> Dict[str, Any]:
        """Run structural validation tests"""
        print("🏗️  STRUCTURAL VALIDATION")
        print("=" * 50)
        
        if not self.standards_validator:
            print("❌ Standards validator not available")
            return {"available": False}
        
        components = self.discover_components()
        total_components = len(components)
        passed_components = 0
        detailed_results = []
        
        for component in components:
            file_path = self.components_dir / f"{component}.md"
            is_valid, details = self.standards_validator.validate_component(str(file_path))
            
            if is_valid:
                passed_components += 1
                status = "✅"
            else:
                status = "❌"
            
            max_score = details.get('total_checks', 8)  # Default to 8 checks
            print(f"{status} {component}: {details['score']}/{max_score} ({details['score']/max_score*100:.1f}%)")
            
            detailed_results.append({
                "component": component,
                "valid": is_valid,
                "details": details
            })
        
        pass_rate = (passed_components / total_components * 100) if total_components > 0 else 0
        print(f"\\nStructural Validation: {passed_components}/{total_components} valid ({pass_rate:.1f}%)")
        
        return {
            "available": True,
            "total": total_components,
            "passed": passed_components,
            "pass_rate": pass_rate,
            "results": detailed_results
        }
    
    def run_unit_tests(self) -> Dict[str, Any]:
        """Run individual component unit tests"""
        print("\\n🧪 UNIT TESTING")
        print("=" * 50)
        
        if not self.unit_tester:
            print("❌ Unit tester not available")
            return {"available": False}
        
        # Run unit tests using existing framework
        results = self.unit_tester.test_all_components()
        
        # Extract component scores for critical analysis
        component_scores = {}
        if 'components' in results:
            for comp_name, comp_data in results['components'].items():
                component_scores[comp_name] = comp_data.get('score', 0)
        
        # Add component_scores to results for critical analysis
        results['component_scores'] = component_scores
        results['overall_pass_rate'] = results.get('summary', {}).get('pass_rate', 0)
        results['available'] = True
        
        return results
    
    def run_integration_tests(self) -> Dict[str, Any]:
        """Run component integration tests"""
        print("\\n🔗 INTEGRATION TESTING")
        print("=" * 50)
        
        if not self.integration_tester:
            print("❌ Integration tester not available")
            return {"available": False}
        
        # Run integration tests using existing framework
        results = self.integration_tester.run_all_tests()
        results['available'] = True
        return results
    
    def analyze_critical_components(self, unit_results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze the health of critical components"""
        print("\\n🎯 CRITICAL COMPONENT ANALYSIS")
        print("=" * 50)
        
        critical_analysis = {
            "total_critical": len(self.test_config['critical_components']),
            "passing_critical": 0,
            "failing_critical": [],
            "critical_health": 0.0
        }
        
        if not unit_results.get('available') or 'component_scores' not in unit_results:
            print("❌ Unit test results not available for critical analysis")
            return critical_analysis
        
        component_scores = unit_results['component_scores']
        
        for component in self.test_config['critical_components']:
            # Try both with and without .md extension
            component_key = None
            for key in component_scores.keys():
                if key == component or key == f"{component}.md":
                    component_key = key
                    break
            
            if component_key:
                score = component_scores[component_key]
                if score >= self.test_config['unit_test_threshold']:
                    critical_analysis['passing_critical'] += 1
                    status = "✅"
                else:
                    critical_analysis['failing_critical'].append({
                        "component": component,
                        "score": score,
                        "threshold": self.test_config['unit_test_threshold']
                    })
                    status = "❌"
                
                print(f"{status} {component}: {score:.1f}% (Critical)")
            else:
                print(f"⚠️  {component}: Not found in unit test results")
                critical_analysis['failing_critical'].append({
                    "component": component,
                    "score": 0,
                    "threshold": self.test_config['unit_test_threshold']
                })
        
        critical_analysis['critical_health'] = (
            critical_analysis['passing_critical'] / critical_analysis['total_critical'] * 100
            if critical_analysis['total_critical'] > 0 else 0
        )
        
        print(f"\\nCritical Components Health: {critical_analysis['critical_health']:.1f}%")
        
        return critical_analysis
    
    def calculate_overall_health(self, structural: Dict, unit: Dict, integration: Dict, critical: Dict) -> Dict[str, Any]:
        """Calculate overall component system health"""
        print("\\n📊 OVERALL HEALTH ASSESSMENT")
        print("=" * 50)
        
        health_metrics = {
            "structural_weight": 0.2,
            "unit_weight": 0.4,
            "integration_weight": 0.3,
            "critical_weight": 0.1
        }
        
        scores = {
            "structural": structural.get('pass_rate', 0) if structural.get('available') else 0,
            "unit": unit.get('overall_pass_rate', 0) if unit.get('available') else 0,
            "integration": integration.get('overall', {}).get('pass_rate', 0) if integration.get('available') else 0,
            "critical": critical.get('critical_health', 0)
        }
        
        # Calculate weighted overall health
        overall_health = (
            scores['structural'] * health_metrics['structural_weight'] +
            scores['unit'] * health_metrics['unit_weight'] +
            scores['integration'] * health_metrics['integration_weight'] +
            scores['critical'] * health_metrics['critical_weight']
        )
        
        # Determine health grade
        if overall_health >= 90:
            grade = "A"
            status = "Excellent"
        elif overall_health >= 80:
            grade = "B" 
            status = "Good"
        elif overall_health >= 70:
            grade = "C"
            status = "Acceptable"
        elif overall_health >= 60:
            grade = "D"
            status = "Needs Improvement"
        else:
            grade = "F"
            status = "Critical Issues"
        
        print(f"Structural Validation: {scores['structural']:.1f}% (Weight: {health_metrics['structural_weight']*100:.0f}%)")
        print(f"Unit Tests: {scores['unit']:.1f}% (Weight: {health_metrics['unit_weight']*100:.0f}%)")
        print(f"Integration Tests: {scores['integration']:.1f}% (Weight: {health_metrics['integration_weight']*100:.0f}%)")
        print(f"Critical Components: {scores['critical']:.1f}% (Weight: {health_metrics['critical_weight']*100:.0f}%)")
        print(f"\\n🏆 Overall Health: {overall_health:.1f}% (Grade: {grade} - {status})")
        
        return {
            "scores": scores,
            "weights": health_metrics,
            "overall_health": overall_health,
            "grade": grade,
            "status": status,
            "meets_threshold": overall_health >= self.test_config['overall_health_threshold']
        }
    
    def save_test_history(self, test_results: Dict[str, Any]) -> None:
        """Save test results to history for trend analysis"""
        timestamp = datetime.now().isoformat()
        
        history_entry = {
            "timestamp": timestamp,
            "overall_health": test_results.get('overall_health', {}).get('overall_health', 0),
            "unit_pass_rate": test_results.get('unit_tests', {}).get('overall_pass_rate', 0),
            "integration_pass_rate": test_results.get('integration_tests', {}).get('overall', {}).get('pass_rate', 0),
            "critical_health": test_results.get('critical_analysis', {}).get('critical_health', 0),
            "total_components": len(self.discover_components())
        }
        
        # Load existing history
        history = []
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    history = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                history = []
        
        # Add new entry
        history.append(history_entry)
        
        # Keep only last 50 entries
        history = history[-50:]
        
        # Save updated history
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    def detect_regressions(self) -> Dict[str, Any]:
        """Detect regressions by comparing with previous test results"""
        if not self.history_file.exists():
            return {"available": False}
        
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {"available": False}
        
        if len(history) < 2:
            return {"available": False, "reason": "Insufficient history"}
        
        current = history[-1]
        previous = history[-2]
        
        regressions = []
        improvements = []
        
        metrics = ['overall_health', 'unit_pass_rate', 'integration_pass_rate', 'critical_health']
        
        for metric in metrics:
            current_value = current.get(metric, 0)
            previous_value = previous.get(metric, 0)
            change = current_value - previous_value
            
            if change < -5:  # Regression threshold: -5%
                regressions.append({
                    "metric": metric,
                    "previous": previous_value,
                    "current": current_value,
                    "change": change
                })
            elif change > 5:  # Improvement threshold: +5%
                improvements.append({
                    "metric": metric,
                    "previous": previous_value,
                    "current": current_value,
                    "change": change
                })
        
        return {
            "available": True,
            "regressions": regressions,
            "improvements": improvements,
            "has_regressions": len(regressions) > 0,
            "has_improvements": len(improvements) > 0
        }
    
    def generate_detailed_report(self, test_results: Dict[str, Any]) -> str:
        """Generate a detailed test report"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = f"""# Component Testing Framework Report
Generated: {timestamp}

## Executive Summary
Overall Health: {test_results.get('overall_health', {}).get('overall_health', 0):.1f}% 
Grade: {test_results.get('overall_health', {}).get('grade', 'N/A')}
Status: {test_results.get('overall_health', {}).get('status', 'Unknown')}

## Test Results Summary

### Structural Validation
- Pass Rate: {test_results.get('structural_validation', {}).get('pass_rate', 0):.1f}%
- Components Validated: {test_results.get('structural_validation', {}).get('total', 0)}

### Unit Testing  
- Pass Rate: {test_results.get('unit_tests', {}).get('overall_pass_rate', 0):.1f}%
- Components Tested: {test_results.get('unit_tests', {}).get('total_components', 0)}

### Integration Testing
- Pass Rate: {test_results.get('integration_tests', {}).get('overall', {}).get('pass_rate', 0):.1f}%
- Tests Executed: {test_results.get('integration_tests', {}).get('overall', {}).get('total_tests', 0)}

### Critical Components
- Health Score: {test_results.get('critical_analysis', {}).get('critical_health', 0):.1f}%
- Passing: {test_results.get('critical_analysis', {}).get('passing_critical', 0)}/{test_results.get('critical_analysis', {}).get('total_critical', 0)}

## Recommendations
"""
        
        # Add recommendations based on results
        overall_health = test_results.get('overall_health', {}).get('overall_health', 0)
        
        if overall_health >= 80:
            report += "- ✅ System health is good. Continue monitoring.\n"
        elif overall_health >= 70:
            report += "- ⚠️ System health is acceptable but could be improved.\n"
        else:
            report += "- ❌ System health needs immediate attention.\n"
        
        # Check for failing critical components
        failing_critical = test_results.get('critical_analysis', {}).get('failing_critical', [])
        if failing_critical:
            report += f"- 🎯 Fix {len(failing_critical)} failing critical components immediately.\n"
        
        # Check test thresholds
        unit_pass_rate = test_results.get('unit_tests', {}).get('overall_pass_rate', 0)
        if unit_pass_rate < self.test_config['unit_test_threshold']:
            report += f"- 🧪 Unit test pass rate ({unit_pass_rate:.1f}%) below threshold ({self.test_config['unit_test_threshold']:.1f}%).\n"
        
        integration_pass_rate = test_results.get('integration_tests', {}).get('overall', {}).get('pass_rate', 0)
        if integration_pass_rate < self.test_config['integration_test_threshold']:
            report += f"- 🔗 Integration test pass rate ({integration_pass_rate:.1f}%) below threshold ({self.test_config['integration_test_threshold']:.1f}%).\n"
        
        report += f"\\n*Report generated by Component Testing Framework v1.0*"
        
        return report
    
    def run_comprehensive_tests(self) -> Dict[str, Any]:
        """Run all tests and generate comprehensive results"""
        print("🔬 COMPREHENSIVE COMPONENT TESTING FRAMEWORK")
        print("=" * 70)
        print(f"Testing {len(self.discover_components())} atomic components")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Run all test categories
        structural_results = self.run_structural_validation()
        unit_results = self.run_unit_tests()
        integration_results = self.run_integration_tests()
        critical_results = self.analyze_critical_components(unit_results)
        overall_health = self.calculate_overall_health(
            structural_results, unit_results, integration_results, critical_results
        )
        
        # Compile comprehensive results
        test_results = {
            "timestamp": datetime.now().isoformat(),
            "structural_validation": structural_results,
            "unit_tests": unit_results,
            "integration_tests": integration_results,
            "critical_analysis": critical_results,
            "overall_health": overall_health
        }
        
        # Save to history and detect regressions
        self.save_test_history(test_results)
        regression_analysis = self.detect_regressions()
        test_results["regression_analysis"] = regression_analysis
        
        # Display regression information
        if regression_analysis.get('available') and regression_analysis.get('has_regressions'):
            print("\\n⚠️  REGRESSIONS DETECTED")
            print("=" * 50)
            for regression in regression_analysis['regressions']:
                print(f"❌ {regression['metric']}: {regression['previous']:.1f}% → {regression['current']:.1f}% ({regression['change']:+.1f}%)")
        
        if regression_analysis.get('available') and regression_analysis.get('has_improvements'):
            print("\\n🎉 IMPROVEMENTS DETECTED")
            print("=" * 50)
            for improvement in regression_analysis['improvements']:
                print(f"✅ {improvement['metric']}: {improvement['previous']:.1f}% → {improvement['current']:.1f}% ({improvement['change']:+.1f}%)")
        
        return test_results
    
    def continuous_monitoring(self, interval_minutes: int = 30) -> None:
        """Run continuous monitoring of component health"""
        print(f"🔄 Starting continuous monitoring (every {interval_minutes} minutes)")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                print(f"\\n⏰ Running scheduled tests - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                results = self.run_comprehensive_tests()
                
                # Check if health is below threshold
                overall_health = results.get('overall_health', {}).get('overall_health', 0)
                if overall_health < self.test_config['overall_health_threshold']:
                    print(f"\\n🚨 HEALTH ALERT: Overall health ({overall_health:.1f}%) below threshold ({self.test_config['overall_health_threshold']:.1f}%)")
                
                # Sleep until next run
                print(f"\\n😴 Sleeping for {interval_minutes} minutes...")
                time.sleep(interval_minutes * 60)
                
        except KeyboardInterrupt:
            print("\\n🛑 Continuous monitoring stopped")

def main():
    parser = argparse.ArgumentParser(description='Comprehensive Component Testing Framework')
    parser.add_argument('--unit', action='store_true', help='Run unit tests only')
    parser.add_argument('--integration', action='store_true', help='Run integration tests only')
    parser.add_argument('--structural', action='store_true', help='Run structural validation only')
    parser.add_argument('--critical', action='store_true', help='Analyze critical components only')
    parser.add_argument('--continuous', type=int, metavar='MINUTES', help='Run continuous monitoring (interval in minutes)')
    parser.add_argument('--report', action='store_true', help='Generate detailed report')
    args = parser.parse_args()
    
    framework = ComponentTestingFramework()
    
    # Handle specific test types
    if args.structural:
        framework.run_structural_validation()
    elif args.unit:
        framework.run_unit_tests()
    elif args.integration:
        framework.run_integration_tests()
    elif args.critical:
        unit_results = framework.run_unit_tests()
        framework.analyze_critical_components(unit_results)
    elif args.continuous:
        framework.continuous_monitoring(args.continuous)
    else:
        # Run comprehensive tests
        results = framework.run_comprehensive_tests()
        
        # Generate report if requested
        if args.report:
            report = framework.generate_detailed_report(results)
            report_file = framework.reports_dir / f"component-test-report-{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(report_file, 'w') as f:
                f.write(report)
            print(f"\\n📋 Detailed report saved to: {report_file}")

if __name__ == "__main__":
    main()