<command_file>
  <metadata>
    <name>/dev build</name>
    <purpose>Provides comprehensive build automation for development workflows.</purpose>
    <usage>
      <![CDATA[
      /dev build <target="all">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="false" default="all">
      <description>The build target to run (e.g., 'all', 'frontend', 'backend', 'tests').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Run a full project build.</description>
      <usage>/dev build</usage>
    </example>
    <example>
      <description>Build only the frontend assets.</description>
      <usage>/dev build target="frontend"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a build automation tool. The user wants to run a development build.

      1.  **Read Configuration**: Read the `PROJECT_CONFIG.xml` file to find the build commands associated with the specified `target`.
      2.  **Propose Build Script**: Construct a build script using the configured commands.
      3.  **Execute Script**: Present the script to the user for confirmation. Upon approval, execute the script.
      4.  **Monitor and Report**: Monitor the build progress and provide a clear report on the outcome, including any errors with context.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>build.targets.target</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>