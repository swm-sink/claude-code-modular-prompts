---
name: /framework-tester
description: Specialized agent for comprehensive framework validation and integration testing
usage: /framework-tester [test_scope] [validation_mode] [coverage_level]
tools: Read, Bash, Grep, Glob, Write
---

# Specialized agent for comprehensive framework validation and integration testing

**Usage**: `/framework-tester $TEST_SCOPE $VALIDATION_MODE $COVERAGE_LEVEL`

## Key Arguments

- **$TEST_SCOPE** (required): Testing scope: full_validation, command_discovery, component_system, or routing_...
- **$VALIDATION_MODE** (optional): Validation approach: local, claude (Claude Code), or integration testing.
- **$COVERAGE_LEVEL** (optional): Testing depth: basic, standard, or deep coverage analysis.

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

