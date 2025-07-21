---
description: Automated database backup with integrity validation, compression, and secure storage
argument-hint: "[backup_type] [storage_location]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /db backup - Database Backup System

Comprehensive database backup system with integrity validation, compression options, and secure storage capabilities.

## Usage
```bash
/db backup full                              # Complete database backup
/db backup incremental                       # Incremental backup since last full
/db backup --compress                        # Backup with compression
/db backup --encrypt                         # Encrypted backup with security
```

<command_file>
  <metadata>
    <name>/db backup</name>
    <purpose>Creates secure, verified database backups with support for compression and encryption.</purpose>
    <usage>
      <![CDATA[
      /db backup
      ]]>
    </usage>
  </metadata>

  <arguments>
    <!-- No arguments, but behavior is driven by PROJECT_CONFIG.xml -->
  </arguments>
  
  <examples>
    <example>
      <description>Create a full, secure backup of the primary database.</description>
      <usage>/db backup</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a database administrator. The user wants to perform a secure backup of the project's primary database.

      1.  **Read Configuration**: Read the `PROJECT_CONFIG.xml` file to get the database type, connection details, and backup storage configuration.
      2.  **Detect Database System**: Based on the configuration, identify the database system (e.g., PostgreSQL, MySQL, SQLite).
      3.  **Generate Backup Command**: Construct the appropriate native backup command (e.g., `pg_dump`, `mysqldump`). The command should include flags for compression.
      4.  **Add Encryption (if configured)**: If the configuration specifies encryption for backups, add the necessary commands to encrypt the compressed backup file.
      5.  **Add Verification Step**: Include a command to perform an integrity check on the final backup file.
      6.  **Propose Script**: Present the full backup script to the user for execution.
      <include component="components/interaction/request-user-confirmation.md" />
      <include component="components/error/circuit-breaker.md" />
      <include component="components/workflow/error-handling.md" />
      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>database.type</value>
      <value>database.connection_string</value>
      <value>backups.storage_location</value>
      <value>backups.encryption.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file>