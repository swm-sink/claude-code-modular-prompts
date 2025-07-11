| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Template Customization Pattern

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="template_customization_pattern" category="patterns">
  
  <purpose>
    Provide systematic template customization patterns for domain-specific adaptation and configuration.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze customization requirements and constraints</step>
    <step>2. Design customization strategy and approach</step>
    <step>3. Implement template customization and adaptation</step>
    <step>4. Validate customization effectiveness and quality</step>
    <step>5. Document customization patterns and decisions</step>
  </thinking_pattern>
  
  <customization_framework>
    <requirement_analysis>
      <action>Analyze domain-specific customization needs</action>
      <action>Identify template modification requirements</action>
      <action>Define customization constraints and boundaries</action>
      <validation>Requirements properly analyzed and defined</validation>
    </requirement_analysis>
    
    <customization_strategy>
      <action>Design customization approach and methodology</action>
      <action>Plan template modification and adaptation steps</action>
      <action>Define validation criteria and success metrics</action>
      <validation>Strategy properly designed and documented</validation>
    </customization_strategy>
    
    <template_adaptation>
      <action>Implement template customization changes</action>
      <action>Adapt templates for specific domain requirements</action>
      <action>Maintain template consistency and quality</action>
      <validation>Templates properly customized and adapted</validation>
    </template_adaptation>
    
    <validation_testing>
      <action>Test customized templates for functionality</action>
      <action>Validate customization meets requirements</action>
      <action>Verify template integration and compatibility</action>
      <validation>Customization properly validated and tested</validation>
    </validation_testing>
  </customization_framework>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for customization patterns
      getting-started/domain-adaptation.md for domain context
    </depends_on>
    <provides_to>
      getting-started/template-orchestration.md for template management
      commands/adapt.md for adaptation execution
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">template_systems</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">configuration_management</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">domain_adaptation</uses_pattern>
    <implementation_notes>
      Template customization provides systematic adaptation methodology
      Configuration management ensures consistent customization
      Domain adaptation guides template-specific modifications
    </implementation_notes>
  </pattern_usage>
  
</module>
```