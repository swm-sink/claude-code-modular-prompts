<command_file>
  <metadata>
    <name>/docs check</name>
    <purpose>Validates the completeness, accuracy, and consistency of project documentation.</purpose>
    <usage>
      <![CDATA[
      /docs check <target_directory="./docs">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="false" default="./docs">
      <description>The directory to scan for documentation files.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Check all documentation in the default 'docs' directory.</description>
      <usage>/docs check</usage>
    </example>
    <example>
      <description>Check documentation within the 'guides' subdirectory.</description>
      <usage>/docs check target="./docs/guides"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a documentation quality assurance tool. Your task is to validate the project's documentation.

      1.  **Scan and Analyze**: Scan the `target` directory for all documentation files.
      2.  **Perform Checks**:
          *   **Completeness**: Check for missing READMEs or undocumented public functions/modules.
          *   **Accuracy**: Validate that code examples are correct and match the actual code.
          *   **Consistency**: Check for consistent formatting and style.
          *   **Broken Links**: Check for broken internal and external links.
      3.  **Generate Report**: Create a detailed report summarizing the findings.
          *   Provide a quality score and list all identified issues with file paths and line numbers.
          *   Offer actionable recommendations for improvement.
          *   <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>