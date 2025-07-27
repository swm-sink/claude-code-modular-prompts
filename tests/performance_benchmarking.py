#!/usr/bin/env python3
"""
Component Stack Performance Benchmarking

Integration Testing Agent Beta - Performance Validation
Mission: Measure and validate component loading performance against targets (25-70ms per stack)

This module provides detailed performance benchmarking including:
- Stack loading time measurement with statistical analysis
- Memory usage tracking and optimization analysis
- Cache effectiveness testing
- Performance regression detection
- Optimization recommendations based on metrics
"""

import time
import json
import statistics
import psutil
import gc
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import concurrent.futures
import threading


@dataclass
class PerformanceMetrics:
    """Performance metrics for component loading"""
    min_time_ms: float
    max_time_ms: float
    mean_time_ms: float
    median_time_ms: float
    std_dev_ms: float
    percentile_95_ms: float
    percentile_99_ms: float
    samples: int


@dataclass
class MemoryMetrics:
    """Memory usage metrics"""
    baseline_mb: float
    peak_mb: float
    final_mb: float
    net_increase_mb: float
    gc_collections: int


@dataclass
class StackBenchmarkResult:
    """Comprehensive benchmark result for a component stack"""
    stack_name: str
    components: List[str]
    performance_metrics: PerformanceMetrics
    memory_metrics: MemoryMetrics
    cache_hit_rate: float
    meets_target: bool
    target_min_ms: float
    target_max_ms: float
    optimization_score: float
    recommendations: List[str]


