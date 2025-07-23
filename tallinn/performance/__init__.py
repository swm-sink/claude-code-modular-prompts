"""
Real Performance Monitoring System

This package provides transparent, measurable performance monitoring
with real metrics instead of fabricated claims.

Key Components:
- benchmarker: Core measurement capabilities using psutil
- monitor: Prometheus metrics integration for system observability
- context_optimizer: Measurable context window optimization

All metrics are based on actual system measurements.
"""

from .benchmarker import (
    PerformanceBenchmarker,
    BenchmarkResult,
    CachePerformanceTracker,
    benchmarker,
    cache_tracker,
    benchmark_operation,
    benchmark_function_call,
    save_benchmark_results,
    get_performance_summary,
    clear_benchmark_results
)

from .monitor import (
    PrometheusPerformanceMonitor,
    SystemMetrics,
    MetricsCollector,
    monitor,
    start_performance_monitoring,
    stop_performance_monitoring,
    measure_command_execution,
    get_performance_summary as get_monitoring_summary,
    record_cache_hit_ratio,
    export_prometheus_metrics
)

from .context_optimizer import (
    ContextWindowOptimizer,
    CompressionResult,
    context_optimizer,
    optimize_text,
    adaptive_optimize,
    get_compression_stats,
    benchmark_techniques,
    export_performance_report
)

# Version information
__version__ = "1.0.0"
__author__ = "Claude Code Performance Team"
__description__ = "Real performance monitoring with transparent measurements"

# Global instances for easy access
__all__ = [
    # Classes
    "PerformanceBenchmarker",
    "BenchmarkResult", 
    "CachePerformanceTracker",
    "PrometheusPerformanceMonitor",
    "SystemMetrics",
    "MetricsCollector",
    "ContextWindowOptimizer",
    "CompressionResult",
    
    # Global instances
    "benchmarker",
    "cache_tracker", 
    "monitor",
    "context_optimizer",
    
    # Convenience functions
    "benchmark_operation",
    "benchmark_function_call",
    "save_benchmark_results",
    "get_performance_summary",
    "clear_benchmark_results",
    "start_performance_monitoring",
    "stop_performance_monitoring",
    "measure_command_execution",
    "get_monitoring_summary",
    "record_cache_hit_ratio",
    "export_prometheus_metrics",
    "optimize_text",
    "adaptive_optimize",
    "get_compression_stats",
    "benchmark_techniques",
    "export_performance_report",
]

# Module metadata
TRANSPARENCY_STATEMENT = """
All performance metrics provided by this module are based on real, 
measurable system operations. No fabricated or estimated claims.

Measurement methods:
- Execution times: actual time.time() measurements
- Memory usage: psutil process RSS monitoring  
- CPU usage: psutil CPU percentage measurements
- Cache performance: real hit/miss ratio tracking
- Context compression: measured text processing results
- System monitoring: continuous resource tracking

Every metric can be independently verified and reproduced.
"""