---
name: /perf-report
description: Performance reporting with comprehensive metrics, trends, and recommendations
usage: /perf-report [report_type] [time_period]
tools: Read, Write, Edit, Bash, Grep
---

# Performance reporting with comprehensive metrics, trends, and recommendations

**Usage**: `/perf-report $TIMEFRAME`

## Key Arguments

- **$TIMEFRAME** (optional): The time window for the report (e.g., '24h', '7d', '30d').

## Examples

```bash
/perf report
```
*Generate a performance report for the last 7 days.*

```bash
/perf report timeframe="30d"
```
*Generate a performance report for the last 30 days.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/reporting/generate-structured-report.md
 components/analysis/trend-analysis.md
 components/visualization/performance-charts.md
 components/analysis/performance-metrics.md
 components/optimization/recommendation-engine.md
 
 You are a performance analyst. The user wants a report on application performance.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured monitoring and benchmarking data sources.
 2. **Gather Performance Data**:
 * Fetch performance data (e.g., response times, throughput, error rates) from the configured services for the specified `timeframe`.
 * Incorporate data from recent benchmark runs.
 3. **Analyze and Identify Trends**:
 * Analyze the data to identify performance trends, patterns, and anomalies.
 * Compare the current performance against historical baselines.
 4. **Generate Report**:
 * Create a comprehensive report with clear visualizations of key performance metrics.
 * Highlight any significant performance regressions or improvements.
 * Provide actionable recommendations for optimization.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

