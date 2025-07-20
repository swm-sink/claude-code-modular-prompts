# Command Constraint Integration

| module | version | last_updated | status |
|--------|---------|--------------|--------|
| command-constraint-integration | 1.0.0 | 2025-07-20 | production |

## Purpose

Seamlessly integrate architectural constraints into all framework commands, providing automatic enforcement, constraint-aware templates, and intelligent fallback mechanisms for reliable LLM code generation.

## Command Integration Architecture

### Universal Constraint Integration

```xml
<universal_integration>
  <constraint_injection_points>
    <pre_execution>
      <design_validation>Validate planned implementation against constraints</design_validation>
      <size_estimation>Estimate implementation size and complexity</size_estimation>
      <constraint_awareness>Make constraints visible to command execution</constraint_awareness>
      <template_selection>Select constraint-compliant templates</template_selection>
    </pre_execution>
    
    <during_execution>
      <real_time_monitoring>Monitor constraint adherence during implementation</real_time_monitoring>
      <threshold_alerting>Alert when approaching constraint limits</threshold_alerting>
      <adaptive_guidance>Provide real-time guidance for constraint compliance</adaptive_guidance>
      <automatic_decomposition>Trigger decomposition when limits approached</automatic_decomposition>
    </during_execution>
    
    <post_execution>
      <validation_enforcement>Enforce constraint compliance before completion</validation_enforcement>
      <violation_remediation>Automatically remediate constraint violations</violation_remediation>
      <quality_reporting>Report constraint adherence metrics</quality_reporting>
      <learning_integration>Learn from constraint patterns for future improvements</learning_integration>
    </post_execution>
  </constraint_injection_points>
  
  <integration_layers>
    <command_layer>
      <constraint_orchestration>Commands orchestrate constraint checking</constraint_orchestration>
      <enforcement_decisions>Commands make enforcement decisions</enforcement_decisions>
      <user_communication>Commands communicate constraint issues to users</user_communication>
    </command_layer>
    
    <module_layer>
      <constraint_implementation>Modules implement specific constraint logic</constraint_implementation>
      <validation_execution>Modules execute validation algorithms</validation_execution>
      <remediation_suggestions>Modules suggest constraint remediation</remediation_suggestions>
    </module_layer>
    
    <framework_layer>
      <constraint_coordination>Framework coordinates constraint enforcement</constraint_coordination>
      <policy_management>Framework manages constraint policies</policy_management>
      <metrics_aggregation>Framework aggregates constraint metrics</metrics_aggregation>
    </framework_layer>
  </integration_layers>
</universal_integration>
```

### Command-Specific Integration Patterns

