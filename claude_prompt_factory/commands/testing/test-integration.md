---
description: Intelligent integration testing with automated environment setup, service dependency management, and comprehensive validation
argument-hint: "[test_suite] [environment_config]"
allowed-tools: Read, Write, Edit, Bash, Grep
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
You are an advanced integration testing specialist. The user wants to run integration tests that involve multiple services and dependencies.

**Integration Testing Process:**
1. **Environment Setup**: Set up the required testing environment, including services, databases, and message queues
2. **Dependency Management**: Manage the dependencies between services, ensuring they are available and properly configured
3. **Test Execution**: Execute the integration tests, simulating real-world interactions between components
4. **Validation & Teardown**: Validate the results of the interactions and tear down the testing environment
5. **Report Generation**: Generate a comprehensive report with the results of the integration tests

**Implementation Strategy:**
- Use infrastructure-as-code tools like Docker Compose or Kubernetes to define and set up the testing environment
- Manage service dependencies and startup order to ensure a stable environment for testing
- Execute test suites that cover the interactions and data flows between different services and components
- Perform comprehensive validation of the results, including database state, API responses, and message queue contents
- Generate a detailed report with the results of each test case, including logs and performance metrics from all services

<include component="components/testing/test-integration.md" />
<include component="components/deployment/auto-provision.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/testing/test-integration.md</component>
      <component>components/deployment/auto-provision.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>testing.integration.environment</value>
      <value>testing.integration.db_seed_script</value>
    </uses_config_values>
  </dependencies>
</command_file>