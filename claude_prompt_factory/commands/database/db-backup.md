# /db backup - Database Backup Command

**Purpose**: Create secure, verified database backups, with support for full and incremental backups, compression, and encryption.

## Usage
```bash
/db backup [--incremental]
```

## Workflow

The `/db backup` command follows a systematic process to create secure and reliable database backups.

```xml
<backup_workflow>
  <step name="Detect Database System">
    <description>Detect the database system (e.g., PostgreSQL, MySQL) in use to determine the appropriate backup tools.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read project configuration files to identify the database system.</description>
    </tool_usage>
  </step>
  
  <step name="Create Backup">
    <description>Create a full or incremental backup of the database using the appropriate native tools (e.g., 'pg_dump', 'mysqldump').</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate database backup command.</description>
    </tool_usage>
  </step>
  
  <step name="Compress & Encrypt">
    <description>Compress the backup to save space and, if configured, encrypt it to protect sensitive data.</description>
  </step>
  
  <step name="Verify Integrity">
    <description>After the backup is complete, perform an integrity check to ensure that the backup is valid and can be restored.</description>
  </step>
  
  <step name="Store Securely">
    <description>Store the backup in a secure location, as defined in the project's configuration.</description>
  </step>
</backup_workflow>
```

## Security Features
- Pre-backup connection testing
- Encrypted backup files for production
- Access control verification
- Audit logging of backup operations