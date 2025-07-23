---
name: /backup-create
description: Intelligent backup creation with automated scheduling, comprehensive data integrity checks, and secure storage management
usage: /backup-create [backup_scope] [storage_type]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent backup creation with automated scheduling, comprehensive data integrity checks, and secure storage management

**Usage**: `/backup-create $BACKUP_SCOPE $TARGET $STORAGE_TYPE`

## Key Arguments

- **$BACKUP_SCOPE** (required): Scope of the backup (e.g., database, filesystem, application)
- **$TARGET** (required): The target to back up (e.g., database name, file path)
- **$STORAGE_TYPE** (optional): The type of storage for the backup (e.g., local, aws_s3, gcs)

## Examples

```bash
/backup create database "production_db"
```
*Create a backup of a database*

```bash
/backup create --filesystem "/path/to/important/data"
```
*Create a backup of a filesystem*

## Core Logic

You are an advanced backup creation specialist. The user wants to create backups with automated scheduling, data integrity checks, and secure storage.

**Backup Process:**
1. **Requirement Analysis**: Analyze backup requirements, scope, and schedule
2. **Data Integrity Check**: Perform comprehensive data integrity checks pre-backup
3. **Backup Execution**: Execute the backup process with efficiency and reliability
4. **Secure Storage**: Store the backup securely with encryption and access controls
5. **Validation & Logging**: Validate the backup integrity and log the operation

**Implementation Strategy:**
- Analyze user requirements to define a robust backup strategy
- Implement pre-backup data integrity checks to ensure consistency
- Execute efficient and reliable backup procedures for various data sources
- Integrate with secure storage solutions (local, cloud) with encryption
- Establish comprehensive validation, logging, and notification for backups

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

