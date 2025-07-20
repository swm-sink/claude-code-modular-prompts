# /secure report - Security Report Generator

**Purpose**: Generate comprehensive security reports with vulnerability trends, remediation status, and compliance insights for stakeholders.

## Usage
```bash
/secure report [scope] [--format=summary|detailed|json|sarif]
```

## Workflow

The `/secure report` command follows a systematic process to generate detailed security reports.

```xml
<security_report_workflow>
  <step name="Gather Security Data">
    <description>Collect security data from various sources, including vulnerability scans, compliance tools, and incident response systems.</description>
    <tool_usage>
      <tool>Parallel Read</tool>
      <description>Read data from security scan reports, compliance logs, and incident databases.</description>
    </tool_usage>
  </step>
  <step name="Analyze & Synthesize Data">
    <description>Analyze the gathered data to calculate security metrics, identify vulnerability trends, assess compliance status, and identify priority issues.</description>
  </step>
  <step name="Generate Report">
    <description>Generate a comprehensive security report in the specified format, including security metrics, trend analysis, actionable intelligence, and remediation plans.</description>
    <output>A detailed security report.</output>
  </step>
</security_report_workflow>
```

## Report Content

### Security Metrics
- **Vulnerability Count**: Critical, High, Medium, Low severity
- **Risk Score**: CVSS-based organizational risk rating
- **Compliance Status**: OWASP 2025, SOC2, ISO27001 alignment
- **Remediation Rate**: Time-to-fix averages, SLA compliance

### Trend Analysis
- **Vulnerability Trends**: New vs. fixed vulnerabilities over time
- **Attack Surface**: Changes in exposed services and endpoints
- **Compliance Drift**: Deviation from security baselines
- **Team Performance**: Security fix velocity by team/component

### Actionable Intelligence
- **Priority Issues**: Highest-risk vulnerabilities requiring immediate attention
- **Remediation Plans**: Recommended fix sequences and timelines
- **Resource Needs**: Security team capacity and training gaps
- **Policy Updates**: Required security policy changes