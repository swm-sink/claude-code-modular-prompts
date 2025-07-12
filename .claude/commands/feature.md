| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 80%      |

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
    <module>patterns/thinking/critical-thinking-pattern.md</module>
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
    <module>patterns/error-recovery.md</module>
    <module>patterns/context-management-pattern.md</module>
    <module>patterns/validation-pattern.md</module>
    <module>patterns/documentation-pattern.md</module>
  </support_modules>
</module_orchestration>
```

## Error Handling

```xml
<error_handling>
  <rollback_procedures>
    <prd_validation_failure>Return to requirements gathering with stakeholder clarification</prd_validation_failure>
    <architecture_failure>Redesign components with improved interface contracts</architecture_failure>
    <tdd_failure>git reset --hard to last stable component and retry with improved tests</tdd_failure>
    <integration_failure>Isolate failing component, validate interfaces, fix integration issues</integration_failure>
    <quality_gate_failure>Address specific quality issues, re-validate all gates</quality_gate_failure>
  </rollback_procedures>
  
  <escalation_paths>
    <requirements_unclear>Route to /query for stakeholder research and clarification</requirements_unclear>
    <complex_coordination>Route to /swarm for multi-agent development coordination</complex_coordination>
    <production_deployment>Route to /protocol for strict production standards</production_deployment>
    <long_development>Route to /session for GitHub issue tracking and progress management</long_development>
  </escalation_paths>
  
  <failure_recovery>
    <component_failures>Isolate failed component, validate interface contracts, re-implement with TDD</component_failures>
    <integration_issues>Test component interfaces individually, fix integration points systematically</integration_issues>
    <performance_failures>Profile performance bottlenecks, optimize critical paths, re-validate benchmarks</performance_failures>
    <quality_standards>Address specific quality violations, improve test coverage, re-validate gates</quality_standards>
  </failure_recovery>
</error_handling>
```

## Examples

- `/feature "User profile management"` - Complete user profile feature
- `/feature "Payment processing integration"` - Payment feature development
- `/feature "Real-time notifications"` - Notification system feature