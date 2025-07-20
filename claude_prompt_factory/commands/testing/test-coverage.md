# /test coverage - Test Coverage Analysis Command

**Purpose**: Analyze test coverage, generate comprehensive reports, and track coverage metrics over time.

## Usage
```bash
/test coverage [path] [--threshold=80] [--format=html|json|text]
```

## Workflow

The `/test coverage` command follows a systematic process to analyze and report on test coverage.

```xml
<coverage_analysis_workflow>
  <step name="Discover Code & Tests">
    <description>Identify all source code files and their corresponding test files within the specified path. Also, detect the testing framework in use.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob</tool>
      <description>Scan the project for source code and test files.</description>
    </tool_usage>
  </step>
  
  <step name="Measure Coverage">
    <description>Run the test suite with coverage measurement enabled. Calculate coverage percentages for lines, branches, and functions, and identify uncovered code.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the test command with coverage flags.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Reports & Recommendations">
    <description>Generate detailed coverage reports in the specified format, highlight coverage gaps, and provide actionable recommendations for improving test coverage.</description>
    <output>A comprehensive test coverage report with identified gaps and recommendations.</output>
  </step>
</coverage_analysis_workflow>
```

## Output
- Coverage percentage by file/function.
- Uncovered code identification.
- Trend analysis and threshold compliance.
- Actionable recommendations for improvement.