# Search Files Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/search-files.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>search-files</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>file_operations</subcategory>
  <complexity_metrics>
    <usage_complexity>low</usage_complexity>
    <implementation_effort>hours_2</implementation_effort>
    <prerequisite_knowledge>beginner</prerequisite_knowledge>
  </complexity_metrics>
  <assembly_compatibility>
    <compatible_components>
      <component>file-reader</component>
      <component>input-validation</component>
      <component>output-formatter</component>
      <component>error-handler</component>
    </compatible_components>
    <incompatible_components>
      <component>none</component>
    </incompatible_components>
  </assembly_compatibility>
  <usage_patterns>
    <primary_use_case>File and content search operations using Grep and Glob</primary_use_case>
    <common_combinations>search-files + file-reader + output-formatter</common_combinations>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>file_operations</primary_discovery_path>
    <alternative_discovery_path>content_search</alternative_discovery_path>
    <key_concepts>file_search content_search grep glob patterns</key_concepts>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <dependency type="input">Search patterns and file criteria</dependency>
    </upstream_dependencies>
    <downstream_dependencies>
      <dependency type="output">Search results and matched content</dependency>
    </downstream_dependencies>
    <peer_alternatives>
      <alternative>file-reader (reads specific files vs searches for files)</alternative>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Finding files by name or pattern</scenario>
      <scenario>Searching content within files</scenario>
      <scenario>Code discovery and exploration</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Reading specific known files</scenario>
      <scenario>Complex database-style queries</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>file_search content_search grep glob patterns text_search file_discovery</keywords>
    <semantic_tags>atomic_component file_operations search_operations content_discovery</semantic_tags>
    <functionality_vectors>
      <vector>file_operations</vector>
      <vector>search_operations</vector>
      <vector>content_discovery</vector>
    </functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>component</scope_level>
    <context_retention>low</context_retention>
    <memory_priority>6</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file>.claude/components/atomic/file-reader.md</context_file>
    </required_context>
    <helpful_context>
      <context_file>.claude/components/atomic/input-validation.md</context_file>
      <context_file>.claude/components/atomic/output-formatter.md</context_file>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <typical_workflow_position>early_stage_discovery</typical_workflow_position>
    <integration_patterns>
      <pattern>search-files → file-reader → processing</pattern>
      <pattern>input → search-files → output-formatter</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>File system search operations and pattern matching</concept_introduction>
    <skill_progression>Basic file finding → Advanced pattern matching → Complex search strategies</skill_progression>
    <mastery_indicator>Ability to design efficient search workflows for large codebases</mastery_indicator>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
To search for content:
- Accept and parse input data or parameters
- apply Grep for text patterns
- apply Glob for file patterns
- Combine both for targeted searches
- Handle errors and edge cases according to defined criteria
- Report findings clearly
```