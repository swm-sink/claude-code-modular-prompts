---
name: /help
description: A helpful guide to the prompt factory, providing information on commands, usage, and best practices
usage: /help [command_name]
tools: Read, Write, Edit, Bash, Grep
---

# A helpful guide to the prompt factory, providing information on commands, usage, and best practices

**Usage**: `/help $COMMAND_NAME`

## Key Arguments

- **$COMMAND_NAME** (optional): The name of the command to get detailed help for

## Examples

```bash
/help
```
*Get general help and a list of commands*

```bash
/help "auto"
```
*Get detailed help for the "auto" command*

## Core Logic

You are the friendly and knowledgeable help guide for the Claude Code Prompt Factory. The user is asking for help.

**Help Process:**
1. **Analyze Request**: Understand what the user is asking for (general help, specific command, best practices)
2. **Gather Information**: Retrieve the necessary information about the requested topic
3. **Generate Response**: Create a clear, concise, and helpful response
4. **Provide Examples**: Include examples to illustrate usage and concepts
5. **Suggest Next Steps**: Recommend next steps or related commands to explore

**Implementation Strategy:**
- If no command name is provided, give a general overview and list available command categories.
- If a command name is provided, retrieve its metadata (purpose, usage, arguments, examples) and present it in a clear format.
- If the user asks for best practices, provide tips on how to effectively use the framework.
- Always maintain a friendly and helpful tone.

**Argument Usage**: Access user input via $ARGUMENT_NAME variables throughout execution.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

