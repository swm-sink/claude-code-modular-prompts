# State Manager Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/state-manager.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>state-manager</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>workflow_control</subcategory>
  
  <complexity_metrics>
    <usage_complexity>complex</usage_complexity>
    <implementation_effort>hours_1</implementation_effort>
    <prerequisite_knowledge>advanced</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="workflow-coordinator" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="progress-indicator" strength="strong"/>
      <component ref="completion-tracker" strength="medium"/>
      <component ref="dependency-resolver" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="file-writer" reason="different_persistence_patterns"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>complex_orchestration</common_workflow>
    <typical_position>utility</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_workflow_control</primary_discovery_path>
    <alternative_paths>
      <path>state_management</path>
      <path>workflow_orchestration</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="parameter-parser" relation="configuration_input"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="workflow-coordinator" relation="state_coordination"/>
      <file type="component" ref="progress-indicator" relation="progress_tracking"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="completion-tracker" similarity="0.50"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Complex workflows requiring state persistence</scenario>
      <scenario>Multi-step operations with rollback capabilities</scenario>
      <scenario>Workflows that need to resume from checkpoints</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple, stateless operations</scenario>
      <scenario>Single-step tasks without persistence needs</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>state management workflow state persistence checkpoints rollback coordination</keywords>
    <semantic_tags>state_management workflow_control persistence</semantic_tags>
    <functionality_vectors>state_coordination workflow_management persistence</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../orchestration/workflow-patterns.md" importance="critical"/>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/llm-antipatterns.md" importance="high"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>state_management</workflow_stage>
    <integration_patterns>
      <pattern>checkpoint_recovery</pattern>
      <pattern>atomic_transactions</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>state_management</concept_introduction>
    <skill_progression>advanced</skill_progression>
    <mastery_indicators>
      <indicator>Can implement atomic state transitions with rollback</indicator>
      <indicator>Manages complex workflow state across multiple operations</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Coordinate command execution state management:
- Initialize state variables from parsed configuration file parameters
- Track workflow progress using timestamped checkpoint files
- Execute atomic state transitions with immediate rollback on errors
- Validate state consistency using checksum verification across operations
- Persist state changes to designated JSON/YAML storage files  
- Generate state reports with detailed error messages and recovery steps
```