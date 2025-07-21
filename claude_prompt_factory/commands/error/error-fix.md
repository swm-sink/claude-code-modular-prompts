<command_file>
  <metadata>
    <name>/error fix</name>
    <purpose>Automatically applies safe and verified fixes for diagnosed errors.</purpose>
    <usage>
      <![CDATA[
      /error fix "[error_message_or_log_file]" <dry_run=false>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="error_context" type="string" required="true">
      <description>The full error message, stack trace, or path to a log file containing the error to be fixed.</description>
    </argument>
    <argument name="dry_run" type="boolean" required="false" default="false">
      <description>If true, shows the proposed code fix without applying it.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Automatically diagnose and propose a fix for a given error.</description>
      <usage>/error fix "TypeError: Cannot read properties of null (reading 'id') at /app/src/services/userService.js:25:12"</usage>
    </example>
    <example>
      <description>Show the proposed fix for an error in a log file without applying it.</description>
      <usage>/error fix "logs/production-error.log" dry_run=true</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are an automated error correction system. The user wants you to diagnose and fix an error.

      1.  **Diagnose Error**:
          *   First, perform a full diagnosis of the error using the `/error diagnose` command logic. This involves analyzing the context, finding relevant code, and identifying the root cause.
          *   <include component="components/context/find-relevant-code.md" />

      2.  **Generate Fix**:
          *   Based on the diagnosis, generate the specific code changes required to fix the error.

      3.  **Propose Fix**:
          *   Present the proposed code changes to the user.
          *   If `dry_run` is true, stop here.

      4.  **Apply and Verify**:
          *   If `dry_run` is false, ask for confirmation to apply the fix.
          *   <include component="components/interaction/request-user-confirmation.md" />
          *   On confirmation, apply the changes.
          *   <include component="components/actions/apply-code-changes.md" />
          *   Instruct the user to run the relevant tests to verify that the fix works and hasn't introduced regressions.
    </prompt>
  </claude_prompt>

  <dependencies>
    <chain>
      <command>/error diagnose</command>
      <command>/test unit</command>
    </chain>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>