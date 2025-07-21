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
      You are an expert debugger. The user needs help diagnosing and fixing an issue.

      1.  **Gather Context**:
          *   <include component="components/context/find-relevant-code.md" />
      2.  **Analyze & Hypothesize**:
          *   Based on the issue description and relevant code, form a set of likely hypotheses for the root cause.
      3.  **Create Debugging Plan**:
          *   Create a step-by-step plan to test each hypothesis. This could involve suggesting `console.log` placements, asking the user to set breakpoints, or analyzing execution flow.
          *   <include component="components/planning/create-step-by-step-plan.md" />
      4.  **Interactive Debugging**:
          *   If `interactive` is true, guide the user through the plan step-by-step, analyzing the output at each stage.
          *   <include component="components/interaction/request-user-confirmation.md" />
      5.  **Propose Solution**:
          *   Once the root cause is confirmed, provide a clear explanation and the exact code changes needed to fix the bug.
          *   <include component="components/actions/apply-code-changes.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>