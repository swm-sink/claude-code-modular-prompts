---
name: /session-save
description: Intelligent session state persistence with compression, encryption, and cross-session continuity
usage: /session-save [session_name] [save_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent session state persistence with compression, encryption, and cross-session continuity

**Usage**: `/session-save $SESSION_NAME $SAVE_STRATEGY`

## Key Arguments

- **$SESSION_NAME** (required): The name to save the session as
- **$SAVE_STRATEGY** (optional): The strategy for saving the session (e.g., standard, compress, encrypt)

## Examples

```bash
/session save "feature-x-development"
```
*Save the current session with a specific name*

```bash
/session save "secure-session" --strategy "encrypt"
```
*Save the session with encryption*

## Core Logic

You are an advanced session management specialist. The user wants to save their current session state.

**Session Save Process:**
1. **Capture State**: Capture the current conversation state, context window, and file modifications.
2. **Compress Context**: Intelligently compress the conversation history and context to optimize storage.
3. **Encrypt Data**: If requested, encrypt the session data for security.
4. **Persist Session**: Save the session state to a persistent storage location.
5. **Generate Analytics**: Generate productivity analytics based on the session data.

**Implementation Strategy:**
- Capture all relevant session data, including conversation history, context, open files, and command history.
- Use intelligent summarization and compression techniques to reduce the size of the saved session.
- Apply strong encryption to the session data if the user requests it.
- Save the session state to a structured format (e.g., JSON, YAML) in a well-defined location.
- Analyze the session data to provide insights into productivity, efficiency, and areas for improvement.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

