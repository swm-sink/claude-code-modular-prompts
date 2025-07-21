---
description: Seeds a database with realistic test data, handling relationships and validation
argument-hint: "[env] [count]"
allowed-tools: Bash, Read, Write, Grep
---

# /db seed - Database Seeding Tool

Seeds a database with realistic test data, properly handling relationships and validation.

## Usage
```bash
/db seed                          # Default: development with 100 records
/db seed env="testing" count=500  # Testing environment with 500 records
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
      You are a database seeding tool. The user wants to populate the database with test data. This may be a destructive action.

      1.  **Warning & Confirmation**: Inform the user that this action might truncate existing data and require their explicit confirmation to proceed.
          <include component="components/interaction/request-user-confirmation.md" />

      2.  **On Confirmation**:
          *   **Read Configuration**: Read `PROJECT_CONFIG.xml` to find the seed configuration file (e.g., `db/seeds.js`).
          *   **Generate Seeding Script**: Generate a data seeding script (e.g., Python, Node.js, or SQL) that:
              *   Generates realistic data for the specified `env` and `count`.
              *   Correctly handles foreign key relationships to maintain integrity.
              *   Wraps all insertion operations in a single transaction.
          *   **Present Script**: Present the complete seeding script to the user for review and execution.
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