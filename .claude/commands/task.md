| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /task - Single-component development with quality gates

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Execute focused development tasks with MANDATORY TDD cycle">
  
  <delegation target="modules/development/task-management.md">
    Research → Write FAILING test → Implement → Make test PASS → Refactor → Quality gates
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Understand requirement and define acceptance criteria</action>
      <critical_thinking>
        - What exactly needs to be implemented/fixed?
        - What are the edge cases and constraints?
        - Is this truly a single-component task or multi-component?
        - What could go wrong with this approach?
      </critical_thinking>
      <output_format>REQUIREMENT_ANALYSIS: Clear problem statement with acceptance criteria</output_format>
      <validation>Acceptance criteria defined and testable</validation>
      <enforcement>BLOCK if requirements unclear or multi-component detected</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Execute TDD RED phase - write failing tests FIRST</action>
      <critical_thinking>
        - What behavior should I test to verify correctness?
        - Are my test scenarios comprehensive (normal, edge, error cases)?
        - Do tests fail for the RIGHT reasons?
        - Have I covered all acceptance criteria with tests?
      </critical_thinking>
      <output_format>FAILING_TESTS_CREATED: Test files with specific failing assertions</output_format>
      <validation>Tests written, executed, and fail with expected error messages</validation>
      <enforcement>BLOCK implementation until tests properly fail - use quality/tdd.md#red_phase</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Execute TDD GREEN phase - minimal implementation</action>
      <critical_thinking>
        - What's the simplest code that makes tests pass?
        - Am I avoiding premature optimization?
        - Does implementation directly address test requirements?
        - Are all tests now passing?
      </critical_thinking>
      <output_format>MINIMAL_IMPLEMENTATION: Code that makes all tests pass</output_format>
      <validation>All tests pass with minimal, focused implementation</validation>
      <enforcement>BLOCK refactoring until GREEN achieved - use quality/tdd.md#green_phase</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Execute TDD REFACTOR phase - improve design while maintaining green tests</action>
      <critical_thinking>
        - How can I improve code structure without changing behavior?
        - What design patterns would improve maintainability?
        - Are there any code smells to eliminate?
        - Do tests remain green throughout refactoring?
      </critical_thinking>
      <output_format>REFACTORED_CODE: Improved design with all tests still passing</output_format>
      <validation>Code quality improved, all tests remain green, no behavior changes</validation>
      <enforcement>ROLLBACK immediately if any test fails - use quality/tdd.md#refactor_phase</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Validate quality gates and coverage requirements</action>
      <critical_thinking>
        - Is test coverage ≥90% for new code?
        - Do all quality gates pass per production-standards.md?
        - Are there any security or performance concerns?
        - Is documentation adequate for the changes?
      </critical_thinking>
      <output_format>QUALITY_VALIDATION: Coverage metrics, quality gate results, documentation status</output_format>
      <validation>All quality gates pass, coverage requirements met</validation>
      <enforcement>BLOCK completion until quality/production-standards.md gates pass</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <tdd_integration enforcement="MANDATORY">
    <red_phase>Write failing tests for all acceptance criteria using quality/tdd.md#red_phase_compliance</red_phase>
    <green_phase>Implement minimal solution to make tests pass using quality/tdd.md#green_phase_compliance</green_phase>
    <refactor_phase>Improve design while maintaining green tests using quality/tdd.md#refactor_phase_compliance</refactor_phase>
    <validation>Reference quality/tdd.md#quality_gates for strict enforcement</validation>
    <blocking_conditions>
      <condition>Implementation attempted before tests written</condition>
      <condition>Tests pass when they should fail (incorrect tests)</condition>
      <condition>Implementation exceeds test requirements (over-engineering)</condition>
      <condition>Refactoring breaks any existing tests</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <examples>
    /task "Add email validation"      # Creates test_email_validation.py FIRST
    /task "Fix memory leak" --fix     # Creates regression test FIRST
    /task "Refactor to SOLID" --refactor # Ensures tests exist FIRST
    /task "Optimize database query"   # Creates performance test FIRST
  </examples>
  
  <rules enforcement="STRICT">
    <rule priority="CRITICAL">ALWAYS write failing test BEFORE implementation</rule>
    <rule priority="CRITICAL">NEVER write code without test coverage</rule>
    <rule priority="HIGH">90%+ test coverage MANDATORY</rule>
    <rule priority="HIGH">Quality gates from production-standards.md</rule>
    <rule priority="MEDIUM">Escalate to /swarm if touches 3+ files</rule>
  </rules>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before any action</module>
      <module>quality/tdd.md - Strict RED-GREEN-REFACTOR enforcement</module>
      <module>development/task-management.md - Task execution workflow</module>
      <module>quality/production-standards.md - Quality gate validation</module>
    </core_stack>
    <contextual_modules>
      <conditional module="patterns/session-management.md" condition="complex_task OR multiple_files"/>
      <conditional module="git/conventional-commits.md" condition="task_complete"/>
      <conditional module="quality/pre-commit.md" condition="code_changes"/>
    </contextual_modules>
  </module_execution>
  
  <pattern_usage>
    • Implements tdd_cycle pattern EXPLICITLY (RED→GREEN→REFACTOR)
    • Uses parallel_execution for file operations
    • Applies single_responsibility pattern
    • Leverages explicit_validation for error handling
    • Uses three_x_rule for implementation planning
    • Integrates quality gates from production-standards.md
    • Uses error-recovery.md for resilient development
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/development/task-management.md for full implementation
    See modules/quality/tdd.md for TDD enforcement
  </pattern_usage>
  
</command>
```