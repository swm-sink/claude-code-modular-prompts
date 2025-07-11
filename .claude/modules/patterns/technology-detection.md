| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Technology Detection Pattern

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="technology_detection" category="patterns">
  
  <purpose>
    Provide systematic technology detection patterns for automated technology stack identification and analysis.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Scan project files and configuration for technology indicators</step>
    <step>2. Analyze dependency files and package managers</step>
    <step>3. Identify frameworks, libraries, and tools used</step>
    <step>4. Classify technology stack and ecosystem</step>
    <step>5. Generate technology detection report</step>
  </thinking_pattern>
  
  <detection_framework>
    <file_analysis>
      <action>Scan project files for technology indicators</action>
      <action>Analyze file extensions and naming patterns</action>
      <action>Identify configuration files and build scripts</action>
      <validation>Files properly analyzed for technology indicators</validation>
    </file_analysis>
    
    <dependency_analysis>
      <action>Analyze package.json, requirements.txt, Cargo.toml, etc.</action>
      <action>Identify direct and indirect dependencies</action>
      <action>Map dependency relationships and versions</action>
      <validation>Dependencies properly analyzed and mapped</validation>
    </dependency_analysis>
    
    <framework_identification>
      <action>Identify primary frameworks and libraries</action>
      <action>Detect development tools and build systems</action>
      <action>Classify technology ecosystem and patterns</action>
      <validation>Frameworks properly identified and classified</validation>
    </framework_identification>
    
    <technology_classification>
      <action>Classify technology stack by domain and purpose</action>
      <action>Identify technology maturity and support levels</action>
      <action>Generate technology compatibility matrix</action>
      <validation>Technology stack properly classified</validation>
    </technology_classification>
  </detection_framework>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for detection patterns
      patterns/codebase-analysis.md for project analysis
    </depends_on>
    <provides_to>
      getting-started/domain-classification.md for classification
      patterns/domain-analysis.md for domain understanding
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">automated_detection</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">pattern_recognition</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">dependency_analysis</uses_pattern>
    <implementation_notes>
      Technology detection provides automated stack identification
      Pattern recognition enhances detection accuracy
      Dependency analysis maps technology relationships
    </implementation_notes>
  </pattern_usage>
  
</module>
```