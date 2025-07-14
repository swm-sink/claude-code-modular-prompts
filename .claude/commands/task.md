| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 95%      |

# Task Command - Research-First TDD Development

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="task" category="development" enforcement="BLOCKING">
  
  <purpose>
    Execute focused development tasks with mandatory research-first methodology, strict TDD cycle enforcement, and atomic commit safety for single-component modifications with Claude 4 optimization.
  </purpose>
  
  <scope>
    <includes>Single file modifications, focused feature additions, bug fixes, performance improvements</includes>
    <excludes>Multi-component features, system-wide changes, complex integrations, documentation generation</excludes>
    <boundaries>Tasks affecting >3 files or requiring coordination should use /swarm or /feature</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Task description with clear requirements and acceptance criteria</required_arguments>
    <context_requirements>Existing codebase, related files, test framework availability</context_requirements>
    <preconditions>Development environment ready, git repository available, testing tools configured</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Working code with comprehensive tests, atomic git commits, quality validation report</deliverables>
    <success_criteria>Tests pass, coverage ≥90%, TDD cycle completed, production standards met</success_criteria>
    <artifacts>Test files, implementation code, commit history, coverage reports</artifacts>
  </output_specification>
</command>
```

Research-first focused development with mandatory TDD cycle and atomic commits.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Research-First Analysis: Analyze requirements, existing code patterns, and architecture before implementation</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What exactly needs to be accomplished in this task?
        - What existing code patterns and architecture inform the approach?
        - How does this task fit within the broader system context?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Primary Question: What specific functionality needs to be implemented?]
        - [Context Question: How does this integrate with existing systems?]
        - [Risk Question: What could go wrong or cause regressions?]
        - [Quality Question: What testing strategy ensures reliable implementation?]
        - [Consequence Question: What are the impacts if this implementation fails?]
      </critical_thinking>
      <decision_reasoning>
        - Why is the chosen implementation approach optimal?
        - What evidence supports this technical decision?
        - How will success be measured and validated?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch file reads for code analysis and pattern identification</tool_optimization>
      <context_efficiency>Load related files and documentation concurrently</context_efficiency>
      <dependency_analysis>Identify sequential vs parallel analysis opportunities</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>RESEARCH: [findings] affecting [components] requiring [approach] with [test_strategy]</output_format>
    <validation>Requirements clearly understood, patterns identified, approach validated, acceptance criteria defined</validation>
    <enforcement>BLOCK implementation until comprehensive research validates approach</enforcement>
    <context_transfer>Research findings, implementation approach, test strategy, acceptance criteria</context_transfer>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>TDD RED Phase: Write failing tests that define expected behavior before any implementation</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What specific behaviors need to be tested?
        - How can tests comprehensively cover requirements and edge cases?
        - What test structure ensures maintainable and reliable validation?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Primary Question: Do tests cover all acceptance criteria and edge cases?]
        - [Risk Question: What scenarios could cause tests to be insufficient?]
        - [Alternative Question: Are there better testing approaches or frameworks?]
        - [Quality Question: Will these tests ensure long-term code reliability?]
        - [Consequence Question: What happens if tests miss critical behaviors?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this test approach ensure comprehensive coverage?
        - What evidence shows tests properly validate requirements?
        - How will test failures guide implementation decisions?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Can test file creation and validation be batched?</tool_optimization>
      <context_efficiency>Optimize test execution and failure verification</context_efficiency>
      <dependency_analysis>Identify test dependencies and execution order</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>TDD_RED: [test_count] tests covering [requirements] - ALL FAILING as expected</output_format>
    <validation>Tests written first, comprehensive coverage planned, all tests fail correctly, no implementation exists</validation>
    <enforcement>BLOCK implementation until proper failing tests exist with rollback safety</enforcement>
    <context_transfer>Failing tests, coverage strategy, implementation requirements</context_transfer>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="standard">
    <action>TDD GREEN Phase: Implement minimal code to make tests pass with ≥90% coverage validation</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What is the minimal implementation needed to make tests pass?
        - How can implementation be kept simple while meeting requirements?
        - What coverage validation ensures quality standards?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Primary Question: Does implementation make all tests pass minimally?]
        - [Risk Question: Is implementation over-engineered or insufficient?]
        - [Quality Question: Does coverage meet 90% threshold with meaningful assertions?]
        - [Performance Question: Are there obvious performance issues to address?]
        - [Consequence Question: What breaks if this implementation fails?]
      </critical_thinking>
      <decision_reasoning>
        - Why is this implementation approach optimal for the requirements?
        - What evidence shows code meets quality and coverage standards?
        - How does implementation maintain system consistency?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch implementation and test execution for rapid feedback</tool_optimization>
      <context_efficiency>Optimize coverage reporting and validation</context_efficiency>
      <dependency_analysis>Identify implementation steps that can be parallelized</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>TDD_GREEN: [implementation] with [coverage]% passing [test_count] tests</output_format>
    <validation>All tests pass, coverage ≥90% with assertions, implementation minimal and focused</validation>
    <enforcement>BLOCK progression until coverage validated and tests green with rollback safety</enforcement>
    <context_transfer>Working implementation, test results, coverage metrics</context_transfer>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="CONDITIONAL" thinking_mode="standard">
    <action>TDD REFACTOR Phase: Improve code quality while maintaining test coverage and green status</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What refactoring opportunities improve code quality?
        - How can refactoring maintain or improve test coverage?
        - What quality improvements provide the most value?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Primary Question: What refactoring provides maximum quality improvement?]
        - [Risk Question: Could refactoring break existing functionality?]
        - [Quality Question: Do refactored patterns improve maintainability?]
        - [Performance Question: Does refactoring improve or degrade performance?]
        - [Consequence Question: What are the long-term benefits of this refactoring?]
      </critical_thinking>
      <decision_reasoning>
        - Why are these refactoring changes beneficial?
        - What evidence shows improved code quality without regressions?
        - How does refactoring align with established patterns?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch refactoring validation and test execution</tool_optimization>
      <context_efficiency>Optimize quality assessment and pattern validation</context_efficiency>
      <dependency_analysis>Identify refactoring steps that preserve independence</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>TDD_REFACTOR: [improvements] maintaining [coverage]% with [test_status]</output_format>
    <validation>Tests remain green, coverage maintained/improved, code quality enhanced, patterns consistent</validation>
    <enforcement>CONDITIONAL - proceed if quality improved, rollback if tests broken</enforcement>
    <context_transfer>Refactored code, maintained test coverage, quality improvements</context_transfer>
  </checkpoint>
  
  <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Quality Gates Validation: Ensure production standards, security, and comprehensive testing</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What quality gates must be validated for production readiness?
        - How can security and performance implications be assessed?
        - What comprehensive validation ensures system reliability?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Primary Question: Do all quality gates pass with measurable evidence?]
        - [Security Question: Are there security implications requiring threat assessment?]
        - [Performance Question: Does implementation meet performance requirements?]
        - [Integration Question: How does this integrate with existing systems?]
        - [Production Question: Is this implementation ready for production deployment?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this implementation meet production standards?
        - What evidence demonstrates comprehensive quality validation?
        - How do quality metrics support deployment readiness?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch quality gate validation and security assessment</tool_optimization>
      <context_efficiency>Optimize comprehensive testing and validation reporting</context_efficiency>
      <dependency_analysis>Identify validation steps that can be executed concurrently</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>QUALITY_GATES: [gates_passed] with [evidence] confirming [production_readiness]</output_format>
    <validation>All quality gates pass, security assessed, performance validated, integration confirmed</validation>
    <enforcement>BLOCK completion until comprehensive quality validation passes</enforcement>
    <context_transfer>Quality validation results, production readiness confirmation</context_transfer>
  </checkpoint>
  
</thinking_pattern>
```

