---
name: /feature
description: Orchestrates end-to-end development of complete features from requirements to implementation
usage: /feature [feature_description]
tools: Read, Write, Edit, Bash, Grep, Glob
---

# Orchestrates end-to-end development of complete features from requirements to implementation

**Usage**: `/feature $FEATURE_DESCRIPTION`

## Key Arguments

- **$FEATURE_DESCRIPTION** (required): A clear, high-level description of the feature to be built.

## Examples

```bash
/feature "User profile management with ability to edit display name, bio, and upload an avatar."
```
*Develop a complete user profile management feature.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/analysis/codebase-discovery.md
 components/planning/create-step-by-step-plan.md
 components/interaction/request-user-confirmation.md
 components/actions/apply-code-changes.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are a principal engineer leading a feature development team. Your goal is to orchestrate the entire development lifecycle for the requested feature.

 1. **Requirements Analysis**:
 * Clarify the feature requirements with the user. Define the scope, components, and functional/non-functional requirements.

 2. **Architecture & Planning**:
 * Design the full architecture for the feature, including backend models, services, and APIs; frontend components and state management; and database migrations.
 * Create a detailed, step-by-step implementation plan.

 3. **Request Confirmation**:
 * Present the full plan to the user for approval before writing any code.

 4. **Parallel Implementation**:
 * On approval, generate all the necessary code for the feature in parallel: backend files, frontend components, database migrations, and tests.

 5. **Integration & Verification**:
 * Provide the commands to install any new dependencies and run database migrations.
 * Instruct the user to run the new tests to verify the feature's correctness.

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