class PerformanceBenchmarker:
    """Performance benchmarker for component stacks"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.components_path = self.base_path / ".claude" / "components"
        self.stacks = {
            "orchestration": ["orchestration/dag-orchestrator.md", "orchestration/task-execution.md", "orchestration/progress-tracking.md"],
            "validation": ["validation/validation-framework.md"],
            "context": ["context/hierarchical-loading.md", "context/context-optimization.md", "context/adaptive-thinking.md"],
            "intelligence": ["intelligence/multi-agent-coordination.md", "reasoning/pattern-extraction.md", "intelligence/cognitive-architecture.md"]
        }
        
        # Performance targets
        self.target_min_ms = 25
        self.target_max_ms = 70
        self.memory_limit_mb = 50
        
        # Cache for performance testing
        self.component_cache = {}
        self.cache_hits = 0
        self.cache_misses = 0
        
        # Results storage
        self.benchmark_results = {}
    
    def benchmark_stack_loading(self, stack_name: str, iterations: int = 100) -> StackBenchmarkResult:
        """Benchmark loading performance for a specific stack"""
        print(f"🏃 Benchmarking {stack_name} stack ({iterations} iterations)...")
        
        components = self.stacks[stack_name]
        load_times = []
        
        # Reset cache statistics
        self.cache_hits = 0
        self.cache_misses = 0
        
        # Measure baseline memory
        gc.collect()
        baseline_memory = psutil.Process().memory_info().rss / 1024 / 1024
        peak_memory = baseline_memory
        
        # Benchmark loading iterations
        for i in range(iterations):
            if i % 20 == 0:
                print(f"  Progress: {i}/{iterations}")
            
            start_time = time.perf_counter()
            current_memory = psutil.Process().memory_info().rss / 1024 / 1024
            
            # Load all components in the stack
            for component_path in components:
                self._load_component_with_cache(component_path)
            
            end_time = time.perf_counter()
            load_time_ms = (end_time - start_time) * 1000
            load_times.append(load_time_ms)
            
            # Track peak memory
            end_memory = psutil.Process().memory_info().rss / 1024 / 1024
            peak_memory = max(peak_memory, end_memory)
            
            # Periodically clean cache to simulate real conditions
            if i % 25 == 0:
                self._partial_cache_cleanup()
        
        # Final memory measurement
        final_memory = psutil.Process().memory_info().rss / 1024 / 1024
        
        # Calculate performance metrics
        performance_metrics = PerformanceMetrics(
            min_time_ms=min(load_times),
            max_time_ms=max(load_times),
            mean_time_ms=statistics.mean(load_times),
            median_time_ms=statistics.median(load_times),
            std_dev_ms=statistics.stdev(load_times) if len(load_times) > 1 else 0,
            percentile_95_ms=self._percentile(load_times, 95),
            percentile_99_ms=self._percentile(load_times, 99),
            samples=len(load_times)
        )
        
        # Calculate memory metrics
        memory_metrics = MemoryMetrics(
            baseline_mb=baseline_memory,
            peak_mb=peak_memory,
            final_mb=final_memory,
            net_increase_mb=final_memory - baseline_memory,
            gc_collections=gc.get_count()[0]
        )
        
        # Calculate cache hit rate
        total_requests = self.cache_hits + self.cache_misses
        cache_hit_rate = self.cache_hits / total_requests if total_requests > 0 else 0
        
        # Check if meets performance targets
        meets_target = (
            performance_metrics.median_time_ms >= self.target_min_ms and
            performance_metrics.percentile_95_ms <= self.target_max_ms and
            memory_metrics.net_increase_mb <= self.memory_limit_mb
        )
        
        # Calculate optimization score
        optimization_score = self._calculate_optimization_score(performance_metrics, memory_metrics, cache_hit_rate)
        
        # Generate recommendations
        recommendations = self._generate_performance_recommendations(performance_metrics, memory_metrics, cache_hit_rate)
        
        result = StackBenchmarkResult(
            stack_name=stack_name,
            components=components,
            performance_metrics=performance_metrics,
            memory_metrics=memory_metrics,
            cache_hit_rate=cache_hit_rate,
            meets_target=meets_target,
            target_min_ms=self.target_min_ms,
            target_max_ms=self.target_max_ms,
            optimization_score=optimization_score,
            recommendations=recommendations
        )
        
        self.benchmark_results[stack_name] = result
        return result
    
    def _load_component_with_cache(self, component_path: str) -> str:
        """Load component with caching for performance testing"""
        if component_path in self.component_cache:
            self.cache_hits += 1
            return self.component_cache[component_path]
        
        self.cache_misses += 1
        full_path = self.components_path / component_path
        
        if not full_path.exists():
            return ""
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simulate processing overhead
        _ = len(content.split())  # Word count
        _ = content.count('<')    # Tag count
        
        self.component_cache[component_path] = content
        return content
    
    def _partial_cache_cleanup(self):
        """Partially clean cache to simulate real conditions"""
        if len(self.component_cache) > 5:
            # Remove oldest entries (simulate LRU)
            items = list(self.component_cache.items())
            to_remove = items[:2]  # Remove 2 oldest
            for key, _ in to_remove:
                del self.component_cache[key]
    
    def _percentile(self, data: List[float], percentile: float) -> float:
        """Calculate percentile of data"""
        if not data:
            return 0
        sorted_data = sorted(data)
        index = (percentile / 100) * (len(sorted_data) - 1)
        lower = int(index)
        upper = min(lower + 1, len(sorted_data) - 1)
        weight = index - lower
        return sorted_data[lower] * (1 - weight) + sorted_data[upper] * weight
    
    def _calculate_optimization_score(self, perf: PerformanceMetrics, mem: MemoryMetrics, cache_rate: float) -> float:
        """Calculate optimization score (0-100)"""
        score = 100
        
        # Performance score (40% weight)
        if perf.median_time_ms > self.target_max_ms:
            score -= 20
        elif perf.median_time_ms < self.target_min_ms:
            score -= 5  # Too fast might indicate insufficient processing
        
        if perf.percentile_95_ms > self.target_max_ms * 1.5:
            score -= 10
        
        # Memory score (30% weight)
        if mem.net_increase_mb > self.memory_limit_mb:
            score -= 15
        elif mem.net_increase_mb > self.memory_limit_mb * 0.8:
            score -= 10
        
        # Cache effectiveness (20% weight)
        if cache_rate < 0.5:
            score -= 10
        elif cache_rate < 0.7:
            score -= 5
        
        # Consistency score (10% weight)
        cv = perf.std_dev_ms / perf.mean_time_ms if perf.mean_time_ms > 0 else 0
        if cv > 0.3:  # High coefficient of variation
            score -= 5
        
        return max(score, 0)
    
    def _generate_performance_recommendations(self, perf: PerformanceMetrics, mem: MemoryMetrics, cache_rate: float) -> List[str]:
        """Generate performance optimization recommendations"""
        recommendations = []
        
        # Performance recommendations
        if perf.median_time_ms > self.target_max_ms:
            recommendations.append("Optimize component loading - exceeds target performance")
        
        if perf.percentile_95_ms > self.target_max_ms * 2:
            recommendations.append("Investigate performance outliers - high tail latency")
        
        if perf.std_dev_ms > perf.mean_time_ms * 0.3:
            recommendations.append("Improve performance consistency - high variance detected")
        
        # Memory recommendations
        if mem.net_increase_mb > self.memory_limit_mb:
            recommendations.append("Reduce memory usage - exceeds limit")
        
        if mem.net_increase_mb > self.memory_limit_mb * 0.8:
            recommendations.append("Monitor memory usage - approaching limit")
        
        # Cache recommendations
        if cache_rate < 0.5:
            recommendations.append("Improve caching strategy - low cache hit rate")
        
        if cache_rate < 0.7:
            recommendations.append("Optimize cache policy - moderate cache hit rate")
        
        # Positive recommendations
        if not recommendations:
            if perf.median_time_ms <= self.target_max_ms and mem.net_increase_mb <= self.memory_limit_mb:
                recommendations.append("Performance meets targets - consider advanced optimizations")
        
        return recommendations
    
    def benchmark_parallel_loading(self, stack_name: str, max_workers: int = 4) -> Dict[str, Any]:
        """Benchmark parallel component loading"""
        print(f"⚡ Benchmarking parallel loading for {stack_name} stack...")
        
        components = self.stacks[stack_name]
        
        # Sequential loading benchmark
        start_time = time.perf_counter()
        for component_path in components:
            self._load_component_with_cache(component_path)
        sequential_time = (time.perf_counter() - start_time) * 1000
        
        # Parallel loading benchmark
        start_time = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(self._load_component_with_cache, comp) for comp in components]
            concurrent.futures.wait(futures)
        parallel_time = (time.perf_counter() - start_time) * 1000
        
        speedup = sequential_time / parallel_time if parallel_time > 0 else 1
        efficiency = speedup / max_workers
        
        return {
            "sequential_time_ms": sequential_time,
            "parallel_time_ms": parallel_time,
            "speedup": speedup,
            "efficiency": efficiency,
            "recommended": speedup > 1.2
        }
    
    def run_comprehensive_benchmarks(self, iterations: int = 100) -> Dict[str, Any]:
        """Run comprehensive benchmarks for all stacks"""
        print("🏁 Running Comprehensive Performance Benchmarks")
        print("=" * 80)
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "benchmark_config": {
                "iterations": iterations,
                "target_min_ms": self.target_min_ms,
                "target_max_ms": self.target_max_ms,
                "memory_limit_mb": self.memory_limit_mb
            },
            "stack_results": {},
            "parallel_analysis": {},
            "overall_analysis": {}
        }
        
        # Benchmark each stack
        for stack_name in self.stacks.keys():
            result = self.benchmark_stack_loading(stack_name, iterations)
            results["stack_results"][stack_name] = {
                "performance": {
                    "min_ms": result.performance_metrics.min_time_ms,
                    "max_ms": result.performance_metrics.max_time_ms,
                    "mean_ms": result.performance_metrics.mean_time_ms,
                    "median_ms": result.performance_metrics.median_time_ms,
                    "std_dev_ms": result.performance_metrics.std_dev_ms,
                    "p95_ms": result.performance_metrics.percentile_95_ms,
                    "p99_ms": result.performance_metrics.percentile_99_ms
                },
                "memory": {
                    "baseline_mb": result.memory_metrics.baseline_mb,
                    "peak_mb": result.memory_metrics.peak_mb,
                    "net_increase_mb": result.memory_metrics.net_increase_mb
                },
                "cache_hit_rate": result.cache_hit_rate,
                "meets_target": result.meets_target,
                "optimization_score": result.optimization_score,
                "recommendations": result.recommendations
            }
            
            # Test parallel loading
            parallel_result = self.benchmark_parallel_loading(stack_name)
            results["parallel_analysis"][stack_name] = parallel_result
        
        # Overall analysis
        all_medians = [res.performance_metrics.median_time_ms for res in self.benchmark_results.values()]
        all_memory = [res.memory_metrics.net_increase_mb for res in self.benchmark_results.values()]
        
        results["overall_analysis"] = {
            "avg_median_time_ms": statistics.mean(all_medians),
            "total_memory_mb": sum(all_memory),
            "stacks_meeting_targets": sum(1 for res in self.benchmark_results.values() if res.meets_target),
            "avg_optimization_score": statistics.mean([res.optimization_score for res in self.benchmark_results.values()]),
            "performance_rating": self._get_overall_performance_rating()
        }
        
        return results
    
    def _get_overall_performance_rating(self) -> str:
        """Get overall performance rating"""
        avg_score = statistics.mean([res.optimization_score for res in self.benchmark_results.values()])
        meeting_targets = sum(1 for res in self.benchmark_results.values() if res.meets_target)
        total_stacks = len(self.benchmark_results)
        
        if avg_score >= 90 and meeting_targets == total_stacks:
            return "Excellent"
        elif avg_score >= 75 and meeting_targets >= total_stacks * 0.75:
            return "Good"
        elif avg_score >= 60:
            return "Fair"
        else:
            return "Needs Improvement"
    
    def save_benchmark_results(self, output_path: str):
        """Save comprehensive benchmark results"""
        results = self.run_comprehensive_benchmarks()
        
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"📊 Benchmark results saved to: {output_path}")
        
        # Generate performance report
        report_path = output_path.replace('.json', '_report.md')
        self._generate_performance_report(results, report_path)
    
    def _generate_performance_report(self, results: Dict[str, Any], output_path: str):
        """Generate detailed performance report"""
        report = f"""# Component Stack Performance Benchmark Report

