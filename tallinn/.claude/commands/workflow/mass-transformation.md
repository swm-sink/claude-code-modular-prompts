---
name: /mass-transformation
description: Ultimate transformation workflow that spawns 50+ agents for complete framework conversion
usage: /mass-transformation [transformation_scope] [agent_limit] [parallel_mode]
tools: Task, Read, Write, Edit, Bash, Grep, Glob
---

# Ultimate transformation workflow that spawns 50+ agents for complete framework conversion

**Usage**: `/mass-transformation $TRANSFORMATION_SCOPE $AGENT_LIMIT $PARALLEL_MODE`

## Key Arguments

- **$TRANSFORMATION_SCOPE** (required): Scope of transformation: complete_factory, commands_only, validation_only, or st...
- **$AGENT_LIMIT** (optional): Maximum agents to spawn: number or "unlimited" for stress testing limits.
- **$PARALLEL_MODE** (optional): Parallel processing intensity: conservative, aggressive, or maximum.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

