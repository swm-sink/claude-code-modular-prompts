---
name: /session-create
description: Intelligent session creation with automated context loading, goal setting, and productivity optimization
usage: /session-create [session_name] [goal_description]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent session creation with automated context loading, goal setting, and productivity optimization

**Usage**: `/session-create $SESSION_NAME $GOAL_DESCRIPTION $TEMPLATE`

## Key Arguments

- **$SESSION_NAME** (required): The name for the new session
- **$GOAL_DESCRIPTION** (required): A clear description of the session's goal
- **$TEMPLATE** (optional): A template to use for the new session (e.g., bug_fix, feature_dev, research)

## Examples

```bash
/session create "User Profile Feature" "Implement the user profile page with editable fields"
```
*Create a new session to implement a feature*

```bash
/session create --template "bug_fix" "Fix the off-by-one error in the pagination logic"
```
*Create a new session from a bug fix template*

## Core Logic

You are an advanced session management specialist. The user wants to create a new, productive session.

**Session Creation Process:**
1. **Define Goal**: Clearly define the primary goal and success criteria for the session.
2. **Load Context**: Automatically load relevant context from previous sessions, documentation, or codebase analysis.
3. **Set Up Workspace**: Prepare the workspace by opening relevant files and setting up necessary tools.
4. **Generate Plan**: Generate a high-level plan or checklist to guide the session's workflow.
5. **Optimize for Productivity**: Provide tips and suggestions to optimize productivity for the session's goal.

**Implementation Strategy:**
- Prompt the user for a clear, concise goal for the session.
- Analyze the goal to identify and automatically load relevant context, such as related code files, documentation, or previous session summaries.
- Prepare the user's workspace by opening the identified files and suggesting relevant commands.
- Generate a step-by-step plan or a to-do list to provide a clear path forward for the user.
- Offer productivity tips tailored to the session's goal, such as suggesting a specific testing strategy for a bug fix or a component-based approach for a new feature.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

