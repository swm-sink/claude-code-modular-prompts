#!/usr/bin/env python3
"""
Performance Benchmark Tests for YAML Validation
TDD approach: Define performance targets, then optimize to meet them
"""

import time
import os
import statistics
from pathlib import Path
import sys
sys.path.append('.')

def validate_yaml_frontmatter(file_path):
    """Lightweight YAML validation for benchmarking"""
    import yaml
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            return ["Missing YAML frontmatter"]
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            return ["Invalid YAML frontmatter structure"]
        
        yaml_content = parts[1]
        yaml_data = yaml.safe_load(yaml_content)
        
        if not isinstance(yaml_data, dict):
            return ["YAML frontmatter must be a dictionary"]
        
        issues = []
        required_fields = ['name', 'description']
        for field in required_fields:
            if field not in yaml_data:
                issues.append(f"Missing required field: '{field}'")
        
        return issues
        
    except Exception as e:
        return [f"Validation error: {e}"]

class PerformanceBenchmark:
    """Performance benchmarking for validation operations"""
    
    def __init__(self):
        self.target_validation_time = 0.002  # 2ms target
        self.target_total_time = 0.164  # 164ms for 82 files (2ms each)
        self.results = []
    
    def benchmark_single_file_validation(self, file_path, iterations=10):
        """Benchmark single file validation performance"""
        times = []
        
        for _ in range(iterations):
            start_time = time.perf_counter()
            validate_yaml_frontmatter(file_path)
            end_time = time.perf_counter()
            times.append(end_time - start_time)
        
        avg_time = statistics.mean(times)
        min_time = min(times)
        max_time = max(times)
        
        return {
            'average': avg_time,
            'minimum': min_time,
            'maximum': max_time,
            'meets_target': avg_time <= self.target_validation_time,
            'target': self.target_validation_time
        }
    
    def benchmark_full_validation_suite(self):
        """Benchmark full validation suite performance"""
        command_files = list(Path('.claude/commands').rglob('*.md'))
        
        start_time = time.perf_counter()
        
        for file_path in command_files:
            validate_yaml_frontmatter(str(file_path))
        
        end_time = time.perf_counter()
        total_time = end_time - start_time
        
        avg_per_file = total_time / len(command_files)
        
        return {
            'total_files': len(command_files),
            'total_time': total_time,
            'average_per_file': avg_per_file,
            'meets_target': total_time <= self.target_total_time,
            'target_total': self.target_total_time,
            'target_per_file': self.target_validation_time
        }
    
    def run_comprehensive_benchmark(self):
        """Run comprehensive performance benchmark"""
        print("🚀 PERFORMANCE BENCHMARK TESTS")
        print("=" * 50)
        print(f"🎯 Target: <{self.target_validation_time*1000:.1f}ms per file")
        print(f"🎯 Target: <{self.target_total_time*1000:.0f}ms total (82 files)")
        print()
        
        # Test sample files
        sample_files = [
            '.claude/commands/core/task.md',
            '.claude/commands/quality/test.md',
            '.claude/commands/specialized/swarm.md'
        ]
        
        print("📊 SINGLE FILE BENCHMARKS:")
        for file_path in sample_files:
            if os.path.exists(file_path):
                result = self.benchmark_single_file_validation(file_path)
                status = "✅ PASS" if result['meets_target'] else "❌ FAIL"
                print(f"{status} {file_path}")
                print(f"    Average: {result['average']*1000:.2f}ms")
                print(f"    Range: {result['minimum']*1000:.2f}-{result['maximum']*1000:.2f}ms")
                print(f"    Target: {result['target']*1000:.1f}ms")
                print()
        
        # Full suite benchmark
        print("📊 FULL VALIDATION SUITE BENCHMARK:")
        suite_result = self.benchmark_full_validation_suite()
        status = "✅ PASS" if suite_result['meets_target'] else "❌ FAIL"
        
        print(f"{status} Full Validation Suite")
        print(f"    Files processed: {suite_result['total_files']}")
        print(f"    Total time: {suite_result['total_time']*1000:.0f}ms")
        print(f"    Average per file: {suite_result['average_per_file']*1000:.2f}ms")
        print(f"    Target total: {suite_result['target_total']*1000:.0f}ms")
        print(f"    Target per file: {suite_result['target_per_file']*1000:.1f}ms")
        
        # Performance assessment
        print("\n🏆 PERFORMANCE ASSESSMENT:")
        if suite_result['meets_target']:
            print("✅ EXCELLENT: Performance targets exceeded!")
        else:
            improvement_needed = ((suite_result['total_time'] / suite_result['target_total']) - 1) * 100
            print(f"⚠️  NEEDS OPTIMIZATION: {improvement_needed:.1f}% improvement required")
        
        return suite_result

def run_performance_tests():
    """Run performance benchmark tests"""
    benchmark = PerformanceBenchmark()
    return benchmark.run_comprehensive_benchmark()

if __name__ == "__main__":
    run_performance_tests()