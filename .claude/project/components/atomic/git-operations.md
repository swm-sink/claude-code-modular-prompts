# Git Operations Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/git-operations.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>git-operations</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>version_control</subcategory>
  <complexity_metrics>
    <usage_complexity>medium</usage_complexity>
    <implementation_effort>hours_8</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  <assembly_compatibility>
    <compatible_components>
      <component>command-security-wrapper</component>
      <component>error-handler</component>
      <component>input-validation</component>
      <component>progress-indicator</component>
    </compatible_components>
    <incompatible_components>
      <component>none</component>
    </incompatible_components>
  </assembly_compatibility>
  <usage_patterns>
    <primary_use_case>Safe git version control operations with validation</primary_use_case>
    <common_combinations>git-operations + command-security-wrapper + error-handler</common_combinations>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>version_control</primary_discovery_path>
    <alternative_discovery_path>development_operations</alternative_discovery_path>
    <key_concepts>git version_control repository_management safe_commands</key_concepts>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <dependency type="input">Git command parameters and repository context</dependency>
    </upstream_dependencies>
    <downstream_dependencies>
      <dependency type="output">Git operation results and repository state</dependency>
    </downstream_dependencies>
    <peer_alternatives>
      <alternative>command-security-wrapper (broader command execution vs git-specific)</alternative>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Automated git workflows</scenario>
      <scenario>Repository status checking</scenario>
      <scenario>Safe command execution with validation</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple read-only git queries</scenario>
      <scenario>Complex interactive git operations</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>git version_control repository commands status merge conflict validation</keywords>
    <semantic_tags>atomic_component version_control development_operations command_execution</semantic_tags>
    <functionality_vectors>
      <vector>version_control_operations</vector>
      <vector>command_execution</vector>
      <vector>repository_management</vector>
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
      <context_file>.claude/components/security/command-security-wrapper.md</context_file>
      <context_file>.claude/components/atomic/input-validation.md</context_file>
    </required_context>
    <helpful_context>
      <context_file>.claude/components/atomic/error-handler.md</context_file>
      <context_file>.claude/components/atomic/progress-indicator.md</context_file>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <typical_workflow_position>development_operations</typical_workflow_position>
    <integration_patterns>
      <pattern>validation → git-operations → error-handler</pattern>
      <pattern>git-status → git-operations → progress-indicator</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>Safe git command execution and repository management</concept_introduction>
    <skill_progression>Basic git commands → Advanced workflow automation → Custom git integrations</skill_progression>
    <mastery_indicator>Ability to design secure automated git workflows with proper error handling</mastery_indicator>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
process git version control operations:
- Parse and examine input parameters for validation
- Execute git commands safely with validation
- Check repository status before operations
- process merge conflicts and error conditions
- Provide clear feedback on operation results
- Ensure working directory cleanliness
```