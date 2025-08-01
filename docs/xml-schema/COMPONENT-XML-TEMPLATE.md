# Component XML Template

This template provides the standardized XML metadata structure for all component files.

## Template Structure

```xml
<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>{{FULL_FILE_PATH}}</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>{{COMPONENT_NAME}}</component_id>
  <component_count>91</component_count>
  <category>{{CATEGORY_NAME}}</category>
  <subcategory>{{SUBCATEGORY_NAME}}</subcategory>
  
  <complexity_metrics>
    <usage_complexity>{{simple|moderate|complex}}</usage_complexity>
    <implementation_effort>{{minutes_5|minutes_15|hours_1|hours_3}}</implementation_effort>
    <prerequisite_knowledge>{{basic|intermediate|advanced}}</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="{{COMPONENT_NAME}}" strength="{{required|strong|medium|weak}}"/>
    </compatible_components>
    <incompatible_components>
      <component ref="{{COMPONENT_NAME}}" reason="{{REASON_DESCRIPTION}}"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>{{WORKFLOW_NAME}}</common_workflow>
    <typical_position>{{entry_point|processing|output|utility}}</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>{{CATEGORY_PATH}}</primary_discovery_path>
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
      <pattern>{{PATTERN_NAME}}</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>{{CONCEPT_NAME}}</concept_introduction>
    <skill_progression>{{beginner|intermediate|advanced}}</skill_progression>
    <mastery_indicators>
      <indicator>{{MASTERY_INDICATOR}}</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->
```

## Component Categories

### Valid Categories
- **atomic**: Single-purpose building blocks (21 components)
- **analysis**: Code and data analysis capabilities
- **orchestration**: Complex workflow management  
- **security**: Enterprise security frameworks
- **performance**: Optimization and efficiency
- **intelligence**: Advanced AI capabilities
- **context**: Claude understanding management
- **constitutional**: AI safety frameworks
- **quality**: Quality assurance components
- **reasoning**: Enhanced reasoning capabilities
- **workflow**: Workflow execution control
- **testing**: Testing and validation
- **other**: Specialized categories

### Subcategory Examples
- **atomic**: io_operations, data_processing, workflow_control, system_operations, user_interface, validation
- **security**: protection, validation, compliance
- **performance**: optimization, automation, scaling
- **intelligence**: architecture, coordination, reasoning

## Field Descriptions

### Component-Specific Fields
- `component_id`: The component name (e.g., "file-reader")
- `category`: Primary functional category
- `subcategory`: More specific categorization
- `complexity_metrics`: Implementation difficulty and time investment
- `assembly_compatibility`: Which components work well together
- `usage_patterns`: Common workflows and typical usage position

### Usage Notes
- All components should have `component_count: 91`
- Use `ai_consumption_priority: high` for most components
- Include realistic compatibility and incompatibility relationships
- Focus assembly_compatibility on the most common integration patterns