**Generated:** {results['timestamp']}
**Testing Agent:** Integration Testing Agent Beta
**Benchmark Type:** Component Stack Performance Validation

## Configuration

- **Iterations:** {results['benchmark_config']['iterations']}
- **Target Range:** {results['benchmark_config']['target_min_ms']}-{results['benchmark_config']['target_max_ms']}ms
- **Memory Limit:** {results['benchmark_config']['memory_limit_mb']}MB

## Executive Summary

- **Overall Performance Rating:** {results['overall_analysis']['performance_rating']}
- **Average Load Time:** {results['overall_analysis']['avg_median_time_ms']:.1f}ms
- **Total Memory Usage:** {results['overall_analysis']['total_memory_mb']:.1f}MB
- **Stacks Meeting Targets:** {results['overall_analysis']['stacks_meeting_targets']}/{len(results['stack_results'])}
- **Average Optimization Score:** {results['overall_analysis']['avg_optimization_score']:.1f}/100

## Stack Performance Details

"""
        
        for stack_name, stack_data in results['stack_results'].items():
            perf = stack_data['performance']
            mem = stack_data['memory']
            status = "✅ PASS" if stack_data['meets_target'] else "⚠️ REVIEW"
            
            report += f"""
### {status} {stack_name.title()} Stack

