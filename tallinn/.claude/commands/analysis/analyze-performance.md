---
name: /analyze-performance
description: Performance analysis with bottleneck detection, optimization recommendations, and benchmarking
usage: /analyze-performance [performance_scope] [analysis_depth]
tools: Read, Write, Edit, Bash, Grep
---

# Performance analysis with bottleneck detection, optimization recommendations, and benchmarking

**Usage**: `/analyze-performance $TARGET_PATH $FOCUS`

## Key Arguments

- **$TARGET_PATH** (optional): The file or directory to analyze. Defaults to the current directory.
- **$FOCUS** (optional): The specific area to focus on (e.g., 'time', 'memory', 'io').

## Examples

```bash
/analyze performance
```
*Run a time-focused performance analysis on the entire project.*

```bash
/analyze performance "src/user_service/" focus="memory"
```
*Analyze the memory usage of a specific service.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

 You are a senior performance engineer. The user wants to analyze their application for performance bottlenecks and get optimization recommendations.

 Once the target code is identified, perform a deep performance analysis covering these areas:
 - **Bottleneck Detection**: Algorithmic complexity, hot paths, memory leaks, and I/O blocking.
 - **Performance Patterns**: N+1 queries, unnecessary nested loops, and synchronous operations.
 - **Metrics Analysis**: Response times, throughput, and resource utilization.

 Based on your analysis, provide a set of actionable optimization recommendations.

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

