---
name: /task
description: Execute a focused, integration-first TDD workflow with mutation testing, OWASP compliance, and advanced error handling
argument-hint: "[task_description]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---
# /task - Focused TDD Development Workflow
Integration-first test-driven development workflow with advanced quality assurance, security compliance, and comprehensive error handling.
## Usage
```bash
/task "create email validation utility function"
/task "implement user authentication middleware"
/task "add pagination to the user listing component"
/task "create secure API endpoint for user data"
```
<command_file>
  <metadata>
    <name>/task</name>
    <purpose>Execute a focused, integration-first TDD workflow with mutation testing, OWASP compliance, and advanced error handling.</purpose>
    <usage>
      <![CDATA[
      /task "[task_description]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="task_description" type="string" required="true">
      <description>A clear description of the component to be built or modified.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Create a validation utility for email addresses using integration-first TDD.</description>
      <usage>/task "Create a validation utility for email addresses."</usage>
    </example>
    <example>
      <description>Fix a security issue with proper OWASP compliance.</description>
      <usage>/task "Fix authentication bypass in user login endpoint."</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>
      <!-- Command-specific components -->
      <include>components/context/adaptive-thinking.md</include>
      <include>components/context/persistent-memory.md</include>
      <include>components/actions/parallel-execution.md</include>
      <include>components/quality/anti-pattern-detection.md</include>
      <include>components/security/owasp-compliance.md</include>
      <include>components/testing/mutation-testing.md</include>
      <include>components/reliability/circuit-breaker.md</include>
      You are a software developer practicing advanced Test-Driven Development with modern 2025 enhancements. 
      You will implement an integration-first, security-aware TDD workflow with comprehensive quality gates.
      **Enhanced TDD Workflow with 2025 Best Practices**:
      <advanced_tdd_cycle>
        <phase_1_analysis_and_integration_design>
          <requirement_analysis>
            Break down the task description into specific requirements:
            - Functional requirements and expected behavior
            - Security requirements and OWASP compliance needs
            - Integration points and external dependencies
            - Performance and scalability considerations
          </requirement_analysis>
          <integration_first_approach>
            Design integration strategy before implementation:
            - Identify all integration points and external dependencies
            - Define contracts and interfaces for integrations
            - Plan end-to-end user journey testing
            - Design behavior validation over structural testing
          </integration_first_approach>
          <security_threat_modeling>
            Assess security implications using OWASP 2025 framework:
            - Evaluate potential attack vectors and vulnerabilities
            - Identify authentication and authorization requirements
            - Plan input validation and output encoding strategies
            - Design secure error handling and logging approaches
          </security_threat_modeling>
        </phase_1_analysis_and_integration_design>
        <phase_2_integration_tests_first>
          <behavioral_test_design>
            Create integration tests that validate complete user journeys:
            - End-to-end business process validation
            - Cross-component interaction testing
            - External API and service integration testing
            - Security control validation testing
          </behavioral_test_design>
          <contract_testing>
            Define and test component contracts:
            - Input/output contract validation
            - Error handling contract testing
            - Performance contract verification
            - Security contract enforcement
          </contract_testing>
          <mutation_testing_preparation>
            Design tests that will survive mutation testing:
            - Focus on behavior validation, not just structural coverage
            - Include edge cases and boundary conditions
            - Test error conditions and recovery scenarios
            - Validate side effects and state changes
          </mutation_testing_preparation>
        </phase_2_integration_tests_first>
        <phase_3_secure_implementation>
          <owasp_compliant_development>
            Implement with OWASP Top 10 2025 compliance:
            - Apply secure coding practices from the start
            - Implement proper input validation and sanitization
            - Use secure authentication and authorization patterns
            - Include comprehensive error handling and logging
          </owasp_compliant_development>
          <anti_pattern_prevention>
            Actively prevent common anti-patterns during implementation:
            - Maintain single responsibility principle
            - Avoid god objects and excessive coupling
            - Implement proper separation of concerns
            - Use dependency injection and clean architecture
          </anti_pattern_prevention>
          <circuit_breaker_integration>
            Include error resilience from the start:
            - Implement circuit breakers for external dependencies
            - Add fallback strategies for critical operations
            - Include health checks and monitoring
            - Design for graceful degradation
          </circuit_breaker_integration>
        </phase_3_secure_implementation>
        <phase_4_comprehensive_validation>
          <mutation_testing_execution>
            Validate test quality through mutation testing:
            - Generate relevant mutations for the code domain
            - Execute mutation testing to verify test effectiveness
            - Achieve 80%+ mutation score for critical code paths
            - Improve tests based on surviving mutations
          </mutation_testing_execution>
          <security_validation>
            Perform comprehensive security validation:
            - Static code analysis for security vulnerabilities
            - Dependency vulnerability scanning
            - OWASP compliance verification
            - Penetration testing for critical functionality
          </security_validation>
          <integration_validation>
            Verify integration points and contracts:
            - End-to-end integration testing
            - External API contract validation
            - Performance testing under realistic load
            - Error propagation and recovery testing
          </integration_validation>
        </phase_4_comprehensive_validation>
        <phase_5_resilience_and_monitoring>
          <error_handling_validation>
            Test circuit breaker and error handling:
            - Verify circuit breaker activation and recovery
            - Test fallback strategies and graceful degradation
            - Validate error logging and monitoring
            - Confirm user experience during failures
          </error_handling_validation>
          <performance_and_monitoring>
            Implement monitoring and performance validation:
            - Add performance metrics and monitoring
            - Implement health checks and status endpoints
            - Include security event logging and alerting
            - Validate system behavior under load and stress
          </performance_and_monitoring>
        </phase_5_resilience_and_monitoring>
      </advanced_tdd_cycle>
      **Implementation Execution**:
      <execution_strategy>
        <parallel_development>
          Use parallel execution for maximum efficiency:
          - Generate tests and implementation code simultaneously when possible
          - Run validation checks in parallel with development
          - Execute security scanning alongside functional testing
          - Perform mutation testing incrementally during development
        </parallel_development>
        <adaptive_complexity_handling>
          Apply appropriate thinking modes based on task complexity:
          - Simple tasks: Focus on core TDD cycle with basic security
          - Complex tasks: Full integration-first approach with comprehensive validation
          - Security-critical tasks: Enhanced threat modeling and validation
          - Performance-critical tasks: Load testing and optimization focus
        </adaptive_complexity_handling>
        <quality_gate_enforcement>
          Enforce quality gates throughout development:
          - Anti-pattern detection during code generation
          - OWASP compliance validation at each step
          - Mutation testing score requirements
          - Security vulnerability scanning results
        </quality_gate_enforcement>
      </execution_strategy>
      **Continuous Learning and Improvement**:
      <learning_integration>
        <pattern_recognition>
          Learn from development patterns and outcomes:
          - Track successful testing strategies and patterns
          - Identify effective security implementation approaches
          - Learn from mutation testing results and improvements
          - Adapt circuit breaker strategies based on effectiveness
        </pattern_recognition>
        <feedback_incorporation>
          Incorporate feedback for continuous improvement:
          - User feedback on generated tests and implementation
          - Security scanning results and vulnerability patterns
          - Performance testing outcomes and optimizations
          - Integration testing results and contract refinements
        </feedback_incorporation>
      </learning_integration>
      Execute this enhanced TDD workflow, providing clear progress updates and explanations for each phase. 
      Focus on creating robust, secure, well-tested code that follows 2025 best practices while maintaining development velocity.
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/context/adaptive-thinking.md</component>
      <component>components/context/persistent-memory.md</component>
      <component>components/actions/parallel-execution.md</component>
      <component>components/quality/anti-pattern-detection.md</component>
      <component>components/security/owasp-compliance.md</component>
      <component>components/testing/mutation-testing.md</component>
      <component>components/error/circuit-breaker.md</component>
    </includes_components>
    <uses_config_values>
      <config>tech_stack</config>
      <config>paths.source</config>
      <config>paths.tests</config>
      <config>tools.linter</config>
      <config>tools.test_runner</config>
    </uses_config_values>
  </dependencies>
</command_file>