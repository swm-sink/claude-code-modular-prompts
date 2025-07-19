| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Compliance Validation System

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="compliance_validation" category="quality">
  
  <purpose>
    Provide comprehensive compliance validation for regulatory and standards compliance verification.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Define compliance requirements and standards</step>
    <step>2. Execute compliance tests and audits</step>
    <step>3. Analyze compliance gaps and violations</step>
    <step>4. Generate compliance validation report</step>
    <step>5. Provide compliance improvement recommendations</step>
  </thinking_pattern>
  
  <validation_framework>
    <standards_compliance>
      <action>Validate against industry standards and frameworks</action>
      <action>Verify compliance with regulatory requirements</action>
      <action>Assess adherence to best practices and guidelines</action>
      <validation>Standards compliance properly validated</validation>
    </standards_compliance>
    
    <audit_execution>
      <action>Execute compliance audits and assessments</action>
      <action>Perform documentation review and verification</action>
      <action>Validate process compliance and procedures</action>
      <validation>Audits properly executed and documented</validation>
    </audit_execution>
    
    <gap_analysis>
      <action>Identify compliance gaps and deficiencies</action>
      <action>Analyze root causes of non-compliance</action>
      <action>Assess compliance risk and impact</action>
      <validation>Gaps properly analyzed and documented</validation>
    </gap_analysis>
    
    <certification_support>
      <action>Support certification and accreditation processes</action>
      <action>Generate compliance evidence and documentation</action>
      <action>Provide certification readiness assessments</action>
      <validation>Certification support properly provided</validation>
    </certification_support>
  </validation_framework>
  
  <integration_points>
    <depends_on>
      quality/universal-quality-gates.md for quality standards
      quality/security-validation.md for security compliance
    </depends_on>
    <provides_to>
      commands/validate.md for validation execution
      quality/comprehensive-testing.md for testing compliance
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">compliance_validation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">audit_execution</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">gap_analysis</uses_pattern>
    <implementation_notes>
      Compliance validation ensures regulatory compliance
      Audit execution provides systematic compliance verification
      Gap analysis identifies compliance improvement opportunities
    </implementation_notes>
  </pattern_usage>
  
</module>
```