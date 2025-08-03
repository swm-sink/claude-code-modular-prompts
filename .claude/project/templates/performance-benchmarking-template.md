# Performance Benchmarking Template

## Benchmark Overview
- **Component/Command**: [Name of component or command being benchmarked]
- **Benchmark Type**: [Command Execution / Component Loading / Integration Workflow]
- **Test Environment**: [OS, Claude Code version, hardware specs]
- **Benchmark Date**: [YYYY-MM-DD]
- **Baseline Version**: [Previous version for comparison]

## Performance Requirements

### ✅ Target Performance Standards
- **Command Load Time**: < 2 seconds (target), < 5 seconds (acceptable)
- **Command Execution Time**: < 30 seconds (typical), < 120 seconds (complex)
- **Component Load Time**: < 500ms (target), < 1 second (acceptable)
- **Memory Usage**: < 100MB (typical), < 500MB (complex workflows)
- **Prompt Token Size**: < 10k tokens (recommended), < 25k tokens (maximum)

### ✅ Benchmark Scenarios
- **Light Load**: Minimal input, basic functionality
- **Normal Load**: Typical real-world usage patterns
- **Heavy Load**: Large inputs, complex operations
- **Stress Load**: Maximum reasonable usage scenarios

## Benchmark Setup

### ✅ Environment Configuration
```bash
# System Information
echo "=== System Benchmark Environment ==="
echo "OS: $(uname -a)"
echo "Memory: $(free -h 2>/dev/null || echo 'N/A')"
echo "CPU: $(nproc 2>/dev/null || echo 'N/A') cores"
echo "Claude Code Version: $(claude --version 2>/dev/null || echo 'Unknown')"

# Clean Environment Setup
echo "=== Preparing Clean Environment ==="
# Clear Claude Code caches
# Reset memory usage baselines  
# Ensure consistent starting state
```

### ✅ Baseline Measurements
```bash
# Measure system baseline before testing
echo "=== Establishing Baseline Metrics ==="

# Memory baseline
echo "Measuring memory baseline..."
# Record initial memory usage
# Record Claude Code memory footprint

# Performance baseline  
echo "Measuring performance baseline..."
# Record system load
# Record available resources
```

## Performance Test Cases

### Test Case 1: Component Loading Performance
```bash
# Test: Measure component loading time and resource usage
echo "=== Component Loading Performance Test ==="

# Test 1.1: Individual Component Loading
echo "Testing individual component loading..."
for component in [list of components]; do
    echo "Testing component: $component"
    
    # Measure load time
    start_time=$(date +%s.%N)
    # Load component (simulation)
    end_time=$(date +%s.%N)
    load_time=$(echo "$end_time - $start_time" | bc)
    
    echo "Component $component load time: ${load_time}s"
    
    # Measure memory impact
    # Record token size impact
    # Record any error conditions
done

# Test 1.2: Multiple Component Loading
echo "Testing multiple component loading..."
# Test loading multiple components simultaneously
# Measure total time vs sum of individual times
# Check for any performance degradation
```

### Test Case 2: Command Execution Performance  
```bash
# Test: Measure command execution time across different scenarios
echo "=== Command Execution Performance Test ==="

# Test 2.1: Light Load Scenario
echo "Testing light load scenario..."
command_name="/test-command"
input_size="small"

start_time=$(date +%s.%N)
# Execute command with minimal input
end_time=$(date +%s.%N)
execution_time=$(echo "$end_time - $start_time" | bc)

echo "Light load execution time: ${execution_time}s"

# Test 2.2: Normal Load Scenario
echo "Testing normal load scenario..."
# Execute command with typical input
# Measure execution time
# Record memory usage during execution

# Test 2.3: Heavy Load Scenario  
echo "Testing heavy load scenario..."
# Execute command with large input
# Measure execution time
# Monitor resource usage throughout execution

# Test 2.4: Stress Load Scenario
echo "Testing stress load scenario..."
# Execute command with maximum reasonable input
# Measure execution time and resource usage
# Check for memory leaks or performance degradation
```

