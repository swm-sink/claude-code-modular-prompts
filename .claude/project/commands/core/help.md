---
name: help
description: Comprehensive guide to available commands for the context engineering system
category: core
parameters: 
  - name: COMMAND_NAME
    type: string
    required: false
    description: Specific command name to get detailed help for (optional)
  - name: HELP_TYPE
    type: string
    required: false
    description: Type of help requested (--all, --best-practices, --v2-features)
usage_examples:
  - "/help - Get general help and command overview"
  - "/help task - Get detailed help for the task command"
  - "/help --all - Comprehensive list of all commands"
  - "/help --features - Learn about context engineering system features"
prerequisites: 
  - "Claude Code environment configured"
  - "Template library installed"
output_format: structured
tags: [help, documentation, guidance, commands]
version: "1.0"
author: "template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Grep
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/path/to/your/project/.claude/commands/core/help.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>help</command_id>
  <command_count>comprehensive</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="help_request_processing"/>
      <component ref="output-formatter" role="help_display"/>
      <component ref="search-files" role="command_discovery"/>
    </required_components>
    <optional_components>
      <component ref="examples-library" benefit="usage_examples"/>
      <component ref="context-optimization" benefit="relevant_help"/>
      <component ref="progress-tracking" benefit="learning_progress"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="quick-command" context="beginner_guidance"/>
      <command ref="build-command" context="intermediate_guidance"/>
      <command ref="assemble-command" context="advanced_guidance"/>
      <command ref="find-commands" context="command_discovery"/>
    </invokable_commands>
    <orchestration_patterns>conditional|interactive|progressive</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Provide comprehensive, context-aware help for all 88 commands with Interactive Consultation System guidance</task_description>
    <implementation_strategy>parse_help_request|analyze_user_level|provide_contextual_help|suggest_next_steps|enable_progressive_learning</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>help_and_guidance_system</primary_discovery_path>
    <alternative_paths>
      <path>user_support_entry_point</path>
      <path>command_reference_system</path>
      <path>learning_and_onboarding</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/comprehensive-project-learnings.md" relation="user_guidance"/>
      <file type="component" ref=".claude/components/context/hierarchical-loading.md" relation="help_organization"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="welcome" relation="onboarding_flow"/>
      <file type="command" ref="quick-command" relation="beginner_escalation"/>
      <file type="command" ref="build-command" relation="intermediate_escalation"/>
      <file type="command" ref="assemble-command" relation="advanced_escalation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="help-plus" similarity="0.90"/>
      <file type="command" ref="quick-help" similarity="0.75"/>
      <file type="command" ref="find-commands" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>new_user_getting_started</scenario>
      <scenario>exploring_available_commands</scenario>
      <scenario>learning_specific_command_usage</scenario>
      <scenario>understanding_v2_enhancements</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>during_focused_development_work</scenario>
      <scenario>when_specific_command_already_known</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>help guide commands documentation assistance progressive disclosure v2 features</keywords>
    <semantic_tags>user_guidance command_reference learning_system comprehensive_help</semantic_tags>
    <functionality_vectors>[1.0, 0.9, 0.3, 0.8, 0.9]</functionality_vectors>
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
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="critical"/>
      <context_file ref=".claude/context/prompt-engineering-best-practices.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref=".claude/context/user-experience-patterns.md" importance="medium"/>
      <context_file ref=".claude/context/interactive-consultation-guide.md" importance="high"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>entry_point</workflow_stage>
    <integration_patterns>
      <pattern>user_assessment</pattern>
      <pattern>contextual_help_delivery</pattern>
      <pattern>progressive_disclosure_navigation</pattern>
      <pattern>learning_path_guidance</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>template_library_navigation</concept_introduction>
    <skill_progression>all_levels</skill_progression>
    <mastery_indicators>
      <indicator>successful_help_request_resolution</indicator>
      <indicator>appropriate_progressive_disclosure_navigation</indicator>
      <indicator>reduced_need_for_repeated_help</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /help - Comprehensive Command Guide v1.0

<context type="project">
Lusaka context engineering system with 88 Claude Code commands featuring v1.0 enhancements: enhanced metadata, XML semantic structure, parameter validation, Interactive Consultation System, and team collaboration features.
</context>

<instructions>
Provide comprehensive help and guidance for the context engineering system. Process $COMMAND_NAME for specific command help, or use $HELP_TYPE for specialized help categories. Default to general overview with quick start guidance.
</instructions>

## Usage Examples

<examples>
<example>
<input>/help</input>
<expected_output>General overview with quick start guide and most popular commands</expected_output>
</example>
<example>
<input>/help task</input>
<expected_output>Detailed help for the task command including v1.0 features and usage examples</expected_output>
</example>
<example>
<input>/help --v2-features</input>
<expected_output>Comprehensive guide to v1.0 enhancements: metadata, XML structure, team features</expected_output>
</example>
</examples>

## Help System Workflow

<workflow type="sequential">
<task priority="high">
**Request Analysis**: Determine help type and scope
- Parse $COMMAND_NAME for specific command help
- Process $HELP_TYPE for specialized categories
- Default to general overview if no parameters provided
</task>

<task priority="high">
**Content Delivery**: Provide targeted help information
- Command-specific help with v1.0 features explanation
- Category overviews with command listings
- Best practices and usage patterns
</task>

<task priority="medium">
**Guidance Enhancement**: Offer next steps and learning paths
- Suggest related commands and workflows
- Provide Interactive Consultation System navigation
- Link to advanced features and team collaboration
</task>
</workflow>

## 🚀 Quick Start Guide

### **Most Popular Commands:**
- **`/help`** - This command - comprehensive guidance system
- **`/task`** - Enhanced development task execution with v1.0 features
- **`/quick-command`** - 30-second auto-generation (Layer 1 Interactive Consultation)
- **`/welcome`** - Interactive onboarding and project setup

### **Interactive Consultation System (v1.0):**
1. **Layer 1**: `/quick-command` - Instant generation, zero learning curve
2. **Layer 2**: `/build-command` - Guided customization with smart options  
3. **Layer 3**: `/assemble-command` - Professional assembly with 96 components

### **Command Categories (88 Total):**
- **Core (15)**: Essential commands for daily development
- **Quality (12)**: Testing, validation, and analysis tools
- **Meta (17)**: Adaptation, memory management, and system commands
- **Specialized (11)**: Advanced orchestration and complex workflows
- **DevOps (5)**: Deployment, CI/CD, and infrastructure
- **Testing (5)**: Unit, integration, e2e testing frameworks
- **Database (4)**: Migration, backup, and data management
- **Development (6)**: Environment setup and API design
- **Others (13)**: Security, monitoring, examples, and utilities

## 🆕 v1.0 Enhanced Features

### **Enhanced Metadata System:**
- Parameter validation with type checking
- Usage examples with expected outputs
- Prerequisites and dependency tracking
- Version control and team attribution

### **XML Semantic Structure:**
- `<context>` - Project-specific information
- `<instructions>` - Procedural guidance with parameters
- `<examples>` - Structured input/output demonstrations
- `<workflow>` - Implementation phases and task organization

### **Team Collaboration:**
- Hierarchical memory management (Project/Personal/Global)
- MCP integration for external tools
- Advanced command discovery and knowledge sharing

<automation trigger="completion">
- Log help request for usage analytics
- Suggest related commands based on request pattern
- Update user journey tracking for Interactive Consultation navigation
</automation>
