# Pattern Validation Rules

## Overview

Comprehensive validation system ensuring all prompt patterns meet quality, effectiveness, and consistency standards before deployment. Includes structural, semantic, and performance validation with automated and human review processes.

## Framework Integration

<delegation_reference>
  This module implements quality assurance validation for all prompt patterns
</delegation_reference>

## Validation Framework

### Multi-Level Validation Architecture

<validation_architecture>
  <validation_levels>
    <level_1_structural>
      <description>Basic format and structure validation</description>
      <automated>100% automated checking</automated>
      <speed>< 10ms per pattern</speed>
      <scope>XML structure, required fields, format compliance</scope>
    </level_1_structural>
    
    <level_2_semantic>
      <description>Logical consistency and meaning validation</description>
      <automated>80% automated, 20% human review</automated>
      <speed>< 100ms per pattern</speed>
      <scope>Logic validation, coherence, completeness</scope>
    </level_2_semantic>
    
    <level_3_effectiveness>
      <description>Performance and outcome validation</description>
      <automated>60% automated, 40% human review</automated>
      <speed>< 1 second per pattern</speed>
      <scope>Expected effectiveness, comparative performance</scope>
    </level_3_effectiveness>
    
    <level_4_integration>
      <description>Framework integration and compatibility validation</description>
      <automated>70% automated, 30% human review</automated>
      <speed>< 2 seconds per pattern</speed>
      <scope>Command compatibility, module integration, ecosystem fit</scope>
    </level_4_integration>
  </validation_levels>
  
  <validation_gates>
    <gate_1>Pattern must pass all Level 1 checks to proceed</gate_1>
    <gate_2>Pattern must pass 90% of Level 2 checks to proceed</gate_2>
    <gate_3>Pattern must achieve minimum effectiveness threshold</gate_3>
    <gate_4>Pattern must integrate properly with framework</gate_4>
  </validation_gates>
</validation_architecture>

## Structural Validation Rules

### XML Structure Requirements

<structural_rules>
  <template_compliance>
    <rule_id>STRUCT-001</rule_id>
    <rule_name>Standard Template Adherence</rule_name>
    <description>Pattern must follow established template structure</description>
    <validation_logic>
      <required_sections>
        <section>metadata</section>
        <section>description</section>
        <section>template_structure</section>
        <section>validation_rules</section>
        <section>usage_metrics</section>
      </required_sections>
    </validation_logic>
    <error_handling>Provide specific missing section information</error_handling>
    <severity>Critical - blocks pattern acceptance</severity>
  </template_compliance>
  
  <metadata_completeness>
    <rule_id>STRUCT-002</rule_id>
    <rule_name>Complete Metadata Requirements</rule_name>
    <description>All required metadata fields must be present and valid</description>
    <validation_logic>
      <required_fields>
        <field name="pattern_id" type="string" format="^[a-z0-9-]+$">Unique identifier</field>
        <field name="pattern_name" type="string" min_length="5" max_length="100">Human-readable name</field>
        <field name="category" type="enum" values="reasoning,learning,structural,optimization">Primary category</field>
        <field name="effectiveness_score" type="number" min="0.0" max="1.0">Performance rating</field>
        <field name="version" type="string" format="semver">Semantic version</field>
        <field name="last_updated" type="date" format="ISO8601">Update timestamp</field>
      </required_fields>
    </validation_logic>
    <validation_checks>
      <uniqueness>pattern_id must be unique across all patterns</uniqueness>
      <format_compliance>All fields must match specified formats</format_compliance>
      <value_ranges>Numerical fields must be within valid ranges</value_ranges>
    </validation_checks>
    <severity>Critical - essential for pattern identification and management</severity>
  </metadata_completeness>
  
  <xml_well_formedness>
    <rule_id>STRUCT-003</rule_id>
    <rule_name>Valid XML Structure</rule_name>
    <description>Pattern template must be well-formed XML</description>
    <validation_logic>
      <xml_parsing>Must parse without syntax errors</xml_parsing>
      <tag_matching>All opening tags must have corresponding closing tags</tag_matching>
      <nesting_validation>Proper hierarchical nesting structure</nesting_validation>
      <encoding_compliance>UTF-8 encoding compliance</encoding_compliance>
    </validation_logic>
    <common_errors>
      <error>Unclosed tags</error>
      <error>Invalid characters in tag names</error>
      <error>Improper nesting</error>
      <error>Missing namespace declarations</error>
    </common_errors>
    <severity>Critical - prevents pattern parsing and usage</severity>
  </xml_well_formedness>
  
  <semantic_tag_naming>
    <rule_id>STRUCT-004</rule_id>
    <rule_name>Meaningful Tag Names</rule_name>
    <description>XML tags must be semantically meaningful and follow naming conventions</description>
    <validation_logic>
      <naming_conventions>
        <format>lowercase with underscores (snake_case)</format>
        <length>minimum 3 characters, maximum 30 characters</length>
        <prohibited>Generic names like "thing", "stuff", "data"</prohibited>
        <required>Tags must describe their content purpose</required>
      </naming_conventions>
    </validation_logic>
    <tag_dictionary>
      <approved_tags>Curated list of approved semantic tag names</approved_tags>
      <deprecated_tags>Tags that should no longer be used</deprecated_tags>
      <suggested_alternatives>Replacements for commonly misused tags</suggested_alternatives>
    </tag_dictionary>
    <severity>Medium - affects maintainability and clarity</severity>
  </semantic_tag_naming>
