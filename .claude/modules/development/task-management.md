| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# Task Management Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="task_management" category="development">
  
  <purpose>
    Execute single-component development tasks with TDD enforcement and intelligent session management.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Understand requirements completely - what EXACTLY needs to be built?</step>
    <step>2. Write FAILING test FIRST (RED phase) - no implementation yet</step>
    <step>3. Write MINIMAL code to pass test (GREEN phase) - no more than needed</step>
    <step>4. REFACTOR for quality while keeping tests green</step>
    <step>5. Check if task affects 3+ files → escalate to /swarm if yes</step>
    <step>6. Run quality gates: linting, type checking, coverage validation</step>
    <step>7. Document implementation decisions in session if active</step>
  </thinking_pattern>
  
  <trigger_conditions>
    <condition type="automatic">Feature implementation, bug fixes, refactoring requests</condition>
    <condition type="explicit">User requests /task command or single-component development</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="analysis" order="1">
      <requirements>
        Requirements clearly understood and acceptance criteria defined
        Codebase patterns identified through search and analysis
        Complexity assessment completed with session decision
      </requirements>
      <actions>
        Apply critical thinking analysis to understand true requirements
        Search existing codebase for similar implementations (DRY principle)
        Assess task complexity and determine session requirements
        Plan TDD approach with comprehensive test strategy
      </actions>
      <validation>
        Requirements documented with clear acceptance criteria
        Similar functionality identified or confirmed unique
        Session decision made based on complexity assessment
      </validation>
    </phase>
    
    <phase name="tdd_implementation" order="2">
      <requirements>
        TDD cycle strictly followed: RED-GREEN-REFACTOR
        Test coverage maintained per quality/tdd.md standards
        Code quality gates enforced throughout development
      </requirements>
      <actions>
        RED: Write failing tests defining desired behavior
        GREEN: Implement minimal code to pass tests
        REFACTOR: Improve code structure while maintaining green tests
        Continuous testing after each significant change
      </actions>
      <validation>
        All tests pass with appropriate coverage thresholds
        Code quality metrics meet standards (linting, type checking)
        TDD compliance documented in session if active
      </validation>
    </phase>
    
    <phase name="quality_verification" order="3">
      <requirements>
        TDD enforcement evidence collected per quality/tdd-enforcement.md
        Security verification completed per quality/security-gate-verification.md
        Performance benchmarks validated per quality/performance-gates.md
        Comprehensive quality gates passed per quality/gate-verification.md
      </requirements>
      <actions>
        Execute TDD enforcement verification with evidence collection
        Run security gate verification including threat modeling
        Perform performance benchmark testing with automated thresholds
        Execute comprehensive quality gate verification suite
        Generate quality compliance certificate with evidence archive
      </actions>
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
    <gate name="tdd_enforcement" requirement="Mandatory TDD enforcement per quality/tdd-enforcement.md" blocking="true"/>
    <gate name="security_verification" requirement="Security gate verification per quality/security-gate-verification.md" blocking="true"/>
    <gate name="performance_benchmarks" requirement="Performance gates per quality/performance-gates.md" blocking="true"/>
    <gate name="gate_verification" requirement="Comprehensive quality gate verification per quality/gate-verification.md" blocking="true"/>
    <gate name="code_quality" requirement="Zero linting errors, clean type checking" blocking="true"/>
    <gate name="integration_testing" requirement="All integration scenarios tested successfully" blocking="false"/>
  </quality_gates>
  
  <escalation_logic>
    <trigger condition="multiple_components">Task affects 3+ system components → escalate to /swarm</trigger>
    <trigger condition="architectural_changes">Changes affect system design → escalate to /swarm</trigger>
    <trigger condition="integration_heavy">Complex external system integration → escalate to /swarm</trigger>
    <trigger condition="performance_critical">Multi-layer optimization needed → escalate to /swarm</trigger>
    <trigger condition="prompt_engineering">Complex prompt development → escalate to /auto</trigger>
    <trigger condition="prompt_evaluation">Multi-agent prompt evaluation → escalate to /swarm</trigger>
  </escalation_logic>
  
  <session_integration>
    <mandatory_conditions>
      Multi-step tasks requiring multiple development phases
      Complex features affecting multiple system components
      Architectural changes impacting system design
    </mandatory_conditions>
    <optional_conditions>
      Single-component features with moderate complexity
      Bug fixes requiring extensive analysis
      Refactoring with broad code impact
    </optional_conditions>
    <session_documentation>
      Requirements analysis and design decisions
      TDD progress tracking with test coverage metrics
      Quality gate results and compliance verification
      Lessons learned for future development tasks
    </session_documentation>
  </session_integration>
  
  <integration_points>
    <depends_on>
      quality/tdd-enforcement.md for non-bypassable TDD enforcement
      quality/security-gate-verification.md for security verification
      quality/performance-gates.md for performance benchmarking
      quality/gate-verification.md for comprehensive quality gate orchestration
      quality/critical-thinking.md for requirement analysis
      patterns/session-management.md for session decisions
    </depends_on>
    <provides_to>
      quality/gate-verification.md for task-level quality gate results
      quality/production-standards.md for production standards integration
      patterns/multi-agent.md for escalation triggers
    </provides_to>
  </integration_points>
  
</module>
```