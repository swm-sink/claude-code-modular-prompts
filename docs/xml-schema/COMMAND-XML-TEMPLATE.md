# Command XML Template

This template provides the standardized XML metadata structure for all command files.

## Template Structure

```xml
<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>{{FULL_FILE_PATH}}</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>{{COMMAND_NAME}}</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>{{1|2|3|N/A}}</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="{{COMPONENT_NAME}}" role="{{ROLE_DESCRIPTION}}"/>
    </required_components>
    <optional_components>
      <component ref="{{COMPONENT_NAME}}" benefit="{{BENEFIT_DESCRIPTION}}"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>{{true|false}}</can_invoke_commands>
    <invokable_commands>
      <command ref="{{COMMAND_NAME}}" context="{{CONTEXT_DESCRIPTION}}"/>
    </invokable_commands>
    <orchestration_patterns>{{PATTERN_LIST}}</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>{{TASK_DESCRIPTION}}</task_description>
    <implementation_strategy>{{STRATEGY_STEPS}}</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>{{PRIMARY_PATH}}</primary_discovery_path>
    <alternative_paths>
      <path>{{ALTERNATIVE_PATH}}</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="{{TYPE}}" ref="{{FILE_REFERENCE}}" relation="{{RELATIONSHIP}}"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="{{TYPE}}" ref="{{FILE_REFERENCE}}" relation="{{RELATIONSHIP}}"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="{{TYPE}}" ref="{{FILE_REFERENCE}}" similarity="{{0.00-1.00}}"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>{{SCENARIO_DESCRIPTION}}</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>{{SCENARIO_DESCRIPTION}}</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>{{KEYWORD_LIST}}</keywords>
    <semantic_tags>{{SEMANTIC_TAG_LIST}}</semantic_tags>
    <functionality_vectors>{{VECTOR_VALUES}}</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>{{local|project|global}}</scope_level>
    <context_retention>{{session|persistent|temporary}}</context_retention>
    <memory_priority>{{1-10}}</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="{{FILE_REFERENCE}}" importance="{{critical|high|medium|low}}"/>
    </required_context>
    <helpful_context>
      <context_file ref="{{FILE_REFERENCE}}" importance="{{critical|high|medium|low}}"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>{{STAGE_NAME}}</workflow_stage>
    <integration_patterns>
      <pattern>[PATTERN_NAME]</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>[CONCEPT_NAME]</concept_introduction>
    <skill_progression>[beginner|intermediate|advanced]</skill_progression>
    <mastery_indicators>
      <indicator>[MASTERY_INDICATOR]</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->
```

## Field Descriptions

### Command-Specific Fields
- `command_id`: The command name (e.g., "quick-command")
- `progressive_disclosure_layer`: 1=Auto-generation, 2=Guided, 3=Assembly, N/A=Other
- `component_dependencies`: Required and optional components
- `orchestration_capability`: Commands this command can invoke
- `v2_features`: Enhanced v1.0 capabilities

### Usage Notes
- All commands should have `command_count: 88`
- Use `ai_consumption_priority: critical` for core commands
- Include realistic component dependencies and orchestration patterns
- Ensure `file_path` reflects actual file location