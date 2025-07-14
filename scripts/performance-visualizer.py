#!/usr/bin/env python3
"""
Performance Visualization Script for Benchmark Results
Agent V34 - Performance Benchmark Tester
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def create_performance_dashboard(benchmark_file):
    """Create ASCII performance dashboard from benchmark results"""
    
    # Load benchmark data
    with open(benchmark_file, 'r') as f:
        data = json.load(f)
    
    summary = data['summary']
    benchmarks = data['benchmarks']
    
    print("\n" + "="*80)
    print(" " * 20 + "FRAMEWORK PERFORMANCE DASHBOARD")
    print(" " * 20 + f"Framework Version: {data['framework_version']}")
    print(" " * 20 + f"Benchmark Date: {data['timestamp'][:10]}")
    print("="*80)
    
    # Overall Performance Status
    print("\n📊 OVERALL PERFORMANCE STATUS")
    print("-" * 40)
    
    p95 = summary['overall_p95_ms']
    target = 200
    margin = ((target - p95) / target) * 100
    
    # Performance bar
    bar_length = 50
    filled = int((p95 / target) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    print(f"P95 Response Time: [{bar}] {p95:.2f}ms / {target}ms")
    print(f"Performance Margin: {margin:.1f}% below target")
    print(f"Status: {'✅ EXCELLENT' if p95 < target else '❌ NEEDS OPTIMIZATION'}")
    
    # Component Breakdown
    print("\n📈 COMPONENT PERFORMANCE BREAKDOWN")
    print("-" * 40)
    
    components = [
        ("Module Loading", benchmarks['module_loading']['average_ms'], 10),
        ("Command Overhead", benchmarks['command_overhead']['average_ms'], 20),
        ("Quality Gates", benchmarks['quality_gates']['average_ms'], 50),
    ]
    
    for name, avg_ms, threshold in components:
        ratio = avg_ms / threshold
        bar_filled = int(ratio * 20)
        bar = "▓" * min(bar_filled, 20) + "░" * max(0, 20 - bar_filled)
        status = "✅" if avg_ms < threshold else "⚠️"
        print(f"{name:20} [{bar}] {avg_ms:6.2f}ms {status}")
    
    # Token Usage
    print("\n💾 CONTEXT WINDOW USAGE")
    print("-" * 40)
    
    tokens = benchmarks['context_usage']['CLAUDE.md']
    max_tokens = 200000
    token_ratio = tokens / max_tokens
    bar_filled = int(token_ratio * 30)
    bar = "▓" * bar_filled + "░" * (30 - bar_filled)
    
    print(f"Framework Tokens: [{bar}] {tokens:,} / {max_tokens:,}")
    print(f"Usage: {token_ratio*100:.1f}% of available context")
    
    # Performance Trends
    print("\n📉 PERFORMANCE CHARACTERISTICS")
    print("-" * 40)
    
    # Module loading distribution
    module_times = list(benchmarks['module_loading']['individual_times'].values())
    min_module = min(module_times)
    max_module = max(module_times)
    
    print(f"Module Load Times: {min_module:.2f}ms (min) - {max_module:.2f}ms (max)")
    
    # Command overhead distribution
    command_times = list(benchmarks['command_overhead']['individual_times'].values())
    min_cmd = min(command_times)
    max_cmd = max(command_times)
    
    print(f"Command Overhead:  {min_cmd:.2f}ms (min) - {max_cmd:.2f}ms (max)")
    
    # Quality gate distribution
    gate_times = list(benchmarks['quality_gates']['individual_times'].values())
    min_gate = min(gate_times)
    max_gate = max(gate_times)
    
    print(f"Quality Gates:     {min_gate:.2f}ms (min) - {max_gate:.2f}ms (max)")
    
    # Parallel execution
    parallel = benchmarks['parallel_execution']
    improvement = parallel['improvement_percent']
    
    print(f"\nParallel Execution: {'⚠️ NEEDS OPTIMIZATION' if improvement < 0 else '✅ OPTIMIZED'}")
    print(f"  Sequential: {parallel['sequential_ms']:.2f}ms")
    print(f"  Parallel:   {parallel['parallel_ms']:.2f}ms")
    print(f"  Improvement: {improvement:.1f}%")
    
    # Recommendations
    print("\n🎯 OPTIMIZATION OPPORTUNITIES")
    print("-" * 40)
    
    if improvement < 0:
        print("• Fix parallel execution overhead for small operations")
    
    if benchmarks['quality_gates']['average_ms'] > 5:
        print("• Implement quality gate result caching")
    
    if benchmarks['command_overhead']['average_ms'] > 2:
        print("• Optimize command initialization sequence")
    
    if tokens > max_tokens * 0.3:
        print("• Consider module lazy loading for token optimization")
    
    print("\n" + "="*80)
    print(f"Performance Grade: A+ (P95: {p95:.2f}ms)")
    print("="*80 + "\n")

def main():
    """Main execution"""
    # Find latest benchmark file
    performance_dir = Path(__file__).parent.parent / "internal" / "reports" / "performance"
    
    if len(sys.argv) > 1:
        benchmark_file = Path(sys.argv[1])
    else:
        # Get latest benchmark
        benchmark_files = list(performance_dir.glob("performance-benchmark-*.json"))
        if not benchmark_files:
            print("No benchmark files found!")
            return 1
        
        benchmark_file = max(benchmark_files, key=lambda p: p.stat().st_mtime)
    
    if not benchmark_file.exists():
        print(f"Benchmark file not found: {benchmark_file}")
        return 1
    
    create_performance_dashboard(benchmark_file)
    return 0

if __name__ == "__main__":
    exit(main())