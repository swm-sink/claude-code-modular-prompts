---
name: /cd-rollback
description: "[DEPRECATED] Advanced CD rollback with intelligent recovery, automated health checks, and zero-downtime restoration - use /project rollback instead"
argument-hint: "[rollback_strategy] [recovery_scope]"
allowed-tools: Read, Write, Edit, Bash, Grep
test_coverage: 0%
# DEPRECATION METADATA
deprecated: true
deprecated_date: "2025-07-25"
replacement_command: "/project rollback"
reason: "Consolidated into unified /project command for integrated rollback operations and project management"
removal_date: "2025-08-25"
---
# ⚠️ DEPRECATED: /cd-rollback

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Please use `/project rollback` instead:**
```
# Old command:
/cd rollback "v1.2.3"

# New command:
/project rollback --version "v1.2.3"
```

The new unified `/project` command provides:
- ✅ All legacy rollback functionality in rollback mode
- ✅ Enhanced integration with deployment workflows and progress tracking
- ✅ Improved version management and risk assessment capabilities
- ✅ Better data integrity checks and recovery procedures
- ✅ Unified incident reporting and post-rollback validation

---

# /deploy cd-rollback - Advanced CD Rollback [DEPRECATED]

Sophisticated CD rollback system with intelligent recovery, automated health checks, and zero-downtime restoration capabilities.
## Migration to `/pipeline rollback`

### Old Usage → New Usage
```bash
# OLD: /deploy cd-rollback immediate
# NEW: 
/pipeline rollback "v1.2.3" --immediate

# OLD: /deploy cd-rollback --health-check
# NEW:
/pipeline rollback --health-check

# OLD: /deploy cd-rollback --zero-downtime
# NEW:
/pipeline rollback --zero-downtime

# OLD: /deploy cd-rollback --comprehensive
# NEW:
/pipeline rollback --comprehensive
```

## Legacy Usage (Deprecated)
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
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <!-- Command-specific components -->
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      You are a deployment manager. The user wants to perform a rollback, which is a high-risk operation.
      1.  **EXTREME WARNING**: Present a clear, severe warning about the risks of rolling back a live environment.
      2.  **Request Confirmation**: Require explicit user confirmation to proceed.
      3.  **On Confirmation**:
          *   **Read Configuration**: Read `project-config.yaml` to determine the deployment platform (e.g., Kubernetes, Docker Swarm, Serverless).
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