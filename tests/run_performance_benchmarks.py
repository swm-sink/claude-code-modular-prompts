#!/usr/bin/env python3
"""Performance Benchmark Runner for Meta-Prompting Framework Optimization.

This script demonstrates and validates the performance benchmarking tools
by running comprehensive performance analysis to identify optimization
opportunities in the meta-prompting framework.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.framework.performance_benchmarking_tools import (
    PerformanceBenchmarkSuite,
    BenchmarkCategory,
    TokenAnalyzer
)


def run_quick_performance_validation():
    """Run quick performance validation with core benchmarks."""
    print("⚡ Quick Performance Benchmarking Validation")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create output directory
    output_dir = project_root / "tests" / "results" / "performance"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize performance benchmark suite
    benchmark_suite = PerformanceBenchmarkSuite(project_root, output_dir)
    
    # Run token efficiency analysis
    print("🧪 Token Efficiency Analysis")
    print("-" * 30)
    
    token_analyzer = TokenAnalyzer()
    
    # Compare baseline vs enhanced prompts
    baseline_prompt = "Complete this task: Create a function"
    enhanced_prompt = """
<thinking_pattern>
<checkpoint>Understand requirements: Create a function</checkpoint>
<analysis>Break down task components and identify key requirements</analysis>
<validation>Verify understanding before proceeding</validation>
</thinking_pattern>

Using structured analysis, complete this task: Create a function

