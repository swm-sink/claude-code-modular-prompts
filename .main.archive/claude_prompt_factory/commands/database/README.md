# Database Commands

Tools for database management, migration, and seeding.

## Available Commands

*   **`/db backup`**: Create comprehensive database backups with versioning.
*   **`/db migrate`**: Execute database migrations with rollback capabilities.
*   **`/db restore`**: Restore database from backup with validation.
*   **`/db seed`**: Populate database with development or test data.

## Command Details

### Backup Operations
- Full database backups with compression
- Incremental backup support
- Automated backup verification
- Version tagging and retention policies

### Migration Management
- Forward and backward migration execution
- Migration validation and testing
- Dependency tracking and ordering
- Rollback safety checks

### Data Seeding
- Development data creation
- Test fixture generation
- Production data sanitization
- Seed data versioning

## Usage Examples

```bash
# Create a full backup
/db backup "pre-migration-backup"

# Run pending migrations
/db migrate up

# Rollback to specific migration
/db migrate down 20240101_create_users

# Seed development data
/db seed development

# Restore from backup
/db restore "pre-migration-backup" --verify
```

## Configuration

Database commands read connection settings and migration paths from `PROJECT_CONFIG.xml`:

```xml
<database>
  <type>postgresql</type>
  <migrations_path>migrations/</migrations_path>
  <seeds_path>seeds/</seeds_path>
</database>
```

## Safety Features

- Automatic backup before destructive operations
- Migration validation before execution
- Rollback plans for all operations
- Data integrity verification 