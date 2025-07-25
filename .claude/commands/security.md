---
description: Advanced security analysis with threat detection, vulnerability assessment, and automated compliance checking
argument-hint: "[security_scope] [analysis_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /analyze security - Advanced Security Analysis

Comprehensive security analysis system with intelligent threat detection, vulnerability assessment, and automated compliance checking.

## Usage
```bash
/analyze security comprehensive              # Comprehensive security analysis
/analyze security --threats                  # Threat detection and modeling
/analyze security --vulnerabilities         # Vulnerability assessment
/analyze security --compliance              # Compliance framework analysis
```

<command_file>
  <metadata>
    <name>/analyze security</name>
    <purpose>Performs a comprehensive security analysis of the codebase based on OWASP standards.</purpose>
    <usage>
      <![CDATA[
      /analyze security <target_path=".">
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
      <description>Run a security analysis on the entire project.</description>
      <usage>/analyze security</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>

      You are a principal security engineer. Your task is to perform a comprehensive security analysis.

      <include component="components/context/find-relevant-code.md" />

      Once the code is identified, perform the following:
      1.  **Scan for Vulnerabilities**: Scan the codebase for a wide range of security vulnerabilities, including the OWASP Top 10, hard-coded secrets, and insecure dependencies.
      2.  **Analyze Security Patterns**: Analyze authentication, authorization, input validation, and data encryption patterns for weaknesses.
      3.  **Generate Report**: Generate a prioritized report of vulnerabilities by severity.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <invokes_commands>
      <command>/security fix</command>
    </invokes_commands>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/context/find-relevant-code.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>paths.source</value>
    </uses_config_values>
  </dependencies>
</command_file>