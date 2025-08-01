# Parameter Parser Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/parameter-parser.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>parameter-parser</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>io_operations</subcategory>
  
  <complexity_metrics>
    <usage_complexity>moderate</usage_complexity>
    <implementation_effort>minutes_15</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="input-validation" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="api-caller" strength="medium"/>
      <component ref="data-transformer" strength="medium"/>
      <component ref="output-formatter" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="file-reader" reason="different_input_source_patterns"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>command_processing</common_workflow>
    <typical_position>entry_point</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_io_operations</primary_discovery_path>
    <alternative_paths>
      <path>command_line_processing</path>
      <path>input_validation</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="raw_input" ref="command_line_args" relation="input_source"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="input-validation" relation="validation_pipeline"/>
      <file type="component" ref="data-transformer" relation="parameter_processing"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="input-validation" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Processing command-line arguments with complex validation</scenario>
      <scenario>Parsing configuration parameters from multiple sources</scenario>
      <scenario>Handling parameter aliases and shorthand notation</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple parameter passing without validation needs</scenario>
      <scenario>File-based configuration (use file-reader instead)</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>parameter parsing command line arguments validation configuration input processing</keywords>
    <semantic_tags>input_processing argument_parsing parameter_validation</semantic_tags>
    <functionality_vectors>command_processing input_validation parameter_handling</functionality_vectors>
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
    <workflow_stage>input_processing</workflow_stage>
    <integration_patterns>
      <pattern>command_line_interface</pattern>
      <pattern>parameter_validation_chain</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>parameter_parsing</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>Can handle complex parameter schemas with validation rules</indicator>
      <indicator>Provides clear error messages for invalid parameter formats</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Parse command arguments with validation:
- Extract named parameters using regex patterns (--flag=value, -f value)
- Process positional arguments in specified order with type checking
- Apply default values for optional parameters from configuration
- Validate parameter combinations against defined schema rules
- Generate detailed error messages for invalid parameter formats
- Support parameter aliases and shorthand notation
```