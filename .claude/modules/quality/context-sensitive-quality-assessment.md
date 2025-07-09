| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | active |

# Context-Sensitive Quality Assessment Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="context_sensitive_quality_assessment" category="quality">
  
  <purpose>
    Intelligent quality assessment system that adapts appropriate quality measures based on task complexity and requirements, providing 60% reduction in quality overhead for simple tasks while maintaining rigorous standards where needed.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>task_description, file_count, modification_scope, business_criticality</required>
      <optional>existing_tests, performance_requirements, security_requirements, user_impact</optional>
    </inputs>
    <outputs>
      <success>complexity_classification, quality_level, adapted_gates, testing_strategy, performance_thresholds</success>
      <failure>classification_errors, insufficient_context, ambiguous_requirements</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Analyze task characteristics using multi-dimensional complexity assessment
      2. Classify task complexity level with confidence scoring
      3. Select appropriate quality gates and testing strategies
      4. Adapt performance thresholds and validation requirements
      5. Generate context-sensitive quality plan with clear rationale
    </claude_4_behavior>
  </execution_pattern>
  
  <complexity_classification>
    <classification_dimensions>
      <dimension name="scope">
        <simple>Single file modification, <50 lines changed</simple>
        <medium>Multiple file changes, <5 files, <500 lines total</medium>
        <complex>System-wide changes, >5 files, integration dependencies</complex>
        <critical>Production systems, security-sensitive, high user impact</critical>
      </dimension>
      
      <dimension name="risk_level">
        <low>Documentation, configuration, non-functional changes</low>
        <medium>Feature enhancements, bug fixes, refactoring</medium>
        <high>Architecture changes, performance optimizations, security updates</high>
        <critical>Core system modifications, data handling, user authentication</critical>
      </dimension>
      
      <dimension name="testing_requirements">
        <minimal>Syntax validation, basic functionality checks</minimal>
        <standard>Unit tests, integration testing, code quality checks</standard>
        <comprehensive>Full TDD cycle, performance testing, security validation</comprehensive>
        <extensive>End-to-end testing, load testing, security auditing, compliance validation</extensive>
      </dimension>
      
      <dimension name="performance_sensitivity">
        <none>No performance impact expected</none>
        <low>Minor performance considerations</low>
        <medium>Moderate performance requirements (p95 < 500ms)</medium>
        <high>Strict performance requirements (p95 < 200ms)</high>
        <critical>Real-time performance requirements (p95 < 50ms)</critical>
      </dimension>
    </classification_dimensions>
    
    <classification_algorithm>
      <weighted_scoring>
        <weight dimension="scope">30%</weight>
        <weight dimension="risk_level">35%</weight>
        <weight dimension="testing_requirements">20%</weight>
        <weight dimension="performance_sensitivity">15%</weight>
      </weighted_scoring>
      
      <scoring_thresholds>
        <simple_task>Score 0-25: Basic quality checks, minimal testing</simple_task>
        <medium_task>Score 26-50: Standard quality gates, integrated testing</medium_task>
        <complex_task>Score 51-75: Comprehensive quality validation, full TDD cycle</complex_task>
        <critical_task>Score 76-100: Maximum quality enforcement, extensive validation</critical_task>
      </scoring_thresholds>
      
      <confidence_scoring>
        <high_confidence>All dimensions clearly defined, unambiguous context</high_confidence>
        <medium_confidence>Most dimensions clear, some assumptions required</medium_confidence>
        <low_confidence>Limited context, significant assumptions, human review recommended</low_confidence>
      </confidence_scoring>
    </classification_algorithm>
  </complexity_classification>
  
  <adaptive_quality_levels>
    <level name="simple_task" efficiency_target="60% overhead reduction">
      <description>Single file changes, documentation updates, configuration modifications</description>
      <quality_gates>
        <gate name="syntax_validation" enforcement="BLOCKING">Basic syntax and format validation</gate>
        <gate name="functionality_check" enforcement="BLOCKING">Core functionality verification</gate>
        <gate name="integration_impact" enforcement="CONDITIONAL">Check integration dependencies</gate>
      </quality_gates>
      <testing_strategy>
        <approach>Lightweight validation with automated checks</approach>
        <coverage_requirement>Basic functionality coverage (>60%)</coverage_requirement>
        <test_types>Unit tests for modified functions only</test_types>
        <performance_validation>Basic performance check if applicable</performance_validation>
      </testing_strategy>
      <validation_time_target>< 2 minutes</validation_time_target>
    </level>
    
    <level name="medium_task" efficiency_target="30% overhead reduction">
      <description>Multi-file changes, feature enhancements, moderate complexity</description>
      <quality_gates>
        <gate name="code_quality_standards" enforcement="BLOCKING">Standard code quality requirements</gate>
        <gate name="integration_testing" enforcement="BLOCKING">Component integration validation</gate>
        <gate name="performance_validation" enforcement="CONDITIONAL">Performance threshold validation</gate>
        <gate name="security_review" enforcement="CONDITIONAL">Basic security considerations</gate>
      </quality_gates>
      <testing_strategy>
        <approach>Balanced testing with focus on changed components</approach>
        <coverage_requirement>Good coverage of modified areas (>75%)</coverage_requirement>
        <test_types>Unit tests, integration tests for affected components</test_types>
        <performance_validation>Performance testing for affected workflows</performance_validation>
      </testing_strategy>
      <validation_time_target>< 10 minutes</validation_time_target>
    </level>
    
    <level name="complex_task" efficiency_target="Maintain thoroughness">
      <description>System-wide changes, architectural modifications, high complexity</description>
      <quality_gates>
        <gate name="comprehensive_tdd" enforcement="BLOCKING">Full TDD cycle enforcement</gate>
        <gate name="architecture_validation" enforcement="BLOCKING">System architecture integrity</gate>
        <gate name="performance_testing" enforcement="BLOCKING">Comprehensive performance validation</gate>
        <gate name="security_assessment" enforcement="BLOCKING">Security impact assessment</gate>
        <gate name="integration_validation" enforcement="BLOCKING">End-to-end integration testing</gate>
      </quality_gates>
      <testing_strategy>
        <approach>Comprehensive testing with full TDD cycle</approach>
        <coverage_requirement>High coverage requirements (>90%)</coverage_requirement>
        <test_types>Unit, integration, end-to-end, performance tests</test_types>
        <performance_validation>Full performance validation against requirements</performance_validation>
      </testing_strategy>
      <validation_time_target>< 30 minutes</validation_time_target>
    </level>
    
    <level name="critical_task" efficiency_target="Maximum thoroughness">
      <description>Production-critical changes, security-sensitive, high user impact</description>
      <quality_gates>
        <gate name="maximum_validation" enforcement="BLOCKING">All universal quality gates</gate>
        <gate name="security_audit" enforcement="BLOCKING">Comprehensive security audit</gate>
        <gate name="performance_benchmarking" enforcement="BLOCKING">Performance benchmarking</gate>
        <gate name="compliance_validation" enforcement="BLOCKING">Regulatory compliance check</gate>
        <gate name="rollback_validation" enforcement="BLOCKING">Rollback capability verification</gate>
      </quality_gates>
      <testing_strategy>
        <approach>Exhaustive testing with all validation types</approach>
        <coverage_requirement>Maximum coverage requirements (>95%)</coverage_requirement>
        <test_types>All test types including security, load, stress, compliance</test_types>
        <performance_validation>Comprehensive performance validation with benchmarking</performance_validation>
      </testing_strategy>
      <validation_time_target>No time limit - thoroughness priority</validation_time_target>
    </level>
  </adaptive_quality_levels>
  
  <context_analysis_engine>
    <task_characteristics_analyzer>
      <file_analysis>
        <file_count_assessment>Count and analyze files being modified</file_count_assessment>
        <modification_scope>Assess scope and depth of changes</modification_scope>
        <dependency_impact>Analyze impact on system dependencies</dependency_impact>
        <criticality_assessment>Evaluate business criticality of affected components</criticality_assessment>
      </file_analysis>
      
      <change_impact_analysis>
        <functional_impact>Assess impact on system functionality</functional_impact>
        <performance_impact>Evaluate potential performance implications</performance_impact>
        <security_impact>Analyze security implications of changes</security_impact>
        <user_impact>Assess impact on user experience and workflows</user_impact>
      </change_impact_analysis>
      
      <risk_assessment>
        <technical_risk>Evaluate technical risks and complexity</technical_risk>
        <business_risk>Assess business impact and risk exposure</business_risk>
        <operational_risk>Evaluate operational risks and deployment concerns</operational_risk>
        <compliance_risk>Assess regulatory and compliance implications</compliance_risk>
      </risk_assessment>
    </task_characteristics_analyzer>
    
    <intelligent_gate_selection>
      <gate_prioritization>
        <essential_gates>Gates that are always required regardless of complexity</essential_gates>
        <conditional_gates>Gates that depend on specific conditions or risk levels</conditional_gates>
        <optional_gates>Gates that enhance quality but aren't strictly necessary</optional_gates>
        <contextual_gates>Gates that are added based on specific context or requirements</contextual_gates>
      </gate_prioritization>
      
      <dynamic_enforcement>
        <blocking_criteria>Conditions that require blocking enforcement</blocking_criteria>
        <conditional_criteria>Conditions that allow conditional enforcement</conditional_criteria>
        <warning_criteria>Conditions that warrant warnings but not blocking</warning_criteria>
        <informational_criteria>Conditions that provide informational feedback</informational_criteria>
      </dynamic_enforcement>
    </intelligent_gate_selection>
  </context_analysis_engine>
  
  <progressive_testing_integration>
    <testing_level_progression>
      <level_1_basic>
        <description>Minimal testing for simple changes</description>
        <test_types>Syntax validation, basic functionality</test_types>
        <automation_level>Fully automated</automation_level>
        <execution_time>< 30 seconds</execution_time>
      </level_1_basic>
      
      <level_2_standard>
        <description>Standard testing for medium complexity</description>
        <test_types>Unit tests, integration tests, code quality</test_types>
        <automation_level>Mostly automated with some manual review</automation_level>
        <execution_time>< 5 minutes</execution_time>
      </level_2_standard>
      
      <level_3_comprehensive>
        <description>Comprehensive testing for complex changes</description>
        <test_types>Full TDD cycle, performance testing, security validation</test_types>
        <automation_level>Automated with manual verification</automation_level>
        <execution_time>< 15 minutes</execution_time>
      </level_3_comprehensive>
      
      <level_4_extensive>
        <description>Extensive testing for critical changes</description>
        <test_types>All test types including compliance and audit</test_types>
        <automation_level>Mix of automated and manual processes</automation_level>
        <execution_time>No time limit</execution_time>
      </level_4_extensive>
    </testing_level_progression>
    
    <smart_tdd_integration>
      <tdd_applicability_assessment>
        <always_required>New feature development, bug fixes with new functionality</always_required>
        <conditionally_required>Refactoring with behavior changes, performance optimizations</conditionally_required>
        <optional>Documentation updates, configuration changes, minor fixes</optional>
        <not_applicable>Pure refactoring without behavior changes, formatting updates</not_applicable>
      </tdd_applicability_assessment>
      
      <tdd_cycle_adaptation>
        <full_cycle>Complete RED-GREEN-REFACTOR for complex development</full_cycle>
        <abbreviated_cycle>Fast RED-GREEN for simple changes</abbreviated_cycle>
        <validation_only>Test validation without full TDD cycle</validation_only>
        <post_hoc_testing>Testing after implementation for low-risk changes</post_hoc_testing>
      </tdd_cycle_adaptation>
    </smart_tdd_integration>
  </progressive_testing_integration>
  
  <performance_adaptive_validation>
    <performance_thresholds>
      <simple_task_thresholds>
        <response_time>p95 < 1s (if applicable)</response_time>
        <resource_usage>Basic resource monitoring</resource_usage>
        <scalability>Not required</scalability>
      </simple_task_thresholds>
      
      <medium_task_thresholds>
        <response_time>p95 < 500ms for affected workflows</response_time>
        <resource_usage>Moderate resource monitoring</resource_usage>
        <scalability>Basic scalability considerations</scalability>
      </medium_task_thresholds>
      
      <complex_task_thresholds>
        <response_time>p95 < 200ms for all workflows</response_time>
        <resource_usage>Comprehensive resource monitoring</resource_usage>
        <scalability>Scalability testing required</scalability>
      </complex_task_thresholds>
      
      <critical_task_thresholds>
        <response_time>p95 < 100ms for critical paths</response_time>
        <resource_usage>Detailed resource optimization</resource_usage>
        <scalability>Comprehensive scalability validation</scalability>
      </critical_task_thresholds>
    </performance_thresholds>
    
    <adaptive_benchmarking>
      <baseline_establishment>Establish performance baselines appropriate to task complexity</baseline_establishment>
      <regression_detection>Monitor for performance regressions at appropriate sensitivity levels</regression_detection>
      <optimization_recommendations>Provide optimization guidance based on complexity level</optimization_recommendations>
    </adaptive_benchmarking>
  </performance_adaptive_validation>
  
  <intelligent_error_recovery>
    <error_classification>
      <blocking_errors>Errors that prevent task completion</blocking_errors>
      <warning_errors>Errors that should be addressed but don't block completion</warning_errors>
      <informational_errors>Errors that provide useful information but don't require action</informational_errors>
    </error_classification>
    
    <recovery_strategies>
      <automatic_recovery>Automated fixes for common, low-risk errors</automatic_recovery>
      <guided_recovery>Step-by-step guidance for manual resolution</guided_recovery>
      <escalation_recovery>Escalation to higher quality levels for complex errors</escalation_recovery>
      <rollback_recovery>Automatic rollback for critical errors</rollback_recovery>
    </recovery_strategies>
    
    <adaptive_rollback>
      <simple_rollback>File-level rollback for simple changes</simple_rollback>
      <component_rollback>Component-level rollback for medium changes</component_rollback>
      <system_rollback>System-level rollback for complex changes</system_rollback>
      <comprehensive_rollback>Full system rollback with audit trail for critical changes</comprehensive_rollback>
    </adaptive_rollback>
  </intelligent_error_recovery>
  
  <quality_metrics_dashboard>
    <real_time_monitoring>
      <task_complexity_tracking>Real-time tracking of task complexity classifications</task_complexity_tracking>
      <quality_gate_performance>Monitor quality gate pass/fail rates by complexity level</quality_gate_performance>
      <efficiency_metrics>Track efficiency improvements from context-sensitive approach</efficiency_metrics>
      <time_savings>Measure time savings from reduced overhead on simple tasks</time_savings>
    </real_time_monitoring>
    
    <adaptive_reporting>
      <context_sensitive_reports>Generate reports appropriate to task complexity</context_sensitive_reports>
      <efficiency_analysis>Analyze efficiency gains from context-sensitive approach</efficiency_analysis>
      <quality_trend_analysis">Monitor quality trends across different complexity levels</quality_trend_analysis>
      <optimization_recommendations>Provide recommendations for further optimization</optimization_recommendations>
    </adaptive_reporting>
  </quality_metrics_dashboard>
  
  <success_metrics>
    <efficiency_targets>
      <simple_task_efficiency>60% reduction in quality overhead</simple_task_efficiency>
      <medium_task_efficiency>30% reduction in quality overhead</medium_task_efficiency>
      <complex_task_efficiency>Maintain current thoroughness</complex_task_efficiency>
      <critical_task_efficiency>Enhance thoroughness where needed</critical_task_efficiency>
    </efficiency_targets>
    
    <quality_maintenance>
      <defect_detection_rate>Maintain or improve defect detection rates</defect_detection_rate>
      <false_positive_reduction>Reduce false positive quality alerts</false_positive_reduction>
      <developer_satisfaction>Improve developer experience with context-appropriate quality</developer_satisfaction>
      <time_to_completion">Reduce average time to completion for appropriate complexity levels</time_to_completion>
    </quality_maintenance>
    
    <system_reliability>
      <uptime_target>95% uptime for quality assessment system</uptime_target>
      <accuracy_target>90% accuracy in complexity classification</accuracy_target>
      <response_time_target>< 5 seconds for complexity assessment</response_time_target>
      <user_satisfaction_target>85% user satisfaction with quality feedback</user_satisfaction_target>
    </system_reliability>
  </success_metrics>
  
  <integration_points>
    <depends_on>
      quality/universal-quality-gates.md for comprehensive quality gate definitions
      quality/tdd.md for TDD enforcement patterns
      patterns/tool-usage.md for parallel execution optimization
      quality/critical-thinking.md for intelligent analysis capabilities
    </depends_on>
    <provides_to>
      All commands for context-sensitive quality assessment
      quality/framework-metrics.md for quality measurement and optimization
      development/task-management.md for task complexity integration
      patterns/intelligent-routing.md for quality-aware routing decisions
    </provides_to>
  </integration_points>
  
  <claude_4_enhancements>
    <intelligent_classification>
      <thinking_integration>Leverage Claude 4 thinking patterns for complexity analysis</thinking_integration>
      <parallel_analysis>Parallel assessment of multiple complexity dimensions</parallel_analysis>
      <context_optimization>Efficient context usage for quality assessment</context_optimization>
      <adaptive_reasoning>Dynamic reasoning based on task characteristics</adaptive_reasoning>
    </intelligent_classification>
    
    <quality_optimization>
      <performance_improvement>Optimize quality assessment for parallel execution</performance_improvement>
      <context_efficiency>Efficient token usage for quality validation</context_efficiency>
      <intelligent_feedback">Provide intelligent, actionable quality feedback</intelligent_feedback>
      <continuous_learning>Learn from quality patterns to improve assessment</continuous_learning>
    </quality_optimization>
  </claude_4_enhancements>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

*Context-sensitive quality assessment system that balances thoroughness with efficiency, providing appropriate quality measures based on task complexity and requirements.*