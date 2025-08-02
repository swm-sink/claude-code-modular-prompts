---
name: /test
description: Unified intelligent testing framework with automated test generation, comprehensive coverage analysis, environment management, and multi-format reporting (v1.0)
version: "1.0"
usage: '/test [type] [target] [--coverage high|medium|low] [--parallel] [--watch] [--generate]'
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
- LS
- Glob
dependencies:
- /test-unit
- /test-integration-project
- /test-e2e
- /quick-test
category: quality
validation:
  pre-execution: Validate test framework configuration and dependencies
  during-execution: Monitor test execution with progress tracking
  post-execution: Generate comprehensive reports with trend analysis
progressive-disclosure:
  layer-integration: Layer 2 unified testing hub with smart defaults
  layer-1-experience: Users typically start with /quick-test
  layer-2-experience: Full-featured testing with customizable options
  layer-3-experience: Advanced parallel execution and custom reporting
safety-features:
  input-validation: Test type and target validation
  error-recovery: Automatic retry and failure analysis
  security-checks: Secure test environment isolation
performance:
  optimization: Parallel test execution and smart ordering
  caching: Test result and coverage caching
  resource-limits: Configurable memory and CPU limits
test-features:
  automated-generation: Generate tests for new code
  coverage-analysis: Line, branch, and function coverage
  environment-management: Docker and service orchestration
  multi-format-reporting: HTML, PDF, JSON, JUnit formats
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/commands/quality/test.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>test</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>2</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="file-reader" role="test_discovery"/>
      <component ref="parameter-parser" role="test_configuration"/>
      <component ref="test-runner" role="test_execution"/>
      <component ref="api-caller" role="test_framework_integration"/>
      <component ref="progress-indicator" role="test_progress_tracking"/>
      <component ref="task-summary" role="test_report_generation"/>
    </required_components>
    <optional_components>
      <component ref="performance-monitoring" benefit="test_performance_analysis"/>
      <component ref="git-operations" benefit="version_control_integration"/>
      <component ref="error-handler" benefit="test_failure_recovery"/>
      <component ref="output-formatter" benefit="multi_format_reporting"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="test-unit" context="unit_testing"/>
      <command ref="test-integration-project" context="integration_testing"/>
      <command ref="test-e2e" context="end_to_end_testing"/>
      <command ref="quick-test" context="rapid_testing"/>
      <command ref="analyze-code" context="code_quality_integration"/>
    </invokable_commands>
    <orchestration_patterns>unified_testing|parallel_execution|coverage_analysis|automated_generation</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Unified intelligent testing framework with automated test generation, comprehensive coverage analysis, and multi-format reporting</task_description>
    <implementation_strategy>test_type_selection|target_validation|test_execution|coverage_analysis|report_generation|environment_management</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>testing_framework_hub</primary_discovery_path>
    <alternative_paths>
      <path>automated_test_generation</path>
      <path>coverage_analysis</path>
      <path>test_environment_management</path>
      <path>test_reporting_and_analytics</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="command" ref="test-unit" relation="unit_testing_foundation"/>
      <file type="command" ref="test-integration-project" relation="integration_testing"/>
      <file type="command" ref="test-e2e" relation="end_to_end_testing"/>
      <file type="context" ref=".claude/context/testing-frameworks.md" relation="testing_methodology"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="analyze-code" relation="quality_integration"/>
      <file type="command" ref="quality" relation="quality_assurance_workflow"/>
      <file type="context" ref=".claude/context/test-reports.md" relation="reporting_documentation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="quick-test" similarity="0.80"/>
      <file type="command" ref="test-integration" similarity="0.75"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>comprehensive_testing_requirements</scenario>
      <scenario>automated_test_generation</scenario>
      <scenario>coverage_analysis</scenario>
      <scenario>test_environment_management</scenario>
      <scenario>unified_testing_workflow</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_single_test_execution</scenario>
      <scenario>basic_syntax_validation</scenario>
      <scenario>non_testing_code_analysis</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>test testing framework unit integration coverage automated generation reporting</keywords>
    <semantic_tags>testing_framework automated_testing coverage_analysis test_generation unified_testing</semantic_tags>
    <functionality_vectors>[1.0, 0.9, 0.9, 0.8, 0.8]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <critical_context>
      <context_file ref=".claude/context/testing-frameworks.md" importance="critical"/>
      <context_file ref=".claude/context/test-automation-patterns.md" importance="critical"/>
      <context_file ref=".claude/context/coverage-analysis-guide.md" importance="critical"/>
    </critical_context>
    <helpful_context>
      <context_file ref=".claude/context/test-environment-setup.md" importance="high"/>
      <context_file ref=".claude/context/test-reporting-standards.md" importance="high"/>
      <context_file ref=".claude/context/performance-testing-patterns.md" importance="medium"/>
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>testing_and_validation</workflow_stage>
    <integration_patterns>
      <pattern>unified_testing_orchestration</pattern>
      <pattern>automated_test_generation</pattern>
      <pattern>comprehensive_coverage_analysis</pattern>
      <pattern>multi_format_reporting</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>unified_testing_framework</concept_introduction>
    <skill_progression>intermediate_to_advanced</skill_progression>
    <mastery_indicators>
      <indicator>effective_test_type_selection</indicator>
      <indicator>successful_automated_test_generation</indicator>
      <indicator>comprehensive_coverage_analysis</indicator>
      <indicator>professional_test_reporting</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /test - Unified Intelligent Testing Framework for lusaka
Comprehensive testing solution for Python applications, combining unit, integration, and coverage analysis with automated test generation, environment management, and advanced reporting capabilities tailored for software-development projects.
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
      
You are an advanced unified testing specialist for lusaka with expertise in Python testing frameworks and software-development best practices. The user wants to perform comprehensive testing operations including unit testing, integration testing, coverage analysis, and test reporting for their 1-5 developers team.

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
- Detect and use appropriate testing framework (pytest or alternatives)
- Support Python languages and frameworks
- Integrate with GitHub Actions pipelines
- Provide clear, actionable feedback for 1-5 developers team
- Optimize for performance with caching and parallelization on AWS

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