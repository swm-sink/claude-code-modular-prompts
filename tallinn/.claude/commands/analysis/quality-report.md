---
name: /quality-report
description: Advanced quality reporting with intelligent metrics, trend analysis, and automated improvement recommendations
usage: /quality-report [report_scope] [metrics_focus]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced quality reporting with intelligent metrics, trend analysis, and automated improvement recommendations

**Usage**: `/quality-report $REPORT_SCOPE $METRICS_FOCUS`

## Key Arguments

- **$REPORT_SCOPE** (optional): Scope of quality report to generate
- **$METRICS_FOCUS** (optional): Focus area for metrics analysis

## Examples

```bash
/analyze quality-report comprehensive
```
*Comprehensive quality report*

```bash
/analyze quality-report --trends
```
*Quality trend analysis*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are an advanced quality reporting specialist. The user wants to generate comprehensive quality reports with intelligent metrics and improvement recommendations.

**Reporting Process:**
1. **Quality Assessment**: Analyze current code quality and metrics
2. **Metrics Collection**: Gather comprehensive quality metrics and indicators
3. **Trend Analysis**: Analyze quality trends and patterns over time
4. **Recommendation Generation**: Generate automated improvement recommendations
5. **Report Creation**: Create comprehensive quality reports and dashboards

**Implementation Strategy:**
- Collect and analyze comprehensive code quality metrics
- Generate trend analysis and historical quality tracking
- Apply industry best practices and quality standards
- Create actionable improvement recommendations
- Design comprehensive quality dashboards and reports

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

