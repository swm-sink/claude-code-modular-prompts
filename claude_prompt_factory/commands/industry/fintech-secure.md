---
description: FinTech industry security with compliance frameworks (PCI-DSS, SOC 2), fraud detection, and transactional integrity
argument-hint: "[fintech_domain] [security_standard]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /industry fintech-secure - FinTech Industry Security

Advanced FinTech industry security with compliance frameworks (PCI-DSS, SOC 2), advanced fraud detection, and transactional integrity systems.

## Usage
```bash
/industry fintech-secure payments          # Payments systems security
/industry fintech-secure --pci-dss         # PCI-DSS compliance framework
/industry fintech-secure --fraud-detection   # Advanced fraud detection systems
/industry fintech-secure --transactional-integrity # Transactional integrity validation
```

<command_file>
  <metadata>
    <n>/industry fintech-secure</n>
    <purpose>FinTech industry security with compliance frameworks (PCI-DSS, SOC 2), fraud detection, and transactional integrity</purpose>
    <usage>
      <![CDATA[
      /industry fintech-secure [domain] --standard [security_standard]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="domain" type="string" required="false" default="payments">
      <description>FinTech domain (payments, banking, investments, insurance)</description>
    </argument>
    <argument name="security_standard" type="string" required="false" default="pci-dss">
      <description>Security standard to comply with (pci-dss, soc_2, iso_27001)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>PCI-DSS compliant payments systems</description>
      <usage>/industry fintech-secure payments --standard pci-dss</usage>
    </example>
    <example>
      <description>Advanced fraud detection for banking</description>
      <usage>/industry fintech-secure banking --fraud-detection</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are a FinTech security specialist. The user wants to secure their systems with industry-specific compliance and fraud detection.

**Security Process:**
1. **FinTech Risk Assessment**: Analyze current systems for financial-specific risks
2. **Compliance Framework Implementation**: Implement relevant compliance frameworks (PCI-DSS, SOC 2, etc.)
3. **Fraud Detection Systems**: Design and integrate advanced fraud detection mechanisms
4. **Transactional Integrity**: Ensure the integrity and security of financial transactions
5. **Security Auditing &amp; Reporting**: Conduct regular security audits and generate compliance reports

**Implementation Strategy:**
- Implement robust compliance controls for standards like PCI-DSS, SOC 2, and ISO 27001
- Design and integrate machine learning-based fraud detection systems for real-time analysis
- Ensure end-to-end encryption and integrity checks for all financial transactions
- Establish continuous security monitoring, logging, and alerting for financial systems
- Conduct regular penetration testing and vulnerability assessments to identify and remediate security weaknesses

<include component="components/security/owasp-compliance.md" />
<include component="components/constitutional/safety-framework.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/security/owasp-compliance.md</component>
      <component>components/constitutional/safety-framework.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>fintech.compliance.standard</value>
      <value>security.fraud_detection.model</value>
    </uses_config_values>
  </dependencies>
</command_file> 