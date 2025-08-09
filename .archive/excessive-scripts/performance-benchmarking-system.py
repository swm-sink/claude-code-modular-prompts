#!/usr/bin/env python3
"""
Performance Benchmarking System
Step 82 of 100-Step Finalization Plan

PURPOSE: Comprehensive performance measurement across all system components
SCOPE: Commands, components, validation, workflows, and integration points
"""

import os
import sys
import time
import psutil
import yaml
import json
import statistics
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

@dataclass
class PerformanceMetric:
    metric_name: str
    value: float
    unit: str
    category: str
    target: Optional[float] = None
    status: str = "UNKNOWN"  # EXCELLENT, GOOD, ACCEPTABLE, POOR

class PerformanceBenchmarkSystem:
    """Comprehensive performance benchmarking for the entire system"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.results: List[PerformanceMetric] = []
        self.start_time = time.time()
        
        # Core paths
        self.claude_dir = project_root / ".claude"
        self.commands_dir = self.claude_dir / "commands"
        self.components_dir = self.claude_dir / "components"
        
        # Performance targets (based on research and best practices)
        self.targets = {
            "yaml_validation_ms": 2.0,  # < 2ms per file
            "file_read_ms": 1.0,  # < 1ms per file
            "command_discovery_ms": 10.0,  # < 10ms total
            "component_load_ms": 5.0,  # < 5ms total
            "memory_usage_mb": 50.0,  # < 50MB total
            "disk_io_ms": 100.0,  # < 100ms for full scan
        }
    
    def run_comprehensive_benchmarks(self) -> Dict[str, Any]:
        """Execute all performance benchmarks"""
        print("📊 COMPREHENSIVE PERFORMANCE BENCHMARKING")
        print("=" * 60)
        
        # Benchmark categories
        benchmark_categories = [
            ("File System Performance", self._benchmark_file_system),
            ("YAML Processing Performance", self._benchmark_yaml_processing),
            ("Command Discovery Performance", self._benchmark_command_discovery),
            ("Component Loading Performance", self._benchmark_component_loading),
            ("Memory Usage Analysis", self._benchmark_memory_usage),
            ("Concurrent Processing", self._benchmark_concurrent_processing),
            ("Disk I/O Performance", self._benchmark_disk_io),
            ("Integration Performance", self._benchmark_integration_performance)
        ]
        
        for category_name, benchmark_method in benchmark_categories:
            print(f"\n🏃 Benchmarking: {category_name}")
            try:
                benchmark_method()
            except Exception as e:
                self._add_metric(f"{category_name} - Error", 0, "error", "ERROR", 
                               message=f"Benchmark failed: {str(e)}")
        
        return self._generate_performance_report()
    
    def _benchmark_file_# SECURITY WARNING: system() call - validate all inputssystem(self):
        """Benchmark file system operations"""
        
        # File enumeration performance
        start = time.time()
        command_files = list(self.commands_dir.rglob("*.md"))
        enum_time = (time.time() - start) * 1000
        self._add_metric("File Enumeration", enum_time, "ms", "FileSystem")
        
        # File reading performance
        if command_files:
            read_times = []
            for i, file_path in enumerate(command_files[:10]):  # Sample first 10
                start = time.time()
                try:
                    content = file_path.read_text(encoding='utf-8')
                    read_time = (time.time() - start) * 1000
                    read_times.append(read_time)
                except Exception:
                    continue
            
            if read_times:
                avg_read_time = statistics.mean(read_times)
                self._add_metric("Average File Read", avg_read_time, "ms", "FileSystem",
                               target=self.targets["file_read_ms"])
                
                max_read_time = max(read_times)
                self._add_metric("Maximum File Read", max_read_time, "ms", "FileSystem")
        
        # Directory traversal performance
        start = time.time()
        all_files = list(self.project_root.rglob("*"))
        traversal_time = (time.time() - start) * 1000
        self._add_metric("Full Directory Traversal", traversal_time, "ms", "FileSystem")
        
        print(f"  📁 Files enumerated: {len(command_files)}, Total files: {len(all_files)}")
    
    def _benchmark_yaml_processing(self):
        """Benchmark YAML processing performance"""
        
        command_files = list(self.commands_dir.rglob("*.md"))
        yaml_times = []
        yaml_success = 0
        
        for file_path in command_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end > 0:
                        yaml_content = content[3:yaml_end]
                        
                        start = time.time()
                        yaml_data = yaml.safe_load(yaml_content)
                        yaml_time = (time.time() - start) * 1000
                        
                        yaml_times.append(yaml_time)
                        yaml_success += 1
            except Exception:
                continue
        
        if yaml_times:
            avg_yaml_time = statistics.mean(yaml_times)
            self._add_metric("Average YAML Processing", avg_yaml_time, "ms", "YAML",
                           target=self.targets["yaml_validation_ms"])
            
            max_yaml_time = max(yaml_times)
            self._add_metric("Maximum YAML Processing", max_yaml_time, "ms", "YAML")
            
            total_yaml_time = sum(yaml_times)
            self._add_metric("Total YAML Processing", total_yaml_time, "ms", "YAML")
        
        print(f"  📄 YAML files processed: {yaml_success}/{len(command_files)}")
    
    def _benchmark_command_discovery(self):
        """Benchmark command discovery performance"""
        
        start = time.time()
        
        # Simulate command discovery process
        commands = {}
        command_files = list(self.commands_dir.rglob("*.md"))
        
        for file_path in command_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end > 0:
                        yaml_content = content[3:yaml_end]
                        yaml_data = yaml.safe_load(yaml_content)
                        
                        if 'name' in yaml_data:
                            commands[yaml_data['name']] = {
                                'file': str(file_path),
                                'description': yaml_data.get('description', ''),
                                'category': yaml_data.get('category', 'uncategorized')
                            }
            except Exception:
                continue
        
        discovery_time = (time.time() - start) * 1000
        self._add_metric("Command Discovery", discovery_time, "ms", "Discovery",
                        target=self.targets["command_discovery_ms"])
        
        print(f"  🔍 Commands discovered: {len(commands)}")
    
    def _benchmark_component_loading(self):
        """Benchmark component loading performance"""
        
        start = time.time()
        
        component_files = list(self.components_dir.rglob("*.md"))
        components = {}
        
        for file_path in component_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                components[file_path.stem] = {
                    'content': content,
                    'size': len(content),
                    'lines': len(content.split('\n'))
                }
            except Exception:
                continue
        
        loading_time = (time.time() - start) * 1000
        self._add_metric("Component Loading", loading_time, "ms", "Components",
                        target=self.targets["component_load_ms"])
        
        if components:
            avg_component_size = statistics.mean([c['size'] for c in components.values()])
            self._add_metric("Average Component Size", avg_component_size, "bytes", "Components")
        
        print(f"  🧩 Components loaded: {len(components)}")
    
    def _benchmark_memory_usage(self):
        """Benchmark memory usage"""
        
        process = psutil.Process()
        
        # Baseline memory
        baseline_memory = process.memory_info().rss / 1024 / 1024  # MB
        
        # Load all files into memory to simulate heavy usage
        loaded_content = []
        for file_path in self.project_root.rglob("*.md"):
            try:
                content = file_path.read_text(encoding='utf-8')
                loaded_content.append(content)
            except Exception:
                continue
        
        # Peak memory
        peak_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_delta = peak_memory - baseline_memory
        
        self._add_metric("Baseline Memory Usage", baseline_memory, "MB", "Memory")
        self._add_metric("Peak Memory Usage", peak_memory, "MB", "Memory")
        self._add_metric("Memory Delta", memory_delta, "MB", "Memory",
                        target=self.targets["memory_usage_mb"])
        
        # CPU usage
        cpu_percent = process.cpu_percent()
        self._add_metric("CPU Usage", cpu_percent, "%", "Performance")
        
        print(f"  💾 Memory: {baseline_memory:.1f}MB → {peak_memory:.1f}MB (Δ{memory_delta:.1f}MB)")
    
    def _benchmark_concurrent_processing(self):
        """Benchmark concurrent processing performance"""
        
        command_files = list(self.commands_dir.rglob("*.md"))[:20]  # Sample
        
        # Sequential processing
        start = time.time()
        sequential_results = []
        for file_path in command_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                sequential_results.append(len(content))
            except Exception:
                continue
        sequential_time = (time.time() - start) * 1000
        
        # Concurrent processing
        start = time.time()
        concurrent_results = []
        
        def process_file(file_path):
            try:
                content = file_path.read_text(encoding='utf-8')
                return len(content)
            except Exception:
                return 0
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(process_file, fp) for fp in command_files]
            for future in as_completed(futures):
                concurrent_results.append(future.result())
        
        concurrent_time = (time.time() - start) * 1000
        
        self._add_metric("Sequential Processing", sequential_time, "ms", "Concurrency")
        self._add_metric("Concurrent Processing", concurrent_time, "ms", "Concurrency")
        
        if sequential_time > 0:
            speedup = sequential_time / concurrent_time
            self._add_metric("Concurrency Speedup", speedup, "x", "Concurrency")
        
        print(f"  ⚡ Sequential: {sequential_time:.1f}ms, Concurrent: {concurrent_time:.1f}ms")
    
    def _benchmark_disk_io(self):
        """Benchmark disk I/O performance"""
        
        # Full project scan
        start = time.time()
        file_count = 0
        total_size = 0
        
        for file_path in self.project_root.rglob("*"):
            if file_path.is_file():
                try:
                    file_count += 1
                    total_size += file_path.stat().st_size
                except Exception:
                    continue
        
        scan_time = (time.time() - start) * 1000
        self._add_metric("Full Project Scan", scan_time, "ms", "DiskIO",
                        target=self.targets["disk_io_ms"])
        
        if file_count > 0:
            avg_file_size = total_size / file_count
            self._add_metric("Average File Size", avg_file_size, "bytes", "DiskIO")
        
        self._add_metric("Total Files Scanned", file_count, "files", "DiskIO")
        self._add_metric("Total Project Size", total_size / 1024 / 1024, "MB", "DiskIO")
        
        print(f"  💽 Scanned: {file_count} files, {total_size/1024/1024:.1f}MB in {scan_time:.1f}ms")
    
    def _benchmark_integration_performance(self):
        """Benchmark integration performance (simulated workflows)"""
        
        # Simulate a typical workflow: discover commands → validate YAML → load components
        start = time.time()
        
        # Step 1: Command discovery
        command_files = list(self.commands_dir.rglob("*.md"))
        
        # Step 2: YAML validation
        valid_commands = 0
        for file_path in command_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end > 0:
                        yaml_content = content[3:yaml_end]
                        yaml_data = yaml.safe_load(yaml_content)
                        if 'name' in yaml_data and 'description' in yaml_data:
                            valid_commands += 1
            except Exception:
                continue
        
        # Step 3: Component loading
        component_files = list(self.components_dir.rglob("*.md"))
        loaded_components = 0
        for file_path in component_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                if content.strip():
                    loaded_components += 1
            except Exception:
                continue
        
        workflow_time = (time.time() - start) * 1000
        self._add_metric("Full Workflow Integration", workflow_time, "ms", "Integration")
        
        print(f"  🔄 Workflow: {len(command_files)} commands, {valid_commands} valid, {loaded_components} components")
    
    def _add_metric(self, name: str, value: float, unit: str, category: str, 
                   target: Optional[float] = None, message: str = ""):
        """Add performance metric"""
        
        # Determine status based on target
        status = "UNKNOWN"
        if target is not None:
            if value <= target * 0.5:
                status = "EXCELLENT"
            elif value <= target:
                status = "GOOD"
            elif value <= target * 2:
                status = "ACCEPTABLE"
            else:
                status = "POOR"
        
        metric = PerformanceMetric(
            metric_name=name,
            value=value,
            unit=unit,
            category=category,
            target=target,
            status=status
        )
        
        self.results.append(metric)
        
        # Real-time feedback
        status_emoji = {
            "EXCELLENT": "🟢", "GOOD": "🟡", "ACCEPTABLE": "🟠", 
            "POOR": "🔴", "UNKNOWN": "⚪", "ERROR": "💥"
        }
        
        target_str = f" (target: {target}{unit})" if target else ""
        print(f"    {status_emoji.get(status, '❓')} {name}: {value:.2f}{unit}{target_str}")
    
    def _generate_performance_report(self) -> Dict[str, Any]:
        """Generate comprehensive performance report"""
        total_time = time.time() - self.start_time
        
        # Categorize results
        categories = {}
        for metric in self.results:
            if metric.category not in categories:
                categories[metric.category] = []
            categories[metric.category].append(metric)
        
        # Calculate category statistics
        category_stats = {}
        for category, metrics in categories.items():
            status_counts = {}
            for metric in metrics:
                status_counts[metric.status] = status_counts.get(metric.status, 0) + 1
            
            # Calculate category grade
            total_metrics = len(metrics)
            excellent = status_counts.get("EXCELLENT", 0)
            good = status_counts.get("GOOD", 0)
            acceptable = status_counts.get("ACCEPTABLE", 0)
            
            score = (excellent * 100 + good * 80 + acceptable * 60) / total_metrics
            
            if score >= 90:
                grade = "A+ (Excellent)"
            elif score >= 80:
                grade = "A (Very Good)"
            elif score >= 70:
                grade = "B (Good)"
            elif score >= 60:
                grade = "C (Acceptable)"
            else:
                grade = "D (Needs Improvement)"
            
            category_stats[category] = {
                "total_metrics": total_metrics,
                "status_counts": status_counts,
                "score": score,
                "grade": grade
            }
        
        # Overall system grade
        all_scores = [stats["score"] for stats in category_stats.values()]
        overall_score = statistics.mean(all_scores) if all_scores else 0
        
        if overall_score >= 90:
            overall_grade = "A+ (Excellent Performance)"
        elif overall_score >= 80:
            overall_grade = "A (Very Good Performance)"
        elif overall_score >= 70:
            overall_grade = "B (Good Performance)"
        elif overall_score >= 60:
            overall_grade = "C (Acceptable Performance)"
        else:
            overall_grade = "D (Performance Issues)"
        
        report = {
            "benchmark_summary": {
                "total_metrics": len(self.results),
                "total_benchmarking_time": f"{total_time:.2f}s",
                "overall_score": f"{overall_score:.1f}",
                "overall_grade": overall_grade,
                "benchmark_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            },
            "category_performance": category_stats,
            "detailed_metrics": [
                {
                    "metric": m.metric_name,
                    "value": f"{m.value:.3f}",
                    "unit": m.unit,
                    "category": m.category,
                    "status": m.status,
                    "target": f"{m.target:.1f}{m.unit}" if m.target else "N/A"
                }
                for m in self.results
            ],
            "performance_recommendations": self._generate_performance_recommendations()
        }
        
        return report
    
    def _generate_performance_recommendations(self) -> List[str]:
        """Generate performance improvement recommendations"""
        recommendations = []
        
        poor_metrics = [m for m in self.results if m.status == "POOR"]
        if poor_metrics:
            recommendations.append(f"Address {len(poor_metrics)} performance bottlenecks")
        
        # Category-specific recommendations
        categories = {}
        for metric in self.results:
            if metric.category not in categories:
                categories[metric.category] = []
            categories[metric.category].append(metric)
        
        for category, metrics in categories.items():
            poor_in_category = [m for m in metrics if m.status == "POOR"]
            if poor_in_category:
                recommendations.append(f"Optimize {category} performance ({len(poor_in_category)} issues)")
        
        if not recommendations:
            recommendations.append("Performance is excellent across all metrics")
        
        return recommendations

def main():
    """Run comprehensive performance benchmarking"""
    project_root = Path.cwd()
    
    print(f"🔍 Project root: {project_root}")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    benchmark_system = PerformanceBenchmark# SECURITY WARNING: system() call - validate all inputsSystem(project_root)
    report = benchmark_system.run_comprehensive_benchmarks()
    
    # Display summary
    print("\n" + "="*60)
    print("📊 PERFORMANCE BENCHMARKING SUMMARY")
    print("="*60)
    
    summary = report["benchmark_summary"]
    print(f"Total Metrics: {summary['total_metrics']}")
    print(f"Overall Score: {summary['overall_score']}")
    print(f"Overall Grade: {summary['overall_grade']}")
    print(f"Benchmarking Time: {summary['total_benchmarking_time']}")
    
    print(f"\n📈 CATEGORY PERFORMANCE:")
    for category, stats in report["category_performance"].items():
        print(f"  {category}: {stats['grade']} ({stats['score']:.1f})")
    
    if report["performance_recommendations"]:
        print(f"\n🎯 RECOMMENDATIONS:")
        for i, rec in enumerate(report["performance_recommendations"], 1):
            print(f"{i}. {rec}")
    
    # Save detailed report
    report_file = project_root / "STEP-82-PERFORMANCE-BENCHMARK-RESULTS.md"
    with open(report_file, 'w') as f:
        f.write("# Step 82: Comprehensive Performance Benchmark Results\n\n")
        f.write(f"**Executed**: {summary['benchmark_date']}\n")
        f.write(f"**Overall Grade**: {summary['overall_grade']}\n\n")
        
        f.write("## Executive Summary\n\n")
        f.write(f"- **Total Metrics Measured**: {summary['total_metrics']}\n")
        f.write(f"- **Overall Performance Score**: {summary['overall_score']}\n")
        f.write(f"- **Benchmarking Duration**: {summary['total_benchmarking_time']}\n\n")
        
        f.write("## Category Performance\n\n")
        for category, stats in report["category_performance"].items():
            f.write(f"### {category}: {stats['grade']}\n")
            f.write(f"- **Score**: {stats['score']:.1f}/100\n")
            f.write(f"- **Metrics**: {stats['total_metrics']}\n")
            f.write(f"- **Status Distribution**: {stats['status_counts']}\n\n")
        
        f.write("## Detailed Metrics\n\n")
        f.write("| Metric | Value | Unit | Category | Status | Target |\n")
        f.write("|--------|-------|------|----------|--------|--------|\n")
        for metric in report["detailed_metrics"]:
            f.write(f"| {metric['metric']} | {metric['value']} | {metric['unit']} | {metric['category']} | {metric['status']} | {metric['target']} |\n")
        
        f.write("\n## Performance Recommendations\n\n")
        for i, rec in enumerate(report["performance_recommendations"], 1):
            f.write(f"{i}. {rec}\n")
    
    print(f"\n📄 Detailed report saved: {report_file}")
    
    return float(summary['overall_score']) >= 70  # Return success boolean

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)