**Performance Metrics:**
- Median Load Time: {perf['median_ms']:.1f}ms
- 95th Percentile: {perf['p95_ms']:.1f}ms
- Standard Deviation: {perf['std_dev_ms']:.1f}ms
- Range: {perf['min_ms']:.1f}ms - {perf['max_ms']:.1f}ms

**Memory Metrics:**
- Net Memory Increase: {mem['net_increase_mb']:.1f}MB
- Peak Memory: {mem['peak_mb']:.1f}MB

**Cache Performance:**
- Cache Hit Rate: {stack_data['cache_hit_rate']:.1%}

**Optimization Score:** {stack_data['optimization_score']:.0f}/100

"""
            
            if stack_data['recommendations']:
                report += "**Recommendations:**\\n"
                for rec in stack_data['recommendations']:
                    report += f"- {rec}\\n"
        
        report += f"""
## Parallel Loading Analysis

"""
        
        for stack_name, parallel_data in results['parallel_analysis'].items():
            speedup = parallel_data['speedup']
            efficiency = parallel_data['efficiency']
            recommended = "✅ Recommended" if parallel_data['recommended'] else "❌ Not Beneficial"
            
            report += f"""
### {stack_name.title()} Stack Parallelization

- **Sequential Time:** {parallel_data['sequential_time_ms']:.1f}ms
- **Parallel Time:** {parallel_data['parallel_time_ms']:.1f}ms
- **Speedup:** {speedup:.2f}x
- **Efficiency:** {efficiency:.2f}
- **Recommendation:** {recommended}

