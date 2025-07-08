#!/usr/bin/env python3
"""A/B Test Validation Runner for Meta-Prompting Framework.

This script demonstrates and validates the A/B testing framework by running
comprehensive tests comparing baseline vs meta-enhanced prompts.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.framework.ab_testing_framework import (
    ABTestingFramework, 
    TestScenarioType,
    ABTestConfiguration
)


def run_comprehensive_validation():
    """Run comprehensive A/B test validation across all scenarios."""
    print("🚀 Meta-Prompting Framework A/B Test Validation")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create output directory
    output_dir = project_root / "tests" / "results" / "ab_testing"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize A/B testing framework
    ab_framework = ABTestingFramework(output_dir)
    
    # Test Configuration 1: Comprehensive validation across all scenarios
    print("🧪 Test 1: Comprehensive Multi-Scenario Validation")
    print("-" * 50)
    
    comprehensive_config = ab_framework.create_test_configuration(
        test_name="comprehensive_meta_prompting_validation",
        description="Complete validation of meta-prompting effectiveness across all scenario types",
        sample_size=25,
        scenarios=list(TestScenarioType)
    )
    
    comprehensive_report = ab_framework.run_ab_test(comprehensive_config)
    print_test_summary(comprehensive_report, "Comprehensive Validation")
    
    # Test Configuration 2: High-stakes scenarios (complex reasoning and architectural analysis)
    print("\n🧪 Test 2: High-Stakes Scenarios Validation")
    print("-" * 50)
    
    high_stakes_config = ab_framework.create_test_configuration(
        test_name="high_stakes_scenarios_validation",
        description="Validation focused on complex reasoning and architectural analysis scenarios",
        sample_size=40,
        scenarios=[
            TestScenarioType.COMPLEX_REASONING,
            TestScenarioType.ARCHITECTURAL_ANALYSIS,
            TestScenarioType.PROBLEM_SOLVING
        ]
    )
    
    high_stakes_report = ab_framework.run_ab_test(high_stakes_config)
    print_test_summary(high_stakes_report, "High-Stakes Scenarios")
    
    # Test Configuration 3: Development workflows (task completion and code generation)
    print("\n🧪 Test 3: Development Workflow Validation")
    print("-" * 50)
    
    dev_workflow_config = ab_framework.create_test_configuration(
        test_name="development_workflow_validation",
        description="Validation focused on development and workflow optimization scenarios",
        sample_size=35,
        scenarios=[
            TestScenarioType.SIMPLE_TASK,
            TestScenarioType.CODE_GENERATION,
            TestScenarioType.WORKFLOW_OPTIMIZATION
        ]
    )
    
    dev_workflow_report = ab_framework.run_ab_test(dev_workflow_config)
    print_test_summary(dev_workflow_report, "Development Workflow")
    
    # Generate overall summary
    print("\n" + "=" * 60)
    print("📊 OVERALL VALIDATION SUMMARY")
    print("=" * 60)
    
    all_reports = [comprehensive_report, high_stakes_report, dev_workflow_report]
    generate_overall_summary(all_reports)
    
    # Validation results
    print("\n🎯 VALIDATION RESULTS:")
    validation_passed = validate_framework_effectiveness(all_reports)
    
    if validation_passed:
        print("✅ Meta-Prompting Framework VALIDATION PASSED")
        print("🚀 Framework demonstrates significant effectiveness improvements")
        return 0
    else:
        print("❌ Meta-Prompting Framework VALIDATION FAILED") 
        print("⚠️  Framework needs further optimization before production deployment")
        return 1


def print_test_summary(report, test_name):
    """Print a summary of A/B test results."""
    overall = report.statistical_summary["overall"]
    
    print(f"📈 {test_name} Results:")
    print(f"  Total Tests: {report.total_tests_run}")
    print(f"  Baseline Average: {overall.baseline_mean:.2f}/10")
    print(f"  Meta-Enhanced Average: {overall.meta_enhanced_mean:.2f}/10")
    print(f"  Improvement: {overall.improvement_percentage:.1f}%")
    print(f"  Statistically Significant: {'YES' if overall.statistical_significance else 'NO'}")
    print(f"  P-Value: {overall.p_value:.4f}")
    print(f"  Effect Size: {overall.effect_size:.3f}")
    
    # Performance metrics
    performance = report.detailed_analysis["performance_metrics"]
    print(f"  Response Time Improvement: {performance['response_time_improvement']:.1f}%")
    
    # Top recommendation
    if report.recommendations:
        print(f"  Top Recommendation: {report.recommendations[0]}")


def generate_overall_summary(reports):
    """Generate an overall summary across all test reports."""
    total_tests = sum(r.total_tests_run for r in reports)
    
    # Calculate weighted averages
    total_weight = 0
    weighted_improvement = 0
    significant_tests = 0
    
    for report in reports:
        overall = report.statistical_summary["overall"]
        weight = report.total_tests_run
        total_weight += weight
        weighted_improvement += overall.improvement_percentage * weight
        
        if overall.statistical_significance:
            significant_tests += 1
    
    avg_improvement = weighted_improvement / total_weight if total_weight > 0 else 0
    significance_rate = (significant_tests / len(reports)) * 100
    
    print(f"Total Tests Executed: {total_tests}")
    print(f"Average Improvement: {avg_improvement:.1f}%")
    print(f"Statistical Significance Rate: {significance_rate:.0f}%")
    
    # Analyze by scenario type
    print(f"\n📊 Performance by Scenario Type:")
    scenario_performance = analyze_scenario_performance(reports)
    
    for scenario, perf in scenario_performance.items():
        print(f"  {scenario}: {perf['improvement']:.1f}% improvement "
              f"({perf['tests']} tests, {perf['significant']} significant)")


def analyze_scenario_performance(reports):
    """Analyze performance across different scenario types."""
    scenario_data = {}
    
    for report in reports:
        scenario_analysis = report.detailed_analysis["scenario_breakdown"]
        
        for scenario, data in scenario_analysis.items():
            if scenario not in scenario_data:
                scenario_data[scenario] = {
                    "improvements": [],
                    "tests": 0,
                    "significant": 0
                }
            
            scenario_data[scenario]["improvements"].append(data["improvement_percentage"])
            scenario_data[scenario]["tests"] += data["sample_size"]
            
            # Check if this scenario was statistically significant in this report
            # This is a simplification - in a real implementation, you'd track significance per scenario
            if report.statistical_summary["overall"].statistical_significance:
                scenario_data[scenario]["significant"] += 1
    
    # Calculate averages
    scenario_performance = {}
    for scenario, data in scenario_data.items():
        avg_improvement = sum(data["improvements"]) / len(data["improvements"]) if data["improvements"] else 0
        scenario_performance[scenario] = {
            "improvement": avg_improvement,
            "tests": data["tests"],
            "significant": data["significant"]
        }
    
    return scenario_performance


def validate_framework_effectiveness(reports):
    """Validate that the framework meets effectiveness criteria."""
    print("\n🔍 VALIDATION CRITERIA:")
    
    criteria_met = 0
    total_criteria = 5
    
    # Criterion 1: Overall improvement > 10%
    total_improvement = sum(r.statistical_summary["overall"].improvement_percentage for r in reports) / len(reports)
    improvement_met = total_improvement > 10
    print(f"  1. Average improvement > 10%: {'✅' if improvement_met else '❌'} ({total_improvement:.1f}%)")
    if improvement_met:
        criteria_met += 1
    
    # Criterion 2: Statistical significance in majority of tests
    significant_tests = sum(1 for r in reports if r.statistical_summary["overall"].statistical_significance)
    significance_met = significant_tests >= len(reports) * 0.6
    print(f"  2. Statistical significance in ≥60% of tests: {'✅' if significance_met else '❌'} ({significant_tests}/{len(reports)})")
    if significance_met:
        criteria_met += 1
    
    # Criterion 3: Effect size > 0.5 (medium effect)
    avg_effect_size = sum(r.statistical_summary["overall"].effect_size for r in reports) / len(reports)
    effect_size_met = avg_effect_size > 0.5
    print(f"  3. Average effect size > 0.5: {'✅' if effect_size_met else '❌'} ({avg_effect_size:.3f})")
    if effect_size_met:
        criteria_met += 1
    
    # Criterion 4: No degradation in any scenario
    worst_performance = min(r.statistical_summary["overall"].improvement_percentage for r in reports)
    no_degradation_met = worst_performance >= -5  # Allow up to 5% degradation
    print(f"  4. No significant degradation: {'✅' if no_degradation_met else '❌'} (worst: {worst_performance:.1f}%)")
    if no_degradation_met:
        criteria_met += 1
    
    # Criterion 5: Response time not significantly worse
    avg_response_time_improvement = sum(
        r.detailed_analysis["performance_metrics"]["response_time_improvement"] for r in reports
    ) / len(reports)
    response_time_met = avg_response_time_improvement >= -10  # Allow up to 10% slower
    print(f"  5. Response time not degraded: {'✅' if response_time_met else '❌'} ({avg_response_time_improvement:.1f}%)")
    if response_time_met:
        criteria_met += 1
    
    # Overall validation
    validation_passed = criteria_met >= 4  # Require 4 out of 5 criteria
    pass_rate = (criteria_met / total_criteria) * 100
    
    print(f"\n📋 VALIDATION SCORE: {criteria_met}/{total_criteria} criteria met ({pass_rate:.0f}%)")
    
    return validation_passed


def run_quick_validation():
    """Run a quick validation test with smaller sample sizes."""
    print("⚡ Quick Meta-Prompting Validation (Reduced Sample Size)")
    print("=" * 55)
    
    output_dir = project_root / "tests" / "results" / "ab_testing"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    ab_framework = ABTestingFramework(output_dir)
    
    quick_config = ab_framework.create_test_configuration(
        test_name="quick_validation_test",
        description="Quick validation with reduced sample size for testing purposes",
        sample_size=10,
        scenarios=[
            TestScenarioType.SIMPLE_TASK,
            TestScenarioType.COMPLEX_REASONING,
            TestScenarioType.CODE_GENERATION
        ]
    )
    
    report = ab_framework.run_ab_test(quick_config)
    print_test_summary(report, "Quick Validation")
    
    return 0


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(description="Run A/B test validation for meta-prompting framework")
    parser.add_argument(
        "--mode", 
        choices=["comprehensive", "quick"], 
        default="comprehensive",
        help="Validation mode: comprehensive (full testing) or quick (reduced sample size)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_root / "tests" / "results" / "ab_testing",
        help="Output directory for test results"
    )
    
    args = parser.parse_args()
    
    try:
        if args.mode == "comprehensive":
            return run_comprehensive_validation()
        else:
            return run_quick_validation()
    
    except KeyboardInterrupt:
        print("\n⚠️  Test interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Error during validation: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())