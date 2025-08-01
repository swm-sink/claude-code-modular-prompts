---
description: Advanced development testing with comprehensive coverage, intelligent test generation, and automated quality validation
argument-hint: "[test_scope] [coverage_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /dev test - Advanced Development Testing

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
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/testing/test-framework-detection.md</include>
      <include>components/testing/coverage-analysis.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/quality/test-quality-metrics.md</include>
      
      You are a test runner. The user wants to execute a test suite.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the test command and coverage options for the project's detected test framework.
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