---
version: 1.0.0
last_updated: 2025-07-07
status: stable
---

<module name="evaluation_dashboard" category="patterns">
  
  <purpose>
    Provide comprehensive visualization and analysis dashboard for prompt evaluation results, tracking trends, and enabling data-driven prompt optimization decisions.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Multiple evaluation results available for analysis</condition>
    <condition type="explicit">User requests evaluation dashboard or trend analysis</condition>
    <condition type="periodic">Weekly/monthly evaluation reporting cycles</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="data_aggregation" order="1">
      <requirements>
        Historical evaluation data collected and validated
        Evaluation results normalized for comparison analysis
        Statistical metrics calculated for trend identification
        Data quality verification completed
      </requirements>
      <actions>
        Collect all available evaluation results from session history
        Normalize scoring data across different evaluation periods
        Calculate statistical metrics (mean, median, trends, variance)
        Validate data completeness and identify any gaps
      </actions>
      <validation>
        All evaluation data successfully collected and validated
        Statistical calculations accurate and properly weighted
        Data quality meets requirements for trend analysis
        Missing data identified and documented
      </validation>
    </phase>
    
    <phase name="visualization_generation" order="2">
      <requirements>
        Dashboard components generated in markdown format
        Interactive elements properly formatted for GitHub display
        Charts and graphs represented in ASCII or mermaid format
        Navigation structure created for easy dashboard exploration
      </requirements>
      <actions>
        Generate overall evaluation summary dashboard
        Create trend analysis charts for score evolution
        Build comparative analysis views for prompt versions
        Construct drill-down sections for detailed investigation
      </actions>
      <validation>
        All dashboard components properly formatted
        Visualizations accurately represent underlying data
        Navigation structure enables efficient dashboard exploration
        Interactive elements function correctly in GitHub context
      </validation>
    </phase>
    
    <phase name="insights_generation" order="3">
      <requirements>
        Automated insights generated from evaluation patterns
        Improvement recommendations based on statistical analysis
        Risk identification for prompts with declining scores
        Optimization opportunities highlighted with specific actions
      </requirements>
      <actions>
        Analyze evaluation patterns to identify improvement opportunities
        Generate automated insights from statistical trends
        Create specific recommendations for prompt optimization
        Identify high-risk prompts requiring immediate attention
      </actions>
      <validation>
        Insights accurately reflect evaluation data patterns
        Recommendations are specific and actionable
        Risk identification properly prioritized
        Optimization opportunities clearly documented
      </validation>
    </phase>
    
  </implementation>
  
  <dashboard_structure>
    <executive_summary>
      <overall_metrics>
        <metric name="total_evaluations">Count of all evaluations completed</metric>
        <metric name="average_score">Mean score across all evaluations</metric>
        <metric name="score_trend">30-day and 90-day trend analysis</metric>
        <metric name="improvement_rate">Percentage of prompts showing improvement</metric>
      </overall_metrics>
      
      <health_indicators>
        <indicator name="quality_distribution">Distribution of scores across quality benchmarks</indicator>
        <indicator name="evaluation_velocity">Rate of evaluations over time</indicator>
        <indicator name="optimization_impact">Effectiveness of prompt improvements</indicator>
        <indicator name="model_efficiency">Claude model usage optimization</indicator>
      </health_indicators>
    </executive_summary>
    
    <detailed_analytics>
      <score_analysis>
        <clarity_trends>Historical clarity scores with trend analysis</clarity_trends>
        <efficiency_trends>Token efficiency improvements over time</efficiency_trends>
        <model_optimization_trends>Model selection accuracy and cost impact</model_optimization_trends>
        <improvement_success_rate>Success rate of implemented improvements</improvement_success_rate>
      </score_analysis>
      
      <comparative_analysis>
        <version_comparison>Side-by-side comparison of prompt versions</version_comparison>
        <benchmark_compliance>Compliance rates against established benchmarks</benchmark_compliance>
        <peer_comparison>Relative performance against similar prompts</peer_comparison>
        <best_practices_adoption>Adoption rate of recommended improvements</best_practices_adoption>
      </comparative_analysis>
    </detailed_analytics>
    
    <operational_insights>
      <evaluation_patterns>
        <peak_times>Times when most evaluations are performed</peak_times>
        <evaluation_duration>Average time to complete evaluations</evaluation_duration>
        <agent_performance>Individual evaluator agent effectiveness</agent_performance>
        <consensus_quality>Quality of agent consensus mechanisms</consensus_quality>
      </evaluation_patterns>
      
      <optimization_opportunities>
        <high_impact_improvements>Improvements with highest score impact</high_impact_improvements>
        <quick_wins>Low-effort improvements with good returns</quick_wins>
        <systematic_issues">Patterns requiring architectural changes</systematic_issues>
        <training_needs>Areas where additional guidance is needed</training_needs>
      </optimization_opportunities>
    </operational_insights>
  </dashboard_structure>
  
  <visualization_templates>
    <trend_chart_ascii>
      Score Trends (Last 30 Days)
      ┌─────────────────────────────────────────┐
      │ 10 ┤                               ●     │
      │  9 ┤                         ●   ●       │
      │  8 ┤                   ●   ●             │
      │  7 ┤             ●   ●                   │
      │  6 ┤       ●   ●                         │
      │  5 ┤ ●   ●                               │
      │    └┬────┬────┬────┬────┬────┬────┬─────┤
      │     W1   W2   W3   W4   W5   W6   W7    │
      └─────────────────────────────────────────┘
      Trend: ↗ Improving (+2.3 points over 30 days)
    </trend_chart_ascii>
    
    <distribution_chart_ascii>
      Score Distribution
      ┌─────────────────────────────────────────┐
      │ 9-10 ████████████████ 45% (Excellent)   │
      │ 7-8  ██████████ 30% (Good)              │
      │ 5-6  ████ 15% (Acceptable)              │
      │ 3-4  ██ 7% (Poor)                       │
      │ 1-2  █ 3% (Unacceptable)                │
      └─────────────────────────────────────────┘
      Quality Status: 75% Above Acceptable
    </distribution_chart_ascii>
    
    <comparison_matrix>
      Version Comparison Matrix
      ┌─────────────┬─────────┬───────────┬──────────┬─────────┐
      │ Version     │ Clarity │ Efficiency│ Model    │ Overall │
      ├─────────────┼─────────┼───────────┼──────────┼─────────┤
      │ v1.0        │   6.2   │    5.8    │  Sonnet  │   6.0   │
      │ v1.1        │   7.8   │    7.2    │  Sonnet  │   7.5   │
      │ v2.0        │   8.9   │    8.6    │  Sonnet  │   8.8   │
      │ v2.1 (Best) │   9.2   │    9.1    │  Sonnet  │   9.2   │
      └─────────────┴─────────┴───────────┴──────────┴─────────┘
      Improvement: +3.2 points over 4 versions
    </comparison_matrix>
  </visualization_templates>
  
  <statistical_analysis>
    <descriptive_statistics>
      <central_tendency>
        <mean>Average score across all evaluations</mean>
        <median>Middle score value for robust central measurement</median>
        <mode>Most frequent score range for pattern identification</mode>
      </central_tendency>
      
      <variability_measures>
        <standard_deviation>Score consistency measurement</standard_deviation>
        <interquartile_range>Score distribution analysis</interquartile_range>
        <coefficient_of_variation>Relative variability assessment</coefficient_of_variation>
      </variability_measures>
    </descriptive_statistics>
    
    <trend_analysis>
      <linear_regression>
        Calculate trend lines for score evolution over time
        Identify statistically significant improvement patterns
        Predict future score trajectories based on current trends
      </linear_regression>
      
      <moving_averages>
        <short_term>7-day moving average for recent performance</short_term>
        <medium_term>30-day moving average for monthly trends</medium_term>
        <long_term>90-day moving average for quarterly analysis</long_term>
      </moving_averages>
    </trend_analysis>
    
    <correlation_analysis>
      <score_correlations>
        Correlation between different evaluation criteria
        Identification of strongly related scoring dimensions
        Analysis of improvement interdependencies
      </score_correlations>
      
      <external_factors>
        Correlation with evaluation timing and context
        Analysis of evaluator agent consistency
        Impact of prompt complexity on scoring patterns
      </external_factors>
    </correlation_analysis>
  </statistical_analysis>
  
  <automated_insights>
    <pattern_recognition>
      <improvement_patterns>
        Identify consistent patterns in prompt improvements
        Recognition of successful optimization strategies
        Detection of recurring improvement opportunities
      </improvement_patterns>
      
      <risk_patterns>
        Early detection of declining score trends
        Identification of prompts at risk of quality degradation
        Recognition of systematic quality issues
      </risk_patterns>
    </pattern_recognition>
    
    <recommendation_engine>
      <optimization_recommendations>
        Data-driven suggestions for prompt improvements
        Prioritization based on impact and effort analysis
        Specific action items with implementation guidance
      </optimization_recommendations>
      
      <quality_alerts>
        Automated alerts for scores below benchmarks
        Proactive notifications for declining trends
        Escalation triggers for critical quality issues
      </quality_alerts>
    </recommendation_engine>
  </automated_insights>
  
  <dashboard_navigation>
    <main_sections>
      <section name="executive_overview">High-level metrics and health indicators</section>
      <section name="detailed_analytics">Deep-dive analysis and trend exploration</section>
      <section name="comparative_analysis">Version and benchmark comparisons</section>
      <section name="operational_insights">Process optimization and improvement opportunities</section>
      <section name="historical_archive">Complete evaluation history and data export</section>
    </main_sections>
    
    <interactive_features>
      <filters>
        <date_range>Filter by evaluation date ranges</date_range>
        <score_range>Filter by score thresholds</score_range>
        <prompt_type>Filter by prompt category or type</prompt_type>
        <evaluator>Filter by specific evaluator agents</evaluator>
      </filters>
      
      <drill_down>
        <score_details>Click through from summary to detailed evaluation</score_details>
        <trend_investigation>Deep dive into specific trend patterns</trend_investigation>
        <comparison_analysis">Side-by-side detailed comparison views</comparison_analysis>
      </drill_down>
    </interactive_features>
  </dashboard_navigation>
  
  <data_export>
    <export_formats>
      <csv_export>Raw evaluation data for external analysis</csv_export>
      <json_export>Structured data for API integration</json_export>
      <markdown_export">Formatted reports for documentation</markdown_export>
      <pdf_export>Professional reports for stakeholder communication</pdf_export>
    </export_formats>
    
    <export_options>
      <full_dataset>Complete evaluation history</full_dataset>
      <filtered_subset>Data matching current filter criteria</filtered_subset>
      <summary_report>Executive summary with key metrics</summary_report>
      <detailed_analysis">Comprehensive analysis with visualizations</detailed_analysis>
    </export_options>
  </data_export>
  
  <history_tracking>
    <evaluation_archive>
      <storage_structure>
        Organized by date, prompt, and evaluation session
        Indexed for fast retrieval and analysis
        Compressed for efficient storage management
        Backed up for data protection and recovery
      </storage_structure>
      
      <retention_policy>
        <short_term>90 days of detailed evaluation data</short_term>
        <medium_term">1 year of summary metrics and trends</medium_term>
        <long_term>Indefinite retention of key benchmarks and milestones</long_term>
        <archival>Compressed historical data for research purposes</archival>
      </retention_policy>
    </evaluation_archive>
    
    <change_tracking>
      <version_history>
        Complete history of prompt versions and changes
        Attribution of changes to specific evaluations
        Impact analysis of modifications on scores
        Rollback capability for regression scenarios
      </version_history>
      
      <improvement_tracking>
        Documentation of all implemented improvements
        Success rate measurement for optimization efforts
        ROI analysis for prompt optimization investments
        Best practices extraction from successful changes
      </improvement_tracking>
    </change_tracking>
  </history_tracking>
  
  <integration_points>
    <depends_on>
      patterns/prompt-evaluation.md for evaluation data source
      patterns/session-management.md for session-based data organization
      development/research-analysis.md for statistical analysis capabilities
    </depends_on>
    <provides_to>
      All commands for evaluation insights and recommendations
      patterns/intelligent-routing.md for data-driven routing decisions
      quality/production-standards.md for quality trend monitoring
    </provides_to>
  </integration_points>
  
</module>