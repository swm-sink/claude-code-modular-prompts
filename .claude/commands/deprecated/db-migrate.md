---
name: /db-migrate
description: Safe database migration with rollback capabilities, validation, and change tracking
argument-hint: "[migration_direction] [target_version]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
deprecation_deadline: "2025-08-25"
deprecation_replacement: "/db-admin migrate"
deprecation_reason: "Consolidated into unified /db-admin command for better maintenance and consistency"
---
# /db migrate - Database Migration System

⚠️ **DEPRECATION NOTICE** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Migration:** Use `/db-admin migrate` instead.

**Examples:**
- `/db migrate up` → `/db-admin migrate up`
- `/db migrate down` → `/db-admin migrate down`
- `/db migrate --target 1.2.3` → `/db-admin migrate --target 1.2.3`
- `/db migrate --dry-run` → `/db-admin migrate --dry-run`

The new `/db-admin` command provides all the same functionality with improved consistency and maintainability.

---

Advanced database migration system with safe execution, rollback capabilities, and comprehensive change tracking.
## Usage
```bash
/db migrate up                               # Apply pending migrations
/db migrate down                             # Rollback last migration
/db migrate --target 1.2.3                  # Migrate to specific version
/db migrate --dry-run                        # Preview migration changes
```
<command_file>
  <metadata>
    <name>/db migrate</name>
    <purpose>Safely manages database migrations with support for creation, execution, and rollback.</purpose>
    <usage>
      <![CDATA[
      /db migrate <action="up"> <name="migration_name">
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="action" type="string" required="false" default="up">
      <description>The migration action to perform. Can be 'up', 'down', 'status', or 'create'.</description>
    </argument>
    <argument name="name" type="string" required="false">
      <description>The name for a new migration file (only used with action="create").</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Apply all pending database migrations.</description>
      <usage>/db migrate</usage>
    </example>
    <example>
      <description>Create a new migration file named 'add_user_roles'.</description>
      <usage>/db migrate action="create" name="add_user_roles"</usage>
    </example>
    <example>
      <description>Roll back the last applied migration.</description>
      <usage>/db migrate action="down"</usage>
    </example>
     <example>
      <description>Check the status of all migrations.</description>
      <usage>/db migrate action="status"</usage>
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
      You are a database administrator. The user wants to manage database migrations.
      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to determine the migration framework (e.g., Alembic, Django migrations, Rails migrations) and directory.
      2.  **Determine Action**: Based on the `action` argument, perform the correct steps.
      3.  **Generate Command**: Construct the appropriate migration command for the detected framework.
      *   **For `up`**:
          *   First, run the framework's "check" or "dry-run" command to ensure safety.
          *   Present the plan to the user for confirmation.
          *   On approval, run the command to apply pending migrations.
          *   Afterward, run the "status" command to verify.
      *   **For `down`**:
          *   Present a clear warning about rolling back.
          *   On approval, run the command to roll back the last migration.
      *   **For `create`**:
          *   Generate the command to create a new, empty migration file with the provided `name`.
      *   **For `status`**:
          *   Run the command to show the current migration status.
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>database.migration_framework</value>
      <value>database.migration_directory</value>
    </uses_config_values>
    <includes_components>
      <component>components/interaction/request-user-confirmation.md</component>
    </includes_components>
  </dependencies>
</command_file>