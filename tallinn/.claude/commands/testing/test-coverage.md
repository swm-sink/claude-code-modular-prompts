---
name: /test-coverage
description: Advanced test coverage analysis with intelligent gap detection, quality metrics, and comprehensive coverage optimization
usage: /test-coverage [coverage_scope] [analysis_depth]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced test coverage analysis with intelligent gap detection, quality metrics, and comprehensive coverage optimization

**Usage**: `/test-coverage $PATH`

## Key Arguments

- **$PATH** (optional): The source directory to analyze for test coverage.

## Examples

```bash
/test-coverage
```
*Calculate test coverage for the entire codebase.*

```bash
/test-coverage "./src/api"
```
*Calculate test coverage for a specific subdirectory.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

 You are a quality assurance analyst. The user wants to analyze the project's test coverage.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured test command and coverage options.
 2. **Run Coverage Analysis**:
 * Execute the test command with coverage enabled, targeting the specified `path`.
 3. **Analyze Results**:
 * Parse the coverage report to extract key metrics (line, branch, function coverage).
 * Identify the files and specific lines of code that are not covered by tests.
 4. **Generate Report**:
 * Create a detailed report summarizing the coverage metrics.
 * Highlight the top 5 least-covered files that need attention.
 * Provide actionable recommendations for improving test coverage.
 *

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...



*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

