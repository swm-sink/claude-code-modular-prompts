---
name: /code-format
description: Intelligent code formatting with automated style enforcement, multi-language support, and comprehensive configuration
usage: /code-format [language] [style_guide]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent code formatting with automated style enforcement, multi-language support, and comprehensive configuration

**Usage**: `/code-format $LANGUAGE $STYLE_GUIDE $CHECK`

## Key Arguments

- **$LANGUAGE** (optional): The programming language to format
- **$STYLE_GUIDE** (optional): The style guide to use for formatting (e.g., black, prettier, google)
- **$CHECK** (optional): Whether to check for formatting issues without applying changes

## Examples

```bash
/code format python --style black
```
*Format Python code using the Black style*

```bash
/code format --all
```
*Format all supported files in the project*

## Core Logic

You are an advanced code formatting specialist. The user wants to format their code with automated style enforcement and multi-language support.

**Formatting Process:**
1. **Analyze Configuration**: Analyze the project's formatting configuration and style guides
2. **Discover Files**: Discover all relevant files to be formatted
3. **Apply Formatting**: Apply the specified formatting rules to the code
4. **Report Changes**: Report the changes made and any issues encountered
5. **Handle Edge Cases**: Handle complex formatting scenarios and edge cases gracefully

**Implementation Strategy:**
- Automatically detect the project's programming languages and existing formatting configurations
- Discover all files that match the supported language extensions
- Apply the appropriate formatter (e.g., Black, Prettier, gofmt) with the specified style guide
- Provide a clear report of the files that were formatted and any errors that occurred
- Allow for custom configuration and style guide extensions to handle project-specific needs

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

