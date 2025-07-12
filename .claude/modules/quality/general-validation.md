| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# General Validation System

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="general_validation" category="quality">
  
  <purpose>
    Provide comprehensive general validation capabilities for framework quality assurance and verification.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Define general validation requirements and scope</step>
    <step>2. Execute general validation tests and checks</step>
    <step>3. Analyze validation results and identify issues</step>
    <step>4. Generate validation report and recommendations</step>
    <step>5. Provide general quality improvement guidance</step>
  </thinking_pattern>
  
  <validation_framework>
    <basic_validation>
      <action>Execute basic framework validation checks</action>
      <action>Verify fundamental functionality and structure</action>
      <action>Test basic integration and compatibility</action>
      <validation>Basic validation properly executed</validation>
    </basic_validation>
    
    <general_testing>
      <action>Execute general testing suite and verification</action>
      <action>Validate common use cases and workflows</action>
      <action>Test general performance and reliability</action>
      <validation>General testing properly executed</validation>
    </general_testing>
    
    <quality_assessment>
      <action>Assess general quality metrics and standards</action>
      <action>Validate code quality and maintainability</action>
      <action>Verify documentation completeness and accuracy</action>
      <validation>Quality assessment properly conducted</validation>
    </quality_assessment>
    
    <validation_reporting>
      <action>Generate general validation reports</action>
      <action>Provide general improvement recommendations</action>
      <action>Document validation findings and outcomes</action>
      <validation>Validation reporting properly completed</validation>
    </validation_reporting>
  </validation_framework>
  
  <integration_points>
    <depends_on>
      quality/universal-quality-gates.md for quality standards
      patterns/validation-pattern.md for validation methodology
    </depends_on>
    <provides_to>
      commands/validate.md for validation fallback
      quality/comprehensive-testing.md for testing integration
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">general_validation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">quality_assessment</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">validation_reporting</uses_pattern>
    <implementation_notes>
      General validation provides fallback validation capabilities
      Quality assessment ensures basic quality standards
      Validation reporting documents validation outcomes
    </implementation_notes>
  </pattern_usage>
  
</module>
```