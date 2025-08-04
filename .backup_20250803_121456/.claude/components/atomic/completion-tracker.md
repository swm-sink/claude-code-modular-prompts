# Completion Tracker Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/completion-tracker.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>completion-tracker</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>workflow_control</subcategory>
  
  <complexity_metrics>
    <usage_complexity>moderate</usage_complexity>
    <implementation_effort>minutes_15</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="progress-indicator" strength="strong"/>
      <component ref="state-manager" strength="strong"/>
      <component ref="task-summary" strength="strong"/>
      <component ref="workflow-coordinator" strength="medium"/>
      <component ref="error-handler" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="user-confirmation" reason="different_tracking_paradigms"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>progress_monitoring</common_workflow>
    <typical_position>utility</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_workflow_control</primary_discovery_path>
    <alternative_paths>
      <path>progress_tracking</path>
      <path>task_monitoring</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="workflow-coordinator" relation="task_definitions"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="progress-indicator" relation="progress_updates"/>
      <file type="component" ref="task-summary" relation="completion_data"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="state-manager" similarity="0.50"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Tracking completion status of multiple tasks</scenario>
      <scenario>Calculating overall progress percentages</scenario>
      <scenario>Identifying remaining tasks and blockers</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple binary completion states</scenario>
      <scenario>Single-task operations without progress tracking</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>completion tracking task monitoring progress calculation status tracking workflow progress</keywords>
    <semantic_tags>completion_tracking progress_monitoring task_status</semantic_tags>
    <functionality_vectors>progress_calculation completion_monitoring task_tracking</functionality_vectors>
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
      <context_file ref="../context/comprehensive-project-learnings.md" importance="medium"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/llm-antipatterns.md" importance="low"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>progress_monitoring</workflow_stage>
    <integration_patterns>
      <pattern>completion_tracking</pattern>
      <pattern>progress_calculation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>completion_tracking</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>Can accurately track completion status across multiple tasks</indicator>
      <indicator>Provides meaningful progress percentages and remaining task estimates</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Track task completion and progress:
- Accept and parse input data or parameters
- Monitor individual task completion status
- Calculate overall progress percentage
- Identify remaining tasks and blockers
- Generate progress reports and summaries
- Handle errors and edge cases according to defined criteria
- Trigger completion notifications and actions
```