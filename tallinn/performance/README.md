# Performance Monitoring System

This directory contains a comprehensive, real performance monitoring system that provides transparent, measurable metrics instead of fabricated claims.

## Overview

The performance monitoring system consists of four main components:

1. **benchmarker.py** - Core measurement capabilities using psutil
2. **monitor.py** - Prometheus metrics integration for real-time monitoring
3. **context_optimizer.py** - Measurable context window optimization techniques
4. **../run_performance_benchmarks.py** - Comprehensive benchmark runner

## Components

### 1. Performance Benchmarker (`benchmarker.py`)

Real-time performance measurement system using psutil for accurate system metrics.

**Features:**
- Actual execution time measurement with microsecond precision
- Real memory usage tracking (RSS memory in MB)
- Peak memory consumption monitoring during operations
- CPU usage percentage measurement
- Context manager for easy operation measurement
- Function decorator for automatic benchmarking
- Results export to JSON format

**Key Classes:**
- `PerformanceBenchmarker` - Main benchmarking class
- `BenchmarkResult` - Container for measurement results
- `CachePerformanceTracker` - Cache hit ratio and performance tracking

**Usage Example:**
```python
from performance.benchmarker import benchmarker

# Using context manager
with benchmarker.measure_operation("my_operation"):
    # Your code here
    result = expensive_function()

# Get summary statistics
stats = benchmarker.get_summary_statistics()
print(f"Average duration: {stats['duration_stats']['avg_seconds']:.4f}s")
```

### 2. Prometheus Monitor (`monitor.py`)

Real-time system monitoring with Prometheus metrics integration.

**Features:**
- System resource monitoring (CPU, memory, disk, network)
- Command execution timing and counting
- Cache performance metrics
- Context compression tracking
- Performance alerting system
- HTTP metrics server for Prometheus integration
- Fallback metrics collector when Prometheus unavailable

**Key Classes:**
- `PrometheusPerformanceMonitor` - Main monitoring class
- `SystemMetrics` - Container for system-level metrics
- `MetricsCollector` - Simplified fallback collector

**Usage Example:**
```python
from performance.monitor import monitor, start_performance_monitoring

# Start background monitoring
start_performance_monitoring()

# Measure command execution
with monitor.measure_command("my_command"):
    # Your command execution here
    process_data()

# Get current metrics
summary = monitor.get_metrics_summary()
```

### 3. Context Optimizer (`context_optimizer.py`)

Real context window optimization with measurable compression techniques.

**Features:**
- Multiple compression techniques with real measurements
- Token count estimation and tracking
- Adaptive compression based on context limits
- Performance benchmarking of compression methods
- Compression history and statistics
- Methodology documentation

**Compression Techniques:**
- Whitespace compression
- Comment removal
- JSON data compression
- Pattern compression (repeated content)
- Intelligent summarization
- Comprehensive (all techniques combined)

**Key Classes:**
- `ContextWindowOptimizer` - Main optimization class
- `CompressionResult` - Container for compression results

**Usage Example:**
```python
from performance.context_optimizer import context_optimizer

# Optimize text with specific technique
result = context_optimizer.optimize_context(text, "comprehensive")
print(f"Compression ratio: {result.compression_ratio:.3f}")
print(f"Tokens saved: {result.tokens_saved}")

# Adaptive compression to fit context limit
compressed_text, result = context_optimizer.adaptive_compression(text, 5000)
```

## Benchmark Runner

The `run_performance_benchmarks.py` script provides comprehensive performance testing:

**Test Categories:**
- Memory operation benchmarks
- Context compression performance
- Cache hit ratio simulation
- Command execution timing
- Parallel vs sequential operation comparison
- System resource monitoring

**Usage:**
```bash
# Run standard benchmarks
python run_performance_benchmarks.py

# Quick benchmark (reduced scope)
python run_performance_benchmarks.py --quick

# Full comprehensive benchmark
python run_performance_benchmarks.py --full
```

**Output:**
- JSON results files with detailed measurements
- Performance summary to console
- Methodology documentation
- System performance alerts

## Real Metrics vs Fabricated Claims

### What This System Provides (Real):
- ✅ Actual execution times measured with `time.time()`
- ✅ Real memory usage via psutil RSS tracking
- ✅ True CPU percentage measurements
- ✅ Genuine cache hit/miss ratios with timing
- ✅ Measured context compression with token counting
- ✅ System resource monitoring with alerts
- ✅ Comparative performance analysis

### What It Replaces (Fabricated):
- ❌ Estimated or theoretical performance gains
- ❌ Hardcoded "expected" metrics
- ❌ Unverifiable claims about efficiency
- ❌ Static performance numbers
- ❌ Simulated cache ratios without measurement

## Methodology

All performance measurements follow these principles:

1. **Transparent Measurement**: Every metric is directly measured from system operations
2. **Reproducible Results**: Benchmarks can be run repeatedly for consistency verification
3. **Real System Impact**: Measurements reflect actual resource usage and timing
4. **Documented Methods**: All measurement techniques are clearly documented
5. **No Fabrication**: All claims are backed by measurable evidence

## Dependencies

- `psutil` - System and process monitoring
- `prometheus-client` - Metrics collection and export (optional)

Install dependencies:
```bash
pip install psutil prometheus-client
```

## Integration

The performance monitoring system is designed to integrate with existing code:

```python
# Import global instances
from performance.benchmarker import benchmarker
from performance.monitor import monitor, start_performance_monitoring  
from performance.context_optimizer import context_optimizer

# Start monitoring
start_performance_monitoring()

# Use in your application
with benchmarker.measure_operation("user_command"):
    with monitor.measure_command("process_request"):
        # Your application code
        optimized_text, compression_result = context_optimizer.adaptive_compression(
            user_input, context_limit=8000
        )
        result = process_request(optimized_text)

# Get comprehensive statistics
performance_stats = benchmarker.get_summary_statistics()
system_metrics = monitor.get_metrics_summary()
compression_stats = context_optimizer.get_compression_statistics()
```

## File Structure

```
performance/
├── README.md                 # This documentation
├── benchmarker.py           # Core measurement capabilities
├── monitor.py               # Prometheus metrics integration
├── context_optimizer.py     # Context window optimization
└── (results/)               # Generated benchmark results (created at runtime)

../run_performance_benchmarks.py  # Comprehensive benchmark runner
```

## Transparency Commitment

This performance monitoring system is built on the principle of transparency. Every measurement is:
- Directly observable
- Reproducible
- Based on real system operations
- Documented with clear methodology
- Free from fabricated or estimated claims

All performance reports generated by this system include methodology notes explaining exactly how each metric was measured.