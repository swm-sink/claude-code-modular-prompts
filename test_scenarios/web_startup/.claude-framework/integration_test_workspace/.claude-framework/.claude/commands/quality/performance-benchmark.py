#!/usr/bin/env python3
"""
Performance Integration Benchmarking Tool
Executes comprehensive performance validation of all integration patterns.

Agent: Performance Integration Agent
Mission: Systematic performance benchmarking against established baselines
Focus: Command loading, component loading, workflow execution, memory usage
"""

import os
import sys
import time
import psutil
import json
import re
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
from datetime import datetime

@dataclass
class PerformanceMetrics:
    """Performance measurement data structure"""
    name: str
    load_time_ms: float
    memory_usage_mb: float
    file_size_kb: float
    component_count: int
    dependency_count: int
    status: str
    baseline_target_ms: float
    performance_grade: str

@dataclass
class BenchmarkResult:
    """Complete benchmark result structure"""
    test_type: str
    test_name: str
    metrics: PerformanceMetrics
    timestamp: str
    baseline_met: bool
    optimization_needed: bool

class PerformanceBenchmarker:
    """Comprehensive performance benchmarking framework"""
    
    def __init__(self, commands_dir: str, components_dir: str):
        self.commands_dir = Path(commands_dir)
        self.components_dir = Path(components_dir)
        self.results: List[BenchmarkResult] = []
        
        # Performance baselines from integration-test-matrices.md
        self.command_baselines = {
            'simple': 50,    # ms - /help, /query
            'medium': 100,   # ms - /task, /test  
            'complex': 150,  # ms - /auto, /test-integration
            'maximum': 200   # ms - absolute limit
        }
        
        self.component_baselines = {
            'individual': 25,    # ms - single components
            'stack': 75,         # ms - 3-5 components
            'framework': 200,    # ms - 10+ components
            'maximum': 300       # ms - absolute limit
        }
        
        self.memory_baselines = {
            'baseline': 128,     # MB - system baseline
            'command': 64,       # MB - additional per command
            'workflow': 256,     # MB - total workflow limit
            'maximum': 512       # MB - absolute limit
        }

    def measure_file_load_performance(self, file_path: Path) -> Tuple[float, float, int]:
        """Measure file loading time, memory usage, and component count"""
        process = psutil.Process()
        
        # Memory before loading
        memory_before = process.memory_info().rss / 1024 / 1024  # MB
        
        # Time the file loading
        start_time = time.perf_counter()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Count components referenced (basic heuristic)
            component_count = len(re.findall(r'@import|@include|components/', content))
            
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return 0.0, 0.0, 0
        
        end_time = time.perf_counter()
        
        # Memory after loading
        memory_after = process.memory_info().rss / 1024 / 1024  # MB
        
        load_time_ms = (end_time - start_time) * 1000
        memory_usage_mb = memory_after - memory_before
        
        return load_time_ms, memory_usage_mb, component_count

    def classify_command_complexity(self, file_path: Path) -> str:
        """Classify command complexity based on content analysis"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Complexity indicators
            indicators = {
                'tools': len(re.findall(r'tools:\s*\[([^\]]+)\]', content, re.IGNORECASE)),
                'components': len(re.findall(r'@import|@include|components/', content)),
                'sections': len(re.findall(r'^#{1,3}\s', content, re.MULTILINE)),
                'code_blocks': len(re.findall(r'```', content)),
                'file_size': file_path.stat().st_size
            }
            
            complexity_score = (
                indicators['tools'] * 2 +
                indicators['components'] * 3 +
                indicators['sections'] * 1 +
                indicators['code_blocks'] * 1 +
                indicators['file_size'] / 1000
            )
            
            if complexity_score < 10:
                return 'simple'
            elif complexity_score < 25:
                return 'medium'
            else:
                return 'complex'
                
        except Exception:
            return 'simple'

    def get_performance_grade(self, actual_ms: float, baseline_ms: float) -> str:
        """Calculate performance grade based on baseline comparison"""
        ratio = actual_ms / baseline_ms
        
        if ratio <= 0.5:
            return 'A+'
        elif ratio <= 0.75:
            return 'A'
        elif ratio <= 1.0:
            return 'B+'
        elif ratio <= 1.25:
            return 'B'
        elif ratio <= 1.5:
            return 'C+'
        elif ratio <= 2.0:
            return 'C'
        else:
            return 'F'

    def benchmark_command_loading(self) -> List[BenchmarkResult]:
        """Benchmark all active command loading performance"""
        print("🧪 Benchmarking Command Loading Performance...")
        
        command_files = []
        for pattern in ['**/*.md']:
            command_files.extend(self.commands_dir.glob(pattern))
        
        # Filter out deprecated commands
        active_commands = [f for f in command_files if 'deprecated' not in str(f)]
        
        results = []
        
        for cmd_file in active_commands:
            relative_path = cmd_file.relative_to(self.commands_dir)
            
            # Measure performance
            load_time_ms, memory_usage_mb, component_count = self.measure_file_load_performance(cmd_file)
            
            # Classify complexity and get baseline
            complexity = self.classify_command_complexity(cmd_file)
            baseline_ms = self.command_baselines[complexity]
            
            # Calculate metrics
            file_size_kb = cmd_file.stat().st_size / 1024
            performance_grade = self.get_performance_grade(load_time_ms, baseline_ms)
            
            metrics = PerformanceMetrics(
                name=str(relative_path),
                load_time_ms=load_time_ms,
                memory_usage_mb=memory_usage_mb,
                file_size_kb=file_size_kb,
                component_count=component_count,
                dependency_count=0,  # Would need dependency analysis
                status='measured',
                baseline_target_ms=baseline_ms,
                performance_grade=performance_grade
            )
            
            result = BenchmarkResult(
                test_type='command_loading',
                test_name=str(relative_path),
                metrics=metrics,
                timestamp=datetime.now().isoformat(),
                baseline_met=load_time_ms <= baseline_ms,
                optimization_needed=load_time_ms > baseline_ms * 1.2
            )
            
            results.append(result)
            
            print(f"  {relative_path}: {load_time_ms:.1f}ms ({complexity}, {performance_grade})")
        
        return results

    def benchmark_component_loading(self) -> List[BenchmarkResult]:
        """Benchmark component loading performance for defined stacks"""
        print("\n🔧 Benchmarking Component Loading Performance...")
        
        # Component stacks from integration-test-matrices.md
        component_stacks = {
            'orchestration': ['dag-orchestrator', 'task-execution', 'progress-tracking'],
            'validation': ['validation-framework', 'input-validation', 'security-validation'],
            'context': ['hierarchical-loading', 'context-optimization', 'adaptive-thinking'],
            'intelligence': ['multi-agent-coordination', 'cognitive-architecture', 'pattern-extraction'],
            'testing': ['testing-framework', 'framework-validation', 'mutation-testing'],
            'error': ['error-handling', 'circuit-breaker', 'chaos-engineering'],
            'performance': ['performance-optimization', 'component-cache', 'framework-optimization'],
            'security': ['owasp-compliance', 'secure-config', 'anti-pattern-detection']
        }
        
        results = []
        
        for stack_name, components in component_stacks.items():
            stack_load_time = 0
            stack_memory = 0
            found_components = 0
            
            for component_name in components:
                # Find component file
                component_files = list(self.components_dir.glob(f'**/{component_name}.md'))
                if not component_files:
                    # Try variations
                    component_files = list(self.components_dir.glob(f'**/*{component_name.replace("-", "_")}*.md'))
                
                if component_files:
                    comp_file = component_files[0]
                    load_time_ms, memory_usage_mb, comp_count = self.measure_file_load_performance(comp_file)
                    stack_load_time += load_time_ms
                    stack_memory += memory_usage_mb
                    found_components += 1
            
            if found_components > 0:
                # Calculate stack performance
                baseline_ms = self.component_baselines['stack']
                performance_grade = self.get_performance_grade(stack_load_time, baseline_ms)
                
                metrics = PerformanceMetrics(
                    name=f"{stack_name}_stack",
                    load_time_ms=stack_load_time,
                    memory_usage_mb=stack_memory,
                    file_size_kb=0,  # Stack aggregate
                    component_count=found_components,
                    dependency_count=len(components),
                    status='measured',
                    baseline_target_ms=baseline_ms,
                    performance_grade=performance_grade
                )
                
                result = BenchmarkResult(
                    test_type='component_stack_loading',
                    test_name=stack_name,
                    metrics=metrics,
                    timestamp=datetime.now().isoformat(),
                    baseline_met=stack_load_time <= baseline_ms,
                    optimization_needed=stack_load_time > baseline_ms * 1.2
                )
                
                results.append(result)
                
                print(f"  {stack_name} stack: {stack_load_time:.1f}ms ({found_components}/{len(components)} components, {performance_grade})")
        
        return results

    def benchmark_integration_patterns(self) -> List[BenchmarkResult]:
        """Benchmark command-to-command integration patterns"""
        print("\n🔗 Benchmarking Integration Pattern Performance...")
        
        # Integration patterns from matrices
        integration_patterns = [
            ('intelligent_routing', ['/auto', '/task', '/test', '/validate-command']),
            ('development_workflow', ['/task', '/test', '/validate-command', '/auto']),
            ('quality_assurance', ['/validate-command', '/test-integration', '/analyze-system']),
            ('discovery_implementation', ['/help', '/query', '/task', '/test']),
            ('diagnostic_fix', ['/analyze-system', '/task', '/test', '/validate-command'])
        ]
        
        results = []
        
        for pattern_name, command_sequence in integration_patterns:
            pattern_load_time = 0
            pattern_memory = 0
            found_commands = 0
            
            for command in command_sequence:
                # Find command file (remove leading slash and look for .md files)
                cmd_name = command.lstrip('/')
                cmd_files = list(self.commands_dir.glob(f'**/{cmd_name}.md'))
                
                if cmd_files:
                    cmd_file = cmd_files[0]
                    load_time_ms, memory_usage_mb, comp_count = self.measure_file_load_performance(cmd_file)
                    pattern_load_time += load_time_ms
                    pattern_memory += memory_usage_mb
                    found_commands += 1
            
            if found_commands > 0:
                # Estimate integration overhead (20% penalty for chaining)
                integration_overhead = pattern_load_time * 0.2
                total_time = pattern_load_time + integration_overhead
                
                # Use medium baseline for integration patterns
                baseline_ms = self.command_baselines['medium'] * len(command_sequence)
                performance_grade = self.get_performance_grade(total_time, baseline_ms)
                
                metrics = PerformanceMetrics(
                    name=f"{pattern_name}_integration",
                    load_time_ms=total_time,
                    memory_usage_mb=pattern_memory,
                    file_size_kb=0,  # Integration aggregate
                    component_count=found_commands,
                    dependency_count=len(command_sequence),
                    status='estimated',
                    baseline_target_ms=baseline_ms,
                    performance_grade=performance_grade
                )
                
                result = BenchmarkResult(
                    test_type='integration_pattern',
                    test_name=pattern_name,
                    metrics=metrics,
                    timestamp=datetime.now().isoformat(),
                    baseline_met=total_time <= baseline_ms,
                    optimization_needed=total_time > baseline_ms * 1.2
                )
                
                results.append(result)
                
                print(f"  {pattern_name}: {total_time:.1f}ms ({found_commands}/{len(command_sequence)} commands, {performance_grade})")
        
        return results

    def generate_performance_report(self, all_results: List[BenchmarkResult]) -> str:
        """Generate comprehensive performance benchmarking report"""
        report = []
        report.append("# Performance Integration Benchmarking Report")
        report.append(f"**Generated**: {datetime.now().isoformat()}")
        report.append(f"**Total Tests**: {len(all_results)}")
        report.append("")
        
        # Group results by test type
        by_type = {}
        for result in all_results:
            if result.test_type not in by_type:
                by_type[result.test_type] = []
            by_type[result.test_type].append(result)
        
        # Summary statistics
        report.append("## Executive Summary")
        report.append("")
        
        total_baseline_met = sum(1 for r in all_results if r.baseline_met)
        total_optimization_needed = sum(1 for r in all_results if r.optimization_needed)
        baseline_rate = (total_baseline_met / len(all_results)) * 100 if all_results else 0
        
        report.append(f"- **Baseline Compliance**: {total_baseline_met}/{len(all_results)} ({baseline_rate:.1f}%)")
        report.append(f"- **Optimization Needed**: {total_optimization_needed}/{len(all_results)}")
        report.append("")
        
        # Performance grade distribution
        grades = [r.metrics.performance_grade for r in all_results]
        grade_counts = {grade: grades.count(grade) for grade in set(grades)}
        report.append("### Performance Grade Distribution")
        for grade in ['A+', 'A', 'B+', 'B', 'C+', 'C', 'F']:
            if grade in grade_counts:
                report.append(f"- **{grade}**: {grade_counts[grade]} tests")
        report.append("")
        
        # Detailed results by test type
        for test_type, results in by_type.items():
            report.append(f"## {test_type.replace('_', ' ').title()} Results")
            report.append("")
            
            # Calculate statistics for this test type
            load_times = [r.metrics.load_time_ms for r in results]
            avg_load_time = sum(load_times) / len(load_times) if load_times else 0
            max_load_time = max(load_times) if load_times else 0
            
            baseline_met_type = sum(1 for r in results if r.baseline_met)
            baseline_rate_type = (baseline_met_type / len(results)) * 100 if results else 0
            
            report.append(f"- **Tests**: {len(results)}")
            report.append(f"- **Average Load Time**: {avg_load_time:.1f}ms")
            report.append(f"- **Maximum Load Time**: {max_load_time:.1f}ms")
            report.append(f"- **Baseline Compliance**: {baseline_met_type}/{len(results)} ({baseline_rate_type:.1f}%)")
            report.append("")
            
            # Top performers and problem areas
            sorted_results = sorted(results, key=lambda r: r.metrics.load_time_ms)
            
            report.append("### Top Performers")
            for result in sorted_results[:3]:
                report.append(f"- **{result.test_name}**: {result.metrics.load_time_ms:.1f}ms ({result.metrics.performance_grade})")
            report.append("")
            
            if total_optimization_needed > 0:
                problem_results = [r for r in results if r.optimization_needed]
                if problem_results:
                    report.append("### Optimization Needed")
                    for result in problem_results:
                        report.append(f"- **{result.test_name}**: {result.metrics.load_time_ms:.1f}ms (target: {result.metrics.baseline_target_ms:.1f}ms)")
                    report.append("")
        
        # Optimization recommendations
        report.append("## Optimization Recommendations")
        report.append("")
        
        high_load_times = [r for r in all_results if r.metrics.load_time_ms > 100]
        if high_load_times:
            report.append("### High Load Time Items")
            for result in high_load_times:
                report.append(f"- **{result.test_name}**: {result.metrics.load_time_ms:.1f}ms")
                if result.metrics.component_count > 5:
                    report.append("  - Consider component lazy loading")
                if result.metrics.file_size_kb > 50:
                    report.append("  - Consider content optimization")
                report.append("")
        
        # Memory usage analysis
        high_memory = [r for r in all_results if r.metrics.memory_usage_mb > 10]
        if high_memory:
            report.append("### High Memory Usage Items")
            for result in high_memory:
                report.append(f"- **{result.test_name}**: {result.metrics.memory_usage_mb:.1f}MB")
            report.append("")
        
        return '\n'.join(report)

    def save_results(self, results: List[BenchmarkResult], filename: str):
        """Save benchmark results to JSON file"""
        with open(filename, 'w') as f:
            json.dump([asdict(result) for result in results], f, indent=2)

def main():
    """Main benchmarking execution"""
    if len(sys.argv) != 3:
        print("Usage: python performance-benchmark.py <commands_dir> <components_dir>")
        sys.exit(1)
    
    commands_dir = sys.argv[1]
    components_dir = sys.argv[2]
    
    benchmarker = PerformanceBenchmarker(commands_dir, components_dir)
    
    print("🚀 Performance Integration Benchmarking Starting...")
    print("=" * 60)
    
    all_results = []
    
    # Execute all benchmark tests
    all_results.extend(benchmarker.benchmark_command_loading())
    all_results.extend(benchmarker.benchmark_component_loading())
    all_results.extend(benchmarker.benchmark_integration_patterns())
    
    print("\n" + "=" * 60)
    print(f"✅ Performance Benchmarking Complete: {len(all_results)} tests executed")
    
    # Generate and save report
    report = benchmarker.generate_performance_report(all_results)
    
    # Save results
    results_file = f"performance_benchmark_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    benchmarker.save_results(all_results, results_file)
    
    print(f"📊 Results saved to: {results_file}")
    print("\n" + report)

if __name__ == "__main__":
    main()