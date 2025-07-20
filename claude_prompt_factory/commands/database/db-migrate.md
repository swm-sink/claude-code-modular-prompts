# /db migrate - Database Migration Command

**Purpose**: Safely manage database migrations with support for creation, execution, rollback, and status checks.

## Usage
```bash
/db migrate [action] [target]
```

## Workflow

The `/db migrate` command follows a systematic process to safely manage database migrations.

```xml
<migration_workflow>
  <step name="Detect Database System">
    <description>Detect the database system (e.g., PostgreSQL, MySQL) and migration framework (e.g., Django, Rails, Alembic) in use.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read project configuration files to identify the database system and migration framework.</description>
    </tool_usage>
  </step>
  
  <step name="Validate Migration Safety">
    <description>Perform a series of safety checks to ensure that the migration can be applied without data loss. This includes verifying backups, checking schema compatibility, and ensuring data preservation.</description>
  </step>
  
  <step name="Execute Migration">
    <description>Execute the migration with real-time progress monitoring and error capture. If any issues occur, the command will automatically prepare for a rollback.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the project's configured migration command.</description>
    </tool_usage>
  </step>
  
  <step name="Verify Schema Integrity">
    <description>After the migration is complete, verify the integrity of the database schema to ensure that the changes were applied correctly.</description>
  </step>
</migration_workflow>
```

## Safety Features
- **Backup validation**: Ensures recent backup exists
- **Dry-run mode**: Preview changes without applying
- **Rollback protection**: Automatic rollback scripts
- **Schema verification**: Post-migration validation
- **Data preservation**: No destructive operations without confirmation

## Output Format
```
MIGRATION STATUS
━━━━━━━━━━━━━━━━
✓ Backup verified (5 minutes ago)
✓ 3 pending migrations

APPLYING MIGRATIONS:
[1/3] 001_add_users_table.sql... ✓ Complete (0.2s)
[2/3] 002_add_indexes.sql... ✓ Complete (1.1s)  
[3/3] 003_update_schema.sql... ✓ Complete (0.3s)

Schema integrity: ✓ Valid
Migration history: Updated
```