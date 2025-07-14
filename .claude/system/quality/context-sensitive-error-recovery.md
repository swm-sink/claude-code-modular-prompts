| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Context-Sensitive Error Recovery Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="context_sensitive_error_recovery" category="quality">
  
  <purpose>
    Intelligent error recovery system that provides context-appropriate error handling and rollback mechanisms, scaling response from simple fixes to comprehensive recovery based on task complexity and error severity.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>error_context, complexity_classification, error_severity, system_state</required>
      <optional>user_preferences, recovery_constraints, rollback_options, escalation_thresholds</optional>
    </inputs>
    <outputs>
      <success>recovery_plan, rollback_strategy, error_resolution, system_restoration</success>
      <failure>recovery_planning_errors, rollback_failures, escalation_triggers</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Analyze error context and classify severity with task complexity consideration
      2. Determine appropriate recovery strategy based on context and constraints
      3. Execute recovery plan with intelligent monitoring and adaptation
      4. Provide rollback capability appropriate to the error and task complexity
      5. Generate recovery report with lessons learned and prevention recommendations
    </claude_4_behavior>
  </execution_pattern>
  
  <error_classification_framework>
    <severity_levels>
      <level name="informational" priority="low">
        <description>Informational issues that don't block progress</description>
        <examples>Style warnings, minor documentation issues, optional optimizations</examples>
        <impact>No functional impact, minimal user disruption</impact>
        <recovery_urgency>Low priority, can be addressed later</recovery_urgency>
      </level>
      
      <level name="warning" priority="medium">
        <description>Warning issues that should be addressed but don't block completion</description>
        <examples>Performance concerns, deprecated API usage, minor security considerations</examples>
        <impact">Minor functional impact, some user experience degradation</impact>
        <recovery_urgency">Medium priority, should be addressed soon</recovery_urgency>
      </level>
      
      <level name="error" priority="high">
        <description>Error issues that block completion and require resolution</description>
        <examples">Test failures, compilation errors, integration failures</examples>
        <impact">Significant functional impact, user experience degradation</impact>
        <recovery_urgency">High priority, must be resolved to continue</recovery_urgency>
      </level>
      
      <level name="critical" priority="critical">
        <description>Critical issues that pose significant risk to system stability</description>
        <examples">Security vulnerabilities, data corruption, system crashes</examples>
        <impact">Severe functional impact, potential data loss or security breach</impact>
        <recovery_urgency">Critical priority, immediate resolution required</recovery_urgency>
      </level>
    </severity_levels>
    
    <context_based_severity_adjustment>
      <adjustment_factors>
        <factor name="task_complexity" weight="30%">
          <description>Adjust severity based on task complexity level</description>
          <rules>
            <rule>Simple tasks: Reduce severity by one level for non-critical errors</rule>
            <rule>Complex tasks: Increase severity by one level for potential system impact</rule>
            <rule>Critical tasks: Treat all errors as high priority minimum</rule>
          </rules>
        </factor>
        
        <factor name="system_criticality" weight="25%">
          <description>Adjust severity based on affected system criticality</description>
          <rules>
            <rule>Production systems: Increase severity for all errors</rule>
            <rule>Development systems: Reduce severity for recoverable errors</rule>
            <rule>Test systems: Minimize severity for non-blocking errors</rule>
          </rules>
        </factor>
        
        <factor name="user_impact" weight="25%">
          <description>Adjust severity based on potential user impact</description>
          <rules>
            <rule>High user impact: Increase severity regardless of error type</rule>
            <rule>Medium user impact: Maintain standard severity levels</rule>
            <rule>Low user impact: Reduce severity for non-critical errors</rule>
          </rules>
        </factor>
        
        <factor name="recovery_capability" weight="20%">
          <description>Adjust severity based on recovery capability</description>
          <rules>
            <rule>Easy recovery: Reduce severity for recoverable errors</rule>
            <rule>Difficult recovery: Increase severity for complex recovery scenarios</rule>
            <rule>No recovery: Treat as critical regardless of original severity</rule>
          </rules>
        </factor>
      </adjustment_factors>
    </context_based_severity_adjustment>
  </error_classification_framework>
  
  <adaptive_recovery_strategies>
    <strategy name="auto_fix" complexity="simple_tasks">
      <description>Automated fixes for common, simple errors</description>
      <applicability>
        <error_types>Syntax errors, formatting issues, simple configuration problems</error_types>
        <confidence_threshold>95% confidence in fix correctness</confidence_threshold>
        <risk_level>Low risk of introducing new issues</risk_level>
      </applicability>
      
      <implementation>
        <fix_patterns>
          <pattern name="syntax_correction">Automatic syntax error correction</pattern>
          <pattern name="format_standardization">Apply standard formatting rules</pattern>
          <pattern name="configuration_repair">Fix common configuration issues</pattern>
          <pattern name="dependency_resolution">Resolve simple dependency conflicts</pattern>
        </fix_patterns>
        
        <validation_process>
          <step>Apply automated fix</step>
          <step>Validate fix doesn't introduce new errors</step>
          <step">Run basic functionality tests</step>
          <step>Confirm fix resolves original issue</step>
        </validation_process>
        
        <fallback_mechanism">
          <fallback_condition>Automated fix fails validation</fallback_condition>
          <fallback_action>Escalate to guided recovery</fallback_action>
          <rollback_option">Revert to pre-fix state</rollback_option>
        </fallback_mechanism>
      </implementation>
    </strategy>
    
    <strategy name="guided_recovery" complexity="medium_tasks">
      <description>Step-by-step guidance for manual error resolution</description>
      <applicability>
        <error_types">Logic errors, integration issues, moderate complexity problems</error_types>
        <confidence_threshold">70% confidence in recovery approach</confidence_threshold>
        <risk_level">Medium risk requiring careful manual intervention</risk_level>
      </applicability>
      
      <implementation>
        <guidance_generation>
          <step_by_step_instructions">Generate clear, actionable recovery steps</step_by_step_instructions>
          <context_specific_guidance">Tailor guidance to specific error context</context_specific_guidance>
          <alternative_approaches">Provide multiple recovery approaches</alternative_approaches>
          <risk_warnings">Highlight potential risks and precautions</risk_warnings>
        </guidance_generation>
        
        <interactive_assistance>
          <progress_monitoring">Monitor recovery progress and provide feedback</progress_monitoring>
          <adaptive_guidance">Adjust guidance based on recovery progress</adaptive_guidance>
          <error_detection">Detect new errors introduced during recovery</error_detection>
          <course_correction">Provide course correction if recovery goes off track</course_correction>
        </interactive_assistance>
        
        <validation_checkpoints>
          <checkpoint name="pre_recovery">Validate system state before recovery</checkpoint>
          <checkpoint name="mid_recovery">Validate progress during recovery</checkpoint>
          <checkpoint name="post_recovery">Validate successful recovery completion</checkpoint>
        </validation_checkpoints>
      </implementation>
    </strategy>
    
    <strategy name="escalation_recovery" complexity="complex_tasks">
      <description>Escalation to higher-level recovery procedures</description>
      <applicability>
        <error_types">System-wide failures, complex integration issues, architecture problems</error_types>
        <confidence_threshold">50% confidence requiring expert intervention</confidence_threshold>
        <risk_level">High risk requiring careful analysis and planning</risk_level>
      </applicability>
      
      <implementation>
        <escalation_triggers>
          <trigger name="recovery_failure">Previous recovery attempts failed</trigger>
          <trigger name="complexity_threshold">Error complexity exceeds threshold</trigger>
          <trigger name="risk_assessment">High risk of system damage</trigger>
          <trigger name="expert_required">Technical expertise required</trigger>
        </escalation_triggers>
        
        <escalation_process">
          <step name="context_preparation">Prepare comprehensive error context</step>
          <step name="expert_notification">Notify appropriate technical experts</step>
          <step name="collaborative_analysis">Collaborative analysis of error and recovery options</step>
          <step name="recovery_planning">Develop comprehensive recovery plan</step>
          <step name="monitored_execution">Execute recovery with expert monitoring</step>
        </escalation_process>
        
        <expert_integration>
          <expert_selection">Select appropriate experts based on error type</expert_selection>
          <knowledge_transfer">Transfer error context and analysis to experts</knowledge_transfer>
          <collaborative_tools">Provide tools for collaborative error resolution</collaborative_tools>
          <resolution_documentation">Document expert resolution for future reference</resolution_documentation>
        </expert_integration>
      </implementation>
    </strategy>
    
    <strategy name="emergency_rollback" complexity="critical_tasks">
      <description>Emergency rollback procedures for critical system failures</description>
      <applicability>
        <error_types">Critical system failures, security breaches, data corruption</error_types>
        <confidence_threshold">100% confidence in rollback safety</confidence_threshold>
        <risk_level">Critical risk requiring immediate system restoration</risk_level>
      </applicability>
      
      <implementation>
        <rollback_triggers>
          <trigger name="system_failure">Critical system failure detected</trigger>
          <trigger name="security_breach">Security vulnerability or breach detected</trigger>
          <trigger name="data_integrity">Data corruption or integrity issues</trigger>
          <trigger name="service_unavailability">Service becomes unavailable</trigger>
        </rollback_triggers>
        
        <rollback_process>
          <step name="immediate_isolation">Isolate affected systems immediately</step>
          <step name="state_preservation">Preserve current state for analysis</step>
          <step name="rollback_execution">Execute rollback to known good state</step>
          <step name="system_validation">Validate system integrity after rollback</step>
          <step name="service_restoration">Restore service with monitoring</step>
        </rollback_process>
        
        <emergency_procedures>
          <procedure name="automatic_rollback">Automatic rollback for predefined scenarios</procedure>
          <procedure name="manual_rollback">Manual rollback with expert oversight</procedure>
          <procedure name="partial_rollback">Partial rollback for isolated failures</procedure>
          <procedure name="complete_rollback">Complete system rollback for critical failures</procedure>
        </emergency_procedures>
      </implementation>
    </strategy>
  </adaptive_recovery_strategies>
  
  <intelligent_rollback_system>
    <rollback_granularity>
      <level name="file_level" complexity="simple_tasks">
        <description>Rollback individual files to previous versions</description>
        <applicability">Simple changes affecting single files</applicability>
        <scope">File-specific changes and modifications</scope>
        <risk_level">Low risk, minimal system impact</risk_level>
        <execution_time">< 10 seconds</execution_time>
      </level>
      
      <level name="component_level" complexity="medium_tasks">
        <description>Rollback related components and dependencies</description>
        <applicability">Changes affecting multiple related components</applicability>
        <scope">Component and dependency rollback</scope>
        <risk_level">Medium risk, component-level impact</risk_level>
        <execution_time">< 60 seconds</execution_time>
      </level>
      
      <level name="system_level" complexity="complex_tasks">
        <description>Rollback system-wide changes and configurations</description>
        <applicability">Complex changes affecting system architecture</applicability>
        <scope">System-wide configuration and state rollback</scope>
        <risk_level">High risk, system-wide impact</risk_level>
        <execution_time">< 300 seconds</execution_time>
      </level>
      
      <level name="comprehensive_rollback" complexity="critical_tasks">
        <description>Complete system rollback with audit trail</description>
        <applicability">Critical changes requiring complete system restoration</applicability>
        <scope">Complete system state restoration</scope>
        <risk_level">Critical risk, complete system impact</risk_level>
        <execution_time">< 600 seconds</execution_time>
      </level>
    </rollback_granularity>
    
    <rollback_safety_mechanisms>
      <safety_checks>
        <check name="dependency_validation">Validate rollback won't break dependencies</check>
        <check name="data_integrity">Ensure data integrity during rollback</check>
        <check name="service_continuity">Maintain service continuity during rollback</check>
        <check name="user_impact_assessment">Assess user impact of rollback</check>
      </safety_checks>
      
      <rollback_validation>
        <validation_phase name="pre_rollback">
          <description">Validate rollback safety before execution</description>
          <checks">System state validation, dependency checks, impact assessment</checks>
          <blocking_conditions">Unsafe rollback conditions, data loss risk</blocking_conditions>
        </validation_phase>
        
        <validation_phase name="during_rollback">
          <description>Monitor rollback execution for issues</description>
          <checks">Progress monitoring, error detection, system health</checks>
          <blocking_conditions">Rollback failures, system degradation</blocking_conditions>
        </validation_phase>
        
        <validation_phase name="post_rollback">
          <description>Validate successful rollback completion</description>
          <checks">System functionality, data integrity, service availability</checks>
          <blocking_conditions">Incomplete rollback, system instability</blocking_conditions>
        </validation_phase>
      </rollback_validation>
    </rollback_safety_mechanisms>
  </intelligent_rollback_system>
  
  <context_aware_error_analysis>
    <error_context_collection>
      <context_dimensions>
        <dimension name="technical_context">
          <description>Technical details of error and system state</description>
          <data_points">Error messages, stack traces, system logs, configuration state</data_points>
          <collection_method">Automated collection from system monitoring</collection_method>
          <retention_period">30 days for analysis and pattern recognition</retention_period>
        </dimension>
        
        <dimension name="user_context">
          <description>User actions and context leading to error</description>
          <data_points">User actions, workflows, input data, session state</data_points>
          <collection_method">User session tracking and action logging</collection_method>
          <retention_period">7 days for user experience analysis</retention_period>
        </dimension>
        
        <dimension name="system_context">
          <description>System state and environment during error</description>
          <data_points">System load, resource usage, network state, external dependencies</data_points>
          <collection_method">System monitoring and telemetry</collection_method>
          <retention_period">90 days for system analysis and optimization</retention_period>
        </dimension>
        
        <dimension name="business_context">
          <description>Business impact and criticality of error</description>
          <data_points">Business processes affected, user impact, financial implications</data_points>
          <collection_method">Business impact assessment and user feedback</collection_method>
          <retention_period">1 year for business analysis and planning</retention_period>
        </dimension>
      </context_dimensions>
    </error_context_collection>
    
    <intelligent_error_correlation>
      <correlation_analysis>
        <pattern_recognition">
          <description>Identify patterns in error occurrence and context</description>
          <algorithms">Statistical analysis, machine learning, pattern matching</algorithms>
          <correlation_factors">Time patterns, user patterns, system patterns, error patterns</correlation_factors>
          <insight_generation">Generate insights about error causes and prevention</insight_generation>
        </pattern_recognition>
        
        <root_cause_analysis>
          <description>Analyze root causes of errors using context data</description>
          <methodology">Fishbone analysis, 5 whys, fault tree analysis</methodology>
          <correlation_mapping">Map errors to potential root causes</correlation_mapping>
          <validation_process">Validate root cause hypotheses through testing</validation_process>
        </root_cause_analysis>
        
        <predictive_analysis>
          <description>Predict potential errors based on context patterns</description>
          <prediction_models">Machine learning models for error prediction</prediction_models>
          <early_warning_system">Early warning system for potential errors</early_warning_system>
          <prevention_recommendations">Recommendations for error prevention</prevention_recommendations>
        </predictive_analysis>
      </correlation_analysis>
    </intelligent_error_correlation>
  </context_aware_error_analysis>
  
  <recovery_optimization>
    <recovery_efficiency>
      <optimization_strategies>
        <strategy name="parallel_recovery">
          <description>Execute independent recovery actions in parallel</description>
          <applicability">Multi-component errors with independent recovery paths</applicability>
          <implementation">Parallel execution of recovery actions with coordination</implementation>
          <benefits">Reduced recovery time, improved efficiency</benefits>
        </strategy>
        
        <strategy name="incremental_recovery">
          <description>Implement recovery in incremental steps</description>
          <applicability">Complex errors requiring staged recovery</applicability>
          <implementation">Step-by-step recovery with validation at each stage</implementation>
          <benefits">Reduced risk, easier rollback, better monitoring</benefits>
        </strategy>
        
        <strategy name="predictive_recovery">
          <description>Proactive recovery based on error prediction</description>
          <applicability">Predictable errors with known recovery patterns</applicability>
          <implementation">Pre-emptive recovery actions before error manifestation</implementation>
          <benefits">Reduced downtime, improved user experience</benefits>
        </strategy>
      </optimization_strategies>
    </recovery_efficiency>
    
    <learning_and_adaptation>
      <recovery_learning>
        <learning_mechanisms>
          <mechanism name="success_pattern_learning">Learn from successful recovery patterns</mechanism>
          <mechanism name="failure_pattern_learning">Learn from recovery failures</mechanism>
          <mechanism name="efficiency_optimization">Optimize recovery efficiency based on experience</mechanism>
          <mechanism name="context_adaptation">Adapt recovery strategies to specific contexts</mechanism>
        </learning_mechanisms>
        
        <knowledge_base_evolution>
          <evolution_process">
            <step>Collect recovery data and outcomes</step>
            <step>Analyze patterns and effectiveness</step>
            <step>Update recovery strategies and procedures</step>
            <step>Validate improvements through testing</step>
          </evolution_process>
          
          <continuous_improvement>
            <improvement_cycle">Monthly review and optimization of recovery strategies</improvement_cycle>
            <feedback_integration">Integration of user feedback and expert insights</feedback_integration>
            <best_practice_sharing">Sharing of best practices across teams</best_practice_sharing>
          </continuous_improvement>
        </knowledge_base_evolution>
      </recovery_learning>
    </learning_and_adaptation>
  </recovery_optimization>
  
  <user_experience_optimization>
    <user_centric_recovery>
      <user_impact_minimization>
        <strategy name="transparent_recovery">
          <description">Provide clear communication about recovery progress</description>
          <implementation">Real-time status updates, progress indicators, time estimates</implementation>
          <user_benefits">Reduced anxiety, better planning, improved trust</user_benefits>
        </strategy>
        
        <strategy name="graceful_degradation">
          <description>Maintain partial functionality during recovery</description>
          <implementation">Selective service degradation, alternative workflows</implementation>
          <user_benefits">Continued productivity, minimal disruption</user_benefits>
        </strategy>
        
        <strategy name="user_choice_recovery">
          <description>Provide users with recovery options and choices</description>
          <implementation">Multiple recovery paths, user preference consideration</implementation>
          <user_benefits">User control, personalized experience</user_benefits>
        </strategy>
      </user_impact_minimization>
    </user_centric_recovery>
    
    <recovery_communication">
      <communication_strategies>
        <strategy name="proactive_communication">
          <description">Proactive communication about potential issues</description>
          <channels">Email, dashboard notifications, system alerts</channels>
          <timing">Before issues occur, early warning system</timing>
          <content">Clear, actionable information with next steps</content>
        </strategy>
        
        <strategy name="real_time_updates">
          <description">Real-time updates during recovery process</description>
          <channels">Dashboard, mobile notifications, status pages</channels>
          <timing">Continuous updates during recovery</timing>
          <content">Progress indicators, time estimates, completion status</content>
        </strategy>
        
        <strategy name="post_recovery_communication">
          <description>Communication after recovery completion</description>
          <channels">Email, system notifications, reports</channels>
          <timing">Immediately after recovery completion</timing>
          <content">Recovery summary, lessons learned, prevention measures</content>
        </strategy>
      </communication_strategies>
    </recovery_communication>
  </user_experience_optimization>
  
  <success_metrics>
    <recovery_effectiveness>
      <metric name="recovery_success_rate">Percentage of errors successfully recovered</metric>
      <metric name="recovery_time">Average time to recover from errors by severity</metric>
      <metric name="recovery_accuracy">Accuracy of recovery strategy selection</metric>
      <metric name="rollback_success_rate">Success rate of rollback operations</metric>
    </recovery_effectiveness>
    
    <user_experience_metrics>
      <metric name="user_satisfaction">User satisfaction with error recovery experience</metric>
      <metric name="downtime_reduction">Reduction in user-facing downtime</metric>
      <metric name="recovery_transparency">User perception of recovery transparency</metric>
      <metric name="trust_metrics">User trust in system reliability</metric>
    </user_experience_metrics>
    
    <system_reliability_metrics>
      <metric name="error_recurrence_rate">Rate of error recurrence after recovery</metric>
      <metric name="system_stability">System stability after recovery operations</metric>
      <metric name="recovery_overhead">Resource overhead of recovery operations</metric>
      <metric name="learning_effectiveness">Effectiveness of recovery learning and adaptation</metric>
    </system_reliability_metrics>
  </success_metrics>
  
  <integration_points>
    <depends_on>
      quality/context-sensitive-quality-assessment.md for complexity classification
      quality/adaptive-quality-gates.md for error detection and escalation
      quality/quality-metrics-dashboard.md for error monitoring and reporting
      patterns/tool-usage.md for recovery execution optimization
    </depends_on>
    <provides_to>
      All quality modules for error recovery capabilities
      development/task-management.md for task-specific error recovery
      quality/quality-metrics-dashboard.md for recovery metrics and analysis
      patterns/intelligent-routing.md for recovery-aware routing decisions
    </provides_to>
  </integration_points>
  
