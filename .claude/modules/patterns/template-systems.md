| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Template Systems Pattern

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="template_systems" category="patterns">
  
  <purpose>
    Provide comprehensive template systems patterns for systematic template management and customization.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze template requirements and architecture needs</step>
    <step>2. Design template systems and management framework</step>
    <step>3. Implement template creation and customization mechanisms</step>
    <step>4. Validate template functionality and integration</step>
    <step>5. Maintain template quality and evolution</step>
  </thinking_pattern>
  
  <template_framework>
    <template_architecture>
      <action>Design modular template architecture</action>
      <action>Create template inheritance and composition systems</action>
      <action>Implement template versioning and lifecycle management</action>
      <validation>Architecture properly designed and implemented</validation>
    </template_architecture>
    
    <template_management>
      <action>Implement template storage and retrieval systems</action>
      <action>Create template discovery and selection mechanisms</action>
      <action>Manage template dependencies and relationships</action>
      <validation>Management systems properly implemented</validation>
    </template_management>
    
    <template_customization>
      <action>Implement template customization and parameterization</action>
      <action>Create template adaptation and specialization mechanisms</action>
      <action>Support template extension and modification</action>
      <validation>Customization properly implemented and tested</validation>
    </template_customization>
    
    <template_validation>
      <action>Validate template syntax and structure</action>
      <action>Test template functionality and compatibility</action>
      <action>Ensure template quality and maintainability</action>
      <validation>Templates properly validated and tested</validation>
    </template_validation>
  </template_framework>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for template patterns
      patterns/configuration-management.md for configuration systems
    </depends_on>
    <provides_to>
      ../../domain/adaptation/template-orchestration.md for template orchestration
      ../../domain/templates/README.md for domain templates
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">template_architecture</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">template_composition</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">template_validation</uses_pattern>
    <implementation_notes>
      Template systems provide comprehensive template management
      Template architecture enables modular template design
      Template validation ensures template quality and reliability
    </implementation_notes>
  </pattern_usage>
  
</module>
```