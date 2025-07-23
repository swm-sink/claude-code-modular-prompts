---
name: /dev-test
description: Advanced development testing with comprehensive coverage, intelligent test generation, and automated quality validation
usage: /dev-test [test_scope] [coverage_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced development testing with comprehensive coverage, intelligent test generation, and automated quality validation

**Usage**: `/dev-test $PATTERN`

## Key Arguments

- **$PATTERN** (optional): A pattern or filter to run a specific subset of tests.

## Examples

```bash
/dev test
```
*Run the entire test suite.*

```bash
/dev test "user-authentication"
```
*Run only the tests that match the 'user-authentication' pattern.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/testing/test-framework-detection.md
 components/testing/coverage-analysis.md
 components/reporting/generate-structured-report.md
 components/quality/test-quality-metrics.md
 
 You are a test runner. The user wants to execute a test suite.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the test command and coverage options for the project's detected test framework.
 2. **Construct Test Command**: Build the full test command, incorporating the user's `pattern` if provided.
 3. **Execute Tests**: Run the test command.
 4. **Generate Report**: After execution, parse the output and generate a comprehensive report.
 * Include pass/fail counts, duration, and code coverage percentage.
 * For failed tests, provide the error details and suggestions for fixes.

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

