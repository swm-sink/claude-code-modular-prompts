<command_file>
  <metadata>
    <name>/analyze performance</name>
    <purpose>Analyzes application code for performance bottlenecks and provides optimization recommendations.</purpose>
    <usage>
      <![CDATA[
      /analyze performance <target_path="." focus="time">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target_path" type="string" required="false" default=".">
      <description>The file or directory to analyze. Defaults to the current directory.</description>
    </argument>
    <argument name="focus" type="string" required="false" default="time">
      <description>The specific area to focus on (e.g., 'time', 'memory', 'io').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Run a time-focused performance analysis on the entire project.</description>
      <usage>/analyze performance</usage>
    </example>
    <example>
      <description>Analyze the memory usage of a specific service.</description>
      <usage>/analyze performance "src/user_service/" focus="memory"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a senior performance engineer. The user wants to analyze their application for performance bottlenecks and get optimization recommendations.

      <include component="components/context/find-relevant-code.md" />

      Once the target code is identified, perform a deep performance analysis covering these areas:
      - **Bottleneck Detection**: Algorithmic complexity, hot paths, memory leaks, and I/O blocking.
      - **Performance Patterns**: N+1 queries, unnecessary nested loops, and synchronous operations.
      - **Metrics Analysis**: Response times, throughput, and resource utilization.

      Based on your analysis, provide a set of actionable optimization recommendations.

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