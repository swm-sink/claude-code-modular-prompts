---
description: Intelligent cost analysis with automated resource tracking, comprehensive spending reports, and actionable optimization recommendations
argument-hint: "[cloud_provider] [analysis_period]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /cost analyze - Intelligent Cost Analysis

Advanced cost analysis system with automated resource tracking, comprehensive spending reports, and actionable recommendations for optimization.

## Usage
```bash
/cost analyze aws --period "last_month"      # Analyze AWS costs for the last month
/cost analyze --gcp --service "gke"        # Analyze GCP costs for a specific service
/cost analyze --report "detailed"            # Generate a detailed cost analysis report
/cost analyze --recommendations "true"       # Get cost optimization recommendations
```

<command_file>
  <metadata>
    <n>/cost analyze</n>
    <purpose>Intelligent cost analysis with automated resource tracking, comprehensive spending reports, and actionable optimization recommendations</purpose>
    <usage>
      <![CDATA[
      /cost analyze [cloud_provider] --period [analysis_period]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="cloud_provider" type="string" required="true" default="aws">
      <description>The cloud provider to analyze costs for (e.g., aws, gcp, azure)</description>
    </argument>
    <argument name="analysis_period" type="string" required="false" default="last_30_days">
      <description>The period to analyze costs for (e.g., last_7_days, last_month, custom)</description>
    </argument>
    <argument name="recommendations" type="boolean" required="false" default="true">
      <description>Whether to include cost optimization recommendations in the report</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Analyze AWS costs for the last month</description>
      <usage>/cost analyze aws --period "last_month"</usage>
    </example>
    <example>
      <description>Analyze GCP costs for a specific service</description>
      <usage>/cost analyze --gcp --service "gke"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced cost analysis specialist. The user wants to analyze their cloud costs and get recommendations for optimization.

**Cost Analysis Process:**
1. **Data Ingestion**: Ingest cost and usage data from the cloud provider
2. **Resource Tagging Analysis**: Analyze resource tags to attribute costs accurately
3. **Spending Pattern Analysis**: Analyze spending patterns to identify trends and anomalies
4. **Generate Report**: Generate a comprehensive report with detailed cost breakdowns
5. **Provide Recommendations**: Provide actionable recommendations for cost optimization

**Implementation Strategy:**
- Ingest cost and usage data from cloud provider APIs (e.g., AWS Cost Explorer, GCP Billing)
- Analyze resource tags to group costs by project, service, or environment
- Use statistical analysis and machine learning to identify spending trends, anomalies, and waste
- Generate detailed, easy-to-understand reports with visualizations and cost breakdowns
- Provide concrete, actionable recommendations for cost optimization, such as rightsizing instances, using reserved instances, or deleting unused resources

<include component="components/performance/cost-optimization.md" />
<include component="components/analytics/business-intelligence.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/performance/cost-optimization.md</component>
      <component>components/analytics/business-intelligence.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>cost_analysis.provider.credentials</value>
      <value>cost_optimization.recommendation_level</value>
    </uses_config_values>
  </dependencies>
</command_file>