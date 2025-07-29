---
name: /secure-config
description: "Configuration validation and best practice recommendations"
argument-hint: "[config_type] [environment]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation-date: 2025-07-25
removal-date: 2025-08-25
replacement: "/secure-manage config"
---
# /secure config - Configuration Validator

⚠️ **DEPRECATED COMMAND** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/secure-manage config`

This command has been consolidated into the new `/secure-manage` command with `config` mode for better organization and consistency.

---

Advanced configuration validator with environment-specific best practices and compliance checking.
## Usage
```bash
/secure config server               # Server configuration validation
/secure config database            # Database configuration review
/secure config web --env production # Web server config for production
```
<command_file>
  <metadata>
    <name>/secure config</name>
    <purpose>Validates and configures comprehensive settings for applications following best practices.</purpose>
    <usage>
      <![CDATA[
      /secure config <compliance_standard="none">
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="compliance" type="string" required="false" default="none">
      <description>The compliance standard to configure for (e.g., 'gdpr', 'hipaa', 'pci-dss').</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Review and suggest baseline configuration improvements.</description>
      <usage>/secure config</usage>
    </example>
    <example>
      <description>Apply strict configurations required for HIPAA compliance.</description>
      <usage>/secure config compliance="hipaa"</usage>
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
      <include>components/actions/apply-code-changes.md</include>
      You are a configuration architect. The user wants to apply best-practice configurations to their project.
      1.  **Analyze Current Configuration**: Review the project's configuration files (e.g., framework settings, web server configs) to assess the current setup.
      2.  **Generate Improvement Plan**:
          *   Based on best practices and the specified `compliance` standard, create a plan to improve the configuration.
          *   This should include recommendations for:
              *   Authentication (e.g., password policies, MFA).
              *   Headers (e.g., CSP, HSTS).
              *   Encryption settings.
              *   Secrets management.
              *   Cookie settings.
      3.  **Propose Changes**:
          *   Generate the necessary configuration changes and present them for user approval.
      4.  **Apply and Verify**:
          *   On confirmation, apply the changes.
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