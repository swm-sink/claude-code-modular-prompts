---
name: /error-trace
description: Advanced error tracing with stack trace analysis, distributed tracing, and root cause investigation
usage: /error-trace [trace_id] [trace_depth]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced error tracing with stack trace analysis, distributed tracing, and root cause investigation

**Usage**: `/error-trace $ERROR_CONTEXT`

## Key Arguments

- **$ERROR_CONTEXT** (required): The full error message, stack trace, or path to a log file containing the error ...

## Examples

```bash
/error trace "TypeError: Cannot read properties of null (reading 'id') at /app/src/services/userService.js:25:12"
```
*Trace the propagation path of a specific error message.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/analysis/codebase-discovery.md
 components/context/find-relevant-code.md
 components/reporting/generate-structured-report.md
 components/visualization/flow-diagrams.md
 components/analysis/root-cause-analysis.md
 
 You are a system diagnostician. The user wants to trace an error's propagation path through the system.

 1. **Analyze Context**:
 * Parse the provided `error_context` to identify the origin point of the error (file, function, line number).
 2. **Trace Backwards**:
 * Starting from the error's origin, trace the execution flow backwards.
 * Identify the sequence of function calls that led to the error state.
 * Examine how data (especially the data causing the error) was passed between functions.
 3. **Build Flow Map**:
 * Construct a map or diagram of the error flow, showing how the error propagated from its root cause to the point where it was reported.
 4. **Generate Trace Report**:
 * Generate a report that includes:
 * A visualization of the error flow (e.g., as a Mermaid sequence diagram).
 * An identification of the root cause.
 * Recommendations for where to add more robust error handling to stop the propagation.

## Essential Component Logic

### Input Validation

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

