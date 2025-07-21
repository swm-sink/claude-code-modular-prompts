---
description: Intelligent test reporting with automated data aggregation, comprehensive visualization, and actionable insights
argument-hint: "[report_type] [data_source]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /test report - Intelligent Test Reporting

Advanced test reporting system with automated data aggregation from various testing tools, comprehensive visualizations, and actionable insights to improve quality.

## Usage
```bash
/test report "summary" --source "junit.xml"  # Generate a summary report from a JUnit XML file
/test report --detailed --source "coverage.json" # Generate a detailed report from a coverage JSON file
/test report --historical "last_7_days"      # Generate a historical test report for the last 7 days
```

<command_file>
  <metadata>
    <n>/test report</n>
    <purpose>Intelligent test reporting with automated data aggregation, comprehensive visualization, and actionable insights</purpose>
    <usage>
      <![CDATA[
      /test report "[report_type]" --source "[data_source]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="report_type" type="string" required="true" default="summary">
      <description>The type of report to generate (e.g., summary, detailed, historical)</description>
    </argument>
    <argument name="data_source" type="string" required="true">
      <description>The path to the test data source (e.g., junit.xml, coverage.json)</description>
    </argument>
    <argument name="output_format" type="string" required="false" default="html">
      <description>The format of the report (e.g., html, pdf, json)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Generate a summary report from a JUnit XML file</description>
      <usage>/test report "summary" --source "reports/junit.xml"</usage>
    </example>
    <example>
      <description>Generate a detailed report from a coverage JSON file</description>
      <usage>/test report --detailed --source "coverage/coverage.json"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
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

<include component="components/reporting/generate-structured-report.md" />
<include component="components/analytics/business-intelligence.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
      <component>components/analytics/business-intelligence.md</component>
    </includes_components>
    <uses_config_values>
      <value>reporting.default_format</value>
      <value>reporting.distribution.channels</value>
    </uses_config_values>
  </dependencies>
</command_file>

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