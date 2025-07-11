| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Codebase Analysis Pattern

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="codebase_analysis" category="patterns">
  
  <purpose>
    Provide systematic codebase analysis patterns for project understanding and domain classification.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Analyze codebase structure and organization</step>
    <step>2. Identify technology stack and dependencies</step>
    <step>3. Classify domain characteristics and patterns</step>
    <step>4. Generate analysis report and recommendations</step>
    <step>5. Determine optimization opportunities</step>
  </thinking_pattern>
  
  <analysis_framework>
    <structure_analysis>
      <action>Analyze project directory structure and organization</action>
      <action>Identify key files and configuration patterns</action>
      <action>Map project architecture and components</action>
      <validation>Structure properly analyzed and documented</validation>
    </structure_analysis>
    
    <technology_analysis>
      <action>Identify programming languages and frameworks</action>
      <action>Analyze dependencies and library usage</action>
      <action>Assess technology stack maturity and patterns</action>
      <validation>Technology stack properly analyzed</validation>
    </technology_analysis>
    
    <domain_classification>
      <action>Classify project domain and characteristics</action>
      <action>Identify domain-specific patterns and requirements</action>
      <action>Determine appropriate framework adaptations</action>
      <validation>Domain properly classified and documented</validation>
    </domain_classification>
    
    <quality_assessment>
      <action>Assess code quality and maintainability</action>
      <action>Identify improvement opportunities</action>
      <action>Generate quality metrics and recommendations</action>
      <validation>Quality properly assessed and documented</validation>
    </quality_assessment>
  </analysis_framework>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for analysis patterns
      patterns/technology-detection.md for technology identification
    </depends_on>
    <provides_to>
      getting-started/domain-classification.md for classification
      commands/init.md for project initialization
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">intelligent_analysis</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">systematic_validation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">domain_detection</uses_pattern>
    <implementation_notes>
      Codebase analysis provides systematic project understanding
      Intelligent analysis patterns enhance accuracy and depth
      Domain detection guides classification and adaptation
    </implementation_notes>
  </pattern_usage>
  
</module>
```