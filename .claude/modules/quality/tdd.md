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
      </requirements>
      <actions>
        Write failing tests that specify exact behavior requirements
        Verify tests fail for expected reasons (not due to test errors)
        Cover edge cases and boundary conditions with dedicated tests
        Ensure test names clearly describe behavior being tested
      </actions>
      <validation>
        All tests fail with clear failure messages indicating missing functionality
        Test coverage includes normal cases, edge cases, and error conditions
        Test names provide clear documentation of expected behaviors
      </validation>
    </phase>
    
    <phase name="green_phase" order="2">
      <requirements>
        Minimal implementation written to make tests pass
        No premature optimization or additional features added
        Focus maintained on current test requirements only
        All tests pass with implemented functionality
      </requirements>
      <actions>
        Write simplest possible code to make failing tests pass
        Resist adding features not required by current tests
        Ensure implementation directly addresses test requirements
        Verify all tests pass before proceeding to refactor phase
      </actions>
      <validation>
        All tests pass with minimal implementation
        No unnecessary complexity or premature optimization present
        Implementation directly corresponds to test specifications
      </validation>
    </phase>
    
    <phase name="refactor_phase" order="3">
      <requirements>
        Code structure improved while maintaining passing tests
        Design patterns applied for better maintainability
        Code duplication eliminated through extraction and abstraction
        Tests remain green throughout refactoring process
      </requirements>
      <actions>
        Improve code structure and readability without changing behavior
        Apply SOLID principles and appropriate design patterns
        Extract common functionality and eliminate code duplication
        Run tests continuously to ensure behavior preservation
      </actions>
      <validation>
        All tests continue to pass throughout refactoring
        Code quality improved with better structure and maintainability
        No behavior changes introduced during refactoring process
      </validation>
    </phase>
    
  </implementation>
  
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
    </depends_on>
    <provides_to>
      development/task-management.md for TDD workflow integration
      development/protocol-enforcement.md for enhanced coverage requirements
      development/prompt-engineering.md for prompt testing methodology
      quality/production-standards.md for enterprise testing standards
    </provides_to>
  </integration_points>
  
</module>