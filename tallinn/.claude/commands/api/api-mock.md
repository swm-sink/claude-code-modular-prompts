---
name: /api-mock
description: API mocking and simulation with realistic data generation and behavior simulation
usage: /api-mock [mock_type] [data_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# API mocking and simulation with realistic data generation and behavior simulation

**Usage**: `/api-mock $SPEC_FILE`

## Key Arguments

- **$SPEC_FILE** (required): Path to the OpenAPI specification file (e.g., `openapi.json`).

## Examples

```bash
/api mock "docs/api/openapi.json"
```
*Create a mock server from a local OpenAPI file.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/actions/apply-code-changes.md
 components/testing/test-integration.md
 components/reporting/generate-structured-report.md

You are a mock server generator. The user wants to create a mock API server from a specification file.

 1. **Parse Specification**: Parse the provided OpenAPI specification to understand the endpoints, schemas, and responses.
 2. **Generate Mock Data**: Generate realistic mock data for the API's responses that matches the defined schemas.
 3. **Set Up & Run Server**: Provide the code for a simple mock server (e.g., using Express.js or FastAPI) that serves the generated mock data. The server should support configurable response delays and error rates.

 Your output should be the code for the mock server.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


### Command Execution
**Command Execution Wrapper**: Standardized wrapper for command execution that provides consistent initialization, parameter handling, progress tracking, and cleanup across all commands. 1. **Initialization Phase**: - Validate envi...
**Complete**: Apply command execution wrapper completion

### Error Handling

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

