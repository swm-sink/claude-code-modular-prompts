<prompt_component>
  <step name="Anti-Pattern Detection and Prevention">
    <description>
Real-time detection and prevention of common anti-patterns in LLM-generated code including god objects, testing theatre, premature optimization, and hallucinated dependencies. Provides immediate feedback and alternative patterns to ensure code quality and maintainability.
    </description>
  </step>

  <anti_pattern_detection>
    <real_time_validation>
      <!-- Detect and prevent common LLM anti-patterns during code generation -->
      <pattern_recognition>
        <god_object_detection>
          <trigger>Class or module with excessive responsibilities</trigger>
          <indicators>
            - Single class with 10+ methods across different domains
            - Method names spanning authentication, validation, database, API, UI concerns
            - File size exceeding 500 lines with mixed responsibilities
            - Import statements from 5+ different domains
          </indicators>
          <prevention>
            When generating code, actively check for responsibility separation:
            - Limit each class to a single, well-defined responsibility
            - Extract distinct concerns into separate modules/classes
            - Use composition and dependency injection over inheritance
            - Suggest service layer patterns for complex operations
          </prevention>
        </god_object_detection>
        
        <testing_theatre_detection>
          <trigger>Tests that don't actually validate functionality</trigger>
          <indicators>
            - Tests that only check method existence without behavior validation
            - Mock-heavy tests that don't test real integrations
            - Tests with no assertions or trivial assertions
            - 100% coverage with no meaningful failure scenarios
          </indicators>
          <prevention>
            Generate meaningful tests that validate behavior:
            - Focus on input/output relationships and business logic
            - Test edge cases and error conditions explicitly
            - Use integration tests for critical user journeys
            - Implement mutation testing validation where appropriate
          </prevention>
        </testing_theatre_detection>
        
        <hallucinated_api_detection>
          <trigger>Usage of non-existent APIs or methods</trigger>
          <indicators>
            - Method calls to non-existent library functions
            - Import statements for packages not in dependencies
            - Configuration options that don't exist in frameworks
            - Syntax patterns that don't match language specifications
          </indicators>
          <prevention>
            Validate all API usage before code generation:
            - Check against project dependencies and versions
            - Verify method signatures against documentation
            - Use only confirmed, existing API patterns
            - When uncertain, suggest verification steps to user
          </prevention>
        </hallucinated_api_detection>
        
        <complexity_explosion_detection>
          <trigger>Unnecessarily complex solutions to simple problems</trigger>
          <indicators>
            - Over-engineered patterns for straightforward requirements
            - Multiple layers of abstraction for simple operations
            - Complex inheritance hierarchies for basic functionality
            - Framework-heavy solutions for simple data processing
          </indicators>
          <prevention>
            Apply simplicity-first principles:
            - Start with the simplest solution that works
            - Add complexity only when clearly justified
            - Prefer composition over complex inheritance
            - Use established patterns appropriately, not universally
          </prevention>
        </complexity_explosion_detection>
      </pattern_recognition>
      
      <quality_gates>
        <!-- Implement quality gates that prevent anti-patterns -->
        <pre_generation_checks>
          <requirement_analysis>
            Before generating code, analyze requirements for:
            - Scope and complexity appropriateness
            - Existing patterns in the codebase
            - Architecture alignment and consistency
            - Dependency and integration implications
          </requirement_analysis>
          
          <architecture_validation>
            Ensure proposed solution aligns with:
            - Existing project architecture patterns
            - Technology stack capabilities and limitations
            - Team coding standards and conventions
            - Performance and scalability requirements
          </architecture_validation>
        </pre_generation_checks>
        
        <generation_monitoring>
          <real_time_validation>
            During code generation, continuously check for:
            - Responsibility concentration in single components
            - API usage against verified documentation
            - Test quality and meaningful coverage
            - Complexity appropriateness for requirements
          </real_time_validation>
          
          <pattern_enforcement>
            Actively enforce positive patterns:
            - Single Responsibility Principle adherence
            - Dependency injection over hard coupling
            - Interface segregation and clean abstractions
            - Meaningful test scenarios with proper assertions
          </pattern_enforcement>
        </generation_monitoring>
        
        <post_generation_verification>
          <automated_analysis>
            After code generation, verify:
            - All imported packages exist in project dependencies
            - Method calls match actual API signatures
            - Test coverage includes meaningful failure scenarios
            - Code complexity metrics within acceptable ranges
          </automated_analysis>
          
          <quality_scoring>
            Generate quality scores based on:
            - Anti-pattern presence and severity
            - Architecture alignment and consistency
            - Test quality and coverage meaningfulness
            - Code maintainability and readability metrics
          </quality_scoring>
        </post_generation_verification>
      </quality_gates>
    </real_time_validation>
    
    <improvement_suggestions>
      <!-- Provide specific, actionable improvement recommendations -->
      <refactoring_recommendations>
        <god_object_resolution>
          When god objects detected, suggest specific refactoring:
          - Extract authentication logic into AuthService
          - Move validation to separate ValidationService
          - Create dedicated data access layer
          - Implement facade pattern for complex integrations
        </god_object_resolution>
        
        <test_improvement>
          When testing theatre detected, suggest improvements:
          - Add behavior-driven test scenarios
          - Implement integration tests for critical paths
          - Use property-based testing for complex logic
          - Add mutation testing for test quality validation
        </test_improvement>
        
        <api_verification>
          When API issues detected, provide guidance:
          - Verify against official documentation
          - Check package versions and compatibility
          - Suggest alternative, verified approaches
          - Recommend gradual implementation with validation
        </api_verification>
      </refactoring_recommendations>
      
      <preventive_guidance>
        <design_principles>
          Promote positive patterns through:
          - Clear separation of concerns examples
          - Dependency injection and inversion patterns
          - Interface-based design for testability
          - Incremental complexity introduction
        </design_principles>
        
        <quality_metrics>
          Track and improve based on:
          - Cyclomatic complexity per method/class
          - Dependency counts and coupling metrics
          - Test mutation score and coverage quality
          - Code duplication and reusability metrics
        </quality_metrics>
      </preventive_guidance>
    </improvement_suggestions>
    
    <learning_integration>
      <!-- Learn from detected patterns to improve future generation -->
      <pattern_memory>
        <success_patterns>
          Record successful patterns that avoid anti-patterns:
          - Well-structured service layer implementations
          - Effective test organization and coverage
          - Clean API integration examples
          - Appropriate complexity management
        </success_patterns>
        
        <failure_patterns>
          Learn from detected anti-patterns:
          - Common god object emergence patterns
          - Typical testing theatre indicators
          - Frequent API hallucination scenarios
          - Complexity explosion triggers
        </failure_patterns>
      </pattern_memory>
      
      <adaptive_prevention>
        <project_specific_learning>
          Adapt detection to project patterns:
          - Learn project's architecture conventions
          - Understand team's testing approaches
          - Recognize established design patterns
          - Identify common integration patterns
        </project_specific_learning>
        
        <continuous_improvement>
          Evolve detection capabilities:
          - Refine anti-pattern recognition accuracy
          - Improve suggestion relevance and specificity
          - Update validation rules based on new patterns
          - Enhance quality metrics and scoring
        </continuous_improvement>
      </adaptive_prevention>
    </learning_integration>
  </anti_pattern_detection>

  <o>
Anti-pattern detection completed with real-time validation and prevention mechanisms active:

**Patterns Detected:** [count] potential anti-patterns identified
**Prevented Issues:** God objects, testing theatre, premature optimization, hallucinated dependencies  
**Quality Score:** [0-100] code quality rating
**Recommendations:** [count] improvement suggestions provided
**Validation Status:** All generated code validated against anti-pattern rules
  </o>
</prompt_component> 