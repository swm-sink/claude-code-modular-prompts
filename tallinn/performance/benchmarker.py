"""
Real Performance Benchmarker

This module provides actual measurement capabilities for performance monitoring
using psutil for system metrics and time-based measurements.
"""

import time
import psutil
import functools
import json
import os
from typing import Dict, Any, Optional, List, Callable
from datetime import datetime
from contextlib import contextmanager
import threading
from dataclasses import dataclass, asdict


@dataclass
class BenchmarkResult:
    """Container for benchmark measurement results"""
    operation: str
    duration_seconds: float
    memory_before_mb: float
    memory_after_mb: float
    memory_peak_mb: float
    cpu_percent: float
    timestamp: str
    metadata: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class PerformanceBenchmarker:
    """Real performance measurement system using psutil"""
    
    def __init__(self, results_dir: str = "benchmark_results"):
        self.results_dir = results_dir
        self.results: List[BenchmarkResult] = []
        self._ensure_results_dir()
        
        # Initialize process monitoring
        self.process = psutil.Process()
        self._memory_monitor = None
        self._peak_memory = 0.0
        self._monitoring_active = False
    
    def _ensure_results_dir(self):
        """Ensure the results directory exists"""
        os.makedirs(self.results_dir, exist_ok=True)
    
    def _start_memory_monitoring(self):
        """Start continuous memory monitoring in background thread"""
        self._monitoring_active = True
        self._peak_memory = self.get_memory_usage_mb()
        
        def monitor_memory():
            while self._monitoring_active:
                current_memory = self.get_memory_usage_mb()
                if current_memory > self._peak_memory:
                    self._peak_memory = current_memory
                time.sleep(0.01)  # Check every 10ms
        
        self._memory_monitor = threading.Thread(target=monitor_memory, daemon=True)
        self._memory_monitor.start()
    
    def _stop_memory_monitoring(self):
        """Stop memory monitoring"""
        self._monitoring_active = False
        if self._memory_monitor:
            self._memory_monitor.join(timeout=0.1)
    
    def get_memory_usage_mb(self) -> float:
        """Get current memory usage in MB"""
        try:
            memory_info = self.process.memory_info()
            return memory_info.rss / 1024 / 1024  # Convert bytes to MB
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return 0.0
    
    def get_cpu_percent(self, interval: float = 0.1) -> float:
        """Get CPU usage percentage"""
        try:
            return self.process.cpu_percent(interval=interval)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return 0.0
    
    @contextmanager
    def measure_operation(self, operation_name: str, metadata: Optional[Dict[str, Any]] = None):
        """Context manager for measuring operation performance"""
        if metadata is None:
            metadata = {}
        
        # Record initial state
        memory_before = self.get_memory_usage_mb()
        start_time = time.time()
        self._start_memory_monitoring()
        
        try:
            yield
        finally:
            # Record final state
            end_time = time.time()
            self._stop_memory_monitoring()
            memory_after = self.get_memory_usage_mb()
            cpu_percent = self.get_cpu_percent()
            
            # Create benchmark result
            result = BenchmarkResult(
                operation=operation_name,
                duration_seconds=end_time - start_time,
                memory_before_mb=memory_before,
                memory_after_mb=memory_after,
                memory_peak_mb=self._peak_memory,
                cpu_percent=cpu_percent,
                timestamp=datetime.now().isoformat(),
                metadata=metadata
            )
            
            self.results.append(result)
    
    def benchmark_function(self, func: Callable, *args, **kwargs) -> BenchmarkResult:
        """Benchmark a single function call"""
        operation_name = f"{func.__module__}.{func.__name__}"
        metadata = {
            "args_count": len(args),
            "kwargs_count": len(kwargs),
            "function_name": func.__name__
        }
        
        with self.measure_operation(operation_name, metadata):
            result = func(*args, **kwargs)
            metadata["result_type"] = type(result).__name__
            if hasattr(result, '__len__'):
                metadata["result_length"] = len(result)
        
        return self.results[-1]
    
    def benchmark_decorator(self, operation_name: Optional[str] = None):
        """Decorator for automatic function benchmarking"""
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                op_name = operation_name or f"{func.__module__}.{func.__name__}"
                metadata = {
                    "function_name": func.__name__,
                    "args_count": len(args),
                    "kwargs_count": len(kwargs)
                }
                
                with self.measure_operation(op_name, metadata):
                    return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def measure_command_execution(self, command_name: str, execution_func: Callable) -> BenchmarkResult:
        """Measure command execution with specialized metadata"""
        metadata = {
            "command_name": command_name,
            "measurement_type": "command_execution"
        }
        
        with self.measure_operation(f"command.{command_name}", metadata):
            result = execution_func()
            
            # Add command-specific metadata
            if isinstance(result, dict):
                metadata.update({
                    "result_keys": list(result.keys()) if result else [],
                    "result_size": len(str(result))
                })
            elif isinstance(result, (list, tuple)):
                metadata["result_count"] = len(result)
        
        return self.results[-1]
    
    def get_summary_statistics(self) -> Dict[str, Any]:
        """Generate summary statistics from all benchmark results"""
        if not self.results:
            return {"error": "No benchmark results available"}
        
        durations = [r.duration_seconds for r in self.results]
        memory_peaks = [r.memory_peak_mb for r in self.results]
        cpu_usage = [r.cpu_percent for r in self.results]
        
        return {
            "total_operations": len(self.results),
            "duration_stats": {
                "min_seconds": min(durations),
                "max_seconds": max(durations),
                "avg_seconds": sum(durations) / len(durations),
                "total_seconds": sum(durations)
            },
            "memory_stats": {
                "min_peak_mb": min(memory_peaks),
                "max_peak_mb": max(memory_peaks),
                "avg_peak_mb": sum(memory_peaks) / len(memory_peaks)
            },
            "cpu_stats": {
                "min_percent": min(cpu_usage),
                "max_percent": max(cpu_usage),
                "avg_percent": sum(cpu_usage) / len(cpu_usage)
            },
            "operations": list(set(r.operation for r in self.results))
        }
    
    def save_results(self, filename: Optional[str] = None) -> str:
        """Save benchmark results to JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"benchmark_results_{timestamp}.json"
        
        filepath = os.path.join(self.results_dir, filename)
        
        data = {
            "benchmark_session": {
                "timestamp": datetime.now().isoformat(),
                "total_operations": len(self.results),
                "summary": self.get_summary_statistics()
            },
            "results": [result.to_dict() for result in self.results]
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        return filepath
    
    def load_results(self, filepath: str) -> bool:
        """Load benchmark results from JSON file"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            self.results = []
            for result_dict in data.get("results", []):
                result = BenchmarkResult(**result_dict)
                self.results.append(result)
            
            return True
        except (FileNotFoundError, json.JSONDecodeError, TypeError) as e:
            print(f"Error loading results: {e}")
            return False
    
    def clear_results(self):
        """Clear all stored benchmark results"""
        self.results.clear()
    
    def compare_operations(self, operation1: str, operation2: str) -> Dict[str, Any]:
        """Compare performance between two operations"""
        op1_results = [r for r in self.results if r.operation == operation1]
        op2_results = [r for r in self.results if r.operation == operation2]
        
        if not op1_results or not op2_results:
            return {"error": "One or both operations not found in results"}
        
        op1_avg_duration = sum(r.duration_seconds for r in op1_results) / len(op1_results)
        op2_avg_duration = sum(r.duration_seconds for r in op2_results) / len(op2_results)
        
        op1_avg_memory = sum(r.memory_peak_mb for r in op1_results) / len(op1_results)
        op2_avg_memory = sum(r.memory_peak_mb for r in op2_results) / len(op2_results)
        
        return {
            "operation1": operation1,
            "operation2": operation2,
            "duration_comparison": {
                "op1_avg_seconds": op1_avg_duration,
                "op2_avg_seconds": op2_avg_duration,
                "speedup_factor": op2_avg_duration / op1_avg_duration if op1_avg_duration > 0 else 0,
                "faster_operation": operation1 if op1_avg_duration < op2_avg_duration else operation2
            },
            "memory_comparison": {
                "op1_avg_mb": op1_avg_memory,
                "op2_avg_mb": op2_avg_memory,
                "memory_difference_mb": abs(op1_avg_memory - op2_avg_memory),
                "more_efficient": operation1 if op1_avg_memory < op2_avg_memory else operation2
            }
        }


