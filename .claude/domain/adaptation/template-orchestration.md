| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Template Orchestration System

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="template_orchestration" category="getting-started">
  
  <purpose>
    Provide systematic template orchestration for framework customization and domain-specific configuration management.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze template requirements and domain context</step>
    <step>2. Select appropriate templates based on classification</step>
    <step>3. Orchestrate template application and customization</step>
    <step>4. Validate template integration and functionality</step>
    <step>5. Generate template orchestration report</step>
  </thinking_pattern>
  
  <orchestration_framework>
    <template_selection>
      <action>Select domain-appropriate templates from template library</action>
      <action>Analyze template dependencies and compatibility</action>
      <action>Determine template application order and priority</action>
      <validation>Templates properly selected and prioritized</validation>
    </template_selection>
    
    <template_application>
      <action>Apply templates in dependency order</action>
      <action>Customize templates for specific domain requirements</action>
      <action>Handle template conflicts and resolution</action>
      <validation>Templates applied successfully with customizations</validation>
    </template_application>
    
    <integration_validation>
      <action>Validate template integration and functionality</action>
      <action>Test template interactions and dependencies</action>
      <action>Verify domain-specific requirements are met</action>
      <validation>Template integration properly validated</validation>
    </integration_validation>
    
    <configuration_finalization>
      <action>Finalize template configuration and settings</action>
      <action>Generate configuration documentation</action>
      <action>Create template application report</action>
      <validation>Configuration finalized and documented</validation>
    </configuration_finalization>
  </orchestration_framework>
  
  <integration_points>
    <depends_on>
      getting-started/domain-classification.md for domain analysis
      patterns/template-systems.md for template management
    </depends_on>
    <provides_to>
      getting-started/domain-adaptation.md for adaptation guidance
      getting-started/framework-configurator.md for configuration
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">template_systems</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">configuration_management</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">dependency_resolution</uses_pattern>
    <implementation_notes>
      Template orchestration provides systematic template management
      Configuration management ensures consistent template application
      Dependency resolution handles template compatibility
    </implementation_notes>
  </pattern_usage>
  
</module>
```