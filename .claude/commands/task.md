| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 80%      |

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
    <module>patterns/thinking/critical-thinking-pattern.md</module>
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
    <module>patterns/error-recovery.md</module>
    <module>patterns/context-management-pattern.md</module>
    <module>patterns/validation-pattern.md</module>
  </support_modules>
</module_orchestration>
```

## Error Handling

```xml
<error_handling>
  <rollback_procedures>
    <tdd_failure>git reset --hard HEAD~1 to previous checkpoint</tdd_failure>
    <coverage_failure>git reset --hard HEAD~1 and retry with improved tests</coverage_failure>
    <quality_gate_failure>Address specific failures and re-validate</quality_gate_failure>
    <implementation_failure>Return to GREEN phase with corrected approach</implementation_failure>
  </rollback_procedures>
  
  <escalation_paths>
    <requirements_unclear>Route to /query for clarification</requirements_unclear>
    <multi_component_scope>Route to /swarm for coordination</multi_component_scope>
    <complex_integration>Route to /feature for comprehensive planning</complex_integration>
    <production_deployment>Route to /protocol for strict standards</production_deployment>
  </escalation_paths>
  
  <failure_recovery>
    <test_failures>Analyze failure root cause, fix tests or implementation</test_failures>
    <coverage_insufficient>Identify missing test scenarios, add comprehensive coverage</coverage_insufficient>
    <quality_standards>Address specific quality issues, re-validate gates</quality_standards>
    <atomic_commit_issues>Review commit strategy, ensure proper checkpointing</atomic_commit_issues>
  </failure_recovery>
</error_handling>
```

## Examples

- `/task "Add email validation"` - Creates email validation with tests
- `/task "Fix memory leak in component"` - Creates regression test first
- `/task "Optimize database query"` - Creates performance test first