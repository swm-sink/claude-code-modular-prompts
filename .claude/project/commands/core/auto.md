---
name: /auto
description: Intelligent command router with context-aware selection and automatic parameter detection (v1.0)
version: "1.0"
usage: '/auto "[your request in natural language]"'
allowed-tools:
- Read
- Write
- Edit
- Grep
- Glob
- Bash
dependencies:
- /help
- /quick-command
- /task
validation:
  pre-execution: Parse request and identify intent with confidence scoring
  during-execution: Monitor command execution and provide fallback options
  post-execution: Verify request was fulfilled and suggest follow-up commands
progressive-disclosure:
  layer-integration: Automatically routes to appropriate layer based on request complexity
  escalation-path: Simple routing → parameter inference → multi-command orchestration
  de-escalation: Suggests simpler alternatives when appropriate
safety-measures:
  - Confirm destructive operations
  - Validate command parameters
  - Prevent infinite routing loops
  - Show routing decisions transparently
error-recovery:
  ambiguous-request: Provide clarification options with examples
  no-match: Suggest closest commands and ask for refinement
  execution-failure: Offer alternative approaches
category: core
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/path/to/your/project/.claude/commands/core/auto.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>auto</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="natural_language_processing"/>
      <component ref="intelligent-summarization" role="intent_analysis"/>
      <component ref="workflow-coordinator" role="command_routing"/>
      <component ref="validation-framework" role="execution_safety"/>
    </required_components>
    <optional_components>
      <component ref="context-optimization" benefit="request_understanding"/>
      <component ref="user-confirmation" benefit="safety_validation"/>
      <component ref="progress-tracking" benefit="execution_monitoring"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="help" context="command_discovery"/>
      <command ref="quick-command" context="simple_requests"/>
      <command ref="task" context="development_requests"/>
      <command ref="research" context="information_requests"/>
      <command ref="project" context="project_management_requests"/>
    </invokable_commands>
    <orchestration_patterns>intelligent_routing|context_aware|fallback_mechanisms</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Intelligent command routing with natural language processing, context-aware selection, and automatic parameter detection</task_description>
    <implementation_strategy>parse_natural_language|analyze_intent|route_to_appropriate_command|monitor_execution|provide_feedback</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>intelligent_command_routing</primary_discovery_path>
    <alternative_paths>
      <path>natural_language_interface</path>
      <path>command_automation_system</path>
      <path>smart_workflow_router</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/natural-language-processing.md" relation="nlp_guidance"/>
      <file type="component" ref=".claude/components/intelligence/intelligent-summarization.md" relation="intent_analysis"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="help" relation="discovery_routing"/>
      <file type="command" ref="quick-command" relation="simple_task_routing"/>
      <file type="command" ref="task" relation="development_routing"/>
      <file type="command" ref="research" relation="information_routing"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="help" similarity="0.60"/>
      <file type="command" ref="quick-command" similarity="0.50"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>natural_language_command_requests</scenario>
      <scenario>uncertain_about_which_command_to_use</scenario>
      <scenario>complex_multi_step_workflows</scenario>
      <scenario>beginner_users_learning_the_system</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>direct_command_usage_preferred</scenario>
      <scenario>expert_users_with_specific_needs</scenario>
      <scenario>performance_critical_operations</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>auto intelligent routing natural language command automation smart workflow</keywords>
    <semantic_tags>intelligent_routing natural_language_processing command_automation workflow_optimization</semantic_tags>
    <functionality_vectors>[0.9, 0.6, 0.8, 0.9, 0.8]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>global</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>10</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref=".claude/context/natural-language-processing.md" importance="critical"/>
      <context_file ref=".claude/context/command-routing-patterns.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref=".claude/context/user-intent-analysis.md" importance="medium"/>
      <context_file ref=".claude/context/progressive-disclosure-guide.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>entry_point</workflow_stage>
    <integration_patterns>
      <pattern>natural_language_parsing</pattern>
      <pattern>intelligent_command_selection</pattern>
      <pattern>automatic_parameter_detection</pattern>
      <pattern>execution_monitoring</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>intelligent_command_routing</concept_introduction>
    <skill_progression>all_levels</skill_progression>
    <mastery_indicators>
      <indicator>successful_intent_recognition</indicator>
      <indicator>appropriate_command_routing</indicator>
      <indicator>effective_parameter_inference</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /auto - Intelligent Command Router for your project

I'll analyze your request and automatically route it to the most appropriate command for your software-development project using Python.

## How It Works

This command analyzes your natural language request and routes it to the best available command in your prompt library.
## Usage
```bash
/auto "fix the authentication bug in the login system"
/auto "add user profile editing functionality"  
/auto "analyze the performance bottleneck in our API"
/auto "refactor the database connection logic safely"
```

## Examples

**Development Tasks:**
- `/auto "implement user authentication"`
- `/auto "fix the database connection issue"`

**Analysis & Research:**
- `/auto "analyze performance bottlenecks"`
- `/auto "research best practices for Python"`

I'll route your request to the most appropriate command and provide you with the best implementation approach for your project.
