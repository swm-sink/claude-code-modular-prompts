# Input Validation Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/input-validation.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>input-validation</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>validation</subcategory>
  
  <complexity_metrics>
    <usage_complexity>moderate</usage_complexity>
    <implementation_effort>minutes_15</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="parameter-parser" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="response-validator" strength="strong"/>
      <component ref="content-sanitizer" strength="medium"/>
      <component ref="data-transformer" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="output-formatter" reason="different_processing_direction"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>input_processing</common_workflow>
    <typical_position>entry_point</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_validation</primary_discovery_path>
    <alternative_paths>
      <path>security_validation</path>
      <path>input_processing</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="parameter-parser" relation="input_parsing"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="data-transformer" relation="validated_data_processing"/>
      <file type="component" ref="error-handler" relation="validation_error_handling"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="response-validator" similarity="0.70"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Validating user input against defined schemas</scenario>
      <scenario>Checking required parameters and data types</scenario>
      <scenario>Preventing injection attacks and invalid data</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Output validation (use response-validator instead)</scenario>
      <scenario>Simple existence checks without validation rules</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>input validation security data validation parameter checking schema validation</keywords>
    <semantic_tags>input_validation security_validation data_integrity</semantic_tags>
    <functionality_vectors>validation security_checking data_verification</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../security/input-validation-framework.md" importance="critical"/>
      <context_file ref="../context/llm-antipatterns.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>input_processing</workflow_stage>
    <integration_patterns>
      <pattern>security_validation_chain</pattern>
      <pattern>data_integrity_pipeline</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>input_validation</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>Can implement comprehensive validation rules</indicator>
      <indicator>Prevents common security vulnerabilities through input validation</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Validate the provided input:
- Check for required parameters
- Verify data types match expectations
- Validate input ranges and constraints
- Return clear error messages if validation fails
- Continue only with valid inputs
```