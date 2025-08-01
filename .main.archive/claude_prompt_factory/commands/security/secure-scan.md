---
description: Automated security scanning with vulnerability detection and compliance reporting
argument-hint: "[scan_type] [output_format]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /secure scan - Automated Security Scanner

High-performance security scanner with multiple detection engines and comprehensive reporting.

## Usage
```bash
/secure scan vulnerabilities         # Scan for known vulnerabilities
/secure scan dependencies           # Dependency vulnerability scan
/secure scan static --format json   # Static code analysis with JSON output
```

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
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/security/vulnerability-scanning.md</include>
      <include>components/security/dependency-scanning.md</include>
      <include>components/security/secret-detection.md</include>
      <include>components/analysis/severity-assessment.md</include>
      
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