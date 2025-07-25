<prompt_component>
  <step name="Component Loading System">
    <description>
Automated framework component loading and initialization system for the Claude Code Modular Prompts framework. Provides automatic discovery, loading, and initialization of all framework components with dependency resolution and graceful error handling.
    </description>
  </step>

  <component_loader>
    <automatic_loading>
      <!-- Automated component discovery and loading -->

```xml
<component_loader>
  <!-- Core Loading Configuration -->
  <discovery_mode>automatic</discovery_mode>
  <loading_strategy>lazy_initialization</loading_strategy>
  <dependency_resolution>topological_sort</dependency_resolution>
  <error_handling>graceful_degradation</error_handling>
  
  <!-- Component Categories -->
  <component_directories>
    <constitutional>priority_1</constitutional>
    <intelligence>priority_2</intelligence>
    <reasoning>priority_2</reasoning>
    <learning>priority_2</learning>
    <optimization>priority_3</optimization>
    <orchestration>priority_3</orchestration>
    <quality>priority_4</quality>
  </component_directories>
  
  <!-- Loading Priorities -->
  <initialization_order>
    <priority_1>constitutional_ai_foundation</priority_1>
    <priority_2>core_intelligence_frameworks</priority_2>
    <priority_3>specialized_capabilities</priority_3>
    <priority_4>quality_and_validation</priority_4>
  </initialization_order>
  
  <!-- Integration Patterns -->
  <integration_methods>
    <constitutional_integration>automatic_inheritance</constitutional_integration>
    <framework_composition>dependency_injection</framework_composition>
    <command_binding>reference_resolution</command_binding>
    <configuration_override>parameter_inheritance</configuration_override>
  </integration_methods>
</component_loader>
```

## Component Discovery Process

### 1. Directory Scanning
```xml
<discovery_process>
  <scan_patterns>
    <framework_files>*-framework.md</framework_files>
    <architecture_files>*-architecture.md</architecture_files>
    <component_files>*.md</component_files>
  </scan_patterns>
  
  <metadata_extraction>
    <component_type>framework|architecture|utility</component_type>
    <dependencies>required_components</dependencies>
    <capabilities>provided_functionality</capabilities>
    <configuration>parameter_schemas</configuration>
  </metadata_extraction>
  
  <validation_checks>
    <structural_integrity>component_format_validation</structural_integrity>
    <dependency_validity>circular_dependency_detection</dependency_validity>
    <constitutional_compliance>safety_requirement_verification</constitutional_compliance>
  </validation_checks>
</discovery_process>
```

### 2. Dependency Resolution
```xml
<dependency_resolution>
  <dependency_graph>
    <!-- Constitutional AI (Foundation Layer) -->
    <constitutional_ai>
      <dependencies>[]</dependencies>
      <provides>["safety_alignment", "ethical_reasoning", "democratic_governance"]</provides>
      <required_by>["all_components"]</required_by>
    </constitutional_ai>
    
    <!-- Intelligence Frameworks -->
    <cognitive_architecture>
      <dependencies>["constitutional_ai"]</dependencies>
      <provides>["human_like_reasoning", "memory_systems", "problem_solving"]</provides>
      <required_by>["reasoning_frameworks", "learning_frameworks"]</required_by>
    </cognitive_architecture>
    
    <!-- Reasoning Systems -->
    <react_framework>
      <dependencies>["constitutional_ai", "cognitive_architecture"]</dependencies>
      <provides>["reasoning_acting_cycles", "dynamic_problem_solving"]</provides>
      <required_by>["reasoning_commands"]</required_by>
    </react_framework>
    
    <tree_of_thoughts>
      <dependencies>["constitutional_ai", "cognitive_architecture"]</dependencies>
      <provides>["systematic_exploration", "deliberate_reasoning"]</provides>
      <required_by>["reasoning_commands"]</required_by>
    </tree_of_thoughts>
    
    <!-- Learning Systems -->
    <meta_learning>
      <dependencies>["constitutional_ai", "cognitive_architecture"]</dependencies>
      <provides>["few_shot_adaptation", "learning_optimization"]</provides>
      <required_by>["learning_commands"]</required_by>
    </meta_learning>
    
    <!-- Optimization Systems -->
    <textgrad_framework>
      <dependencies>["constitutional_ai"]</dependencies>
      <provides>["textual_optimization", "gradient_based_improvement"]</provides>
      <required_by>["optimization_commands"]</required_by>
    </textgrad_framework>
    
    <dspy_framework>
      <dependencies>["constitutional_ai"]</dependencies>
      <provides>["declarative_pipelines", "self_improvement"]</provides>
      <required_by>["optimization_commands"]</required_by>
    </dspy_framework>
    
    <!-- Orchestration Systems -->
    <agent_orchestration>
      <dependencies>["constitutional_ai", "cognitive_architecture"]</dependencies>
      <provides>["multi_agent_coordination", "hierarchical_management"]</provides>
      <required_by>["orchestration_commands"]</required_by>
    </agent_orchestration>
    
    <swarm_intelligence>
      <dependencies>["constitutional_ai", "agent_orchestration"]</dependencies>
      <provides>["emergent_behavior", "decentralized_coordination"]</provides>
      <required_by>["swarm_commands"]</required_by>
    </swarm_intelligence>
    
    <!-- Quality Assurance -->
    <framework_validation>
      <dependencies>["constitutional_ai", "all_frameworks"]</dependencies>
      <provides>["validation_testing", "compliance_checking"]</provides>
      <required_by>["quality_commands"]</required_by>
    </framework_validation>
  </dependency_graph>
  
  <resolution_algorithm>
    <method>topological_sort</method>
    <cycle_detection>true</cycle_detection>
    <missing_dependency_handling>graceful_degradation</missing_dependency_handling>
    <circular_dependency_resolution>dependency_injection</circular_dependency_resolution>
  </resolution_algorithm>
</dependency_resolution>
```