class CachePerformanceTracker:
    """Track cache hit ratios and performance"""
    
    def __init__(self):
        self.hits = 0
        self.misses = 0
        self.total_requests = 0
        self.hit_times: List[float] = []
        self.miss_times: List[float] = []
    
    def record_hit(self, duration: float):
        """Record a cache hit with duration"""
        self.hits += 1
        self.total_requests += 1
        self.hit_times.append(duration)
    
    def record_miss(self, duration: float):
        """Record a cache miss with duration"""
        self.misses += 1
        self.total_requests += 1
        self.miss_times.append(duration)
    
    def get_hit_ratio(self) -> float:
        """Calculate cache hit ratio"""
        if self.total_requests == 0:
            return 0.0
        return self.hits / self.total_requests
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Get comprehensive cache performance statistics"""
        hit_ratio = self.get_hit_ratio()
        
        avg_hit_time = sum(self.hit_times) / len(self.hit_times) if self.hit_times else 0.0
        avg_miss_time = sum(self.miss_times) / len(self.miss_times) if self.miss_times else 0.0
        
        return {
            "hit_ratio": hit_ratio,
            "hit_ratio_percent": hit_ratio * 100,
            "total_requests": self.total_requests,
            "hits": self.hits,
            "misses": self.misses,
            "performance": {
                "avg_hit_time_seconds": avg_hit_time,
                "avg_miss_time_seconds": avg_miss_time,
                "cache_speedup_factor": avg_miss_time / avg_hit_time if avg_hit_time > 0 else 0.0
            }
        }
    
    def reset(self):
        """Reset all tracking data"""
        self.hits = 0
        self.misses = 0
        self.total_requests = 0
        self.hit_times.clear()
        self.miss_times.clear()


# Global benchmarker instance
benchmarker = PerformanceBenchmarker()
cache_tracker = CachePerformanceTracker()


# Convenience functions for easy usage
def benchmark_operation(operation_name: str, metadata: Optional[Dict[str, Any]] = None):
    """Convenience function to get measurement context manager"""
    return benchmarker.measure_operation(operation_name, metadata)


def benchmark_function_call(func: Callable, *args, **kwargs) -> BenchmarkResult:
    """Convenience function to benchmark a function call"""
    return benchmarker.benchmark_function(func, *args, **kwargs)


def save_benchmark_results(filename: Optional[str] = None) -> str:
    """Convenience function to save benchmark results"""
    return benchmarker.save_results(filename)


def get_performance_summary() -> Dict[str, Any]:
    """Convenience function to get performance summary"""
    return benchmarker.get_summary_statistics()


def clear_benchmark_results():
    """Convenience function to clear benchmark results"""
    benchmarker.clear_results()