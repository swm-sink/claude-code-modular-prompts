| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-16   | stable |

# Template Resolution Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="template_resolution" category="context">
  
  <purpose>
    Dynamic resolution of [PROJECT_CONFIG: ...] placeholders throughout the framework, enabling project-specific customization without modifying core framework files.
  </purpose>
  
  <resolution_mechanism>
    <placeholder_syntax>
      <format>[PROJECT_CONFIG: path.to.value | DEFAULT: fallback_value]</format>
      <examples>
        <example>[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]</example>
        <example>[PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms]</example>
        <example>[PROJECT_CONFIG: source_directory | DEFAULT: src]</example>
      </examples>
    </placeholder_syntax>
    
    <resolution_process>
      <step order="1">Detect placeholder pattern in framework text</step>
      <step order="2">Extract configuration path and default value</step>
      <step order="3">Check for PROJECT_CONFIG.xml in project root</step>
      <step order="4">Parse XML and navigate to specified path</step>
      <step order="5">Return configured value or fallback to default</step>
      <step order="6">Cache resolved values for performance</step>
    </resolution_process>
    
    <configuration_loading>
      <primary_source>PROJECT_CONFIG.xml in project root</primary_source>
      <fallback_strategy>Use DEFAULT values when config missing or path not found</fallback_strategy>
      <validation>Validate XML structure and required fields on load</validation>
      <caching>Cache parsed configuration for session duration</caching>
    </configuration_loading>
  </resolution_mechanism>
  
  <implementation_details>
    <resolution_contexts>
      <context name="commands">Resolution within command definitions and workflows</context>
      <context name="modules">Resolution within module configurations and rules</context>
      <context name="quality_gates">Resolution within quality gate thresholds</context>
      <context name="personas">Resolution within persona capabilities</context>
      <context name="thinking_patterns">Resolution within critical thinking questions</context>
    </resolution_contexts>
    
    <path_navigation>
      <description>Navigate XML structure using dot notation</description>
      <examples>
        <path>quality_standards.test_coverage.threshold → <test_coverage><threshold>90</threshold></test_coverage></path>
        <path>project_structure.source_directory → <project_structure><source_directory>src</source_directory></project_structure></path>
        <path>commands.test → <commands><test>npm test</test></commands></path>
      </examples>
    </path_navigation>
    
    <default_handling>
      <rule>Always provide sensible defaults for missing configuration</rule>
      <rule>Defaults should work for most common project types</rule>
      <rule>Log when defaults are used for transparency</rule>
    </default_handling>
  </implementation_details>
  
  <integration_points>
    <framework_initialization>
      <description>Load and validate configuration during /init command</description>
      <validation>Ensure all critical paths have valid values</validation>
      <user_feedback>Report configuration status and any missing values</user_feedback>
    </framework_initialization>
    
    <runtime_resolution>
      <description>Resolve placeholders dynamically during command execution</description>
      <performance>Cache lookups to avoid repeated XML parsing</performance>
      <error_handling>Gracefully handle missing configuration with defaults</error_handling>
    </runtime_resolution>
    
    <configuration_updates>
      <description>Support configuration changes without framework restart</description>
      <cache_invalidation>Clear cache when PROJECT_CONFIG.xml modified</cache_invalidation>
      <hot_reload>Optional hot-reload for development workflows</hot_reload>
    </configuration_updates>
  </integration_points>
  
  <special_placeholders>
    <domain_specific_rules>
      <description>Resolution of domain-specific rule arrays</description>
      <format>[PROJECT_CONFIG: domain_specific_rules | DEFAULT: none]</format>
      <handling>Parse as array and inject appropriate rules for domain</handling>
    </domain_specific_rules>
    
    <custom_personas>
      <description>Resolution of project-specific personas</description>
      <format>[PROJECT_CONFIG: custom_personas | DEFAULT: none]</format>
      <handling>Load additional personas from configuration</handling>
    </custom_personas>
    
    <workflow_commands>
      <description>Resolution of project-specific commands</description>
      <format>[PROJECT_CONFIG: commands.* | DEFAULT: auto_detect]</format>
      <handling>Detect appropriate commands based on project type if not configured</handling>
    </workflow_commands>
  </special_placeholders>
  
  <error_handling>
    <missing_configuration>
      <behavior>Use default value and log resolution</behavior>
      <user_notification>Inform user during initialization about missing config</user_notification>
    </missing_configuration>
    
    <invalid_path>
      <behavior>Use default value and warn about invalid path</behavior>
      <debugging>Provide path navigation hints for correction</debugging>
    </invalid_path>
    
    <malformed_placeholder>
      <behavior>Leave placeholder unchanged and warn</behavior>
      <validation>Validate placeholder syntax during framework testing</validation>
    </malformed_placeholder>
  </error_handling>
  
  <examples>
    <resolution_example>
      <input>Coverage must be [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% or higher</input>
      <config_present>Coverage must be 95% or higher</config_present>
      <config_absent>Coverage must be 90% or higher</config_absent>
    </resolution_example>
    
    <command_example>
      <input>Run tests with [PROJECT_CONFIG: commands.test | DEFAULT: npm test]</input>
      <config_present>Run tests with pytest</config_present>
      <config_absent>Run tests with npm test</config_absent>
    </command_example>
    
    <directory_example>
      <input>Source files in [PROJECT_CONFIG: source_directory | DEFAULT: src]</input>
      <config_present>Source files in app</config_present>
      <config_absent>Source files in src</config_absent>
    </directory_example>
  </examples>
  
  <performance_optimization>
    <caching_strategy>
      <description>Aggressive caching of resolved values</description>
      <implementation>In-memory cache with TTL based on file modification time</implementation>
      <invalidation>Watch PROJECT_CONFIG.xml for changes</invalidation>
    </caching_strategy>
    
    <lazy_loading>
      <description>Only parse configuration when placeholders encountered</description>
      <benefit>Avoid overhead for commands that don't use configuration</benefit>
    </lazy_loading>
    
    <batch_resolution>
      <description>Resolve multiple placeholders in single pass</description>
      <benefit>Reduce repeated parsing and path navigation</benefit>
    </batch_resolution>
  </performance_optimization>
</module>
```