---
version: 1.0.0
last_updated: 2025-01-07
status: stable
---

<module name="iterative_testing" category="testing">
  
  <purpose>
    Execute TDD-driven iterative development with continuous feedback integration, ensuring high-quality implementation through systematic test-feedback cycles and progressive enhancement.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Feature development workflow Step 3 - Iterative Development</condition>
    <condition type="explicit">User requests TDD implementation or iterative development</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="tdd_cycle_implementation" order="1">
      <purpose>Execute strict TDD RED-GREEN-REFACTOR cycle for all feature implementation</purpose>
      <requirements>
        TDD cycle followed for every code change
        Test coverage maintained above 90% throughout development
        Tests written before implementation code
        Refactoring conducted after each green phase
      </requirements>
      <actions>
        RED: Write failing tests defining desired behavior
        GREEN: Implement minimal code to make tests pass
        REFACTOR: Improve code structure while maintaining green tests
        REPEAT: Continue cycle for each feature increment
      </actions>
      <validation>
        All code changes follow TDD cycle
        Test coverage consistently above 90%
        Tests are meaningful and test behavior, not implementation
        Refactoring improves code quality without breaking tests
      </validation>
    </phase>
    
    <phase name="continuous_integration" order="2">
      <purpose>Implement continuous integration with automated testing and quality checks</purpose>
      <requirements>
        Automated test suite runs on every commit
        Quality gates enforced through CI pipeline
        Integration tests validate component interactions
        Performance tests ensure requirements are met
      </requirements>
      <actions>
        Configure CI pipeline with automated test execution
        Implement quality gates for code coverage and linting
        Create integration tests for component interactions
        Add performance tests for critical user workflows
      </actions>
      <validation>
        CI pipeline runs successfully on all commits
        Quality gates prevent low-quality code from merging
        Integration tests catch component interaction issues
        Performance tests validate response time requirements
      </validation>
    </phase>
    
    <phase name="stakeholder_feedback_integration" order="3">
      <purpose>Regular stakeholder demos and feedback integration throughout development</purpose>
      <requirements>
        Regular demo sessions scheduled with stakeholders
        Feedback captured and prioritized systematically
        User experience validated through testing scenarios
        Requirements adjustments integrated quickly
      </requirements>
      <actions>
        Schedule regular demo sessions (weekly or bi-weekly)
        Capture stakeholder feedback using structured format
        Prioritize feedback using impact and effort analysis
        Integrate high-priority feedback into development cycle
      </actions>
      <validation>
        Demo sessions conducted regularly with stakeholder participation
        Feedback captured comprehensively and prioritized
        High-impact feedback integrated within current iteration
        User experience improvements validated through testing
      </validation>
    </phase>
    
    <phase name="progressive_enhancement" order="4">
      <purpose>Implement features incrementally with continuous improvement and optimization</purpose>
      <requirements>
        Features implemented in small, testable increments
        Each increment provides value to end users
        Code quality maintained through continuous refactoring
        Performance optimized incrementally
      </requirements>
      <actions>
        Break features into small, deployable increments
        Implement basic functionality first, then enhance
        Conduct code reviews and refactoring after each increment
        Monitor performance and optimize bottlenecks
      </actions>
      <validation>
        Each increment is independently testable and valuable
        Code quality metrics maintained or improved
        Performance requirements met throughout development
        No technical debt accumulated during development
      </validation>
    </phase>
    
  </implementation>
  
  <tdd_methodology enforcement="strict">
    
    <red_phase>
      <purpose>Write failing tests that define desired behavior</purpose>
      <requirements>
        Test clearly defines expected behavior
        Test fails for the right reason (missing implementation)
        Test is minimal and focused on single behavior
        Test follows naming conventions and best practices
      </requirements>
      <best_practices>
        Use descriptive test names that explain behavior
        Test one behavior per test method
        Use arrange-act-assert pattern
        Write tests from user perspective when possible
      </best_practices>
    </red_phase>
    
    <green_phase>
      <purpose>Implement minimal code to make tests pass</purpose>
      <requirements>
        Implementation makes test pass with minimal code
        No premature optimization or over-engineering
        Code is simple and focused on test requirements
        Implementation follows existing code patterns
      </requirements>
      <best_practices>
        Implement simplest solution that makes test pass
        Avoid adding functionality not required by tests
        Focus on making tests pass, not perfect code
        Use consistent coding style and patterns
      </best_practices>
    </green_phase>
    
    <refactor_phase>
      <purpose>Improve code structure while maintaining green tests</purpose>
      <requirements>
        Code structure improved without changing behavior
        All tests remain green after refactoring
        Code quality metrics maintained or improved
        Design patterns applied appropriately
      </requirements>
      <best_practices>
        Remove duplication and improve code structure
        Apply SOLID principles and design patterns
        Improve readability and maintainability
        Keep refactoring changes small and focused
      </best_practices>
    </refactor_phase>
    
  </tdd_methodology>
  
  <testing_strategy enforcement="comprehensive">
    
    <unit_testing>
      <coverage_requirement>90% line coverage minimum</coverage_requirement>
      <quality_standards>
        Tests validate behavior, not implementation details
        Tests are fast, reliable, and independent
        Tests provide clear failure messages
        Tests follow AAA (Arrange-Act-Assert) pattern
      </quality_standards>
    </unit_testing>
    
    <integration_testing>
      <purpose>Validate component interactions and data flow</purpose>
      <scope>
        API endpoint testing with real database
        Service integration testing
        External system integration validation
        End-to-end workflow testing
      </scope>
    </integration_testing>
    
    <performance_testing>
      <requirements>
        Response time under 200ms for 95th percentile
        System handles expected load without degradation
        Memory usage remains within acceptable limits
        Database queries optimized for performance
      </requirements>
      <tools>
        Load testing for concurrent user scenarios
        Profiling tools for bottleneck identification
        Database query analysis and optimization
        Memory leak detection and prevention
      </tools>
    </performance_testing>
    
  </testing_strategy>
  
  <feedback_integration_process>
    
    <stakeholder_demos>
      <frequency>Weekly or bi-weekly depending on iteration length</frequency>
      <format>
        Live demonstration of new functionality
        Structured feedback collection process
        Impact and effort analysis of feedback
        Priority assignment and integration planning
      </format>
    </stakeholder_demos>
    
    <user_testing>
      <methodology>
        User story validation through testing scenarios
        Usability testing for user experience optimization
        Accessibility testing for inclusive design
        Cross-browser and device compatibility testing
      </methodology>
    </user_testing>
    
    <feedback_prioritization>
      <criteria>
        Business impact and user value
        Implementation effort and complexity
        Alignment with MVP scope and objectives
        Technical feasibility and architecture fit
      </criteria>
    </feedback_prioritization>
    
  </feedback_integration_process>
  
  <quality_gates enforcement="strict">
    <gate name="tdd_compliance" requirement="Full TDD cycle followed for all code changes"/>
    <gate name="test_coverage" requirement="90% test coverage maintained throughout development"/>
    <gate name="ci_success" requirement="All CI pipeline checks pass on every commit"/>
    <gate name="stakeholder_validation" requirement="Regular stakeholder feedback captured and integrated"/>
    <gate name="performance_requirements" requirement="Performance benchmarks met at each iteration"/>
  </quality_gates>
  
  <continuous_improvement>
    <retrospectives>
      <frequency>End of each development iteration</frequency>
      <focus>
        What worked well in the iteration
        What could be improved in the process
        Action items for next iteration
        Process optimization opportunities
      </focus>
    </retrospectives>
    <metrics_tracking>
      <code_quality>Test coverage, linting results, code complexity</code_quality>
      <development_velocity>Story points completed, time to completion</development_velocity>
      <defect_rates>Bugs found in testing vs production</defect_rates>
      <stakeholder_satisfaction>Feedback quality and integration success</stakeholder_satisfaction>
    </metrics_tracking>
  </continuous_improvement>
  
  <integration_points>
    <depends_on>
      development/mvp-strategy.md for implementation guidance
      quality/tdd.md for TDD methodology and best practices
      patterns/session-management.md for stakeholder collaboration
    </depends_on>
    <provides_to>
      development/feature-workflow.md for Step 3 iterative development
      quality/feature-validation.md for validation criteria
      quality/production-standards.md for quality enforcement
    </provides_to>
  </integration_points>
  
</module>