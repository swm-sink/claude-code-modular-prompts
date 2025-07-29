---
name: /secure-assess
description: "Comprehensive security assessment with vulnerability scanning, threat analysis, compliance validation, and automated remediation"
argument-hint: "[mode] [scope] [format]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /secure-assess - Comprehensive Security Assessment for [INSERT_PROJECT_NAME]

Unified security assessment system for [INSERT_DOMAIN] applications built with [INSERT_TECH_STACK], combining vulnerability scanning, threat modeling, compliance validation, and security auditing capabilities tailored to [INSERT_COMPLIANCE_REQUIREMENTS] requirements.

## Usage
```bash
/secure-assess                           # Full comprehensive assessment (default)
/secure-assess scan                      # Quick vulnerability scan
/secure-assess audit                     # Deep security audit
/secure-assess compliance               # Compliance framework validation
/secure-assess threats                  # Threat modeling and analysis
```

<command_file>
  <metadata>
    <name>/secure-assess</name>
    <purpose>Comprehensive security assessment with vulnerability scanning, threat analysis, compliance validation, and automated remediation</purpose>
    <usage>
      <![CDATA[
      /secure-assess [mode] [scope] [format]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="mode" type="string" required="false" default="full">
      <description>Assessment mode: full, scan, audit, compliance, threats</description>
    </argument>
    <argument name="scope" type="string" required="false" default="all">
      <description>Assessment scope: all, code, dependencies, secrets, infrastructure</description>
    </argument>
    <argument name="format" type="string" required="false" default="structured">
      <description>Output format: structured, json, compliance-report</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Comprehensive security assessment</description>
      <usage>/secure-assess</usage>
    </example>
    <example>
      <description>Quick vulnerability scan</description>
      <usage>/secure-assess scan</usage>
    </example>
    <example>
      <description>Deep security audit with OWASP compliance</description>
      <usage>/secure-assess audit owasp</usage>
    </example>
    <example>
      <description>Compliance validation only</description>
      <usage>/secure-assess compliance all compliance-report</usage>
    </example>
    <example>
      <description>Threat modeling for infrastructure</description>
      <usage>/secure-assess threats infrastructure</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>
      
      <!-- Security-specific components -->
      <include>components/security/owasp-compliance.md</include>
      <include>components/security/credential-protection.md</include>
      <include>components/security/protection-feedback.md</include>
      <include>components/constitutional/safety-framework.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/context/find-relevant-code.md</include>

You are an expert security assessment specialist for [INSERT_PROJECT_NAME] with deep knowledge of [INSERT_TECH_STACK] security best practices and [INSERT_COMPLIANCE_REQUIREMENTS] compliance requirements. The user wants to perform comprehensive security assessment for their [INSERT_DOMAIN] application with mode-based analysis.

**Assessment Modes:**

**1. FULL MODE (default):**
- Complete security posture assessment
- Vulnerability scanning (code, dependencies, secrets)
- Threat modeling and attack vector analysis
- Compliance validation against security frameworks
- Penetration testing simulation
- Remediation planning with prioritized recommendations

**2. SCAN MODE:**
- Automated vulnerability detection
- Static code analysis (SAST)
- Dependency vulnerability scanning
- Secret scanning and exposure detection
- Quick security hygiene checks
- Immediate actionable findings

**3. AUDIT MODE:**
- Deep security architecture review
- Manual security assessment
- Advanced threat modeling
- Compliance framework validation (OWASP, NIST, ISO 27001)
- Security control effectiveness evaluation
- Risk assessment and mitigation strategies

**4. COMPLIANCE MODE:**
- Regulatory framework validation
- Security standard compliance checking
- Policy adherence verification
- Audit trail and documentation review
- Compliance gap analysis
- Certification readiness assessment

**5. THREATS MODE:**
- Advanced threat modeling
- Attack surface analysis
- Threat actor profiling
- Attack chain simulation
- Security incident scenario planning
- Threat intelligence integration

**Implementation Strategy:**

1. **Initialize Assessment**: Determine mode, scope, and configure tools
2. **Discover Assets**: Map codebase, dependencies, and infrastructure
3. **Execute Assessment**: Run mode-specific security analysis
4. **Analyze Findings**: Correlate results and assess risk levels
5. **Generate Report**: Create comprehensive security assessment report
6. **Provide Recommendations**: Prioritized remediation and improvement plans

**Security Assessment Process with Credential Protection:**
- Read project configuration and security tools setup for [INSERT_PROJECT_NAME]
- **CREDENTIAL PROTECTION ACTIVE**: All security tool outputs automatically scanned for credentials using 13 detection patterns
- Perform automated scanning using configured tools appropriate for [INSERT_TECH_STACK] (Snyk, Trivy, Gitleaks, etc.)
- **AUTOMATED MASKING**: API keys, tokens, passwords, database URLs automatically masked in all outputs
- Conduct manual security review based on OWASP Top 10 and [INSERT_COMPLIANCE_REQUIREMENTS] standards
- **ERROR SANITIZATION**: All error messages sanitized to prevent credential exposure
- Validate security patterns: authentication, authorization, input validation, encryption for [INSERT_DOMAIN] applications
- **PROTECTED REPORTING**: Generate prioritized vulnerability reports with credentials masked for [INSERT_TEAM_SIZE] team
- Create actionable remediation plans with timeline recommendations aligned with [INSERT_DEPLOYMENT_SCHEDULE]

**Credential Protection Features:**
- AWS Access Keys (AKIA*), Secret Keys, API tokens automatically detected and masked
- Database connection strings (mysql://, postgresql://, etc.) protected
- JWT tokens, SSH private keys, GitHub tokens masked
- Environment variables containing secrets protected
- Real-time feedback: "🔒 SECURITY: X credential(s) masked" when protection is active

**Output Formats:**
- **structured**: Human-readable comprehensive report
- **json**: Machine-readable JSON format for CI/CD integration
- **compliance-report**: Formal compliance documentation format
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      
      <!-- Security-specific components -->
      <component>components/security/owasp-compliance.md</component>
      <component>components/security/credential-protection.md</component>
      <component>components/constitutional/safety-framework.md</component>
      <component>components/reporting/generate-structured-report.md</component>
      <component>components/context/find-relevant-code.md</component>
    </includes_components>
    <uses_config_values>
      <value>security.audit.depth</value>
      <value>compliance.frameworks.required</value>
      <value>security.sast_tool</value>
      <value>security.dependency_scanner</value>
      <value>security.secret_scanner</value>
      <value>paths.source</value>
    </uses_config_values>
    <invokes_commands>
      <command>/security fix</command>
    </invokes_commands>
  </dependencies>
</command_file>