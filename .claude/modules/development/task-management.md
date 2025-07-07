---
version: 1.0.0
last_updated: 2025-01-07
status: stable
---

<module name="task_management" category="development">
  
  <purpose>
    Execute single-component development tasks with TDD enforcement and intelligent session management.
  </purpose>
  
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
        Test coverage >90% line, >85% branch maintained
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
        All quality gates passed before completion
        Integration testing completed successfully
        Security implications reviewed and addressed
      </requirements>
      <actions>
        Execute comprehensive quality gate validation
        Run integration tests with system components
        Perform security review for sensitive changes
        Update documentation reflecting implementation
      </actions>
      <validation>
        Zero linting errors and clean security scan
        Integration tests pass without system regressions
        Documentation updated with implementation details
      </validation>
    </phase>
    
  </implementation>
  
  <quality_gates enforcement="strict">
    <gate name="tdd_compliance" requirement="RED-GREEN-REFACTOR cycle documented and followed"/>
    <gate name="test_coverage" requirement="90% line coverage and 85% branch coverage minimum"/>
    <gate name="code_quality" requirement="Zero linting errors, clean type checking"/>
    <gate name="integration_testing" requirement="All integration scenarios tested successfully"/>
    <gate name="security_review" requirement="Security implications identified and addressed"/>
  </quality_gates>
  
  <escalation_logic>
    <trigger condition="multiple_components">Task affects 3+ system components → escalate to /swarm</trigger>
    <trigger condition="architectural_changes">Changes affect system design → escalate to /swarm</trigger>
    <trigger condition="integration_heavy">Complex external system integration → escalate to /swarm</trigger>
    <trigger condition="performance_critical">Multi-layer optimization needed → escalate to /swarm</trigger>
    <trigger condition="prompt_engineering">Complex prompt development → delegate to /prompt</trigger>
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
      quality/tdd.md for TDD cycle enforcement
      quality/critical-thinking.md for requirement analysis
      patterns/session-management.md for session decisions
    </depends_on>
    <provides_to>
      development/protocol-enforcement.md for production standards
      patterns/multi-agent.md for escalation triggers
    </provides_to>
  </integration_points>
  
</module>