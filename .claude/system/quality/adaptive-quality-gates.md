| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Adaptive Quality Gates Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="adaptive_quality_gates" category="quality">
  
  <purpose>
    Dynamic quality gates that adapt their enforcement level and requirements based on task complexity, providing efficient quality validation while maintaining appropriate rigor for different scenarios.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>complexity_classification, task_context, risk_assessment</required>
      <optional>performance_requirements, security_requirements, compliance_requirements</optional>
    </inputs>
    <outputs>
      <success>adapted_gate_set, enforcement_levels, validation_strategy, quality_plan</success>
      <failure>gate_selection_errors, enforcement_conflicts, validation_failures</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Analyze task complexity and context from context-sensitive assessment
      2. Select appropriate quality gates based on complexity level
      3. Adapt enforcement levels and validation strategies
      4. Configure performance thresholds and validation criteria
      5. Generate quality validation plan with clear rationale
    </claude_4_behavior>
  </execution_pattern>
  
  <gate_adaptation_framework>
    <adaptation_principles>
      <principle name="proportional_rigor">Quality rigor should be proportional to task complexity and risk</principle>
      <principle name="efficiency_optimization">Minimize overhead while maintaining necessary quality standards</principle>
      <principle name="context_awareness">Gates should adapt to specific task context and requirements</principle>
      <principle name="progressive_enforcement">Start with basic gates, escalate as complexity increases</principle>
      <principle name="intelligent_selection">Use intelligent analysis to select most relevant gates</principle>
    </adaptation_principles>
    
    <complexity_gate_mapping>
      <simple_task_gates>
        <core_gates>
          <gate name="syntax_validation" enforcement="BLOCKING" priority="critical">
            <description>Basic syntax and format validation</description>
            <criteria>Code compiles/parses without errors</criteria>
            <execution_time>< 10 seconds</execution_time>
            <automation_level>Fully automated</automation_level>
          </gate>
          <gate name="basic_functionality" enforcement="BLOCKING" priority="critical">
            <description>Core functionality works as expected</description>
            <criteria>Basic functionality tests pass</criteria>
            <execution_time>< 30 seconds</execution_time>
            <automation_level>Fully automated</automation_level>
          </gate>
        </core_gates>
        <optional_gates>
          <gate name="style_compliance" enforcement="CONDITIONAL" priority="low">
            <description>Code style and formatting compliance</description>
            <criteria>Style guide compliance with minor violations allowed</criteria>
            <execution_time>< 5 seconds</execution_time>
            <automation_level>Fully automated</automation_level>
          </gate>
          <gate name="documentation_check" enforcement="CONDITIONAL" priority="low">
            <description>Basic documentation presence</description>
            <criteria>Key functions have basic documentation</criteria>
            <execution_time>< 5 seconds</execution_time>
            <automation_level>Fully automated</automation_level>
          </gate>
        </optional_gates>
      </simple_task_gates>
      
      <medium_task_gates>
        <core_gates>
          <gate name="code_quality_standards" enforcement="BLOCKING" priority="critical">
            <description>Standard code quality requirements</description>
            <criteria>Code quality metrics within acceptable limits</criteria>
            <execution_time>< 60 seconds</execution_time>
            <automation_level>Mostly automated</automation_level>
          </gate>
          <gate name="unit_test_coverage" enforcement="BLOCKING" priority="critical">
            <description>Adequate unit test coverage</description>
            <criteria>Unit test coverage > 75% for modified code</criteria>
            <execution_time>< 120 seconds</execution_time>
            <automation_level>Automated with manual review</automation_level>
          </gate>
          <gate name="integration_validation" enforcement="BLOCKING" priority="high">
            <description>Component integration validation</description>
            <criteria>Integration tests pass for affected components</criteria>
            <execution_time>< 180 seconds</execution_time>
            <automation_level>Mostly automated</automation_level>
          </gate>
        </core_gates>
        <conditional_gates>
          <gate name="performance_check" enforcement="CONDITIONAL" priority="medium">
            <description>Basic performance validation</description>
            <criteria>Performance within acceptable ranges</criteria>
            <execution_time>< 60 seconds</execution_time>
            <automation_level>Automated with thresholds</automation_level>
          </gate>
          <gate name="security_review" enforcement="CONDITIONAL" priority="medium">
            <description>Basic security considerations</description>
            <criteria>No obvious security vulnerabilities</criteria>
            <execution_time>< 30 seconds</execution_time>
            <automation_level>Automated scanning</automation_level>
          </gate>
        </conditional_gates>
      </medium_task_gates>
      
      <complex_task_gates>
        <core_gates>
          <gate name="comprehensive_tdd" enforcement="BLOCKING" priority="critical">
            <description>Full TDD cycle enforcement</description>
            <criteria>Complete RED-GREEN-REFACTOR cycle documented</criteria>
            <execution_time>No time limit</execution_time>
            <automation_level>Manual verification required</automation_level>
          </gate>
          <gate name="architecture_validation" enforcement="BLOCKING" priority="critical">
            <description>System architecture integrity</description>
            <criteria>Architecture patterns and principles maintained</criteria>
            <execution_time>< 300 seconds</execution_time>
            <automation_level>Automated analysis with manual review</automation_level>
          </gate>
          <gate name="comprehensive_testing" enforcement="BLOCKING" priority="critical">
            <description>Comprehensive test coverage</description>
            <criteria>Test coverage > 90% with quality assertions</criteria>
            <execution_time>< 600 seconds</execution_time>
            <automation_level>Automated with manual verification</automation_level>
          </gate>
          <gate name="performance_validation" enforcement="BLOCKING" priority="high">
            <description>Performance requirements validation</description>
            <criteria>Performance meets specified requirements</criteria>
            <execution_time>< 300 seconds</execution_time>
            <automation_level>Automated benchmarking</automation_level>
          </gate>
        </core_gates>
        <security_gates>
          <gate name="security_assessment" enforcement="BLOCKING" priority="high">
            <description>Security impact assessment</description>
            <criteria>Security review completed with no high/critical issues</criteria>
            <execution_time>< 180 seconds</execution_time>
            <automation_level>Automated scanning with manual review</automation_level>
          </gate>
        </security_gates>
      </complex_task_gates>
      
      <critical_task_gates>
        <comprehensive_gates>
          <gate name="maximum_quality_validation" enforcement="BLOCKING" priority="critical">
            <description>All quality gates from universal quality gates module</description>
            <criteria>All universal quality gates pass</criteria>
            <execution_time>No time limit</execution_time>
            <automation_level>Mix of automated and manual processes</automation_level>
          </gate>
          <gate name="security_audit" enforcement="BLOCKING" priority="critical">
            <description>Comprehensive security audit</description>
            <criteria>Full security audit with zero critical/high issues</criteria>
            <execution_time>No time limit</execution_time>
            <automation_level>Manual security review required</automation_level>
          </gate>
          <gate name="compliance_validation" enforcement="BLOCKING" priority="critical">
            <description>Regulatory compliance validation</description>
            <criteria>All applicable compliance requirements met</criteria>
            <execution_time>No time limit</execution_time>
            <automation_level>Manual compliance review</automation_level>
          </gate>
          <gate name="disaster_recovery" enforcement="BLOCKING" priority="critical">
            <description>Disaster recovery and rollback validation</description>
            <criteria>Rollback procedures tested and verified</criteria>
            <execution_time>No time limit</execution_time>
            <automation_level>Manual testing required</automation_level>
          </gate>
        </comprehensive_gates>
      </critical_task_gates>
    </complexity_gate_mapping>
  </gate_adaptation_framework>
  
  <intelligent_gate_selection>
    <selection_algorithms>
      <risk_based_selection>
        <high_risk_indicators>
          <indicator>Production system modification</indicator>
          <indicator>Security-sensitive code changes</indicator>
          <indicator>Database schema modifications</indicator>
          <indicator>User authentication/authorization changes</indicator>
          <indicator>Performance-critical path modifications</indicator>
        </high_risk_indicators>
        <medium_risk_indicators>
          <indicator>Business logic modifications</indicator>
          <indicator>API interface changes</indicator>
          <indicator>Configuration changes</indicator>
          <indicator>Third-party integration modifications</indicator>
        </medium_risk_indicators>
        <low_risk_indicators>
          <indicator>Documentation updates</indicator>
          <indicator>Code formatting changes</indicator>
          <indicator>Comment additions</indicator>
          <indicator>Non-functional refactoring</indicator>
        </low_risk_indicators>
      </risk_based_selection>
      
      <context_based_selection>
        <development_context>
          <new_feature_development>Enhanced gate set with comprehensive testing</new_feature_development>
          <bug_fixing>Focused gate set with regression testing</bug_fixing>
          <refactoring>Architecture and quality focused gates</refactoring>
          <maintenance>Basic gate set with integration focus</maintenance>
        </development_context>
        
        <environmental_context>
          <development_environment>Relaxed enforcement with fast feedback</development_environment>
          <staging_environment>Standard enforcement with integration focus</staging_environment>
          <production_environment>Maximum enforcement with comprehensive validation</production_environment>
        </environmental_context>
      </context_based_selection>
      
      <dynamic_gate_escalation>
        <escalation_triggers>
          <trigger name="test_failure">Escalate to higher quality level on test failures</trigger>
          <trigger name="security_concern">Escalate to security-focused gates</trigger>
          <trigger name="performance_issue">Escalate to performance-focused gates</trigger>
          <trigger name="complexity_increase">Escalate when complexity analysis changes</trigger>
        </escalation_triggers>
        
        <escalation_strategies>
          <strategy name="gradual_escalation">Gradually increase gate rigor</strategy>
          <strategy name="context_escalation">Escalate based on specific context</strategy>
          <strategy name="risk_escalation">Escalate based on risk assessment</strategy>
          <strategy name="failure_escalation">Escalate based on failure patterns</strategy>
        </escalation_strategies>
      </dynamic_gate_escalation>
    </selection_algorithms>
  </intelligent_gate_selection>
  
  <adaptive_enforcement_mechanisms>
    <enforcement_levels>
      <level name="strict_blocking" description="Hard blocking, no exceptions">
        <conditions>Critical tasks, security-sensitive changes, production deployments</conditions>
        <behavior>Complete halt until requirements satisfied</behavior>
        <escalation>Immediate escalation to human oversight</escalation>
        <rollback>Automatic rollback on failure</rollback>
      </level>
      
      <level name="conditional_blocking" description="Blocking with alternative paths">
        <conditions>Medium to complex tasks, standard development</conditions>
        <behavior>Block with alternative workflows available</behavior>
        <escalation>Escalation after retry attempts</escalation>
        <rollback>Conditional rollback based on failure type</rollback>
      </level>
      
      <level name="warning_with_override" description="Warning with manual override">
        <conditions>Simple tasks, non-critical changes</conditions>
        <behavior>Warn but allow override with justification</behavior>
        <escalation>Log override for review</escalation>
        <rollback>Optional rollback with user confirmation</rollback>
      </level>
      
      <level name="informational_only" description="Information without blocking">
        <conditions>Documentation, formatting, minor changes</conditions>
        <behavior>Provide information without blocking</behavior>
        <escalation>No escalation required</escalation>
        <rollback>No rollback needed</rollback>
      </level>
    </enforcement_levels>
    
    <dynamic_enforcement_adjustment>
      <adjustment_criteria>
        <failure_rate>Adjust enforcement based on historical failure rates</failure_rate>
        <user_experience>Adjust based on user feedback and satisfaction</user_experience>
        <efficiency_metrics>Adjust based on efficiency and productivity metrics</efficiency_metrics>
        <quality_outcomes">Adjust based on quality outcomes and defect rates</quality_outcomes>
      </adjustment_criteria>
      
      <adjustment_algorithms>
        <algorithm name="feedback_learning">Learn from user feedback and adjust accordingly</algorithm>
        <algorithm name="pattern_recognition">Recognize patterns and adjust enforcement</algorithm>
        <algorithm name="performance_optimization">Optimize enforcement for performance</algorithm>
        <algorithm name="quality_maintenance">Maintain quality while optimizing efficiency</algorithm>
      </adjustment_algorithms>
    </dynamic_enforcement_adjustment>
  </adaptive_enforcement_mechanisms>
  
  <performance_adaptive_validation>
    <performance_gate_adaptation>
      <simple_task_performance>
        <validation_scope>Basic functionality only</validation_scope>
        <thresholds>Relaxed performance thresholds</thresholds>
        <testing_depth>Minimal performance testing</testing_depth>
        <execution_time>< 30 seconds</execution_time>
      </simple_task_performance>
      
      <medium_task_performance>
        <validation_scope>Affected workflows and components</validation_scope>
        <thresholds>Standard performance thresholds</thresholds>
        <testing_depth>Focused performance testing</testing_depth>
        <execution_time>< 120 seconds</execution_time>
      </medium_task_performance>
      
      <complex_task_performance>
        <validation_scope>System-wide performance validation</validation_scope>
        <thresholds>Strict performance thresholds</thresholds>
        <testing_depth>Comprehensive performance testing</testing_depth>
        <execution_time>< 600 seconds</execution_time>
      </complex_task_performance>
      
      <critical_task_performance>
        <validation_scope>Complete system performance audit</validation_scope>
        <thresholds>Maximum performance thresholds</thresholds>
        <testing_depth>Extensive performance validation</testing_depth>
        <execution_time>No time limit</execution_time>
      </critical_task_performance>
    </performance_gate_adaptation>
    
    <intelligent_threshold_adjustment>
      <baseline_establishment>
        <current_performance>Establish baseline from current system performance</current_performance>
        <historical_data>Use historical performance data for context</historical_data>
        <industry_standards>Reference industry standards for comparison</industry_standards>
        <user_expectations>Consider user expectations and requirements</user_expectations>
      </baseline_establishment>
      
      <adaptive_thresholds>
        <dynamic_adjustment>Adjust thresholds based on system capacity</dynamic_adjustment>
        <context_awareness">Adjust based on task context and requirements</context_awareness>
        <load_consideration>Consider current system load and capacity</load_consideration>
        <trend_analysis">Analyze performance trends for threshold optimization</trend_analysis>
      </adaptive_thresholds>
    </intelligent_threshold_adjustment>
  </performance_adaptive_validation>
  
  <quality_feedback_loop>
    <continuous_improvement>
      <effectiveness_monitoring>
        <gate_success_rates>Monitor success rates for different gate types</gate_success_rates>
        <false_positive_tracking">Track false positive rates for optimization</false_positive_tracking>
        <user_satisfaction">Monitor user satisfaction with gate enforcement</user_satisfaction>
        <efficiency_metrics">Track efficiency improvements from adaptive approach</efficiency_metrics>
      </effectiveness_monitoring>
      
      <adaptation_learning>
        <pattern_recognition>Recognize patterns in gate effectiveness</pattern_recognition>
        <user_behavior_analysis">Analyze user behavior and preferences</user_behavior_analysis>
        <quality_outcome_correlation">Correlate gate enforcement with quality outcomes</quality_outcome_correlation>
        <optimization_identification">Identify optimization opportunities</optimization_identification>
      </adaptation_learning>
    </continuous_improvement>
    
    <feedback_integration>
      <real_time_adjustment>
        <immediate_feedback>Incorporate immediate feedback for quick adjustments</immediate_feedback>
        <session_learning">Learn within session for immediate improvements</session_learning>
        <context_memory">Remember context-specific preferences and adjustments</context_memory>
        <user_preferences">Adapt to individual user preferences and patterns</user_preferences>
      </real_time_adjustment>
      
      <long_term_optimization>
        <trend_analysis">Analyze long-term trends for systematic improvements</trend_analysis>
        <pattern_evolution">Evolve patterns based on accumulated experience</pattern_evolution>
        <systematic_updates">Implement systematic updates based on learning</systematic_updates>
        <quality_evolution">Evolve quality standards based on outcomes</quality_evolution>
      </long_term_optimization>
    </feedback_integration>
  </quality_feedback_loop>
  
  <integration_with_existing_systems>
    <universal_quality_gates_integration>
      <gate_inheritance>Inherit comprehensive gates from universal quality gates</gate_inheritance>
      <selective_application">Apply gates selectively based on context</selective_application>
      <enhancement_layer">Add adaptive layer on top of existing gates</enhancement_layer>
      <backward_compatibility">Maintain backward compatibility with existing systems</backward_compatibility>
    </universal_quality_gates_integration>
    
    <tdd_integration>
      <adaptive_tdd_enforcement">Adapt TDD enforcement based on task complexity</adaptive_tdd_enforcement>
      <smart_test_selection">Select appropriate testing strategies</smart_test_selection>
      <cycle_optimization">Optimize TDD cycle based on context</cycle_optimization>
      <quality_correlation">Correlate TDD compliance with quality outcomes</quality_correlation>
    </tdd_integration>
    
    <command_integration>
      <command_specific_adaptation">Adapt gates for specific commands</command_specific_adaptation>
      <routing_integration">Integrate with intelligent routing for quality-aware decisions</routing_integration>
      <session_awareness">Adapt based on session context and history</session_awareness>
      <workflow_optimization">Optimize workflow based on quality requirements</workflow_optimization>
    </command_integration>
  </integration_with_existing_systems>
  
  <success_metrics>
    <efficiency_improvements>
      <time_savings>Measure time savings from adaptive approach</time_savings>
      <overhead_reduction">Track overhead reduction for different complexity levels</overhead_reduction>
      <user_productivity">Monitor user productivity improvements</user_productivity>
      <system_efficiency">Track overall system efficiency improvements</system_efficiency>
    </efficiency_improvements>
    
    <quality_maintenance>
      <defect_rates">Monitor defect rates across complexity levels</defect_rates>
      <quality_scores">Track quality scores and trends</quality_scores>
      <user_satisfaction">Monitor user satisfaction with quality process</user_satisfaction>
      <system_reliability">Track system reliability and stability</system_reliability>
    </quality_maintenance>
    
    <adaptation_effectiveness>
      <classification_accuracy">Track accuracy of complexity classification</classification_accuracy>
      <gate_relevance">Monitor relevance of selected gates</gate_relevance>
      <enforcement_appropriateness">Track appropriateness of enforcement levels</enforcement_appropriateness>
      <learning_effectiveness">Monitor effectiveness of continuous learning</learning_effectiveness>
    </adaptation_effectiveness>
  </success_metrics>
  
  <integration_points>
    <depends_on>
      quality/context-sensitive-quality-assessment.md for complexity classification
      quality/universal-quality-gates.md for comprehensive gate definitions
      quality/tdd.md for TDD enforcement patterns
      patterns/tool-usage.md for parallel execution optimization
    </depends_on>
    <provides_to>
      All commands for adaptive quality gate enforcement
      quality/framework-metrics.md for quality measurement
      development/task-management.md for task-specific quality integration
      patterns/intelligent-routing.md for quality-aware routing
    </provides_to>
  </integration_points>
  
