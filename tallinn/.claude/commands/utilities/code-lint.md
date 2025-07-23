---
name: /code-lint
description: Intelligent code linting with automated issue detection, configurable rules, and comprehensive reporting
usage: /code-lint [language] [config_file]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent code linting with automated issue detection, configurable rules, and comprehensive reporting

**Usage**: `/code-lint $LANGUAGE $CONFIG_FILE $FIX`

## Key Arguments

- **$LANGUAGE** (optional): The programming language to lint
- **$CONFIG_FILE** (optional): The path to the linting configuration file
- **$FIX** (optional): Whether to automatically fix linting issues

## Examples

```bash
/code lint python --config .pylintrc
```
*Lint Python code using a specific config file*

```bash
/code lint --javascript --fix
```
*Lint and automatically fix JavaScript issues*

## Core Logic

You are an advanced code linting specialist. The user wants to lint their code with automated issue detection and configurable rules.

**Linting Process:**
1. **Analyze Configuration**: Analyze the project's linting configuration and rule sets
2. **Discover Files**: Discover all relevant files to be linted
3. **Perform Linting**: Run the appropriate linter on the code to detect issues
4. **Generate Report**: Generate a comprehensive report of the detected issues
5. **Apply Fixes**: If requested, automatically apply fixes for the detected issues

**Implementation Strategy:**
- Automatically detect the project's programming languages and existing linting configurations
- Discover all files that match the supported language extensions
- Run the appropriate linter (e.g., Pylint, ESLint, GoLint) with the specified configuration
- Generate a clear, actionable report with issue descriptions, locations, and severity levels
- If the `--fix` flag is used, apply the linter's automatic fixes and report the changes

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

