# API Caller Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/api-caller.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>api-caller</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>system_operations</subcategory>
  
  <complexity_metrics>
    <usage_complexity>simple</usage_complexity>
    <implementation_effort>minutes_15</implementation_effort>
    <prerequisite_knowledge>basic</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="response-validator" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="parameter-parser" strength="medium"/>
      <component ref="output-formatter" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="file-writer" reason="different_data_flow_patterns"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>api_integration</common_workflow>
    <typical_position>processing</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_system_operations</primary_discovery_path>
    <alternative_paths>
      <path>external_integration</path>
      <path>data_retrieval</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="parameter-parser" relation="input_preparation"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="response-validator" relation="output_validation"/>
      <file type="component" ref="error-handler" relation="error_processing"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="file-reader" similarity="0.30"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Need to integrate with external APIs or services</scenario>
      <scenario>Retrieving data from REST endpoints</scenario>
      <scenario>Submitting data to external systems</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Working with local files or databases</scenario>
      <scenario>Simple string processing tasks</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>api http rest authentication requests responses external integration</keywords>
    <semantic_tags>network_communication external_services data_exchange</semantic_tags>
    <functionality_vectors>network_operations data_retrieval authentication</functionality_vectors>
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
      <pattern>external_api_integration</pattern>
      <pattern>request_response_cycle</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>api_integration</concept_introduction>
    <skill_progression>beginner</skill_progression>
    <mastery_indicators>
      <indicator>Can construct proper API requests with authentication</indicator>
      <indicator>Handles API errors and rate limiting appropriately</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
generate API calls with proper handling:
- Construct API requests with headers and parameters
- process authentication and authorization
- coordinate request timeouts and retries
- Parse and validate API responses
- process API errors and rate limiting
```