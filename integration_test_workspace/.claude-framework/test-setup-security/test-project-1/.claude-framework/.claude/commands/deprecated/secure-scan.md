---
name: /secure-scan
description: "Pattern analysis tool with code review and configuration validation"
argument-hint: "[scan_type] [output_format]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation-date: 2025-07-25
removal-date: 2025-08-25
replacement: "/secure-assess scan"
---
# /secure scan - Code Analysis Tool

⚠️ **DEPRECATED COMMAND** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/secure-assess scan`

This command has been consolidated into the new `/secure-assess` command with `scan` mode for better organization and consistency.

---

Code analysis tool with pattern detection and configuration review capabilities.
## Usage
```bash
/secure scan patterns              # Analyze code patterns
/secure scan dependencies           # Review dependency configuration
/secure scan static --format json   # Static code analysis with JSON output
```
<command_file>
  <metadata>
    <name>/secure scan</name>
    <purpose>Performs code pattern analysis and configuration review.</purpose>
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
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <!-- Command-specific components -->
      <include>components/reporting/generate-structured-report.md</include>
      
      You are a code analysis tool. The user wants to review the project for patterns and configuration issues.
      1.  **Read Configuration**: Read `project-config.yaml` to get the configured analysis tools.
      2.  **Determine Analysis Scope**: Based on the `target` argument, determine which reviews to run.
      3.  **Execute Analysis**:
          *   Run the appropriate configured tool(s) for the specified target(s).
          *   For `code`, run static analysis and pattern detection.
          *   For `dependencies`, review dependency configuration and compatibility.
          *   For `secrets`, check for hardcoded values and configuration issues.
      4.  **Generate Report**:
          *   Aggregate and organize the findings from all the tools.
          *   Create a report that lists identified patterns, their impact, and recommended improvements.
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>analysis.static_tool</value>
      <value>analysis.dependency_checker</value>
      <value>analysis.pattern_scanner</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>