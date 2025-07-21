<command_file>
  <metadata>
    <name>/db restore</name>
    <purpose>Restores a database from a backup, with support for validation and multiple recovery options.</purpose>
    <usage>
      <![CDATA[
      /db restore <backup_file>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="backup_file" type="string" required="true">
      <description>Path to the database backup file to restore.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Restore the database from a specified backup file.</description>
      <usage>/db restore "backups/db_2024-07-21.sql.gz"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a database administrator. The user wants to restore the database from a backup file. This is a highly destructive operation.

      1.  **EXTREME WARNING**: Present a clear, severe warning to the user about the destructive nature of this action (overwriting the current database).
      2.  **Request Confirmation**: Require explicit confirmation from the user before proceeding.
          <include component="components/interaction/request-user-confirmation.md" />

      3.  **On Confirmation**:
          *   **Validate Backup**: First, validate the integrity and compatibility of the backup file.
          *   **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the database type and connection details.
          *   **Generate Restore Command**: Construct the appropriate native restore command (e.g., `pg_restore`, `mysql`).
          *   **Propose Script**: Present the full restore script to the user for final review before they execute it.
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>database.type</value>
      <value>database.connection_string</value>
    </uses_config_values>
    <includes_components>
      <component>components/interaction/request-user-confirmation.md</component>
    </includes_components>
  </dependencies>
</command_file>