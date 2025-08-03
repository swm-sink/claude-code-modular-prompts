---
name: /find-commands
description: Smart command discovery tool with filtering and search capabilities (v1.0)
version: "1.0"
usage: '/find-commands [category] [keyword] [--list-categories]'
category: meta
allowed-tools:  
- Read
- LS
- Grep
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate search parameters and category filters
  during-execution: Search through command library efficiently
  post-execution: Present results in organized format
progressive-disclosure:
  layer-integration: Command discovery for all system layers
  escalation-path: Browse categories → keyword search → advanced filtering
  de-escalation: Simple category listing
safety-measures:
  - Validate search patterns
  - Limit result sets for performance
  - Handle missing commands gracefully
  - Cache search results
error-recovery:
  no-results: Suggest alternative search terms
  invalid-category: Show available categories
  search-error: Fallback to basic listing
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/path/to/your/project/.claude/commands/meta/find-commands.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>find-commands</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="file-reader" role="command_library_scanning"/>
      <component ref="search-files" role="pattern_based_searching"/>
      <component ref="parameter-parser" role="search_criteria_processing"/>
      <component ref="output-formatter" role="organized_result_presentation"/>
    </required_components>
    <optional_components>
      <component ref="context-optimization" benefit="intelligent_search_suggestions"/>
      <component ref="component-cache" benefit="performance_optimization"/>
      <component ref="examples-library" benefit="contextual_usage_examples"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="help" context="detailed_command_information"/>
      <command ref="welcome" context="onboarding_integration"/>
    </invokable_commands>
    <orchestration_patterns>discovery|filtering|categorization|suggestion</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Smart command discovery tool with filtering, search capabilities, and intelligent suggestion system</task_description>
    <implementation_strategy>parameter_analysis|library_scanning|pattern_matching|organized_presentation|intelligent_suggestions</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>command_discovery_and_search</primary_discovery_path>
    <alternative_paths>
      <path>template_library_exploration</path>
      <path>command_categorization</path>
      <path>intelligent_command_suggestions</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="command" ref="help" relation="basic_help_foundation"/>
      <file type="command" ref="welcome" relation="discovery_integration"/>
      <file type="context" ref=".claude/context/command-categorization.md" relation="categorization_framework"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="help" relation="detailed_command_help"/>
      <file type="context" ref=".claude/context/command-usage-patterns.md" relation="usage_analytics"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="help" similarity="0.70"/>
      <file type="command" ref="help-plus" similarity="0.65"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>exploring_available_commands</scenario>
      <scenario>searching_for_specific_functionality</scenario>
      <scenario>discovering_commands_by_category</scenario>
      <scenario>finding_related_commands</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>detailed_command_help_needed</scenario>
      <scenario>specific_command_execution</scenario>
      <scenario>troubleshooting_specific_issues</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>find commands discovery search categories filtering exploration</keywords>
    <semantic_tags>command_discovery intelligent_search categorization filtering</semantic_tags>
    <functionality_vectors>[0.9, 0.8, 1.0, 0.7, 0.6]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>global</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>6</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <critical_context>
      <context_file ref=".claude/context/command-categorization.md" importance="critical"/>
      <context_file ref=".claude/context/command-library-index.md" importance="critical"/>
    </critical_context>
    <helpful_context>
      <context_file ref=".claude/context/command-usage-patterns.md" importance="high"/>
      <context_file ref=".claude/context/search-optimization-patterns.md" importance="medium"/>
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="low"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>discovery_and_exploration</workflow_stage>
    <integration_patterns>
      <pattern>intelligent_command_discovery</pattern>
      <pattern>category_based_exploration</pattern>
      <pattern>keyword_search_functionality</pattern>
      <pattern>suggestion_based_navigation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>command_discovery_system</concept_introduction>
    <skill_progression>beginner_to_intermediate</skill_progression>
    <mastery_indicators>
      <indicator>effective_command_search</indicator>
      <indicator>successful_category_exploration</indicator>
      <indicator>intelligent_suggestion_utilization</indicator>
      <indicator>efficient_command_library_navigation</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /find-commands - Smart Command Discovery

I'll help you discover available commands with category [CATEGORY], keyword [KEYWORD], or list all categories with --list-categories.

## Implementation

I'll search through the available commands and provide:
- Commands matching your criteria
- Brief descriptions of each command
- Usage examples and categories
- Suggestions for related commands
