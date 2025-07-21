---
description: Comprehensive error handling patterns with recovery strategies and resilience patterns
argument-hint: "[error_pattern] [recovery_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /error handle - Error Handling & Recovery

Advanced error handling system with comprehensive recovery patterns, circuit breakers, and resilience engineering.

## Usage
```bash
/error handle exceptions                     # Implement exception handling patterns
/error handle async                         # Handle asynchronous error patterns
/error handle resilience                    # Add resilience and circuit breaker patterns
/error handle graceful-degradation          # Implement graceful degradation strategies
```

<command_file>
  <metadata>
    <name>/error handle</name>
    <purpose>Adds comprehensive and robust error handling to code to improve reliability.</purpose>
    <usage>
      <![CDATA[
      /error handle "[file_path]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="file_path" type="string" required="true">
      <description>The path to the file where error handling should be added.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Add robust error handling to a specific service file.</description>
      <usage>/error handle "src/services/paymentService.js"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a software reliability engineer. The user wants to add robust error handling to a file.

      1.  **Analyze Code**:
          *   Read the contents of the specified `file_path`.
          *   Identify critical code paths that lack sufficient error handling (e.g., I/O operations, network requests, parsing, complex logic).

      2.  **Generate Plan**:
          *   Propose a plan to add error handling. This should include:
              *   Wrapping critical sections in `try-catch` blocks.
              *   Implementing specific catch blocks for different error types.
              *   Adding logging for errors.
              *   Defining graceful fallback behavior.
          *   <include component="components/planning/create-step-by-step-plan.md" />

      3.  **Propose Changes**:
          *   Generate the code modifications needed to implement the plan.
          *   Present the changes to the user for confirmation.
          *   <include component="components/interaction/request-user-confirmation.md" />

      4.  **Apply Changes**:
          *   On confirmation, apply the changes to the file.
          *   <include component="components/actions/apply-code-changes.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>

<include component="components/error/circuit-breaker.md" />
<include component="components/workflow/error-handling.md" />
<include component="components/actions/parallel-execution.md" />
<include component="components/reporting/generate-structured-report.md" />