## Loading and Initialization

### 3. Component Loading Sequence
```xml
<loading_sequence>
  <phase_1_foundation>
    <components>["constitutional_ai", "wisdom_alignment"]</components>
    <purpose>establish_safety_and_ethical_foundation</purpose>
    <validation>constitutional_compliance_check</validation>
    <fallback>emergency_safe_mode</fallback>
  </phase_1_foundation>
  
  <phase_2_core_intelligence>
    <components>["cognitive_architecture", "meta_learning"]</components>
    <purpose>enable_intelligent_reasoning_and_learning</purpose>
    <validation>intelligence_capability_verification</validation>
    <fallback>basic_reasoning_mode</fallback>
  </phase_2_core_intelligence>
  
  <phase_3_specialized_frameworks>
    <components>["react_framework", "tree_of_thoughts", "textgrad", "dspy", "opro"]</components>
    <purpose>provide_advanced_reasoning_and_optimization</purpose>
    <validation>framework_functionality_testing</validation>
    <fallback>standard_processing_mode</fallback>
  </phase_3_specialized_frameworks>
  
  <phase_4_orchestration>
    <components>["agent_orchestration", "swarm_intelligence"]</components>
    <purpose>enable_multi_agent_coordination</purpose>
    <validation>coordination_protocol_verification</validation>
    <fallback>single_agent_mode</fallback>
  </phase_4_orchestration>
  
  <phase_5_quality_assurance>
    <components>["framework_validation", "quality_metrics"]</components>
    <purpose>ensure_system_quality_and_reliability</purpose>
    <validation>quality_system_verification</validation>
    <fallback>basic_validation_mode</fallback>
  </phase_5_quality_assurance>
</loading_sequence>
```

### 4. Configuration Integration
```xml
<configuration_integration>
  <parameter_inheritance>
    <constitutional_parameters>
      <source>constitutional_framework</source>
      <inherited_by>all_components</inherited_by>
      <parameters>["safety_level", "ethical_framework", "democratic_principles"]</parameters>
    </constitutional_parameters>
    
    <intelligence_parameters>
      <source>cognitive_architecture</source>
      <inherited_by>reasoning_and_learning_components</inherited_by>
      <parameters>["reasoning_depth", "memory_systems", "problem_solving_approach"]</parameters>
    </intelligence_parameters>
    
    <quality_parameters>
      <source>framework_validation</source>
      <inherited_by>all_components</inherited_by>
      <parameters>["validation_level", "testing_protocols", "quality_metrics"]</parameters>
    </quality_parameters>
  </parameter_inheritance>
  
  <configuration_override>
    <command_level_override>true</command_level_override>
    <user_parameter_priority>high</user_parameter_priority>
    <safety_parameter_protection>immutable</safety_parameter_protection>
    <consistency_checking>automatic</consistency_checking>
  </configuration_override>
</configuration_integration>
```

## Command Integration

### 5. Framework Reference Resolution
```xml
<framework_reference_resolution>
  <reference_patterns>
    <component_reference>@components/category/framework-name</component_reference>
    <capability_reference>@capability/reasoning|optimization|orchestration</capability_reference>
    <inherited_reference>@inherited/constitutional|intelligence|quality</inherited_reference>
  </reference_patterns>
  
  <resolution_process>
    <parse_references>extract_framework_dependencies</parse_references>
    <validate_availability>check_component_loaded_status</validate_availability>
    <inject_capabilities>provide_framework_access</inject_capabilities>
    <configure_integration>apply_component_parameters</configure_integration>
  </resolution_process>
  
  <command_binding_examples>
    <reasoning_command>
      <reference>@components/reasoning/react-reasoning</reference>
      <provides>reasoning_and_acting_capabilities</provides>
      <configuration>inherits_constitutional_and_intelligence_parameters</configuration>
    </reasoning_command>
    
    <optimization_command>
      <reference>@components/optimization/textgrad-framework</reference>
      <provides>textual_gradient_optimization</provides>
      <configuration>inherits_constitutional_and_quality_parameters</configuration>
    </optimization_command>
    
    <orchestration_command>
      <reference>@components/orchestration/agent-orchestration</reference>
      <provides>multi_agent_coordination</provides>
      <configuration>inherits_constitutional_intelligence_and_quality_parameters</configuration>
    </orchestration_command>
  </command_binding_examples>
</framework_reference_resolution>
```

