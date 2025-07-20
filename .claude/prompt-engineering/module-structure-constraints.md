# Module Structure Constraints

| module | version | last_updated | status |
|--------|---------|--------------|--------|
| module-structure-constraints | 1.0.0 | 2025-07-20 | production |

## Purpose

Enforce consistent module organization, single responsibility principles, and clear interface contracts across the entire framework to ensure maintainable and scalable architecture.

## Single Responsibility Enforcement

### Responsibility Definition Framework

```xml
<responsibility_definition enforcement="BLOCKING">
  <single_responsibility_principle>
    <definition>Each module should have one and only one reason to change</definition>
    <identification>
      <primary_purpose>What is the main function of this module?</primary_purpose>
      <change_drivers>What would cause this module to change?</change_drivers>
      <abstraction_level>At what level of abstraction does it operate?</abstraction_level>
    </identification>
  </single_responsibility_principle>
  
  <responsibility_categories>
    <data_management>Modules that handle data storage, retrieval, transformation</data_management>
    <business_logic>Modules that implement domain-specific rules and processes</business_logic>
    <presentation>Modules that handle user interface and display logic</presentation>
    <coordination>Modules that orchestrate interactions between other modules</coordination>
    <infrastructure>Modules that provide technical services and utilities</infrastructure>
  </responsibility_categories>
  
  <mixing_violations>
    <data_and_ui>BLOCKED: Modules mixing data handling with presentation</data_and_ui>
    <business_and_infrastructure>BLOCKED: Domain logic mixed with technical concerns</business_and_infrastructure>
    <coordination_and_implementation>BLOCKED: Orchestration mixed with execution</coordination_and_implementation>
    <multiple_domains>BLOCKED: Modules handling multiple business domains</multiple_domains>
  </mixing_violations>
</responsibility_definition>
```

### Responsibility Validation Rules

```xml
<responsibility_validation>
  <validation_questions>
    <question>Can you describe this module's purpose in one sentence?</question>
    <question>Would changes in different business areas affect this module?</question>
    <question>Does this module know about implementation details of its dependencies?</question>
    <question>Are there unrelated functions grouped together?</question>
  </validation_questions>
  
  <validation_criteria>
    <cohesion>All elements work toward same goal</cohesion>
    <coupling>Minimal dependencies on other modules</coupling>
    <abstraction>Consistent level of abstraction throughout</abstraction>
    <encapsulation>Clear public interface hiding implementation</encapsulation>
  </validation_criteria>
  
  <violation_detection>
    <mixed_abstractions>Methods at different abstraction levels</mixed_abstractions>
    <unrelated_functions>Functions serving different purposes</unrelated_functions>
    <knowledge_violations>Knowing too much about other modules</knowledge_violations>
    <temporal_coupling>Dependencies on execution order</temporal_coupling>
  </violation_detection>
</responsibility_validation>
```

## Interface Contract Templates

### Standard Interface Patterns

```xml
<interface_patterns>
  <command_interface>
    <structure>
      <input>Clear input specification with validation</input>
      <processing>Single processing method with clear purpose</processing>
      <output>Standardized output format</output>
      <errors>Explicit error handling and reporting</errors>
    </structure>
    
    <template>
      <thinking_pattern>Step-by-step execution planning</thinking_pattern>
      <validation>Input validation and precondition checking</validation>
      <execution>Core processing logic</execution>
      <post_processing>Output formatting and cleanup</post_processing>
      <error_handling>Comprehensive error recovery</error_handling>
    </template>
  </command_interface>
  
  <module_interface>
    <structure>
      <purpose>Clear module purpose and scope definition</purpose>
      <dependencies>Explicit dependency declarations</dependencies>
      <contracts>Input/output contracts with validation</contracts>
      <integration>Integration points with other modules</integration>
    </structure>
    
    <template>
      <metadata>Version, status, compatibility information</metadata>
      <interface_definition>Public methods and their contracts</interface_definition>
      <implementation_guide>How to implement the interface</implementation_guide>
      <usage_examples>Clear examples of proper usage</usage_examples>
    </template>
  </module_interface>
  
  <service_interface>
    <structure>
      <initialization>Service setup and configuration</initialization>
      <operations>Core service operations</operations>
      <lifecycle>Service lifecycle management</lifecycle>
      <monitoring>Health checks and diagnostics</monitoring>
    </structure>
    
    <contract_specifications>
      <availability>Service availability guarantees</availability>
      <performance>Response time and throughput requirements</performance>
      <reliability>Error rates and recovery procedures</reliability>
      <compatibility>Version compatibility commitments</compatibility>
    </contract_specifications>
  </service_interface>
</interface_patterns>
```

