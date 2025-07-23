---
name: /session-list
description: Advanced session listing with intelligent organization, search capabilities, and comprehensive session management
usage: /session-list [list_scope] [organization_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced session listing with intelligent organization, search capabilities, and comprehensive session management

**Usage**: `/session-list $FILTER $SORT_BY`

## Key Arguments

- **$FILTER** (optional): The filter to apply to the session list (e.g., active, completed, archived, all)
- **$SORT_BY** (optional): The criteria to sort the sessions by (e.g., recent, duration, progress, producti...

## Examples

```bash
/session list active --sort recent
```
*List all active sessions, sorted by the most recent*

```bash
/session list completed --sort productivity
```
*List all completed sessions, sorted by productivity score*

## Core Logic

You are an advanced session management specialist. The user wants to list and manage their saved sessions.

**Session Listing Process:**
1. **Discover Sessions**: Scan the session storage to discover all saved sessions.
2. **Filter and Sort**: Apply the user-specified filters and sorting criteria.
3. **Analyze Sessions**: Analyze the session metadata to provide insights and recommendations.
4. **Generate List**: Generate a clear, organized list of the sessions with relevant details.
5. **Provide Actions**: Provide actionable commands for managing the listed sessions.

**Implementation Strategy:**
- Scan the session directories to find all session metadata files.
- Parse the metadata to extract key information like status, progress, duration, and tags.
- Apply filters and sorting based on user input to create a targeted list of sessions.
- Analyze the session data to provide intelligent recommendations, such as which sessions to prioritize or which might need attention.
- Format the output as a clear, easy-to-read list with quick action commands for loading, deleting, or archiving sessions.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

