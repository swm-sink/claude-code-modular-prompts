| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | active |

# Context-Sensitive Quality Reporting Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="context_sensitive_quality_reporting" category="quality">
  
  <purpose>
    Intelligent quality reporting system that generates clear, actionable reports with context-sensitive recommendations, adapting report content and detail level based on audience, task complexity, and quality outcomes.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>quality_metrics, complexity_data, audience_profile, reporting_context</required>
      <optional>historical_data, comparison_baselines, user_preferences, business_requirements</optional>
    </inputs>
    <outputs>
      <success>context_sensitive_report, actionable_recommendations, trend_analysis, optimization_roadmap</success>
      <failure>report_generation_errors, data_analysis_failures, recommendation_generation_issues</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Analyze quality data and metrics in context of task complexity and audience
      2. Generate context-appropriate report content with relevant insights
      3. Provide actionable recommendations based on context and constraints
      4. Create visual representations optimized for audience understanding
      5. Deliver reports through appropriate channels with follow-up mechanisms
    </claude_4_behavior>
  </execution_pattern>
  
  <audience_specific_reporting>
    <audience_profiles>
      <profile name="developer" reporting_focus="technical_details">
        <description>Individual developers working on tasks</description>
        <information_needs>
          <need>Personal quality metrics and trends</need>
          <need">Task-specific quality feedback</need>
          <need>Technical recommendations for improvement</need>
          <need>Quality gate results and explanations</need>
        </information_needs>
        <preferred_format>Interactive dashboard with drill-down capabilities</preferred_format>
        <update_frequency>Real-time for active tasks, daily summaries</update_frequency>
        <detail_level>High technical detail with code-level insights</detail_level>
      </profile>
      
      <profile name="team_lead" reporting_focus="team_performance">
        <description>Team leads managing development teams</description>
        <information_needs>
          <need>Team quality performance and trends</need>
          <need>Resource allocation and efficiency metrics</need>
          <need>Quality bottlenecks and improvement opportunities</need>
          <need>Team member development and training needs</need>
        </information_needs>
        <preferred_format>Dashboard with team comparisons and trends</preferred_format>
        <update_frequency">Daily summaries with weekly detailed reports</update_frequency>
        <detail_level">Medium detail with focus on team dynamics</detail_level>
      </profile>
      
      <profile name="project_manager" reporting_focus="project_health">
        <description>Project managers overseeing multiple projects</description>
        <information_needs>
          <need>Project quality status and risk assessment</need>
          <need>Timeline impact from quality issues</need>
          <need>Resource requirements for quality improvements</need>
          <need>Quality compliance and audit readiness</need>
        </information_needs>
        <preferred_format">Executive dashboard with status indicators</preferred_format>
        <update_frequency">Daily status updates with weekly project reports</update_frequency>
        <detail_level">Medium detail with focus on project impact</detail_level>
      </profile>
      
      <profile name="quality_engineer" reporting_focus="quality_system">
        <description>Quality engineers managing quality systems</description>
        <information_needs>
          <need>Quality system performance and effectiveness</need>
          <need>Quality gate analytics and optimization</need>
          <need>Quality process improvement opportunities</need>
          <need>Quality metrics validation and accuracy</need>
        </information_needs>
        <preferred_format">Technical analysis reports with detailed metrics</preferred_format>
        <update_frequency">Continuous monitoring with weekly analysis reports</update_frequency>
        <detail_level">High technical detail with system analysis</detail_level>
      </profile>
      
      <profile name="executive" reporting_focus="business_impact">
        <description>Executives and senior management</description>
        <information_needs>
          <need>Quality impact on business objectives</need>
          <need>Quality investment ROI and cost analysis</need>
          <need>Quality risk assessment and mitigation</need>
          <need>Quality competitive advantage and benchmarking</need>
        </information_needs>
        <preferred_format">Executive summary with key insights</preferred_format>
        <update_frequency">Weekly summaries with monthly strategic reports</update_frequency>
        <detail_level">High-level strategic overview with business focus</detail_level>
      </profile>
    </audience_profiles>
    
    <adaptive_content_generation>
      <content_adaptation_rules>
        <rule audience="developer" complexity="simple_tasks">
          <focus>Quick feedback on code quality and immediate improvements</focus>
          <content_depth">Basic quality metrics with specific code recommendations</content_depth>
          <actionability">Direct code changes and optimization suggestions</actionability>
        </rule>
        
        <rule audience="developer" complexity="complex_tasks">
          <focus>Comprehensive quality analysis with architectural insights</focus>
          <content_depth">Detailed quality metrics with design pattern recommendations</content_depth>
          <actionability">Architectural improvements and refactoring suggestions</actionability>
        </rule>
        
        <rule audience="team_lead" complexity="medium_tasks">
          <focus>Team coordination and resource optimization</focus>
          <content_depth">Team performance metrics with collaboration insights</content_depth>
          <actionability">Team process improvements and skill development</actionability>
        </rule>
        
        <rule audience="executive" complexity="critical_tasks">
          <focus>Business risk assessment and strategic implications</focus>
          <content_depth">High-level quality metrics with business impact analysis</content_depth>
          <actionability">Strategic decisions and resource allocation</actionability>
        </rule>
      </content_adaptation_rules>
    </adaptive_content_generation>
  </audience_specific_reporting>
  
  <context_sensitive_report_types>
    <report_type name="task_completion_report" trigger="task_completion">
      <description>Generated upon task completion with context-specific insights</description>
      <content_structure>
        <section name="task_summary">
          <description>Summary of task characteristics and complexity</description>
          <adaptive_content>
            <simple_tasks>Basic task summary with key metrics</simple_tasks>
            <complex_tasks">Detailed task analysis with architectural impact</complex_tasks>
          </adaptive_content>
        </section>
        
        <section name="quality_outcomes">
          <description>Quality results and achievements</description>
          <adaptive_content>
            <simple_tasks">Pass/fail status with basic quality scores</simple_tasks>
            <complex_tasks">Comprehensive quality analysis with detailed metrics</complex_tasks>
          </adaptive_content>
        </section>
        
        <section name="efficiency_analysis">
          <description>Efficiency gains and time savings achieved</description>
          <adaptive_content>
            <simple_tasks">Time savings and overhead reduction</simple_tasks>
            <complex_tasks">Detailed efficiency analysis with optimization opportunities</complex_tasks>
          </adaptive_content>
        </section>
        
        <section name="recommendations">
          <description>Context-specific recommendations for improvement</description>
          <adaptive_content>
            <simple_tasks">Quick improvement suggestions</simple_tasks>
            <complex_tasks">Strategic improvement roadmap</complex_tasks>
          </adaptive_content>
        </section>
      </content_structure>
      
      <delivery_mechanism>
        <immediate_feedback">Real-time feedback within development environment</immediate_feedback>
        <dashboard_integration">Integration with personal and team dashboards</dashboard_integration>
        <email_summary">Optional email summary for stakeholders</email_summary>
      </delivery_mechanism>
    </report_type>
    
    <report_type name="quality_trend_report" trigger="scheduled_weekly">
      <description>Weekly quality trend analysis with predictive insights</description>
      <content_structure>
        <section name="trend_analysis">
          <description>Quality trends and patterns over time</description>
          <adaptive_content>
            <all_audiences">Trend visualization with context-appropriate detail</all_audiences>
          </adaptive_content>
        </section>
        
        <section name="performance_insights">
          <description>Performance insights and efficiency trends</description>
          <adaptive_content>
            <technical_audience">Detailed performance metrics and optimization opportunities</technical_audience>
            <business_audience">Performance impact on business objectives</business_audience>
          </adaptive_content>
        </section>
        
        <section name="predictive_analysis">
          <description>Predictive analysis of future quality trends</description>
          <adaptive_content>
            <all_audiences">Predictions tailored to audience expertise level</all_audiences>
          </adaptive_content>
        </section>
      </content_structure>
    </report_type>
    
    <report_type name="quality_incident_report" trigger="quality_issue">
      <description>Generated when quality issues or incidents occur</description>
      <content_structure>
        <section name="incident_summary">
          <description>Summary of quality incident and impact</description>
          <adaptive_content>
            <severity_based">Detail level based on incident severity</severity_based>
          </adaptive_content>
        </section>
        
        <section name="root_cause_analysis">
          <description>Root cause analysis and contributing factors</description>
          <adaptive_content>
            <technical_audience">Technical root cause analysis</technical_audience>
            <business_audience">Business impact and risk assessment</business_audience>
          </adaptive_content>
        </section>
        
        <section name="corrective_actions">
          <description>Immediate and long-term corrective actions</description>
          <adaptive_content">
            <all_audiences">Action items appropriate to audience role</all_audiences>
          </adaptive_content>
        </section>
      </content_structure>
    </report_type>
    
    <report_type name="quality_optimization_report" trigger="optimization_opportunity">
      <description>Generated when optimization opportunities are identified</description>
      <content_structure>
        <section name="opportunity_analysis">
          <description>Analysis of optimization opportunities</description>
          <adaptive_content>
            <technical_audience">Technical optimization details</technical_audience>
            <business_audience">Business value and ROI analysis</business_audience>
          </adaptive_content>
        </section>
        
        <section name="implementation_roadmap">
          <description>Roadmap for implementing optimizations</description>
          <adaptive_content>
            <all_audiences">Roadmap appropriate to audience planning horizon</all_audiences>
          </adaptive_content>
        </section>
      </content_structure>
    </report_type>
  </context_sensitive_report_types>
  
  <intelligent_recommendation_engine>
    <recommendation_generation>
      <context_analysis>
        <factor name="task_complexity" weight="30%">
          <description>Adapt recommendations based on task complexity level</description>
          <implementation">
            <simple_tasks">Focus on immediate, actionable improvements</simple_tasks>
            <complex_tasks">Provide strategic, architectural recommendations</complex_tasks>
          </implementation>
        </factor>
        
        <factor name="quality_outcomes" weight="25%">
          <description>Base recommendations on actual quality results</description>
          <implementation">
            <high_quality">Optimization and efficiency recommendations</high_quality>
            <low_quality">Fundamental quality improvement recommendations</low_quality>
          </implementation>
        </factor>
        
        <factor name="user_context" weight="25%">
          <description>Tailor recommendations to user role and expertise</description>
          <implementation">
            <developers">Technical implementation recommendations</developers>
            <managers">Process and resource recommendations</managers>
          </implementation>
        </factor>
        
        <factor name="historical_patterns" weight="20%">
          <description>Use historical data to inform recommendations</description>
          <implementation">
            <pattern_recognition">Identify recurring issues and proven solutions</pattern_recognition>
            <success_patterns">Recommend approaches with historical success</success_patterns>
          </implementation>
        </factor>
      </context_analysis>
      
      <recommendation_types>
        <type name="immediate_actions" priority="high">
          <description">Actions that can be taken immediately to improve quality</description>
          <characteristics">
            <time_to_implement">< 1 hour</time_to_implement>
            <resource_requirement">Low</resource_requirement>
            <impact_level">Medium</impact_level>
          </characteristics>
          <examples">
            <example>Fix specific code quality issues</example>
            <example>Update configuration settings</example>
            <example>Add missing tests for critical functions</example>
          </examples>
        </type>
        
        <type name="short_term_improvements" priority="medium">
          <description>Improvements that can be implemented in the short term</description>
          <characteristics">
            <time_to_implement">< 1 week</time_to_implement>
            <resource_requirement">Medium</resource_requirement>
            <impact_level">High</impact_level>
          </characteristics>
          <examples">
            <example>Implement automated testing for components</example>
            <example>Refactor complex modules for better maintainability</example>
            <example>Establish performance monitoring for critical paths</example>
          </examples>
        </type>
        
        <type name="strategic_initiatives" priority="low">
          <description>Long-term strategic initiatives for quality improvement</description>
          <characteristics">
            <time_to_implement">< 3 months</time_to_implement>
            <resource_requirement">High</resource_requirement>
            <impact_level">Very High</impact_level>
          </characteristics>
          <examples">
            <example>Implement comprehensive quality management system</example>
            <example>Establish quality-driven development culture</example>
            <example>Invest in advanced quality tooling and automation</example>
          </examples>
        </type>
      </recommendation_types>
    </recommendation_generation>
    
    <recommendation_prioritization>
      <prioritization_algorithm>
        <criteria name="impact_assessment" weight="40%">
          <description>Assess potential impact of recommendation</description>
          <measurement">
            <quality_improvement">Expected improvement in quality metrics</quality_improvement>
            <efficiency_gain">Expected efficiency gains</efficiency_gain>
            <risk_reduction">Expected reduction in quality risks</risk_reduction>
          </measurement>
        </criteria>
        
        <criteria name="implementation_effort" weight="30%">
          <description>Assess effort required for implementation</description>
          <measurement">
            <time_investment">Time required for implementation</time_investment>
            <resource_requirement">Resources needed for implementation</resource_requirement>
            <complexity_level">Complexity of implementation</complexity_level>
          </measurement>
        </criteria>
        
        <criteria name="urgency_level" weight="20%">
          <description>Assess urgency of addressing the issue</description>
          <measurement">
            <risk_level">Level of risk if not addressed</risk_level>
            <business_impact">Business impact of delayed implementation</business_impact>
            <stakeholder_pressure">Stakeholder pressure for resolution</stakeholder_pressure>
          </measurement>
        </criteria>
        
        <criteria name="feasibility" weight="10%">
          <description>Assess feasibility of implementation</description>
          <measurement">
            <technical_feasibility">Technical feasibility of solution</technical_feasibility>
            <resource_availability">Availability of required resources</resource_availability>
            <organizational_readiness">Organizational readiness for change</organizational_readiness>
          </measurement>
        </criteria>
      </prioritization_algorithm>
      
      <recommendation_ranking>
        <ranking_approach">
          <step>Calculate weighted score for each recommendation</step>
          <step>Rank recommendations by score</step>
          <step>Group recommendations by priority level</step>
          <step>Provide implementation sequence suggestions</step>
        </ranking_approach>
        
        <context_adjustment">
          <adjustment_factors">
            <factor>Audience expertise level</factor>
            <factor>Available resources and constraints</factor>
            <factor>Business priorities and deadlines</factor>
            <factor>Technical debt and system state</factor>
          </adjustment_factors>
        </context_adjustment>
      </recommendation_ranking>
    </recommendation_prioritization>
  </intelligent_recommendation_engine>
  
  <visualization_and_presentation>
    <adaptive_visualization>
      <visualization_selection>
        <selection_criteria>
          <criterion name="data_type">Select visualization based on data characteristics</criterion>
          <criterion name="audience_expertise">Adapt complexity to audience technical level</criterion>
          <criterion name="message_clarity">Optimize for clear message communication</criterion>
          <criterion name="actionability">Enable actionable insights from visualization</criterion>
        </selection_criteria>
        
        <visualization_types>
          <type name="trend_charts" audience="all">
            <description>Time series visualization for trend analysis</description>
            <best_for">Quality trends, performance metrics, efficiency gains</best_for>
            <adaptive_features">
              <simple_view">Basic trend line with key indicators</simple_view>
              <detailed_view">Multi-dimensional trend analysis with annotations</detailed_view>
            </adaptive_features>
          </type>
          
          <type name="dashboard_widgets" audience="technical">
            <description>Interactive widgets for real-time monitoring</description>
            <best_for">Real-time metrics, status indicators, alerts</best_for>
            <adaptive_features">
              <minimal_view">Key metrics with status indicators</minimal_view>
              <comprehensive_view">Detailed metrics with drill-down capabilities</comprehensive_view>
            </adaptive_features>
          </type>
          
          <type name="heatmaps" audience="analysts">
            <description>Heatmap visualization for pattern recognition</description>
            <best_for">Quality gate performance, complexity distribution, error patterns</best_for>
            <adaptive_features">
              <overview_view">High-level pattern visualization</overview_view>
              <detailed_view">Granular pattern analysis with filtering</detailed_view>
            </adaptive_features>
          </type>
          
          <type name="executive_summaries" audience="executives">
            <description>High-level summary visualizations</description>
            <best_for">Business impact, ROI analysis, strategic overview</best_for>
            <adaptive_features">
              <strategic_view">Business-focused metrics and insights</strategic_view>
              <operational_view">Operational efficiency and resource utilization</operational_view>
            </adaptive_features>
          </type>
        </visualization_types>
      </visualization_selection>
      
      <interactive_features>
        <feature name="drill_down_capability">
          <description">Enable drilling down from high-level to detailed views</description>
          <implementation">Click-through navigation with context preservation</implementation>
          <benefit">Allows exploration of root causes and detailed analysis</benefit>
        </feature>
        
        <feature name="filtering_and_segmentation">
          <description>Enable filtering and segmentation of data views</description>
          <implementation">Dynamic filters with real-time updates</implementation>
          <benefit">Enables focused analysis on specific aspects or time periods</benefit>
        </feature>
        
        <feature name="comparative_analysis">
          <description>Enable comparison between different time periods or entities</description>
          <implementation">Side-by-side comparisons with highlighting</implementation>
          <benefit">Enables trend analysis and benchmarking</benefit>
        </feature>
        
        <feature name="export_and_sharing">
          <description>Enable export and sharing of reports and visualizations</description>
          <implementation">Multiple export formats with sharing capabilities</implementation>
          <benefit">Enables collaboration and offline analysis</benefit>
        </feature>
      </interactive_features>
    </adaptive_visualization>
    
    <presentation_optimization>
      <content_organization>
        <organization_principles>
          <principle name="information_hierarchy">Organize information by importance and relevance</principle>
          <principle name="progressive_disclosure">Present information in layers from general to specific</principle>
          <principle name="context_preservation">Maintain context throughout the report</principle>
          <principle name="actionable_focus">Focus on actionable insights and recommendations</principle>
        </organization_principles>
        
        <layout_adaptation>
          <layout_factors">
            <factor name="audience_attention_span">Adapt layout for audience attention patterns</factor>
            <factor name="information_density">Optimize information density for comprehension</factor>
            <factor name="visual_hierarchy">Create clear visual hierarchy for navigation</factor>
            <factor name="mobile_responsiveness">Ensure accessibility across devices</factor>
          </layout_factors>
        </layout_adaptation>
      </content_organization>
      
      <narrative_construction>
        <storytelling_approach">
          <structure name="situation_action_result">
            <description>Present situation, actions taken, and results achieved</description>
            <application">Task completion reports and improvement initiatives</application>
          </structure>
          
          <structure name="problem_solution_benefit">
            <description>Identify problem, present solution, highlight benefits</description>
            <application">Quality incident reports and optimization recommendations</application>
          </structure>
          
          <structure name="trend_insight_prediction">
            <description>Show trends, provide insights, make predictions</description>
            <application">Quality trend reports and strategic planning</application>
          </structure>
        </storytelling_approach>
        
        <narrative_adaptation>
          <adaptation_factors">
            <factor name="audience_expertise">Adapt technical depth to audience knowledge</factor>
            <factor name="business_context">Frame narrative in relevant business context</factor>
            <factor name="decision_support">Structure narrative to support decision-making</factor>
            <factor name="action_orientation">Focus narrative on actionable outcomes</factor>
          </adaptation_factors>
        </narrative_adaptation>
      </narrative_construction>
    </presentation_optimization>
  </visualization_and_presentation>
  
  <delivery_and_distribution>
    <multi_channel_delivery>
      <delivery_channels">
        <channel name="dashboard_integration">
          <description">Integration with existing dashboards and monitoring systems</description>
          <best_for">Real-time monitoring and immediate feedback</best_for>
          <update_frequency">Real-time to hourly updates</update_frequency>
          <interactivity">High interactivity with drill-down capabilities</interactivity>
        </channel>
        
        <channel name="email_reports">
          <description>Email delivery of formatted reports</description>
          <best_for">Scheduled reports and important notifications</best_for>
          <update_frequency">Daily to weekly scheduled delivery</update_frequency>
          <interactivity">Limited interactivity with links to full reports</interactivity>
        </channel>
        
        <channel name="mobile_notifications">
          <description>Mobile notifications for urgent quality issues</description>
          <best_for">Critical alerts and time-sensitive information</best_for>
          <update_frequency">Immediate notifications for critical issues</update_frequency>
          <interactivity">Basic interactivity with link to detailed information</interactivity>
        </channel>
        
        <channel name="api_integration">
          <description>API endpoints for system integration</description>
          <best_for">Integration with third-party systems and tools</best_for>
          <update_frequency">Real-time API access to current data</update_frequency>
          <interactivity">Programmatic access with query capabilities</interactivity>
        </channel>
      </delivery_channels>
      
      <intelligent_routing">
        <routing_rules">
          <rule name="urgency_based_routing">
            <condition>Critical quality issues detected</condition>
            <action">Immediate notification through multiple channels</action>
            <escalation">Escalate to management if not acknowledged</escalation>
          </rule>
          
          <rule name="audience_preference_routing">
            <condition>Regular report generation</condition>
            <action">Deliver through user-preferred channels</action>
            <personalization">Adapt content and timing to user preferences</personalization>
          </rule>
          
          <rule name="context_sensitive_routing">
            <condition>Context-specific reports</condition>
            <action">Route to appropriate stakeholders based on context</action>
            <intelligence">Learn from user engagement patterns</intelligence>
          </rule>
        </routing_rules>
      </intelligent_routing>
    </multi_channel_delivery>
    
    <feedback_and_iteration>
      <feedback_collection">
        <feedback_mechanisms">
          <mechanism name="user_ratings">
            <description>User ratings for report usefulness and clarity</description>
            <implementation">Rating system with optional comments</implementation>
            <usage">Improve report quality and relevance</usage>
          </mechanism>
          
          <mechanism name="engagement_analytics">
            <description>Analytics on user engagement with reports</description>
            <implementation">Track views, interactions, and actions taken</implementation>
            <usage">Optimize report content and presentation</usage>
          </mechanism>
          
          <mechanism name="action_tracking">
            <description>Track actions taken based on recommendations</description>
            <implementation">Follow-up on recommended actions</implementation>
            <usage">Measure recommendation effectiveness</usage>
          </mechanism>
        </feedback_mechanisms>
      </feedback_collection>
      
      <continuous_improvement">
        <improvement_cycle">
          <step name="data_collection">Collect feedback and usage data</step>
          <step name="analysis">Analyze patterns and effectiveness</step>
          <step name="optimization">Optimize reports based on insights</step>
          <step name="validation">Validate improvements through testing</step>
        </improvement_cycle>
        
        <learning_integration">
          <learning_aspects">
            <aspect name="content_optimization">Learn what content is most valuable</aspect>
            <aspect name="presentation_optimization">Learn optimal presentation formats</aspect>
            <aspect name="timing_optimization">Learn optimal timing for delivery</aspect>
            <aspect name="channel_optimization">Learn preferred delivery channels</aspect>
          </learning_aspects>
        </learning_integration>
      </continuous_improvement>
    </feedback_and_iteration>
  </delivery_and_distribution>
  
  <success_metrics>
    <report_effectiveness">
      <metric name="report_usage_rate">Percentage of generated reports that are viewed</metric>
      <metric name="user_engagement_score">Average time spent reviewing reports</metric>
      <metric name="recommendation_adoption_rate">Percentage of recommendations that are implemented</metric>
      <metric name="report_accuracy">Accuracy of insights and predictions in reports</metric>
    </report_effectiveness>
    
    <user_satisfaction>
      <metric name="user_satisfaction_score">User satisfaction with report quality and usefulness</metric>
      <metric name="clarity_rating">User rating of report clarity and understandability</metric>
      <metric name="actionability_rating">User rating of recommendation actionability</metric>
      <metric name="timeliness_rating">User rating of report timeliness and relevance</metric>
    </user_satisfaction>
    
    <business_impact>
      <metric name="decision_support_effectiveness">Effectiveness of reports in supporting decisions</metric>
      <metric name="quality_improvement_correlation">Correlation between reports and quality improvements</metric>
      <metric name="cost_benefit_analysis">Cost-benefit analysis of reporting system</metric>
      <metric name="competitive_advantage">Reporting as source of competitive advantage</metric>
    </business_impact>
  </success_metrics>
  
  <integration_points>
    <depends_on>
      quality/quality-metrics-dashboard.md for metrics data and visualization
      quality/context-sensitive-quality-assessment.md for complexity context
      quality/adaptive-quality-gates.md for quality outcomes data
      quality/progressive-testing-integration.md for testing results
    </depends_on>
    <provides_to>
      All stakeholders for quality insights and recommendations
      quality/quality-metrics-dashboard.md for report content integration
      development/task-management.md for task-specific quality reporting
      patterns/intelligent-routing.md for quality-aware decision support
    </provides_to>
  </integration_points>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

*Intelligent quality reporting system that generates clear, actionable reports with context-sensitive recommendations, adapting content and detail level based on audience, task complexity, and quality outcomes.*