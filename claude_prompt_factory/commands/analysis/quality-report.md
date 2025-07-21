---
description: Advanced quality reporting with intelligent metrics, trend analysis, and automated improvement recommendations
argument-hint: "[report_scope] [metrics_focus]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /analyze quality-report - Advanced Quality Reporting

Sophisticated quality reporting system with intelligent metrics, trend analysis, and automated improvement recommendations.

## Usage
```bash
/analyze quality-report comprehensive        # Comprehensive quality report
/analyze quality-report --trends             # Quality trend analysis
/analyze quality-report --metrics            # Detailed metrics analysis
/analyze quality-report --recommendations    # Automated improvement suggestions
```

  <claude_prompt>
    <prompt>
      You are a QA engineering lead. The user wants a comprehensive quality report for their project.
      Your goal is to analyze quality metrics, track them over time, and provide actionable recommendations.

      <include component="components/context/find-relevant-code.md" />

      Once the scope is identified, perform the following analysis:
      1.  **Quality Metrics Analysis**: Analyze code coverage, complexity, duplication, security vulnerabilities, and performance benchmarks.
      2.  **Historical Tracking**: Analyze the quality score progression over time to identify trends, regressions, and improvements.

      Compile all your findings into a detailed report.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>paths.source</value>
    </uses_config_values>
  </dependencies>
</rewritten_file>