```xml
<command_specific_patterns>
  <task_command_integration>
    <constraint_profile>
      <focus>Single file/component constraints</focus>
      <optimization>Fast validation for focused changes</optimization>
      <enforcement_level>Standard enforcement with quick feedback</enforcement_level>
    </constraint_profile>
    
    <integration_workflow>
      <step_1>Analyze task scope against size constraints</step_1>
      <step_2>Select appropriate implementation strategy</step_2>
      <step_3>Monitor implementation progress against limits</step_3>
      <step_4>Trigger decomposition if constraints approached</step_4>
      <step_5>Validate final implementation compliance</step_5>
    </integration_workflow>
    
    <constraint_adaptations>
      <size_awareness>Task command becomes size-aware in planning</size_awareness>
      <decomposition_triggers>Automatic task splitting when needed</decomposition_triggers>
      <template_selection>Choose size-appropriate templates</template_selection>
      <incremental_validation>Validate incrementally during implementation</incremental_validation>
    </constraint_adaptations>
  </task_command_integration>
  
  <feature_command_integration>
    <constraint_profile>
      <focus>Multi-component architectural constraints</focus>
      <optimization>Comprehensive validation across components</optimization>
      <enforcement_level>Strict enforcement with architectural guidance</enforcement_level>
    </constraint_profile>
    
    <integration_workflow>
      <step_1>Analyze feature architecture against constraints</step_1>
      <step_2>Plan component decomposition strategy</step_2>
      <step_3>Design constraint-compliant interfaces</step_3>
      <step_4>Implement with continuous constraint monitoring</step_4>
      <step_5>Validate entire feature against constraints</step_5>
    </integration_workflow>
    
    <constraint_adaptations>
      <architectural_planning>Feature planning includes constraint considerations</architectural_planning>
      <component_sizing>Components designed within size constraints</component_sizing>
      <interface_design>Interfaces designed for constraint compliance</interface_design>
      <god_object_prevention>Active prevention of god objects in features</god_object_prevention>
    </constraint_adaptations>
  </feature_command_integration>
  
  <swarm_command_integration>
    <constraint_profile>
      <focus>Distributed constraint enforcement across agents</focus>
      <optimization>Coordinated validation across multiple agents</optimization>
      <enforcement_level>Consistent enforcement with coordination</enforcement_level>
    </constraint_profile>
    
    <integration_workflow>
      <step_1>Distribute constraint-aware work across agents</step_1>
      <step_2>Coordinate constraint enforcement strategies</step_2>
      <step_3>Monitor constraint adherence across all agents</step_3>
      <step_4>Aggregate constraint violations and resolutions</step_4>
      <step_5>Validate integrated result against constraints</step_5>
    </integration_workflow>
    
    <constraint_adaptations>
      <agent_coordination>Agents coordinate constraint enforcement</agent_coordination>
      <distributed_validation>Validation distributed across agents</distributed_validation>
      <consistency_enforcement>Consistent constraint application</consistency_enforcement>
      <aggregated_reporting>Combined constraint reporting</aggregated_reporting>
    </constraint_adaptations>
  </swarm_command_integration>
</command_specific_patterns>
```

## Constraint-Aware Templates

### Template Architecture

```xml
<template_architecture>
  <constraint_embedded_templates>
    <size_aware_templates>
      <small_implementation>Templates for implementations <100 lines</small_implementation>
      <medium_implementation>Templates for implementations 100-200 lines</medium_implementation>
      <large_implementation>Templates with built-in decomposition for >200 lines</large_implementation>
      <decomposition_templates>Templates that automatically split large implementations</decomposition_templates>
    </size_aware_templates>
    
    <complexity_aware_templates>
      <simple_logic>Templates for straightforward logic implementation</simple_logic>
      <moderate_complexity>Templates with complexity management patterns</moderate_complexity>
      <complex_logic>Templates with mandatory decomposition strategies</complex_logic>
      <algorithm_templates>Templates for specific algorithmic patterns</algorithm_templates>
    </complexity_aware_templates>
    
    <structure_aware_templates>
      <single_responsibility>Templates enforcing single responsibility</single_responsibility>
      <interface_contracts>Templates with built-in interface definitions</interface_contracts>
      <dependency_management>Templates with proper dependency patterns</dependency_management>
      <composition_patterns>Templates favoring composition over inheritance</composition_patterns>
    </structure_aware_templates>
  </constraint_embedded_templates>
  
  <adaptive_template_selection>
    <requirement_analysis>
      <size_estimation>Estimate implementation size from requirements</size_estimation>
      <complexity_assessment>Assess complexity from requirements</complexity_assessment>
      <structure_planning>Plan structure from requirements</structure_planning>
    </requirement_analysis>
    
    <template_matching>
      <constraint_compatibility>Match templates to constraint requirements</constraint_compatibility>
      <pattern_suitability>Select patterns suitable for requirements</pattern_suitability>
      <scalability_consideration>Consider future scalability needs</scalability_consideration>
    </template_matching>
    
    <template_customization>
      <constraint_parameterization>Customize templates with constraint parameters</constraint_parameterization>
      <project_adaptation>Adapt templates to project-specific constraints</project_adaptation>
      <domain_specialization>Specialize templates for domain requirements</domain_specialization>
    </template_customization>
  </adaptive_template_selection>
</template_architecture>
```

### Template Examples

