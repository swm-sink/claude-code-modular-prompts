# /analyze performance - Performance Analysis Command

## Purpose
Comprehensive performance bottleneck analysis and optimization recommendations for code, systems, and applications.

## Usage
```bash
/analyze performance [target] [--depth=shallow|deep] [--focus=time|memory|io]
```

## Core Analysis Areas

### 🔍 Bottleneck Detection
- **Algorithmic complexity**: Time/space complexity analysis (O(n), O(n²), etc.)
- **Hot paths**: Identify CPU-intensive code sections
- **Memory leaks**: Track object lifecycle and allocation patterns
- **I/O blocks**: Database queries, file operations, network calls

### ⚡ Performance Patterns
- **N+1 queries**: Database query optimization opportunities
- **Nested loops**: Unnecessary iteration patterns
- **Synchronous operations**: Blocking vs async opportunities
- **Resource contention**: Lock conflicts, thread safety issues

### 📊 Metrics Analysis
- **Response times**: P50, P95, P99 latency measurements
- **Throughput**: Requests per second, operations per minute
- **Resource utilization**: CPU, memory, disk, network usage
- **Scaling characteristics**: Performance under load

## Optimization Recommendations

### Code-Level Optimizations
- Algorithm improvements (e.g., O(n²) → O(n log n))
- Caching strategies (memoization, Redis, CDN)
- Lazy loading and pagination
- Connection pooling and resource reuse

### Architecture Optimizations
- Database indexing strategies
- Query optimization and denormalization
- Microservice boundaries and communication
- Event-driven vs synchronous patterns

### Infrastructure Optimizations
- Horizontal vs vertical scaling recommendations
- Load balancing and traffic distribution
- CDN and edge computing opportunities
- Container and serverless optimizations

## Output Format
- **Performance bottlenecks** (ranked by impact)
- **Quick wins** (high-impact, low-effort improvements)
- **Code examples** (before/after optimizations)
- **Benchmarking recommendations** (how to measure improvements)