---
name: /session-load
description: Intelligent session restoration with context rebuilding, state validation, and continuity management
usage: /session-load [session_name] [load_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent session restoration with context rebuilding, state validation, and continuity management

**Usage**: `/session-load $SESSION_NAME $LOAD_STRATEGY`

## Key Arguments

- **$SESSION_NAME** (required): The name of the session to load
- **$LOAD_STRATEGY** (optional): The strategy for loading the session (e.g., resume, review, analyze)

## Examples

```bash
/session load "feature-x-development"
```
*Load a saved session to resume work*

```bash
/session load "bug-fix-session" --strategy "review"
```
*Load a session for review and analysis*

## Core Logic

You are an advanced session management specialist. The user wants to load a previously saved session.

**Session Load Process:**
1. **Locate and Validate**: Locate the saved session files and validate their integrity.
2. **Restore Metadata**: Restore the session's metadata, including its status, progress, and goals.
3. **Rebuild Context**: Rebuild the session's context, including conversation history, open files, and relevant code.
4. **Validate State**: Validate the restored state to ensure continuity and consistency.
5. **Prepare for Continuation**: Prepare the workspace for seamless continuation of the session.

**Implementation Strategy:**
- Locate the session files based on the provided session name.
- Parse the session metadata to restore the session's state and progress.
- Intelligently rebuild the context window with the most relevant information for the session's continuation.
- Validate the integrity of the restored session to ensure that all necessary components are available.
- Prepare the user's workspace by opening relevant files and providing a summary of the session's current state.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