### Contract Validation

```xml
<contract_validation>
  <interface_compliance>
    <signature_validation>Method signatures match interface definition</signature_validation>
    <behavior_validation>Implementation behavior matches contract</behavior_validation>
    <error_handling>Error handling matches contract specifications</error_handling>
    <performance_validation>Performance meets contract requirements</performance_validation>
  </interface_compliance>
  
  <contract_testing>
    <unit_tests>Tests for individual method contracts</unit_tests>
    <integration_tests>Tests for module interaction contracts</integration_tests>
    <performance_tests>Tests for performance contract compliance</performance_tests>
    <error_scenario_tests>Tests for error handling contracts</error_scenario_tests>
  </contract_testing>
  
  <contract_evolution>
    <backward_compatibility>Ensure changes don't break existing contracts</backward_compatibility>
    <version_management>Version contracts appropriately</version_management>
    <deprecation_process>Graceful deprecation of old contracts</deprecation_process>
    <migration_support>Support migration to new contracts</migration_support>
  </contract_evolution>
</contract_validation>
```

## Dependency Validation

### Dependency Analysis Framework

```xml
<dependency_analysis>
  <dependency_types>
    <functional_dependencies>Dependencies required for core functionality</functional_dependencies>
    <structural_dependencies>Dependencies on module structure or organization</structural_dependencies>
    <temporal_dependencies>Dependencies on execution order or timing</temporal_dependencies>
    <data_dependencies>Dependencies on specific data formats or schemas</data_dependencies>
  </dependency_types>
  
  <validation_rules>
    <circular_dependency_prevention>
      <detection>Identify circular dependencies in module graph</detection>
      <prevention>Design modules to avoid circular references</prevention>
      <resolution>Break circular dependencies through abstraction</resolution>
    </circular_dependency_prevention>
    
    <layered_architecture>
      <layer_definition>Define clear architectural layers</layer_definition>
      <dependency_direction>Dependencies only flow in one direction</dependency_direction>
      <layer_isolation>Layers don't skip levels in dependencies</layer_isolation>
    </layered_architecture>
    
    <coupling_minimization>
      <loose_coupling>Minimize dependencies between modules</loose_coupling>
      <interface_based>Depend on interfaces, not implementations</interface_based>
      <dependency_injection>Use dependency injection patterns</dependency_injection>
    </coupling_minimization>
  </validation_rules>
  
  <dependency_metrics>
    <fan_in>Number of modules depending on this module</fan_in>
    <fan_out>Number of modules this module depends on</fan_out>
    <instability>Fan-out / (Fan-in + Fan-out)</instability>
    <abstractness>Ratio of abstract to concrete elements</abstractness>
  </dependency_metrics>
</dependency_analysis>
```

### Dependency Management Patterns

```xml
<dependency_management>
  <inversion_of_control>
    <principle>High-level modules should not depend on low-level modules</principle>
    <implementation>Both should depend on abstractions</implementation>
    <benefits>Reduced coupling, increased testability</benefits>
  </inversion_of_control>
  
  <dependency_injection>
    <constructor_injection>Dependencies provided via constructor</constructor_injection>
    <setter_injection>Dependencies provided via setter methods</setter_injection>
    <interface_injection>Dependencies provided via interface methods</interface_injection>
  </dependency_injection>
  
  <service_locator>
    <centralized_registry>Central registry of available services</centralized_registry>
    <lookup_mechanism>Modules look up dependencies as needed</lookup_mechanism>
    <configuration>External configuration of service locations</configuration>
  </service_locator>
  
  <factory_patterns>
    <abstract_factory>Create families of related objects</abstract_factory>
    <factory_method>Create objects without specifying concrete classes</factory_method>
    <builder_pattern>Construct complex objects step by step</builder_pattern>
  </factory_patterns>
</dependency_management>
```

## Naming Conventions

### Module Naming Standards

