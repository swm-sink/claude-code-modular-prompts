---
name: /debug
description: Performs advanced AI-assisted debugging to diagnose and fix issues
usage: /debug [issue_description] [interactive]
tools: Read, Grep, Edit, Bash
---

# Performs advanced AI-assisted debugging to diagnose and fix issues

**Usage**: `/debug $ISSUE_DESCRIPTION $INTERACTIVE`

## Key Arguments

- **$ISSUE_DESCRIPTION** (required): A detailed description of the bug or issue to be debugged.
- **$INTERACTIVE** (optional): If true, conducts a step-by-step interactive debugging session.

## Examples

```bash
/debug "Users are unable to log in; the login page just refreshes with no error."
```
*Automatically debug an issue with user logins.*

```bash
/debug "Getting 'undefined is not a function' in Cart.js on line 42" interactive=true
```
*Start an interactive debugging session for a specific error.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/context/find-relevant-code.md
 components/analysis/codebase-discovery.md
 components/planning/create-step-by-step-plan.md
 components/interaction/request-user-confirmation.md
 components/actions/apply-code-changes.md
 components/workflow/report-generation.md

You are an expert debugger. The user needs help diagnosing and fixing an issue.

 1. **Gather Context**:
 * Use context and discovery components to understand the relevant code

 2. **Analyze & Hypothesize**:
 * Based on the issue description and relevant code, form a set of likely hypotheses for the root cause.
 * Apply error handling patterns to identify potential failure points
 
 3. **Create Debugging Plan**:
 * Create a step-by-step plan to test each hypothesis. This could involve suggesting `console.log` placements, asking the user to set breakpoints, or analyzing execution flow.

 4. **Interactive Debugging**:
 * If `interactive` is true, guide the user through the plan step-by-step, analyzing the output at each stage.

 5. **Propose Solution**:
 * Once the root cause is confirmed, provide a clear explanation and the exact code changes needed to fix the bug.


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

