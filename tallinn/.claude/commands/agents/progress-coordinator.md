---
name: /progress-coordinator
description: Meta-coordinator for tracking transformation progress across all 121 command files
usage: /progress-coordinator [tracking_mode] [reporting_frequency] [coordination_scope]
tools: Read, Write, Bash, Grep, Glob
---

# Meta-coordinator for tracking transformation progress across all 121 command files

**Usage**: `/progress-coordinator $TARGET $OPTIONS`

## Key Arguments

- **$TARGET** (optional): Target specification for command execution
- **$OPTIONS** (optional): Additional options for command configuration

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

