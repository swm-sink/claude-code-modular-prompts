| version | last_updated | status |
|---------|--------------|--------|
| 1.1.0   | 2025-01-08   | stable |

# TDD Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="tdd" category="quality">
  
  <purpose>
    Enforce disciplined TDD with RED-GREEN-REFACTOR cycle and comprehensive coverage standards.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Any development task requiring new functionality implementation</condition>
    <condition type="explicit">User requests TDD enforcement or test-driven development</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="red_phase" order="1">
      <requirements>
        Failing tests written that define expected behavior clearly
        Tests fail for correct reasons demonstrating missing functionality
        Edge cases and error conditions covered in test scenarios
        All acceptance criteria translated into verifiable test cases
        BLOCKING GATE: Implementation CANNOT begin until RED tests exist
      </requirements>
      <actions>
        Write failing tests that specify exact behavior requirements
        Verify tests fail for expected reasons (not due to test errors)
        Cover edge cases and boundary conditions with dedicated tests
        Ensure test names clearly describe behavior being tested
        MANDATORY: Execute tests to confirm they fail with expected messages
        MANDATORY: Document test failure reasons for validation
      </actions>
      <validation>
        All tests fail with clear failure messages indicating missing functionality
        Test coverage includes normal cases, edge cases, and error conditions
        Test names provide clear documentation of expected behaviors
        ENFORCEMENT: No implementation code written until this phase complete
        VERIFICATION: Test execution results showing expected failures documented
      </validation>
      <blocking_conditions>
        <condition>Tests pass when they should fail (indicates test errors)</condition>
        <condition>Tests fail for wrong reasons (syntax errors, import issues)</condition>
        <condition>Missing tests for any acceptance criteria</condition>
        <condition>Test names are generic or unclear</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="green_phase" order="2">
      <requirements>
        Minimal implementation written to make tests pass
        No premature optimization or additional features added
        Focus maintained on current test requirements only
        All tests pass with implemented functionality
        BLOCKING GATE: Refactoring CANNOT begin until GREEN achieved
      </requirements>
      <actions>
        Write simplest possible code to make failing tests pass
        Resist adding features not required by current tests
        Ensure implementation directly addresses test requirements
        MANDATORY: Execute full test suite to verify all tests pass
        MANDATORY: Verify no new functionality beyond test requirements
        ENFORCEMENT: Reject implementations that exceed test scope
      </actions>
      <validation>
        All tests pass with minimal implementation
        No unnecessary complexity or premature optimization present
        Implementation directly corresponds to test specifications
        VERIFICATION: Test execution results showing all tests green
        ENFORCEMENT: Code review confirms minimal implementation principle
      </validation>
      <blocking_conditions>
        <condition>Any tests still failing after implementation</condition>
        <condition>Implementation includes features not tested</condition>
        <condition>Premature optimization present (complex algorithms, caching, etc.)</condition>
        <condition>Dependencies added that aren't strictly necessary</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="refactor_phase" order="3">
      <requirements>
        Code structure improved while maintaining passing tests
        Design patterns applied for better maintainability
        Code duplication eliminated through extraction and abstraction
        Tests remain green throughout refactoring process
        BLOCKING GATE: ANY test failure aborts refactoring immediately
      </requirements>
      <actions>
        Improve code structure and readability without changing behavior
        Apply SOLID principles and appropriate design patterns
        Extract common functionality and eliminate code duplication
        MANDATORY: Run tests after EVERY refactoring step
        MANDATORY: Commit after each successful refactoring iteration
        ENFORCEMENT: Stop immediately if any test starts failing
      </actions>
      <validation>
        All tests continue to pass throughout refactoring
        Code quality improved with better structure and maintainability
        No behavior changes introduced during refactoring process
        VERIFICATION: Continuous test execution confirms behavior preservation
        ENFORCEMENT: Git history shows incremental refactoring commits
      </validation>
      <blocking_conditions>
        <condition>Any test failure during refactoring (immediate rollback required)</condition>
        <condition>Behavior changes detected (test assertions modified)</condition>
        <condition>New functionality added during refactoring</condition>
        <condition>Refactoring steps too large (not incrementally verifiable)</condition>
      </blocking_conditions>
    </phase>
    
  </implementation>
  
  <strict_enforcement>
    <red_green_refactor_cycle enforcement="MANDATORY">
      <rule priority="CRITICAL">Tests MUST be written before ANY implementation code</rule>
      <rule priority="CRITICAL">Tests MUST fail for the RIGHT reasons before implementation</rule>
      <rule priority="CRITICAL">Implementation MUST be minimal to make tests pass</rule>
      <rule priority="CRITICAL">Refactoring MUST preserve ALL test behavior</rule>
      <verification>
        Each phase completion verified with test execution output
        Git history shows proper RED→GREEN→REFACTOR commit sequence
        No implementation commits without preceding test commits
      </verification>
    </red_green_refactor_cycle>
    
    <blocking_enforcement>
      <gate name="red_phase_complete">
        <requirement>All tests written and failing with expected messages</requirement>
        <verification>Execute test suite and capture failure output</verification>
        <blocking_action>PREVENT implementation until tests properly fail</blocking_action>
      </gate>
      <gate name="green_phase_complete">
        <requirement>All tests passing with minimal implementation</requirement>
        <verification>Execute test suite and confirm all green</verification>
        <blocking_action>PREVENT refactoring until all tests pass</blocking_action>
      </gate>
      <gate name="refactor_continuous">
        <requirement>Tests remain green throughout refactoring</requirement>
        <verification>Continuous test execution after each refactor step</verification>
        <blocking_action>ROLLBACK immediately on any test failure</blocking_action>
      </gate>
    </blocking_enforcement>
    
    <violation_responses>
      <violation type="implementation_before_tests">
        <action>DELETE implementation code and restart with tests</action>
        <message>TDD violation: Implementation written before tests. Restarting with RED phase.</message>
      </violation>
      <violation type="tests_pass_when_should_fail">
        <action>FIX test to properly fail before implementation</action>
        <message>TDD violation: Tests pass without implementation. Tests must fail first.</message>
      </violation>
      <violation type="premature_optimization">
        <action>SIMPLIFY implementation to minimal working code</action>
        <message>TDD violation: Implementation exceeds test requirements. Simplifying to minimal.</message>
      </violation>
      <violation type="refactor_breaks_tests">
        <action>ROLLBACK refactor and proceed incrementally</action>
        <message>TDD violation: Refactoring broke tests. Rolling back to last green state.</message>
      </violation>
    </violation_responses>
  </strict_enforcement>
  
  <coverage_requirements>
    <minimum_standards>
      Line coverage: 90% minimum for production code
      Branch coverage: 85% minimum for all decision points
      Critical paths: 100% coverage required for business logic
      Error handling: 100% coverage for exception scenarios
    </minimum_standards>
    <quality_over_quantity>
      Focus on meaningful behavior testing rather than coverage metrics
      Test business logic and critical functionality thoroughly
      Avoid testing simple getters/setters without business logic
      Ensure assertions verify actual behavior and outcomes
    </quality_over_quantity>
  </coverage_requirements>
  
  <test_organization>
    <structure>
      tests/unit/ for fast, isolated component tests
      tests/integration/ for component interaction tests
      tests/e2e/ for complete user workflow tests
      tests/fixtures/ for test data and mock objects
    </structure>
    <naming_conventions>
      Test names describe behavior: test_expired_token_returns_401_unauthorized
      Test methods follow pattern: test_[condition]_[expected_outcome]
      Test classes group related behavior: TestUserAuthentication
    </naming_conventions>
  </test_organization>
  
  <test_patterns>
    <unit_tests>
      Test individual functions and methods in isolation
      Mock external dependencies and collaborating objects
      Focus on single responsibility and behavior verification
      Execute quickly with minimal setup requirements
    </unit_tests>
    <integration_tests>
      Test component interactions and data flow
      Use real dependencies where practical for integration verification
      Verify end-to-end scenarios within bounded contexts
      Test error propagation and recovery mechanisms
    </integration_tests>
    <mocking_strategy>
      Mock external services and third-party dependencies
      Avoid mocking code you own - test real implementations
      Use dependency injection to enable effective mocking
      Verify mock interactions for behavior validation
    </mocking_strategy>
  </test_patterns>
  
  <tdd_workflows>
    <feature_development>
      Write comprehensive test suite covering all feature scenarios
      Implement feature incrementally following RED-GREEN-REFACTOR cycle
      Refactor continuously to maintain code quality and design
      Document TDD compliance in development session if active
    </feature_development>
    <bug_fixing>
      Write failing test reproducing the reported bug exactly
      Implement minimal fix to make reproduction test pass
      Add regression tests covering related scenarios
      Refactor if fix reveals design improvement opportunities
    </bug_fixing>
    <refactoring>
      Ensure comprehensive test coverage exists before refactoring
      Refactor in small incremental steps with continuous test verification
      Maintain test suite integrity throughout refactoring process
      Add tests for any previously untested code discovered during refactoring
    </refactoring>
    <prompt_engineering>
      Write failing test scenarios that specify expected prompt behavior
      Implement minimal prompt changes to make test scenarios pass
      Refactor prompts for clarity and effectiveness while maintaining test success
      Document prompt TDD compliance in prompt engineering sessions
    </prompt_engineering>
  </tdd_workflows>
  
  <quality_gates enforcement="strict">
    <gate name="red_phase_compliance" requirement="Tests written first and fail for correct reasons"/>
    <gate name="green_phase_compliance" requirement="Minimal implementation makes all tests pass"/>
    <gate name="refactor_phase_compliance" requirement="Code improved while maintaining green tests"/>
    <gate name="coverage_standards" requirement="90% line coverage, 85% branch coverage minimum"/>
    <gate name="test_quality" requirement="Meaningful behavior testing with clear assertions"/>
  </quality_gates>
  
  <session_integration>
    <complexity_tracking>
      Complex features requiring multiple TDD cycles tracked in sessions
      TDD phase progress documented with test coverage metrics
      Quality gate results preserved for audit and compliance
      Lessons learned captured for future TDD improvement
    </complexity_tracking>
    <session_documentation>
      RED phase: Failing tests and behavior specifications
      GREEN phase: Implementation approach and test passage verification
      REFACTOR phase: Design improvements and quality enhancements
      Coverage metrics: Line/branch coverage with quality assessment
    </session_documentation>
  </session_integration>
  
  <integration_points>
    <depends_on>
      patterns/tool-usage.md for parallel test execution optimization
      quality/critical-thinking.md for rigorous test case analysis
      git/conventional-commits.md for TDD-aware commit message generation
    </depends_on>
    <provides_to>
      development/task-management.md for TDD workflow integration
      quality/production-standards.md for enhanced coverage requirements
      development/prompt-engineering.md for prompt testing methodology
      git/conventional-commits.md for test-driven commit messaging
      All commands for strict TDD enforcement
    </provides_to>
  </integration_points>
  
</module>
```