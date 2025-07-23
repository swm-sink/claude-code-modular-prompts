---
name: /error-handle
description: Comprehensive error handling patterns with recovery strategies and resilience patterns
usage: /error-handle [error_pattern] [recovery_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Comprehensive error handling patterns with recovery strategies and resilience patterns

**Usage**: `/error-handle $FILE_PATH`

## Key Arguments

- **$FILE_PATH** (required): The path to the file where error handling should be added.

## Examples

```bash
/error handle "src/services/paymentService.js"
```
*Add robust error handling to a specific service file.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/analysis/codebase-discovery.md
 components/planning/create-step-by-step-plan.md
 components/interaction/request-user-confirmation.md
 components/actions/apply-code-changes.md
 components/error/circuit-breaker.md
 
 You are a software reliability engineer. The user wants to add robust error handling to a file.

 1. **Analyze Code**:
 * Read the contents of the specified `file_path`.
 * Identify critical code paths that lack sufficient error handling (e.g., I/O operations, network requests, parsing, complex logic).

 2. **Generate Plan**:
 * Propose a plan to add error handling. This should include:
 * Wrapping critical sections in `try-catch` blocks.
 * Implementing specific catch blocks for different error types.
 * Adding logging for errors.
 * Defining graceful fallback behavior.
 3. **Propose Changes**:
 * Generate the code modifications needed to implement the plan.
 * Present the changes to the user for confirmation.

 4. **Apply Changes**:
 * On confirmation, apply the changes to the file.


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

