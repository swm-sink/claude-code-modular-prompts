---
name: /db-migrate
description: Safe database migration with rollback capabilities, validation, and change tracking
usage: /db-migrate [migration_direction] [target_version]
tools: Read, Write, Edit, Bash, Grep
---

# Safe database migration with rollback capabilities, validation, and change tracking

**Usage**: `/db-migrate $ACTION $NAME`

## Key Arguments

- **$ACTION** (optional): The migration action to perform. Can be 'up', 'down', 'status', or 'create'.
- **$NAME** (optional): The name for a new migration file (only used with action="create").

## Examples

```bash
/db migrate
```
*Apply all pending database migrations.*

```bash
/db migrate action="create" name="add_user_roles"
```
*Create a new migration file named 'add_user_roles'.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/interaction/request-user-confirmation.md
 components/database/migration-framework-detection.md
 components/database/schema-validation.md
 components/workflow/rollback-capabilities.md
 components/quality/change-tracking.md
 
 You are a database administrator. The user wants to manage database migrations.

 1. **Read Configuration**: Read `PROJECT_CONFIG.xml` to determine the migration framework (e.g., Alembic, Django migrations, Rails migrations) and directory.
 2. **Determine Action**: Based on the `action` argument, perform the correct steps.
 3. **Generate Command**: Construct the appropriate migration command for the detected framework.

 * **For `up`**:
 * First, run the framework's "check" or "dry-run" command to ensure safety.
 * Present the plan to the user for confirmation.
 * On approval, run the command to apply pending migrations.
 * Afterward, run the "status" command to verify.

 * **For `down`**:
 * Present a clear warning about rolling back.
 * On approval, run the command to roll back the last migration.

 * **For `create`**:
 * Generate the command to create a new, empty migration file with the provided `name`.


*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

