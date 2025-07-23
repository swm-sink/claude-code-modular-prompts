---
name: /api-test
description: Intelligent API testing with automated test case generation, comprehensive validation, and detailed reporting
usage: /api-test [api_endpoint] [http_method]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent API testing with automated test case generation, comprehensive validation, and detailed reporting

**Usage**: `/api-test $API_ENDPOINT $HTTP_METHOD $SPEC`

## Key Arguments

- **$API_ENDPOINT** (required): The API endpoint to test
- **$HTTP_METHOD** (optional): The HTTP method to use for the test (e.g., GET, POST, PUT, DELETE)
- **$SPEC** (optional): The path to the API specification file (e.g., OpenAPI, Postman)

## Examples

```bash
/api test "/users/123" --method "GET"
```
*Test a specific API endpoint*

```bash
/api test --spec "docs/openapi.json" --all
```
*Test all endpoints defined in an OpenAPI specification*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/testing/test-integration.md
 components/reporting/generate-structured-report.md
 components/testing/test-e2e.md
 components/quality/quality-metrics.md
 components/actions/parallel-execution.md

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

## Essential Component Logic

### Input Validation

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