```xml
<template_examples>
  <size_constrained_class_template>
    <template_structure>
      <header>Class definition with size monitoring comments</header>
      <fields>Limited field count with grouping suggestions</fields>
      <constructor>Simple constructor with parameter limits</constructor>
      <methods>Method templates with size constraints</methods>
      <decomposition_triggers>Comments indicating when to extract classes</decomposition_triggers>
    </template_structure>
    
    <constraint_integration>
      <size_tracking>Built-in line counting and warnings</size_tracking>
      <method_limits>Automatic method count monitoring</method_limits>
      <responsibility_focus>Comments enforcing single responsibility</responsibility_focus>
      <extraction_guidance>Clear guidance on when to extract components</extraction_guidance>
    </constraint_integration>
    
    <template_content>
      # Class: [ClassName] (Target: <150 lines, <10 methods)
      # Responsibility: [Single clear responsibility]
      # Extraction triggers: >8 methods, >120 lines, multiple concerns
      
      class [ClassName]:
          """
          [Single responsibility description]
          
          Constraints:
          - Max 10 public methods
          - Max 150 total lines  
          - Single responsibility only
          - Extract collaborators if >8 methods
          """
          
          def __init__(self, [max_5_parameters]):
              # Constructor implementation
              # Constraint: <20 lines, <5 parameters
              
          def [method_name](self, [parameters]):
              # Method implementation
              # Constraint: <25 lines, <5 parameters, single purpose
              
          # EXTRACTION POINT: If adding 9th method, extract collaborator class
    </template_content>
  </size_constrained_class_template>
  
  <decomposition_method_template>
    <template_structure>
      <main_method>Primary method with size constraints</main_method>
      <helper_methods>Helper method templates with extraction points</helper_methods>
      <complexity_management>Built-in complexity reduction patterns</complexity_management>
      <parameter_objects>Templates for parameter object creation</parameter_objects>
    </template_structure>
    
    <constraint_integration>
      <line_counting>Automatic line count monitoring</line_counting>
      <complexity_tracking>Cyclomatic complexity awareness</complexity_tracking>
      <parameter_limits>Parameter count enforcement</parameter_limits>
      <extraction_automation>Automatic helper method extraction</extraction_automation>
    </constraint_integration>
    
    <template_content>
      def [method_name](self, [parameters]):  # Max 5 parameters
          """
          [Method purpose - single responsibility]
          
          Constraints:
          - Max 25 lines total
          - Max 5 parameters (use parameter objects if more needed)
          - Max cyclomatic complexity 10
          - Extract helper methods at 15+ lines
          """
          
          # Input validation (lines 1-3)
          if not self._validate_inputs([parameters]):
              raise ValueError("Invalid inputs")
          
          # Main algorithm (lines 4-20)
          # EXTRACTION POINT: If logic >15 lines, extract to helper method
          result = self._execute_main_logic([parameters])
          
          # Result processing (lines 21-25)
          return self._format_result(result)
      
      def _execute_main_logic(self, [parameters]):
          """Helper method for main algorithm logic"""
          # Constraint: Single focused algorithm, <20 lines
          
      def _format_result(self, result):
          """Helper method for result formatting"""
          # Constraint: Single responsibility, <15 lines
    </template_content>
  </decomposition_method_template>
  
  <interface_contract_template>
    <template_structure>
      <interface_definition>Clear interface specification</interface_definition>
      <contract_documentation>Detailed contract documentation</contract_documentation>
      <validation_patterns>Built-in validation patterns</validation_patterns>
      <error_handling>Standardized error handling</error_handling>
    </template_structure>
    
    <constraint_integration>
      <interface_simplicity>Simple, focused interfaces</interface_simplicity>
      <contract_completeness>Complete contract specifications</contract_completeness>
      <dependency_minimization>Minimal dependency requirements</dependency_minimization>
      <testing_support>Built-in testing support</testing_support>
    </constraint_integration>
    
    <template_content>
      # Interface: [InterfaceName]
      # Responsibility: [Single clear purpose]
      # Constraints: <10 public methods, minimal dependencies
      
      from abc import ABC, abstractmethod
      from typing import [required_types]
      
      class [InterfaceName](ABC):
          """
          [Interface purpose and responsibility]
          
          Contract constraints:
          - Single responsibility principle
          - <10 public methods
          - Clear input/output specifications
          - Comprehensive error handling
          """
          
          @abstractmethod
          def [method_name](self, [typed_parameters]) -> [return_type]:
              """
              [Method purpose and behavior]
              
              Args:
                  [parameter]: [description and constraints]
              
              Returns:
                  [return_description]: [format and constraints]
              
              Raises:
                  [ExceptionType]: [when and why]
              
              Contract:
                  - Preconditions: [input validation requirements]
                  - Postconditions: [output guarantees]
                  - Performance: [response time requirements]
              """
              pass
    </template_content>
  </interface_contract_template>
</template_examples>
```

