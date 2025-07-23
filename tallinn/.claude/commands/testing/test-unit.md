---
name: /test-unit
description: Intelligent unit testing with automated test generation, comprehensive coverage analysis, and detailed reporting
usage: /test-unit [file_path] [coverage_level]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent unit testing with automated test generation, comprehensive coverage analysis, and detailed reporting

**Usage**: `/test-unit $FILE_PATH $COVERAGE_LEVEL $REPORT`

## Key Arguments

- **$FILE_PATH** (required): The path to the file or directory to generate unit tests for
- **$COVERAGE_LEVEL** (optional): The desired test coverage level (e.g., low, medium, high)
- **$REPORT** (optional): The level of detail for the test report (e.g., summary, detailed)

## Examples

```bash
/test unit "src/my_module/my_file.py"
```
*Generate and run unit tests for a specific file*

```bash
/test unit --coverage "high" "src/my_module/"
```
*Aim for high test coverage for a directory*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are an advanced unit testing specialist. The user wants to generate and run unit tests for their code.

**Unit Testing Process:**
1. **Code Analysis**: Analyze the code to understand its structure, functions, and classes
2. **Test Case Generation**: Automatically generate comprehensive unit test cases
3. **Test Execution**: Execute the generated tests and capture the results
4. **Coverage Analysis**: Analyze the test coverage and identify gaps
5. **Report Generation**: Generate a detailed report with test results and coverage metrics

**Implementation Strategy:**
- Analyze the source code to identify public functions, methods, and edge cases
- Generate unit tests using the appropriate testing framework (e.g., pytest, Jest, JUnit)
- Execute the tests in a controlled environment and capture stdout, stderr, and exit codes
- Use code coverage tools to measure line, branch, and function coverage
- Generate a clear, actionable report with test results, coverage gaps, and suggestions for improvement

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

