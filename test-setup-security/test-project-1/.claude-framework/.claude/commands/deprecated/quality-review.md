---
name: /quality-review
description: "Comprehensive quality review with automated code review, best practices validation, and improvement recommendations"
argument-hint: "[review_scope] [quality_standard]"
allowed-tools: Read, Write, Edit, Bash, Grep
# DEPRECATION METADATA
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/quality review"
reason: "Consolidated into unified /quality command for better UX and maintainability"
migration_deadline: "2025-08-25"
---
# ⚠️ DEPRECATED: /quality-review

**This command is deprecated and will be removed on 2025-08-25.**

## Migration Path
This functionality has been consolidated into the unified `/quality` command:

### Old Usage → New Usage
```bash
# OLD (deprecated)
/quality-review code                 # Review code quality
/quality-review architecture         # Review architectural quality 
/quality-review security             # Security-focused quality review
/quality-review performance          # Performance quality review

# NEW (recommended)
/quality review "src/"               # Comprehensive code review
/quality review --scope security     # Security-focused review
/quality review --scope performance  # Performance-focused review
/quality review --depth deep         # Deep architectural analysis
```

### Migration Benefits
- **Unified Interface**: Single command for all quality operations
- **Enhanced Options**: More granular control with --scope, --depth, --format flags
- **Better Integration**: Seamless workflow with metrics, reports, and suggestions
- **Consistent UX**: Standardized argument patterns across all quality functions

### Quick Migration Guide
1. Replace `/quality-review` calls with `/quality review`
2. Add `--scope` flag for focused analysis areas
3. Use `--depth deep` for comprehensive architectural review
4. Combine with other modes: `/quality all` for complete analysis

For detailed usage examples, see `/quality --help` or the [Quality Command Documentation](.claude/commands/quality/quality.md).

---

# /quality review - Quality Review Framework (LEGACY)
Advanced quality review system with automated code review, best practices validation, and comprehensive improvement recommendations.
## Usage
```bash
/quality review code                         # Review code quality
/quality review architecture                 # Review architectural quality
/quality review security                     # Security-focused quality review
/quality review performance                  # Performance quality review
```
<command_file>
  <metadata>
    <name>/quality review</name>
    <purpose>Performs an automated, comprehensive code review for compliance with standards and best practices.</purpose>
    <usage>
      <![CDATA[
      /quality review <target_path=".">
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="target_path" type="string" required="false" default=".">
      <description>The file or directory to review. Defaults to the current directory.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Review the entire project's code quality.</description>
      <usage>/quality review</usage>
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
      You are a principal software engineer performing a code review.
      <include component="components/context/find-relevant-code.md" />
      Once the code is identified, perform a deep analysis covering:
      -   **Coding standards**: Compliance with project conventions.
      -   **Design patterns**: Correct usage and opportunities for improvement.
      -   **Error handling**: Completeness and correctness.
      -   **Test coverage**: Adequacy and quality of tests.
      -   **Security**: Adherence to best practices.
      <include component="components/quality/anti-pattern-detection.md" />
      <include component="components/quality/framework-validation.md" />
      <include component="components/context/adaptive-thinking.md" />
      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
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