## Instructions

Execute the following workflow for the task: $ARGUMENTS

1. **Research First**: Analyze the requirements, existing code, and patterns before any implementation.
   - **Atomic Checkpoint**: `git add -A && git commit -m "TASK RESEARCH: [task_name] - requirements analyzed and patterns identified"`

2. **TDD Red Phase**: Write failing tests that define the expected behavior. Tests must fail initially.
   - **Atomic Checkpoint**: `git add -A && git commit -m "TDD RED: [test_description] - failing tests created for [task_name]"`
   - **Rollback Safety**: If tests don't fail correctly, rollback with `git reset --hard HEAD~1`

3. **TDD Green Phase**: Implement the minimal code to make tests pass. Measure test coverage and ensure ≥90% threshold.
   - **Atomic Checkpoint**: `git add -A && git commit -m "TDD GREEN: [implementation] - tests passing for [task_name]"`
   - **Coverage Validation**: Run coverage tools and validate ≥90% before commit
   - **Rollback Safety**: If coverage fails, rollback with `git reset --hard HEAD~1`

4. **TDD Refactor Phase**: Improve code quality while keeping tests green.
   - **Atomic Checkpoint**: `git add -A && git commit -m "TDD REFACTOR: [refactoring] - quality improved for [task_name]"`
   - **Safety Check**: Ensure tests still pass after refactoring

