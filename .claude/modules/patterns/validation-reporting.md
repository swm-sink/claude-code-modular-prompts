| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Validation Reporting Pattern

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="validation_reporting" category="patterns">
  
  <purpose>
    Provide systematic validation reporting patterns for comprehensive validation results and documentation.
  </purpose>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>1. Collect validation results and metrics</step>
    <step>2. Analyze validation data and identify patterns</step>
    <step>3. Generate comprehensive validation reports</step>
    <step>4. Provide actionable recommendations and next steps</step>
    <step>5. Document validation process and outcomes</step>
  </thinking_pattern>
  
  <reporting_framework>
    <data_collection>
      <action>Collect validation results from all sources</action>
      <action>Aggregate metrics and performance data</action>
      <action>Compile test results and coverage information</action>
      <validation>Data properly collected and aggregated</validation>
    </data_collection>
    
    <analysis_reporting>
      <action>Analyze validation patterns and trends</action>
      <action>Identify critical issues and failure patterns</action>
      <action>Generate statistical analysis and insights</action>
      <validation>Analysis properly conducted and documented</validation>
    </analysis_reporting>
    
    <report_generation>
      <action>Generate comprehensive validation reports</action>
      <action>Create executive summaries and detailed findings</action>
      <action>Provide visual representations and dashboards</action>
      <validation>Reports properly generated and formatted</validation>
    </report_generation>
    
    <recommendation_engine>
      <action>Generate actionable recommendations</action>
      <action>Prioritize issues and improvement opportunities</action>
      <action>Provide implementation guidance and next steps</action>
      <validation>Recommendations properly generated and prioritized</validation>
    </recommendation_engine>
  </reporting_framework>
  
  <integration_points>
    <depends_on>
      patterns/pattern-library.md for reporting patterns
      quality/universal-quality-gates.md for validation standards
    </depends_on>
    <provides_to>
      commands/validate.md for validation execution
      quality/comprehensive-testing.md for testing reports
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">comprehensive_reporting</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">data_visualization</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">actionable_insights</uses_pattern>
    <implementation_notes>
      Validation reporting provides comprehensive result documentation
      Data visualization enhances report clarity and understanding
      Actionable insights guide improvement efforts
    </implementation_notes>
  </pattern_usage>
  
</module>
```