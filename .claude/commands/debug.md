---
description: Performs advanced AI-assisted debugging to diagnose and fix issues
argument-hint: "[issue_description] [interactive]"
allowed-tools: Read, Grep, Edit, Bash
---

# /debug - AI-Assisted Debugging

Performs an advanced, AI-assisted debugging session to diagnose and fix issues.

## Usage
```bash
/debug "Users can't log in; page just refreshes"        # Automatic debugging
/debug "Undefined error in Cart.js" interactive=true    # Interactive session
```

## Arguments
- `issue_description` (required): Detailed description of the bug or issue
- `interactive` (optional): Enables step-by-step interactive debugging (default: false)

<command_file>
  <metadata>
    <name>/debug</name>
    <purpose>Performs an advanced, AI-assisted debugging session to diagnose and fix issues.</purpose>
    <usage>
      <![CDATA[
      /debug "[issue_description]" <interactive=false>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="issue_description" type="string" required="true">
      <description>A detailed description of the bug or issue to be debugged.</description>
    </argument>
    <argument name="interactive" type="boolean" required="false" default="false">
      <description>If true, conducts a step-by-step interactive debugging session.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Automatically debug an issue with user logins.</description>
      <usage>/debug "Users are unable to log in; the login page just refreshes with no error."</usage>
    </example>
    <example>
      <description>Start an interactive debugging session for a specific error.</description>
      <usage>/debug "Getting 'undefined is not a function' in Cart.js on line 42" interactive=true</usage>
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
      <include>components/context/find-relevant-code.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/actions/apply-code-changes.md</include>
      <include>components/workflow/report-generation.md</include>
      
      <![CDATA[
You are an expert debugger. The user needs help diagnosing and fixing an issue.

      1.  **Gather Context**:
          *   Use context and discovery components to understand the relevant code

      2.  **Analyze & Hypothesize**:
          *   Based on the issue description and relevant code, form a set of likely hypotheses for the root cause.
          *   Apply error handling patterns to identify potential failure points
      
      3.  **Create Debugging Plan**:
          *   Create a step-by-step plan to test each hypothesis. This could involve suggesting `console.log` placements, asking the user to set breakpoints, or analyzing execution flow.

      4.  **Interactive Debugging**:
          *   If `interactive` is true, guide the user through the plan step-by-step, analyzing the output at each stage.

      5.  **Propose Solution**:
          *   Once the root cause is confirmed, provide a clear explanation and the exact code changes needed to fix the bug.
]]>
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
      <component>components/workflow/report-generation.md</component>
    </includes_components>
  </dependencies>
</command_file>