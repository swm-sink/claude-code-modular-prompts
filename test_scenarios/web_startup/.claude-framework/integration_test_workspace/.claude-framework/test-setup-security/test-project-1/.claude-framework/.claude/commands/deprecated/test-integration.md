---
name: /test-integration
description: "Intelligent integration testing with automated environment setup, service dependency management, and comprehensive validation"
argument-hint: "[test_suite] [environment_config]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecated_date: 2025-07-25
removal_date: 2025-08-25
migration_path: /test
---
# DEPRECATED: This command has been consolidated

This command has been deprecated and will be removed on 2025-08-25.

**Migration Path**: Use `/test` with the following options:
- For integration testing: `/test integration [test_suite] --env [config]`
- With database setup: `/test integration --setup-db`
- For all integration tests: `/test integration --all`

**Reason**: Consolidating testing commands to reduce complexity and improve user experience.

---

# /test integration - Intelligent Integration Testing
Advanced integration testing system with automated environment setup, service dependency management, and comprehensive validation of interactions between components.
## Usage
```bash
/test integration "user_service_tests" --env "docker-compose.yml" # Run integration tests for a specific service
/test integration --all --setup-db "true" # Run all integration tests and set up the database
/test integration --report "detailed" # Generate a detailed integration test report
```
<command_file>
  <metadata>
    <n>/test integration</n>
    <purpose>Intelligent integration testing with automated environment setup, service dependency management, and comprehensive validation</purpose>
    <usage>
      <![CDATA[
      /test integration "[test_suite]" --env "[environment_config]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="test_suite" type="string" required="true">
      <description>The name of the integration test suite to run</description>
    </argument>
    <argument name="environment_config" type="string" required="true">
      <description>The path to the environment configuration file (e.g., docker-compose.yml)</description>
    </argument>
    <argument name="setup_db" type="boolean" required="false" default="false">
      <description>Whether to set up and seed the database before running the tests</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Run integration tests for a specific service using a Docker Compose environment</description>
      <usage>/test integration "user_service_tests" --env "environments/docker-compose.test.yml"</usage>
    </example>
    <example>
      <description>Run all integration tests and set up the database</description>
      <usage>/test integration --all --setup-db "true"</usage>
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
You are an advanced integration testing specialist. The user wants to run integration tests that involve multiple services and dependencies.
**Integration Testing Process:**
1. **Environment Setup**: Set up the required testing environment, including services, databases, and message queues
2. **Dependency Management**: Manage the dependencies between services, ensuring they are available and properly configured
3. **Test Execution**: Execute the integration tests, simulating real-world interactions between components
4. **Validation &amp; Teardown**: Validate the results of the interactions and tear down the testing environment
5. **Report Generation**: Generate a comprehensive report with the results of the integration tests
**Implementation Strategy:**
- Use infrastructure-as-code tools like Docker Compose or Kubernetes to define and set up the testing environment
- Manage service dependencies and startup order to ensure a stable environment for testing
- Execute test suites that cover the interactions and data flows between different services and components
- Perform comprehensive validation of the results, including database state, API responses, and message queue contents
- Generate a detailed report with the results of each test case, including logs and performance metrics from all services
<include component="components/testing/testing-framework.md" />
<include component="components/deployment/auto-provision.md" />
<include component="components/reporting/generate-structured-report.md" />
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
      <component>components/testing/testing-framework.md</component>
      <component>components/deployment/auto-provision.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>testing.integration.environment</value>
      <value>testing.integration.db_seed_script</value>
    </uses_config_values>
  </dependencies>
</command_file>