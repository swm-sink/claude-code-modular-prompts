---
description: Advanced quality suggestions with intelligent recommendations, automated improvements, and best practice guidance
argument-hint: "[suggestion_scope] [improvement_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
# DEPRECATION METADATA
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/quality suggest"
reason: "Consolidated into unified /quality command for better UX and maintainability"
migration_deadline: "2025-08-25"
---
# ⚠️ DEPRECATED: /quality-suggest

**This command is deprecated and will be removed on 2025-08-25.**

## Migration Path
This functionality has been consolidated into the unified `/quality` command:

### Old Usage → New Usage
```bash
# OLD (deprecated)
/analyze quality-suggest comprehensive      # Comprehensive quality suggestions
/analyze quality-suggest --performance      # Performance improvement suggestions
/analyze quality-suggest --security         # Security enhancement suggestions
/analyze quality-suggest --maintainability  # Maintainability improvements

# NEW (recommended)
/quality suggest                            # Get prioritized improvements
/quality suggest --category performance     # Performance-focused suggestions
/quality suggest --category security        # Security-focused suggestions
/quality suggest --effort low               # Quick wins only
/quality suggest --category maintainability # Maintainability improvements
```

### Migration Benefits
- **Impact vs Effort Matrix**: Prioritized by ROI (Return on Investment)
- **Category Filtering**: Focus on specific improvement areas
- **Effort-Based Filtering**: Find quick wins or major initiatives
- **Implementation Roadmap**: Ordered improvement timeline
- **Code Examples**: Before/after examples for suggestions

### Advanced Suggestion Features
```bash
# Prioritized improvement strategies
/quality suggest --effort low --category performance  # Quick performance wins
/quality suggest --category security --format detailed # Detailed security improvements
/quality all --threshold 8.0                         # Full analysis with suggestions
```

### Suggestion Categories
- `performance`: Speed and efficiency improvements
- `maintainability`: Code clarity and structure
- `security`: Vulnerability fixes and hardening
- `documentation`: Code comments and docs

### Effort Levels
- `low`: Quick wins (hours to days)
- `medium`: Moderate effort (days to weeks)
- `high`: Major initiatives (weeks to months)

### Priority Matrix
- **High Impact/Low Effort**: Quick wins (do first)
- **High Impact/High Effort**: Major initiatives (plan carefully)
- **Low Impact/Low Effort**: Nice to have (fill spare time)
- **Low Impact/High Effort**: Avoid (lowest priority)

### Quick Migration Guide
1. Replace `/analyze quality-suggest` with `/quality suggest`
2. Add `--category` flag to focus on specific areas
3. Add `--effort` flag to filter by implementation effort
4. Use `--format detailed` for comprehensive suggestions
5. Combine with analysis: `/quality all` for complete workflow

For detailed usage examples, see `/quality --help` or the [Quality Command Documentation](.claude/commands/quality/quality.md).

---

# /analyze quality-suggest - Advanced Quality Suggestions (LEGACY)
Sophisticated quality suggestion system with intelligent recommendations, automated improvements, and comprehensive best practice guidance.
## Usage
```bash
/analyze quality-suggest comprehensive       # Comprehensive quality suggestions
/analyze quality-suggest --performance       # Performance improvement suggestions
/analyze quality-suggest --security          # Security enhancement suggestions
/analyze quality-suggest --maintainability   # Maintainability improvements
```
<command_file>
  <metadata>
    <name>/quality suggest</name>
    <purpose>Generates a prioritized, actionable list of quality improvement suggestions.</purpose>
    <usage>
      <![CDATA[
      /quality suggest <target_path=".">
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
      <description>Get quality improvement suggestions for the entire project.</description>
      <usage>/quality suggest</usage>
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
      You are a senior software architect. Your task is to provide a prioritized, actionable list of quality improvements.
      <include component="components/context/find-relevant-code.md" />
      Once the code is identified, perform the following:
      1.  **Analyze Code Quality**: Identify areas for improvement in performance, maintainability, security, and documentation.
      2.  **Prioritize Opportunities**: Prioritize the opportunities based on their potential impact and estimated effort.
      3.  **Generate Suggestions**: Generate a clear list of suggestions, complete with code examples.
      Your output should be a structured report, but instead of findings, the sections should be prioritized suggestions (e.g., "Priority 1: High Impact, Low Effort").
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
