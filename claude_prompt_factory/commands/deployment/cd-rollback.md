<command_file>
  <metadata>
    <name>/cd rollback</name>
    <purpose>Safely rolls back a deployment to a previous version, with data integrity checks and incident reporting.</purpose>
    <usage>
      <![CDATA[
      /cd rollback <version>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="version" type="string" required="true">
      <description>The specific, valid version or tag to roll back to.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Roll back the current deployment to version 'v1.2.3'.</description>
      <usage>/cd rollback "v1.2.3"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a deployment manager. The user wants to perform a rollback, which is a high-risk operation.

      1.  **EXTREME WARNING**: Present a clear, severe warning about the risks of rolling back a live environment.
      2.  **Request Confirmation**: Require explicit user confirmation to proceed.
          <include component="components/interaction/request-user-confirmation.md" />

      3.  **On Confirmation**:
          *   **Read Configuration**: Read `PROJECT_CONFIG.xml` to determine the deployment platform (e.g., Kubernetes, Docker Swarm, Serverless).
          *   **Validate Target**: Verify that the specified `version` is a valid and available rollback target.
          *   **Generate Rollback Plan**: Propose a rollback plan including:
              *   Pre-rollback steps (e.g., initiating a DB backup with `/db backup`).
              *   The platform-specific rollback command (e.g., `kubectl rollout undo`, `docker service update`).
              *   Post-rollback health check commands.
          *   **Generate Incident Report**: After execution, create a post-mortem incident report.
              <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>deployment.platform</value>
    </uses_config_values>
    <chain>
      <command>/db backup</command>
    </chain>
    <includes_components>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>