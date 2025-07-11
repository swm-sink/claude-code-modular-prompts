| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Setup Validation System

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="setup_validation" category="quality">
  
  <purpose>
    Provide comprehensive setup validation for project initialization and configuration verification.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Define setup validation criteria and requirements</step>
    <step>2. Execute setup validation tests and checks</step>
    <step>3. Analyze setup results and identify issues</step>
    <step>4. Generate setup validation report</step>
    <step>5. Provide setup improvement recommendations</step>
  </thinking_pattern>
  
  <validation_framework>
    <environment_validation>
      <action>Validate environment setup and configuration</action>
      <action>Verify required dependencies and tools</action>
      <action>Test environment compatibility and versions</action>
      <validation>Environment properly validated and verified</validation>
    </environment_validation>
    
    <configuration_validation>
      <action>Validate configuration files and settings</action>
      <action>Verify configuration completeness and correctness</action>
      <action>Test configuration integration and compatibility</action>
      <validation>Configuration properly validated</validation>
    </configuration_validation>
    
    <dependency_validation>
      <action>Validate dependency installation and versions</action>
      <action>Verify dependency compatibility and conflicts</action>
      <action>Test dependency resolution and availability</action>
      <validation>Dependencies properly validated</validation>
    </dependency_validation>
    
    <integration_validation>
      <action>Validate setup integration with external systems</action>
      <action>Test setup functionality and basic operations</action>
      <action>Verify setup completeness and readiness</action>
      <validation>Integration properly validated</validation>
    </integration_validation>
  </validation_framework>
  
  <integration_points>
    <depends_on>
      quality/universal-quality-gates.md for quality standards
      patterns/setup-orchestration-pattern.md for setup patterns
    </depends_on>
    <provides_to>
      commands/init.md for initialization validation
      getting-started/project-initialization.md for project setup
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">setup_validation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">dependency_validation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">configuration_validation</uses_pattern>
    <implementation_notes>
      Setup validation ensures proper project initialization
      Dependency validation verifies required components
      Configuration validation ensures correct setup
    </implementation_notes>
  </pattern_usage>
  
</module>
```