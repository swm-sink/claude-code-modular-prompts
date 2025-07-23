---
name: /db-restore
description: Advanced database restoration with intelligent recovery, point-in-time restoration, and comprehensive data integrity validation
usage: /db-restore [restore_strategy] [recovery_point]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced database restoration with intelligent recovery, point-in-time restoration, and comprehensive data integrity validation

**Usage**: `/db-restore $BACKUP_SOURCE $RESTORE_STRATEGY`

## Key Arguments

- **$BACKUP_SOURCE** (required): Path or identifier of the backup source to restore from
- **$RESTORE_STRATEGY** (optional): Restoration strategy (full, incremental, point-in-time)

## Examples

```bash
/db restore backup_20240101.sql full
```
*Full database restoration*

```bash
/db restore --point-in-time "2024-01-01 12:00:00"
```
*Point-in-time recovery*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/error/circuit-breaker.md
 components/quality/framework-validation.md
 components/reporting/generate-structured-report.md
 components/database/backup-validation.md
 components/database/recovery-strategies.md
 
You are a database restoration specialist. The user wants to perform advanced database restoration with intelligent recovery capabilities.

**Restoration Process:**
1. **Backup Validation**: Validate backup integrity and compatibility
2. **Recovery Planning**: Plan optimal restoration strategy and timeline
3. **Data Restoration**: Execute restoration with integrity monitoring
4. **Validation Testing**: Comprehensive testing of restored data
5. **Performance Optimization**: Optimize restored database performance

**Implementation Strategy:**
- Validate backup files and check integrity
- Plan restoration timeline and rollback strategies
- Execute point-in-time or full restoration procedures
- Perform comprehensive data validation and integrity checks
- Optimize database performance post-restoration

## Essential Component Logic

### Input Validation

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