</structural_rules>

### Content Structure Requirements

<content_structure_rules>
  <template_variables>
    <rule_id>CONTENT-001</rule_id>
    <rule_name>Valid Variable Definitions</rule_name>
    <description>All template variables must be properly defined and used</description>
    <validation_logic>
      <variable_declaration>
        <required_attributes>name, type, required</required_attributes>
        <supported_types>string, number, boolean, array, object</supported_types>
        <naming_format>descriptive snake_case names</naming_format>
      </variable_declaration>
      <variable_usage>
        <placeholder_format>${variable_name} in templates</placeholder_format>
        <usage_validation>All declared variables must be used</usage_validation>
        <undefined_check>No undefined variables in templates</undefined_check>
      </variable_usage>
    </validation_logic>
    <error_prevention>
      <unused_variables>Warning for declared but unused variables</unused_variables>
      <undefined_references>Error for template references to undefined variables</undefined_references>
      <type_consistency>Validation that variable usage matches declared type</type_consistency>
    </error_prevention>
    <severity>High - affects pattern functionality</severity>
  </template_variables>
  
  <example_consistency>
    <rule_id>CONTENT-002</rule_id>
    <rule_name>Consistent Examples</rule_name>
    <description>All examples must be consistent with pattern purpose and format</description>
    <validation_logic>
      <format_consistency>
        <input_format>All example inputs follow same format</input_format>
        <output_format>All example outputs follow same format</output_format>
        <style_consistency>Consistent tone and style across examples</style_consistency>
      </format_consistency>
      <quality_requirements>
        <completeness>Examples show complete input-output pairs</completeness>
        <relevance>Examples directly relate to pattern purpose</relevance>
        <diversity>Examples cover different scenarios within pattern scope</diversity>
      </quality_requirements>
    </validation_logic>
    <quality_checks>
      <minimum_examples>At least 2 examples required, maximum 5 recommended</minimum_examples>
      <example_quality>Each example must demonstrate clear value</example_quality>
      <edge_case_coverage>Include at least one edge case example</edge_case_coverage>
    </quality_checks>
    <severity>High - examples are critical for pattern understanding</severity>
  </example_consistency>
  
  <anti_pattern_compliance>
    <rule_id>CONTENT-003</rule_id>
    <rule_name>Anti-Pattern Avoidance</rule_name>
    <description>Pattern must not contain known anti-patterns</description>
    <validation_logic>
      <anti_pattern_scanning>Automated detection of common anti-patterns</anti_pattern_scanning>
      <pattern_analysis>Analysis against anti-pattern database</pattern_analysis>
      <risk_assessment>Evaluation of potential negative impacts</risk_assessment>
    </validation_logic>
    <checked_anti_patterns>
      <circular_reasoning>Avoid self-referential logic</circular_reasoning>
      <false_precision>Avoid unjustified specific claims</false_precision>
      <information_soup>Maintain clear organization</information_soup>
      <over_complexity>Avoid unnecessary complexity</over_complexity>
    </checked_anti_patterns>
    <severity>High - anti-patterns significantly reduce effectiveness</severity>
  </anti_pattern_compliance>
</content_structure_rules>

## Semantic Validation Rules

### Logical Consistency Requirements