<execution_pattern>
1. Analyze requirements comprehensively
2. Plan approach with quality gates
3. Implement solution with verification
4. Validate results against requirements
</execution_pattern>
"""
    
    baseline_analysis = token_analyzer.analyze_token_efficiency(baseline_prompt)
    enhanced_analysis = token_analyzer.analyze_token_efficiency(enhanced_prompt)
    
    print(f"📊 Token Analysis Results:")
    print(f"  Baseline Prompt:")
    print(f"    Tokens: {baseline_analysis['prompt_tokens']}")
    print(f"    Structure Efficiency: {baseline_analysis['structure_efficiency_score']:.3f}")
    
    print(f"  Enhanced Prompt:")
    print(f"    Tokens: {enhanced_analysis['prompt_tokens']}")
    print(f"    Structure Efficiency: {enhanced_analysis['structure_efficiency_score']:.3f}")
    print(f"    XML Overhead: {enhanced_analysis['xml_overhead_percentage']:.1f}%")
    print(f"    Thinking Pattern Ratio: {enhanced_analysis['thinking_pattern_ratio']:.3f}")
    
    token_overhead = enhanced_analysis['prompt_tokens'] - baseline_analysis['prompt_tokens']
    efficiency_gain = enhanced_analysis['structure_efficiency_score'] - baseline_analysis['structure_efficiency_score']
    
    print(f"\n📈 Comparison:")
    print(f"  Token Overhead: +{token_overhead} tokens ({(token_overhead/baseline_analysis['prompt_tokens'])*100:.1f}%)")
    print(f"  Efficiency Gain: +{efficiency_gain:.3f} ({(efficiency_gain/baseline_analysis['structure_efficiency_score'])*100:.1f}%)")
    
    # Quick performance validation
    if efficiency_gain > 0.2 and token_overhead < 200:
        print("✅ QUICK VALIDATION PASSED")
        print("🚀 Enhanced prompts show significant efficiency improvement")
        return 0
    else:
        print("⚠️  QUICK VALIDATION NEEDS ATTENTION")
        print("🔧 Enhanced prompts may need optimization")
        return 1


def run_comprehensive_performance_benchmarks():
    """Run comprehensive performance benchmarking across all categories."""
    print("🚀 Comprehensive Performance Benchmarking")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Create output directory
    output_dir = project_root / "tests" / "results" / "performance"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize performance benchmark suite
    benchmark_suite = PerformanceBenchmarkSuite(project_root, output_dir)
    
    # Run comprehensive benchmarks
    report = benchmark_suite.run_comprehensive_benchmarks()
    
    # Additional analysis
    print("\n" + "=" * 60)
    print("🔍 COMPREHENSIVE PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    # Analyze results by category
    analyze_performance_by_category(report.benchmark_results)
    
    # Validate performance targets
    validate_performance_targets(report)
    
    # Overall validation result
    performance_metrics = report.performance_summary.get("performance_metrics", {})
    avg_time = performance_metrics.get("avg_execution_time_ms", 1000)
    p95_time = performance_metrics.get("p95_execution_time_ms", 1000)
    efficiency_score = performance_metrics.get("avg_efficiency_score", 0)
    
    validation_passed = (
        avg_time <= 100 and
        p95_time <= 200 and
        efficiency_score >= 0.7 and
        report.successful_benchmarks >= report.total_benchmarks * 0.9
    )
    
    print(f"\n🎯 OVERALL PERFORMANCE VALIDATION:")
    if validation_passed:
        print("✅ COMPREHENSIVE VALIDATION PASSED")
        print("🚀 Framework performance meets all targets")
        return 0
    else:
        print("❌ COMPREHENSIVE VALIDATION FAILED")
        print("⚠️  Framework performance needs optimization")
        print(f"   Average Time: {avg_time:.1f}ms (target: ≤100ms)")
        print(f"   P95 Time: {p95_time:.1f}ms (target: ≤200ms)")
        print(f"   Efficiency Score: {efficiency_score:.3f} (target: ≥0.7)")
        print(f"   Success Rate: {(report.successful_benchmarks/report.total_benchmarks)*100:.1f}% (target: ≥90%)")
        return 1


def analyze_performance_by_category(benchmark_results):
    """Analyze performance results broken down by benchmark category."""
    print("📈 Performance by Category:")
    
    category_analysis = {}
    
    for result in benchmark_results:
        category = result.config.category.value
        
        if category not in category_analysis:
            category_analysis[category] = {
                "total": 0,
                "successful": 0,
                "execution_times": [],
                "efficiency_scores": []
            }
        
        category_analysis[category]["total"] += 1
        
        if result.success:
            category_analysis[category]["successful"] += 1
            category_analysis[category]["execution_times"].append(result.execution_time_ms)
            category_analysis[category]["efficiency_scores"].append(result.token_efficiency_score)
    
    for category, data in category_analysis.items():
        success_rate = (data["successful"] / data["total"]) * 100 if data["total"] > 0 else 0
        avg_time = sum(data["execution_times"]) / len(data["execution_times"]) if data["execution_times"] else 0
        avg_efficiency = sum(data["efficiency_scores"]) / len(data["efficiency_scores"]) if data["efficiency_scores"] else 0
        
        print(f"  {category.replace('_', ' ').title()}:")
        print(f"    Success Rate: {success_rate:.1f}% ({data['successful']}/{data['total']})")
        print(f"    Average Time: {avg_time:.1f}ms")
        print(f"    Average Efficiency: {avg_efficiency:.3f}")
        
        # Performance assessment
        if avg_time <= 50 and avg_efficiency >= 0.8:
            print(f"    Status: ✅ Excellent performance")
        elif avg_time <= 100 and avg_efficiency >= 0.7:
            print(f"    Status: ✅ Good performance")
        elif avg_time <= 200 and avg_efficiency >= 0.6:
            print(f"    Status: ⚠️  Moderate performance")
        else:
            print(f"    Status: ❌ Needs optimization")


def validate_performance_targets(report):
    """Validate that performance targets are being met."""
    print("\n🎯 Performance Target Validation:")
    
    performance_metrics = report.performance_summary.get("performance_metrics", {})
    
    # Target 1: Average execution time ≤ 100ms
    avg_time = performance_metrics.get("avg_execution_time_ms", 0)
    avg_target_met = avg_time <= 100
    print(f"  Average Execution Time Target (≤100ms): {'✅' if avg_target_met else '❌'} {avg_time:.1f}ms")
    
    # Target 2: P95 execution time ≤ 200ms
    p95_time = performance_metrics.get("p95_execution_time_ms", 0)
    p95_target_met = p95_time <= 200
    print(f"  P95 Execution Time Target (≤200ms): {'✅' if p95_target_met else '❌'} {p95_time:.1f}ms")
    
    # Target 3: Average efficiency score ≥ 0.7
    avg_efficiency = performance_metrics.get("avg_efficiency_score", 0)
    efficiency_target_met = avg_efficiency >= 0.7
    print(f"  Efficiency Score Target (≥0.7): {'✅' if efficiency_target_met else '❌'} {avg_efficiency:.3f}")
    
    # Target 4: Success rate ≥ 90%
    success_rate = (report.successful_benchmarks / report.total_benchmarks) * 100 if report.total_benchmarks > 0 else 0
    success_target_met = success_rate >= 90
    print(f"  Success Rate Target (≥90%): {'✅' if success_target_met else '❌'} {success_rate:.1f}%")
    
    # Overall performance assessment
    targets_met = sum([avg_target_met, p95_target_met, efficiency_target_met, success_target_met])
    total_targets = 4
    
    print(f"\n📊 Performance Targets Met: {targets_met}/{total_targets} ({(targets_met/total_targets)*100:.0f}%)")
    
    if targets_met >= 3:
        print("✅ Performance targets largely met - framework optimized well")
    elif targets_met >= 2:
        print("⚠️  Some performance targets missed - optimization opportunities exist")
    else:
        print("❌ Significant performance issues - immediate optimization required")


def run_token_optimization_analysis():
    """Run detailed token optimization analysis."""
    print("📝 Token Optimization Analysis")
    print("=" * 40)
    
    token_analyzer = TokenAnalyzer()
    
    # Test different prompt structures
    prompt_variants = {
        "minimal": "Complete task X",
        "structured": """
