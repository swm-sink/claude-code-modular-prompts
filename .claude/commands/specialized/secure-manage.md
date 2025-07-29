---
name: /secure-manage
description: "Unified security management system with configuration, fixing, reporting, and hardening capabilities"
usage: "[mode] [scope] [format]"
tools: Read, Write, Edit, Bash, Grep
---

# /secure-manage - Unified Security Management

Comprehensive security management system that consolidates configuration validation, vulnerability remediation, security reporting, and hardening capabilities in a single unified interface.

## Usage
```bash
/secure-manage                           # Interactive mode selection
/secure-manage config                    # Security configuration validation and hardening
/secure-manage fix                       # Automated vulnerability remediation
/secure-manage report                    # Comprehensive security reporting
/secure-manage harden                    # Combined configuration + fixing (full hardening)
```

<command_file>
  <metadata>
    <name>/secure-manage</name>
    <purpose>Unified security management system with configuration, fixing, reporting, and hardening capabilities</purpose>
    <usage>
      <![CDATA[
      /secure-manage [mode] [scope] [format]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="mode" type="string" required="false" default="interactive">
      <description>Management mode: config, fix, report, harden, interactive</description>
    </argument>
    <argument name="scope" type="string" required="false" default="all">
      <description>Scope of operation: all, vulnerabilities, compliance, dependencies, configuration</description>
    </argument>
    <argument name="format" type="string" required="false" default="structured">
      <description>Output format: structured, json, compliance-report, executive</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Interactive mode selection</description>
      <usage>/secure-manage</usage>
    </example>
    <example>
      <description>Security configuration validation and hardening</description>
      <usage>/secure-manage config</usage>
    </example>
    <example>
      <description>Fix specific vulnerability with validation</description>
      <usage>/secure-manage fix vulnerabilities</usage>
    </example>
    <example>
      <description>Generate comprehensive security report</description>
      <usage>/secure-manage report all executive</usage>
    </example>
    <example>
      <description>Full security hardening (config + fix)</description>
      <usage>/secure-manage harden</usage>
    </example>
    <example>
      <description>HIPAA compliance configuration</description>
      <usage>/secure-manage config compliance structured</usage>
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
      <include>components/constitutional/safety-framework.md</include>
      <include>components/reporting/generate-structured-report.md</include>
      <include>components/context/find-relevant-code.md</include>
      
      <!-- Management-specific components -->
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/actions/apply-code-changes.md</include>

You are an expert security management specialist. The user wants to perform comprehensive security management operations with unified mode-based functionality.

**Management Modes:**

**1. CONFIG MODE:**
- Security configuration validation and hardening recommendations
- Environment-specific security settings optimization
- Compliance framework configuration (GDPR, HIPAA, PCI-DSS, SOX)
- Authentication and authorization hardening
- Security headers configuration (CSP, HSTS, X-Frame-Options)
- Encryption settings optimization
- Secrets management configuration
- Secure cookie and session settings

**2. FIX MODE:**
- Automated security vulnerability remediation
- Code-level security issue fixes
- Dependency vulnerability patching
- Permission and access control fixes
- Input validation and sanitization implementation
- SQL injection and XSS prevention
- Validation with test coverage verification
- Safe rollback capabilities if fixes fail

**3. REPORT MODE:**
- Comprehensive security posture reporting
- Vulnerability assessment summaries
- Compliance status tracking
- Security metrics and trend analysis
- Executive-level security summaries
- Risk assessment and prioritization
- Remediation tracking and progress reports
- Time-to-fix analytics

**4. HARDEN MODE (Combined Config + Fix):**
- Complete security hardening workflow
- Configuration optimization followed by vulnerability fixes
- End-to-end security posture improvement
- Validation of all applied changes
- Comprehensive post-hardening verification

**5. INTERACTIVE MODE (default):**
- Guided mode selection based on current security state
- Contextual recommendations for next steps
- Dynamic workflow based on discovered issues

**Implementation Strategy:**

**For CONFIG mode:**
1. **Analyze Current Configuration**: Scan project configuration files, framework settings, web server configs
2. **Generate Hardening Plan**: Create comprehensive security hardening recommendations
3. **Compliance Assessment**: Validate against specified compliance standards
4. **Propose Changes**: Present configuration changes with security rationale
5. **Apply and Verify**: Implement changes with validation

**For FIX mode:**
1. **Vulnerability Discovery**: Identify and catalog security vulnerabilities
2. **Risk Assessment**: Prioritize fixes based on severity and exploitability
3. **Generate Fixes**: Develop secure remediation patches
4. **Test Coverage**: Ensure adequate testing of security fixes
5. **Apply with Rollback**: Implement fixes with safe rollback capability
6. **Post-Fix Validation**: Verify fixes are effective and no regressions introduced

**For REPORT mode:**
1. **Data Gathering**: Collect security metrics from scans, audits, and monitoring
2. **Trend Analysis**: Analyze security posture changes over time
3. **Risk Calculation**: Compute current risk scores and exposure levels
4. **Compliance Status**: Assess adherence to security frameworks
5. **Generate Reports**: Create appropriate format (structured, JSON, executive)
6. **Actionable Recommendations**: Provide prioritized next steps

**For HARDEN mode:**
1. **Security Assessment**: Complete current state analysis
2. **Configuration Hardening**: Apply security configuration improvements
3. **Vulnerability Remediation**: Fix identified security issues
4. **Validation Testing**: Comprehensive security testing post-changes
5. **Documentation**: Update security documentation and procedures

**Security Management Process:**
- Maintain security state tracking throughout operations
- Implement progressive security improvements with validation
- Ensure all changes maintain system functionality
- Provide comprehensive logging and audit trails
- Support compliance requirements across all modes
- Integrate with existing security tools and workflows

**Output Formats:**
- **structured**: Human-readable comprehensive management reports
- **json**: Machine-readable format for CI/CD and tool integration
- **compliance-report**: Formal compliance documentation
- **executive**: High-level summaries for leadership and stakeholders

**Rollback and Safety:**
- All fix operations include automatic backup creation
- Rollback procedures documented and tested
- Change validation before permanent application
- Progressive deployment with checkpoints
- Failure recovery and incident response procedures
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
      <component>components/constitutional/safety-framework.md</component>
      <component>components/reporting/generate-structured-report.md</component>
      <component>components/context/find-relevant-code.md</component>
      
      <!-- Management-specific components -->
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
    <uses_config_values>
      <value>security.audit.depth</value>
      <value>compliance.frameworks.required</value>
      <value>security.sast_tool</value>
      <value>security.dependency_scanner</value>
      <value>security.secret_scanner</value>
      <value>security.scanning_service</value>
      <value>security.monitoring_service</value>
      <value>paths.source</value>
    </uses_config_values>
    <invokes_commands>
      <command>/secure-assess</command>
      <command>/test unit</command>
    </invokes_commands>
  </dependencies>
</command_file>