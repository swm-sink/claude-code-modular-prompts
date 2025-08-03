# Error Handler Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/error-handler.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>error-handler</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>workflow_control</subcategory>
  
  <complexity_metrics>
    <usage_complexity>simple</usage_complexity>
    <implementation_effort>minutes_15</implementation_effort>
    <prerequisite_knowledge>basic</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="api-caller" strength="strong"/>
      <component ref="file-reader" strength="strong"/>
      <component ref="data-transformer" strength="strong"/>
      <component ref="response-validator" strength="medium"/>
      <component ref="progress-indicator" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="user-confirmation" reason="conflicting_user_interaction_patterns"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>error_recovery</common_workflow>
    <typical_position>utility</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_workflow_control</primary_discovery_path>
    <alternative_paths>
      <path>error_management</path>
      <path>reliability_patterns</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="any" relation="error_source"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="progress-indicator" relation="status_reporting"/>
      <file type="component" ref="task-summary" relation="error_documentation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="response-validator" similarity="0.40"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Any component that might fail or produce errors</scenario>
      <scenario>Complex workflows requiring graceful failure handling</scenario>
      <scenario>User-facing operations that need clear error messages</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple, single-step operations with minimal failure risk</scenario>
      <scenario>Internal utility functions with predictable inputs</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>error handling exception management failure recovery debugging logging</keywords>
    <semantic_tags>reliability fault_tolerance error_recovery</semantic_tags>
    <functionality_vectors>error_processing failure_management reliability</functionality_vectors>
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
      <context_file ref="../context/llm-antipatterns.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>error_management</workflow_stage>
    <integration_patterns>
      <pattern>try_catch_wrapper</pattern>
      <pattern>graceful_degradation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>error_handling</concept_introduction>
    <skill_progression>beginner</skill_progression>
    <mastery_indicators>
      <indicator>Can categorize different types of errors appropriately</indicator>
      <indicator>Provides clear, actionable error messages to users</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
If an error occurs:
- Identify the error type (user input, system, logic)
- Provide a clear, actionable error message
- Suggest next steps to resolve
- Log the error for debugging
```