<command_file>
  <metadata>
    <name>/error report</name>
    <purpose>Generates comprehensive error analysis reports with trends, classifications, and actionable insights.</purpose>
    <usage>
      <![CDATA[
      /error report <timeframe="7d">
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
      <description>Generate an error report for the last 7 days.</description>
      <usage>/error report</usage>
    </example>
    <example>
      <description>Generate an error report for the last 24 hours.</description>
      <usage>/error report timeframe="24h"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a data analyst specializing in software quality. The user wants a report on error trends.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured logging and monitoring service integrations.
      2.  **Gather Error Data**:
          *   Fetch error data from the configured services (e.g., Sentry, LogRocket, Datadog) for the specified `timeframe`.
          *   If no integration is configured, analyze local log files.
      3.  **Analyze and Classify**:
          *   Process the data to identify error trends.
          *   Classify errors by type (e.g., Frontend, Backend, Database) and root cause.
          *   Calculate key metrics like error frequency, impact (number of users affected), and new vs. regressed errors.
      4.  **Generate Report**:
          *   Create a comprehensive report summarizing the findings with clear visualizations.
          *   Highlight the most critical errors that need immediate attention.
          *   Provide actionable insights and recommendations.
          *   <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>monitoring.logging_service</value>
      <value>monitoring.error_tracking_service</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>