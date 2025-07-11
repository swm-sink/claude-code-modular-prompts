| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Domain-Specific Validation System

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="domain_specific_validation" category="domains">
  
  <purpose>
    Provide comprehensive domain-specific validation for specialized development contexts and requirements.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze domain-specific validation requirements</step>
    <step>2. Design domain-appropriate validation strategies</step>
    <step>3. Execute domain-specific validation tests</step>
    <step>4. Validate domain compliance and standards</step>
    <step>5. Generate domain-specific validation reports</step>
  </thinking_pattern>
  
  <validation_framework>
    <domain_analysis>
      <action>Analyze domain-specific requirements and constraints</action>
      <action>Identify domain validation criteria and standards</action>
      <action>Define domain-appropriate validation approaches</action>
      <validation>Domain properly analyzed and documented</validation>
    </domain_analysis>
    
    <specialized_validation>
      <action>Execute domain-specific validation tests</action>
      <action>Validate domain compliance and best practices</action>
      <action>Test domain-specific functionality and workflows</action>
      <validation>Specialized validation properly executed</validation>
    </specialized_validation>
    
    <compliance_verification>
      <action>Verify compliance with domain standards</action>
      <action>Validate domain-specific security requirements</action>
      <action>Check domain regulatory compliance</action>
      <validation>Compliance properly verified</validation>
    </compliance_verification>
    
    <domain_reporting>
      <action>Generate domain-specific validation reports</action>
      <action>Provide domain-appropriate recommendations</action>
      <action>Document domain validation outcomes</action>
      <validation>Domain reporting properly completed</validation>
    </domain_reporting>
  </validation_framework>
  
  <integration_points>
    <depends_on>
      quality/universal-quality-gates.md for quality standards
      patterns/validation-pattern.md for validation methodology
    </depends_on>
    <provides_to>
      commands/validate.md for domain validation
      quality/domain-validation.md for domain-specific validation
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">domain_validation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">specialized_testing</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">compliance_verification</uses_pattern>
    <implementation_notes>
      Domain-specific validation provides specialized validation
      Specialized testing ensures domain-appropriate validation
      Compliance verification validates domain standards
    </implementation_notes>
  </pattern_usage>
  
</module>
```