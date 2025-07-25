---
description: Security configuration validation and hardening recommendations
argument-hint: "[config_type] [environment]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation-date: 2025-07-25
removal-date: 2025-08-25
replacement: "/secure-manage config"
---
# /secure config - Security Configuration Validator

⚠️ **DEPRECATED COMMAND** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/secure-manage config`

This command has been consolidated into the new `/secure-manage` command with `config` mode for better organization and consistency.

---

Advanced configuration security validator with environment-specific hardening and compliance checking.
## Usage
```bash
/secure config server               # Server configuration security check
/secure config database            # Database security configuration
/secure config web --env production # Web server config for production
```
<command_file>
  <metadata>
    <name>/secure config</name>
    <purpose>Configures comprehensive security settings for applications to prevent vulnerabilities.</purpose>
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
      <description>Review and suggest baseline security configurations.</description>
      <usage>/secure config</usage>
    </example>
    <example>
      <description>Apply strict security configurations required for HIPAA compliance.</description>
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
      You are a security architect. The user wants to apply security best-practice configurations to their project.
      1.  **Analyze Current Configuration**: Scan the project's configuration files (e.g., framework settings, web server configs) to assess the current security posture.
      2.  **Generate Hardening Plan**:
          *   Based on security best practices and the specified `compliance` standard, create a plan to harden the configuration.
          *   This should include recommendations for:
              *   Authentication (e.g., password policies, MFA).
              *   Security Headers (e.g., CSP, HSTS).
              *   Encryption settings.
              *   Secrets management.
              *   Secure cookie settings.
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