```xml
<naming_standards>
  <module_names>
    <pattern>[domain]-[purpose]-[type].md</pattern>
    <examples>
      <command>user-authentication-command.md</command>
      <module>payment-processing-service.md</module>
      <pattern>error-handling-pattern.md</pattern>
      <util>string-formatting-util.md</util>
    </examples>
    <requirements>
      <lowercase>All lowercase with hyphens</lowercase>
      <descriptive>Clearly indicates module purpose</descriptive>
      <consistent>Follows established patterns</consistent>
      <domain_prefix>Includes domain or functional area</domain_prefix>
    </requirements>
  </module_names>
  
  <directory_structure>
    <pattern>[category]/[subcategory]/</pattern>
    <examples>
      <commands>commands/core/, commands/meta/, commands/setup/</commands>
      <modules>modules/patterns/, modules/development/, modules/meta/</modules>
      <system>system/quality/, system/security/, system/context/</system>
    </examples>
    <organization>
      <functional>Group by functional purpose</functional>
      <hierarchical>Use hierarchical structure for related items</hierarchical>
      <scalable>Structure supports growth and addition</scalable>
    </organization>
  </directory_structure>
  
  <interface_naming>
    <methods>
      <verbs>Use verbs for action methods (execute, validate, transform)</verbs>
      <nouns>Use nouns for query methods (getStatus, findItems)</nouns>
      <boolean>Use is/has/can for boolean methods</boolean>
    </methods>
    
    <parameters>
      <descriptive>Parameter names clearly indicate purpose</descriptive>
      <consistent>Consistent naming across related methods</consistent>
      <typed>Include type information where helpful</typed>
    </parameters>
    
    <return_values>
      <descriptive>Return value names indicate content</descriptive>
      <standard_formats>Use standard formats (result, status, data)</standard_formats>
      <error_indication>Clear indication of error conditions</error_indication>
    </return_values>
  </interface_naming>
</naming_standards>
```

### Consistency Enforcement

```xml
<consistency_enforcement>
  <naming_validation>
    <pattern_checking>Validate names follow established patterns</pattern_checking>
    <consistency_checking>Check consistency within and across modules</consistency_checking>
    <domain_alignment>Ensure names align with domain terminology</domain_alignment>
  </naming_validation>
  
  <automated_checking>
    <pre_commit_hooks>Check naming conventions before commit</pre_commit_hooks>
    <continuous_integration>Validate naming in CI pipeline</continuous_integration>
    <documentation_generation>Generate docs with consistent naming</documentation_generation>
  </automated_checking>
  
  <refactoring_support>
    <rename_refactoring>Support safe renaming across modules</rename_refactoring>
    <impact_analysis>Analyze impact of naming changes</impact_analysis>
    <migration_tools>Tools to migrate to new naming conventions</migration_tools>
  </refactoring_support>
</consistency_enforcement>
```

## Framework Integration Examples

### Current Framework Analysis

```xml
<framework_analysis>
  <well_structured_modules>
    <example>
      <module>.claude/modules/patterns/tdd-cycle-pattern.md</module>
      <strengths>
        <single_responsibility>Focused on TDD workflow only</single_responsibility>
        <clear_interface>Well-defined input/output contracts</clear_interface>
        <proper_naming>Descriptive, follows conventions</proper_naming>
      </strengths>
    </example>
    
    <example>
      <module>.claude/system/quality/comprehensive-validation.md</module>
      <strengths>
        <domain_focus>Quality validation domain only</domain_focus>
        <interface_clarity>Clear validation contracts</interface_clarity>
        <dependency_management>Minimal, well-defined dependencies</dependency_management>
      </strengths>
    </example>
  </well_structured_modules>
  
  <modules_needing_improvement>
    <example>
      <module>Large command modules with mixed concerns</module>
      <issues>
        <responsibility_mixing>Command parsing, execution, validation mixed</responsibility_mixing>
        <size_violations>Exceeding recommended size limits</size_violations>
        <coupling_issues>Too many dependencies</coupling_issues>
      </issues>
      <improvements>
        <separation>Split into focused modules</separation>
        <interface_extraction>Extract clear interfaces</interface_extraction>
        <dependency_reduction>Reduce coupling through abstraction</dependency_reduction>
      </improvements>
    </example>
  </modules_needing_improvement>
</framework_analysis>
```

### Structure Improvement Roadmap

