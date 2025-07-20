# /db seed - Database Seeding Command

**Purpose**: Seed a database with realistic test data, with support for relationship handling, data validation, and environment-specific data sets.

## Usage
```bash
/db seed [--env=development] [--tables=users,orders] [--count=100]
```

## Workflow

The `/db seed` command follows a systematic process to safely seed a database with high-quality test data.

```xml
<seeding_workflow>
  <step name="Parse Configuration">
    <description>Parse the user's request and the project's seed configuration to determine the target environment, tables, and data volumes.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read the project's seed configuration file.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Data">
    <description>Generate a set of realistic test data, using faker libraries and other techniques to ensure the data is varied and realistic. This step also ensures that all foreign key relationships are maintained.</description>
  </step>
  
  <step name="Validate Schema & Insert Data">
    <description>Validate that the generated data matches the database schema constraints, and then insert the data safely using transactions with rollback on failure.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the database insertion commands within a transaction.</description>
    </tool_usage>
  </step>
  
  <step name="Verify Integrity">
    <description>After the data has been inserted, run a series of post-insertion validation checks to ensure data integrity and consistency.</description>
  </step>
</seeding_workflow>
```

## Capabilities
- **Data Generation**: Creates realistic test data using faker libraries
- **Relationship Handling**: Maintains foreign key relationships and referential integrity
- **Environment Support**: Supports dev/test/staging environments with different data sets
- **Validation**: Verifies data integrity and constraint compliance
- **Configurable**: Allows custom data volumes and scenarios

## Technical Implementation
1. **Parse Configuration**: Read seed configuration and target environment
2. **Generate Data**: Create realistic data using faker with proper relationships
3. **Validate Schema**: Ensure data matches database schema constraints
4. **Insert Safely**: Use transactions with rollback on validation failures
5. **Verify Integrity**: Run post-insert validation checks

## Quality Gates
- All foreign key relationships must be valid
- Data must pass schema validation
- Transaction rollback on any constraint violation
- Configurable data volume limits to prevent accidents

## Output
- Data generation summary with counts per table
- Relationship validation report
- Performance metrics (insert speed, validation time)
- Error details for any failed constraints

## Error Handling
- Transaction rollback on constraint violations
- Graceful handling of duplicate key conflicts
- Memory management for large data sets
- Connection pool management

---
*Part of Claude Code database management suite - Good seed data enables effective testing*