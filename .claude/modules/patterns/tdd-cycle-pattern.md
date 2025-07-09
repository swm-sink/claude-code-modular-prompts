| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# TDD Cycle Pattern Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="tdd_cycle_pattern" category="patterns">
  
  <purpose>
    Test-driven development workflow with Red-Green-Refactor cycle, ensuring code quality through systematic test-first development approach with quality gates and enforcement.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Any code implementation task</condition>
    <condition type="explicit">Bug fixes requiring regression tests</condition>
    <condition type="explicit">Feature development work</condition>
    <condition type="explicit">Refactoring existing code</condition>
    <condition type="explicit">Code quality improvement</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="red_phase_write_failing_test" order="1">
      <requirements>
        Requirements must be clearly defined
        Test framework must be available
        Test structure must be planned
        No implementation code should exist yet
      </requirements>
      <actions>
        Create tests that define the desired behavior
        Write tests that specify exactly what the code should do
        Make sure tests fail for the right reasons
        Cover normal cases, edge cases, and error conditions
        Use clear, descriptive test names
        Verify tests fail with expected error messages
      </actions>
      <validation>
        Tests are written before any implementation
        Tests fail with clear, expected error messages
        All requirements are covered by tests
        Test names clearly describe behavior
        Tests fail for the right reasons (not syntax errors)
      </validation>
    </phase>
    
    <phase name="green_phase_make_tests_pass" order="2">
      <requirements>
        Failing tests from red phase must exist
        Tests must be running and failing correctly
        Implementation environment must be ready
      </requirements>
      <actions>
        Write minimal code to make tests pass
        Write the simplest possible code that makes tests pass
        Don't add features not required by tests
        Focus only on making the current tests green
        Avoid premature optimization
        Run tests frequently to ensure they pass
      </actions>
      <validation>
        All tests pass with minimal implementation
        No unnecessary complexity added
        Implementation directly addresses test requirements
        No features beyond what tests specify
        Tests can be run repeatedly with consistent results
      </validation>
    </phase>
    
    <phase name="refactor_phase_improve_code_quality" order="3">
      <requirements>
        All tests must be passing (green)
        Code quality issues must be identified
        Refactoring plan must be established
      </requirements>
      <actions>
        Improve code structure while keeping tests green
        Improve code readability and maintainability
        Remove duplication and apply design patterns
        Optimize for clarity, not premature performance
        Run tests after each refactoring step
        Make small, incremental improvements
      </actions>
      <validation>
        All tests remain green throughout refactoring
        Code quality is improved
        No behavior changes introduced
        Each refactoring step is small and safe
        Code is more maintainable after refactoring
      </validation>
    </phase>
    
  </implementation>
  
  <quality_gates>
    <gate name="test_first_enforcement" severity="blocking">
      Tests must be written before implementation
      Block implementation if no failing tests exist
    </gate>
    <gate name="test_failure_verification" severity="blocking">
      Tests must fail initially for correct reasons
      Tests must fail with expected error messages
    </gate>
    <gate name="minimal_implementation" severity="blocking">
      Implementation must be minimal to pass tests
      No features beyond what tests specify
    </gate>
    <gate name="green_tests_required" severity="blocking">
      All tests must pass after implementation
      Block refactoring if any tests are failing
    </gate>
    <gate name="refactoring_safety" severity="blocking">
      Tests must remain green throughout refactoring
      Rollback immediately if tests break during refactoring
    </gate>
    <gate name="coverage_requirements" severity="warning">
      90% line coverage minimum
      85% branch coverage minimum  
      100% coverage for business logic
      100% coverage for error handling
    </gate>
  </quality_gates>
  
  <enforcement>
    <rule type="blocking">Block implementation if no failing tests exist</rule>
    <rule type="blocking">Block refactoring if any tests are failing</rule>
    <rule type="immediate">Rollback immediately if tests break during refactoring</rule>
    <rule type="verification">Require test execution evidence at each phase</rule>
  </enforcement>
  
  <integration_points>
    <provides_to>
      quality/quality-validation.md for comprehensive testing
      development/task-management.md for development workflow
      patterns/implementation.md for code development
    </provides_to>
    <depends_on>
      patterns/critical-thinking-pattern.md for test design
      development/research-analysis.md for understanding requirements
      quality/tdd.md for TDD enforcement framework
    </depends_on>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="pattern-library.md">systematic_development</uses_pattern>
    <uses_pattern from="pattern-library.md">quality_enforcement</uses_pattern>
    <implementation_notes>
      Enforces test-first development through blocking quality gates
      Integrates with critical thinking for test design decisions
      Supports incremental development with safety nets
      Enables safe refactoring with continuous validation
    </implementation_notes>
  </pattern_usage>
  
  <configuration>
    <setting name="minimum_coverage_line" default="90" required="true">
      Minimum percentage of line coverage required
    </setting>
    <setting name="minimum_coverage_branch" default="85" required="true">
      Minimum percentage of branch coverage required
    </setting>
    <setting name="business_logic_coverage" default="100" required="true">
      Required coverage percentage for business logic
    </setting>
    <setting name="error_handling_coverage" default="100" required="true">
      Required coverage percentage for error handling
    </setting>
    <setting name="test_timeout" default="30_seconds" required="false">
      Maximum time allowed for test execution
    </setting>
  </configuration>
  
  <error_handling>
    <error code="TDD001" severity="critical">
      Implementation attempted without failing tests - enforce red phase
    </error>
    <error code="TDD002" severity="critical">
      Tests passing without implementation - review test quality
    </error>
    <error code="TDD003" severity="critical">
      Refactoring attempted with failing tests - ensure green phase
    </error>
    <error code="TDD004" severity="warning">
      Coverage below minimum threshold - improve test coverage
    </error>
    <error code="TDD005" severity="warning">
      Large refactoring step detected - break into smaller steps
    </error>
  </error_handling>
  
  <examples>
    <example name="new_feature_development">
      <description>New feature development with behavior specification</description>
      <code>
        RED: Write failing test for user authentication
        test_user_login_with_valid_credentials_should_return_token()
        GREEN: Implement minimal authentication logic to pass test
        REFACTOR: Improve authentication code structure while keeping tests green
      </code>
      <expected_output>
        Working authentication feature with comprehensive tests
        Code passes all tests with good coverage
        Clean, maintainable implementation
      </expected_output>
    </example>
    
    <example name="bug_fix_with_regression_test">
      <description>Bug fixes with regression test creation</description>
      <code>
        RED: Write failing test that reproduces the bug
        test_division_by_zero_should_raise_exception()
        GREEN: Fix the bug with minimal code changes
        REFACTOR: Improve error handling while keeping tests green
      </code>
      <expected_output>
        Bug fixed with regression test in place
        No impact on existing functionality
        Improved error handling where appropriate
      </expected_output>
    </example>
  </examples>
  
</module>
```

## Anti-patterns to Avoid
- Writing implementation before tests
- Tests that pass without implementation
- Adding features not covered by tests
- Skipping refactoring phase
- Large refactoring steps that break tests

## TDD Cycle Validation Checklist
- [ ] RED: Tests written first and failing for correct reasons
- [ ] GREEN: Minimal implementation makes all tests pass
- [ ] REFACTOR: Code quality improved while tests stay green
- [ ] Coverage requirements met (90% line, 85% branch)
- [ ] Each phase properly validated before proceeding