# Task Summary Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/task-summary.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>task-summary</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>user_interface</subcategory>
  
  <complexity_metrics>
    <usage_complexity>moderate</usage_complexity>
    <implementation_effort>minutes_15</implementation_effort>
    <prerequisite_knowledge>intermediate</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="workflow-coordinator" strength="strong"/>
      <component ref="progress-indicator" strength="strong"/>
      <component ref="completion-tracker" strength="strong"/>
      <component ref="output-formatter" strength="medium"/>
      <component ref="error-handler" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="parameter-parser" reason="different_workflow_stages"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>task_completion</common_workflow>
    <typical_position>output</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_user_interface</primary_discovery_path>
    <alternative_paths>
      <path>reporting</path>
      <path>task_completion</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="completion-tracker" relation="completion_data"/>
      <file type="component" ref="workflow-coordinator" relation="workflow_results"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="component" ref="output-formatter" relation="summary_formatting"/>
      <file type="user_interface" ref="display" relation="summary_presentation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="progress-indicator" similarity="0.45"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Generating completion reports for complex workflows</scenario>
      <scenario>Summarizing task results and outcomes</scenario>
      <scenario>Providing users with comprehensive task completion status</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Real-time progress updates (use progress-indicator instead)</scenario>
      <scenario>Simple success/failure notifications</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>task summary completion report workflow results task outcomes status reporting</keywords>
    <semantic_tags>task_reporting completion_summary outcome_documentation</semantic_tags>
    <functionality_vectors>summary_generation task_reporting completion_documentation</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>6</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="medium"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/llm-antipatterns.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>completion_reporting</workflow_stage>
    <integration_patterns>
      <pattern>task_completion_summary</pattern>
      <pattern>outcome_documentation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>task_reporting</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>Can generate comprehensive task completion summaries</indicator>
      <indicator>Handles missing or incomplete task information gracefully</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Generate comprehensive task completion summary:
- Review input task list and completion status data
- Document specific tasks completed with measurable results
- Identify and categorize any issues or blockers encountered
- process missing or incomplete task information gracefully
- Provide clear, actionable next steps with priorities
- Validate summary completeness against original objectives
- Format output as structured report with clear sections
```