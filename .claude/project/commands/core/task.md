---
name: task
description: Execute a focused development task with best practices and quality standards
category: workflow
parameters: 
  - name: TASK_DESCRIPTION
    type: string
    required: true
    description: Detailed description of the development task to be implemented
usage_examples:
  - "/task create email validation utility function"
  - "/task implement user authentication middleware"
  - "/task add pagination to the user listing component"
prerequisites: 
  - "Git repository initialized"
  - "Project dependencies installed"
  - "Development environment configured"
output_format: structured
tags: [development, implementation, testing, documentation, quality]
version: "1.0"
author: "template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Write
- Edit
- Grep
- Glob
- Bash
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/path/to/your/project/.claude/commands/core/task.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>task</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="input_processing"/>
      <component ref="workflow-coordinator" role="task_orchestration"/>
      <component ref="error-handler" role="quality_assurance"/>
      <component ref="progress-indicator" role="user_feedback"/>
    </required_components>
    <optional_components>
      <component ref="git-operations" benefit="version_control"/>
      <component ref="test-runner" benefit="quality_validation"/>
      <component ref="task-summary" benefit="completion_tracking"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="test-unit" context="quality_validation"/>
      <command ref="analyze-code" context="quality_check"/>
      <command ref="validate-command" context="output_validation"/>
    </invokable_commands>
    <orchestration_patterns>sequential|conditional|iterative</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Execute focused development tasks with comprehensive quality standards and automated validation</task_description>
    <implementation_strategy>parse_requirements|plan_implementation|execute_development|validate_quality|document_results</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>core_workflow_commands</primary_discovery_path>
    <alternative_paths>
      <path>development_workflow_entry_point</path>
      <path>focused_implementation_command</path>
      <path>quality_driven_development</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/prompt-engineering-best-practices.md" relation="quality_standards"/>
      <file type="component" ref=".claude/components/atomic/workflow-coordinator.md" relation="core_dependency"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="test-unit" relation="quality_validation"/>
      <file type="command" ref="analyze-code" relation="code_review"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="project-task" similarity="0.85"/>
      <file type="command" ref="dev" similarity="0.70"/>
      <file type="command" ref="quick-task" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>focused_development_task_implementation</scenario>
      <scenario>quality_driven_development_workflow</scenario>
      <scenario>structured_implementation_with_validation</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>quick_prototype_development</scenario>
      <scenario>exploratory_research_tasks</scenario>
      <scenario>large_architectural_changes</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>task development workflow implementation quality testing validation</keywords>
    <semantic_tags>focused_development structured_workflow quality_assurance best_practices</semantic_tags>
    <functionality_vectors>[0.9, 0.8, 0.7, 0.9, 0.8]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref=".claude/context/prompt-engineering-best-practices.md" importance="high"/>
      <context_file ref=".claude/context/claude-code-tools.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref=".claude/context/llm-antipatterns.md" importance="medium"/>
      <context_file ref=".claude/context/development-patterns.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>implementation</workflow_stage>
    <integration_patterns>
      <pattern>requirement_analysis</pattern>
      <pattern>structured_development</pattern>
      <pattern>quality_validation</pattern>
      <pattern>documentation_generation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>focused_development_workflow</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>successful_task_completion</indicator>
      <indicator>quality_standards_met</indicator>
      <indicator>comprehensive_documentation</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /task - Focused Development Workflow

<context type="project">
context engineering system specializing in Claude Code command development with Python-focused implementation patterns, automated testing integration, and comprehensive documentation standards.
</context>

<instructions>
Execute a focused development task using industry best practices, quality standards, and systematic approach. Process $TASK_DESCRIPTION with comprehensive analysis, implementation, testing, and documentation.
</instructions>

## Usage Examples

<examples>
<example>
<input>/task "create email validation utility function"</input>
<expected_output>Complete utility function with regex validation, error handling, unit tests, and documentation</expected_output>
</example>
<example>
<input>/task "implement user authentication middleware"</input>
<expected_output>Middleware with JWT handling, error responses, security headers, and integration tests</expected_output>
</example>
<example>
<input>/task "add pagination to user listing component"</input>
<expected_output>Component with page controls, data fetching, loading states, and unit tests</expected_output>
</example>
</examples>

## Implementation Workflow

<workflow type="sequential">
<task priority="high">
**Analysis Phase**: Understand requirements, dependencies, and context
- Parse $TASK_DESCRIPTION for technical requirements
- Identify affected files and components  
- Determine testing strategy and documentation needs
</task>

<task priority="high">
**Design Phase**: Plan implementation approach and architecture
- Design API interfaces and data structures
- Plan error handling and edge cases
- Consider performance and security implications
</task>

<task priority="high">
**Implementation Phase**: Write clean, maintainable code
- Follow established coding standards and patterns
- Implement core functionality with proper error handling
- Add logging and monitoring where appropriate
</task>

<task priority="medium">
**Testing Phase**: Comprehensive test coverage
- Unit tests for individual functions/methods
- Integration tests for component interactions
- End-to-end tests for complete workflows
</task>

<task priority="medium">
**Documentation Phase**: Update relevant documentation
- Code comments and docstrings
- README updates for new features
- API documentation where applicable
</task>
</workflow>

<automation trigger="completion">
- Run test suite to verify functionality
- Check code quality and standards compliance
- Update project documentation and examples
</automation>
