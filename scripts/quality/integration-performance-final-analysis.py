#!/usr/bin/env python3
"""
Integration Performance Final Analysis
Comprehensive memory usage analysis and load testing for all integration patterns.

Focus: Memory efficiency, load scaling, performance under stress
"""

import os
import sys
import time
import psutil
import json
import threading
import concurrent.futures
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
from datetime import datetime
import statistics

@dataclass
class MemoryProfile:
    """Memory usage profiling data"""
    test_name: str
    baseline_memory_mb: float
    peak_memory_mb: float
    memory_growth_mb: float
    memory_efficiency_score: float
    garbage_collection_impact: float

@dataclass
class LoadTestResult:
    """Load testing performance result"""
    concurrent_operations: int
    avg_response_time_ms: float
    max_response_time_ms: float
    min_response_time_ms: float
    throughput_ops_per_second: float
    error_rate_percent: float
    memory_pressure_mb: float

@dataclass
class IntegrationPerformanceSummary:
    """Complete integration performance analysis"""
    test_type: str
    total_tests: int
    memory_profiles: List[MemoryProfile]
    load_test_results: List[LoadTestResult]
    scaling_analysis: Dict
    optimization_recommendations: List[str]

class IntegrationPerformanceAnalyzer:
    """Final comprehensive performance analysis framework"""
    
    def __init__(self, commands_dir: str, components_dir: str):
        self.commands_dir = Path(commands_dir)
        self.components_dir = Path(components_dir)
        self.baseline_memory = None
        
        # Test configurations
        self.load_test_configs = [1, 2, 4, 8, 16, 32]  # Concurrent operations
        self.memory_stress_configs = [10, 50, 100, 200, 500]  # Operations per test

    def establish_memory_baseline(self) -> float:
        """Establish baseline memory usage"""
        process = psutil.Process()
        
        # Clear any existing memory usage
        import gc
        gc.collect()
        time.sleep(1)
        
        baseline_readings = []
        for _ in range(5):
            reading = process.memory_info().rss / 1024 / 1024
            baseline_readings.append(reading)
            time.sleep(0.2)
        
        self.baseline_memory = statistics.mean(baseline_readings)
        return self.baseline_memory

    def simulate_file_operation(self, file_path: Path, operation_type: str) -> Tuple[float, float]:
        """Simulate file operation and measure memory impact"""
        process = psutil.Process()
        memory_before = process.memory_info().rss / 1024 / 1024
        
        start_time = time.perf_counter()
        
        try:
            if operation_type == 'read':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Simulate processing
                processed_content = content.upper()
                del processed_content
                
            elif operation_type == 'analyze':
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Simulate complex analysis
                import re
                analysis = {
                    'lines': len(content.split('\n')),
                    'words': len(content.split()),
                    'imports': len(re.findall(r'@import|@include', content)),
                    'tools': len(re.findall(r'tools:', content)),
                    'complexity': len(content) / 1000
                }
                del analysis
                
            elif operation_type == 'load_component_stack':
                # Simulate loading multiple related files
                related_files = list(file_path.parent.glob('*.md'))[:5]
                loaded_content = []
                for related_file in related_files:
                    if related_file.exists():
                        with open(related_file, 'r', encoding='utf-8') as f:
                            loaded_content.append(f.read())
                del loaded_content
                
        except Exception as e:
            print(f"Error in file operation {operation_type} on {file_path}: {e}")
        
        end_time = time.perf_counter()
        memory_after = process.memory_info().rss / 1024 / 1024
        
        execution_time_ms = (end_time - start_time) * 1000
        memory_impact_mb = memory_after - memory_before
        
        return execution_time_ms, memory_impact_mb

    def profile_memory_usage(self) -> List[MemoryProfile]:
        """Profile memory usage across different operations"""
        print("🧠 Memory Usage Profiling...")
        
        baseline = self.establish_memory_baseline()
        memory_profiles = []
        
        # Test categories
        test_cases = [
            ('command_loading', 'read', list(self.commands_dir.glob('**/*.md'))[:10]),
            ('component_loading', 'analyze', list(self.components_dir.glob('**/*.md'))[:10]),
            ('stack_loading', 'load_component_stack', list(self.components_dir.glob('**/*.md'))[:5]),
        ]
        
        for test_name, operation_type, file_list in test_cases:
            print(f"  📊 Profiling {test_name}...")
            
            # Filter out deprecated files
            active_files = [f for f in file_list if 'deprecated' not in str(f)][:5]
            
            memory_readings = []
            execution_times = []
            
            for file_path in active_files:
                # Force garbage collection before test
                import gc
                gc.collect()
                
                pre_test_memory = psutil.Process().memory_info().rss / 1024 / 1024
                
                exec_time, memory_impact = self.simulate_file_operation(file_path, operation_type)
                execution_times.append(exec_time)
                
                post_test_memory = psutil.Process().memory_info().rss / 1024 / 1024
                memory_readings.append(post_test_memory - pre_test_memory)
                
                # Brief pause between operations
                time.sleep(0.1)
            
            if memory_readings:
                peak_memory = max(memory_readings)
                avg_memory_growth = statistics.mean(memory_readings)
                memory_efficiency = 100 / (1 + avg_memory_growth)  # Higher efficiency for lower memory usage
                
                # Estimate garbage collection impact
                gc_impact = peak_memory - avg_memory_growth
                
                profile = MemoryProfile(
                    test_name=test_name,
                    baseline_memory_mb=baseline,
                    peak_memory_mb=baseline + peak_memory,
                    memory_growth_mb=avg_memory_growth,
                    memory_efficiency_score=memory_efficiency,
                    garbage_collection_impact=gc_impact
                )
                
                memory_profiles.append(profile)
                
                print(f"    ✓ {test_name}: {avg_memory_growth:.1f}MB avg growth, "
                      f"{memory_efficiency:.1f} efficiency score")
        
        return memory_profiles

    def execute_load_test(self, file_list: List[Path], concurrent_ops: int) -> LoadTestResult:
        """Execute load test with specified concurrency"""
        print(f"    🔄 Testing {concurrent_ops} concurrent operations...")
        
        response_times = []
        errors = 0
        
        def worker_task(file_path: Path) -> float:
            """Worker task for concurrent execution"""
            try:
                start_time = time.perf_counter()
                
                # Simulate realistic operation
                exec_time, memory_impact = self.simulate_file_operation(file_path, 'analyze')
                
                end_time = time.perf_counter()
                return (end_time - start_time) * 1000
                
            except Exception as e:
                print(f"Worker error: {e}")
                return -1  # Error indicator
        
        # Monitor memory during load test
        process = psutil.Process()
        memory_before = process.memory_info().rss / 1024 / 1024
        
        start_time = time.perf_counter()
        
        # Execute concurrent operations
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_ops) as executor:
            # Create task list (cycle through files if needed)
            tasks = []
            for i in range(concurrent_ops):
                file_index = i % len(file_list)
                tasks.append(executor.submit(worker_task, file_list[file_index]))
            
            # Collect results
            for future in concurrent.futures.as_completed(tasks):
                result = future.result()
                if result > 0:
                    response_times.append(result)
                else:
                    errors += 1
        
        end_time = time.perf_counter()
        memory_after = process.memory_info().rss / 1024 / 1024
        
        # Calculate metrics
        total_time = end_time - start_time
        throughput = concurrent_ops / total_time if total_time > 0 else 0
        error_rate = (errors / concurrent_ops) * 100 if concurrent_ops > 0 else 0
        memory_pressure = memory_after - memory_before
        
        if response_times:
            avg_response_time = statistics.mean(response_times)
            max_response_time = max(response_times)
            min_response_time = min(response_times)
        else:
            avg_response_time = max_response_time = min_response_time = 0
        
        return LoadTestResult(
            concurrent_operations=concurrent_ops,
            avg_response_time_ms=avg_response_time,
            max_response_time_ms=max_response_time,
            min_response_time_ms=min_response_time,
            throughput_ops_per_second=throughput,
            error_rate_percent=error_rate,
            memory_pressure_mb=memory_pressure
        )

    def run_load_testing(self) -> List[LoadTestResult]:
        """Execute comprehensive load testing"""
        print("\n⚡ Load Testing Performance...")
        
        # Prepare test files
        command_files = list(self.commands_dir.glob('**/*.md'))
        active_commands = [f for f in command_files if 'deprecated' not in str(f)][:10]
        
        if not active_commands:
            print("  ⚠️ No active command files found for load testing")
            return []
        
        load_results = []
        
        for concurrent_ops in self.load_test_configs:
            try:
                # Force garbage collection before each test
                import gc
                gc.collect()
                time.sleep(0.5)
                
                result = self.execute_load_test(active_commands, concurrent_ops)
                load_results.append(result)
                
                print(f"      ✓ {concurrent_ops} ops: {result.avg_response_time_ms:.1f}ms avg, "
                      f"{result.throughput_ops_per_second:.1f} ops/s, "
                      f"{result.error_rate_percent:.1f}% errors")
                
                # Brief pause between load tests
                time.sleep(1)
                
            except Exception as e:
                print(f"    ❌ Load test failed for {concurrent_ops} ops: {e}")
        
        return load_results

    def analyze_scaling_behavior(self, load_results: List[LoadTestResult]) -> Dict:
        """Analyze performance scaling patterns"""
        if not load_results:
            return {}
        
        scaling_analysis = {
            'response_time_scaling': {},
            'throughput_scaling': {},
            'memory_scaling': {},
            'error_scaling': {},
            'performance_degradation_points': []
        }
        
        # Response time scaling
        for result in load_results:
            scaling_analysis['response_time_scaling'][result.concurrent_operations] = result.avg_response_time_ms
        
        # Throughput scaling
        for result in load_results:
            scaling_analysis['throughput_scaling'][result.concurrent_operations] = result.throughput_ops_per_second
        
        # Memory scaling
        for result in load_results:
            scaling_analysis['memory_scaling'][result.concurrent_operations] = result.memory_pressure_mb
        
        # Error rate scaling
        for result in load_results:
            scaling_analysis['error_scaling'][result.concurrent_operations] = result.error_rate_percent
        
        # Identify performance degradation points
        for i, result in enumerate(load_results[1:], 1):
            prev_result = load_results[i-1]
            
            # Check for significant performance degradation
            response_time_increase = result.avg_response_time_ms / prev_result.avg_response_time_ms if prev_result.avg_response_time_ms > 0 else 1
            throughput_decrease = prev_result.throughput_ops_per_second / result.throughput_ops_per_second if result.throughput_ops_per_second > 0 else 1
            
            if response_time_increase > 1.5 or throughput_decrease > 1.3:
                scaling_analysis['performance_degradation_points'].append({
                    'concurrent_ops': result.concurrent_operations,
                    'response_time_increase': response_time_increase,
                    'throughput_decrease': throughput_decrease
                })
        
        return scaling_analysis

    def generate_optimization_recommendations(self, memory_profiles: List[MemoryProfile], 
                                            load_results: List[LoadTestResult], 
                                            scaling_analysis: Dict) -> List[str]:
        """Generate comprehensive optimization recommendations"""
        recommendations = []
        
        # Memory optimization recommendations
        high_memory_tests = [p for p in memory_profiles if p.memory_growth_mb > 5]
        if high_memory_tests:
            recommendations.append("Implement memory-efficient file loading patterns for high-memory operations")
            recommendations.append("Add garbage collection optimization points in memory-intensive workflows")
        
        low_efficiency_tests = [p for p in memory_profiles if p.memory_efficiency_score < 50]
        if low_efficiency_tests:
            recommendations.append("Optimize memory allocation patterns for low-efficiency operations")
        
        # Load testing recommendations
        if load_results:
            high_error_results = [r for r in load_results if r.error_rate_percent > 5]
            if high_error_results:
                recommendations.append("Implement better error handling and retry mechanisms for high-load scenarios")
            
            slow_response_results = [r for r in load_results if r.avg_response_time_ms > 1000]
            if slow_response_results:
                recommendations.append("Optimize response times for high-concurrency operations")
            
            high_memory_pressure = [r for r in load_results if r.memory_pressure_mb > 10]
            if high_memory_pressure:
                recommendations.append("Implement memory pooling and resource management for concurrent operations")
        
        # Scaling recommendations
        degradation_points = scaling_analysis.get('performance_degradation_points', [])
        if degradation_points:
            recommendations.append(f"Performance degrades significantly at {degradation_points[0]['concurrent_ops']} concurrent operations")
            recommendations.append("Consider implementing connection pooling and resource limiting")
        
        # General recommendations
        recommendations.append("Implement component lazy loading to reduce initial memory footprint")
        recommendations.append("Add performance monitoring and alerting for production deployments")
        recommendations.append("Consider implementing caching strategies for frequently accessed components")
        
        return recommendations

    def run_comprehensive_analysis(self) -> IntegrationPerformanceSummary:
        """Execute complete integration performance analysis"""
        print("🚀 Integration Performance Final Analysis")
        print("=" * 60)
        
        # Memory profiling
        memory_profiles = self.profile_memory_usage()
        
        # Load testing
        load_results = self.run_load_testing()
        
        # Scaling analysis
        scaling_analysis = self.analyze_scaling_behavior(load_results)
        
        # Generate recommendations
        recommendations = self.generate_optimization_recommendations(
            memory_profiles, load_results, scaling_analysis
        )
        
        total_tests = len(memory_profiles) + len(load_results)
        
        return IntegrationPerformanceSummary(
            test_type='integration_performance_final',
            total_tests=total_tests,
            memory_profiles=memory_profiles,
            load_test_results=load_results,
            scaling_analysis=scaling_analysis,
            optimization_recommendations=recommendations
        )

    def generate_final_report(self, summary: IntegrationPerformanceSummary) -> str:
        """Generate comprehensive final performance report"""
        report = []
        report.append("# Integration Performance Final Analysis Report")
        report.append(f"**Generated**: {datetime.now().isoformat()}")
        report.append(f"**Total Tests Executed**: {summary.total_tests}")
        report.append("")
        
        # Executive Summary
        report.append("## Executive Summary")
        report.append("")
        
        if summary.memory_profiles:
            avg_memory_efficiency = sum(p.memory_efficiency_score for p in summary.memory_profiles) / len(summary.memory_profiles)
            max_memory_growth = max(p.memory_growth_mb for p in summary.memory_profiles)
            report.append(f"- **Average Memory Efficiency**: {avg_memory_efficiency:.1f}%")
            report.append(f"- **Maximum Memory Growth**: {max_memory_growth:.1f}MB")
        
        if summary.load_test_results:
            max_throughput = max(r.throughput_ops_per_second for r in summary.load_test_results)
            avg_error_rate = sum(r.error_rate_percent for r in summary.load_test_results) / len(summary.load_test_results)
            report.append(f"- **Maximum Throughput**: {max_throughput:.1f} ops/second")
            report.append(f"- **Average Error Rate**: {avg_error_rate:.1f}%")
        
        report.append("")
        
        # Memory Analysis
        if summary.memory_profiles:
            report.append("## Memory Usage Analysis")
            report.append("")
            for profile in summary.memory_profiles:
                report.append(f"### {profile.test_name.replace('_', ' ').title()}")
                report.append(f"- **Memory Growth**: {profile.memory_growth_mb:.1f}MB")
                report.append(f"- **Efficiency Score**: {profile.memory_efficiency_score:.1f}%")
                report.append(f"- **GC Impact**: {profile.garbage_collection_impact:.1f}MB")
                report.append("")
        
        # Load Testing Analysis
        if summary.load_test_results:
            report.append("## Load Testing Results")
            report.append("")
            report.append("| Concurrency | Avg Response (ms) | Throughput (ops/s) | Error Rate (%) | Memory Pressure (MB) |")
            report.append("|-------------|-------------------|-------------------|----------------|---------------------|")
            
            for result in summary.load_test_results:
                report.append(f"| {result.concurrent_operations} | {result.avg_response_time_ms:.1f} | "
                             f"{result.throughput_ops_per_second:.1f} | {result.error_rate_percent:.1f} | "
                             f"{result.memory_pressure_mb:.1f} |")
            report.append("")
        
        # Scaling Analysis
        if summary.scaling_analysis:
            report.append("## Performance Scaling Analysis")
            report.append("")
            
            degradation_points = summary.scaling_analysis.get('performance_degradation_points', [])
            if degradation_points:
                report.append("### Performance Degradation Points")
                for point in degradation_points:
                    report.append(f"- **{point['concurrent_ops']} concurrent operations**: "
                                 f"{point['response_time_increase']:.1f}x response time increase")
                report.append("")
        
        # Optimization Recommendations
        report.append("## Optimization Recommendations")
        report.append("")
        for i, recommendation in enumerate(summary.optimization_recommendations, 1):
            report.append(f"{i}. {recommendation}")
        
        return '\n'.join(report)

