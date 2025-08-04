<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/orchestration/task-execution.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>task-execution</component_id>
  <component_count>91</component_count>
  <category>orchestration</category>
  <subcategory>execution</subcategory>
  
  <complexity_metrics>
    <usage_complexity>high</usage_complexity>
    <implementation_effort>hours_3</implementation_effort>
    <prerequisite_knowledge>advanced</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="dag-orchestrator" strength="strong"/>
      <component ref="agent-orchestration" strength="strong"/>
      <component ref="task-planning" strength="strong"/>
      <component ref="progress-tracking" strength="medium"/>
      <component ref="error-handler" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="quick-command" reason="complexity_mismatch"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>orchestrated_task_execution</common_workflow>
    <typical_position>execution_layer</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>task_execution</primary_discovery_path>
    <alternative_paths>
      <path>orchestrated_execution</path>
      <path>isolated_execution</path>
      <path>distributed_processing</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="task-planning" relation="execution_planning"/>
      <file type="component" ref="dag-orchestrator" relation="workflow_execution"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="progress-tracking" relation="execution_monitoring"/>
      <file type="component" ref="error-handler" relation="failure_handling"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="workflow-coordinator" similarity="0.70"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Orchestrated workflows requiring isolated task execution</scenario>
      <scenario>Distributed processing with resource management</scenario>
      <scenario>Complex workflows needing execution monitoring</scenario>
      <scenario>Tasks requiring timeout and retry management</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple single-command operations</scenario>
      <scenario>Interactive workflows requiring user input</scenario>
      <scenario>Synchronous operations without orchestration needs</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>task execution orchestration execution isolation resource management timeout retry distributed processing</keywords>
    <semantic_tags>task_execution orchestrated_processing execution_management</semantic_tags>
    <functionality_vectors>task_execution resource_management execution_monitoring</functionality_vectors>
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
      <context_file ref="../orchestration/task-planning.md" importance="critical"/>
      <context_file ref="../orchestration/dag-orchestrator.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="../orchestration/progress-tracking.md" importance="medium"/>
      <context_file ref="../atomic/error-handler.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>execution_layer</workflow_stage>
    <integration_patterns>
      <pattern>orchestrated_execution</pattern>
      <pattern>isolated_processing</pattern>
      <pattern>monitored_execution</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>orchestrated_task_execution</concept_introduction>
    <skill_progression>advanced</skill_progression>
    <mastery_indicators>
      <indicator>Isolated task execution with proper resource management</indicator>
      <indicator>Distributed processing with monitoring and error handling</indicator>
      <indicator>Quality assurance with validation and verification</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# Task Execution Component

## Purpose
Execute individual tasks within orchestration patterns with proper isolation and monitoring.

## Execution Framework
1. **Task Isolation**: Each task runs in its own context
2. **Resource Allocation**: Assign appropriate resources
3. **Timeout Management**: Enforce execution time limits
4. **Error Boundaries**: Contain failures within tasks
5. **Result Collection**: Gather and validate outputs

## Task Execution Protocol
```json
{
  "execution": {
    "task_id": "unique_id",
    "agent_type": "specialized_agent",
    "context": {},
    "resources": {
      "timeout": 300,
      "memory_limit": "1GB",
      "retry_policy": {
        "max_attempts": 3,
        "backoff": "exponential"
      }
    },
    "monitoring": {
      "start_time": null,
      "checkpoints": [],
      "metrics": {}
    }
  }
}
```

## Execution Strategies
- **Synchronous**: Wait for task completion
- **Asynchronous**: Fire-and-forget with callbacks
- **Batch**: Group similar tasks for efficiency
- **Streaming**: Process results as they arrive

## Quality Assurance
- Pre-execution validation
- Runtime monitoring
- Post-execution verification
- Result integrity checks