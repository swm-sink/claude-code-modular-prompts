# User Confirmation Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/user-confirmation.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>user-confirmation</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>user_interaction</subcategory>
  <complexity_metrics>
    <usage_complexity>low</usage_complexity>
    <implementation_effort>hours_2</implementation_effort>
    <prerequisite_knowledge>beginner</prerequisite_knowledge>
  </complexity_metrics>
  <assembly_compatibility>
    <compatible_components>
      <component>harm-prevention-framework</component>
      <component>error-handler</component>
      <component>output-formatter</component>
      <component>progress-indicator</component>
    </compatible_components>
    <incompatible_components>
      <component>none</component>
    </incompatible_components>
  </assembly_compatibility>
  <usage_patterns>
    <primary_use_case>Safety confirmation for destructive or risky operations</primary_use_case>
    <common_combinations>user-confirmation + harm-prevention-framework + error-handler</common_combinations>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>safety_operations</primary_discovery_path>
    <alternative_discovery_path>user_interaction</alternative_discovery_path>
    <key_concepts>user_confirmation safety_prompts destructive_actions user_consent</key_concepts>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <dependency type="input">Action description and affected resources</dependency>
    </upstream_dependencies>
    <downstream_dependencies>
      <dependency type="output">User consent and approval status</dependency>
    </downstream_dependencies>
    <peer_alternatives>
      <alternative>harm-prevention-framework (broader safety vs specific confirmation)</alternative>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Before destructive file operations</scenario>
      <scenario>Before system-wide changes</scenario>
      <scenario>Before irreversible actions</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Read-only operations</scenario>
      <scenario>Frequent low-risk actions</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>user_confirmation safety_prompts destructive_actions consent approval user_interaction</keywords>
    <semantic_tags>atomic_component safety_operations user_interaction risk_management</semantic_tags>
    <functionality_vectors>
      <vector>safety_operations</vector>
      <vector>user_interaction</vector>
      <vector>risk_management</vector>
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
      <context_file>.claude/components/security/harm-prevention-framework.md</context_file>
    </required_context>
    <helpful_context>
      <context_file>.claude/components/atomic/error-handler.md</context_file>
      <context_file>.claude/components/atomic/output-formatter.md</context_file>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <typical_workflow_position>pre_execution_safety_check</typical_workflow_position>
    <integration_patterns>
      <pattern>risk-assessment → user-confirmation → execution</pattern>
      <pattern>user-confirmation → error-handler → feedback</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>User consent patterns and safety confirmation principles</concept_introduction>
    <skill_progression>Basic confirmation prompts → Risk-aware messaging → Advanced consent workflows</skill_progression>
    <mastery_indicator>Ability to design intuitive safety confirmation patterns that prevent accidental actions</mastery_indicator>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Before destructive actions:
- Accept and parse input data or parameters
- Clearly explain what will happen
- List affected files/resources
- Ask "execute you want to proceed?"
- Handle errors and edge cases according to defined criteria
- Wait for explicit confirmation
```