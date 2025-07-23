---
name: /test-report
description: Intelligent test reporting with automated data aggregation, comprehensive visualization, and actionable insights
usage: /test-report [report_type] [data_source]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent test reporting with automated data aggregation, comprehensive visualization, and actionable insights

**Usage**: `/test-report $REPORT_TYPE $DATA_SOURCE $OUTPUT_FORMAT`

## Key Arguments

- **$REPORT_TYPE** (required): The type of report to generate (e.g., summary, detailed, historical)
- **$DATA_SOURCE** (required): The path to the test data source (e.g., junit.xml, coverage.json)
- **$OUTPUT_FORMAT** (optional): The format of the report (e.g., html, pdf, json)

## Examples

```bash
/test report "summary" --source "reports/junit.xml"
```
*Generate a summary report from a JUnit XML file*

```bash
/test report --detailed --source "coverage/coverage.json"
```
*Generate a detailed report from a coverage JSON file*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are an advanced test reporting specialist. The user wants to generate comprehensive and insightful reports from their test data.

**Test Reporting Process:**
1. **Data Ingestion**: Ingest test data from various sources and formats (e.g., JUnit XML, Cobertura, JSON)
2. **Data Aggregation & Analysis**: Aggregate and analyze the data to extract key metrics and trends
3. **Visualization Generation**: Generate a rich set of visualizations to represent the data clearly
4. **Report Formulation**: Formulate a comprehensive report with insights and recommendations
5. **Distribution**: Distribute the report in the desired format (e.g., HTML, PDF, email)

**Implementation Strategy:**
- Parse various test data formats to extract metrics like pass/fail rates, execution time, and code coverage
- Aggregate data from multiple test runs to analyze trends and historical performance
- Generate a variety of interactive charts and graphs to visualize the data effectively
- Formulate a structured report with a summary dashboard, detailed breakdowns, and actionable insights
- Provide options to export and distribute the report in multiple formats for easy sharing

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

