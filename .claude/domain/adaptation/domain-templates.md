| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Domain Templates System

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="domain_templates" category="getting-started">
  
  <purpose>
    Provide comprehensive domain-specific templates for framework customization and project initialization.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze domain requirements and template needs</step>
    <step>2. Design domain-specific template structure</step>
    <step>3. Create comprehensive template collections</step>
    <step>4. Validate template functionality and integration</step>
    <step>5. Maintain template quality and updates</step>
  </thinking_pattern>
  
  <template_framework>
    <domain_analysis>
      <action>Analyze domain-specific requirements and patterns</action>
      <action>Identify template needs and customization points</action>
      <action>Define template scope and functionality</action>
      <validation>Domain properly analyzed and documented</validation>
    </domain_analysis>
    
    <template_design>
      <action>Design domain-specific template structure</action>
      <action>Create modular and extensible template architecture</action>
      <action>Define template customization mechanisms</action>
      <validation>Templates properly designed and structured</validation>
    </template_design>
    
    <template_creation>
      <action>Create comprehensive template collections</action>
      <action>Develop templates for common domain patterns</action>
      <action>Implement template validation and testing</action>
      <validation>Templates properly created and validated</validation>
    </template_creation>
    
    <template_integration>
      <action>Integrate templates with framework systems</action>
      <action>Ensure template compatibility and functionality</action>
      <action>Test template usage and effectiveness</action>
      <validation>Integration properly implemented and tested</validation>
    </template_integration>
  </template_framework>
  
  <integration_points>
    <depends_on>
      getting-started/domain-classification.md for domain analysis
      patterns/template-systems.md for template management
    </depends_on>
    <provides_to>
      getting-started/template-orchestration.md for template orchestration
      commands/adapt.md for adaptation templates
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">template_systems</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">domain_adaptation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">configuration_management</uses_pattern>
    <implementation_notes>
      Domain templates provide specialized framework customization
      Template systems enable consistent template management
      Configuration management ensures template flexibility
    </implementation_notes>
  </pattern_usage>
  
</module>
```