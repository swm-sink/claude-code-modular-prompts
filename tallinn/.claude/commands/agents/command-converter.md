---
name: /command-converter
description: Specialized agent for converting command files to hybrid Markdown+XML format
usage: /command-converter [file_batch] [conversion_mode] [validation_level]
tools: Read, Write, Edit, MultiEdit, Grep, Glob
---

# Specialized agent for converting command files to hybrid Markdown+XML format

**Usage**: `/command-converter $FILE_BATCH $CONVERSION_MODE $VALIDATION_LEVEL`

## Key Arguments

- **$FILE_BATCH** (required): File pattern or batch specification for conversion (e.g., "commands/analysis/*.m...
- **$CONVERSION_MODE** (optional): Conversion execution mode: sequential, parallel, or adaptive based on file compl...
- **$VALIDATION_LEVEL** (optional): Validation strictness: basic, standard, or strict XML and Markdown validation.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

