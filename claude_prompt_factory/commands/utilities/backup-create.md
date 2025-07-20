# /backup create - Comprehensive Project Backup Command

**Purpose**: Create a comprehensive, verified, and secure backup of the entire project, including files, databases, and Git history.

## Usage
```bash
/backup create "[description]" [--type=full|incremental] [--encrypt]
```

## Workflow

The `/backup create` command follows a systematic process to create a comprehensive project backup.

```xml
<backup_workflow>
  <step name="Analyze & Categorize Assets">
    <description>Scan and categorize all project assets, including source code, documentation, databases, and Git history.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the project to identify all assets to be backed up.</description>
    </tool_usage>
  </step>
  
  <step name="Create & Compress Backup">
    <description>Create a full or incremental backup of the project assets, and then package and compress the data using optimal compression algorithms.</description>
  </step>
  
  <step name="Verify & Store Backup">
    <description>Validate the integrity of the backup with checksums, and then save it to the configured secure storage location (e.g., local, S3, GCS, Azure).</description>
  </step>
</backup_workflow>
```

## Key Features
- **Backup Types**: Full, incremental, and differential backups.
- **Multi-Format Support**: Supports tar.gz, zip, and 7z formats.
- **Encryption**: Provides encryption for sensitive projects.
- **Cloud Storage Integration**: Integrates with S3, GCS, and Azure for secure storage.
- **Database Backup Inclusion**: Includes a backup of the project's database.
- **Git Repository Preservation**: Preserves the full Git repository history.

---
*Comprehensive backups protect against data loss*