<command_file>
  <metadata>
    <name>/analyze code</name>
    <purpose>Performs a comprehensive analysis of a codebase, focusing on structure, complexity, and quality.</purpose>
    <usage>
      <![CDATA[
      /analyze code <target_path="." focus="full">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target_path" type="string" required="false" default=".">
      <description>The file or directory to analyze. Defaults to the current directory.</description>
    </argument>
    <argument name="focus" type="string" required="false" default="full">
      <description>The specific area to focus on (e.g., 'performance', 'security', 'quality').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Run a full analysis on the entire project.</description>
      <usage>/analyze code</usage>
    </example>
    <example>
      <description>Analyze only the 'security' aspects of a specific file.</description>
      <usage>/analyze code "src/auth/service.py" focus="security"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are an expert code analyst. The user wants to perform a comprehensive analysis of their codebase.
      Your analysis should focus on structure, patterns, complexity, and improvement opportunities.

      <include component="components/context/find-relevant-code.md" />

      Once the code is identified, perform the following analysis steps:
      1.  **Code Structure Review**: Analyze component relationships, dependencies, and architectural patterns.
      2.  **Complexity Analysis**: Calculate cyclomatic complexity, assess function length, and evaluate nesting depth.
      3.  **Pattern Recognition**: Identify design patterns, anti-patterns, and code duplication.
      4.  **Quality Assessment**: Detect code smells, score maintainability, and identify technical debt.
      5.  **Improvement Recommendations**: Suggest refactoring opportunities and performance optimizations.

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
      <value>paths.tests</value>
    </uses_config_values>
  </dependencies>
</command_file>