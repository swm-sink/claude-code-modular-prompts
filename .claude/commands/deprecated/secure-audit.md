---
name: /secure-audit
description: "Advanced code audit with comprehensive quality assessment, compliance validation, and risk analysis"
argument-hint: "[audit_scope] [compliance_framework]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation-date: 2025-07-25
removal-date: 2025-08-25
replacement: "/secure-assess audit"
---
# /secure audit - Advanced Code Audit

⚠️ **DEPRECATED COMMAND** ⚠️

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/secure-assess audit`

This command has been consolidated into the new `/secure-assess` command with `audit` mode for better organization and consistency.

---

Sophisticated code audit system with comprehensive quality assessment, compliance validation, and intelligent risk analysis.
## Usage
```bash
/secure audit comprehensive                  # Comprehensive code audit
/secure audit --standards                    # Standards-focused code audit
/secure audit --compliance                   # Compliance framework audit
/secure audit --analysis                     # Deep code analysis audit
```
<command_file>
  <metadata>
    <n>/secure audit</n>
    <purpose>Advanced code audit with comprehensive quality assessment, compliance validation, and risk analysis</purpose>
    <usage>
      <![CDATA[
      /secure audit [audit_scope]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="audit_scope" type="string" required="false" default="comprehensive">
      <description>Scope of code audit to perform</description>
    </argument>
    <argument name="compliance_framework" type="string" required="false" default="owasp">
      <description>Compliance framework to apply</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Comprehensive code audit</description>
      <usage>/secure audit comprehensive</usage>
    </example>
    <example>
      <description>Standards-focused code audit</description>
      <usage>/secure audit --standards</usage>
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
You are an advanced code audit specialist. The user wants to perform comprehensive code auditing with quality assessment and compliance validation.
**Audit Process:**
1. **Quality Assessment**: Analyze current code quality and potential issues
2. **Pattern Analysis**: Comprehensive pattern detection and code analysis
3. **Compliance Validation**: Validate against coding frameworks and standards
4. **Risk Modeling**: Model potential risks and failure points
5. **Improvement Planning**: Create prioritized improvement and enhancement plans
**Implementation Strategy:**
- Perform automated and manual code quality analysis
- Apply coding standards and industry best practices
- Conduct thorough code review and assessments
- Validate compliance with regulatory requirements
- Generate comprehensive audit reports with prioritized recommendations
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/security/owasp-compliance.md</component>
      <component>components/constitutional/safety-framework.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>audit.depth</value>
      <value>compliance.frameworks.required</value>
    </uses_config_values>
  </dependencies>
</command_file>
