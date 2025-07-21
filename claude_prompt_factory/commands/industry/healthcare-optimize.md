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

## Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `domain` | string | false | Healthcare domain (clinical, administrative, research). Default: clinical. |
| `compliance` | string | false | Compliance level (basic, advanced, comprehensive). Default: advanced. |

## Examples

```bash
/industry healthcare-optimize systems --hipaa    # HIPAA-compliant systems
/industry healthcare-optimize --security --gdpr  # Security with GDPR compliance
/industry healthcare-optimize research --ethics  # Research ethics compliance
```

## Claude Prompt

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

## Dependencies

- `components/security/owasp-compliance.md`
- `components/constitutional/safety-framework.md`
- `components/reporting/generate-structured-report.md`
- `healthcare.compliance.hipaa`
- `security.patient_data.encryption` 