5. **Quality Gates**: Validate against production standards and ensure comprehensive coverage.
   - **Final Atomic Checkpoint**: `git add -A && git commit -m "TASK COMPLETE: [task_name] - production ready with quality validation"`

## Critical Rules

- ALWAYS write failing tests BEFORE implementation
- NEVER write code without test coverage
- Research existing patterns and architecture first
- Maintain 90%+ test coverage with atomic commit validation
- Use appropriate testing framework (pytest for Python, Jest for JavaScript, etc.)
- **ATOMIC SAFETY**: Every TDD phase gets atomic commit with rollback capability
- **INSTANT ROLLBACK**: Use `git reset --hard HEAD~1` for immediate rollback to previous phase

## Coverage Commands

- Python: `pytest --cov=. --cov-report=term-missing --cov-fail-under=90`
- JavaScript: `npm test -- --coverage --coverageThreshold='{"global":{"lines":90}}'`

## Module Integration

```xml
<module_orchestration>
  <core_modules>
    <module>patterns/critical-thinking-pattern.md</module>
    <module>quality/tdd.md</module>
    <module>development/task-management.md</module>
    <module>quality/universal-quality-gates.md</module>
  </core_modules>
  
  <contextual_modules>
    <module condition="security_implications">security/threat-modeling.md</module>
    <module condition="performance_requirements">patterns/performance-optimization.md</module>
    <module condition="integration_complexity">patterns/integration-pattern.md</module>
  </contextual_modules>
  
  <support_modules>
    <module>patterns/comprehensive-error-handling.md</module>
    <module>patterns/error-recovery.md</module>
    <module>patterns/context-management-pattern.md</module>
    <module>patterns/validation-pattern.md</module>
  </support_modules>
</module_orchestration>
```

## Comprehensive Error Handling