"""
        
        report += f"""
## Performance Target Analysis

| Stack | Median Time | Target Met | Optimization Score |
|-------|-------------|------------|-------------------|
"""
        
        for stack_name, stack_data in results['stack_results'].items():
            median = stack_data['performance']['median_ms']
            target_met = "✅" if stack_data['meets_target'] else "❌"
            score = stack_data['optimization_score']
            report += f"| {stack_name.title()} | {median:.1f}ms | {target_met} | {score:.0f}/100 |\\n"
        
        report += f"""
## Optimization Recommendations

Based on the benchmark results, here are the top optimization priorities:

"""
        
        # Collect all recommendations and prioritize
        all_recommendations = []
        for stack_data in results['stack_results'].values():
            all_recommendations.extend(stack_data['recommendations'])
        
        # Count frequency and prioritize
        rec_counts = {}
        for rec in all_recommendations:
            rec_counts[rec] = rec_counts.get(rec, 0) + 1
        
        sorted_recs = sorted(rec_counts.items(), key=lambda x: x[1], reverse=True)
        
        for i, (rec, count) in enumerate(sorted_recs[:5], 1):
            report += f"{i}. {rec} (affects {count} stack{'s' if count > 1 else ''})\\n"
        
        report += f"""
---
*Generated by Integration Testing Agent Beta - Component Stack Performance Benchmarking*
*Benchmark includes load time analysis, memory usage tracking, cache performance, and optimization recommendations*
"""
        
        with open(output_path, 'w') as f:
            f.write(report)
        
        print(f"📋 Performance report saved to: {output_path}")


def main():
    """Main execution function for performance benchmarking"""
    base_path = "/Users/smenssink/conductor/repo/claude-code-modular-prompts/casablanca"
    benchmarker = PerformanceBenchmarker(base_path)
    
    try:
        print("🚀 Component Stack Performance Benchmarking")
        print("=" * 80)
        
        # Run benchmarks
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{base_path}/tests/results/performance_benchmark_{timestamp}.json"
        
        benchmarker.save_benchmark_results(output_file)
        
        print("\\n" + "=" * 80)
        print("✅ Performance benchmarking completed successfully")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Performance benchmarking failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()