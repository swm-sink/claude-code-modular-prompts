---
name: /secure-audit
description: Advanced security audit with comprehensive vulnerability assessment, compliance validation, and threat modeling
argument-hint: "[audit_scope] [compliance_framework]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation-date: 2025-07-25
removal-date: 2025-08-25
replacement: "/secure-assess audit"
---
# /secure audit - Advanced Security Audit

⚠️ **DEPRECATED COMMAND** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/secure-assess audit`

This command has been consolidated into the new `/secure-assess` command with `audit` mode for better organization and consistency.

---

Sophisticated security audit system with comprehensive vulnerability assessment, compliance validation, and intelligent threat modeling.
## Usage
```bash
/secure audit comprehensive                  # Comprehensive security audit
/secure audit --owasp                        # OWASP-focused security audit
/secure audit --compliance                   # Compliance framework audit
/secure audit --penetration                  # Penetration testing audit
```
<command_file>
  <metadata>
    <n>/secure audit</n>
    <purpose>Advanced security audit with comprehensive vulnerability assessment, compliance validation, and threat modeling</purpose>
    <usage>
      <![CDATA[
      /secure audit [audit_scope]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="audit_scope" type="string" required="false" default="comprehensive">
      <description>Scope of security audit to perform</description>
    </argument>
    <argument name="compliance_framework" type="string" required="false" default="owasp">
      <description>Compliance framework to apply</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Comprehensive security audit</description>
      <usage>/secure audit comprehensive</usage>
    </example>
    <example>
      <description>OWASP-focused security audit</description>
      <usage>/secure audit --owasp</usage>
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
      <include>components/security/owasp-compliance.md</include>
      <include>components/constitutional/safety-framework.md</include>
      <include>components/reporting/generate-structured-report.md</include>
You are an advanced security audit specialist. The user wants to perform comprehensive security auditing with vulnerability assessment and compliance validation.
**Audit Process:**
1. **Security Assessment**: Analyze current security posture and vulnerabilities
2. **Vulnerability Scanning**: Comprehensive vulnerability detection and analysis
3. **Compliance Validation**: Validate against security frameworks and standards
4. **Threat Modeling**: Model potential threats and attack vectors
5. **Remediation Planning**: Create prioritized remediation and improvement plans
**Implementation Strategy:**
- Perform automated and manual security vulnerability scanning
- Apply OWASP Top 10 and industry security frameworks
- Conduct penetration testing and security assessments
- Validate compliance with regulatory requirements
- Generate comprehensive security reports with prioritized recommendations
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/security/owasp-compliance.md</component>
      <component>components/constitutional/safety-framework.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>security.audit.depth</value>
      <value>compliance.frameworks.required</value>
    </uses_config_values>
  </dependencies>
</command_file>
