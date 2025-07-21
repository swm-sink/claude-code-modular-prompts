---
description: Comprehensive API testing with automated validation, performance testing, and security checks
argument-hint: "[test_type] [test_scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /api test - API Testing Framework

Advanced API testing system with automated validation, performance benchmarking, and comprehensive security testing.

## Usage
```bash
/api test functional                         # Functional API testing
/api test performance                        # Performance and load testing
/api test security                           # Security vulnerability testing
/api test --contract                         # Contract testing validation
```

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `endpoint` | string | true | The full URL of the API endpoint to test. |
| `method` | string | false | The HTTP method to use (GET, POST, PUT, DELETE, etc.). Default: GET. |

## Examples

```bash
/api test "https://api.example.com/users/123"
/api test "https://api.example.com/users" method="POST"
```

## Claude Prompt

You are an API testing tool. The user wants to test an API endpoint.

1.  **Prepare Request**: Prepare the HTTP request using the endpoint and method provided.
2.  **Execute Request**: Use `curl` to send the request. Monitor the response time, status code, and any errors.
3.  **Analyze Response**: Validate the response schema and data integrity.
4.  **Generate Report**: Generate a detailed test report.

<include component="components/reporting/generate-structured-report.md" />

## Dependencies

-   `components/reporting/generate-structured-report.md`
-   `deployment.environments.environment#production.url`