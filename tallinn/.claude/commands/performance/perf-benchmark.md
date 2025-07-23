---
name: /perf-benchmark
description: Performance benchmarking with comprehensive metrics collection and analysis
usage: /perf-benchmark [benchmark_type] [duration]
tools: Read, Write, Edit, Bash, Grep
---

# Performance benchmarking with comprehensive metrics collection and analysis

**Usage**: `/perf-benchmark $TARGET $COMPARE_TO`

## Key Arguments

- **$TARGET** (required): The specific file, function, or class to benchmark.
- **$COMPARE_TO** (optional): The git branch to compare the performance results against.

## Examples

```bash
/perf benchmark "src/utils/processing.js:processData"
```
*Benchmark the main 'processData' function and compare its performance against the 'main' branch.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/reporting/generate-structured-report.md
 components/performance/benchmark-harness.md
 components/analysis/performance-metrics.md
 components/testing/load-testing.md
 components/visualization/performance-charts.md
 
 You are a performance engineer. The user wants to run a benchmark.

 1. **Identify Target**: Locate the `target` file or function to be benchmarked.
 2. **Read Configuration**: Read `PROJECT_CONFIG.xml` to find the project's benchmarking tool and configuration.
 3. **Generate Benchmark Harness**:
 * Create a new benchmark test file.
 * Write the necessary setup code to run the target function within the benchmark tool's harness.
 * Include scenarios for different data sizes (e.g., small, medium, large) to get a comprehensive profile.
 4. **Execute Benchmarks**:
 * Run the benchmark for the current code.
 * If `compare_to` is provided, switch to that branch and run the same benchmark to establish a baseline.
 5. **Generate Report**:
 * Create a detailed report comparing the performance.
 * Highlight any significant regressions or improvements in execution time, memory usage, etc.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

