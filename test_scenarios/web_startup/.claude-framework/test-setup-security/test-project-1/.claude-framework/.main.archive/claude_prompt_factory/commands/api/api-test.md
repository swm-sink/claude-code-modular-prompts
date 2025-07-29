---
description: Intelligent API testing with automated test case generation, comprehensive validation, and detailed reporting
argument-hint: "[api_endpoint] [http_method]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /api test - Intelligent API Testing

Advanced API testing system with automated test case generation from API specifications, comprehensive validation of responses, and detailed, actionable reporting.

## Usage
```bash
/api test "/users/{id}" --method "GET"       # Test a specific API endpoint
/api test --spec "openapi.json" --all        # Test all endpoints defined in an OpenAPI specification
/api test --performance "100" "/orders"      # Run a performance test with 100 virtual users
```

<command_file>
  <metadata>
    <n>/api test</n>
    <purpose>Intelligent API testing with automated test case generation, comprehensive validation, and detailed reporting</purpose>
    <usage>
      <![CDATA[
      /api test "[api_endpoint]" --method "[http_method]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="api_endpoint" type="string" required="true">
      <description>The API endpoint to test</description>
    </argument>
    <argument name="http_method" type="string" required="false" default="GET">
      <description>The HTTP method to use for the test (e.g., GET, POST, PUT, DELETE)</description>
    </argument>
    <argument name="spec" type="string" required="false">
      <description>The path to the API specification file (e.g., OpenAPI, Postman)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Test a specific API endpoint</description>
      <usage>/api test "/users/123" --method "GET"</usage>
    </example>
    <example>
      <description>Test all endpoints defined in an OpenAPI specification</description>
      <usage>/api test --spec "docs/openapi.json" --all</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/testing/test-integration.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/testing/test-e2e.md</include>
      <include>components/quality/quality-metrics.md</include>
      <include>components/actions/parallel-execution.md</include>

You are an advanced API testing specialist. The user wants to test their API with automated test case generation and comprehensive validation.

**API Testing Process:**
1. **Analyze Specification**: Analyze the API specification (e.g., OpenAPI, Swagger) to understand endpoints, methods, and schemas
2. **Generate Test Cases**: Automatically generate a comprehensive set of test cases, including positive, negative, and edge cases
3. **Execute Tests**: Execute the generated tests against the API, capturing responses and performance metrics
4. **Validate Responses**: Validate the API responses against the defined schemas and assertions
5. **Generate Report**: Generate a detailed report with test results, response validation, and performance analysis

**Implementation Strategy:**
- Parse API specifications to automatically discover endpoints, methods, parameters, and response schemas
- Generate a wide range of test cases, including tests for authentication, authorization, data validation, and error handling
- Execute tests using a powerful HTTP client, capturing detailed information about each request and response
- Perform deep validation of API responses, comparing them against the schemas defined in the specification
- Generate a comprehensive report with clear pass/fail status, detailed error messages, and performance benchmarks
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/testing/test-integration.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>api.testing.base_url</value>
      <value>api.testing.auth_token</value>
    </uses_config_values>
  </dependencies>
</command_file>