<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/orchestration/progress-tracking.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>progress-tracking</component_id>
  <component_count>91</component_count>
  <category>orchestration</category>
  <subcategory>monitoring</subcategory>
  
  <complexity_metrics>
    <usage_complexity>moderate</usage_complexity>
    <implementation_effort>hours_2</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="dag-orchestrator" strength="strong"/>
      <component ref="agent-orchestration" strength="strong"/>
      <component ref="task-execution" strength="strong"/>
      <component ref="progress-indicator" strength="medium"/>
      <component ref="task-summary" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="quick-command" reason="overhead_mismatch"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>orchestration_monitoring</common_workflow>
    <typical_position>monitoring_layer</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>orchestration_monitoring</primary_discovery_path>
    <alternative_paths>
      <path>progress_monitoring</path>
      <path>performance_tracking</path>
      <path>workflow_analytics</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="dag-orchestrator" relation="workflow_monitoring"/>
      <file type="component" ref="agent-orchestration" relation="agent_monitoring"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="task-summary" relation="progress_reporting"/>
      <file type="component" ref="progress-indicator" relation="user_feedback"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="dependency-analysis" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Long-running orchestrated workflows</scenario>
      <scenario>Distributed agent coordination requiring monitoring</scenario>
      <scenario>Performance-sensitive operations needing tracking</scenario>
      <scenario>Complex workflows requiring progress visibility</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple single-task operations</scenario>
      <scenario>Fast-executing workflows</scenario>
      <scenario>Internal operations without user visibility needs</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>progress tracking workflow monitoring performance metrics orchestration analytics real time monitoring</keywords>
    <semantic_tags>progress_monitoring workflow_analytics performance_tracking</semantic_tags>
    <functionality_vectors>progress_monitoring performance_analytics workflow_tracking</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>7</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../orchestration/dag-orchestrator.md" importance="high"/>
      <context_file ref="../orchestration/agent-orchestration.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../atomic/progress-indicator.md" importance="medium"/>
      <context_file ref="../atomic/task-summary.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>monitoring_layer</workflow_stage>
    <integration_patterns>
      <pattern>progress_monitoring</pattern>
      <pattern>performance_analytics</pattern>
      <pattern>real_time_tracking</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>orchestration_monitoring</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>Distributed progress tracking across multiple agents</indicator>
      <indicator>Real-time performance monitoring and analytics</indicator>
      <indicator>Comprehensive workflow visualization and reporting</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# Progress Tracking Component

## Purpose
Monitor and report progress across distributed agent tasks in orchestration patterns.

## Progress Tracking Protocol
1. **Status Updates**: Regular heartbeat from active agents
2. **Milestone Tracking**: Key checkpoints and deliverables
3. **Performance Metrics**: Execution time, resource usage
4. **Completion Percentage**: Overall and per-task progress
5. **Blocker Detection**: Identify stalled or failing tasks

## Progress Report Format
```json
{
  "overall_progress": 0.0,
  "active_tasks": 0,
  "completed_tasks": 0,
  "failed_tasks": 0,
  "performance": {
    "avg_task_time": 0,
    "throughput": 0,
    "efficiency": 0.0
  }
}
```

## Real-time Monitoring
- Live progress visualization
- Automated alerts on delays
- Performance trend analysis
- Resource utilization tracking