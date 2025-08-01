# File Reader Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/file-reader.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>file-reader</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>io_operations</subcategory>
  
  <complexity_metrics>
    <usage_complexity>simple</usage_complexity>
    <implementation_effort>minutes_5</implementation_effort>
    <prerequisite_knowledge>basic</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="data-transformer" strength="strong"/>
      <component ref="output-formatter" strength="strong"/>
      <component ref="error-handler" strength="required"/>
      <component ref="path-validation" strength="required"/>
      <component ref="content-sanitizer" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="file-writer" reason="conflicting_io_operations"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>data_ingestion</common_workflow>
    <common_workflow>file_processing</common_workflow>
    <common_workflow>content_analysis</common_workflow>
    <typical_position>entry_point</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_components_io</primary_discovery_path>
    <alternative_paths>
      <path>file_operations</path>
      <path>data_input_components</path>
      <path>basic_building_blocks</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="path-validation" relation="prerequisite"/>
      <file type="context" ref=".claude/context/file-handling-patterns.md" relation="best_practices"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="data-transformer" relation="common_next_step"/>
      <file type="component" ref="format-converter" relation="data_processing"/>
      <file type="command" ref="analyze-code" relation="uses_for_input"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="stream-reader" similarity="0.70"/>
      <file type="component" ref="bulk-file-reader" similarity="0.65"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>reading_single_file_contents</scenario>
      <scenario>loading_configuration_files</scenario>
      <scenario>parsing_structured_data</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>reading_multiple_files_in_bulk</scenario>
      <scenario>streaming_large_files</scenario>
      <scenario>binary_file_processing</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>file reader read content input io atomic component</keywords>
    <semantic_tags>file_operations input_handling data_loading basic_io</semantic_tags>
    <functionality_vectors>[0.9, 0.1, 0.2, 0.3, 0.8]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>temporary</context_retention>
    <memory_priority>6</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref=".claude/context/claude-code-tools.md" importance="high"/>
      <context_file ref=".claude/context/error-handling-patterns.md" importance="medium"/>
    </required_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>entry_point</workflow_stage>
    <integration_patterns>
      <pattern>file_validation</pattern>
      <pattern>content_reading</pattern>
      <pattern>error_handling</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>basic_file_operations</concept_introduction>
    <skill_progression>beginner</skill_progression>
    <mastery_indicators>
      <indicator>successful_file_reading</indicator>
      <indicator>proper_error_handling</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Read file contents with error handling:
- Validate file path format and accessibility permissions
- Execute Read tool with absolute path and optional line limits
- Parse file content according to detected file type (text, binary, structured)
- Handle file not found errors with specific path recommendations
- Extract and return relevant content sections based on requirements
- Generate structured report of read operation results and metadata
```