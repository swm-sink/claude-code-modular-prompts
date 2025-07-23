---
name: /git-history
description: Intelligent git history analysis with pattern detection, contributor insights, and code evolution tracking
usage: /git-history [analysis_type] [scope]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent git history analysis with pattern detection, contributor insights, and code evolution tracking

**Usage**: `/git-history $PATH $SINCE $AUTHOR`

## Key Arguments

- **$PATH** (optional): The file or directory path to analyze. Defaults to the entire repository.
- **$SINCE** (optional): The time window to analyze (e.g., '7d', '30d', '3m').
- **$AUTHOR** (optional): Filter the history by a specific author's email.

## Examples

```bash
/git history
```
*Analyze the commit history for the entire repository over the last 30 days.*

```bash
/git history path="src/core" since="3m"
```
*Analyze the history for the 'src/core' directory over the last 3 months.*

## Core Logic

You are a git history analyst. The user wants to understand the development history of the project.

 1. **Fetch Git Log**:
 * Construct a `git log` command based on the `path`, `since`, and `author` arguments.
 * Use a format that provides the commit hash, author, date, and subject for each commit.
 2. **Analyze Data**:
 * Parse the git log output.
 * Aggregate the data to identify key metrics:
 * Total number of commits.
 * Top contributors.
 * Commit frequency over time.
 3. **Generate Report**:
 * Create a report summarizing the findings.
 * Include simple visualizations (e.g., a bar chart for commit frequency) if possible.
 *

**Argument Usage**: Access user input via $ARGUMENT_NAME variables throughout execution.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

