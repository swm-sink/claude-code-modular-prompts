| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# Research-First Task Management Module with Framework Integration

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="task_management" category="development">
  
  <purpose>
    Execute single-component development tasks with research-first methodology, RISE framework integration, TDD enforcement, and intelligent session management for optimal development outcomes.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>task_description, acceptance_criteria</required>
      <optional>existing_tests, session_context, performance_targets</optional>
    </inputs>
    <outputs>
      <success>implemented_code, passing_tests, coverage_report, quality_validation</success>
      <failure>tdd_violations, quality_failures, escalation_recommendations</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Apply research-first methodology to understand task context and requirements
      2. Integrate RISE framework for structured development approach
      3. Execute TDD cycle: RED → GREEN → REFACTOR with strict enforcement
      4. Run comprehensive quality gates and validation
      5. Document results and escalate if complexity exceeds boundaries
      6. Return validated implementation with complete test coverage and research insights
    </claude_4_behavior>
  </execution_pattern>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Apply research-first methodology - systematically understand context, constraints, and requirements</step>
    <step>2. Integrate RISE framework - define Role, Input, Steps, Expectation for structured development</step>
    <step>3. Write FAILING test FIRST (RED phase) - no implementation yet, based on research insights</step>
    <step>4. Write MINIMAL code to pass test (GREEN phase) - no more than needed, following research-informed approach</step>
    <step>5. REFACTOR for quality while keeping tests green - apply research-discovered patterns</step>
    <step>6. Check if task affects 3+ files → escalate to /swarm if yes</step>
    <step>7. Run quality gates: linting, type checking, coverage validation</step>
    <step>8. Document implementation decisions and research insights in session if active</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="automatic">Feature implementation, bug fixes, refactoring requests</condition>
    <condition type="explicit">User requests /task command or single-component development</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="research_first_analysis" order="1">
      <requirements>
        Research-first methodology applied with systematic context understanding
        RISE framework integration for structured development approach
        Requirements clearly understood and acceptance criteria defined
        Codebase patterns identified through comprehensive search and analysis
        Complexity assessment completed with session decision
      </requirements>
      <actions>
        Apply research-first methodology to understand task context, constraints, and domain
        Integrate RISE framework for structured role definition and expectation setting
        Execute parallel search operations for existing implementations and patterns
        Apply critical thinking analysis to understand true requirements and hidden complexities
        Search existing codebase for similar implementations (DRY principle)
        Assess task complexity and determine session requirements
        Plan TDD approach with comprehensive test strategy informed by research
      </actions>
      <atomic_commit_integration>
        <checkpoint>git add -A && git commit -m "PRE-OP: task-management - backup state before task implementation"</checkpoint>
        <validation_before_commit>Current state preserved for rollback capability</validation_before_commit>
        <rollback_trigger>If task analysis reveals complexity > scope, rollback with: git reset --hard HEAD~1</rollback_trigger>
        <safety_check>Verify task scope appropriate for single-component development before proceeding</safety_check>
      </atomic_commit_integration>
      <validation>
        Research-first context understanding documented with domain insights
        RISE framework integration validated with clear role and expectation definition
        Requirements documented with clear acceptance criteria
        Similar functionality identified or confirmed unique
        Session decision made based on complexity assessment
        Research insights integrated into development planning
      </validation>
    </phase>
    
    <phase name="research_informed_tdd_implementation" order="2">
      <requirements>
        Research insights integrated into TDD cycle implementation
        RISE framework steps followed for structured development
        TDD cycle strictly followed: RED-GREEN-REFACTOR
        Test coverage maintained per ../../system/../../system/quality/tdd.md standards
        Code quality gates enforced throughout development
      </requirements>
      <actions>
        Apply research-discovered patterns and best practices to development approach
        Follow RISE framework steps for systematic implementation
        RED: Write failing tests defining desired behavior based on research insights
        GREEN: Implement minimal code to pass tests following research-informed patterns
        REFACTOR: Improve code structure while maintaining green tests using research findings
        Continuous testing after each significant change with research-based validation
      </actions>
      <atomic_commit_integration>
        <checkpoint>git add . && git commit -m "OP-EXEC: task-management implementation - TDD cycle complete with tests passing"</checkpoint>
        <validation_before_commit>All tests must pass and coverage thresholds met</validation_before_commit>
        <rollback_trigger>If implementation fails or tests don't pass, rollback with: git reset --hard HEAD~1</rollback_trigger>
        <safety_check>Verify complete TDD cycle compliance before proceeding to quality verification</safety_check>
      </atomic_commit_integration>
      <validation>
        Research insights successfully integrated into implementation
        RISE framework steps completed with structured development approach
        All tests pass with appropriate coverage thresholds
        Code quality metrics meet standards (linting, type checking)
        TDD compliance documented in session if active
        Research-informed implementation patterns validated
      </validation>
    </phase>
    
    <phase name="quality_verification" order="3">
      <requirements>
        TDD enforcement evidence collected per ../../system/../../system/quality/tdd-enforcement.md
        Security verification completed per ../../system/../../system/quality/security-gate-verification.md
        Performance benchmarks validated per ../../system/../../system/quality/performance-gates.md
        Comprehensive quality gates passed per ../../system/../../system/quality/gate-verification.md
      </requirements>
      <actions>
        Execute TDD enforcement verification with evidence collection
        Run security gate verification including threat modeling
        Perform performance benchmark testing with automated thresholds
        Execute comprehensive quality gate verification suite
        Generate quality compliance certificate with evidence archive
      </actions>
      <atomic_commit_integration>
        <checkpoint>git add -A && git commit -m "POST-OP: task-management complete - quality verification passed with evidence"</checkpoint>
        <validation_before_commit>All quality gates must pass with evidence collection</validation_before_commit>
        <rollback_trigger>If quality verification fails, rollback with: git reset --hard HEAD~2 (return to pre-task state)</rollback_trigger>
        <safety_check>Verify complete quality compliance before task completion</safety_check>
      </atomic_commit_integration>
      <validation>
        TDD evidence trail complete with RED-GREEN-REFACTOR proof
        Security threats identified and mitigated with evidence
        Performance benchmarks meet p95 <200ms and other thresholds
        All quality gates passed with automated compliance verification
        Quality evidence archived for audit trail
      </validation>
    </phase>
    
  </implementation>
  
  <quality_gates enforcement="strict">
    <gate name="research_first_validation" requirement="Research-first methodology properly applied with context understanding" blocking="true"/>
    <gate name="rise_framework_integration" requirement="RISE framework integration validated with structured development approach" blocking="true"/>
    <gate name="tdd_enforcement" requirement="Mandatory TDD enforcement per ../../system/../../system/quality/tdd-enforcement.md" blocking="true"/>
    <gate name="security_verification" requirement="Security gate verification per ../../system/../../system/quality/security-gate-verification.md" blocking="true"/>
    <gate name="performance_benchmarks" requirement="Performance gates per ../../system/../../system/quality/performance-gates.md" blocking="true"/>
    <gate name="gate_verification" requirement="Comprehensive quality gate verification per ../../system/../../system/quality/gate-verification.md" blocking="true"/>
    <gate name="code_quality" requirement="Zero linting errors, clean type checking" blocking="true"/>
    <gate name="integration_testing" requirement="All integration scenarios tested successfully" blocking="false"/>
  </quality_gates>
  
  <escalation_logic>
    <trigger condition="multiple_components">Task affects 3+ system components → escalate to /swarm with TRACE framework</trigger>
    <trigger condition="architectural_changes">Changes affect system design → escalate to /swarm with TRACE framework</trigger>
    <trigger condition="integration_heavy">Complex external system integration → escalate to /swarm with TRACE framework</trigger>
    <trigger condition="performance_critical">Multi-layer optimization needed → escalate to /swarm with TRACE framework</trigger>
    <trigger condition="complex_requirements">Requirements need comprehensive analysis → escalate to /feature with SOAR/CLEAR frameworks</trigger>
    <trigger condition="research_intensive">Extensive research needed → escalate to /query with LEAP/CLEAR frameworks</trigger>
    <trigger condition="framework_optimization">Framework selection needed → escalate to /auto with framework selection intelligence</trigger>
    <trigger condition="prompt_engineering">Complex prompt development → escalate to /auto with framework optimization</trigger>
    <trigger condition="prompt_evaluation">Multi-agent prompt evaluation → escalate to /swarm with TRACE framework</trigger>
  </escalation_logic>
  
  <session_integration>
    <mandatory_conditions>
      Multi-step tasks requiring multiple development phases
      Complex features affecting multiple system components
      Architectural changes impacting system design
      Research-intensive tasks requiring context preservation
    </mandatory_conditions>
    <optional_conditions>
      Single-component features with moderate complexity
      Bug fixes requiring extensive analysis
      Refactoring with broad code impact
      Tasks with significant research-first methodology requirements
    </optional_conditions>
    <session_documentation>
      Research-first methodology findings and insights
      Requirements analysis and design decisions
      RISE framework integration and structured development approach
      TDD progress tracking with test coverage metrics
      Quality gate results and compliance verification
      Lessons learned for future development tasks
    </session_documentation>
  </session_integration>
  
  <integration_points>
    <depends_on>
      ../../system/../../system/quality/tdd-enforcement.md for non-bypassable TDD enforcement
      ../../system/../../system/quality/security-gate-verification.md for security verification
      ../../system/../../system/quality/performance-gates.md for performance benchmarking
      ../../system/../../system/quality/gate-verification.md for comprehensive quality gate orchestration
      ../../system/../../system/quality/critical-thinking.md for requirement analysis
      ../../system/session/session-management.md for session decisions
    </depends_on>
    <provides_to>
      ../../system/../../system/quality/gate-verification.md for task-level quality gate results
      ../../system/../../system/quality/production-standards.md for production standards integration
      patterns/multi-agent.md for escalation triggers
    </provides_to>
  </integration_points>
  
</module>
```