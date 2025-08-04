# Content Sanitizer Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/content-sanitizer.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>content-sanitizer</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>security</subcategory>
  <complexity_metrics>
    <usage_complexity>medium</usage_complexity>
    <implementation_effort>hours_4</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  <assembly_compatibility>
    <compatible_components>
      <component>input-validation</component>
      <component>error-handler</component>
      <component>output-formatter</component>
      <component>response-validator</component>
    </compatible_components>
    <incompatible_components>
      <component>none</component>
    </incompatible_components>
  </assembly_compatibility>
  <usage_patterns>
    <primary_use_case>Input security validation and sanitization</primary_use_case>
    <common_combinations>content-sanitizer + input-validation + error-handler</common_combinations>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>security_validation</primary_discovery_path>
    <alternative_discovery_path>input_processing</alternative_discovery_path>
    <key_concepts>sanitization security validation input_cleaning</key_concepts>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <dependency type="input">Raw content from various sources</dependency>
    </upstream_dependencies>
    <downstream_dependencies>
      <dependency type="output">Sanitized content for further processing</dependency>
    </downstream_dependencies>
    <peer_alternatives>
      <alternative>input-validation (focuses on validation vs sanitization)</alternative>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Processing user-generated content</scenario>
      <scenario>Handling external data sources</scenario>
      <scenario>Content security requirements</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Trusted internal data sources</scenario>
      <scenario>Performance-critical simple text processing</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>content security sanitization validation input_cleaning safety</keywords>
    <semantic_tags>security atomic_component data_processing input_validation</semantic_tags>
    <functionality_vectors>
      <vector>security_operations</vector>
      <vector>content_processing</vector>
      <vector>data_validation</vector>
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
      <context_file>.claude/components/atomic/input-validation.md</context_file>
      <context_file>.claude/components/security/harm-prevention-framework.md</context_file>
    </required_context>
    <helpful_context>
      <context_file>.claude/components/atomic/error-handler.md</context_file>
      <context_file>.claude/components/atomic/output-formatter.md</context_file>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <typical_workflow_position>early_stage_input_processing</typical_workflow_position>
    <integration_patterns>
      <pattern>content-sanitizer → input-validation → processing</pattern>
      <pattern>input → content-sanitizer → error-handler → output</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>Basic content sanitization principles</concept_introduction>
    <skill_progression>Security-aware input processing → Advanced sanitization patterns</skill_progression>
    <mastery_indicator>Ability to design custom sanitization rules for specific content types</mastery_indicator>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Sanitize input content for security:
- Remove potentially harmful code or scripts
- Escape special characters and markup
- Validate against whitelist patterns
- Strip unnecessary metadata and formatting
- Handle unsupported formats with appropriate fallbacks
- Ensure content meets safety standards
```