```xml
<improvement_roadmap>
  <phase_1_cleanup>
    <identify_violations>Scan all modules for structure violations</identify_violations>
    <prioritize_fixes>Prioritize based on impact and effort</prioritize_fixes>
    <create_refactoring_plan>Plan module restructuring</create_refactoring_plan>
  </phase_1_cleanup>
  
  <phase_2_standardization>
    <apply_naming_conventions>Standardize all module names</apply_naming_conventions>
    <extract_interfaces>Create explicit interface contracts</extract_interfaces>
    <organize_directory_structure>Reorganize for consistency</organize_directory_structure>
  </phase_2_standardization>
  
  <phase_3_optimization>
    <optimize_dependencies>Minimize and clarify dependencies</optimize_dependencies>
    <improve_cohesion>Increase module cohesion</improve_cohesion>
    <reduce_coupling>Reduce inter-module coupling</reduce_coupling>
  </phase_3_optimization>
  
  <phase_4_validation>
    <implement_checking>Implement automated structure checking</implement_checking>
    <create_metrics>Establish structure quality metrics</create_metrics>
    <continuous_monitoring>Monitor structure quality ongoing</continuous_monitoring>
  </phase_4_validation>
</improvement_roadmap>
```

## Validation Tools and Metrics

### Structure Quality Metrics

```xml
<quality_metrics>
  <cohesion_metrics>
    <lcom>Lack of Cohesion of Methods</lcom>
    <functional_cohesion>Degree of functional relatedness</functional_cohesion>
    <semantic_cohesion>Semantic similarity of module elements</semantic_cohesion>
  </cohesion_metrics>
  
  <coupling_metrics>
    <afferent_coupling>Number of modules that depend on this module</afferent_coupling>
    <efferent_coupling>Number of modules this module depends on</efferent_coupling>
    <coupling_factor>Overall coupling in the system</coupling_factor>
  </coupling_metrics>
  
  <responsibility_metrics>
    <purpose_clarity>How clearly defined is the module purpose</purpose_clarity>
    <change_reasons>Number of different reasons this module might change</change_reasons>
    <abstraction_consistency>Consistency of abstraction level</abstraction_consistency>
  </responsibility_metrics>
  
  <interface_metrics>
    <interface_complexity>Complexity of public interface</interface_complexity>
    <contract_completeness>Completeness of interface contracts</contract_completeness>
    <documentation_quality>Quality of interface documentation</documentation_quality>
  </interface_metrics>
</quality_metrics>
```

### Automated Validation Tools

```xml
<validation_tools>
  <structure_analyzers>
    <dependency_analyzer>Analyze module dependencies and detect issues</dependency_analyzer>
    <responsibility_analyzer>Detect responsibility violations</responsibility_analyzer>
    <naming_validator>Validate naming convention compliance</naming_validator>
    <interface_validator>Validate interface contract compliance</interface_validator>
  </structure_analyzers>
  
  <quality_gates>
    <pre_commit>Structure validation before code commit</pre_commit>
    <continuous_integration>Structure checks in CI pipeline</continuous_integration>
    <periodic_audits>Regular comprehensive structure audits</periodic_audits>
  </quality_gates>
  
  <reporting_tools>
    <structure_dashboard>Real-time structure quality dashboard</structure_dashboard>
    <violation_reports>Detailed reports of structure violations</violation_reports>
    <improvement_recommendations>Automated improvement suggestions</improvement_recommendations>
  </reporting_tools>
</validation_tools>
```

## Success Criteria

```xml
<success_criteria>
  <quantitative_goals>
    <single_responsibility>95% of modules pass single responsibility check</single_responsibility>
    <naming_compliance>100% compliance with naming conventions</naming_compliance>
    <interface_completeness>90% of modules have complete interface contracts</interface_completeness>
    <dependency_health>Average coupling <5, cohesion >0.8</dependency_health>
  </quantitative_goals>
  
  <qualitative_goals>
    <maintainability>Code is easy to understand and modify</maintainability>
    <extensibility>New features can be added without structural changes</extensibility>
    <testability>Modules can be tested in isolation</testability>
    <reusability>Modules can be reused in different contexts</reusability>
  </qualitative_goals>
  
  <process_goals>
    <automated_validation>Structure validation is automated and enforced</automated_validation>
    <developer_adoption>Developers consistently follow structure guidelines</developer_adoption>
    <continuous_improvement>Structure quality continuously improves</continuous_improvement>
    <documentation_alignment>Documentation accurately reflects structure</documentation_alignment>
  </process_goals>
</success_criteria>
```