```xml
<error_handling framework="comprehensive" enforcement="PRODUCTION_GRADE">
  
  <error_classification_integration>
    <module>patterns/comprehensive-error-handling.md</module>
    <classification_system>BLOCKING | CONDITIONAL | OPTIONAL | ESCALATION</classification_system>
    <real_time_classification>Error severity determined dynamically based on context and impact</real_time_classification>
  </error_classification_integration>
  
  <graceful_degradation_patterns enforcement="MANDATORY">
    <research_phase_failures>
      <trigger>Research analysis incomplete or inconclusive</trigger>
      <degradation>Continue with available information, flag gaps for manual review</degradation>
      <fallback>Use existing patterns and best practices, document assumptions</fallback>
      <escalation>Route to /query for comprehensive research when critical gaps identified</escalation>
    </research_phase_failures>
    
    <tdd_red_phase_failures>
      <trigger>Tests don't fail as expected or test creation blocked</trigger>
      <degradation>Create manual test scenarios, document expected behaviors</degradation>
      <fallback>Proceed with implementation using behavioral specifications</fallback>
      <rollback>git reset --hard HEAD~1 to research phase, retry with alternative test approach</rollback>
      <escalation>BLOCKING - Cannot proceed without proper failing tests</escalation>
    </tdd_red_phase_failures>
    
    <tdd_green_phase_failures>
      <trigger>Implementation fails to make tests pass or coverage insufficient</trigger>
      <degradation>Implement minimal viable solution, document coverage gaps</degradation>
      <fallback>Focus on core functionality, defer edge cases</fallback>
      <rollback>git reset --hard HEAD~1 to RED phase, improve tests or approach</rollback>
      <escalation>CONDITIONAL - May proceed with reduced scope if core functionality works</escalation>
    </tdd_green_phase_failures>
    
    <refactor_phase_failures>
      <trigger>Refactoring breaks tests or introduces regressions</trigger>
      <degradation>Skip refactoring, proceed with working implementation</degradation>
      <fallback>Apply minimal code quality improvements only</fallback>
      <rollback>git reset --hard HEAD~1 to GREEN phase, maintain working state</rollback>
      <escalation>OPTIONAL - Refactoring can be deferred to future iterations</escalation>
    </refactor_phase_failures>
    
    <quality_gate_failures>
      <trigger>Quality standards not met, security issues, or performance problems</trigger>
      <degradation>Document quality issues, implement mitigation strategies</degradation>
      <fallback>Meet minimum viable quality thresholds, plan improvement iterations</fallback>
      <rollback>git reset --hard HEAD~1 to previous phase, address quality issues</rollback>
      <escalation>BLOCKING for security, CONDITIONAL for performance, OPTIONAL for style</escalation>
    </quality_gate_failures>
  </graceful_degradation_patterns>
  
  <atomic_rollback_mechanisms enforcement="CRITICAL">
    <immediate_rollback>
      <trigger>BLOCKING errors, security violations, system instability</trigger>
      <procedure>git reset --hard HEAD~1 && git clean -fd</procedure>
      <validation>Verify system state after rollback, confirm stability</validation>
      <documentation>Log rollback reason, impact assessment, recovery plan</documentation>
    </immediate_rollback>
    
    <progressive_rollback>
      <trigger>CONDITIONAL errors affecting multiple phases</trigger>
      <procedure>Step-by-step rollback through checkpoints until stable state</procedure>
      <preservation>Maintain successfully completed work where possible</preservation>
      <guidance>Provide specific recovery steps for each failed phase</guidance>
    </progressive_rollback>
    
    <emergency_rollback>
      <trigger>Data corruption risk, compliance violations, critical system errors</trigger>
      <procedure>git reset --hard HEAD~5 && git reflog to find last known good state</procedure>
      <escalation>Immediate human intervention required</escalation>
      <documentation>Comprehensive incident report with timeline and impact assessment</documentation>
    </emergency_rollback>
  </atomic_rollback_mechanisms>
  
  <recovery_procedures enforcement="INTELLIGENT">
    <automatic_retry>
      <transient_failures>
        <examples>Network timeouts, temporary resource unavailability, process locks</examples>
        <strategy>Exponential backoff: 1s, 2s, 4s delays, maximum 3 attempts</strategy>
        <learning>Track success patterns, optimize retry timing</learning>
      </transient_failures>
      
      <resource_contention>
        <examples>File locks, database connections, memory pressure</examples>
        <strategy>Linear backoff with resource monitoring, maximum 5 attempts</strategy>
        <adaptation>Adjust strategy based on resource availability patterns</adaptation>
      </resource_contention>
      
      <test_execution_failures>
        <examples>Flaky tests, environment issues, dependency problems</examples>
        <strategy>Immediate retry once, then longer delay retry, maximum 2 attempts</strategy>
        <improvement>Identify and fix flaky test patterns</improvement>
      </test_execution_failures>
    </automatic_retry>
    
    <intelligent_escalation>
      <pattern_recognition>
        <recurring_errors>Escalate to alternative approach after 2 occurrences</recurring_errors>
        <error_clusters>Escalate when multiple related errors detected</error_clusters>
        <time_based>Escalate when recovery attempts exceed 5 minutes</time_based>
      </pattern_recognition>
      
      <escalation_levels>
        <level_1>Parameter adjustment and immediate retry</level_1>
        <level_2>Alternative approach selection (different test framework, implementation pattern)</level_2>
        <level_3>Scope reduction with quality maintenance</level_3>
        <level_4>Human intervention with complete context and options</level_4>
      </escalation_levels>
    </intelligent_escalation>
    
    <adaptive_learning>
      <success_tracking>
        <metric>Recovery success rate by error type and strategy</metric>
        <metric>Time to recovery optimization</metric>
        <metric>Quality impact of different recovery approaches</metric>
      </success_tracking>
      
      <strategy_optimization>
        <principle>Learn from successful manual interventions</principle>
        <principle>Adapt retry timing based on historical effectiveness</principle>
        <principle>Optimize recovery paths through pattern analysis</principle>
      </strategy_optimization>
    </adaptive_learning>
  </recovery_procedures>
  
  <monitoring_and_alerting enforcement="COMPREHENSIVE">
    <error_tracking>
      <metrics>
        <error_frequency>Track error rates by phase and type</error_frequency>
        <recovery_success>Measure recovery effectiveness by strategy</recovery_success>
        <quality_impact>Assess quality degradation during error scenarios</quality_impact>
        <user_experience>Monitor task completion rates and satisfaction</user_experience>
      </metrics>
      
      <alerting>
        <critical_errors>Immediate notification for BLOCKING errors</critical_errors>
        <pattern_alerts>Notification when error patterns suggest systemic issues</pattern_alerts>
        <recovery_failures>Alert when recovery mechanisms repeatedly fail</recovery_failures>
        <threshold_alerts>Warning when error rates exceed baseline by 50%</threshold_alerts>
      </alerting>
    </error_tracking>
    
    <performance_monitoring>
      <execution_overhead>Measure error handling impact on task completion time</execution_overhead>
      <recovery_efficiency>Track time to successful recovery for different error types</recovery_efficiency>
      <resource_utilization>Monitor system resource usage during error scenarios</resource_utilization>
      <quality_preservation>Ensure error handling doesn't compromise output quality</quality_preservation>
    </performance_monitoring>
    
    <effectiveness_measurement>
      <success_metrics>
        <automated_recovery_rate>Percentage of errors resolved without human intervention</automated_recovery_rate>
        <recovery_time>Average and P95 time to complete recovery</recovery_time>
        <quality_maintenance>Quality standard compliance during error scenarios</quality_maintenance>
        <user_satisfaction>Task completion satisfaction despite error occurrences</user_satisfaction>
      </success_metrics>
      
      <continuous_improvement>
        <feedback_integration>Learn from user feedback on error handling experience</feedback_integration>
        <pattern_analysis>Identify and eliminate recurring error sources</pattern_analysis>
        <process_optimization>Continuously improve error handling procedures</process_optimization>
      </continuous_improvement>
    </effectiveness_measurement>
  </monitoring_and_alerting>
  
  <escalation_paths enhancement="INTELLIGENT_ROUTING">
    <requirements_unclear severity="ESCALATION">
      <trigger>Ambiguous requirements, conflicting specifications, incomplete acceptance criteria</trigger>
      <route>/query for comprehensive research and stakeholder clarification</route>
      <context>Provide detailed analysis of ambiguities and proposed clarification questions</context>
      <fallback>Proceed with best interpretation, document assumptions and risks</fallback>
    </requirements_unclear>
    
    <multi_component_scope severity="ESCALATION">
      <trigger>Task affects >3 files, requires coordination across systems, complex dependencies</trigger>
      <route>/swarm for multi-agent coordination and dependency management</route>
      <context>Provide component analysis, dependency map, coordination requirements</context>
      <fallback>Implement core component only, document integration requirements</fallback>
    </multi_component_scope>
    
    <complex_integration severity="CONDITIONAL">
      <trigger>Integration requirements unclear, external system dependencies, API changes needed</trigger>
      <route>/feature for comprehensive planning and PRD development</route>
      <context>Provide integration analysis, risk assessment, planning recommendations</context>
      <fallback>Implement isolated functionality, define integration interfaces</fallback>
    </complex_integration>
    
    <production_deployment severity="BLOCKING">
      <trigger>Production environment requirements, security implications, compliance needs</trigger>
      <route>/protocol for strict production standards and comprehensive validation</route>
      <context>Provide security assessment, compliance analysis, production readiness evaluation</context>
      <fallback>NONE - Production deployment requires full protocol compliance</fallback>
    </production_deployment>
    
    <resource_limitations severity="ESCALATION">
      <trigger>Insufficient development environment, missing tools, access restrictions</trigger>
      <route>Human intervention for resource provisioning and environment setup</route>
      <context>Provide detailed resource requirements, alternative approaches, timeline impact</context>
      <fallback>Implement using available resources, document limitations and risks</fallback>
    </resource_limitations>
  </escalation_paths>
  
</error_handling>
```

## Examples

- `/task "Add email validation"` - Creates email validation with tests
- `/task "Fix memory leak in component"` - Creates regression test first
- `/task "Optimize database query"` - Creates performance test first