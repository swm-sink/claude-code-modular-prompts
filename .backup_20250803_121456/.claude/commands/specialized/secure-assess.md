---
name: /secure-assess
description: Comprehensive code assessment with pattern analysis, risk analysis, compliance (v1.0)
version: "1.0"
usage: '[mode] [scope] [format]'
category: specialized
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate input parameters and execution context
  during-execution: Monitor progress and maintain safety checks
  post-execution: Verify successful completion and cleanup
progressive-disclosure:
  layer-integration: Integrated command for specialized workflows
  escalation-path: Basic usage → advanced options → full customization
  de-escalation: Simplify to essential functionality
safety-measures:
  - Validate all inputs before execution
  - Create backups when modifying files
  - Confirm destructive operations
  - Maintain system integrity
error-recovery:
  input-error: Provide clear usage examples and syntax
  execution-failure: Show detailed context and recovery steps
  system-error: Fallback to safe mode operation
---

# /secure-assess - Comprehensive Code Assessment for [INSERT_PROJECT_NAME]

Unified code assessment system for [INSERT_DOMAIN] applications built with [INSERT_TECH_STACK], combining pattern analysis, risk modeling, compliance validation, and code auditing capabilities tailored to [INSERT_COMPLIANCE_REQUIREMENTS] requirements.

## Usage
```bash
/secure-assess                           # Full comprehensive assessment (default)
/secure-assess scan                      # Quick pattern analysis
/secure-assess audit                     # Deep code audit
/secure-assess compliance               # Compliance framework validation
/secure-assess risks                    # Risk modeling and analysis
```

<command_file>
  <metadata>
    <name>/secure-assess</name>
    <purpose>Comprehensive code assessment with pattern analysis, risk analysis, compliance validation, and automated improvements</purpose>
    <usage>
      <![CDATA[
      /secure-assess [mode] [scope] [format]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="mode" type="string" required="false" default="full">
      <description>Assessment mode: full, scan, audit, compliance, risks</description>
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
      <description>Comprehensive code assessment</description>
      <usage>/secure-assess</usage>
    </example>
    <example>
      <description>Quick pattern analysis</description>
      <usage>/secure-assess scan</usage>
    </example>
    <example>
      <description>Deep code audit with OWASP patterns</description>
      <usage>/secure-assess audit owasp</usage>
    </example>
    <example>
      <description>Compliance validation only</description>
      <usage>/secure-assess compliance all compliance-report</usage>
    </example>
    <example>
      <description>Risk modeling for infrastructure</description>
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

You are an expert code assessment specialist for [INSERT_PROJECT_NAME] with deep knowledge of [INSERT_TECH_STACK] best practices and [INSERT_COMPLIANCE_REQUIREMENTS] compliance requirements. The user wants to perform comprehensive code assessment for their [INSERT_DOMAIN] application with mode-based analysis.

**Assessment Modes:**

**1. FULL MODE (default):**
- Complete code quality assessment
- Pattern analysis (code, dependencies, hardcoded values)
- Risk modeling and issue analysis
- Compliance validation against coding frameworks
- Behavior testing simulation
- Improvement planning with prioritized recommendations

**2. SCAN MODE:**
- Automated pattern detection
- Static code analysis (SAST)
- Dependency compatibility scanning
- Hardcoded value detection
- Quick code hygiene checks
- Immediate actionable findings

**3. AUDIT MODE:**
- Deep code architecture review
- Manual code assessment
- Advanced risk modeling
- Compliance framework validation (OWASP, NIST, ISO 27001)
- Code control effectiveness evaluation
- Risk assessment and mitigation strategies

**4. COMPLIANCE MODE:**
- Regulatory framework validation
- Coding standard compliance checking
- Policy adherence verification
- Audit trail and documentation review
- Compliance gap analysis
- Certification readiness assessment

**5. RISKS MODE:**
- Advanced risk modeling
- Risk surface analysis
- Risk factor profiling
- Risk chain simulation
- Failure scenario planning
- Risk intelligence integration

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