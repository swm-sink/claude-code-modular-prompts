# /quality metrics - Quality Metrics Command

**Purpose**: Calculate and track code quality metrics, with support for trend analysis and comparison against benchmarks.

## Usage
```bash
/quality metrics [scope]
```

## Workflow

The `/quality metrics` command follows a systematic process to calculate and analyze code quality metrics.

```xml
<metrics_workflow>
  <step name="Analyze Codebase">
    <description>Perform a comprehensive analysis of the codebase to calculate a wide range of quality metrics, including code complexity, maintainability, test coverage, and technical debt.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase to collect all necessary data for metric calculation.</description>
    </tool_usage>
  </step>
  
  <step name="Perform Trend Analysis">
    <description>Compare the current metrics against historical data to identify trends and track the impact of recent changes on code quality.</description>
  </step>
  
  <step name="Compare Against Benchmarks">
    <description>Compare the project's quality metrics against industry standards and the team's own baseline to provide context and identify areas for improvement.</description>
  </step>
  
  <step name="Generate Report">
    <description>Generate a detailed report of the quality metrics, including trend analysis, benchmark comparisons, and a set of actionable recommendations for improvement.</description>
    <output>A comprehensive quality metrics report.</output>
  </step>
</metrics_workflow>
```

## Quality Metrics

The following quality metrics are calculated:

*   **Code Quality**: Cyclomatic complexity, maintainability index, readability score, and test coverage.
*   **Technical Debt**: Technical debt ratio, code smells, duplication percentage, and security vulnerabilities.