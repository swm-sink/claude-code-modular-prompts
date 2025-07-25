---
description: Advanced development build system with intelligent optimization, parallel processing, and automated quality checks
argument-hint: "[build_type] [optimization_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
removal_date: "2025-08-25"
replacement: "/pipeline build"
---
# /dev build - Advanced Development Build

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/pipeline build`

This standalone command has been consolidated into the unified `/pipeline` command. The new command provides the same functionality with improved consistency and maintainability.

---

Sophisticated development build system with intelligent optimization, parallel processing, and automated quality assurance.
## Usage
```bash
/dev build production                        # Production-optimized build
/dev build --parallel                        # Parallel build processing
/dev build --optimize                        # Advanced optimization build
/dev build --watch                           # Continuous build monitoring
```
<command_file>
  <metadata>
    <name>/dev build</name>
    <purpose>Provides comprehensive build automation for development workflows.</purpose>
    <usage>
      <![CDATA[
      /dev build <target="all">
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="target" type="string" required="false" default="all">
      <description>The build target to run (e.g., 'all', 'frontend', 'backend', 'tests').</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Run a full project build.</description>
      <usage>/dev build</usage>
    </example>
    <example>
      <description>Build only the frontend assets.</description>
      <usage>/dev build target="frontend"</usage>
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
      <include>components/actions/parallel-execution.md</include>
      <include>components/quality/quality-metrics.md</include>
      You are a build automation tool. The user wants to run a development build.
      1.  **Read Configuration**: Read the `PROJECT_CONFIG.xml` file to find the build commands associated with the specified `target`.
      2.  **Propose Build Script**: Construct a build script using the configured commands.
      3.  **Execute Script**: Present the script to the user for confirmation. Upon approval, execute the script.
      4.  **Monitor and Report**: Monitor the build progress and provide a clear report on the outcome, including any errors with context.
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>build.targets.target</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>