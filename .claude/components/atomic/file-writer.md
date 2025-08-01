# File Writer Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/file-writer.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>file-writer</component_id>
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
      <component ref="file-reader" strength="strong"/>
      <component ref="output-formatter" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="content-sanitizer" strength="medium"/>
      <component ref="path-validation" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="api-caller" reason="different_data_flow_patterns"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>file_processing</common_workflow>
    <typical_position>output</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_io_operations</primary_discovery_path>
    <alternative_paths>
      <path>file_operations</path>
      <path>output_generation</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="output-formatter" relation="data_formatting"/>
      <file type="component" ref="content-sanitizer" relation="data_validation"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="filesystem" ref="output_files" relation="file_creation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="file-reader" similarity="0.90"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Saving processed data to files</scenario>
      <scenario>Creating configuration or report files</scenario>
      <scenario>Persisting analysis results</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>API output (use output-formatter instead)</scenario>
      <scenario>Temporary data storage (use state-manager instead)</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>file writing file operations output generation persistence storage</keywords>
    <semantic_tags>file_operations output_generation data_persistence</semantic_tags>
    <functionality_vectors>file_io output_processing data_storage</functionality_vectors>
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
      <context_file ref="../context/comprehensive-project-learnings.md" importance="medium"/>
    </required_context>
    <helpful_context>
      <context_file ref="../security/path-validation.md" importance="high"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>output_generation</workflow_stage>
    <integration_patterns>
      <pattern>file_processing_pipeline</pattern>
      <pattern>secure_file_operations</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>file_operations</concept_introduction>
    <skill_progression>beginner</skill_progression>
    <mastery_indicators>
      <indicator>Can safely write files with proper error handling</indicator>
      <indicator>Validates file paths and handles permissions appropriately</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
To write or update files:
- Accept and parse input data or parameters
- apply Write tool for new files
- apply Edit tool for existing files
- Confirm before overwriting
- Handle errors and edge cases according to defined criteria
- Report what was written
```