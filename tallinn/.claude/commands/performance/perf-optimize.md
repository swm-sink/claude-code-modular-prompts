---
name: /perf-optimize
description: Intelligent performance optimization with automated tuning and validation
usage: /perf-optimize [optimization_target] [scope]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent performance optimization with automated tuning and validation

**Usage**: `/perf-optimize $TARGET $FOCUS`

## Key Arguments

- **$TARGET** (required): The specific file, function, or class to optimize.
- **$FOCUS** (optional): The optimization focus (e.g., 'cpu', 'memory', 'io').

## Examples

```bash
/perf optimize "src/utils/dataProcessor.js:processLargeFile"
```
*Analyze and suggest CPU optimizations for a specific function.*

```bash
/perf optimize "src/analytics/engine.py" focus="memory"
```
*Focus on memory optimizations for a data-intensive module.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/planning/create-step-by-step-plan.md
 components/interaction/request-user-confirmation.md
 components/actions/apply-code-changes.md
 components/performance/optimization-strategies.md
 components/performance/profiling-analysis.md
 
 You are a performance optimization expert. The user wants to improve the performance of a specific part of the codebase.

 1. **Profile and Analyze**:
 * First, use the logic of `/perf profile` and `/perf benchmark` to analyze the `target` code and identify the most significant performance bottlenecks related to the specified `focus`.
 2. **Generate Optimization Plan**:
 * Based on the analysis, create a step-by-step plan of specific, actionable optimizations. Examples include:
 * **CPU**: Caching/memoization, algorithmic improvements, avoiding re-computation.
 * **Memory**: Using more efficient data structures, reducing object allocations, streaming large datasets.
 * **I/O**: Batching operations, using asynchronous I/O, compressing data.
 3. **Propose Changes**:
 * Generate the code modifications for the plan and present them to the user.
 4. **Apply and Verify**:
 * On confirmation, apply the changes.
 * Instruct the user to re-run the benchmark (`/perf benchmark`) to verify the improvement.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

