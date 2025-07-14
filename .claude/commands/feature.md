| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 95%      |

# Feature Command - PRD-Driven Development

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="feature" category="development" enforcement="BLOCKING">
  
  <purpose>
    Execute comprehensive feature development with PRD-driven planning, multi-component coordination, strict TDD enforcement, and production-ready quality gates with Claude 4 optimization.
  </purpose>
  
  <scope>
    <includes>Multi-component features, system integrations, user-facing functionality, API development</includes>
    <excludes>Single file changes, simple bug fixes, documentation-only changes, experimental prototypes</excludes>
    <boundaries>Features requiring >10 steps should use /session with GitHub issue tracking</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Feature description with user stories, acceptance criteria, and business requirements</required_arguments>
    <context_requirements>System architecture, existing APIs, user interface patterns, integration points</context_requirements>
    <preconditions>PRD or feature specification available, development environment ready, stakeholder alignment</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Complete feature implementation, comprehensive test suite, integration validation, documentation</deliverables>
    <success_criteria>All acceptance criteria met, tests pass, performance targets achieved, production ready</success_criteria>
    <artifacts>Feature code, test files, API documentation, integration tests, deployment guides</artifacts>
  </output_specification>
</command>
```

PRD-driven autonomous feature development with comprehensive planning and atomic commits.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="extended">
    <action>PRD Analysis and Requirements Validation: Comprehensive analysis of product requirements and acceptance criteria</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What are the complete business requirements and user stories?
        - How do acceptance criteria translate to technical specifications?
        - What system integrations and dependencies are required?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Primary Question: Are all requirements clearly defined and testable?]
        - [User Question: How does this feature provide value to end users?]
        - [Technical Question: What technical challenges and constraints exist?]
        - [Integration Question: How does this feature integrate with existing systems?]
        - [Quality Question: What quality standards ensure feature success?]
        - [Timeline Question: Are requirements achievable within scope and timeline?]
      </critical_thinking>
      <decision_reasoning>
        - Why is this feature approach optimal for user and business needs?
        - What evidence supports the technical feasibility assessment?
        - How will feature success be measured and validated?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch PRD analysis, requirements validation, and stakeholder documentation review</tool_optimization>
      <context_efficiency>Load system architecture, API documentation, and integration patterns concurrently</context_efficiency>
      <dependency_analysis>Identify requirements analysis that can be parallelized vs sequential</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>PRD_ANALYSIS: [requirements] with [acceptance_criteria] requiring [technical_approach] and [integrations]</output_format>
    <validation>Requirements clearly defined, acceptance criteria measurable, technical feasibility confirmed, stakeholder alignment verified</validation>
    <enforcement>BLOCK feature development until comprehensive PRD analysis validates approach</enforcement>
    <context_transfer>Validated requirements, acceptance criteria, technical approach, integration plan</context_transfer>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Feature Architecture and Component Planning: Break down feature into manageable components with clear interfaces</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What components are needed to deliver the complete feature?
        - How should components be structured for maintainability and testability?
        - What interfaces and contracts ensure proper component integration?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Architecture Question: Does component design support scalability and maintainability?]
        - [Interface Question: Are component contracts clear and well-defined?]
        - [Dependency Question: How do components interact and what are the dependencies?]
        - [Testing Question: How can each component be independently tested?]
        - [Risk Question: What architectural risks need mitigation strategies?]
      </critical_thinking>
      <decision_reasoning>
        - Why is this component architecture optimal for the feature requirements?
        - What evidence shows the design supports long-term maintainability?
        - How does the architecture facilitate comprehensive testing?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch architecture analysis, component planning, and interface design</tool_optimization>
      <context_efficiency>Analyze existing patterns and architectural decisions concurrently</context_efficiency>
      <dependency_analysis>Identify component planning steps that can be parallelized</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>ARCHITECTURE: [components] with [interfaces] supporting [requirements] via [integration_strategy]</output_format>
    <validation>Components clearly defined, interfaces specified, dependencies mapped, architecture validated against requirements</validation>
    <enforcement>BLOCK implementation until architecture validated and component plan approved</enforcement>
    <context_transfer>Component architecture, interface specifications, dependency map, implementation plan</context_transfer>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>TDD Implementation by Component: Implement each component with strict test-driven development</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should TDD be applied across multiple components systematically?
        - What testing strategy ensures comprehensive coverage and integration?
        - How can component implementation maintain interface contracts?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [TDD Question: Are tests written first for each component with comprehensive coverage?]
        - [Integration Question: How do component tests validate interface contracts?]
        - [Quality Question: Does implementation maintain code quality standards across components?]
        - [Performance Question: Are performance requirements addressed in implementation?]
        - [Risk Question: What implementation risks require mitigation during development?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this TDD approach ensure feature quality and reliability?
        - What evidence shows comprehensive testing across all components?
        - How does implementation maintain architectural integrity?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch component implementation, test execution, and validation across parallel development streams</tool_optimization>
      <context_efficiency>Optimize component testing and integration validation for efficiency</context_efficiency>
      <dependency_analysis>Identify components that can be developed in parallel vs those requiring sequential implementation</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>TDD_IMPLEMENTATION: [components_completed] with [test_coverage]% across [component_count] components</output_format>
    <validation>All components follow TDD, comprehensive test coverage achieved, interface contracts validated, quality standards met</validation>
    <enforcement>BLOCK progression until all components implemented with proper TDD and validated interfaces</enforcement>
    <context_transfer>Implemented components, comprehensive test suite, validated interfaces, quality metrics</context_transfer>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Integration Testing and System Validation: Ensure feature integrates properly with existing systems</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should feature integration be tested comprehensively?
        - What system-level validation ensures feature reliability?
        - How can integration testing identify potential system issues?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Integration Question: Does the feature integrate seamlessly with existing systems?]
        - [Performance Question: Does integrated feature meet performance requirements?]
        - [Security Question: Are there security implications requiring validation?]
        - [User Question: Does integrated feature provide expected user experience?]
        - [Reliability Question: Is the integrated system stable and reliable?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this integration approach ensure system stability?
        - What evidence demonstrates successful feature integration?
        - How does integration testing validate end-to-end functionality?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch integration testing, performance validation, and security assessment</tool_optimization>
      <context_efficiency>Optimize system-level testing and validation reporting</context_efficiency>
      <dependency_analysis>Identify integration tests that can be executed concurrently vs sequentially</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>INTEGRATION: [feature_integrated] with [system_validation] confirming [performance_metrics] and [reliability_standards]</output_format>
    <validation>Feature integrated successfully, performance targets met, security validated, user experience confirmed</validation>
    <enforcement>BLOCK feature completion until comprehensive integration validation passes</enforcement>
    <context_transfer>Integration validation results, performance metrics, system stability confirmation</context_transfer>
  </checkpoint>
  
  <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Production Quality Validation: Comprehensive quality gates and production readiness assessment</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What quality gates ensure production readiness?
        - How can comprehensive validation confirm feature reliability?
        - What documentation and deployment preparation is required?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Quality Question: Do all quality gates pass with measurable evidence?]
        - [Production Question: Is the feature ready for production deployment?]
        - [Documentation Question: Is comprehensive documentation available for users and developers?]
        - [Monitoring Question: Are monitoring and alerting configured for feature health?]
        - [Rollback Question: Are rollback procedures defined and tested?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this feature meet production quality standards?
        - What evidence demonstrates comprehensive quality validation?
        - How do quality metrics support production deployment readiness?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch quality gate validation, documentation review, and production readiness assessment</tool_optimization>
      <context_efficiency>Optimize comprehensive quality validation and reporting</context_efficiency>
      <dependency_analysis>Identify quality validation steps that can be executed concurrently</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>PRODUCTION_READY: [quality_gates_passed] with [documentation_complete] confirming [deployment_readiness]</output_format>
    <validation>All quality gates pass, documentation complete, monitoring configured, rollback procedures defined, production ready</validation>
    <enforcement>BLOCK feature completion until comprehensive production quality validation passes</enforcement>
    <context_transfer>Production readiness confirmation, quality validation results, deployment documentation</context_transfer>
  </checkpoint>
  
</thinking_pattern>
```

