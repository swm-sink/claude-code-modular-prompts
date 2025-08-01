# Output Formatter Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/output-formatter.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>output-formatter</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>user_interface</subcategory>
  
  <complexity_metrics>
    <usage_complexity>simple</usage_complexity>
    <implementation_effort>minutes_15</implementation_effort>
    <prerequisite_knowledge>basic</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="response-validator" strength="strong"/>
      <component ref="file-writer" strength="strong"/>
      <component ref="progress-indicator" strength="medium"/>
      <component ref="data-transformer" strength="medium"/>
      <component ref="task-summary" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="parameter-parser" reason="different_processing_stages"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>data_presentation</common_workflow>
    <typical_position>output</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_user_interface</primary_discovery_path>
    <alternative_paths>
      <path>data_presentation</path>
      <path>output_formatting</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="data-transformer" relation="data_processing"/>
      <file type="component" ref="response-validator" relation="data_validation"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="file-writer" relation="file_output"/>
      <file type="user_interface" ref="display" relation="user_presentation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="task-summary" similarity="0.50"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Presenting data in user-friendly formats</scenario>
      <scenario>Converting raw data to structured output (tables, lists)</scenario>
      <scenario>Preparing data for display or file output</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Data transformation (use data-transformer instead)</scenario>
      <scenario>Raw file storage (use file-writer directly)</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>output formatting presentation display data visualization user interface</keywords>
    <semantic_tags>output_formatting data_presentation user_interface</semantic_tags>
    <functionality_vectors>formatting presentation visualization</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>6</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="low"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/llm-antipatterns.md" importance="low"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>output_processing</workflow_stage>
    <integration_patterns>
      <pattern>data_presentation_pipeline</pattern>
      <pattern>format_conversion</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>output_formatting</concept_introduction>
    <skill_progression>beginner</skill_progression>
    <mastery_indicators>
      <indicator>Can format complex data structures for readability</indicator>
      <indicator>Chooses appropriate output formats based on data type</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Format output with structured presentation:
- Parse input data and detect current format (JSON, YAML, plain text)
- Apply consistent headers with hierarchical numbering for sections
- Generate bullet points with proper indentation for list structures
- Wrap technical content in appropriate code blocks with syntax highlighting
- Handle unsupported formats using markdown fallback with clear labels
- Create concise summaries with key metrics and actionable next steps
```