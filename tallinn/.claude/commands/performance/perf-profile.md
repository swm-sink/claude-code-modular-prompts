---
name: /perf-profile
description: Application profiling with detailed performance analysis and bottleneck identification
usage: /perf-profile [profile_type] [depth_level]
tools: Read, Write, Edit, Bash, Grep
---

# Application profiling with detailed performance analysis and bottleneck identification

**Usage**: `/perf-profile $TARGET $TYPE`

## Key Arguments

- **$TARGET** (required): The specific file, function, or class to profile.
- **$TYPE** (optional): The type of profiling to perform (e.g., 'cpu', 'memory').

## Examples

```bash
/perf profile "src/utils/dataProcessor.js:processLargeFile"
```
*Run a CPU profile on a specific data processing function.*

```bash
/perf profile "src/analytics/engine.py" type="memory"
```
*Run a memory profile on an analytics engine.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/reporting/generate-structured-report.md
 components/performance/profiling-tools.md
 components/analysis/bottleneck-detection.md
 components/visualization/flame-graphs.md
 components/analysis/memory-leak-detection.md
 
 You are a performance engineer. The user wants to profile a specific part of the code.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the project's configured profiling tool.
 2. **Generate Profiling Script**:
 * Create a script that initializes the appropriate profiler (CPU or memory).
 * The script should attach the profiler to the `target` code and execute it.
 3. **Execute and Collect Data**:
 * Present the profiling script to the user and, on confirmation, execute it to collect performance samples.
 4. **Analyze and Report**:
 * Analyze the collected profiling data to identify performance hotspots and bottlenecks.
 * Generate a report that includes:
 * A summary of the most time-consuming function calls (for CPU profiling).
 * An analysis of memory allocation and potential leaks (for memory profiling).
 * A flame graph visualization for intuitive analysis.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

