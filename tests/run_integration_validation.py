#!/usr/bin/env python3
"""Integration Test Validation Runner for Claude Code Framework.

This script demonstrates and validates the Claude Code integration testing
framework by running comprehensive tests that validate actual framework
functionality in a real Claude Code environment.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add project root to Python path  
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.framework.claude_code_integration_tests import (
    ClaudeCodeIntegrationTester,
    IntegrationTestType
)


def run_quick_integration_validation():
    """Run quick integration validation with core functionality tests."""
    print("⚡ Quick Claude Code Integration Validation")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create output directory
    output_dir = project_root / "tests" / "results" / "integration"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize integration tester
    integration_tester = ClaudeCodeIntegrationTester(project_root, output_dir)
    
    # Run core test suites for quick validation
    print("🧪 Running Core Integration Test Suites")
    print("-" * 40)
    
    all_results = []
    suites_to_run = ["command_execution", "module_orchestration"]
    
    for suite_name in suites_to_run:
        print(f"\n📋 Testing Suite: {suite_name}")
        suite_results = integration_tester.run_test_suite(suite_name)
        all_results.extend(suite_results)
    
    # Print quick summary
    print("\n" + "=" * 50)
    print("📊 QUICK VALIDATION SUMMARY")
    print("=" * 50)
    
    total_tests = len(all_results)
    passed_tests = len([r for r in all_results if r.result.value == "pass"])
    failed_tests = len([r for r in all_results if r.result.value == "fail"])
    error_tests = len([r for r in all_results if r.result.value == "error"])
    
    success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests} ({success_rate:.1f}%)")
    print(f"Failed: {failed_tests}")
    print(f"Errors: {error_tests}")
    
    # Calculate average execution time
    avg_time = sum(r.execution_time_ms for r in all_results) / len(all_results) if all_results else 0
    print(f"Average Execution Time: {avg_time:.1f}ms")
    
    # Validation result
    if success_rate >= 80:
        print("✅ QUICK VALIDATION PASSED")
        print("🚀 Core framework integration is working correctly")
        return 0
    else:
        print("❌ QUICK VALIDATION FAILED")
        print("⚠️  Core framework integration needs attention")
        return 1


def run_comprehensive_integration_validation():
    """Run comprehensive integration validation across all test suites."""
    print("🚀 Comprehensive Claude Code Integration Validation")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create output directory
    output_dir = project_root / "tests" / "results" / "integration"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize integration tester
    integration_tester = ClaudeCodeIntegrationTester(project_root, output_dir)
    
    # Run comprehensive integration tests
    report = integration_tester.run_comprehensive_integration_tests()
    
    # Additional validation checks
    print("\n" + "=" * 60)
    print("🔍 COMPREHENSIVE VALIDATION ANALYSIS")
    print("=" * 60)
    
    # Analyze results by test type
    analyze_results_by_type(report.test_results)
    
    # Validate performance targets
    validate_performance_targets(report)
    
    # Overall validation result
    success_rate = report.performance_summary.get("success_rate", 0)
    p95_time = report.performance_summary.get("p95_execution_time", 0)
    
    validation_passed = (
        success_rate >= 85 and
        p95_time <= 200 and
        report.error_tests <= 2
    )
    
    print(f"\n🎯 OVERALL VALIDATION RESULT:")
    if validation_passed:
        print("✅ COMPREHENSIVE VALIDATION PASSED")
        print("🚀 Framework is ready for production integration testing")
        return 0
    else:
        print("❌ COMPREHENSIVE VALIDATION FAILED") 
        print("⚠️  Framework needs improvements before production deployment")
        print(f"   Success Rate: {success_rate:.1f}% (target: ≥85%)")
        print(f"   P95 Time: {p95_time:.1f}ms (target: ≤200ms)")
        print(f"   Error Tests: {report.error_tests} (target: ≤2)")
        return 1


def analyze_results_by_type(test_results):
    """Analyze test results broken down by integration test type."""
    print("📈 Results by Test Type:")
    
    type_analysis = {}
    
    for result in test_results:
        test_type = result.test_case.test_type.value
        
        if test_type not in type_analysis:
            type_analysis[test_type] = {
                "total": 0,
                "passed": 0,
                "failed": 0,
                "errors": 0,
                "avg_time": []
            }
        
        type_analysis[test_type]["total"] += 1
        type_analysis[test_type]["avg_time"].append(result.execution_time_ms)
        
        if result.result.value == "pass":
            type_analysis[test_type]["passed"] += 1
        elif result.result.value == "fail":
            type_analysis[test_type]["failed"] += 1
        else:
            type_analysis[test_type]["errors"] += 1
    
    for test_type, data in type_analysis.items():
        success_rate = (data["passed"] / data["total"]) * 100 if data["total"] > 0 else 0
        avg_time = sum(data["avg_time"]) / len(data["avg_time"]) if data["avg_time"] else 0
        
        print(f"  {test_type.replace('_', ' ').title()}:")
        print(f"    Success Rate: {success_rate:.1f}% ({data['passed']}/{data['total']})")
        print(f"    Average Time: {avg_time:.1f}ms")
        
        if data["failed"] > 0:
            print(f"    ⚠️  {data['failed']} failed tests")
        if data["errors"] > 0:
            print(f"    🔥 {data['errors']} error tests")


def validate_performance_targets(report):
    """Validate that performance targets are being met."""
    print("\n🎯 Performance Target Validation:")
    
    perf = report.performance_summary
    
    # Target 1: Success rate ≥ 85%
    success_rate = perf.get("success_rate", 0)
    success_target_met = success_rate >= 85
    print(f"  Success Rate Target (≥85%): {'✅' if success_target_met else '❌'} {success_rate:.1f}%")
    
    # Target 2: P95 execution time ≤ 200ms
    p95_time = perf.get("p95_execution_time", 0)
    p95_target_met = p95_time <= 200
    print(f"  P95 Execution Time Target (≤200ms): {'✅' if p95_target_met else '❌'} {p95_time:.1f}ms")
    
    # Target 3: Average execution time ≤ 100ms
    avg_time = perf.get("avg_execution_time", 0)
    avg_target_met = avg_time <= 100
    print(f"  Average Execution Time Target (≤100ms): {'✅' if avg_target_met else '❌'} {avg_time:.1f}ms")
    
    # Target 4: Error rate ≤ 5%
    error_rate = ((report.error_tests + report.timeout_tests) / report.total_tests) * 100 if report.total_tests > 0 else 0
    error_target_met = error_rate <= 5
    print(f"  Error Rate Target (≤5%): {'✅' if error_target_met else '❌'} {error_rate:.1f}%")
    
    # Overall performance assessment
    targets_met = sum([success_target_met, p95_target_met, avg_target_met, error_target_met])
    total_targets = 4
    
    print(f"\n📊 Performance Targets Met: {targets_met}/{total_targets} ({(targets_met/total_targets)*100:.0f}%)")
    
    if targets_met >= 3:
        print("✅ Performance targets largely met - framework ready for production")
    elif targets_met >= 2:
        print("⚠️  Some performance targets missed - optimization recommended")
    else:
        print("❌ Significant performance issues - optimization required")


def run_framework_structure_validation():
    """Validate framework structure and configuration."""
    print("🔍 Framework Structure Validation")
    print("=" * 40)
    
    validation_passed = True
    
    # Check key files exist
    key_files = [
        "CLAUDE.md",
        ".claude/commands/task.md",
        ".claude/commands/auto.md", 
        ".claude/commands/feature.md",
        ".claude/modules/development/task-management.md",
        ".claude/modules/quality/tdd.md"
    ]
    
    print("📂 Checking Key Framework Files:")
    for file_path in key_files:
        full_path = project_root / file_path
        exists = full_path.exists()
        print(f"  {'✅' if exists else '❌'} {file_path}")
        if not exists:
            validation_passed = False
    
    # Check meta-modules
    meta_modules_dir = project_root / ".claude" / "modules" / "meta"
    if meta_modules_dir.exists():
        meta_count = len(list(meta_modules_dir.glob("*.md")))
        print(f"\n🧠 Meta-Modules Found: {meta_count}")
        if meta_count >= 8:
            print("  ✅ Sufficient meta-modules for testing")
        else:
            print("  ⚠️  Limited meta-modules available")
    else:
        print("\n❌ Meta-modules directory not found")
        validation_passed = False
    
    # Check test infrastructure
    test_files = [
        "tests/framework/test_meta_prompt_effectiveness.py",
        "tests/framework/ab_testing_framework.py",
        "tests/framework/claude_code_integration_tests.py"
    ]
    
    print(f"\n🧪 Checking Test Infrastructure:")
    for file_path in test_files:
        full_path = project_root / file_path
        exists = full_path.exists()
        print(f"  {'✅' if exists else '❌'} {file_path}")
        if not exists:
            validation_passed = False
    
    print(f"\n📋 Structure Validation: {'✅ PASSED' if validation_passed else '❌ FAILED'}")
    return 0 if validation_passed else 1


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(description="Run Claude Code integration validation")
    parser.add_argument(
        "--mode",
        choices=["quick", "comprehensive", "structure"],
        default="quick",
        help="Validation mode: quick (core tests), comprehensive (all tests), or structure (framework validation)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_root / "tests" / "results" / "integration",
        help="Output directory for test results"
    )
    
    args = parser.parse_args()
    
    try:
        if args.mode == "comprehensive":
            return run_comprehensive_integration_validation()
        elif args.mode == "structure":
            return run_framework_structure_validation()
        else:
            return run_quick_integration_validation()
    
    except KeyboardInterrupt:
        print("\n⚠️  Test interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Error during validation: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())