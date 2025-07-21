---
description: Advanced error tracing with stack trace analysis, distributed tracing, and root cause investigation
argument-hint: "[trace_id] [trace_depth]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /error trace - Advanced Error Tracing

Comprehensive error tracing system with stack trace analysis, distributed tracing, and multi-layer investigation.

## Usage
```bash
/error trace 12345                          # Trace specific error by ID
/error trace --stack                        # Analyze current stack trace
/error trace --distributed                  # Distributed tracing analysis
/error trace --deep                         # Deep trace with all call paths
```

<command_file>
  <metadata>
    <name>/error trace</name>
    <purpose>Traces error propagation paths and analyzes error flow to identify root causes.</purpose>
    <usage>
      <![CDATA[
      /error trace "[error_message_or_log_file]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="error_context" type="string" required="true">
      <description>The full error message, stack trace, or path to a log file containing the error to be traced.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Trace the propagation path of a specific error message.</description>
      <usage>/error trace "TypeError: Cannot read properties of null (reading 'id') at /app/src/services/userService.js:25:12"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a system diagnostician. The user wants to trace an error's propagation path through the system.

      1.  **Analyze Context**:
          *   Parse the provided `error_context` to identify the origin point of the error (file, function, line number).
      2.  **Trace Backwards**:
          *   Starting from the error's origin, trace the execution flow backwards.
          *   Identify the sequence of function calls that led to the error state.
          *   Examine how data (especially the data causing the error) was passed between functions.
      3.  **Build Flow Map**:
          *   Construct a map or diagram of the error flow, showing how the error propagated from its root cause to the point where it was reported.
      4.  **Generate Trace Report**:
          *   Generate a report that includes:
              *   A visualization of the error flow (e.g., as a Mermaid sequence diagram).
              *   An identification of the root cause.
              *   Recommendations for where to add more robust error handling to stop the propagation.
          *   <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>monitoring.distributed_tracing_service</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>