---
name: /dev-test
description: "Advanced development testing with comprehensive coverage, intelligent test generation, and automated quality validation"
usage: "[test_scope] [coverage_strategy]"
tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/test"
migration_path: "/test with various options (--pattern, --watch, etc.)"
removal_version: "2.0.0"
---
# /dev test - Advanced Development Testing

## ⚠️ DEPRECATION NOTICE

**This command is deprecated and will be removed in version 2.0.0.**

- **Deprecated Date**: 2025-07-25
- **Migration Path**: Use `/test` with various options (--pattern, --watch, etc.) instead
- **Reason**: Command functionality has been consolidated into the unified `/test` command
- **Timeline**: This command will continue to work until version 2.0.0

### Migration Examples:
```bash
# Old usage:
/dev test comprehensive
/dev test --coverage
/dev test --generate
/dev test --parallel
/dev test "user-authentication"

# New usage:
/test --comprehensive
/test --coverage
/test --generate
/test --parallel
/test --pattern "user-authentication"
```

---

Sophisticated development testing system with comprehensive coverage, intelligent test generation, and automated quality validation.
## Usage
```bash
/dev test comprehensive                      # Comprehensive test suite
/dev test --coverage                         # Test coverage analysis
/dev test --generate                         # Intelligent test generation
/dev test --parallel                         # Parallel test execution
```
<command_file>
  <metadata>
    <name>/dev test</name>
    <purpose>Executes a test suite, with support for filtering, coverage reporting, and failure analysis.</purpose>
    <usage>
      <![CDATA[
      /dev test <pattern>
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="pattern" type="string" required="false">
      <description>A pattern or filter to run a specific subset of tests.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Run the entire test suite.</description>
      <usage>/dev test</usage>
    </example>
    <example>
      <description>Run only the tests that match the 'user-authentication' pattern.</description>
      <usage>/dev test "user-authentication"</usage>
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
      You are a test runner. The user wants to execute a test suite.
      1.  **Read Configuration**: Read `project-config.yaml` to get the test command and coverage options for the project's detected test framework.
      2.  **Construct Test Command**: Build the full test command, incorporating the user's `pattern` if provided.
      3.  **Execute Tests**: Run the test command.
      4.  **Generate Report**: After execution, parse the output and generate a comprehensive report.
          *   Include pass/fail counts, duration, and code coverage percentage.
          *   For failed tests, provide the error details and suggestions for fixes.
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>testing.framework</value>
      <value>testing.test_command</value>
      <value>testing.coverage_options</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>