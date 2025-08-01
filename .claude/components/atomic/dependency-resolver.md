# Dependency Resolver Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/dependency-resolver.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>dependency-resolver</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>dependency_management</subcategory>
  <complexity_metrics>
    <usage_complexity>high</usage_complexity>
    <implementation_effort>days_1</implementation_effort>
    <prerequisite_knowledge>expert</prerequisite_knowledge>
  </complexity_metrics>
  <assembly_compatibility>
    <compatible_components>
      <component>workflow-coordinator</component>
      <component>task-planning</component>
      <component>dag-orchestrator</component>
      <component>error-handler</component>
    </compatible_components>
    <incompatible_components>
      <component>none</component>
    </incompatible_components>
  </assembly_compatibility>
  <usage_patterns>
    <primary_use_case>Complex workflow dependency resolution and management</primary_use_case>
    <common_combinations>dependency-resolver + task-planning + workflow-coordinator</common_combinations>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>workflow_orchestration</primary_discovery_path>
    <alternative_discovery_path>dependency_management</alternative_discovery_path>
    <key_concepts>dependencies resolution topological_sort versioning</key_concepts>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <dependency type="input">Dependency specifications and manifest files</dependency>
    </upstream_dependencies>
    <downstream_dependencies>
      <dependency type="output">Resolved dependency graph and loading order</dependency>
    </downstream_dependencies>
    <peer_alternatives>
      <alternative>task-planning (broader task analysis vs specific dependency focus)</alternative>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Complex multi-component workflows</scenario>
      <scenario>Version conflict resolution needed</scenario>
      <scenario>Dependency graph analysis required</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple linear workflows</scenario>
      <scenario>Single-component operations</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>dependency resolution versioning graph_analysis topological_sort manifest</keywords>
    <semantic_tags>atomic_component workflow_management dependency_management orchestration</semantic_tags>
    <functionality_vectors>
      <vector>dependency_operations</vector>
      <vector>workflow_orchestration</vector>
      <vector>graph_analysis</vector>
    </functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>component</scope_level>
    <context_retention>high</context_retention>
    <memory_priority>8</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file>.claude/components/orchestration/dag-orchestrator.md</context_file>
      <context_file>.claude/components/orchestration/task-planning.md</context_file>
    </required_context>
    <helpful_context>
      <context_file>.claude/components/atomic/workflow-coordinator.md</context_file>
      <context_file>.claude/components/atomic/error-handler.md</context_file>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <typical_workflow_position>early_stage_planning</typical_workflow_position>
    <integration_patterns>
      <pattern>dependency-resolver → task-planning → workflow-coordinator</pattern>
      <pattern>manifest-analysis → dependency-resolver → execution-order</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>Dependency graph theory and topological sorting</concept_introduction>
    <skill_progression>Basic dependency tracking → Advanced conflict resolution → Complex graph optimization</skill_progression>
    <mastery_indicator>Ability to design custom dependency resolution strategies for domain-specific workflows</mastery_indicator>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Resolve component and resource dependencies:
- Parse dependency specifications from manifest files
- Verify dependency availability in specified locations
- Detect and resolve version conflicts using semantic versioning
- Execute dependency loading in topological order
- Report missing dependencies with specific installation commands
- Handle circular dependencies with clear error messages
```