## Automatic Enforcement

### Enforcement Mechanisms

```xml
<enforcement_mechanisms>
  <real_time_enforcement>
    <size_monitoring>
      <line_counting>Continuous line count monitoring during implementation</line_counting>
      <threshold_alerts>Alerts at 80%, 90%, and 100% of size limits</threshold_alerts>
      <automatic_breaking>Automatic implementation pausing at hard limits</automatic_breaking>
      <decomposition_suggestions>Real-time suggestions for decomposition</decomposition_suggestions>
    </size_monitoring>
    
    <complexity_monitoring>
      <complexity_tracking>Real-time cyclomatic complexity calculation</complexity_tracking>
      <complexity_alerts>Alerts when complexity approaches limits</complexity_alerts>
      <simplification_suggestions>Suggestions for complexity reduction</simplification_suggestions>
      <pattern_recommendations>Recommendations for complexity management patterns</pattern_recommendations>
    </complexity_monitoring>
    
    <structure_monitoring>
      <responsibility_tracking>Monitor adherence to single responsibility</responsibility_tracking>
      <coupling_monitoring>Track coupling changes during implementation</coupling_monitoring>
      <interface_validation>Validate interface contracts in real-time</interface_validation>
      <naming_enforcement>Enforce naming conventions during development</naming_enforcement>
    </structure_monitoring>
  </real_time_enforcement>
  
  <blocking_enforcement>
    <hard_constraints>
      <size_blocking>Block implementation when hard size limits exceeded</size_blocking>
      <complexity_blocking>Block when complexity limits exceeded</complexity_blocking>
      <god_object_blocking>Block creation of detected god objects</god_object_blocking>
      <structure_blocking>Block severe structure violations</structure_blocking>
    </hard_constraints>
    
    <enforcement_workflow>
      <violation_detection>Detect constraint violations immediately</violation_detection>
      <implementation_pausing>Pause implementation when violations detected</implementation_pausing>
      <remediation_guidance>Provide specific remediation guidance</remediation_guidance>
      <resolution_validation>Validate that remediation resolves violations</resolution_validation>
      <implementation_resumption>Resume implementation after violation resolution</implementation_resumption>
    </enforcement_workflow>
    
    <override_mechanisms>
      <emergency_overrides>Emergency overrides for critical fixes</emergency_overrides>
      <justified_exceptions>Documented exceptions with architectural justification</justified_exceptions>
      <temporary_deferrals>Temporary deferral of constraint enforcement</temporary_deferrals>
      <escalation_procedures>Escalation procedures for constraint conflicts</escalation_procedures>
    </override_mechanisms>
  </blocking_enforcement>
</enforcement_mechanisms>
```

### Automatic Remediation