def main():
    """Main integration performance analysis execution"""
    if len(sys.argv) != 3:
        print("Usage: python integration-performance-final-analysis.py <commands_dir> <components_dir>")
        sys.exit(1)
    
    commands_dir = sys.argv[1]
    components_dir = sys.argv[2]
    
    analyzer = IntegrationPerformanceAnalyzer(commands_dir, components_dir)
    
    # Run comprehensive analysis
    summary = analyzer.run_comprehensive_analysis()
    
    print("\n" + "=" * 60)
    print("✅ Integration Performance Final Analysis Complete")
    print(f"📊 {summary.total_tests} total tests executed")
    print(f"🧠 {len(summary.memory_profiles)} memory profiles analyzed")
    print(f"⚡ {len(summary.load_test_results)} load test configurations executed")
    
    # Generate final report
    report = analyzer.generate_final_report(summary)
    
    # Save results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save detailed results
    results_file = f"integration_performance_final_{timestamp}.json"
    with open(results_file, 'w') as f:
        json.dump(asdict(summary), f, indent=2, default=str)
    
    # Save human-readable report
    report_file = f"integration_performance_report_{timestamp}.md"
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"💾 Detailed results saved to: {results_file}")
    print(f"📋 Report saved to: {report_file}")
    print("\n" + report)

if __name__ == "__main__":
    main()