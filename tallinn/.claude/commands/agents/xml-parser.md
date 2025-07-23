---
name: /xml-parser
description: Specialized agent for fixing XML parsing errors and validating command file structure
usage: /xml-parser [target_files] [error_mode] [validation_depth]
tools: Read, Write, Edit, Grep, Bash
---

# Specialized agent for fixing XML parsing errors and validating command file structure

**Usage**: `/xml-parser $TARGET_FILES $ERROR_MODE $VALIDATION_DEPTH`

## Key Arguments

- **$TARGET_FILES** (required): File pattern, error list, or validation mode (e.g., "commands/**/*.md", "error_f...
- **$ERROR_MODE** (optional): Error fixing aggressiveness: conservative, standard, or aggressive approach.
- **$VALIDATION_DEPTH** (optional): Validation thoroughness: basic, standard, or deep XML structure analysis.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

