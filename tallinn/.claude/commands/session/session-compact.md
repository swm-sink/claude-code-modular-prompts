---
name: /session-compact
description: Advanced session compacting with intelligent compression, context optimization, and efficient state management
usage: /session-compact [compact_strategy] [optimization_level]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced session compacting with intelligent compression, context optimization, and efficient state management

**Usage**: `/session-compact $STRATEGY $OPTIMIZATION_LEVEL`

## Key Arguments

- **$STRATEGY** (optional): The compression strategy to use (e.g., conservative, balanced, aggressive)
- **$OPTIMIZATION_LEVEL** (optional): The level of optimization to apply during compacting

## Examples

```bash
/session compact balanced
```
*Compact the session with a balanced strategy*

```bash
/session compact aggressive --level high
```
*Compact the session aggressively to maximize free space*

## Core Logic

You are an advanced session compacting specialist. The user wants to compact their current session to optimize context usage.

**Compacting Process:**
1. **Analyze Context**: Analyze the current conversation for key elements, patterns, and critical information.
2. **Intelligent Summarization**: Create a hierarchical summary of the conversation, preserving the logical flow and key decisions.
3. **Extract Patterns**: Extract reusable patterns, insights, and working knowledge from the conversation.
4. **Optimize Content**: Compress repetitive content and verbose explanations while preserving essential context.
5. **Validate and Update**: Validate that all critical information is preserved and update the context window with the compacted content.

**Implementation Strategy:**
- Use intelligent summarization techniques to create a concise yet comprehensive summary of the session.
- Identify and extract key decisions, insights, and code snippets to be preserved.
- Compress repetitive conversational patterns and verbose explanations into more concise forms.
- Ensure that the compacted session maintains full continuity and all necessary context for the user to seamlessly continue their work.
- Provide a report detailing the compression results, including the compression ratio and the amount of context freed.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

