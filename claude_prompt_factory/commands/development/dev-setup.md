<command_file>
  <metadata>
    <name>/dev setup</name>
    <purpose>Sets up and configures a complete development environment for a project.</purpose>
    <usage>
      <![CDATA[
      /dev setup
      ]]>
    </usage>
  </metadata>

  <arguments>
    <!-- No arguments, all configuration is read from PROJECT_CONFIG.xml -->
  </arguments>
  
  <examples>
    <example>
      <description>Set up the development environment based on the project's configuration.</description>
      <usage>/dev setup</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a development environment specialist. The user wants to set up the complete development environment for this project.

      1.  **Read Configuration**: Read the `PROJECT_CONFIG.xml` file to get the list of required tools, dependencies, and setup scripts.
      2.  **Generate Setup Plan**: Create a step-by-step plan to:
          *   Install required language runtimes and package managers.
          *   Install project dependencies (e.g., `npm install`, `pip install -r requirements.txt`).
          *   Configure development tools (linters, formatters).
          *   Set up pre-commit Git hooks.
      3.  **Propose Script**: Present the full setup script to the user for confirmation.
      4.  **Execute and Verify**: Upon approval, execute the script. After execution, run the verification steps defined in the configuration to ensure everything is working correctly.
      5.  **Report Outcome**: Generate a report on the setup process, including a troubleshooting guide for any potential issues.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>development.setup.dependencies</value>
      <value>development.setup.scripts</value>
      <value>development.setup.verification</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>