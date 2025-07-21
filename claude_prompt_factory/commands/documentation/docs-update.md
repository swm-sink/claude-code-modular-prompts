<command_file>
  <metadata>
    <name>/docs update</name>
    <purpose>Synchronizes documentation with code changes, updating technical details while preserving custom content.</purpose>
    <usage>
      <![CDATA[
      /docs update <target_docs_dir="./docs">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="false" default="./docs">
      <description>The documentation directory to update.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Check for and apply documentation updates in the default 'docs' directory.</description>
      <usage>/docs update</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a documentation synchronization tool. The user wants to update their documentation to reflect the latest code changes.

      1.  **Analyze Code Changes**: Scan the source code to identify recent changes to public APIs, function signatures, class structures, and configuration options.
      2.  **Detect Documentation Drift**: Compare the existing documentation in the `target` directory against the current codebase to find:
          *   Outdated code examples.
          *   Incorrect function/method signatures.
          *   Undocumented features.
      3.  **Generate Intelligent Updates**:
          *   Generate the necessary updates for the documentation.
          *   Be careful to only update the auto-generated parts of the documentation (like API signatures and examples), preserving any custom narrative content written by humans.
      4.  **Propose Changes**: Present the proposed changes to the user in a diff format for them to review and approve.
          <include component="components/interaction/request-user-confirmation.md" />
      5.  **Apply Updates**:
          *   Upon confirmation, apply the changes to the documentation files.
          *   <include component="components/actions/apply-code-changes.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>documentation.source_dir</value>
    </uses_config_values>
    <includes_components>
      <component>components/actions/apply-code-changes.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
    </includes_components>
  </dependencies>
</command_file>