```xml
<automatic_remediation>
  <size_violation_remediation>
    <file_splitting>
      <functionality_analysis>Analyze file functionality for split points</functionality_analysis>
      <domain_separation>Split files by functional domains</domain_separation>
      <utility_extraction>Extract utility functions to separate files</utility_extraction>
      <interface_preservation>Preserve public interfaces during splitting</interface_preservation>
    </file_splitting>
    
    <class_decomposition>
      <responsibility_analysis>Analyze class responsibilities for decomposition</responsibility_analysis>
      <method_grouping>Group related methods for extraction</method_grouping>
      <collaborator_extraction>Extract collaborator classes</collaborator_extraction>
      <interface_design>Design interfaces for extracted classes</interface_design>
    </class_decomposition>
    
    <method_refactoring>
      <algorithm_extraction>Extract complex algorithms to separate methods</algorithm_extraction>
      <parameter_objects>Create parameter objects for methods with many parameters</parameter_objects>
      <helper_methods>Extract helper methods for complex operations</helper_methods>
      <validation_extraction>Extract validation logic to separate methods</validation_extraction>
    </method_refactoring>
  </size_violation_remediation>
  
  <god_object_remediation>
    <responsibility_separation>
      <domain_extraction>Extract different domain responsibilities</domain_extraction>
      <layer_separation>Separate different architectural layers</layer_separation>
      <concern_isolation>Isolate cross-cutting concerns</concern_isolation>
      <coordination_extraction>Extract coordination logic</coordination_extraction>
    </responsibility_separation>
    
    <pattern_application>
      <strategy_pattern>Apply strategy pattern for algorithmic variations</strategy_pattern>
      <facade_pattern>Apply facade pattern for complex subsystems</facade_pattern>
      <observer_pattern>Apply observer pattern for event handling</observer_pattern>
      <command_pattern>Apply command pattern for operation encapsulation</command_pattern>
    </pattern_application>
    
    <interface_refinement>
      <interface_segregation>Split large interfaces into focused ones</interface_segregation>
      <dependency_inversion>Apply dependency inversion for loose coupling</dependency_inversion>
      <contract_definition>Define clear contracts for interactions</contract_definition>
      <abstraction_introduction>Introduce abstractions to reduce coupling</abstraction_introduction>
    </interface_refinement>
  </god_object_remediation>
  
  <structure_violation_remediation>
    <dependency_management>
      <circular_dependency_breaking>Break circular dependencies through abstraction</circular_dependency_breaking>
      <dependency_inversion>Apply dependency inversion patterns</dependency_inversion>
      <interface_introduction>Introduce interfaces to reduce coupling</interface_introduction>
      <layering_enforcement>Enforce proper layering in architecture</layering_enforcement>
    </dependency_management>
    
    <naming_standardization>
      <consistent_naming>Apply consistent naming conventions</consistent_naming>
      <domain_alignment>Align names with domain terminology</domain_alignment>
      <clarity_improvement>Improve name clarity and descriptiveness</clarity_improvement>
      <pattern_compliance>Ensure names follow established patterns</pattern_compliance>
    </naming_standardization>
    
    <interface_improvement>
      <contract_completion>Complete missing interface contracts</contract_completion>
      <documentation_enhancement>Enhance interface documentation</documentation_enhancement>
      <validation_addition>Add input/output validation</validation_addition>
      <error_handling_improvement>Improve error handling specifications</error_handling_improvement>
    </interface_improvement>
  </structure_violation_remediation>
</automatic_remediation>
```

## Fallback Mechanisms

### Constraint Conflict Resolution

```xml
<conflict_resolution>
  <constraint_prioritization>
    <priority_hierarchy>
      <level_1>Security and safety constraints (highest priority)</level_1>
      <level_2>Functional correctness constraints</level_2>
      <level_3>Architectural quality constraints</level_3>
      <level_4>Style and convention constraints (lowest priority)</level_4>
    </priority_hierarchy>
    
    <conflict_resolution_strategies>
      <constraint_relaxation>Temporarily relax lower-priority constraints</constraint_relaxation>
      <alternative_approaches>Suggest alternative implementation approaches</alternative_approaches>
      <phased_implementation>Implement in phases to meet constraints</phased_implementation>
      <architectural_redesign>Redesign architecture to avoid conflicts</architectural_redesign>
    </conflict_resolution_strategies>
    
    <escalation_procedures>
      <automatic_resolution>Attempt automatic resolution first</automatic_resolution>
      <user_guidance>Provide guidance for manual resolution</user_guidance>
      <architectural_review>Escalate to architectural review if needed</architectural_review>
      <exception_approval>Seek approval for constraint exceptions</exception_approval>
    </escalation_procedures>
  </constraint_prioritization>
  
  <context_aware_flexibility>
    <constraint_adaptation>
      <project_context>Adapt constraints based on project context</project_context>
      <domain_requirements>Consider domain-specific requirements</domain_requirements>
      <timeline_constraints>Balance quality with delivery timelines</timeline_constraints>
      <resource_limitations>Consider available resources and expertise</resource_limitations>
    </constraint_adaptation>
    
    <intelligent_exceptions>
      <pattern_recognition>Recognize valid exception patterns</pattern_recognition>
      <cost_benefit_analysis>Analyze cost/benefit of constraint adherence</cost_benefit_analysis>
      <risk_assessment>Assess risks of constraint violations</risk_assessment>
      <mitigation_planning>Plan mitigation strategies for violations</mitigation_planning>
    </intelligent_exceptions>
  </context_aware_flexibility>
</conflict_resolution>
```