## Instructions

Execute feature development workflow for: $ARGUMENTS

1. **PRD Analysis**: Understand product requirements and acceptance criteria.
   - **Atomic Checkpoint**: `git add -A && git commit -m "FEATURE PLAN: [feature_name] - requirements analyzed and PRD validated"`
   - **Validation**: Ensure acceptance criteria are clearly defined before proceeding

2. **Feature Planning**: Break down feature into components and dependencies.
   - **Atomic Checkpoint**: `git add -A && git commit -m "FEATURE DESIGN: [feature_name] - components planned and dependencies mapped"`
   - **Architecture Safety**: Validate design against existing system architecture

3. **TDD Implementation**: Implement feature with test-driven development.
   - **Per-Component Atomic Checkpoints**: `git add -A && git commit -m "FEATURE IMPL: [component] - functionality added with tests"`
   - **TDD Compliance**: Each component follows RED→GREEN→REFACTOR with atomic commits
   - **Rollback Safety**: Failed components can be rolled back without affecting completed ones

4. **Integration Testing**: Ensure feature integrates properly with existing system.
   - **Atomic Checkpoint**: `git add -A && git commit -m "FEATURE INTEGRATION: [feature_name] - system integrated and tested"`
   - **Integration Validation**: Run full integration test suite before commit

