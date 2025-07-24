---
description: Intelligent backup creation with automated scheduling, comprehensive data integrity checks, and secure storage management
argument-hint: "[backup_scope] [storage_type]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /backup create - Intelligent Backup Creation

Advanced backup creation system with automated scheduling, comprehensive data integrity checks, and secure, multi-location storage management.

## Usage
```bash
/backup create database "production_db"      # Create a backup of a database
/backup create --filesystem "/path/to/data"  # Create a backup of a filesystem
/backup create --scheduled "daily"           # Schedule automated backups
/backup create --secure "aws_s3"             # Create a secure backup in cloud storage
```

<command_file>
  <metadata>
    <n>/backup create</n>
    <purpose>Intelligent backup creation with automated scheduling, comprehensive data integrity checks, and secure storage management</purpose>
    <usage>
      <![CDATA[
      /backup create [backup_scope] "[target]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="backup_scope" type="string" required="true" default="database">
      <description>Scope of the backup (e.g., database, filesystem, application)</description>
    </argument>
    <argument name="target" type="string" required="true">
      <description>The target to back up (e.g., database name, file path)</description>
    </argument>
    <argument name="storage_type" type="string" required="false" default="local">
      <description>The type of storage for the backup (e.g., local, aws_s3, gcs)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Create a backup of a database</description>
      <usage>/backup create database "production_db"</usage>
    </example>
    <example>
      <description>Create a backup of a filesystem</description>
      <usage>/backup create --filesystem "/path/to/important/data"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced backup creation specialist. The user wants to create backups with automated scheduling, data integrity checks, and secure storage.

**Backup Process:**
1. **Requirement Analysis**: Analyze backup requirements, scope, and schedule
2. **Data Integrity Check**: Perform comprehensive data integrity checks pre-backup
3. **Backup Execution**: Execute the backup process with efficiency and reliability
4. **Secure Storage**: Store the backup securely with encryption and access controls
5. **Validation &amp; Logging**: Validate the backup integrity and log the operation

**Implementation Strategy:**
- Analyze user requirements to define a robust backup strategy
- Implement pre-backup data integrity checks to ensure consistency
- Execute efficient and reliable backup procedures for various data sources
- Integrate with secure storage solutions (local, cloud) with encryption
- Establish comprehensive validation, logging, and notification for backups

<include component="components/database/db-backup.md" />
<include component="components/security/secure-config.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/database/db-backup.md</component>
      <component>components/security/secure-config.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>backup.schedule.auto_enabled</value>
      <value>storage.secure.encryption_key</value>
    </uses_config_values>
  </dependencies>
</command_file>