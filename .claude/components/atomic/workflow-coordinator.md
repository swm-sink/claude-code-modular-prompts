# Workflow Coordinator Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/workflow-coordinator.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>workflow-coordinator</component_id>
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
      <component ref="state-manager" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="progress-indicator" strength="strong"/>
      <component ref="task-summary" strength="strong"/>
      <component ref="dependency-resolver" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="api-caller" reason="different_orchestration_levels"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>complex_orchestration</common_workflow>
    <typical_position>processing</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_workflow_control</primary_discovery_path>
    <alternative_paths>
      <path>orchestration_patterns</path>
      <path>workflow_management</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="state-manager" relation="state_coordination"/>
      <file type="component" ref="dependency-resolver" relation="workflow_dependencies"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="progress-indicator" relation="status_reporting"/>
      <file type="component" ref="task-summary" relation="completion_reporting"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="orchestration" ref="agent-orchestration" similarity="0.40"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Complex multi-step workflows with dependencies</scenario>
      <scenario>Coordinating execution of multiple components</scenario>
      <scenario>Workflows requiring error recovery and state management</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple, single-step operations</scenario>
      <scenario>Independent component execution without coordination</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>workflow coordination orchestration multi-step workflow dependency management execution control</keywords>
    <semantic_tags>workflow_orchestration execution_control dependency_management</semantic_tags>
    <functionality_vectors>workflow_coordination orchestration dependency_management</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>10</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../orchestration/workflow-patterns.md" importance="critical"/>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="critical"/>
    </required_context>
    <helpful_context>
      <context_file ref="../orchestration/dag-orchestrator.md" importance="high"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>orchestration</workflow_stage>
    <integration_patterns>
      <pattern>workflow_execution</pattern>
      <pattern>dependency_coordination</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>workflow_orchestration</concept_introduction>
    <skill_progression>advanced</skill_progression>
    <mastery_indicators>
      <indicator>Can coordinate complex multi-step workflows with dependencies</indicator>
      <indicator>Handles workflow failures with appropriate recovery strategies</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Coordinate multi-step workflow execution:
- Accept and parse input data or parameters
- Define workflow step sequence and dependencies
- Execute steps in proper order
- process step failures and recovery
- coordinate parallel step execution when possible
- Ensure workflow completion criteria are met
```