5. **Quality Validation**: Comprehensive testing and production readiness.
   - **Final Atomic Checkpoint**: `git add -A && git commit -m "FEATURE VALIDATED: [feature_name] - production ready with quality gates passed"`

## Feature Development Process

- Product requirements analysis
- Technical specification creation
- Component identification and planning
- Test-driven implementation
- Integration and validation
- Production readiness assessment

## Module Integration

```xml
<module_orchestration>
  <core_modules>
    <module>patterns/critical-thinking-pattern.md</module>
    <module>quality/tdd.md</module>
    <module>development/feature-workflow.md</module>
    <module>quality/universal-quality-gates.md</module>
    <module>development/prd-generation.md</module>
  </core_modules>
  
  <contextual_modules>
    <module condition="user_interface">patterns/user-interaction-pattern.md</module>
    <module condition="api_development">patterns/integration-pattern.md</module>
    <module condition="performance_critical">patterns/performance-optimization.md</module>
    <module condition="security_sensitive">security/threat-modeling.md</module>
  </contextual_modules>
  
  <support_modules>
    <module>patterns/comprehensive-error-handling.md</module>
    <module>patterns/error-recovery.md</module>
    <module>patterns/context-management-pattern.md</module>
    <module>patterns/validation-pattern.md</module>
    <module>patterns/documentation-pattern.md</module>
  </support_modules>
</module_orchestration>
```

## Comprehensive Error Handling

