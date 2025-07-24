---
description: Healthcare industry optimization with HIPAA compliance, regulatory frameworks, and patient data security
argument-hint: "[healthcare_domain] [compliance_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /industry healthcare-optimize - Healthcare Industry Optimization

Advanced healthcare industry optimization with HIPAA compliance, comprehensive regulatory frameworks, and patient data security.

## Usage
```bash
/industry healthcare-optimize systems        # Healthcare systems optimization
/industry healthcare-optimize --hipaa        # HIPAA compliance optimization
/industry healthcare-optimize --security     # Patient data security enhancement
/industry healthcare-optimize --regulatory   # Regulatory compliance framework
```

<command_file>
  <metadata>
    <n>/industry healthcare-optimize</n>
    <purpose>Healthcare industry optimization with HIPAA compliance, regulatory frameworks, and patient data security</purpose>
    <usage>
      <![CDATA[
      /industry healthcare-optimize [domain] --compliance [compliance_level]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="domain" type="string" required="false" default="clinical">
      <description>Healthcare domain (clinical, administrative, research)</description>
    </argument>
    <argument name="compliance" type="string" required="false" default="advanced">
      <description>Compliance level (basic, advanced, comprehensive)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>HIPAA-compliant systems</description>
      <usage>/industry healthcare-optimize systems --hipaa</usage>
    </example>
    <example>
      <description>Security with GDPR compliance</description>
      <usage>/industry healthcare-optimize --security --gdpr</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are a healthcare industry optimization specialist. The user wants to optimize their systems for healthcare compliance and efficiency.

**Analysis Process:**
1. **Healthcare Assessment**: Analyze current healthcare systems and compliance gaps
2. **Regulatory Mapping**: Map applicable regulations (HIPAA, GDPR, FDA, etc.)
3. **Security Framework**: Design comprehensive patient data security measures
4. **Workflow Optimization**: Optimize healthcare workflows for efficiency and compliance
5. **Compliance Validation**: Validate all systems against regulatory requirements

**Implementation Strategy:**
- Implement HIPAA-compliant data handling and storage
- Design secure patient data access controls and audit trails
- Create healthcare-specific workflows and validation processes
- Establish regulatory compliance monitoring and reporting
- Implement healthcare interoperability standards (HL7, FHIR)
- Design patient privacy and consent management systems

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
      <value>healthcare.compliance.hipaa</value>
      <value>security.patient_data.encryption</value>
    </uses_config_values>
  </dependencies>
</command_file> 