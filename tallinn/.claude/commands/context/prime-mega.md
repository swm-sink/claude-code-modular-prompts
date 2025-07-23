---
name: /prime-mega
description: Performs a comprehensive, deep codebase analysis using specialized agents
tools: Bash, Read, Grep, Glob, Task
---

# Performs a comprehensive, deep codebase analysis using specialized agents

## Examples

```bash
/context prime-mega
```
*Run a deep, multi-agent analysis on the current project.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/interaction/request-user-confirmation.md
 components/reporting/generate-structured-report.md
 components/orchestration/agent-orchestration.md
 components/analysis/codebase-discovery.md
 components/planning/create-step-by-step-plan.md

 You are a master project auditor. Your task is to perform a deep, multi-faceted analysis of the entire codebase by orchestrating a team of specialized analysis agents (commands).

 1. **Assess & Plan**:
 * First, get a sense of the project's scale (e.g., small, medium, large, enterprise) by analyzing the file count and directory structure.
 * Based on the scale, propose a multi-phase analysis plan listing the specialized commands you will run (e.g., for a large project, you might propose running `/analyze code`, `/analyze dependencies`, `/security scan`, and `/analyze performance`).

 2. **Request Confirmation**:
 * Present this plan to the user for approval before proceeding.

 3. **Execute Analysis Chain**:
 * Upon confirmation, execute the planned sequence of analysis commands, capturing the output from each.

 4. **Synthesize Master Report**:
 * Aggregate all findings from the individual command reports.
 * Perform a cross-analysis to identify reinforcing or conflicting findings.
 * Prioritize all identified issues by severity and impact.
 * Generate a final, comprehensive master analysis report with an executive summary and an actionable improvement roadmap.

## Essential Component Logic

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

