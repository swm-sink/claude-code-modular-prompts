<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/orchestration/dependency-analysis.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>dependency-analysis</component_id>
  <component_count>91</component_count>
  <category>orchestration</category>
  <subcategory>analysis</subcategory>
  
  <complexity_metrics>
    <usage_complexity>high</usage_complexity>
    <implementation_effort>hours_3</implementation_effort>
    <prerequisite_knowledge>advanced</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="dag-orchestrator" strength="strong"/>
      <component ref="task-planning" strength="strong"/>
      <component ref="task-execution" strength="medium"/>
      <component ref="agent-orchestration" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="quick-command" reason="complexity_mismatch"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>dependency_management</common_workflow>
    <typical_position>analysis_foundation</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>dependency_analysis</primary_discovery_path>
    <alternative_paths>
      <path>graph_analysis</path>
      <path>critical_path_analysis</path>
      <path>resource_dependency</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="algorithm" ref="graph_algorithms" relation="dependency_resolution"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="dag-orchestrator" relation="dependency_modeling"/>
      <file type="component" ref="task-planning" relation="planning_optimization"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="progress-tracking" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Complex workflows with intricate task dependencies</scenario>
      <scenario>DAG orchestration requiring dependency validation</scenario>
      <scenario>Parallel execution optimization planning</scenario>
      <scenario>Critical path analysis for workflow optimization</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple sequential workflows</scenario>
      <scenario>Independent parallel tasks</scenario>
      <scenario>Single-task operations</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>dependency analysis graph analysis critical path task sequencing resource conflicts topological sorting</keywords>
    <semantic_tags>dependency_analysis graph_analysis critical_path</semantic_tags>
    <functionality_vectors>dependency_detection graph_validation resource_analysis</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>8</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../orchestration/dag-orchestrator.md" importance="critical"/>
    </required_context>
    <helpful_context>
      <context_file ref="../orchestration/task-planning.md" importance="high"/>
      <context_file ref="../orchestration/task-execution.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>analysis_foundation</workflow_stage>
    <integration_patterns>
      <pattern>dependency_detection</pattern>
      <pattern>graph_analysis</pattern>
      <pattern>critical_path_optimization</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>dependency_analysis</concept_introduction>
    <skill_progression>advanced</skill_progression>
    <mastery_indicators>
      <indicator>Complex dependency graph analysis and resolution</indicator>
      <indicator>Critical path identification and optimization</indicator>
      <indicator>Resource conflict detection and prevention</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# Dependency Analysis Component

## Purpose
Analyze task dependencies to enable proper sequencing and parallelization in DAG orchestration.

## Dependency Detection
1. **Explicit Dependencies**: Direct prerequisite relationships
2. **Implicit Dependencies**: Resource conflicts, shared state
3. **Circular Detection**: Prevent dependency loops
4. **Transitive Analysis**: Full dependency chains
5. **Critical Path**: Longest dependency sequence

## Dependency Graph Structure
```json
{
  "nodes": {
    "task_id": {
      "depends_on": ["task_ids"],
      "blocks": ["task_ids"],
      "resources": ["shared_resources"],
      "priority": 1
    }
  },
  "edges": [
    {"from": "task_a", "to": "task_b", "type": "hard|soft"}
  ],
  "analysis": {
    "has_cycles": false,
    "critical_path": ["task_sequence"],
    "parallelization_factor": 0.0
  }
}
```

## Resolution Strategies
- Topological sorting for execution order
- Deadlock prevention algorithms
- Resource conflict resolution
- Dynamic dependency updates