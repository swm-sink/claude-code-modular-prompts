---
description: Intelligent unit testing with automated test generation, comprehensive coverage analysis, and detailed reporting
argument-hint: "[file_path] [coverage_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---
# /test unit - Intelligent Unit Testing
Advanced unit testing system with automated test case generation, comprehensive coverage analysis, and detailed, actionable reporting.
## Usage
```bash
/test unit "path/to/my_file.py"              # Generate and run unit tests for a specific file
/test unit --coverage "high" "path/to/dir"   # Aim for high test coverage for a directory
/test unit --report "detailed"               # Generate a detailed unit test report
/test unit --auto-fix "true"                 # Automatically fix simple test failures
```
<command_file>
  <metadata>
    <n>/test unit</n>
    <purpose>Intelligent unit testing with automated test generation, comprehensive coverage analysis, and detailed reporting</purpose>
    <usage>
      <![CDATA[
      /test unit "[file_path]" --coverage [coverage_level]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="file_path" type="string" required="true">
      <description>The path to the file or directory to generate unit tests for</description>
    </argument>
    <argument name="coverage_level" type="string" required="false" default="medium">
      <description>The desired test coverage level (e.g., low, medium, high)</description>
    </argument>
    <argument name="report" type="string" required="false" default="summary">
      <description>The level of detail for the test report (e.g., summary, detailed)</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Generate and run unit tests for a specific file</description>
      <usage>/test unit "src/my_module/my_file.py"</usage>
    </example>
    <example>
      <description>Aim for high test coverage for a directory</description>
      <usage>/test unit --coverage "high" "src/my_module/"</usage>
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
You are an advanced unit testing specialist. The user wants to generate and run unit tests for their code.
**Unit Testing Process:**
1. **Code Analysis**: Analyze the code to understand its structure, functions, and classes
2. **Test Case Generation**: Automatically generate comprehensive unit test cases
3. **Test Execution**: Execute the generated tests and capture the results
4. **Coverage Analysis**: Analyze the test coverage and identify gaps
5. **Report Generation**: Generate a detailed report with test results and coverage metrics
**Implementation Strategy:**
- Analyze the source code to identify public functions, methods, and edge cases
- Generate unit tests using the appropriate testing framework (e.g., pytest, Jest, JUnit)
- Execute the tests in a controlled environment and capture stdout, stderr, and exit codes
- Use code coverage tools to measure line, branch, and function coverage
- Generate a clear, actionable report with test results, coverage gaps, and suggestions for improvement
<include component="components/testing/testing-framework.md" />
<include component="components/analysis/codebase-discovery.md" />
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
      <component>components/testing/testing-framework.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>testing.unit.framework</value>
      <value>testing.coverage.threshold</value>
    </uses_config_values>
  </dependencies>
</command_file>
