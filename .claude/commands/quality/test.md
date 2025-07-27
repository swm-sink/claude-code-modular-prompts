---
name: /test
description: Unified intelligent testing framework with automated test generation, comprehensive coverage analysis, environment management, and multi-format reporting
argument-hint: "[type] [target] [options]"
allowed-tools: Read, Write, Edit, Bash, Grep
---
# /test - Unified Intelligent Testing Framework
Comprehensive testing solution combining unit, integration, and coverage analysis with automated test generation, environment management, and advanced reporting capabilities.
## Usage
```bash
# Unit Testing
/test unit "src/module.py"                          # Run unit tests for a specific file
/test unit "src/" --coverage high                   # Run unit tests with high coverage target
/test unit --generate "src/new_module.py"           # Generate unit tests for new code

# Integration Testing  
/test integration "api_tests" --env "docker.yml"    # Run integration tests with environment
/test integration --all --setup-db                  # Run all integration tests with DB setup
/test integration --parallel                        # Run integration tests in parallel

# Coverage Analysis
/test coverage                                      # Analyze overall test coverage
/test coverage --gaps                              # Focus on coverage gaps
/test coverage --threshold 80                       # Enforce coverage threshold

# Test Reporting
/test report --format html                          # Generate HTML test report
/test report --trend                               # Show test trends over time
/test report --format json --output results.json   # Export results as JSON

# Combined Operations
/test all                                          # Run all test types
/test --watch                                      # Continuous testing mode
/test --pattern "*_critical_*"                     # Test specific patterns
```
<command_file>
  <metadata>
    <name>/test</name>
    <purpose>Unified intelligent testing framework with automated test generation, comprehensive coverage analysis, environment management, and multi-format reporting</purpose>
    <usage>
      <![CDATA[
      /test [type] [target] [options]
      
      Types: unit, integration, coverage, report, all
      Options: --coverage, --env, --format, --parallel, --watch, --gaps, --setup-db, --generate, --pattern, --threshold
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="type" type="string" required="false" default="all">
      <description>Type of testing to perform: unit, integration, coverage, report, or all</description>
    </argument>
    <argument name="target" type="string" required="false" default=".">
      <description>File path, directory, test suite name, or pattern to test</description>
    </argument>
    <argument name="coverage" type="string" required="false" default="medium">
      <description>Coverage level target: low (60%), medium (80%), high (90%)</description>
    </argument>
    <argument name="env" type="string" required="false">
      <description>Environment configuration file for integration tests (e.g., docker-compose.yml)</description>
    </argument>
    <argument name="format" type="string" required="false" default="summary">
      <description>Report format: summary, detailed, html, pdf, json, junit</description>
    </argument>
    <argument name="parallel" type="boolean" required="false" default="false">
      <description>Run tests in parallel for improved performance</description>
    </argument>
    <argument name="watch" type="boolean" required="false" default="false">
      <description>Enable watch mode for continuous testing on file changes</description>
    </argument>
    <argument name="gaps" type="boolean" required="false" default="false">
      <description>Focus on coverage gaps and untested code paths</description>
    </argument>
    <argument name="setup_db" type="boolean" required="false" default="false">
      <description>Setup and seed database before integration tests</description>
    </argument>
    <argument name="generate" type="string" required="false">
      <description>Generate tests for specified file or module</description>
    </argument>
    <argument name="pattern" type="string" required="false">
      <description>Pattern to filter tests (glob or regex)</description>
    </argument>
    <argument name="threshold" type="number" required="false">
      <description>Minimum coverage threshold percentage</description>
    </argument>
    <argument name="output" type="string" required="false">
      <description>Output file for test results</description>
    </argument>
    <argument name="trend" type="boolean" required="false" default="false">
      <description>Show historical test trends and metrics</description>
    </argument>
    <argument name="auto_fix" type="boolean" required="false" default="false">
      <description>Automatically fix simple test failures</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Run all tests with coverage analysis</description>
      <usage>/test all --coverage high</usage>
    </example>
    <example>
      <description>Generate and run unit tests for new module</description>
      <usage>/test unit --generate "src/new_feature.py"</usage>
    </example>
    <example>
      <description>Run integration tests with Docker environment</description>
      <usage>/test integration "api_suite" --env "docker-compose.test.yml" --setup-db</usage>
    </example>
    <example>
      <description>Analyze coverage gaps and generate report</description>
      <usage>/test coverage --gaps --format html</usage>
    </example>
    <example>
      <description>Continuous testing with pattern filtering</description>
      <usage>/test --watch --pattern "*_critical_*" --parallel</usage>
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
      <include>components/testing/testing-framework.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      
You are an advanced unified testing specialist. The user wants to perform comprehensive testing operations including unit testing, integration testing, coverage analysis, and test reporting.

**Unified Testing Process:**

1. **Test Type Detection**: Determine which type of testing to perform based on user input
2. **Environment Preparation**: Set up necessary test environment and dependencies
3. **Test Execution**: Run appropriate tests based on type and options
4. **Results Collection**: Gather test results, coverage data, and metrics
5. **Report Generation**: Create comprehensive reports in requested format

**Type-Specific Strategies:**

### Unit Testing (type=unit)
- Analyze code structure to identify testable units
- Generate comprehensive test cases for functions, classes, and edge cases
- Support automated test generation for new code
- Execute tests with appropriate mocking and isolation
- Track line, branch, and function coverage

### Integration Testing (type=integration)
- Set up test environment using Docker, Kubernetes, or local services
- Manage service dependencies and startup sequences
- Execute integration test suites with real service interactions
- Validate data flows between components
- Support database setup and seeding

### Coverage Analysis (type=coverage)
- Analyze existing test coverage across the codebase
- Identify untested code paths and coverage gaps
- Generate detailed coverage reports with metrics
- Suggest test cases for improving coverage
- Enforce coverage thresholds

### Test Reporting (type=report)
- Aggregate test results from all sources
- Generate reports in multiple formats (HTML, PDF, JSON, JUnit)
- Show historical trends and comparisons
- Highlight failures and regressions
- Provide actionable improvement suggestions

### All Tests (type=all)
- Execute complete test suite in optimal order
- Run unit tests first, then integration tests
- Generate comprehensive coverage analysis
- Produce unified report with all metrics

**Advanced Features:**

1. **Parallel Execution**: Run independent tests concurrently for speed
2. **Watch Mode**: Monitor file changes and re-run affected tests
3. **Pattern Filtering**: Select tests based on file patterns or test names
4. **Auto-Fix**: Attempt to fix simple test failures automatically
5. **Trend Analysis**: Track test metrics over time

**Implementation Requirements:**
- Detect and use appropriate testing framework (pytest, Jest, JUnit, etc.)
- Support multiple programming languages and frameworks
- Integrate with CI/CD pipelines
- Provide clear, actionable feedback
- Optimize for performance with caching and parallelization

<!-- Note: Environment provisioning functionality integrated directly into integration testing flow -->
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
      <!-- Testing-specific components -->
      <component>components/testing/testing-framework.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>testing.framework</value>
      <value>testing.coverage.threshold</value>
      <value>testing.parallel.workers</value>
      <value>testing.integration.environment</value>
      <value>testing.report.format</value>
    </uses_config_values>
  </dependencies>
</command_file>