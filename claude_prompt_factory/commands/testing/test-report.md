---
description: Advanced test reporting with intelligent analytics, trend analysis, and comprehensive quality insights
argument-hint: "[report_scope] [analytics_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /test report - Advanced Test Reporting

Sophisticated test reporting system with intelligent analytics, trend analysis, and comprehensive quality insights.

## Usage
```bash
/test report comprehensive                   # Comprehensive test reporting
/test report --trends                        # Test trend analysis
/test report --quality                       # Quality metrics reporting
/test report --analytics                     # Advanced test analytics
```

## Workflow

The `/test report` command follows a systematic process to generate detailed test reports.

```xml
<test_report_workflow>
  <step name="Collect Test Data">
    <description>Collect test execution data from various sources, including unit, integration, and end-to-end test runs, and coverage reports.</description>
    <tool_usage>
      <tool>Parallel Read</tool>
      <description>Read test results and coverage reports.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze & Synthesize Data">
    <description>Analyze the gathered data to calculate test metrics, identify execution time trends, detect flaky tests, and categorize failures.</description>
  </step>
  
  <step name="Generate Report">
    <description>Generate a comprehensive test report in the specified format, including test execution analysis, coverage integration, quality metrics, and detailed failure analysis.</description>
    <output>A detailed test report.</output>
  </step>
</test_report_workflow>
```

## Features

### Test Execution Analysis
- Pass/fail rates by test type and module.
- Test execution time trends and outliers.
- Flaky test identification and patterns.
- Performance regression detection.

### Coverage Integration
- Coverage percentage by test suite.
- Coverage trend analysis over time.
- Gap identification with priority scoring.
- Branch and line coverage breakdown.

### Quality Metrics
- Test code quality assessment.
- Test maintenance burden analysis.
- Assertion strength evaluation.
- Test isolation and dependency analysis.

### Failure Analysis
- Root cause categorization.
- Failure pattern identification.
- Environment-specific failure tracking.
- Recovery time metrics.