---
name: /component-linker
description: Specialized agent for managing component dependencies and include resolution
usage: /component-linker [operation_mode] [target_scope] [resolution_strategy]
tools: Read, Write, Edit, Grep, Glob, Bash
---

# Specialized agent for managing component dependencies and include resolution

**Usage**: `/component-linker $OPERATION_MODE $TARGET_SCOPE $RESOLUTION_STRATEGY`

## Key Arguments

- **$OPERATION_MODE** (required): Operation type: validate_all, resolve_includes, optimize_graph, or repair_links.
- **$TARGET_SCOPE** (optional): Scope of operation: commands, components, or all framework files.
- **$RESOLUTION_STRATEGY** (optional): Resolution approach: conservative, standard, or aggressive optimization.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

