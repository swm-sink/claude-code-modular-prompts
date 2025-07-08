#!/usr/bin/env python3
"""Real-World Workflow Validation Runner for Meta-Prompting Framework.

This script demonstrates and validates the real-world workflow testing
framework by running comprehensive workflow scenarios that simulate actual
Claude Code usage patterns in realistic development scenarios.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.framework.test_real_world_workflows import (
    RealWorldWorkflowValidator,
    WorkflowScenario,
    WorkflowComplexity
)


def run_quick_workflow_validation():
    """Run quick workflow validation with core scenarios."""
    print("⚡ Quick Real-World Workflow Validation")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create output directory
    output_dir = project_root / "tests" / "results" / "workflows"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize workflow validator
    workflow_validator = RealWorldWorkflowValidator(project_root, output_dir)
    
    # Test core scenarios at simple complexity
    print("🧪 Testing Core Workflow Scenarios")
    print("-" * 40)
    
    core_scenarios = [
        WorkflowScenario.CODE_REVIEW,
        WorkflowScenario.FEATURE_DEVELOPMENT,
        WorkflowScenario.BUG_INVESTIGATION
    ]
    
    # Create simplified test cases
    test_cases = []
    for scenario in core_scenarios:
        test_case = workflow_validator._create_test_case(scenario, WorkflowComplexity.SIMPLE)
        test_cases.append(test_case)
    
    # Execute tests
    results = []
    for i, test_case in enumerate(test_cases):
        print(f"🔄 Executing: {test_case.name}")
        result = workflow_validator.workflow_executor.execute_workflow_test(test_case)
        results.append(result)
        
        if result.success:
            improvement = result.quality_assessment.get('improvement_percentage', 0)
            print(f"  ✅ Success: {improvement:.1f}% improvement")
        else:
            print(f"  ❌ Failed: {result.error_message}")
    
    # Quick analysis
    print("\n" + "=" * 50)
    print("📊 QUICK VALIDATION SUMMARY")
    print("=" * 50)
    
    successful = len([r for r in results if r.success])
    success_rate = (successful / len(results)) * 100
    
    print(f"Total Workflows: {len(results)}")
    print(f"Successful: {successful} ({success_rate:.1f}%)")
    print(f"Failed: {len(results) - successful}")
    
    if successful > 0:
        avg_improvement = sum(r.quality_assessment.get('improvement_percentage', 0) for r in results if r.success) / successful
        avg_execution_time = sum(r.execution_time_seconds for r in results if r.success) / successful
        
        print(f"Average Improvement: {avg_improvement:.1f}%")
        print(f"Average Execution Time: {avg_execution_time:.1f}s")
    
    # Validation result
    if success_rate >= 80 and (successful == 0 or avg_improvement >= 10):
        print("✅ QUICK VALIDATION PASSED")
        print("🚀 Core workflow scenarios show strong meta-prompting effectiveness")
        return 0
    else:
        print("⚠️  QUICK VALIDATION NEEDS ATTENTION")
        print("🔧 Core workflow scenarios may need optimization")
        return 1


def run_comprehensive_workflow_validation():
    """Run comprehensive workflow validation across all scenarios and complexities."""
    print("🚀 Comprehensive Real-World Workflow Validation")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create output directory
    output_dir = project_root / "tests" / "results" / "workflows"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize workflow validator
    workflow_validator = RealWorldWorkflowValidator(project_root, output_dir)
    
    # Run comprehensive workflow validation
    report = workflow_validator.run_workflow_validation()
    
    # Additional analysis
    print("\n" + "=" * 60)
    print("🔍 COMPREHENSIVE WORKFLOW ANALYSIS")
    print("=" * 60)
    
    # Analyze by scenario
    analyze_workflow_by_scenario(report)
    
    # Analyze by complexity
    analyze_workflow_by_complexity(report)
    
    # Validate readiness criteria
    validate_readiness_criteria(report)
    
    # Overall validation result
    readiness_score = report.real_world_readiness_score
    success_rate = report.performance_summary.get('success_rate', 0)
    avg_improvement = report.performance_summary.get('avg_improvement_percentage', 0)
    
    validation_passed = (
        readiness_score >= 0.7 and
        success_rate >= 80 and
        avg_improvement >= 15
    )
    
    print(f"\n🎯 OVERALL WORKFLOW VALIDATION:")
    if validation_passed:
        print("✅ COMPREHENSIVE VALIDATION PASSED")
        print("🚀 Framework demonstrates strong real-world effectiveness")
        return 0
    else:
        print("❌ COMPREHENSIVE VALIDATION FAILED")
        print("⚠️  Framework needs improvements for real-world deployment")
        print(f"   Readiness Score: {readiness_score:.3f} (target: ≥0.7)")
        print(f"   Success Rate: {success_rate:.1f}% (target: ≥80%)")
        print(f"   Average Improvement: {avg_improvement:.1f}% (target: ≥15%)")
        return 1


def analyze_workflow_by_scenario(report):
    """Analyze workflow results by scenario type."""
    print("📈 Results by Workflow Scenario:")
    
    for scenario, data in report.scenario_breakdown.items():
        success_rate = data.get('success_rate', 0)
        improvement = data.get('avg_improvement_percentage', 0)
        execution_time = data.get('avg_execution_time_seconds', 0)
        
        print(f"  {scenario.replace('_', ' ').title()}:")
        print(f"    Success Rate: {success_rate:.1f}% ({data.get('successful_tests', 0)}/{data.get('total_tests', 0)})")
        print(f"    Average Improvement: {improvement:.1f}%")
        print(f"    Average Execution Time: {execution_time:.1f}s")
        
        # Performance assessment
        if success_rate >= 90 and improvement >= 20:
            print(f"    Status: ✅ Excellent performance")
        elif success_rate >= 80 and improvement >= 15:
            print(f"    Status: ✅ Good performance")
        elif success_rate >= 70 and improvement >= 10:
            print(f"    Status: ⚠️  Moderate performance")
        else:
            print(f"    Status: ❌ Needs optimization")


def analyze_workflow_by_complexity(report):
    """Analyze workflow results by complexity level."""
    print("\n📊 Results by Complexity Level:")
    
    for complexity, data in report.complexity_analysis.items():
        success_rate = data.get('success_rate', 0)
        improvement = data.get('avg_improvement_percentage', 0)
        execution_time = data.get('avg_execution_time_seconds', 0)
        
        print(f"  {complexity.title()} Complexity:")
        print(f"    Success Rate: {success_rate:.1f}% ({data.get('successful_tests', 0)}/{data.get('total_tests', 0)})")
        print(f"    Average Improvement: {improvement:.1f}%")
        print(f"    Average Execution Time: {execution_time:.1f}s")
        
        # Complexity-specific assessment
        if complexity == "simple":
            target_success = 95
            target_improvement = 20
        elif complexity == "moderate":
            target_success = 85
            target_improvement = 15
        elif complexity == "complex":
            target_success = 75
            target_improvement = 10
        else:  # expert
            target_success = 70
            target_improvement = 5
        
        if success_rate >= target_success and improvement >= target_improvement:
            print(f"    Status: ✅ Meets complexity targets")
        else:
            print(f"    Status: ⚠️  Below complexity targets")


def validate_readiness_criteria(report):
    """Validate that real-world readiness criteria are met."""
    print("\n🎯 Real-World Readiness Criteria:")
    
    # Criterion 1: Overall success rate ≥ 80%
    success_rate = report.performance_summary.get('success_rate', 0)
    success_target_met = success_rate >= 80
    print(f"  Success Rate Target (≥80%): {'✅' if success_target_met else '❌'} {success_rate:.1f}%")
    
    # Criterion 2: Average improvement ≥ 15%
    avg_improvement = report.performance_summary.get('avg_improvement_percentage', 0)
    improvement_target_met = avg_improvement >= 15
    print(f"  Improvement Target (≥15%): {'✅' if improvement_target_met else '❌'} {avg_improvement:.1f}%")
    
    # Criterion 3: Average execution time ≤ 10s
    avg_execution_time = report.performance_summary.get('avg_execution_time_seconds', 0)
    execution_target_met = avg_execution_time <= 10
    print(f"  Execution Time Target (≤10s): {'✅' if execution_target_met else '❌'} {avg_execution_time:.1f}s")
    
    # Criterion 4: Readiness score ≥ 0.7
    readiness_score = report.real_world_readiness_score
    readiness_target_met = readiness_score >= 0.7
    print(f"  Readiness Score Target (≥0.7): {'✅' if readiness_target_met else '❌'} {readiness_score:.3f}")
    
    # Criterion 5: All core scenarios successful
    core_scenarios = ['code_review', 'feature_development', 'bug_investigation']
    core_success_rates = [
        report.scenario_breakdown.get(scenario, {}).get('success_rate', 0)
        for scenario in core_scenarios
    ]
    core_target_met = all(rate >= 80 for rate in core_success_rates)
    print(f"  Core Scenarios Target (all ≥80%): {'✅' if core_target_met else '❌'} {min(core_success_rates):.1f}% minimum")
    
    # Overall readiness assessment
    targets_met = sum([success_target_met, improvement_target_met, execution_target_met, readiness_target_met, core_target_met])
    total_targets = 5
    
    print(f"\n📊 Readiness Targets Met: {targets_met}/{total_targets} ({(targets_met/total_targets)*100:.0f}%)")
    
    if targets_met >= 4:
        print("✅ Real-world readiness criteria largely met - framework ready for deployment")
    elif targets_met >= 3:
        print("⚠️  Some readiness criteria missed - optimization recommended")
    else:
        print("❌ Significant readiness issues - extensive optimization required")


def run_scenario_specific_validation():
    """Run validation focused on specific high-value scenarios."""
    print("🎯 Scenario-Specific Workflow Validation")
    print("=" * 45)
    
    # Create output directory
    output_dir = project_root / "tests" / "results" / "workflows"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize workflow validator
    workflow_validator = RealWorldWorkflowValidator(project_root, output_dir)
    
    # Focus on high-value scenarios
    high_value_scenarios = [
        (WorkflowScenario.CODE_REVIEW, WorkflowComplexity.MODERATE),
        (WorkflowScenario.FEATURE_DEVELOPMENT, WorkflowComplexity.COMPLEX),
        (WorkflowScenario.BUG_INVESTIGATION, WorkflowComplexity.MODERATE),
        (WorkflowScenario.SECURITY_ANALYSIS, WorkflowComplexity.COMPLEX),
        (WorkflowScenario.PERFORMANCE_OPTIMIZATION, WorkflowComplexity.MODERATE)
    ]
    
    print(f"🧪 Testing {len(high_value_scenarios)} High-Value Scenarios")
    print("-" * 45)
    
    results = []
    for scenario, complexity in high_value_scenarios:
        test_case = workflow_validator._create_test_case(scenario, complexity)
        print(f"🔄 Executing: {scenario.value} ({complexity.value})")
        
        result = workflow_validator.workflow_executor.execute_workflow_test(test_case)
        results.append(result)
        
        if result.success:
            improvement = result.quality_assessment.get('improvement_percentage', 0)
            execution_time = result.execution_time_seconds
            print(f"  ✅ Success: {improvement:.1f}% improvement in {execution_time:.1f}s")
        else:
            print(f"  ❌ Failed: {result.error_message}")
    
    # Analyze high-value scenario results
    print("\n" + "=" * 45)
    print("📊 HIGH-VALUE SCENARIO ANALYSIS")
    print("=" * 45)
    
    successful = len([r for r in results if r.success])
    success_rate = (successful / len(results)) * 100
    
    print(f"Total High-Value Scenarios: {len(results)}")
    print(f"Successful: {successful} ({success_rate:.1f}%)")
    
    if successful > 0:
        avg_improvement = sum(r.quality_assessment.get('improvement_percentage', 0) for r in results if r.success) / successful
        avg_execution_time = sum(r.execution_time_seconds for r in results if r.success) / successful
        
        print(f"Average Improvement: {avg_improvement:.1f}%")
        print(f"Average Execution Time: {avg_execution_time:.1f}s")
        
        # High-value scenario assessment
        if success_rate >= 80 and avg_improvement >= 20:
            print("✅ HIGH-VALUE SCENARIOS EXCEL")
            print("🚀 Framework demonstrates exceptional performance on critical workflows")
            return 0
        elif success_rate >= 70 and avg_improvement >= 15:
            print("✅ HIGH-VALUE SCENARIOS GOOD")
            print("👍 Framework performs well on critical workflows")
            return 0
        else:
            print("⚠️  HIGH-VALUE SCENARIOS NEED IMPROVEMENT")
            print("🔧 Framework requires optimization for critical workflows")
            return 1
    else:
        print("❌ HIGH-VALUE SCENARIOS FAILED")
        print("🔥 Framework not ready for critical workflows")
        return 1


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(description="Run real-world workflow validation")
    parser.add_argument(
        "--mode",
        choices=["quick", "comprehensive", "scenario-specific"],
        default="quick",
        help="Validation mode: quick (core scenarios), comprehensive (all scenarios), or scenario-specific (high-value scenarios)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_root / "tests" / "results" / "workflows",
        help="Output directory for validation results"
    )
    
    args = parser.parse_args()
    
    try:
        if args.mode == "comprehensive":
            return run_comprehensive_workflow_validation()
        elif args.mode == "scenario-specific":
            return run_scenario_specific_validation()
        else:
            return run_quick_workflow_validation()
    
    except KeyboardInterrupt:
        print("\n⚠️  Validation interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Error during validation: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())