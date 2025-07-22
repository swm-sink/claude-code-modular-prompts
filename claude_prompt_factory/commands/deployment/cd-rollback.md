---
description: Advanced CD rollback with intelligent recovery, automated health checks, and zero-downtime restoration
argument-hint: "[rollback_strategy] [recovery_scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /deploy cd-rollback - Advanced CD Rollback

Sophisticated CD rollback system with intelligent recovery, automated health checks, and zero-downtime restoration capabilities.

## Usage
```bash
/deploy cd-rollback immediate                # Immediate rollback execution
/deploy cd-rollback --health-check           # Health-check driven rollback
/deploy cd-rollback --zero-downtime          # Zero-downtime rollback strategy
/deploy cd-rollback --comprehensive          # Comprehensive recovery protocol
```

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
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/deployment/health-check-automation.md</include>
      <include>components/workflow/rollback-capabilities.md</include>
      <include>components/deployment/zero-downtime-strategies.md</include>
      
      You are a deployment manager. The user wants to perform a rollback, which is a high-risk operation.

      1.  **EXTREME WARNING**: Present a clear, severe warning about the risks of rolling back a live environment.
      2.  **Request Confirmation**: Require explicit user confirmation to proceed.

      3.  **On Confirmation**:
          *   **Read Configuration**: Read `PROJECT_CONFIG.xml` to determine the deployment platform (e.g., Kubernetes, Docker Swarm, Serverless).
          *   **Validate Target**: Verify that the specified `version` is a valid and available rollback target.
          *   **Generate Rollback Plan**: Propose a rollback plan including:
              *   Pre-rollback steps (e.g., initiating a DB backup with `/db backup`).
              *   The platform-specific rollback command (e.g., `kubectl rollout undo`, `docker service update`).
              *   Post-rollback health check commands.
          *   **Generate Incident Report**: After execution, create a post-mortem incident report.
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