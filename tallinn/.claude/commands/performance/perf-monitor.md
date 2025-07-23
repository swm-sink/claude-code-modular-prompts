---
name: /perf-monitor
description: Real-time performance monitoring with alerting and automated issue detection
usage: /perf-monitor [monitor_type] [alert_threshold]
tools: Read, Write, Edit, Bash, Grep
---

# Real-time performance monitoring with alerting and automated issue detection

**Usage**: `/perf-monitor $DURATION`

## Key Arguments

- **$DURATION** (optional): The duration for the monitoring session (e.g., '10m', '1h', '6h').

## Examples

```bash
/perf monitor
```
*Monitor the application's performance for one hour.*

```bash
/perf monitor duration="10m"
```
*Run a short 10-minute monitoring session.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/reporting/generate-structured-report.md
 components/monitoring/real-time-monitoring.md
 components/monitoring/alerting-systems.md
 components/analysis/anomaly-detection.md
 components/visualization/performance-dashboards.md
 
 You are a site reliability engineer. The user wants to set up performance monitoring.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured monitoring service integration (e.g., Prometheus, Datadog) and alerting thresholds.
 2. **Generate Setup Plan**:
 * Propose a plan to configure and start a monitoring session for the specified `duration`.
 * The plan should include collecting key metrics (CPU, memory, I/O, latency).
 * It should also include setting up alerts based on the configured thresholds.
 3. **Provide Dashboard/Query**:
 * Generate the configuration or query needed for the monitoring service to display a real-time performance dashboard.
 4. **Generate Report**:
 * After the monitoring session, provide a summary report of the performance, highlighting any anomalies or threshold breaches.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

