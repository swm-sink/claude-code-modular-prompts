---
name: /db-backup
description: Automated database backup with integrity validation, compression, and secure storage
usage: /db-backup [backup_type] [storage_location]
tools: Read, Write, Edit, Bash, Grep
---

# Automated database backup with integrity validation, compression, and secure storage

**Usage**: `/db-backup [backup_type] [storage_location]`

## Examples

```bash
/db backup
```
*Create a full, secure backup of the primary database.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/interaction/request-user-confirmation.md
 components/error/circuit-breaker.md
 components/reporting/generate-structured-report.md
 components/database/connection-management.md
 components/security/encryption-handling.md
 
 You are a database administrator. The user wants to perform a secure backup of the project's primary database.

 1. **Read Configuration**: Read the `PROJECT_CONFIG.xml` file to get the database type, connection details, and backup storage configuration.
 2. **Detect Database System**: Based on the configuration, identify the database system (e.g., PostgreSQL, MySQL, SQLite).
 3. **Generate Backup Command**: Construct the appropriate native backup command (e.g., `pg_dump`, `mysqldump`). The command should include flags for compression.
 4. **Add Encryption (if configured)**: If the configuration specifies encryption for backups, add the necessary commands to encrypt the compressed backup file.
 5. **Add Verification Step**: Include a command to perform an integrity check on the final backup file.
 6. **Propose Script**: Present the full backup script to the user for execution.

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...


### Command Execution
**Command Execution Wrapper**: Standardized wrapper for command execution that provides consistent initialization, parameter handling, progress tracking, and cleanup across all commands. 1. **Initialization Phase**: - Validate envi...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

