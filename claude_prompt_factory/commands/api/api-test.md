# /api test - API Endpoint Testing Command

**Purpose**: Perform comprehensive testing of API endpoints, including functional validation, performance measurement, and detailed reporting.

## Usage
```bash
/api test [endpoint] [--method=GET] [--payload=data.json]
```

## Workflow

The `/api test` command follows a systematic process to test API endpoints.

```xml
<api_test_workflow>
  <step name="Setup & Validate Request">
    <description>Parse the endpoint URL, HTTP method, and any provided payload or authentication credentials. Prepare and validate the request before sending.</description>
  </step>
  
  <step name="Execute Request & Monitor">
    <description>Send the HTTP request to the specified endpoint, measuring response times, latency, and monitoring status codes and error rates.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Use curl or a similar tool to send the HTTP request.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Response & Assess Performance">
    <description>Analyze the response to validate its schema, structure, and data. Also, assess the performance of the endpoint by measuring response time and checking for any timeout issues.</description>
  </step>
  
  <step name="Generate Report">
    <description>Generate a detailed test report that includes a summary of the test, pass/fail counts, performance metrics, and any error analysis with recommendations.</description>
    <output>A comprehensive API test report.</output>
  </step>
</api_test_workflow>
```

## Quality Standards
- **Status Code Validation**: Checks for correct HTTP status codes (2xx, 4xx, 5xx).
- **Response Time Thresholds**: Measures response times against defined thresholds.
- **Data Integrity Verification**: Validates the integrity of the data in the response.
- **Security Header Validation**: Checks for the presence of required security headers.
- **Rate Limiting Compliance**: Tests for compliance with rate limiting rules.