---
name: /db-admin
description: Unified database administration with migration, backup, and restoration (v1.0)
version: "1.0"
usage: '[operation] [options]'
category: specialized
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate input parameters and execution context
  during-execution: Monitor progress and maintain safety checks
  post-execution: Verify successful completion and cleanup
progressive-disclosure:
  layer-integration: Integrated command for specialized workflows
  escalation-path: Basic usage → advanced options → full customization
  de-escalation: Simplify to essential functionality
safety-measures:
  - Validate all inputs before execution
  - Create backups when modifying files
  - Confirm destructive operations
  - Maintain system integrity
error-recovery:
  input-error: Provide clear usage examples and syntax
  execution-failure: Show detailed context and recovery steps
  system-error: Fallback to safe mode operation
---

# /db-admin - Unified Database Administration System for [INSERT_PROJECT_NAME]

Comprehensive database administration command for [INSERT_DATABASE_TYPE] in [INSERT_DOMAIN] applications, combining migration management, backup operations, and restoration procedures with intelligent orchestration and safety features tailored for [INSERT_TECH_STACK] environments.

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

# Seeding Operations
/db-admin seed development                       # Seed development environment
/db-admin seed testing --clean                  # Clean and seed test environment
/db-admin seed production --confirm             # Seed production (with confirmation)
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
      <description>Primary database operation: migrate, backup, restore, or seed</description>
      <valid_values>migrate,backup,restore,seed</valid_values>
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
    <example>
      <description>Seed development database with default record count</description>
      <usage>/db-admin seed development</usage>
    </example>
    <example>
      <description>Clean and seed testing environment with 500 records</description>
      <usage>/db-admin seed testing --clean count=500</usage>
    </example>
    <example>
      <description>Seed production environment with confirmation</description>
      <usage>/db-admin seed production --confirm</usage>
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

      You are a comprehensive database administrator for [INSERT_PROJECT_NAME] with expertise in [INSERT_DATABASE_TYPE] migrations, backups, and restoration procedures. The user wants to perform database administration operations for their [INSERT_DOMAIN] application with maximum safety and reliability in [INSERT_TECH_STACK] environments.

      ## Operation Router
      Based on the `operation` argument, route to the appropriate specialist workflow:

      ### MIGRATE Operations
      When `operation` = "migrate":
      
      1. **Read Configuration**: Read `project-config.yaml` to determine migration framework appropriate for [INSERT_TECH_STACK] (Alembic, Django, Rails, etc.) and directory structure for [INSERT_PROJECT_NAME].
      
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
      
      1. **Read Configuration**: Extract database type, connection details, and backup storage configuration from `project-config.yaml`.
      
      2. **Detect Database System**: Identify database system ([INSERT_DATABASE_TYPE] or alternative) and select appropriate tools for [INSERT_TECH_STACK].
      
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

      ### SEED Operations
      When `operation` = "seed":
      
      1. **Environment Validation**:
         - Validate target environment (development, testing, production)
         - Check database connectivity and access permissions
         - Warn about potential data truncation/overwriting
         - Request explicit user confirmation for destructive operations
      
      2. **Configuration Loading**:
         - Read `project-config.yaml` to find seed configuration file
         - Parse seeding parameters (record counts, data types, relationships)
         - Validate seed data integrity and foreign key constraints
      
      3. **Route by Environment**:
         - **"development"** (default): Standard development dataset
         - **"testing"**: Testing-optimized dataset with edge cases
         - **"production"**: Production-safe seeding (requires --confirm)
         - **Custom environment**: Use environment-specific configuration
      
      4. **Process Options**:
         - **--clean**: Truncate existing data before seeding
         - **--confirm**: Explicit confirmation for production environments
         - **count=N**: Override default record count per table
         - **--validate**: Perform data integrity validation after seeding
      
      5. **Execute Seeding Pipeline**:
         - Generate realistic test data with proper relationships
         - Handle foreign key dependencies in correct order
         - Wrap all operations in single transaction for atomicity
         - Monitor progress and provide status updates
         - Validate data integrity and constraint compliance
         - Generate seeding report with statistics and metrics

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
      - Always read project-config.yaml first to understand the database setup
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
      <value>database.seed_config_file</value>
      <value>database.seed.default_record_count</value>
      <value>database.seed.environments</value>
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