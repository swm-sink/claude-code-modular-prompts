# /error report - Error Reporting Command

**Purpose**: Generate comprehensive error analysis reports with trends, classifications, and actionable insights.

## Usage
```bash
/error report [--timeframe=<timeframe>] [--format=<format>]
```

## Workflow

The `/error report` command follows a systematic process to generate error reports.

```xml
<error_report_workflow>
  <step name="Gather Error Data">
    <description>Gather error data from various sources, including logging platforms, monitoring tools, and version control history. The timeframe for the report can be specified with the `--timeframe` flag.</description>
    <tool_usage>
      <tool>API/Log Reader</tool>
      <description>Fetch error data from logging services and parse log files.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze & Classify Errors">
    <description>Analyze the gathered data to identify trends, classify errors by type (e.g., syntax, runtime, logic), and calculate key metrics such as error frequency and resolution time.</description>
    <tool_usage>
      <tool>Data Analysis</tool>
      <description>Use data analysis techniques to process the error data.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Report">
    <description>Generate a comprehensive report that summarizes the findings. The format of the report can be specified with the `--format` flag (e.g., 'summary', 'dashboard', 'detailed'). The report includes actionable insights and recommendations for improving code quality.</description>
    <output>A detailed error report.</output>
  </step>
</error_report_workflow>
```

## Configuration

The `/error report` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/error report">
  <setting name="default_timeframe" value="7d" description="The default timeframe for error reports (e.g., '7d' for 7 days)." />
  <setting name="default_format" value="summary" description="The default format for error reports." />
</command>
```

## Use Cases

*   **Quality Assurance**: Track and analyze error trends to improve overall code quality.
*   **Team Management**: Identify areas where developers may need additional training or support.
*   **Project Planning**: Use error data to inform decisions about technical debt and refactoring priorities.