### Graceful Degradation

```xml
<graceful_degradation>
  <constraint_relaxation_strategies>
    <progressive_relaxation>
      <phase_1>Warn about constraint violations but allow implementation</phase_1>
      <phase_2>Require justification for constraint violations</phase_2>
      <phase_3>Require architectural review for violations</phase_3>
      <phase_4>Block implementation only for critical violations</phase_4>
    </progressive_relaxation>
    
    <selective_enforcement>
      <critical_constraints>Always enforce critical safety and security constraints</critical_constraints>
      <quality_constraints>Relax quality constraints under time pressure</quality_constraints>
      <style_constraints>Suspend style constraints for emergency fixes</style_constraints>
      <documentation_constraints>Defer documentation constraints if needed</documentation_constraints>
    </selective_enforcement>
    
    <compensation_mechanisms>
      <increased_testing>Require additional testing for constraint violations</increased_testing>
      <enhanced_documentation>Require enhanced documentation for violations</enhanced_documentation>
      <code_review_intensification>Intensify code review for violations</code_review_intensification>
      <monitoring_enhancement>Enhance monitoring for violating components</monitoring_enhancement>
    </compensation_mechanisms>
  </constraint_relaxation_strategies>
  
  <fallback_implementation_patterns>
    <simplified_implementations>
      <minimal_viable_product>Implement minimal version meeting core constraints</minimal_viable_product>
      <incremental_enhancement>Plan incremental enhancement to full requirements</incremental_enhancement>
      <constraint_compliant_subset>Implement subset that meets all constraints</constraint_compliant_subset>
      <phased_delivery>Deliver functionality in constraint-compliant phases</phased_delivery>
    </simplified_implementations>
    
    <alternative_architectures>
      <microservice_decomposition>Break into smaller, constraint-compliant services</microservice_decomposition>
      <plugin_architecture>Use plugin architecture for extensibility</plugin_architecture>
      <event_driven_design>Use events to reduce coupling and complexity</event_driven_design>
      <functional_decomposition>Decompose into functional components</functional_decomposition>
    </alternative_architectures>
  </fallback_implementation_patterns>
</graceful_degradation>
```

### Emergency Procedures

```xml
<emergency_procedures>
  <critical_fix_protocols>
    <immediate_override>
      <security_fixes>Immediate override for security vulnerability fixes</security_fixes>
      <production_outages>Override for critical production outage fixes</production_outages>
      <data_loss_prevention>Override for data loss prevention fixes</data_loss_prevention>
      <compliance_violations>Override for regulatory compliance violations</compliance_violations>
    </immediate_override>
    
    <expedited_review>
      <rapid_architectural_review>Fast-track architectural review for emergencies</rapid_architectural_review>
      <constraint_impact_assessment>Quick assessment of constraint violation impact</constraint_impact_assessment>
      <mitigation_planning>Rapid mitigation planning for violations</mitigation_planning>
      <post_emergency_remediation>Plan remediation after emergency resolution</post_emergency_remediation>
    </expedited_review>
    
    <documentation_requirements>
      <violation_justification>Document justification for constraint violations</violation_justification>
      <impact_assessment>Document expected impact of violations</impact_assessment>
      <remediation_plan>Document plan for post-emergency remediation</remediation_plan>
      <lessons_learned>Document lessons learned for future prevention</lessons_learned>
    </documentation_requirements>
  </critical_fix_protocols>
  
  <recovery_procedures>
    <post_emergency_remediation>
      <constraint_compliance_restoration>Restore constraint compliance after emergency</constraint_compliance_restoration>
      <architectural_debt_paydown>Pay down architectural debt created during emergency</architectural_debt_paydown>
      <quality_improvement>Improve quality beyond pre-emergency state</quality_improvement>
      <prevention_enhancement>Enhance prevention mechanisms</prevention_enhancement>
    </post_emergency_remediation>
    
    <learning_integration>
      <pattern_analysis>Analyze emergency patterns for prevention</pattern_analysis>
      <constraint_refinement>Refine constraints based on emergency learnings</constraint_refinement>
      <process_improvement>Improve emergency response processes</process_improvement>
      <tooling_enhancement>Enhance tooling to prevent similar emergencies</tooling_enhancement>
    </learning_integration>
  </recovery_procedures>
</emergency_procedures>
```

