# /error diagnose - Error Diagnosis Command

**Purpose**: Perform AI-powered error diagnosis to identify the root cause of issues with high accuracy.

## Usage
```bash
/error diagnose "[error_message]" [--deep] [--suggest-fix]
```

## Workflow

The `/error diagnose` command follows a systematic process to diagnose errors.

```xml
<error_diagnose_workflow>
  <step name="Capture Error Context">
    <description>Capture the full error context, including the error message, stack trace, relevant code snippets, recent changes, and system state.</description>
    <tool_usage>
      <tool>Bash/Read</tool>
      <description>Extract error information from logs, source files, and version control.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze & Identify Root Cause">
    <description>Apply pattern recognition and causal analysis to identify the root cause of the error. This involves matching against a knowledge base of known error patterns and tracing the execution flow to pinpoint the origin of the issue.</description>
    <tool_usage>
      <tool>AI Analysis</tool>
      <description>Leverage an AI model trained on error patterns to analyze the context and determine the root cause.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Diagnosis & Suggestions">
    <description>Generate a comprehensive diagnosis that includes a clear explanation of the root cause, an assessment of the impact, and actionable recommendations for fixing the issue. If the `--suggest-fix` flag is used, provide a code patch.</description>
    <output>A detailed error diagnosis report.</output>
  </step>
</error_diagnose_workflow>
```

## Configuration

The `/error diagnose` command can be configured through the `PROJECT_CONFIG.xml` file.

```xml
<command name="/error diagnose">
  <setting name="confidence_threshold" value="0.8" description="The minimum confidence level for a diagnosis to be considered valid." />
  <setting name="max_suggestions" value="3" description="The maximum number of fix suggestions to provide." />
</command>
```

## Use Cases

*   **Debugging**: Quickly understand the cause of a complex bug without extensive manual debugging.
*   **Production Support**: Rapidly diagnose and resolve issues in a live environment.
*   **Developer Onboarding**: Help new developers understand and fix common errors in the codebase.