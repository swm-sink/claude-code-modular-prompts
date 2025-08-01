# Progress Indicator Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/components/atomic/progress-indicator.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>progress-indicator</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>user_interface</subcategory>
  
  <complexity_metrics>
    <usage_complexity>simple</usage_complexity>
    <implementation_effort>minutes_5</implementation_effort>
    <prerequisite_knowledge>basic</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="workflow-coordinator" strength="strong"/>
      <component ref="task-summary" strength="strong"/>
      <component ref="error-handler" strength="strong"/>
      <component ref="state-manager" strength="medium"/>
      <component ref="completion-tracker" strength="medium"/>
    </compatible_components>
    <incompatible_components>
      <component ref="user-confirmation" reason="conflicting_user_interface_patterns"/>
    </compatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>task_execution</common_workflow>
    <typical_position>utility</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_user_interface</primary_discovery_path>
    <alternative_paths>
      <path>progress_tracking</path>
      <path>user_feedback</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="workflow-coordinator" relation="progress_source"/>
      <file type="component" ref="state-manager" relation="state_monitoring"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="user_interface" ref="display" relation="progress_display"/>
      <file type="component" ref="task-summary" relation="completion_reporting"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="component" ref="completion-tracker" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>Long-running tasks requiring user feedback</scenario>
      <scenario>Multi-step workflows with clear milestones</scenario>
      <scenario>Operations where users need status updates</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>Simple, instant operations</scenario>
      <scenario>Background processes without user interaction</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>progress indicator status updates user feedback task tracking workflow progress</keywords>
    <semantic_tags>progress_tracking user_interface status_reporting</semantic_tags>
    <functionality_vectors>progress_display user_feedback status_tracking</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>5</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="../context/comprehensive-project-learnings.md" importance="low"/>
    </required_context>
    <helpful_context>
      <context_file ref="../context/llm-antipatterns.md" importance="low"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>progress_tracking</workflow_stage>
    <integration_patterns>
      <pattern>status_reporting</pattern>
      <pattern>user_feedback_loop</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>progress_tracking</concept_introduction>
    <skill_progression>beginner</skill_progression>
    <mastery_indicators>
      <indicator>Can provide meaningful progress updates at appropriate intervals</indicator>
      <indicator>Calculates accurate progress percentages for quantifiable tasks</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

```
Display task progress with structured indicators:
- Initialize progress tracking with total step count and task name
- Generate timestamped progress messages at key milestones
- Calculate and display percentage completion for quantifiable tasks
- Provide specific status updates for current operation context
- Handle progress tracking errors with fallback messaging
- Generate completion summary with elapsed time and results
```