## Framework Integration Examples

### Command Integration Examples

```xml
<integration_examples>
  <task_command_enhanced>
    <enhanced_workflow>
      <step_1>
        <original>Analyze task requirements</original>
        <enhanced>Analyze task requirements + estimate size and complexity against constraints</enhanced>
      </step_1>
      
      <step_2>
        <original>Plan implementation approach</original>
        <enhanced>Plan constraint-compliant implementation with decomposition strategy</enhanced>
      </step_2>
      
      <step_3>
        <original>Implement solution</original>
        <enhanced>Implement with real-time constraint monitoring and automatic guidance</enhanced>
      </step_3>
      
      <step_4>
        <original>Test implementation</original>
        <enhanced>Test implementation + validate constraint compliance + remediate violations</enhanced>
      </step_4>
    </enhanced_workflow>
    
    <constraint_integration_points>
      <planning_phase>Size estimation and decomposition planning</planning_phase>
      <implementation_phase>Real-time monitoring and guidance</implementation_phase>
      <validation_phase>Comprehensive constraint validation</validation_phase>
      <completion_phase>Constraint compliance reporting</completion_phase>
    </constraint_integration_points>
  </task_command_enhanced>
  
  <feature_command_enhanced>
    <enhanced_workflow>
      <step_1>
        <original>Analyze feature requirements</original>
        <enhanced>Analyze requirements + plan constraint-compliant architecture</enhanced>
      </step_1>
      
      <step_2>
        <original>Design feature architecture</original>
        <enhanced>Design with constraint-aware component decomposition and interfaces</enhanced>
      </step_2>
      
      <step_3>
        <original>Implement feature components</original>
        <enhanced>Implement with constraint monitoring across all components</enhanced>
      </step_3>
      
      <step_4>
        <original>Integrate and test feature</original>
        <enhanced>Integrate with constraint validation + test architectural compliance</enhanced>
      </step_4>
    </enhanced_workflow>
    
    <architectural_integration>
      <component_design>Each component designed within constraint limits</component_design>
      <interface_design>Interfaces designed for constraint compliance</interface_design>
      <dependency_management>Dependencies managed to avoid constraint violations</dependency_management>
      <integration_validation>Integration points validated against constraints</integration_validation>
    </architectural_integration>
  </feature_command_enhanced>
  
  <swarm_command_enhanced>
    <enhanced_coordination>
      <constraint_distribution>
        <agent_awareness>Each agent aware of constraint requirements</agent_awareness>
        <coordinated_enforcement>Coordinated constraint enforcement across agents</coordinated_enforcement>
        <consistent_standards>Consistent constraint application</consistent_standards>
        <aggregated_validation>Combined validation of all agent outputs</aggregated_validation>
      </constraint_distribution>
      
      <collaborative_compliance>
        <shared_constraints>Shared understanding of constraint requirements</shared_constraints>
        <coordination_protocols>Protocols for constraint coordination</coordination_protocols>
        <conflict_resolution>Coordinated resolution of constraint conflicts</conflict_resolution>
        <quality_aggregation>Aggregated quality reporting across agents</quality_aggregation>
      </collaborative_compliance>
    </enhanced_coordination>
  </swarm_command_enhanced>
</integration_examples>
```

