<command_file>
  <metadata>
    <name>/perf report</name>
    <purpose>Generates comprehensive performance reports with trends, insights, and actionable recommendations.</purpose>
    <usage>
      <![CDATA[
      /perf report <timeframe="7d">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="timeframe" type="string" required="false" default="7d">
      <description>The time window for the report (e.g., '24h', '7d', '30d').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Generate a performance report for the last 7 days.</description>
      <usage>/perf report</usage>
    </example>
    <example>
      <description>Generate a performance report for the last 30 days.</description>
      <usage>/perf report timeframe="30d"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a performance analyst. The user wants a report on application performance.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured monitoring and benchmarking data sources.
      2.  **Gather Performance Data**:
          *   Fetch performance data (e.g., response times, throughput, error rates) from the configured services for the specified `timeframe`.
          *   Incorporate data from recent benchmark runs.
      3.  **Analyze and Identify Trends**:
          *   Analyze the data to identify performance trends, patterns, and anomalies.
          *   Compare the current performance against historical baselines.
      4.  **Generate Report**:
          *   Create a comprehensive report with clear visualizations of key performance metrics.
          *   Highlight any significant performance regressions or improvements.
          *   Provide actionable recommendations for optimization.
          *   <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>monitoring.performance_monitoring_service</value>
      <value>performance.benchmark_tool</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>