<semantic_rules>
  <reasoning_validity>
    <rule_id>SEMANTIC-001</rule_id>
    <rule_name>Sound Logical Structure</rule_name>
    <description>Pattern reasoning must be logically sound and consistent</description>
    <validation_logic>
      <premise_conclusion_validation>
        <premise_support>Premises must adequately support conclusions</premise_support>
        <logical_flow>Reasoning steps must follow logically</logical_flow>
        <assumption_identification>Identify and validate all assumptions</assumption_identification>
      </premise_conclusion_validation>
      <consistency_checking>
        <internal_consistency>No contradictory statements within pattern</internal_consistency>
        <external_consistency>Compatible with established knowledge</external_consistency>
        <temporal_consistency>Time-dependent claims remain valid</temporal_consistency>
      </consistency_checking>
    </validation_logic>
    <validation_methods>
      <automated_logic_checking>Basic logical fallacy detection</automated_logic_checking>
      <expert_review>Human validation of complex reasoning</expert_review>
      <cross_reference_validation>Check against authoritative sources</cross_reference_validation>
    </validation_methods>
    <severity>Critical - unsound reasoning undermines pattern utility</severity>
  </reasoning_validity>
  
  <purpose_alignment>
    <rule_id>SEMANTIC-002</rule_id>
    <rule_name>Purpose-Implementation Alignment</rule_name>
    <description>Pattern implementation must align with stated purpose</description>
    <validation_logic>
      <purpose_analysis>
        <goal_identification>Clear identification of pattern objectives</goal_identification>
        <success_criteria>Measurable success indicators</success_criteria>
        <scope_definition>Clear boundaries of pattern applicability</scope_definition>
      </purpose_analysis>
      <implementation_validation>
        <approach_suitability>Implementation approach fits the purpose</approach_suitability>
        <completeness_check>Implementation covers all stated objectives</completeness_check>
        <efficiency_assessment>Implementation is reasonably efficient for purpose</efficiency_assessment>
      </implementation_validation>
    </validation_logic>
    <alignment_metrics>
      <goal_coverage>Percentage of stated goals addressed by implementation</goal_coverage>
      <method_appropriateness>How well chosen methods fit the objectives</method_appropriateness>
      <resource_efficiency>Resource usage appropriateness for intended outcomes</resource_efficiency>
    </alignment_metrics>
    <severity>High - misalignment reduces pattern effectiveness</severity>
  </purpose_alignment>
  
  <coherence_validation>
    <rule_id>SEMANTIC-003</rule_id>
    <rule_name>Content Coherence</rule_name>
    <description>All pattern components must work together coherently</description>
    <validation_logic>
      <component_integration>
        <template_description_alignment>Template matches description</template_description_alignment>
        <example_consistency>Examples align with template and description</example_consistency>
        <metadata_accuracy>Metadata accurately reflects pattern characteristics</metadata_accuracy>
      </component_integration>
      <narrative_flow>
        <logical_progression>Information presented in logical order</logical_progression>
        <smooth_transitions>Clear connections between sections</smooth_transitions>
        <unified_voice>Consistent tone and style throughout</unified_voice>
      </narrative_flow>
    </validation_logic>
    <coherence_checks>
      <cross_section_validation>Ensure all sections support the same narrative</cross_section_validation>
      <terminology_consistency>Consistent use of terms and concepts</terminology_consistency>
      <level_appropriateness>Content complexity matches intended audience</level_appropriateness>
    </coherence_checks>
    <severity>Medium - affects user understanding and trust</severity>
  </coherence_validation>
</semantic_rules>

## Performance Validation Rules

### Effectiveness Requirements

