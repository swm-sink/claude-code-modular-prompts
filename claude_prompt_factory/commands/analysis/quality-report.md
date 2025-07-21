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