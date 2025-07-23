---
name: /cost-analyze
description: Intelligent cost analysis with automated resource tracking, comprehensive spending reports, and actionable optimization recommendations
usage: /cost-analyze [cloud_provider] [analysis_period]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent cost analysis with automated resource tracking, comprehensive spending reports, and actionable optimization recommendations

**Usage**: `/cost-analyze $CLOUD_PROVIDER $ANALYSIS_PERIOD $RECOMMENDATIONS`

## Key Arguments

- **$CLOUD_PROVIDER** (required): The cloud provider to analyze costs for (e.g., aws, gcp, azure)
- **$ANALYSIS_PERIOD** (optional): The period to analyze costs for (e.g., last_7_days, last_month, custom)
- **$RECOMMENDATIONS** (optional): Whether to include cost optimization recommendations in the report

## Examples

```bash
/cost analyze aws --period "last_month"
```
*Analyze AWS costs for the last month*

```bash
/cost analyze --gcp --service "gke"
```
*Analyze GCP costs for a specific service*

## Core Logic

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

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