<performance_rules>
  <minimum_effectiveness>
    <rule_id>PERF-001</rule_id>
    <rule_name>Effectiveness Threshold</rule_name>
    <description>Pattern must meet minimum effectiveness standards</description>
    <validation_logic>
      <threshold_requirements>
        <success_rate>Minimum 70% success rate on test scenarios</success_rate>
        <quality_score>Minimum 0.7 average quality rating</quality_score>
        <user_satisfaction>Minimum 3.5/5.0 user satisfaction rating</user_satisfaction>
      </threshold_requirements>
      <testing_methodology>
        <test_scenarios>Standardized test cases for pattern category</test_scenarios>
        <evaluation_criteria>Consistent evaluation standards</evaluation_criteria>
        <sample_size>Minimum 20 test applications per pattern</sample_size>
      </testing_methodology>
    </validation_logic>
    <measurement_process>
      <automated_testing>Objective metrics where possible</automated_testing>
      <human_evaluation>Expert assessment of subjective qualities</human_evaluation>
      <user_feedback>Real user satisfaction measurement</user_feedback>
    </measurement_process>
    <severity>Critical - ineffective patterns harm user experience</severity>
  </minimum_effectiveness>
  
  <efficiency_standards>
    <rule_id>PERF-002</rule_id>
    <rule_name>Efficiency Requirements</rule_name>
    <description>Pattern must meet reasonable efficiency standards</description>
    <validation_logic>
      <token_efficiency>
        <baseline_comparison>Compare against baseline patterns for similar tasks</baseline_comparison>
        <efficiency_ratio>Quality achieved per token used</efficiency_ratio>
        <optimization_potential>Identify improvement opportunities</optimization_potential>
      </token_efficiency>
      <time_efficiency>
        <processing_time>Reasonable processing time for complexity level</processing_time>
        <user_wait_time>Acceptable user experience timing</user_wait_time>
        <scalability>Performance with varying input sizes</scalability>
      </time_efficiency>
    </validation_logic>
    <efficiency_benchmarks>
      <simple_patterns>< 50 tokens baseline, < 2 seconds processing</simple_patterns>
      <moderate_patterns>< 150 tokens baseline, < 5 seconds processing</moderate_patterns>
      <complex_patterns>< 300 tokens baseline, < 15 seconds processing</complex_patterns>
    </efficiency_benchmarks>
    <severity>Medium - affects user experience and resource usage</severity>
  </efficiency_standards>
  
  <consistency_requirements>
    <rule_id>PERF-003</rule_id>
    <rule_name>Output Consistency</rule_name>
    <description>Pattern must produce consistent results across similar inputs</description>
    <validation_logic>
      <reproducibility_testing>
        <same_input_testing>Multiple runs with identical inputs</same_input_testing>
        <similar_input_testing>Testing with similar but not identical inputs</similar_input_testing>
        <variance_measurement>Statistical analysis of output variation</variance_measurement>
      </reproducibility_testing>
      <consistency_metrics>
        <output_similarity>Similarity of outputs for same inputs</output_similarity>
        <quality_variance>Variation in output quality</quality_variance>
        <format_consistency>Consistent output formatting</format_consistency>
      </consistency_metrics>
    </validation_logic>
    <consistency_thresholds>
      <high_consistency>< 0.1 standard deviation in quality scores</high_consistency>
      <acceptable_consistency>< 0.2 standard deviation in quality scores</acceptable_consistency>
      <unacceptable_variance>> 0.3 standard deviation requires improvement</unacceptable_variance>
    </consistency_thresholds>
    <severity>High - inconsistency reduces user trust and reliability</severity>
  </consistency_requirements>
</performance_rules>

## Integration Validation Rules

### Framework Compatibility