</module>
</module>
</error_classification_framework>
</severity_levels>
</level>
</impact">
</recovery_urgency">
</level>
</examples">
</impact">
</recovery_urgency">
</level>
</examples">
</impact">
</recovery_urgency">
</adaptive_recovery_strategies>
</strategy>
</implementation>
</validation_process>
</step">
</fallback_mechanism">
</rollback_option">
</strategy>
</applicability>
</error_types">
</confidence_threshold">
</risk_level">
</implementation>
</guidance_generation>
</step_by_step_instructions">
</context_specific_guidance">
</alternative_approaches">
</risk_warnings">
</interactive_assistance>
</progress_monitoring">
</adaptive_guidance">
</error_detection">
</course_correction">
</strategy>
</applicability>
</error_types">
</confidence_threshold">
</risk_level">
</implementation>
</escalation_process">
</expert_integration>
</expert_selection">
</knowledge_transfer">
</collaborative_tools">
</resolution_documentation">
</strategy>
</applicability>
</error_types">
</confidence_threshold">
</risk_level">
</intelligent_rollback_system>
</rollback_granularity>
</level>
</applicability">
</scope">
</risk_level">
</execution_time">
</level>
</applicability">
</scope">
</risk_level">
</execution_time">
</level>
</applicability">
</scope">
</risk_level">
</execution_time">
</level>
</applicability">
</scope">
</risk_level">
</execution_time">
</rollback_safety_mechanisms>
</rollback_validation>
</validation_phase>
</description">
</checks">
</blocking_conditions">
</validation_phase>
</checks">
</blocking_conditions">
</validation_phase>
</checks">
</blocking_conditions">
</context_aware_error_analysis>
</error_context_collection>
</context_dimensions>
</dimension>
</data_points">
</collection_method">
</retention_period">
</dimension>
</data_points">
</collection_method">
</retention_period">
</dimension>
</data_points">
</collection_method">
</retention_period">
</dimension>
</data_points">
</collection_method">
</retention_period">
</intelligent_error_correlation>
</correlation_analysis>
</pattern_recognition">
</algorithms">
</correlation_factors">
</insight_generation">
</root_cause_analysis>
</methodology">
</correlation_mapping">
</validation_process">
</predictive_analysis>
</prediction_models">
</early_warning_system">
</prevention_recommendations">
</recovery_optimization>
</recovery_efficiency>
</optimization_strategies>
</strategy>
</applicability">
</implementation">
</benefits">
</strategy>
</applicability">
</implementation">
</benefits">
</strategy>
</applicability">
</implementation">
</benefits">
</learning_and_adaptation>
</recovery_learning>
</knowledge_base_evolution>
</evolution_process">
</continuous_improvement>
</improvement_cycle">
</feedback_integration">
</best_practice_sharing">
</user_experience_optimization>
</user_centric_recovery>
</user_impact_minimization>
</strategy>
</description">
</implementation">
</user_benefits">
</strategy>
</implementation">
</user_benefits">
</strategy>
</implementation">
</user_benefits">
</recovery_communication">
</communication_strategies>
</strategy>
</description">
</channels">
</timing">
</content">
</strategy>
</description">
</channels">
</timing">
</content">
</strategy>
</channels">
</timing">
</content">
```

────────────────────────────────────────────────────────────────────────────────

*Intelligent error recovery system that provides context-appropriate error handling and rollback mechanisms, scaling response from simple fixes to comprehensive recovery based on task complexity and error severity.*