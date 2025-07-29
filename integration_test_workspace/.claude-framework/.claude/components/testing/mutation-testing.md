<prompt_component>
  <mutation_testing>
    <comprehensive_validation>
      <!-- Implement mutation testing for AI-generated code validation -->
      <mutation_strategy>
        <test_quality_validation>
          Mutation testing validates that tests actually detect bugs by:
          - Creating deliberate bugs (mutants) in the code
          - Running tests against mutated code
          - Verifying tests fail when they should
          - Measuring mutation score as test effectiveness metric
        </test_quality_validation>
        
        <mutation_operators>
          <arithmetic_mutations>
            - Change + to - and vice versa
            - Change * to / and vice versa
            - Change &lt; to &lt;= and vice versa
            - Change == to != and vice versa
            - Change increment to decrement operations
          </arithmetic_mutations>
          
          <logical_mutations>
            - Change && to || and vice versa
            - Negate boolean conditions
            - Change true to false and vice versa
            - Remove logical operators
            - Change comparison operators
          </logical_mutations>
          
          <conditional_mutations>
            - Remove if/else conditions
            - Change condition boundaries
            - Negate conditional expressions
            - Change loop conditions
            - Modify exception handling conditions
          </conditional_mutations>
          
          <statement_mutations>
            - Remove method calls
            - Change return statements
            - Remove variable assignments
            - Change constant values
            - Remove exception throwing
          </statement_mutations>
        </mutation_operators>
      </mutation_strategy>
      
      <intelligent_mutation_generation>
        <!-- AI-enhanced mutation selection based on code patterns -->
        <context_aware_mutations>
          <domain_specific_mutations>
            Generate mutations relevant to the code domain:
            - Authentication code: Mutate permission checks, session validations
            - Database code: Mutate query conditions, transaction boundaries
            - API code: Mutate parameter validation, response formatting
            - Security code: Mutate encryption, input sanitization
          </domain_specific_mutations>
          
          <pattern_based_mutations>
            Focus mutations on common failure patterns:
            - Off-by-one errors in loops and array access
            - Null reference exceptions in object access
            - Race conditions in concurrent code
            - Resource leaks in file/connection handling
          </pattern_based_mutations>
        </context_aware_mutations>
        
        <mutation_prioritization>
          <high_priority_mutations>
            Focus on mutations that represent real-world bugs:
            - Business logic critical paths
            - Security-sensitive code sections
            - Error handling and edge cases
            - Data validation and transformation
          </high_priority_mutations>
          
          <equivalence_filtering>
            Filter out equivalent mutations that don't change behavior:
            - Mutations that produce functionally identical code
            - Unreachable code mutations
            - Cosmetic changes that don't affect logic
            - Redundant mutations that test the same failure mode
          </equivalence_filtering>
        </mutation_prioritization>
      </intelligent_mutation_generation>
    </comprehensive_validation>
    
    <test_enhancement_recommendations>
      <!-- Provide specific recommendations for improving test quality -->
      <mutation_analysis>
        <killed_mutations>
          Track successfully detected mutations:
          - Document which tests successfully caught which types of bugs
          - Identify strong test patterns that consistently detect issues
          - Recognize comprehensive test coverage areas
          - Build knowledge base of effective testing strategies
        </killed_mutations>
        
        <surviving_mutations>
          Analyze undetected mutations to improve tests:
          - Identify missing test cases for specific code paths
          - Suggest additional assertions for edge cases
          - Recommend boundary condition testing
          - Highlight untested error handling scenarios
        </surviving_mutations>
      </mutation_analysis>
      
      <test_improvement_suggestions>
        <specific_test_additions>
          When mutations survive, suggest specific improvements:
          - "Add test for null input to method X"
          - "Test boundary condition when array is empty"
          - "Verify exception thrown for invalid parameter Y"
          - "Test concurrent access to shared resource Z"
        </specific_test_additions>
        
        <assertion_enhancements>
          Recommend stronger assertions:
          - Replace existence checks with behavior validation
          - Add state verification after operations
          - Include side effect validation
          - Verify error conditions and recovery
        </assertion_enhancements>
      </test_improvement_suggestions>
    </test_enhancement_recommendations>
    
    <integration_first_testing>
      <!-- Implement integration-first testing paradigm for AI development -->
      <behavioral_validation>
        <user_journey_testing>
          Focus on complete user workflows:
          - Test end-to-end business processes
          - Validate integration between components
          - Verify external API interactions
          - Test data flow through system boundaries
        </user_journey_testing>
        
        <contract_testing>
          Ensure component contracts are honored:
          - Test API input/output contracts
          - Validate data transformation contracts
          - Verify error handling contracts
          - Test performance and timing contracts
        </contract_testing>
      </behavioral_validation>
      
      <rapid_feedback_loops>
        <test_automation_integration>
          Integrate mutation testing into development workflow:
          - Run mutation tests automatically on code changes
          - Provide real-time feedback on test quality
          - Generate mutation reports for code review
          - Track mutation score trends over time
        </test_automation_integration>
        
        <ai_development_velocity>
          Maintain speed while ensuring quality:
          - Run critical mutations immediately for fast feedback
          - Schedule comprehensive mutation testing for CI/CD
          - Use incremental mutation testing for changed code
          - Provide smart mutation suggestions during development
        </ai_development_velocity>
      </rapid_feedback_loops>
    </integration_first_testing>
    
    <vibe_driven_testing>
      <!-- Implement "Test-Driven Vibe Coding" for complex features -->
      <holistic_test_approach>
        <system_behavior_testing>
          Test system "vibe" and overall behavior:
          - Does the system feel responsive and reliable?
          - Are error messages helpful and user-friendly?
          - Does the system handle edge cases gracefully?
          - Is the overall user experience smooth and intuitive?
        </system_behavior_testing>
        
        <emergent_behavior_validation>
          Test behaviors that emerge from component interactions:
          - System performance under realistic load
          - Data consistency across distributed operations
          - Error propagation and recovery across components
          - System resilience to partial failures
        </emergent_behavior_validation>
      </holistic_test_approach>
      
      <adaptive_test_generation>
        <context_aware_testing>
          Generate tests that understand context and intent:
          - Business domain-specific test scenarios
          - User persona-based testing approaches
          - Environment-specific validation (dev, staging, prod)
          - Time-sensitive and state-dependent testing
        </context_aware_testing>
        
        <evolutionary_testing>
          Evolve tests based on system usage and feedback:
          - Add new test scenarios based on production issues
          - Refine test assertions based on user feedback
          - Adapt test coverage based on risk assessment
          - Incorporate lessons learned from mutation testing
        </evolutionary_testing>
      </adaptive_test_generation>
    </vibe_driven_testing>
    
    <quality_metrics_integration>
      <!-- Integrate mutation testing with comprehensive quality metrics -->
      <mutation_score_tracking>
        <score_calculation>
          Calculate mutation testing effectiveness:
          - Mutation Score = (Killed Mutations / Total Mutations) * 100
          - Target: 80%+ mutation score for critical code paths
          - Track mutation score trends over time
          - Compare mutation scores across components and teams
        </score_calculation>
        
        <quality_gates>
          Use mutation scores in quality gates:
          - Require minimum mutation score for critical code
          - Block deployments if mutation score drops significantly
          - Alert on mutation score regressions
          - Track mutation score in code review metrics
        </quality_gates>
      </mutation_score_tracking>
      
      <comprehensive_quality_reporting>
        <multi_dimensional_metrics>
          Combine mutation testing with other quality metrics:
          - Code coverage percentage (structural coverage)
          - Mutation score (test effectiveness)
          - Cyclomatic complexity (code complexity)
          - Test execution time and performance
        </multi_dimensional_metrics>
        
        <actionable_insights>
          Provide actionable recommendations:
          - Prioritize test improvements based on mutation analysis
          - Identify high-risk code areas needing more testing
          - Suggest refactoring opportunities to improve testability
          - Recommend testing strategies for different code patterns
        </actionable_insights>
      </comprehensive_quality_reporting>
    </quality_metrics_integration>
  </mutation_testing>
</prompt_component> 