---
name: /code-lint
description: [DEPRECATED] Intelligent code linting with automated issue detection, configurable rules, and comprehensive reporting - use /dev lint instead
argument-hint: "[language] [config_file]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
replacement: "/dev lint"
removal_date: "2025-08-25"
---
# /code lint - Intelligent Code Linting

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/dev lint`

```bash
# Old command:
/code lint python --config .pylintrc

# New command:
/dev lint python --config .pylintrc
```

This standalone command has been consolidated into the unified `/dev` command. The new command provides the same functionality with improved consistency and maintainability.

---

Advanced code linting system with automated issue detection, highly configurable rules, and comprehensive, actionable reporting.
## Usage
```bash
/code lint python --config .pylintrc       # Lint Python code using a specific config file
/code lint --javascript --fix              # Lint and automatically fix JavaScript issues
/code lint --all                           # Lint all supported files in the project
/code lint --report "summary"              # Generate a summary report of linting issues
```
<command_file>
  <metadata>
    <n>/code lint</n>
    <purpose>Intelligent code linting with automated issue detection, configurable rules, and comprehensive reporting</purpose>
    <usage>
      <![CDATA[
      /code lint [language] --config [config_file]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="language" type="string" required="false">
      <description>The programming language to lint</description>
    </argument>
    <argument name="config_file" type="string" required="false">
      <description>The path to the linting configuration file</description>
    </argument>
    <argument name="fix" type="boolean" required="false" default="false">
      <description>Whether to automatically fix linting issues</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Lint Python code using a specific config file</description>
      <usage>/code lint python --config .pylintrc</usage>
    </example>
    <example>
      <description>Lint and automatically fix JavaScript issues</description>
      <usage>/code lint --javascript --fix</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are an advanced code linting specialist. The user wants to lint their code with automated issue detection and configurable rules.
**Linting Process:**
1. **Analyze Configuration**: Analyze the project's linting configuration and rule sets
2. **Discover Files**: Discover all relevant files to be linted
3. **Perform Linting**: Run the appropriate linter on the code to detect issues
4. **Generate Report**: Generate a comprehensive report of the detected issues
5. **Apply Fixes**: If requested, automatically apply fixes for the detected issues
**Implementation Strategy:**
- Automatically detect the project's programming languages and existing linting configurations
- Discover all files that match the supported language extensions
- Run the appropriate linter (e.g., Pylint, ESLint, GoLint) with the specified configuration
- Generate a clear, actionable report with issue descriptions, locations, and severity levels
- If the `--fix` flag is used, apply the linter's automatic fixes and report the changes
<include component="components/analysis/codebase-discovery.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>linting.config.default</value>
      <value>linting.auto_fix</value>
    </uses_config_values>
  </dependencies>
</command_file>