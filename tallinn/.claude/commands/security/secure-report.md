---
name: /secure-report
description: Comprehensive security reporting with metrics, compliance status, and remediation tracking
usage: /secure-report [report_type] [format]
tools: Read, Write, Edit, Bash, Grep
---

# Comprehensive security reporting with metrics, compliance status, and remediation tracking

**Usage**: `/secure-report $TIMEFRAME`

## Key Arguments

- **$TIMEFRAME** (optional): The time window for the report (e.g., '7d', '30d', '90d').

## Examples

```bash
/secure report
```
*Generate a security report for the last 30 days.*

```bash
/secure report timeframe="90d"
```
*Generate a security report for the last quarter.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/reporting/generate-structured-report.md
 components/security/metrics-calculation.md
 components/analysis/trend-analysis.md
 components/visualization/security-dashboards.md
 components/quality/compliance-tracking.md
 
 You are a security analyst. The user wants a comprehensive report on the project's security posture.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured security scanning and monitoring service integrations.
 2. **Gather Security Data**:
 * Fetch vulnerability and compliance data from the configured services for the specified `timeframe`.
 * Incorporate results from recent `/secure scan` and `/secure audit` runs.
 3. **Analyze and Synthesize**:
 * Analyze the data to identify security trends (e.g., new vs. fixed vulnerabilities).
 * Calculate key metrics like risk scores, time-to-remediate, and compliance status.
 * Identify the highest-risk vulnerabilities that need immediate attention.
 4. **Generate Report**:
 * Create a detailed security report with clear visualizations.
 * Include a prioritized list of actionable recommendations.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

