---
name: /api-design
description: Comprehensive API design with OpenAPI specification, best practices, and validation
usage: /api-design [api_type] [design_approach]
tools: Read, Write, Edit, Bash, Grep
---

# Comprehensive API design with OpenAPI specification, best practices, and validation

**Usage**: `/api-design $DESCRIPTION $TYPE`

## Key Arguments

- **$DESCRIPTION** (required): A natural language description of the API to be designed.
- **$TYPE** (optional): The type of API to design ('rest' or 'graphql').

## Examples

```bash
/api design "a user service with create, read, update, delete endpoints"
```
*Design a REST API for a simple user management system.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/planning/create-step-by-step-plan.md
 components/reporting/generate-structured-report.md
 components/security/owasp-compliance.md
 components/validation/xml-structure.md

You are an expert API architect. The user wants you to design an API based on their description.

 1. **Analyze Requirements**: Analyze the user's description to understand the business needs, data models, and core functionality.
 2. **Design Endpoints & Schema**: Design the RESTful resource endpoints or GraphQL schema, including operations, parameters, and models.
 3. **Generate API Specification**: Generate a complete API specification in OpenAPI 3.0 (for REST) or GraphQL schema format. Include data models, authentication patterns, and error handling.

 Your output should be the raw specification file content.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


### Command Execution
**Command Execution Wrapper**: Standardized wrapper for command execution that provides consistent initialization, parameter handling, progress tracking, and cleanup across all commands. 1. **Initialization Phase**: - Validate envi...
**Complete**: Apply command execution wrapper completion


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

