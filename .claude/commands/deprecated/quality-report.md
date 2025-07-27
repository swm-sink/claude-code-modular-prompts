---
name: /quality-report
description: Advanced quality reporting with intelligent metrics, trend analysis, and automated improvement recommendations
argument-hint: "[report_scope] [metrics_focus]"
allowed-tools: Read, Write, Edit, Bash, Grep
# DEPRECATION METADATA
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/quality report"
reason: "Consolidated into unified /quality command for better UX and maintainability"
migration_deadline: "2025-08-25"
---
# ⚠️ DEPRECATED: /quality-report

**This command is deprecated and will be removed on 2025-08-25.**

## Migration Path
This functionality has been consolidated into the unified `/quality` command:

### Old Usage → New Usage
```bash
# OLD (deprecated)
/analyze quality-report comprehensive     # Comprehensive quality report
/analyze quality-report --trends          # Quality trend analysis
/analyze quality-report --metrics         # Detailed metrics analysis
/analyze quality-report --recommendations # Automated improvement suggestions

# NEW (recommended)
/quality report --format detailed        # Comprehensive quality report
/quality report --dashboard              # Interactive quality dashboard  
/quality report --format html            # HTML quality report
/quality report --format pdf --output "quality.pdf"  # Export PDF report
/quality all                             # Complete analysis with report
```

### Migration Benefits
- **Multiple Formats**: HTML, PDF, JSON, Dashboard exports
- **Interactive Dashboards**: Real-time quality visualization
- **Integrated Analysis**: Combines review, metrics, and suggestions
- **Custom Output**: Specify output files and formats
- **Executive Summaries**: High-level quality status reports

### Advanced Reporting Features
```bash
# Advanced reporting with trend analysis
/quality report --dashboard --trend      # Dashboard with historical trends
/quality report --format json --output "metrics.json"  # Export data
/quality all --format pdf --output "full-report.pdf"   # Complete analysis
```

### Report Format Options
- `summary`: Quick overview (default)
- `detailed`: Comprehensive findings
- `html`: Interactive web report
- `pdf`: Professional document
- `json`: Machine-readable data
- `dashboard`: Interactive visualization

### Quick Migration Guide
1. Replace `/analyze quality-report` with `/quality report`
2. Add `--format` flag to specify output format
3. Use `--dashboard` for interactive visualizations
4. Add `--output filename` to save reports
5. Use `/quality all` for comprehensive analysis with reporting

For detailed usage examples, see `/quality --help` or the [Quality Command Documentation](.claude/commands/quality/quality.md).

---

# /analyze quality-report - Advanced Quality Reporting (LEGACY)
Sophisticated quality reporting system with intelligent metrics, trend analysis, and automated improvement recommendations.
## Usage
```bash
/analyze quality-report comprehensive        # Comprehensive quality report
/analyze quality-report --trends             # Quality trend analysis
/analyze quality-report --metrics            # Detailed metrics analysis
/analyze quality-report --recommendations    # Automated improvement suggestions
```
<command_file>
  <metadata>
    <n>/analyze quality-report</n>
    <purpose>Advanced quality reporting with intelligent metrics, trend analysis, and automated improvement recommendations</purpose>
    <usage>
      <![CDATA[
      /analyze quality-report [report_scope]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="report_scope" type="string" required="false" default="comprehensive">
      <description>Scope of quality report to generate</description>
    </argument>
    <argument name="metrics_focus" type="string" required="false" default="all">
      <description>Focus area for metrics analysis</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Comprehensive quality report</description>
      <usage>/analyze quality-report comprehensive</usage>
    </example>
    <example>
      <description>Quality trend analysis</description>
      <usage>/analyze quality-report --trends</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>
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
<include component="components/quality/quality-metrics.md" />
<include component="components/analytics/business-intelligence.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/quality/quality-metrics.md</component>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>quality.metrics.thresholds</value>
      <value>reporting.quality.format</value>
    </uses_config_values>
  </dependencies>
</command_file>