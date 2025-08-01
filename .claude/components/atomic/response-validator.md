# Response Validator Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/response-validator.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>response-validator</component_id>
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
      <component ref="api-caller" strength="strong"/>
      <component ref="data-transformer" strength="strong"/>
      <component ref="output-formatter" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="input-validation" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="parameter-parser" reason="different_validation_scope"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>quality_assurance</common_workflow>
    <typical_position>processing</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_validation</primary_discovery_path>
    <alternative_paths>
      <path>quality_assurance</path>
      <path>output_validation</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="api-caller" relation="response_source"/>
      <file type="component" ref="data-transformer" relation="processed_data"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="output-formatter" relation="validated_output"/>
      <file type="component" ref="error-handler" relation="validation_errors"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="input-validation" similarity="0.75"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Validating API responses before processing</scenario>
      <scenario>Ensuring data integrity after transformations</scenario>
      <scenario>Quality checking automated outputs</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Input validation (use input-validation instead)</scenario>
      <scenario>Simple existence checks without schema validation</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>response validation output validation quality assurance data integrity schema validation</keywords>
    <semantic_tags>output_validation quality_assurance data_integrity</semantic_tags>
    <functionality_vectors>validation quality_checking output_verification</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>8</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../quality/quality-metrics.md" importance="high"/>
      <context_file ref="../context/llm-antipatterns.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>quality_assurance</workflow_stage>
    <integration_patterns>
      <pattern>validation_pipeline</pattern>
      <pattern>quality_gate</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>response_validation</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>Can validate complex response structures against schemas</indicator>
      <indicator>Provides meaningful validation error messages</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Validate response structure and content:
- Check response format matches expected schema
- Verify all required fields are present
- Validate data types and value ranges
- Ensure response completeness and accuracy
- Handle unsupported formats with appropriate fallbacks
- Flag any structural inconsistencies
```