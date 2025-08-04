# Format Converter Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/format-converter.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>format-converter</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>data_transformation</subcategory>
  <complexity_metrics>
    <usage_complexity>medium</usage_complexity>
    <implementation_effort>hours_6</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  <assembly_compatibility>
    <compatible_components>
      <component>data-transformer</component>
      <component>input-validation</component>
      <component>output-formatter</component>
      <component>error-handler</component>
    </compatible_components>
    <incompatible_components>
      <component>none</component>
    </incompatible_components>
  </assembly_compatibility>
  <usage_patterns>
    <primary_use_case>Data format transformation and standardization</primary_use_case>
    <common_combinations>format-converter + data-transformer + output-formatter</common_combinations>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>data_processing</primary_discovery_path>
    <alternative_discovery_path>format_transformation</alternative_discovery_path>
    <key_concepts>format_conversion data_transformation parsing serialization</key_concepts>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <dependency type="input">Raw data in various formats (JSON, YAML, CSV, XML)</dependency>
    </upstream_dependencies>
    <downstream_dependencies>
      <dependency type="output">Standardized data in target format</dependency>
    </downstream_dependencies>
    <peer_alternatives>
      <alternative>data-transformer (broader data operations vs format-specific conversion)</alternative>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Converting between standard data formats</scenario>
      <scenario>API response normalization</scenario>
      <scenario>Data import/export operations</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Complex data restructuring needs</scenario>
      <scenario>Binary format processing</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>format conversion data_transformation JSON YAML CSV XML parsing serialization</keywords>
    <semantic_tags>atomic_component data_processing format_transformation input_output</semantic_tags>
    <functionality_vectors>
      <vector>data_operations</vector>
      <vector>format_conversion</vector>
      <vector>input_processing</vector>
    </functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>component</scope_level>
    <context_retention>moderate</context_retention>
    <memory_priority>7</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file>.claude/components/atomic/data-transformer.md</context_file>
      <context_file>.claude/components/atomic/input-validation.md</context_file>
    </required_context>
    <helpful_context>
      <context_file>.claude/components/atomic/output-formatter.md</context_file>
      <context_file>.claude/components/atomic/error-handler.md</context_file>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <typical_workflow_position>middle_stage_data_processing</typical_workflow_position>
    <integration_patterns>
      <pattern>input → format-converter → data-transformer → output</pattern>
      <pattern>validation → format-converter → output-formatter</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>Data format standards and conversion principles</concept_introduction>
    <skill_progression>Basic format detection → Advanced parsing → Custom format handling</skill_progression>
    <mastery_indicator>Ability to design robust format conversion with edge case handling</mastery_indicator>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Convert between different data formats:
- Detect current format (JSON, YAML, CSV, XML)
- Parse source format following established standards
- Apply format-specific conversion rules
- Generate output in target format
- Handle unsupported formats with appropriate fallbacks
- Preserve data relationships and structure
```