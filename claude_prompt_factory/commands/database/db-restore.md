---
description: Safe database restoration with validation, rollback capabilities, and integrity verification
argument-hint: "[backup_source] [restore_target]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /db restore - Database Restoration System

Comprehensive database restoration system with safety validation, integrity checks, and rollback capabilities.

## Usage
```bash
/db restore latest                           # Restore from latest backup
/db restore --backup backup_20240127.sql    # Restore from specific backup
/db restore --dry-run                        # Preview restoration process
/db restore --verify                         # Restore with integrity verification
```

## Arguments

```bash
/db restore <backup_file>
```

## Examples

```bash
/db restore "backups/db_2024-07-21.sql.gz"
```

## Dependencies

```bash
/db restore <backup_file>
```