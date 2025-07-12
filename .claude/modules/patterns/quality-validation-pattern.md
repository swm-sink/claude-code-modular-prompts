| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Quality Validation Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="quality_validation_pattern" category="patterns">
  
  <purpose>
    Comprehensive testing and verification of code quality, ensuring systematic validation of coverage, security, performance, and integration points before deployment.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Code implementation is complete</condition>
    <condition type="explicit">Before merging or deployment</condition>
    <condition type="explicit">Quality issues need investigation</condition>
    <condition type="explicit">Compliance verification required</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="test_coverage_analysis" order="1">
      <requirements>
        Test suite must be available
        Coverage tools must be configured
        Thresholds must be defined
      </requirements>
      <actions>
        Verify comprehensive test coverage
        Check line coverage meets minimum thresholds
        Ensure branch coverage includes all decision points
        Verify critical paths are fully tested
        Confirm edge cases and error conditions covered
      </actions>
      <validation>
        Coverage thresholds are met
        All decision points are tested
        Critical paths have full coverage
        Edge cases are properly tested
      </validation>
    </phase>
    
    <phase name="code_quality_review" order="2">
      <requirements>
        Code quality tools must be available
        Style guides must be defined
        Review criteria must be established
      </requirements>
      <actions>
        Assess code quality metrics
        Verify code follows style and conventions
        Check functions are properly structured
        Ensure documentation is complete and accurate
        Identify obvious bugs or issues
      </actions>
      <validation>
        Code follows established conventions
        Function structure is appropriate
        Documentation is complete
        No obvious bugs detected
      </validation>
    </phase>
    
    <phase name="security_validation" order="3">
      <requirements>
        Security scanning tools must be available
        Security standards must be defined
        Vulnerability database must be current
      </requirements>
      <actions>
        Check for security vulnerabilities
        Validate input validation and sanitization
        Verify authentication and authorization
        Check data protection and privacy
        Scan for dependency security issues
      </actions>
      <validation>
        No critical security vulnerabilities
        Input validation is comprehensive
        Authentication is properly implemented
        Data protection is adequate
      </validation>
    </phase>
    
    <phase name="performance_verification" order="4">
      <requirements>
        Performance testing tools must be available
        Performance requirements must be defined
        Load testing environment must be ready
      </requirements>
      <actions>
        Ensure performance meets requirements
        Test response times under load
        Monitor memory usage and efficiency
        Verify database query performance
        Check resource utilization
      </actions>
      <validation>
        Performance requirements are met
        Response times are acceptable
        Memory usage is efficient
        Database performance is optimized
      </validation>
    </phase>
    
    <phase name="integration_testing" order="5">
      <requirements>
        Integration test suite must be available
        External systems must be accessible
        Test data must be prepared
      </requirements>
      <actions>
        Verify system integration points
        Test API contracts and interfaces
        Validate database interactions
        Check external service connections
        Verify error propagation and handling
      </actions>
      <validation>
        Integration points are verified
        API contracts are validated
        Database interactions work correctly
        External services are properly integrated
      </validation>
    </phase>
    
  </implementation>
  
  <quality_gates>
    <gate name="test_coverage" severity="blocking">All tests pass successfully</gate>
    <gate name="coverage_threshold" severity="blocking">Coverage thresholds are met</gate>
    <gate name="security_check" severity="blocking">No critical security issues</gate>
    <gate name="performance_requirements" severity="blocking">Performance requirements satisfied</gate>
    <gate name="integration_verification" severity="blocking">Integration points verified</gate>
  </quality_gates>
  
  <automation>
    <automated_process>Automated test execution</automated_process>
    <automated_process>Code quality metrics collection</automated_process>
    <automated_process>Security vulnerability scanning</automated_process>
    <automated_process>Performance benchmarking</automated_process>
  </automation>
  
  <integration_points>
    <provides_to>
      patterns/error-recovery-pattern.md for failure handling
      patterns/implementation-pattern.md with feedback
    </provides_to>
    <depends_on>
      patterns/tdd-cycle-pattern.md implementation validation
      ../../prompt_eng/../../prompt_eng/patterns/thinking/critical-thinking-pattern.md for issue analysis
    </depends_on>
  </integration_points>
  
  <examples>
    <example name="pre_deployment_validation">
      <description>Pre-deployment quality checks</description>
      <code>
        COVERAGE: Verify 90%+ line coverage, 85%+ branch coverage
        QUALITY: Check code style, structure, documentation
        SECURITY: Scan for vulnerabilities, validate auth
        PERFORMANCE: Test under load, check response times
        INTEGRATION: Verify API contracts, database connections
      </code>
      <expected_output>
        Comprehensive quality validation report
        All quality gates passed successfully
        System ready for deployment
      </expected_output>
    </example>
  </examples>
  
</module>
```