<task>Complete task X</task>
<requirements>Meet all criteria</requirements>
""",
        "enhanced": """
<thinking_pattern>
<analysis>Understand task X requirements</analysis>
<planning>Plan approach systematically</planning>
<validation>Verify solution quality</validation>
</thinking_pattern>

Complete task X with structured analysis

<quality_gates>
- Requirement compliance
- Solution validation
- Performance optimization
</quality_gates>
""",
        "complex": """
<multi_level_analysis>
<system_level>
<context>Task X in broader system context</context>
<constraints>System limitations and requirements</constraints>
</system_level>
<component_level>
<analysis>Individual task components</analysis>
<interactions>Component interactions and dependencies</interactions>
</component_level>
<implementation_level>
<approach>Detailed implementation strategy</approach>
<validation>Comprehensive testing and validation</validation>
</implementation_level>
</multi_level_analysis>

Execute task X with comprehensive multi-level analysis

<execution_framework>
<phase_1>Requirement analysis and planning</phase_1>
<phase_2>Implementation with quality gates</phase_2>
<phase_3>Validation and optimization</phase_3>
</execution_framework>

<quality_assurance>
<criteria>Success criteria and validation methods</criteria>
<testing>Comprehensive testing strategy</testing>
<optimization>Performance and quality optimization</optimization>
</quality_assurance>
"""
    }
    
    print("📊 Token Efficiency Analysis by Prompt Structure:")
    
    optimization_insights = []
    
    for variant_name, prompt in prompt_variants.items():
        analysis = token_analyzer.analyze_token_efficiency(prompt)
        
        print(f"\n  {variant_name.title()} Prompt:")
        print(f"    Tokens: {analysis['prompt_tokens']}")
        print(f"    XML Overhead: {analysis['xml_overhead_percentage']:.1f}%")
        print(f"    Thinking Ratio: {analysis['thinking_pattern_ratio']:.3f}")
        print(f"    Structure Efficiency: {analysis['structure_efficiency_score']:.3f}")
        print(f"    Tokens per Instruction: {analysis['tokens_per_instruction']:.1f}")
        
        # Generate optimization insights
        if analysis['xml_overhead_percentage'] > 30:
            optimization_insights.append(f"⚠️ {variant_name}: High XML overhead ({analysis['xml_overhead_percentage']:.1f}%) - consider simplifying structure")
        
        if analysis['structure_efficiency_score'] < 0.5:
            optimization_insights.append(f"🔧 {variant_name}: Low structure efficiency ({analysis['structure_efficiency_score']:.3f}) - improve organization")
        
        if analysis['tokens_per_instruction'] > 50:
            optimization_insights.append(f"📝 {variant_name}: High tokens per instruction ({analysis['tokens_per_instruction']:.1f}) - consider more concise language")
    
    print(f"\n💡 Optimization Insights:")
    if optimization_insights:
        for i, insight in enumerate(optimization_insights, 1):
            print(f"  {i}. {insight}")
    else:
        print("  ✅ All prompt structures show good token efficiency")
    
    # Optimal structure recommendation
    print(f"\n🎯 Recommendation:")
    print("  For most use cases, 'enhanced' structure provides optimal balance of:")
    print("  - Clear thinking patterns for improved accuracy")
    print("  - Reasonable token overhead (15-25%)")
    print("  - Good structure efficiency (≥0.7)")
    print("  - Maintainable XML hierarchy")
    
    return 0


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(description="Run performance benchmarks for meta-prompting framework")
    parser.add_argument(
        "--mode",
        choices=["quick", "comprehensive", "token-analysis"],
        default="quick",
        help="Benchmark mode: quick (core metrics), comprehensive (all benchmarks), or token-analysis (optimization analysis)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_root / "tests" / "results" / "performance",
        help="Output directory for benchmark results"
    )
    
    args = parser.parse_args()
    
    try:
        if args.mode == "comprehensive":
            return run_comprehensive_performance_benchmarks()
        elif args.mode == "token-analysis":
            return run_token_optimization_analysis()
        else:
            return run_quick_performance_validation()
    
    except KeyboardInterrupt:
        print("\n⚠️  Benchmark interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Error during benchmarking: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())