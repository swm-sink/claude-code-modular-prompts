---
description: Unified database administration with migration, backup, and restoration capabilities
argument-hint: "[operation] [options]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /db-admin - Unified Database Administration System

Comprehensive database administration command combining migration management, backup operations, and restoration procedures with intelligent orchestration and safety features.

## Usage

```bash
# Migration Operations
/db-admin migrate up                             # Apply pending migrations
/db-admin migrate down                           # Rollback last migration
/db-admin migrate --target 1.2.3                # Migrate to specific version
/db-admin migrate create add_user_roles          # Create new migration
/db-admin migrate status                         # Check migration status

# Backup Operations  
/db-admin backup full                            # Complete database backup
/db-admin backup incremental                     # Incremental backup
/db-admin backup --compress                      # Compressed backup
/db-admin backup --encrypt                       # Encrypted backup

# Restoration Operations
/db-admin restore backup_file.sql               # Standard restoration
/db-admin restore --point-in-time               # Point-in-time recovery
/db-admin restore --incremental                 # Incremental restoration
/db-admin restore --validate                    # Restoration with validation
```

<command_file>
  <metadata>
    <name>/db-admin</name>
    <purpose>Unified database administration system providing migration management, backup operations, and restoration procedures with comprehensive safety features.</purpose>
    <usage>
      <![CDATA[
      /db-admin <operation> [action] [options]
      ]]>
    </usage>
  </metadata>
  
  <arguments>
    <argument name="operation" type="string" required="true">
      <description>Primary database operation: migrate, backup, or restore</description>
      <valid_values>migrate,backup,restore</valid_values>
    </argument>
    <argument name="action" type="string" required="false">
      <description>Specific action within the operation (varies by operation type)</description>
    </argument>
    <argument name="target" type="string" required="false">
      <description>Target for operation (migration version, backup file, etc.)</description>
    </argument>
    <argument name="options" type="string" required="false">
      <description>Additional options like --compress, --encrypt, --dry-run, --validate</description>
    </argument>
  </arguments>

  <examples>
    <example>
      <description>Apply all pending database migrations with safety checks</description>
      <usage>/db-admin migrate up</usage>
    </example>
    <example>
      <description>Create a new migration file with descriptive name</description>
      <usage>/db-admin migrate create add_user_authentication</usage>
    </example>
    <example>
      <description>Rollback the last applied migration with confirmation</description>
      <usage>/db-admin migrate down</usage>
    </example>
    <example>
      <description>Check current migration status across all environments</description>
      <usage>/db-admin migrate status</usage>
    </example>
    <example>
      <description>Create a full encrypted backup of the database</description>
      <usage>/db-admin backup full --encrypt</usage>
    </example>
    <example>
      <description>Perform incremental backup with compression</description>
      <usage>/db-admin backup incremental --compress</usage>
    </example>
    <example>
      <description>Restore database from backup file with validation</description>
      <usage>/db-admin restore backup_20240101.sql --validate</usage>
    </example>
    <example>
      <description>Perform point-in-time recovery to specific timestamp</description>
      <usage>/db-admin restore --point-in-time "2024-01-01 12:00:00"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/reliability/circuit-breaker.md</include>
      <include>components/quality/framework-validation.md</include>
      <include>components/reporting/generate-structured-report.md</include>

      You are a comprehensive database administrator with expertise in migrations, backups, and restoration procedures. The user wants to perform database administration operations with maximum safety and reliability.

      ## Operation Router
      Based on the `operation` argument, route to the appropriate specialist workflow:

      ### MIGRATE Operations
      When `operation` = "migrate":
      
      1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to determine migration framework (Alembic, Django, Rails, etc.) and directory structure.
      
      2. **Route by Action**:
         - **"up"** (default): Apply pending migrations
           - Run framework's dry-run/check command first
           - Present migration plan to user for confirmation
           - Execute migrations with progress tracking
           - Verify final state with status command
         
         - **"down"**: Rollback migrations
           - Present clear rollback warning with affected changes
           - Request explicit user confirmation
           - Execute rollback with safety monitoring
           - Verify rollback completion
         
         - **"create"**: Generate new migration
           - Use `target` argument as migration name
           - Generate framework-appropriate migration file
           - Open file for user editing if requested
         
         - **"status"**: Display migration state
           - Show applied vs pending migrations
           - Display current database version
           - Highlight any inconsistencies

      ### BACKUP Operations  
      When `operation` = "backup":
      
      1. **Read Configuration**: Extract database type, connection details, and backup storage configuration from `PROJECT_CONFIG.xml`.
      
      2. **Detect Database System**: Identify database system (PostgreSQL, MySQL, SQLite, etc.) and select appropriate tools.
      
      3. **Route by Action**:
         - **"full"** (default): Complete database backup
         - **"incremental"**: Backup changes since last full backup
         - **Custom action**: Use as backup identifier/tag
      
      4. **Process Options**:
         - **--compress**: Add compression to backup command
         - **--encrypt**: Include encryption pipeline if configured
         - **--validate**: Add integrity verification step
      
      5. **Execute Backup Pipeline**:
         - Generate native backup command (pg_dump, mysqldump, etc.)
         - Apply compression and encryption as requested
         - Perform integrity verification
         - Store backup with metadata (timestamp, size, checksum)

      ### RESTORE Operations
      When `operation` = "restore":
      
      1. **Backup Source Validation**:
         - If `target` provided: validate backup file exists and integrity
         - If `--point-in-time`: validate timestamp format and availability
         - Check backup compatibility with current database version
      
      2. **Route by Action/Options**:
         - **Standard restore**: Full database replacement from backup
         - **--point-in-time**: Time-based recovery using transaction logs
         - **--incremental**: Apply incremental backups in sequence
         - **--validate**: Include comprehensive data validation post-restore
      
      3. **Restoration Pipeline**:
         - Create database backup before restoration (safety net)
         - Plan restoration strategy and estimate timeline
         - Execute restoration with progress monitoring
         - Perform data integrity validation
         - Optimize database performance post-restoration
         - Generate detailed restoration report

      ## Safety and Orchestration Features

      ### Universal Safety Checks
      - Always validate database connectivity before operations
      - Check disk space requirements for operations
      - Verify user permissions for database operations
      - Create safety backups before destructive operations
      - Monitor operation progress and provide clear status updates

      ### Error Handling and Recovery
      - Implement circuit breaker pattern for database operations
      - Provide clear rollback procedures for failed operations
      - Log all operations with detailed audit trail
      - Offer recovery suggestions for common failure scenarios

      ### Integration and Reporting
      - Generate structured reports for all operations
      - Integrate with existing project configuration
      - Support multiple database frameworks and systems
      - Provide performance metrics and operation statistics

      ## Implementation Notes
      - Always read PROJECT_CONFIG.xml first to understand the database setup
      - Use framework-specific commands and best practices
      - Implement proper error handling with clear user feedback
      - Maintain audit logs for all database operations
      - Support both interactive and automated execution modes
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>database.type</value>
      <value>database.connection_string</value>
      <value>database.migration_framework</value>
      <value>database.migration_directory</value>
      <value>backups.storage_location</value>
      <value>backups.encryption.enabled</value>
      <value>database.backup.retention_days</value>
      <value>database.restore.validation_level</value>
    </uses_config_values>
    
    <includes_components>
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/reliability/circuit-breaker.md</component>
      <component>components/quality/framework-validation.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>