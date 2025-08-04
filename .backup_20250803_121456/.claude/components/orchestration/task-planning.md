<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/orchestration/task-planning.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>task-planning</component_id>
  <component_count>91</component_count>
  <category>orchestration</category>
  <subcategory>planning</subcategory>
  
  <complexity_metrics>
    <usage_complexity>high</usage_complexity>
    <implementation_effort>hours_2</implementation_effort>
    <prerequisite_knowledge>advanced</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="agent-orchestration" strength="strong"/>
      <component ref="dependency-analysis" strength="strong"/>
      <component ref="task-execution" strength="strong"/>
      <component ref="agent-swarm" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="quick-command" reason="planning_overhead_mismatch"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>complex_task_planning</common_workflow>
    <typical_position>planning_foundation</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>task_planning</primary_discovery_path>
    <alternative_paths>
      <path>orchestration_planning</path>
      <path>task_decomposition</path>
      <path>workflow_planning</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="algorithm" ref="task_decomposition_algorithms" relation="planning_methodology"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="task-execution" relation="execution_planning"/>
      <file type="component" ref="agent-orchestration" relation="coordination_planning"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="dependency-analysis" similarity="0.80"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Complex multi-step tasks requiring decomposition</scenario>
      <scenario>Agent orchestration needing structured planning</scenario>
      <scenario>Workflows requiring dependency analysis and parallelization</scenario>
      <scenario>Resource estimation and risk assessment requirements</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple single-step operations</scenario>
      <scenario>Well-defined workflows with fixed sequences</scenario>
      <scenario>Ad-hoc tasks without optimization needs</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>task planning orchestration planning task decomposition workflow planning dependency analysis parallelization risk assessment</keywords>
    <semantic_tags>task_planning orchestration_planning workflow_decomposition</semantic_tags>
    <functionality_vectors>task_decomposition dependency_planning resource_estimation</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../orchestration/dependency-analysis.md" importance="critical"/>
    </required_context>
    <helpful_context>
      <context_file ref="../orchestration/agent-orchestration.md" importance="high"/>
      <context_file ref="../orchestration/task-execution.md" importance="high"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>planning_foundation</workflow_stage>
    <integration_patterns>
      <pattern>task_decomposition</pattern>
      <pattern>dependency_planning</pattern>
      <pattern>resource_planning</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>orchestration_task_planning</concept_introduction>
    <skill_progression>advanced</skill_progression>
    <mastery_indicators>
      <indicator>Complex task decomposition into atomic units</indicator>
      <indicator>Dependency identification and parallelization planning</indicator>
      <indicator>Resource estimation and risk assessment for orchestration</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# Task Planning Component

## Purpose
Analyze complex tasks and create structured execution plans for agent orchestration.

## Task Analysis Framework
1. **Decomposition**: Break complex tasks into atomic units
2. **Dependencies**: Identify task relationships and prerequisites  
3. **Parallelization**: Determine which tasks can run concurrently
4. **Resource Estimation**: Estimate time and complexity per task
5. **Risk Assessment**: Identify potential failure points

## Planning Output Structure
```json
{
  "task_breakdown": {
    "atomic_tasks": [],
    "dependencies": {},
    "parallel_groups": [],
    "critical_path": [],
    "estimated_duration": 0
  }
}
```

## Usage
Include this component when agents need to analyze and plan complex multi-step tasks.