### Real Framework Implementation

```xml
<framework_implementation>
  <integration_status>
    <current_state>Constraints framework created and ready for integration</current_state>
    <integration_points>All major commands identified for constraint integration</integration_points>
    <template_library>Constraint-aware templates created for common patterns</template_library>
    <validation_engine>Comprehensive validation engine implemented</validation_engine>
  </integration_status>
  
  <rollout_plan>
    <phase_1>
      <target>Integrate constraints with /task command</target>
      <scope>Single-file implementations with size and complexity constraints</scope>
      <timeline>Immediate deployment</timeline>
      <success_criteria>90% compliance with size constraints in task implementations</success_criteria>
    </phase_1>
    
    <phase_2>
      <target>Integrate constraints with /feature command</target>
      <scope>Multi-component features with architectural constraints</scope>
      <timeline>Within 2 weeks</timeline>
      <success_criteria>85% compliance with structure constraints in feature implementations</success_criteria>
    </phase_2>
    
    <phase_3>
      <target>Integrate constraints with /swarm command</target>
      <scope>Distributed implementations with coordinated constraint enforcement</scope>
      <timeline>Within 4 weeks</timeline>
      <success_criteria>Consistent constraint enforcement across all agents</success_criteria>
    </phase_3>
    
    <phase_4>
      <target>Full framework integration</target>
      <scope>All commands with comprehensive constraint integration</scope>
      <timeline>Within 6 weeks</timeline>
      <success_criteria>Framework-wide constraint compliance and automated enforcement</success_criteria>
    </phase_4>
  </rollout_plan>
  
  <monitoring_and_improvement>
    <metrics_tracking>
      <constraint_compliance_rates>Track compliance rates across all commands</constraint_compliance_rates>
      <violation_patterns>Identify common violation patterns</violation_patterns>
      <remediation_effectiveness>Measure effectiveness of automatic remediation</remediation_effectiveness>
      <developer_satisfaction>Track developer satisfaction with constraint integration</developer_satisfaction>
    </metrics_tracking>
    
    <continuous_improvement>
      <constraint_refinement>Continuously refine constraints based on usage data</constraint_refinement>
      <template_enhancement>Enhance templates based on common patterns</template_enhancement>
      <enforcement_optimization>Optimize enforcement mechanisms for better developer experience</enforcement_optimization>
      <integration_expansion>Expand integration to additional framework components</integration_expansion>
    </continuous_improvement>
  </monitoring_and_improvement>
</framework_implementation>
```

## Success Criteria

```xml
<success_criteria>
  <integration_effectiveness>
    <seamless_integration>Constraints integrated without disrupting development workflow</seamless_integration>
    <automatic_enforcement>95% of constraint violations automatically detected and addressed</automatic_enforcement>
    <developer_adoption>High developer adoption of constraint-aware development practices</developer_adoption>
    <quality_improvement>Measurable improvement in code quality metrics</quality_improvement>
  </integration_effectiveness>
  
  <constraint_compliance>
    <size_compliance>90% compliance with size constraints across all commands</size_compliance>
    <structure_compliance>85% compliance with structure constraints</structure_compliance>
    <god_object_prevention>95% reduction in god object creation</god_object_prevention>
    <interface_quality>90% of interfaces meet contract requirements</interface_quality>
  </constraint_compliance>
  
  <system_performance>
    <minimal_overhead>Constraint enforcement adds <10% to development time</minimal_overhead>
    <fast_validation>Constraint validation completes within acceptable time limits</fast_validation>
    <reliable_operation>99.9% uptime for constraint enforcement systems</reliable_operation>
    <accurate_detection>95% accuracy in constraint violation detection</accurate_detection>
  </system_performance>
  
  <long_term_value>
    <maintainability_improvement>Improved code maintainability and readability</maintainability_improvement>
    <development_velocity>Sustained or improved development velocity</development_velocity>
    <quality_culture>Establishment of quality-focused development culture</quality_culture>
    <architectural_health>Improved overall architectural health of codebase</architectural_health>
  </long_term_value>
</success_criteria>
```