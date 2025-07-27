---
name: /deploy
description: Advanced deployment orchestration with intelligent strategies, rollback capabilities, and environment management
argument-hint: "[deployment_target] [strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
removal_date: "2025-08-25"
replacement: "/pipeline deploy"
---
# /deploy - Advanced Deployment Orchestration

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/pipeline deploy`

This standalone command has been consolidated into the unified `/pipeline` command. The new command provides the same functionality with improved consistency and maintainability.

---

Sophisticated deployment orchestration system with intelligent strategies, automated rollback capabilities, and comprehensive environment management.
## Usage
```bash
/deploy production                           # Production deployment
/deploy --blue-green                         # Blue-green deployment strategy
/deploy --canary                             # Canary deployment with monitoring
/deploy --zero-downtime                      # Zero-downtime deployment
```
<command_file>
  <metadata>
    <name>/deploy</name>
    <purpose>Executes a structured, multi-stage deployment pipeline with support for different environments and quality gates.</purpose>
    <usage>
      <![CDATA[
      /deploy <target="staging"> <dry_run=false>
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="target" type="string" required="true" default="staging">
      <description>The deployment environment to target (e.g., 'staging', 'production').</description>
    </argument>
    <argument name="dry_run" type="boolean" required="false" default="false">
      <description>If true, outputs the deployment plan without executing it.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Deploy the current branch to the staging environment.</description>
      <usage>/deploy</usage>
    </example>
    <example>
      <description>Perform a dry run of a deployment to the production environment.</description>
      <usage>/deploy target="production" dry_run=true</usage>
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
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      You are a release engineer executing a deployment pipeline.
      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the deployment configuration for the specified `target` environment. This includes build, test, deploy, and health check commands.
      2.  **Generate Deployment Plan**: Create a step-by-step deployment plan based on the configuration.
      3.  **Dry Run Check**: If `dry_run` is true, present the plan and stop.
      4.  **Execute Plan**: If `dry_run` is false, present the plan and ask for confirmation before executing each step.
          *   **On Failure**: If any step fails, immediately stop and propose running the configured rollback commands.
      5.  **Report Outcome**: After successful execution (or failure), generate a final report.
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>deployment.environments.environment</value>
    </uses_config_values>
    <includes_components>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file> 