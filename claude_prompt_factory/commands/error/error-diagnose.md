---
description: AI-powered error diagnosis to identify root causes and provide intelligent remediation paths
argument-hint: "[error_message_or_log_file]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /error diagnose - Intelligent Error Diagnosis

Advanced error diagnosis system with AI-powered root cause analysis, pattern recognition, and automated remediation suggestions.

## Usage
```bash
/error diagnose "NullPointerException at line 42"    # Diagnose specific error message
/error diagnose logs/error.log                       # Analyze error log file
/error diagnose --interactive                        # Interactive diagnosis session
/error diagnose --severity critical                  # Focus on critical errors only
```

<command_file>
  <metadata>
    <n>/error diagnose</n>
    <purpose>AI-powered error diagnosis to identify root causes and provide intelligent remediation paths</purpose>
    <usage>
      <![CDATA[
      /error diagnose "[error_context]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="error_context" type="string" required="true">
      <description>The full error message, stack trace, or path to a log file containing the error.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Diagnose a null pointer exception from a pasted error message.</description>
      <usage>/error diagnose "TypeError: Cannot read properties of null (reading 'id') at /app/src/services/userService.js:25:12"</usage>
    </example>
    <example>
      <description>Diagnose an error from a log file.</description>
      <usage>/error diagnose "logs/production-error.log"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an error analysis expert. The user has provided an error context and needs a root cause diagnosis.

**Diagnosis Process:**
1. **Analyze Context**: If the input is a file path, read the file. Parse the error message, stack trace, and any other available information.
2. **Find Relevant Code**: Based on the file paths and line numbers in the stack trace, find the relevant code sections.
3. **Identify Root Cause**: Analyze the error in the context of the code to determine the most likely root cause. Consider things like null values, incorrect types, race conditions, or logic errors.
4. **Generate Diagnosis Report**: Provide a clear, concise explanation of the root cause. Assess the potential impact of the error. Offer actionable recommendations for a fix.

<include component="components/analysis/codebase-discovery.md" />
<include component="components/context/find-relevant-code.md" />
<include component="components/error/circuit-breaker.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/context/find-relevant-code.md</component>
      <component>components/error/circuit-breaker.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>