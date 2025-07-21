<command_file>
  <metadata>
    <name>/secure scan</name>
    <purpose>Performs comprehensive security vulnerability scanning and threat detection.</purpose>
    <usage>
      <![CDATA[
      /secure scan <target="all">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="false" default="all">
      <description>The scan target (e.g., 'all', 'code', 'dependencies', 'secrets').</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Run a comprehensive scan on all targets.</description>
      <usage>/secure scan</usage>
    </example>
    <example>
      <description>Scan only for hardcoded secrets in the codebase.</description>
      <usage>/secure scan target="secrets"</usage>
    </example>
    <example>
      <description>Scan only the project's third-party dependencies.</description>
      <usage>/secure scan target="dependencies"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a security scanner. The user wants to scan the project for vulnerabilities.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the configured security scanning tools (e.g., Snyk, Trivy, Gitleaks).
      2.  **Determine Scan Scope**: Based on the `target` argument, determine which scans to run.
      3.  **Execute Scans**:
          *   Run the appropriate configured tool(s) for the specified target(s).
          *   For `code`, run a static analysis tool (SAST).
          *   For `dependencies`, run a dependency vulnerability scanner.
          *   For `secrets`, run a secret scanning tool.
      4.  **Generate Report**:
          *   Aggregate and de-duplicate the findings from all the tools.
          *   Create a report that lists all identified vulnerabilities, their severity, and recommended remediations.
          *   <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>security.sast_tool</value>
      <value>security.dependency_scanner</value>
      <value>security.secret_scanner</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>