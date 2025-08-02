# Report Generation

**Purpose**: Generate consistent, well-structured reports with standardized formatting, actionable insights, and multiple export options for comprehensive analysis communication.

**Usage**: 
- Create standardized reports with executive summary, detailed analysis, and recommendations
- Format reports consistently across all commands and analysis tools
- Include actionable insights with priority rankings and implementation guidance
- Provide multiple export formats (markdown, PDF, JSON, HTML) for different audiences
- Generate executive summaries for quick consumption and decision-making

**Compatibility**: 
- **Works with**: task-summary, output-formatter, data-transformer, analysis components
- **Requires**: Analysis data and findings from various workflow components
- **Conflicts**: None (universal reporting utility)

**Implementation**:
```python
# Standardized report generation
class ReportGenerator:
    def __init__(self, template_type="standard"):
        self.template_type = template_type
        self.formatter = ReportFormatter()
        
    def generate_comprehensive_report(self, analysis_data, insights, recommendations):
        report = StandardReport()
        
        # 1. Executive Summary
        exec_summary = self.create_executive_summary(
            key_findings=insights['critical'],
            metrics=analysis_data['key_metrics'],
            action_items=recommendations['high_priority'],
            overall_status=self.assess_overall_status(analysis_data)
        )
        
        # 2. Detailed Analysis
        detailed_analysis = self.create_detailed_analysis(
            findings=insights['comprehensive'],
            supporting_data=analysis_data['detailed'],
            trends=analysis_data['trends'],
            comparisons=analysis_data.get('comparisons', [])
        )
        
        # 3. Recommendations Section
        recommendations_section = self.create_recommendations(
            actions=recommendations['prioritized'],
            implementation_guides=recommendations['guidance'],
            risk_assessments=recommendations['risks'],
            timelines=recommendations['timelines']
        )
        
        # 4. Appendices
        appendices = self.create_appendices(
            raw_data=analysis_data['raw'],
            technical_specs=analysis_data.get('technical', {}),
            configurations=analysis_data.get('config', {})
        )
        
        # Assemble complete report
        report.add_section("executive_summary", exec_summary)
        report.add_section("detailed_analysis", detailed_analysis)
        report.add_section("recommendations", recommendations_section)
        report.add_section("appendices", appendices)
        
        return report
    
    def export_report(self, report, format="markdown"):
        exporters = {
            'markdown': self.export_markdown,
            'pdf': self.export_pdf,
            'json': self.export_json,
            'html': self.export_html
        }
        
        if format in exporters:
            return exporters[format](report)
        else:
            raise ValueError(f"Unsupported export format: {format}")
    
    def create_executive_summary(self, key_findings, metrics, action_items, overall_status):
        return {
            'status': overall_status,
            'key_findings': key_findings[:5],  # Top 5 findings
            'critical_metrics': metrics['critical'],
            'immediate_actions': action_items[:3],  # Top 3 actions
            'recommendation': self.generate_overall_recommendation(overall_status, action_items)
        }

# Multi-format export capabilities
def export_markdown(report):
    markdown_content = f"""# {report.title}

## Executive Summary
**Status**: {report.executive_summary['status']}

**Key Findings**:
{format_findings_list(report.executive_summary['key_findings'])}

**Immediate Actions**:
{format_actions_list(report.executive_summary['immediate_actions'])}

## Detailed Analysis
{format_detailed_analysis(report.detailed_analysis)}

## Recommendations
{format_recommendations(report.recommendations)}

## Appendices
{format_appendices(report.appendices)}
"""
    return markdown_content
```

**Category**: workflow | **Complexity**: moderate | **Time**: 2 hours