</module>
</module>
</adaptive_enforcement_mechanisms>
</dynamic_enforcement_adjustment>
</adjustment_criteria>
</quality_outcomes">
</performance_adaptive_validation>
</intelligent_threshold_adjustment>
</adaptive_thresholds>
</context_awareness">
</trend_analysis">
</quality_feedback_loop>
</continuous_improvement>
</effectiveness_monitoring>
</false_positive_tracking">
</user_satisfaction">
</efficiency_metrics">
</adaptation_learning>
</user_behavior_analysis">
</quality_outcome_correlation">
</optimization_identification">
</feedback_integration>
</real_time_adjustment>
</session_learning">
</context_memory">
</user_preferences">
</long_term_optimization>
</trend_analysis">
</pattern_evolution">
</systematic_updates">
</quality_evolution">
</integration_with_existing_systems>
</universal_quality_gates_integration>
</selective_application">
</enhancement_layer">
</backward_compatibility">
</tdd_integration>
</adaptive_tdd_enforcement">
</smart_test_selection">
</cycle_optimization">
</quality_correlation">
</command_integration>
</command_specific_adaptation">
</routing_integration">
</session_awareness">
</workflow_optimization">
</success_metrics>
</efficiency_improvements>
</overhead_reduction">
</user_productivity">
</system_efficiency">
</quality_maintenance>
</defect_rates">
</quality_scores">
</user_satisfaction">
</system_reliability">
</adaptation_effectiveness>
</classification_accuracy">
</gate_relevance">
</enforcement_appropriateness">
</learning_effectiveness">
```

────────────────────────────────────────────────────────────────────────────────

*Dynamic quality gates that adapt enforcement and requirements based on task complexity, providing efficient quality validation while maintaining appropriate rigor.*