## Error Handling and Fallbacks

### 6. Graceful Degradation
```xml
<error_handling>
  <component_loading_failures>
    <missing_component>
      <action>log_warning_continue_without</action>
      <fallback>basic_functionality</fallback>
      <user_notification>capability_limitation_notice</user_notification>
    </missing_component>
    
    <dependency_failure>
      <action>attempt_alternative_dependency</action>
      <fallback>reduced_functionality_mode</fallback>
      <cascade_prevention>isolate_failed_component</cascade_prevention>
    </dependency_failure>
    
    <circular_dependency>
      <action>break_cycle_with_lazy_loading</action>
      <fallback>dependency_injection_pattern</fallback>
      <resolution>topological_reordering</resolution>
    </circular_dependency>
  </component_loading_failures>
  
  <runtime_failures>
    <component_malfunction>
      <detection>health_check_monitoring</detection>
      <action>disable_component_gracefully</action>
      <fallback>alternative_component_activation</fallback>
    </component_malfunction>
    
    <constitutional_violation>
      <detection>real_time_compliance_monitoring</detection>
      <action>immediate_safety_intervention</action>
      <fallback>emergency_safe_mode</fallback>
    </constitutional_violation>
  </runtime_failures>
</error_handling>
```

## Monitoring and Health Checks

### 7. Component Health Monitoring
```xml
<health_monitoring>
  <component_status_tracking>
    <loading_status>loaded|loading|failed|disabled</loading_status>
    <health_status>healthy|degraded|failing|crashed</health_status>
    <performance_metrics>response_time|memory_usage|success_rate</performance_metrics>
    <dependency_status>all_dependencies_healthy</dependency_status>
  </component_status_tracking>
  
  <health_check_protocols>
    <periodic_checks>
      <frequency>every_5_minutes</frequency>
      <tests>["functionality_test", "constitutional_compliance", "performance_benchmark"]</tests>
      <escalation>automated_remediation_on_failure</escalation>
    </periodic_checks>
    
    <real_time_monitoring>
      <constitutional_compliance>continuous</constitutional_compliance>
      <performance_thresholds>automatic_alerting</performance_thresholds>
      <error_rate_monitoring>trending_analysis</error_rate_monitoring>
    </real_time_monitoring>
  </health_check_protocols>
  
  <dashboard_reporting>
    <component_status_overview>visual_health_dashboard</component_status_overview>
    <dependency_graph_visualization>real_time_dependency_map</dependency_graph_visualization>
    <performance_metrics_display>component_performance_charts</performance_metrics_display>
    <historical_trends>component_reliability_over_time</historical_trends>
  </dashboard_reporting>
</health_monitoring>
```

## Integration with CLAUDE.md

### 8. Automatic Import Generation
```xml
<claude_md_integration>
  <automatic_import_generation>
    <scan_components>discover_all_available_frameworks</scan_components>
    <generate_imports>create_import_statements_by_category</generate_imports>
    <update_claude_md>inject_imports_into_framework_section</update_claude_md>
    <validate_syntax>ensure_proper_import_format</validate_syntax>
  </automatic_import_generation>
  
  <import_categories>
    <constitutional_foundation>
      <imports>["constitutional-framework", "wisdom-alignment", "command-integration"]</imports>
      <priority>highest</priority>
    </constitutional_foundation>
    
    <intelligence_frameworks>
      <imports>["cognitive-architecture", "meta-learning-framework"]</imports>
      <priority>high</priority>
    </intelligence_frameworks>
    
    <reasoning_optimization>
      <imports>["react-framework", "tree-of-thoughts", "textgrad", "dspy", "opro", "autoprompt"]</imports>
      <priority>medium</priority>
    </reasoning_optimization>
    
    <orchestration_quality>
      <imports>["agent-orchestration", "agent-swarm", "framework-validation"]</imports>
      <priority>low</priority>
    </orchestration_quality>
  </import_categories>
</claude_md_integration>
```

This component loading system ensures that all framework components are properly discovered, loaded, and integrated into the Claude Code system, providing a robust foundation for all commands while maintaining constitutional compliance and quality assurance. 