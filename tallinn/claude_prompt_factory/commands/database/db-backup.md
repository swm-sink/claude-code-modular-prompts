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
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/error/circuit-breaker.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/database/connection-management.md</include>
      <include>components/security/encryption-handling.md</include>
      
      You are a database administrator. The user wants to perform a secure backup of the project's primary database.

      1.  **Read Configuration**: Read the `PROJECT_CONFIG.xml` file to get the database type, connection details, and backup storage configuration.
      2.  **Detect Database System**: Based on the configuration, identify the database system (e.g., PostgreSQL, MySQL, SQLite).
      3.  **Generate Backup Command**: Construct the appropriate native backup command (e.g., `pg_dump`, `mysqldump`). The command should include flags for compression.
      4.  **Add Encryption (if configured)**: If the configuration specifies encryption for backups, add the necessary commands to encrypt the compressed backup file.
      5.  **Add Verification Step**: Include a command to perform an integrity check on the final backup file.
      6.  **Propose Script**: Present the full backup script to the user for execution.
    </prompt>
  </claude_prompt>

  <includes_components>
    <component>components/constitutional/safety-framework.md</component>
  </includes_components>
</command_file>