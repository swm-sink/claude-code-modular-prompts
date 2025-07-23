---
name: /dev-refactor
description: Advanced development refactoring with intelligent code optimization, pattern recognition, and architectural improvements
usage: /dev-refactor [refactor_scope] [optimization_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced development refactoring with intelligent code optimization, pattern recognition, and architectural improvements

**Usage**: `/dev-refactor $TARGET $STRATEGY`

## Key Arguments

- **$TARGET** (required): The file or directory to analyze for refactoring opportunities.
- **$STRATEGY** (optional): The specific refactoring strategy to apply (e.g., 'extract-method', 'simplify-co...

## Examples

```bash
/dev refactor "src/utils/helpers.js"
```
*Automatically identify and suggest refactorings in a specific file.*

```bash
/dev refactor "src/core/main.py" strategy="extract-method"
```
*Focus on extracting long methods from a file.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/context/find-relevant-code.md
 components/planning/create-step-by-step-plan.md
 components/actions/apply-code-changes.md
 components/quality/anti-pattern-detection.md
 components/testing/test-unit.md
 
 You are a senior software engineer specializing in code quality. The user wants to refactor a specific part of the codebase.

 1. **Analyze Code**:
 * Analyze the provided code for "code smells" (e.g., duplication, long methods, high complexity) based on the chosen `strategy`.
 2. **Ensure Test Coverage**:
 * Check for existing tests covering the target code. If tests are insufficient, first generate new tests to lock in the current behavior. Use `/test unit` as a sub-task.
 3. **Generate Refactoring Plan**:
 * Propose a specific, step-by-step refactoring plan.
 4. **Apply Changes Incrementally**:
 * For each step in the plan, provide the code modification.
 5. **Final Verification**:
 * After applying changes, instruct the user to run the full test suite to verify that behavior is preserved.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

