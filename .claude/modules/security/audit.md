| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-07   | stable |

# Security Audit Module

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="security_audit" category="security">
  
  <purpose>
    Comprehensive security auditing patterns for enterprise-grade code review and vulnerability assessment with compliance verification.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Security audit requests, code review with security focus, compliance verification</condition>
    <condition type="explicit">User requests security assessment, vulnerability analysis, or compliance audit</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="automated_scanning" order="1">
      <requirements>
        Multi-tool security analysis covering static analysis, dependency vulnerabilities, and secret detection
        Comprehensive scan results with categorized findings and risk assessment
        Integration with security compliance frameworks and standards
      </requirements>
      <actions>
        Execute static security analysis using bandit for Python, semgrep for multi-language
        Perform dependency vulnerability scanning with safety, npm audit, or snyk
        Scan for exposed secrets, API keys, and sensitive data using truffleHog or detect-secrets
        Analyze container security if applicable using trivy or clair scanning
      </actions>
      <validation>
        All security scanning tools executed successfully with comprehensive results
        Findings categorized by severity and mapped to security frameworks
        No critical vulnerabilities present or properly documented for acceptance
      </validation>
    </phase>
    
    <phase name="threat_model_analysis" order="2">
      <requirements>
        Attack vectors and entry points systematically identified
        Data flow security analysis completed with trust boundaries defined
        Authentication and authorization mechanisms thoroughly reviewed
      </requirements>
      <actions>
        Map application attack surface including entry points and data flows
        Analyze authentication mechanisms for strength and implementation security
        Review authorization patterns for privilege escalation and access control bypass
        Assess input validation and data sanitization across all user inputs
        Evaluate encryption implementation and secrets management practices
      </actions>
      <validation>
        Threat model documents all significant attack vectors and mitigations
        Authentication and authorization review identifies security gaps
        Input validation assessment covers all user-controlled data entry points
      </validation>
    </phase>
    
    <phase name="compliance_verification" order="3">
      <requirements>
        Compliance requirements verified against applicable standards
        Security controls implementation validated through testing
        Audit trail and documentation prepared for regulatory review
      </requirements>
      <actions>
        Verify PCI DSS compliance for payment processing systems
        Validate SOX compliance for financial reporting systems
        Assess GDPR compliance for data privacy and user rights
        Review HIPAA compliance for healthcare data protection if applicable
        Document security control implementation and testing evidence
      </actions>
      <validation>
        All applicable compliance requirements verified with evidence
        Security controls tested and documented with audit trail
        Non-compliance issues identified with remediation recommendations
      </validation>
    </phase>
    
  </implementation>
  
  <scanning_tools>
    <static_analysis>
      <bandit>Python-specific security issue identification with OWASP coverage</bandit>
      <semgrep>Multi-language security pattern detection with custom rules</semgrep>
      <codeql>Deep semantic analysis for complex security vulnerabilities</codeql>
      <sonarqube>Comprehensive code quality and security analysis platform</sonarqube>
    </static_analysis>
    <dependency_scanning>
      <safety>Python package vulnerability database checking</safety>
      <npm_audit>Node.js dependency vulnerability assessment</npm_audit>
      <snyk>Multi-language dependency and container vulnerability scanning</snyk>
      <owasp_dependency_check>OWASP dependency vulnerability identification</owasp_dependency_check>
    </dependency_scanning>
    <secret_detection>
      <trufflehog>Git repository secret scanning with entropy detection</trufflehog>
      <detect_secrets>Pre-commit secret detection with baseline management</detect_secrets>
      <gitleaks>Fast Git repository secret scanning</gitleaks>
    </secret_detection>
  </scanning_tools>
  
  <vulnerability_categories>
    <authentication_authorization>
      <scope>Session management, token validation, privilege escalation, access control bypass</scope>
      <assessment>Review authentication mechanisms, session handling, authorization implementation</assessment>
      <standards>OWASP authentication guidelines, OAuth 2.0 security best practices</standards>
    </authentication_authorization>
    <input_validation>
      <scope>SQL injection, XSS, CSRF protection, command injection, path traversal</scope>
      <assessment>Input sanitization, output encoding, parameterized queries, validation logic</assessment>
      <standards>OWASP Input Validation Cheat Sheet, secure coding guidelines</standards>
    </input_validation>
    <cryptography>
      <scope>Encryption standards, key management, random number generation, hashing</scope>
      <assessment>Cryptographic algorithm selection, key storage, certificate management</assessment>
      <standards>NIST cryptographic standards, industry best practices</standards>
    </cryptography>
    <infrastructure>
      <scope>Container security, network policies, configuration management, secrets</scope>
      <assessment>Container image scanning, network segmentation, secure configuration</assessment>
      <standards>CIS benchmarks, container security best practices</standards>
    </infrastructure>
    <data_protection>
      <scope>PII handling, data retention, privacy controls, sensitive data exposure</scope>
      <assessment>Data classification, encryption implementation, access logging</assessment>
      <standards>GDPR requirements, data protection regulations</standards>
    </data_protection>
  </vulnerability_categories>
  
  <compliance_frameworks>
    <pci_dss>
      <scope>Payment card industry data security standards</scope>
      <requirements>Secure network, cardholder data protection, vulnerability management, access control</requirements>
      <assessment>No card storage verification, encrypted transmission, network segmentation</assessment>
    </pci_dss>
    <sox>
      <scope>Sarbanes-Oxley financial reporting controls</scope>
      <requirements>Financial data integrity, audit trails, change management, access controls</requirements>
      <assessment>Financial system controls, audit logging, segregation of duties</assessment>
    </sox>
    <gdpr>
      <scope>General Data Protection Regulation privacy requirements</scope>
      <requirements>Data protection principles, user rights, privacy by design, consent management</requirements>
      <assessment>Privacy impact assessment, data subject rights implementation</assessment>
    </gdpr>
    <hipaa>
      <scope>Healthcare data protection requirements</scope>
      <requirements>PHI protection, access controls, audit logging, encryption, breach procedures</requirements>
      <assessment>Healthcare data handling, access controls, audit trail implementation</assessment>
    </hipaa>
  </compliance_frameworks>
  
  <financial_grade_standards>
    <zero_trust_architecture>Verify every access request regardless of source location or user credentials</zero_trust_architecture>
    <defense_in_depth>Multiple security layers with redundant controls and monitoring</defense_in_depth>
    <least_privilege>Minimum necessary access rights with regular access reviews</least_privilege>
    <secure_by_default>Default configurations prioritize security over convenience</secure_by_default>
    <continuous_monitoring>Real-time security monitoring with automated threat detection</continuous_monitoring>
  </financial_grade_standards>
  
  <audit_reporting>
    <executive_summary>
      <risk_overview>High-level security posture assessment with key risks highlighted</risk_overview>
      <compliance_status>Compliance framework adherence with gaps identified</compliance_status>
      <recommendations>Prioritized remediation recommendations with business impact</recommendations>
    </executive_summary>
    <technical_findings>
      <vulnerability_details>Detailed vulnerability descriptions with proof of concept</vulnerability_details>
      <risk_ratings>CVSS scoring with environmental and temporal factors</risk_ratings>
      <remediation_guidance>Specific remediation steps with implementation timelines</remediation_guidance>
    </technical_findings>
    <compliance_assessment>
      <framework_mapping>Findings mapped to applicable compliance requirements</framework_mapping>
      <control_effectiveness>Security control implementation and effectiveness assessment</control_effectiveness>
      <audit_evidence>Documentation and testing evidence for regulatory review</audit_evidence>
    </compliance_assessment>
  </audit_reporting>
  
  <session_integration>
    <audit_tracking>
      <session_creation>Automatic GitHub issue creation for security audit tracking</session_creation>
      <documentation>Security audit checklist, findings categorization, risk assessment</documentation>
      <compliance_status>Compliance framework adherence tracking with remediation progress</compliance_status>
      <follow_up>Remediation task tracking with deadline management and escalation</follow_up>
    </audit_tracking>
    <audit_lifecycle>
      <initiation>Scope definition, tool configuration, baseline establishment</initiation>
      <execution>Scanning, analysis, manual review, compliance verification</execution>
      <reporting>Findings documentation, risk assessment, recommendations</reporting>
      <remediation>Tracking fix implementation, re-testing, closure verification</remediation>
    </audit_lifecycle>
  </session_integration>
  
  <integration_points>
    <depends_on>
      patterns/tool-usage.md for efficient security scanning automation
      quality/production-standards.md for enterprise security standards
    </depends_on>
    <provides_to>
      security/threat-modeling.md for threat analysis integration
      security/financial-compliance.md for compliance verification
      All commands for comprehensive security assessment capabilities
    </provides_to>
  </integration_points>
  
</module>
```