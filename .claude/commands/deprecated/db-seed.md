---
name: /db-seed
description: Populates database with seed data for development and testing environments
argument-hint: "[environment] [data_type]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
deprecation_deadline: "2025-08-25"
deprecation_replacement: "/db-admin seed"
deprecation_reason: "Consolidated into unified /db-admin command for better maintenance and consistency"
---
# /db seed - Database Seeding Command
Intelligent database seeding system with environment-specific data sets and validation.
## Usage
```bash
/db seed development              # Seed development environment
/db seed testing --clean         # Clean and seed test environment
/db seed production --confirm     # Seed production (with confirmation)
```
## Arguments
- `env` (optional): Target environment (default: "development")
- `count` (optional): Number of records per table (default: 100)
<command_file>
  <metadata>
    <name>/db seed</name>
    <purpose>Seeds a database with realistic test data, handling relationships and validation.</purpose>
    <usage>
      <![CDATA[
      /db seed env="development" count=100
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="env" type="string" required="false" default="development">
      <description>The target environment to seed (e.g., development, testing).</description>
    </argument>
    <argument name="count" type="integer" required="false" default="100">
      <description>The number of records to generate for primary tables.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Seed the development database with 100 records per table.</description>
      <usage>/db seed</usage>
    </example>
    <example>
      <description>Seed the testing database with 500 records per table.</description>
      <usage>/db seed env="testing" count=500</usage>
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
      <![CDATA[
      You are a database seeding tool. The user wants to populate the database with test data. This may be a destructive action.
      1.  **Warning & Confirmation**: Inform the user that this action might truncate existing data and require their explicit confirmation to proceed.
      2.  **On Confirmation**:
          *   **Read Configuration**: Read `PROJECT_CONFIG.xml` to find the seed configuration file (e.g., `db/seeds.js`).
          *   **Generate Seeding Script**: Generate a data seeding script (e.g., Python, Node.js, or SQL) that:
              *   Generates realistic data for the specified `env` and `count`.
              *   Correctly handles foreign key relationships to maintain integrity.
              *   Wraps all insertion operations in a single transaction.
          *   **Present Script**: Present the complete seeding script to the user for review and execution.
      ]]>
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>database.seed_config_file</value>
    </uses_config_values>
    <includes_components>
      <component>components/interaction/request-user-confirmation.md</component>
    </includes_components>
  </dependencies>
</command_file>

---

⚠️ **DEPRECATION NOTICE** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Migration:** Use `/db-admin seed` instead.

**Examples:**
- `/db seed development` → `/db-admin seed development`
- `/db seed testing --clean` → `/db-admin seed testing --clean`
- `/db seed production --confirm` → `/db-admin seed production --confirm`

The new `/db-admin` command provides all the same functionality with improved consistency and maintainability.