```xml
<error_handling framework="comprehensive" enforcement="PRODUCTION_GRADE">
  
  <error_classification_integration>
    <module>patterns/comprehensive-error-handling.md</module>
    <classification_system>BLOCKING | CONDITIONAL | OPTIONAL | ESCALATION</classification_system>
    <feature_specific_classification>Multi-component error impact assessment with dependency analysis</feature_specific_classification>
  </error_classification_integration>
  
  <graceful_degradation_patterns enforcement="MANDATORY">
    <prd_analysis_failures>
      <trigger>PRD incomplete, requirements unclear, acceptance criteria ambiguous</trigger>
      <degradation>Proceed with available requirements, document assumptions and gaps</degradation>
      <fallback>Use standard feature patterns, implement core functionality</fallback>
      <escalation>Route to /query for stakeholder research when critical requirements missing</escalation>
    </prd_analysis_failures>
    
    <architecture_planning_failures>
      <trigger>Component design flawed, interface contracts unclear, dependency conflicts</trigger>
      <degradation>Simplify architecture, reduce component coupling, use proven patterns</degradation>
      <fallback>Implement monolithic approach, plan future modularization</fallback>
      <rollback>git reset --hard HEAD~1 to PRD phase, redesign with simpler approach</rollback>
      <escalation>CONDITIONAL - Complex features may require architecture iteration</escalation>
    </architecture_planning_failures>
    
    <component_implementation_failures>
      <trigger>Individual component TDD failures, integration contract violations</trigger>
      <degradation>Isolate failing component, continue with successful components</degradation>
      <fallback>Implement simplified version of failing component</fallback>
      <rollback>git reset --hard to last successful component checkpoint</rollback>
      <escalation>CONDITIONAL - Feature may proceed with reduced component set</escalation>
    </component_implementation_failures>
    
    <integration_testing_failures>
      <trigger>Component integration fails, system conflicts, performance degradation</trigger>
      <degradation>Implement components in isolation, defer integration</degradation>
      <fallback>Create integration adapters, implement compatibility layers</fallback>
      <rollback>git reset --hard to last successful integration checkpoint</rollback>
      <escalation>BLOCKING for critical integrations, CONDITIONAL for optional features</escalation>
    </integration_testing_failures>
    
    <quality_validation_failures>
      <trigger>Feature quality standards not met, performance issues, security concerns</trigger>
      <degradation>Document quality issues, implement mitigation strategies</degradation>
      <fallback>Meet minimum viable quality for core functionality</fallback>
      <rollback>git reset --hard to last quality-compliant checkpoint</rollback>
      <escalation>BLOCKING for security, CONDITIONAL for performance, OPTIONAL for usability</escalation>
    </quality_validation_failures>
  </graceful_degradation_patterns>
  
  <atomic_rollback_mechanisms enforcement="CRITICAL">
    <component_rollback>
      <trigger>Individual component failures without affecting other components</trigger>
      <procedure>git reset --hard HEAD~1 for failing component, preserve successful components</procedure>
      <isolation>Maintain component boundaries to prevent cascade failures</isolation>
      <recovery>Retry component with alternative implementation approach</recovery>
    </component_rollback>
    
    <integration_rollback>
      <trigger>Integration failures affecting multiple components</trigger>
      <procedure>git reset --hard to last successful integration checkpoint</procedure>
      <preservation>Maintain individual component implementations</preservation>
      <strategy>Retry integration with revised interface contracts</strategy>
    </integration_rollback>
    
    <feature_rollback>
      <trigger>Critical failures affecting entire feature viability</trigger>
      <procedure>git reset --hard HEAD~5 to feature planning phase</procedure>
      <analysis>Comprehensive failure analysis and approach reevaluation</analysis>
      <escalation>Human intervention for fundamental feature redesign</escalation>
    </feature_rollback>
    
    <emergency_rollback>
      <trigger>Security violations, data corruption risks, system instability</trigger>
      <procedure>git reset --hard to last known stable state, immediate safety measures</procedure>
      <notification>Immediate alerts to security and development teams</notification>
      <documentation>Comprehensive incident report with timeline and impact assessment</documentation>
    </emergency_rollback>
  </atomic_rollback_mechanisms>
  
  <recovery_procedures enforcement="INTELLIGENT">
    <automatic_retry>
      <component_retry>
        <examples>Test execution failures, build errors, dependency issues</examples>
        <strategy>Exponential backoff with component isolation, maximum 3 attempts per component</strategy>
        <learning>Track component-specific failure patterns and optimize retry strategies</learning>
      </component_retry>
      
      <integration_retry>
        <examples>Network timeouts, service unavailability, resource contention</examples>
        <strategy>Progressive retry with increasing delay, alternative integration paths</strategy>
        <adaptation>Adapt integration approach based on failure type and frequency</adaptation>
      </integration_retry>
      
      <quality_validation_retry>
        <examples>Flaky tests, environment issues, temporary performance degradation</examples>
        <strategy>Immediate retry with environment validation, alternative validation methods</strategy>
        <improvement>Identify and eliminate sources of validation instability</improvement>
      </quality_validation_retry>
    </automatic_retry>
    
    <intelligent_escalation>
      <pattern_recognition>
        <recurring_component_failures>Escalate to alternative implementation after 2 failures</recurring_component_failures>
        <integration_patterns>Escalate when integration failures affect >50% of components</integration_patterns>
        <quality_degradation>Escalate when quality metrics decline consistently</quality_degradation>
        <timeline_impact>Escalate when recovery attempts exceed 20% of planned development time</timeline_impact>
      </pattern_recognition>
      
      <escalation_levels>
        <level_1>Parameter adjustment and alternative component implementation</level_1>
        <level_2>Architecture simplification and component consolidation</level_2>
        <level_3>Feature scope reduction with core functionality preservation</level_3>
        <level_4>Human intervention with comprehensive context and redesign options</level_4>
      </escalation_levels>
    </intelligent_escalation>
    
    <adaptive_learning>
      <success_tracking>
        <metric>Component recovery success rate by implementation approach</metric>
        <metric>Integration recovery effectiveness by architecture pattern</metric>
        <metric>Quality recovery time by validation method</metric>
        <metric>Feature completion rate despite error occurrences</metric>
      </success_tracking>
      
      <strategy_optimization>
        <principle>Learn from successful component implementation patterns</principle>
        <principle>Adapt integration strategies based on failure analysis</principle>
        <principle>Optimize quality validation based on error prevention</principle>
        <principle>Improve feature planning through historical error analysis</principle>
      </strategy_optimization>
    </adaptive_learning>
  </recovery_procedures>
  
  <monitoring_and_alerting enforcement="COMPREHENSIVE">
    <error_tracking>
      <metrics>
        <component_failure_rate>Track failure rates by component type and complexity</component_failure_rate>
        <integration_success_rate>Monitor integration success across different architectures</integration_success_rate>
        <quality_compliance_rate>Measure quality standard compliance by feature type</quality_compliance_rate>
        <feature_completion_rate>Track feature completion despite error scenarios</feature_completion_rate>
      </metrics>
      
      <alerting>
        <critical_errors>Immediate notification for BLOCKING errors affecting feature viability</critical_errors>
        <pattern_alerts>Notification when error patterns suggest architectural issues</pattern_alerts>
        <quality_alerts>Alert when quality degradation affects user experience</quality_alerts>
        <timeline_alerts>Warning when error recovery impacts delivery timelines</timeline_alerts>
      </alerting>
    </error_tracking>
    
    <performance_monitoring>
      <development_velocity>Measure feature development speed with error handling overhead</development_velocity>
      <recovery_efficiency>Track time to successful recovery for different error types</recovery_efficiency>
      <quality_preservation>Monitor quality standard maintenance during error scenarios</quality_preservation>
      <resource_utilization>Track development resource usage during error handling</resource_utilization>
    </performance_monitoring>
    
    <effectiveness_measurement>
      <success_metrics>
        <automated_recovery_rate>Percentage of feature errors resolved without human intervention</automated_recovery_rate>
        <feature_completion_rate>Successful feature delivery rate despite error occurrences</feature_completion_rate>
        <quality_maintenance_rate>Quality standard compliance during error scenarios</quality_maintenance_rate>
        <stakeholder_satisfaction>Feature delivery satisfaction despite development challenges</stakeholder_satisfaction>
      </success_metrics>
      
      <continuous_improvement>
        <feedback_integration>Learn from stakeholder feedback on feature delivery experience</feedback_integration>
        <pattern_analysis>Identify and prevent recurring architectural and implementation issues</pattern_analysis>
        <process_optimization>Continuously improve feature development and error handling procedures</process_optimization>
        <knowledge_capture>Capture and share successful error recovery strategies across teams</knowledge_capture>
      </continuous_improvement>
    </effectiveness_measurement>
  </monitoring_and_alerting>
  
  <escalation_paths enhancement="INTELLIGENT_ROUTING">
    <requirements_ambiguity severity="ESCALATION">
      <trigger>PRD unclear, stakeholder alignment missing, acceptance criteria conflicts</trigger>
      <route>/query for comprehensive stakeholder research and requirement clarification</route>
      <context>Provide detailed analysis of requirement gaps, stakeholder concerns, clarification needs</context>
      <fallback>Proceed with best interpretation, document assumptions and validation checkpoints</fallback>
    </requirements_ambiguity>
    
    <complex_coordination severity="ESCALATION">
      <trigger>Multi-team dependencies, cross-system integrations, complex workflows</trigger>
      <route>/swarm for multi-agent coordination and dependency management</route>
      <context>Provide coordination analysis, dependency mapping, team communication requirements</context>
      <fallback>Implement isolated components, define integration interfaces for future coordination</fallback>
    </complex_coordination>
    
    <production_deployment severity="BLOCKING">
      <trigger>Production environment requirements, security implications, compliance needs</trigger>
      <route>/protocol for strict production standards and comprehensive validation</route>
      <context>Provide production readiness assessment, security analysis, compliance requirements</context>
      <fallback>NONE - Production features require full protocol compliance and validation</fallback>
    </production_deployment>
    
    <extended_development severity="CONDITIONAL">
      <trigger>Feature development >10 components, timeline >2 weeks, complex dependencies</trigger>
      <route>/session for GitHub issue tracking and progress management</route>
      <context>Provide development breakdown, progress tracking needs, milestone planning</context>
      <fallback>Break feature into smaller deliverable components, implement incrementally</fallback>
    </extended_development>
    
    <architectural_complexity severity="ESCALATION">
      <trigger>Complex system design, performance constraints, scalability requirements</trigger>
      <route>Human intervention for architectural review and design validation</route>
      <context>Provide architectural analysis, performance requirements, scalability concerns</context>
      <fallback>Implement simplified architecture, plan future enhancement iterations</fallback>
    </architectural_complexity>
  </escalation_paths>
  
</error_handling>
```

## Examples

- `/feature "User profile management"` - Complete user profile feature
- `/feature "Payment processing integration"` - Payment feature development
- `/feature "Real-time notifications"` - Notification system feature