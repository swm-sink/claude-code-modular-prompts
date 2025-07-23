---
name: /secure-config
description: Security configuration validation and hardening recommendations
usage: /secure-config [config_type] [environment]
tools: Read, Write, Edit, Bash, Grep
---

# Security configuration validation and hardening recommendations

**Usage**: `/secure-config $COMPLIANCE`

## Key Arguments

- **$COMPLIANCE** (optional): The compliance standard to configure for (e.g., 'gdpr', 'hipaa', 'pci-dss').

## Examples

```bash
/secure config
```
*Review and suggest baseline security configurations.*

```bash
/secure config compliance="hipaa"
```
*Apply strict security configurations required for HIPAA compliance.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/planning/create-step-by-step-plan.md
 components/interaction/request-user-confirmation.md
 components/actions/apply-code-changes.md
 components/security/hardening-strategies.md
 components/security/secrets-management.md
 
 You are a security architect. The user wants to apply security best-practice configurations to their project.

 1. **Analyze Current Configuration**: Scan the project's configuration files (e.g., framework settings, web server configs) to assess the current security posture.
 2. **Generate Hardening Plan**:
 * Based on security best practices and the specified `compliance` standard, create a plan to harden the configuration.
 * This should include recommendations for:
 * Authentication (e.g., password policies, MFA).
 * Security Headers (e.g., CSP, HSTS).
 * Encryption settings.
 * Secrets management.
 * Secure cookie settings.
 3. **Propose Changes**:
 * Generate the necessary configuration changes and present them for user approval.
 4. **Apply and Verify**:
 * On confirmation, apply the changes.

## Essential Component Logic

### Input Validation

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