### Test Case 3: Memory Usage Analysis
```bash
# Test: Analyze memory usage patterns and efficiency
echo "=== Memory Usage Analysis ==="

# Test 3.1: Memory Growth Testing
echo "Testing memory growth patterns..."
# Execute command multiple times
# Monitor memory usage over time
# Check for memory leaks

# Test 3.2: Peak Memory Usage
echo "Testing peak memory usage..."
# Monitor memory usage during heaviest operations
# Record peak memory consumption
# Verify memory is released properly

# Test 3.3: Memory Efficiency
echo "Testing memory efficiency..."
# Compare memory usage to input size
# Calculate memory efficiency ratios
# Identify memory optimization opportunities
```

### Test Case 4: Scalability Testing
```bash
# Test: Measure performance scaling with increased load
echo "=== Scalability Testing ==="

# Test 4.1: Input Size Scaling
echo "Testing input size scaling..."
for size in small medium large xlarge; do
    echo "Testing with input size: $size"
    
    # Measure execution time for each size
    # Record memory usage for each size
    # Calculate performance scaling ratios
done

# Test 4.2: Concurrent Usage Scaling
echo "Testing concurrent usage scaling..."
for concurrent in 1 2 4 8; do
    echo "Testing with $concurrent concurrent executions..."
    
    # Run multiple instances simultaneously
    # Measure total time and individual times
    # Monitor resource contention
done
```

### Test Case 5: Network and I/O Performance
```bash
# Test: Measure network and file I/O performance impact
echo "=== Network and I/O Performance Test ==="

# Test 5.1: File I/O Performance
echo "Testing file I/O performance..."
# Test reading/writing various file sizes
# Measure I/O throughput
# Test with different file types

# Test 5.2: Network Performance (if applicable)
echo "Testing network performance..."
# Test API calls or web requests
# Measure network latency impact
# Test with various network conditions
```

## Claude Code Specific Benchmarks

### ✅ Token Usage Optimization
```bash
# Test: Measure and optimize token usage
echo "=== Token Usage Benchmarking ==="

# Measure prompt token size
echo "Measuring prompt token size..."
# Count tokens in command prompt
# Count tokens in included components
# Calculate total token overhead

# Measure token efficiency
echo "Measuring token efficiency..."
# Calculate functionality per token
# Identify token optimization opportunities
# Test token reduction strategies
```

### ✅ Context Loading Performance
```bash
# Test: Measure context loading and management performance  
echo "=== Context Loading Performance ==="

# Test different context sizes
echo "Testing context loading with various sizes..."
# Test with minimal context
# Test with typical context load
# Test with maximum context load

# Measure context processing time
echo "Measuring context processing overhead..."
# Time context parsing and loading
# Measure memory usage for context
# Test context caching effectiveness
```

## Performance Analysis

### ✅ Performance Metrics Collection

**Timing Metrics**
- **Load Time**: [X.XX seconds]
- **Execution Time**: [X.XX seconds]  
- **Total Response Time**: [X.XX seconds]
- **95th Percentile Response Time**: [X.XX seconds]

**Resource Metrics**
- **Peak Memory Usage**: [XXX MB]
- **Average Memory Usage**: [XXX MB]
- **Memory Efficiency**: [XX% of peak]
- **CPU Usage**: [XX% average, XX% peak]

**Scalability Metrics**
- **Throughput**: [XX operations/second]
- **Concurrent Performance**: [X:XX ratio]
- **Input Size Scaling**: [linear/sublinear/supralinear]
- **Resource Scaling**: [linear/sublinear/supralinear]

**Quality Metrics**
- **Token Efficiency**: [XX functionality units per token]
- **Prompt Token Count**: [XXXX tokens]
- **Context Load Impact**: [XX% overhead]
- **Error Rate**: [X.XX%]

### ✅ Performance Comparison

