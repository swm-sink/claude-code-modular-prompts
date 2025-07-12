| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Domain Analysis Pattern

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="domain_analysis" category="patterns">
  
  <purpose>
    Provide systematic domain analysis patterns for project classification and adaptation requirements.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze project structure and technology stack</step>
    <step>2. Identify domain characteristics and requirements</step>
    <step>3. Classify domain type and complexity level</step>
    <step>4. Determine adaptation needs and constraints</step>
    <step>5. Generate domain analysis report and recommendations</step>
  </thinking_pattern>
  
  <analysis_framework>
    <technology_analysis>
      <action>Analyze project dependencies and tech stack</action>
      <action>Identify frameworks, libraries, and tools used</action>
      <action>Assess technology maturity and ecosystem</action>
      <validation>Technology stack properly analyzed</validation>
    </technology_analysis>
    
    <domain_classification>
      <action>Classify primary domain (web, mobile, data, etc.)</action>
      <action>Identify secondary characteristics and patterns</action>
      <action>Assess domain complexity and requirements</action>
      <validation>Domain properly classified and documented</validation>
    </domain_classification>
    
    <requirement_analysis>
      <action>Identify domain-specific requirements and constraints</action>
      <action>Analyze scalability, performance, and security needs</action>
      <action>Assess integration and deployment requirements</action>
      <validation>Requirements comprehensively analyzed</validation>
    </requirement_analysis>
    
    <adaptation_planning>
      <action>Determine framework adaptation needs</action>
      <action>Identify customization opportunities and approaches</action>
      <action>Plan implementation strategy and timeline</action>
      <validation>Adaptation plan properly defined</validation>
    </adaptation_planning>
  </analysis_framework>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for analysis patterns
      getting-started/domain-classification.md for classification algorithms
    </depends_on>
    <provides_to>
      ../../domain/adaptation/domain-adaptation.md for adaptation guidance
      ../../domain/adaptation/template-orchestration.md for template selection
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">intelligent_analysis</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">domain_detection</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">configuration_management</uses_pattern>
    <implementation_notes>
      Domain analysis uses intelligent analysis patterns for accuracy
      Domain detection provides automated classification capabilities
      Configuration management ensures consistent analysis approaches
    </implementation_notes>
  </pattern_usage>
  
</module>
```