<integration_rules>
  <command_compatibility>
    <rule_id>INTEGRATION-001</rule_id>
    <rule_name>Claude Code Command Integration</rule_name>
    <description>Pattern must integrate properly with framework commands</description>
    <validation_logic>
      <command_testing>
        <auto_command>Test pattern with intelligent routing</auto_command>
        <task_command>Validate development workflow integration</task_command>
        <query_command>Ensure research-oriented compatibility</query_command>
        <swarm_command>Verify multi-agent coordination support</swarm_command>
      </command_testing>
      <integration_requirements>
        <input_compatibility>Pattern accepts standard command inputs</input_compatibility>
        <output_format>Produces expected output format for commands</output_format>
        <error_handling>Graceful failure handling in command context</error_handling>
      </integration_requirements>
    </validation_logic>
    <compatibility_matrix>
      <full_compatibility>Pattern works with all applicable commands</full_compatibility>
      <partial_compatibility>Pattern works with subset of commands (documented limitations)</partial_compatibility>
      <incompatible>Pattern cannot be used with certain commands (explicit exclusions)</incompatible>
    </compatibility_matrix>
    <severity>High - integration failures break framework functionality</severity>
  </command_compatibility>
  
  <module_interoperability>
    <rule_id>INTEGRATION-002</rule_id>
    <rule_name>Module System Compatibility</rule_name>
    <description>Pattern must work with other framework modules</description>
    <validation_logic>
      <module_interaction_testing>
        <quality_modules>Integration with TDD, review, performance modules</quality_modules>
        <security_modules>Compatibility with security and compliance checking</security_modules>
        <development_modules>Integration with development workflow modules</development_modules>
      </module_interaction_testing>
      <interoperability_requirements>
        <data_exchange>Proper data format exchange with modules</data_exchange>
        <workflow_integration>Fits into module orchestration workflows</workflow_integration>
        <state_management>Proper handling of shared state and context</state_management>
      </interoperability_requirements>
    </validation_logic>
    <testing_scenarios>
      <sequential_module_usage>Pattern followed by other modules</sequential_module_usage>
      <parallel_module_usage>Pattern used simultaneously with other modules</parallel_module_usage>
      <complex_workflows>Multi-step workflows involving multiple modules</complex_workflows>
    </testing_scenarios>
    <severity>Medium - affects framework ecosystem functionality</severity>
  </module_interoperability>
  
  <ecosystem_fit>
    <rule_id>INTEGRATION-003</rule_id>
    <rule_name>Framework Ecosystem Alignment</rule_name>
    <description>Pattern must align with framework principles and architecture</description>
    <validation_logic>
      <principle_alignment>
        <single_source_truth>Doesn't duplicate functionality from other patterns</single_source_truth>
        <modular_composition>Can be combined with other patterns appropriately</modular_composition>
        <zero_redundancy>Provides unique value not available elsewhere</zero_redundancy>
        <rapid_iteration>Supports framework's rapid development goals</rapid_iteration>
      </principle_alignment>
      <architectural_compliance>
        <delegation_pattern>Follows framework delegation principles</delegation_pattern>
        <xml_structure>Uses framework-standard XML organization</xml_structure>
        <token_optimization>Aligns with framework token efficiency goals</token_optimization>
      </architectural_compliance>
    </validation_logic>
    <ecosystem_metrics>
      <uniqueness_score>How unique the pattern is within the ecosystem</uniqueness_score>
      <composability_score>How well it combines with existing patterns</composability_score>
      <alignment_score>How well it fits framework principles</alignment_score>
    </ecosystem_metrics>
    <severity>Medium - affects overall framework coherence</severity>
  </ecosystem_fit>
</integration_rules>

## Validation Process and Automation

### Automated Validation Pipeline

<validation_automation>
  <continuous_validation>
    <pre_commit_checks>Run basic validation before pattern commits</pre_commit_checks>
    <build_pipeline_integration>Full validation during build process</build_pipeline_integration>
    <deployment_gates>Final validation before pattern library deployment</deployment_gates>
  </continuous_validation>
  
  <validation_tools>
    <xml_validators>Standard XML schema and well-formedness checking</xml_validators>
    <content_analyzers>Semantic analysis and logical consistency checking</content_analyzers>
    <performance_testers>Automated effectiveness and efficiency testing</performance_testers>
    <integration_testers>Framework compatibility and module interoperability testing</integration_testers>
  </validation_tools>
  
  <reporting_system>
    <validation_reports>Comprehensive reports of all validation results</validation_reports>
    <failure_analysis>Detailed analysis of validation failures</failure_analysis>
    <improvement_suggestions>Specific recommendations for addressing issues</improvement_suggestions>
  </reporting_system>
</validation_automation>

### Human Review Process

<human_review>
  <review_triggers>
    <complex_patterns>Patterns with high complexity require human review</complex_patterns>
    <novel_approaches>New pattern types or innovative approaches</novel_approaches>
    <borderline_cases>Patterns that barely meet automated thresholds</borderline_cases>
    <community_contributions>All community-contributed patterns</community_contributions>
  </review_triggers>
  
  <reviewer_qualifications>
    <domain_expertise>Reviewers must have relevant domain knowledge</domain_expertise>
    <framework_knowledge>Understanding of Claude Code framework principles</framework_knowledge>
    <validation_training>Training on validation criteria and processes</validation_training>
  </reviewer_qualifications>
  
  <review_process>
    <blind_review>Reviewers don't know pattern author</blind_review>
    <multiple_reviewers>At least 2 reviewers per pattern</multiple_reviewers>
    <consensus_requirement>Agreement between reviewers or escalation process</consensus_requirement>
  </review_process>
</human_review>

---

*This validation system ensures that all patterns in the library meet high standards for quality, effectiveness, and integration, maintaining the overall excellence of the Claude Code framework.*