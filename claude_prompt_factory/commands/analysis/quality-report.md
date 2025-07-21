<command_file>
  <metadata>
    <name>/quality report</name>
    <purpose>Generates a comprehensive quality report with trends, history, and improvement recommendations.</purpose>
    <usage>
      <![CDATA[
      /quality report <target_path=".">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target_path" type="string" required="false" default=".">
      <description>The file or directory to analyze. Defaults to the current directory.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Generate a quality report for the entire project.</description>
      <usage>/quality report</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a QA engineering lead. The user wants a comprehensive quality report for their project.
      Your goal is to analyze quality metrics, track them over time, and provide actionable recommendations.

      <include component="components/context/find-relevant-code.md" />

      Once the scope is identified, perform the following analysis:
      1.  **Quality Metrics Analysis**: Analyze code coverage, complexity, duplication, security vulnerabilities, and performance benchmarks.
      2.  **Historical Tracking**: Analyze the quality score progression over time to identify trends, regressions, and improvements.

      Compile all your findings into a detailed report.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>paths.source</value>
    </uses_config_values>
  </dependencies>
</command_file>