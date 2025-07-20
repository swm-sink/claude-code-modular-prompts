# /dev test - Test Execution Command

**Purpose**: Execute a test suite, with support for filtering, coverage reporting, and failure analysis.

## Usage
```bash
/dev test [pattern]
```

## Workflow

The `/dev test` command follows a systematic process to execute a test suite.

```xml
<test_execution_workflow>
  <step name="Detect Test Framework">
    <description>Detect the testing framework (e.g., pytest, Jest, JUnit) in use by analyzing the project's configuration and dependencies.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read project configuration files to identify the testing framework.</description>
    </tool_usage>
  </step>
  
  <step name="Execute Test Suite">
    <description>Execute the test suite, applying any user-provided filters or patterns. The command will capture the results, timing, and coverage data.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the project's configured test command.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Failures & Generate Report">
    <description>If any tests have failed, analyze the failures and provide suggestions for how to fix them. Generate a final report with a summary of the test run, including pass/fail counts, coverage, and any suggestions for improvement.</description>
    <output>A comprehensive test execution report.</output>
  </step>
</test_execution_workflow>
```

## Output Format
```
🧪 TEST EXECUTION RESULTS

Framework: [detected framework]
Pattern: [filter applied]
Duration: [execution time]

✅ Passed: [count]
❌ Failed: [count]  
⚠️ Skipped: [count]
📊 Coverage: [percentage]%

Failed Tests:
• [test name]: [failure reason]
• [test name]: [failure reason]

Suggestions:
- [improvement recommendation]
- [fix suggestion]
```