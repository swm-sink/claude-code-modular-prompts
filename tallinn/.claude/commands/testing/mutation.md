---
name: /mutation
description: Performs mutation testing to assess the effectiveness of existing test suites
usage: /mutation [target_file] [auto_fix]
tools: Read, Write, Bash, Edit
---

# Performs mutation testing to assess the effectiveness of existing test suites

**Usage**: `/mutation $TARGET $AUTO_FIX`

## Key Arguments

- **$TARGET** (required): The file containing the code to be mutation-tested.
- **$AUTO_FIX** (optional): If true, automatically generates new tests to kill surviving mutants.

## Examples

```bash
/test mutation "src/utils/stringUtils.js"
```
*Run mutation testing on a specific utility file.*

```bash
/test mutation "src/core/authService.js" auto_fix=true
```
*Run mutation testing and automatically generate tests for any surviving mutants.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are a quality assurance engineer specializing in mutation testing. The user wants to assess the quality of their tests for a specific file.

 1. **Analyze Code and Tests**:
 * Read the `target` file and its corresponding test file.
 2. **Generate Mutants**:
 * Create a set of "mutants" by introducing small, deliberate bugs into the source code (e.g., changing `<` to `<=`, negating a boolean, changing a `+` to a `-`).
 3. **Run Tests Against Mutants**:
 * For each mutant, run the existing test suite against it.
 * If the tests fail, the mutant is "killed."
 * If the tests pass, the mutant "survived," indicating a gap in the test suite.
 4. **Generate Report**:
 * Calculate the mutation score (percentage of mutants killed).
 * Provide a report listing all surviving mutants and the specific code change that was not caught by the tests.
 * 

 5. **Fix Survivors (Optional)**:
 * If `auto_fix` is true, for each surviving mutant, generate a new test case that specifically "kills" it and add it to the test suite.
 *

## Essential Component Logic

### Input Validation

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

