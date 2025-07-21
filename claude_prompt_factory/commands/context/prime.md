<command_file>
  <metadata>
    <name>/context prime</name>
    <purpose>Performs a standard analysis of the codebase to provide a high-level overview of the project.</purpose>
    <usage>
      <![CDATA[
      /context prime
      ]]>
    </usage>
  </metadata>

  <arguments>
    <!-- No arguments -->
  </arguments>
  
  <examples>
    <example>
      <description>Run a standard analysis on the current project.</description>
      <usage>/context prime</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a codebase analysis tool. Perform a high-level analysis of the project to provide a "context priming" summary.

      1.  **Analyze Structure**: Execute `/analyze code` to get the project structure, language, and framework.
      2.  **Analyze Dependencies**: Execute `/analyze dependencies` to list key libraries.
      3.  **Analyze Patterns**: Execute `/analyze patterns` to identify common design patterns.
      4.  **Generate Report**: Synthesize the information from the above steps into a concise summary report.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <chain>
      <command>/analyze code</command>
      <command>/analyze dependencies</command>
      <command>/analyze patterns</command>
    </chain>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file> 