**vs. Baseline Performance**
| Metric | Baseline | Current | Change | Status |
|--------|----------|---------|--------|--------|
| Load Time | [X.XX]s | [X.XX]s | [±X%] | ✅/⚠️/❌ |
| Execution Time | [X.XX]s | [X.XX]s | [±X%] | ✅/⚠️/❌ |
| Memory Usage | [XXX]MB | [XXX]MB | [±X%] | ✅/⚠️/❌ |
| Token Count | [XXXX] | [XXXX] | [±X%] | ✅/⚠️/❌ |

**vs. Performance Targets**
| Metric | Target | Actual | Status | Notes |
|--------|--------|--------|--------|-------|
| Load Time | <2s | [X.XX]s | ✅/⚠️/❌ | [notes] |
| Execution Time | <30s | [X.XX]s | ✅/⚠️/❌ | [notes] |
| Memory Usage | <100MB | [XXX]MB | ✅/⚠️/❌ | [notes] |
| Token Count | <10k | [XXXX] | ✅/⚠️/❌ | [notes] |

### ✅ Performance Bottleneck Analysis

**Identified Bottlenecks**
1. **[Bottleneck Name]**: [Description and impact]
   - **Root Cause**: [Analysis of underlying cause]
   - **Impact**: [Performance impact measurement]
   - **Proposed Fix**: [Optimization strategy]

2. **[Bottleneck Name]**: [Description and impact]
   - **Root Cause**: [Analysis of underlying cause]
   - **Impact**: [Performance impact measurement]  
   - **Proposed Fix**: [Optimization strategy]

**Optimization Opportunities**
- **Token Optimization**: [Specific opportunities to reduce token usage]
- **Memory Optimization**: [Opportunities to reduce memory footprint]
- **Execution Optimization**: [Opportunities to improve execution speed]
- **I/O Optimization**: [Opportunities to improve I/O performance]

## Recommendations

### ✅ Immediate Optimizations
1. **[High Priority]**: [Specific optimization with expected impact]
   - **Implementation Effort**: [Low/Medium/High]
   - **Expected Improvement**: [Quantified improvement estimate]
   - **Risk Level**: [Low/Medium/High]

2. **[Medium Priority]**: [Specific optimization with expected impact]
   - **Implementation Effort**: [Low/Medium/High]
   - **Expected Improvement**: [Quantified improvement estimate]
   - **Risk Level**: [Low/Medium/High]

### ✅ Long-term Performance Strategy
- **Architecture Changes**: [Structural changes for better performance]
- **Technology Upgrades**: [Tools or approaches for improvement]
- **Monitoring Strategy**: [Ongoing performance monitoring approach]
- **Performance Budget**: [Performance targets for future features]

### ✅ Performance Acceptance Criteria
- [ ] **Load Time**: Meets target performance requirements
- [ ] **Execution Time**: Acceptable for intended use cases
- [ ] **Memory Usage**: Within reasonable resource bounds
- [ ] **Scalability**: Performs well under expected load
- [ ] **Token Efficiency**: Optimized for Claude Code usage

## Final Assessment

### ✅ Performance Rating
- [ ] **EXCELLENT** - Exceeds performance targets significantly
- [ ] **GOOD** - Meets all performance targets comfortably
- [ ] **ACCEPTABLE** - Meets minimum performance requirements
- [ ] **NEEDS IMPROVEMENT** - Some performance issues need addressing
- [ ] **UNACCEPTABLE** - Major performance issues block usage

### ✅ Performance Approval
- [ ] **APPROVED** - Performance meets production standards
- [ ] **CONDITIONAL** - Performance approved with optimizations required
- [ ] **REJECTED** - Performance requires significant improvement

### ✅ Monitoring and Maintenance
- **Performance Monitoring**: [Ongoing monitoring strategy]
- **Regression Testing**: [Performance regression prevention]
- **Optimization Schedule**: [Regular optimization review schedule]
- **Next Benchmark Date**: [YYYY-MM-DD]

### ✅ Benchmark Archive
- **Test Data**: [Location of performance test data]
- **Benchmark Scripts**: [Location of benchmark automation]
- **Results Archive**: [Location of historical results]
- **Analysis Reports**: [Location of detailed analysis]