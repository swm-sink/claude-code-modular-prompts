---
name: /code-format
description: [DEPRECATED] Intelligent code formatting with automated style enforcement, multi-language support, and comprehensive configuration - use /dev format instead
argument-hint: "[language] [style_guide]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
replacement: "/dev format"
removal_date: "2025-08-25"
---
# /code format - Intelligent Code Formatting

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/dev format`

```bash
# Old command:
/code format python --style black

# New command:
/dev format python --style black
```

This standalone command has been consolidated into the unified `/dev` command. The new command provides the same functionality with improved consistency and maintainability.

---

Advanced code formatting system with automated style enforcement, multi-language support, and comprehensive, customizable configuration.
## Usage
```bash
/code format python --style black          # Format Python code using the Black style
/code format --javascript --style prettier # Format JavaScript code using Prettier
/code format --all                         # Format all supported files in the project
/code format --check                       # Check for formatting issues without applying changes
```
<command_file>
  <metadata>
    <n>/code format</n>
    <purpose>Intelligent code formatting with automated style enforcement, multi-language support, and comprehensive configuration</purpose>
    <usage>
      <![CDATA[
      /code format [language] --style [style_guide]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="language" type="string" required="false">
      <description>The programming language to format</description>
    </argument>
    <argument name="style_guide" type="string" required="false" default="default">
      <description>The style guide to use for formatting (e.g., black, prettier, google)</description>
    </argument>
    <argument name="check" type="boolean" required="false" default="false">
      <description>Whether to check for formatting issues without applying changes</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Format Python code using the Black style</description>
      <usage>/code format python --style black</usage>
    </example>
    <example>
      <description>Format all supported files in the project</description>
      <usage>/code format --all</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are an advanced code formatting specialist. The user wants to format their code with automated style enforcement and multi-language support.
**Formatting Process:**
1. **Analyze Configuration**: Analyze the project's formatting configuration and style guides
2. **Discover Files**: Discover all relevant files to be formatted
3. **Apply Formatting**: Apply the specified formatting rules to the code
4. **Report Changes**: Report the changes made and any issues encountered
5. **Handle Edge Cases**: Handle complex formatting scenarios and edge cases gracefully
**Implementation Strategy:**
- Automatically detect the project's programming languages and existing formatting configurations
- Discover all files that match the supported language extensions
- Apply the appropriate formatter (e.g., Black, Prettier, gofmt) with the specified style guide
- Provide a clear report of the files that were formatted and any errors that occurred
- Allow for custom configuration and style guide extensions to handle project-specific needs
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
      <value>formatting.style_guide.default</value>
      <value>formatting.exclude_patterns</value>
    </uses_config_values>
  </dependencies>
</command_file>