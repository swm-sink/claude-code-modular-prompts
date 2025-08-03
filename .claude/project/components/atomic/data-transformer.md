# Data Transformer Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/data-transformer.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>data-transformer</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>data_processing</subcategory>
  
  <complexity_metrics>
    <usage_complexity>moderate</usage_complexity>
    <implementation_effort>minutes_15</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="format-converter" strength="strong"/>
      <component ref="response-validator" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="input-validation" strength="medium"/>
      <component ref="output-formatter" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="user-confirmation" reason="automated_processing_conflicts"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>data_pipeline</common_workflow>
    <typical_position>processing</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_data_processing</primary_discovery_path>
    <alternative_paths>
      <path>data_conversion</path>
      <path>format_transformation</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="input-validation" relation="data_validation"/>
      <file type="component" ref="parameter-parser" relation="transformation_config"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="output-formatter" relation="output_processing"/>
      <file type="component" ref="response-validator" relation="result_validation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="format-converter" similarity="0.85"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Converting data between different formats (JSON, CSV, XML)</scenario>
      <scenario>Normalizing data structures for processing</scenario>
      <scenario>Cleaning and preprocessing raw data</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple format conversions (use format-converter instead)</scenario>
      <scenario>UI data presentation (use output-formatter instead)</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>data transformation format conversion preprocessing normalization validation</keywords>
    <semantic_tags>data_processing format_conversion data_pipeline</semantic_tags>
    <functionality_vectors>data_manipulation format_transformation preprocessing</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>7</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="medium"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/llm-antipatterns.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>data_processing</workflow_stage>
    <integration_patterns>
      <pattern>etl_pipeline</pattern>
      <pattern>data_validation_chain</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>data_transformation</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>Can preserve data integrity during complex transformations</indicator>
      <indicator>Handles nested structures and edge cases appropriately</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Transform data between different formats:
- Identify source and target data formats
- Apply appropriate transformation rules
- Preserve data integrity during conversion
- process nested structures and arrays
- Handle transformation failures gracefully
- Validate transformation completeness
```