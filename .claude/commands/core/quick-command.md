---
command: quick-command
description: Layer 1 Progressive Disclosure - Auto-generate complete commands from simple descriptions with 30-second success guarantee
category: core
parameters: 
  - name: TYPE
    type: string
    required: true
    description: Command type (search, analyze, transform, validate, report)
  - name: DESCRIPTION
    type: string
    required: true
    description: Clear description of what you want to accomplish
usage_examples:
  - "/quick-command search 'find TODO comments in JavaScript'"
  - "/quick-command analyze 'check Python code quality'"
  - "/quick-command transform 'convert JSON files to YAML'"
  - "/quick-command validate 'check all API responses'"
prerequisites: 
  - "Clear understanding of desired command functionality"
  - "Basic description of target files or operations"
output_format: structured
tags: [auto-generation, progressive-disclosure, layer-1, zero-setup, v2-enhanced]
version: "2.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools:
- Write
- Read
- Grep
- Glob
- Edit
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/commands/core/quick-command.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>quick-command</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>1</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="input_handling"/>
      <component ref="template-selector" role="type_matching"/>
      <component ref="command-generator" role="output_creation"/>
    </required_components>
    <optional_components>
      <component ref="validation-framework" benefit="quality_assurance"/>
      <component ref="usage-example-generator" benefit="user_guidance"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="build-command" context="layer_2_escalation"/>
      <command ref="assemble-command" context="layer_3_escalation"/>
      <command ref="validate-command" context="quality_check"/>
    </invokable_commands>
    <orchestration_patterns>sequential|conditional</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Auto-generate complete working commands from user descriptions</task_description>
    <implementation_strategy>parse_input|select_template|assemble_components|generate_command|validate_output</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>progressive_disclosure_layer_1</primary_discovery_path>
    <alternative_paths>
      <path>auto_generation_entry_point</path>
      <path>beginner_friendly_command_creation</path>
      <path>30_second_success_path</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/prompt-engineering-best-practices.md"/>
      <file type="component" ref=".claude/components/atomic/template-selector.md"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="build-command" layer="2"/>
      <file type="command" ref="assemble-command" layer="3"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="quick-task" similarity="0.90"/>
      <file type="command" ref="quick-dev" similarity="0.85"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>user_needs_command_in_30_seconds</scenario>
      <scenario>beginner_with_no_customization_knowledge</scenario>
      <scenario>standard_use_case_matching_templates</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>complex_multi_step_workflows</scenario>
      <scenario>highly_customized_requirements</scenario>
      <scenario>needs_specific_component_control</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>quick command auto generate template layer 1 progressive disclosure 30 second</keywords>
    <semantic_tags>auto_generation beginner_friendly instant_command zero_learning_curve</semantic_tags>
    <functionality_vectors>[1.0, 0.2, 0.1, 0.8, 0.9]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>10</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref=".claude/context/progressive-disclosure-guide.md" importance="critical"/>
      <context_file ref=".claude/context/command-templates.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref=".claude/context/llm-antipatterns.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>entry_point</workflow_stage>
    <integration_patterns>
      <pattern>template_selection</pattern>
      <pattern>component_auto_assembly</pattern>
      <pattern>command_generation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>progressive_disclosure_layer_1</concept_introduction>
    <skill_progression>beginner</skill_progression>
    <mastery_indicators>
      <indicator>successful_auto_generation</indicator>
      <indicator>30_second_completion</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# 🚀 Layer 1: Auto-Generation v2.0 

<context type="project">
Progressive Disclosure System Layer 1 for lusaka template library providing 30-second command auto-generation with zero learning curve. Supports 5 command types (search, analyze, transform, validate, report) with intelligent template selection and automatic component assembly.
</context>

<instructions>
Auto-generate complete, working commands from $TYPE and $DESCRIPTION using intelligent template selection, automatic component assembly, and quality assurance. Deliver ready-to-use commands with proper YAML frontmatter, error handling, and usage examples within 30 seconds.
</instructions>

## Usage Examples

<examples>
<example>
<input>/quick-command search "find TODO comments in JavaScript"</input>
<expected_output>Complete /find-js-todos command with Grep pattern matching, file filtering, and result formatting</expected_output>
</example>
<example>
<input>/quick-command analyze "check Python code quality"</input>
<expected_output>Complete /analyze-python-quality command with code examination, quality metrics, and report generation</expected_output>
</example>
<example>
<input>/quick-command transform "convert JSON files to YAML"</input>
<expected_output>Complete /convert-json-yaml command with file discovery, format conversion, and backup creation</expected_output>
</example>
<example>
<input>/quick-command validate "check all API responses"</input>
<expected_output>Complete /validate-api-responses command with input checking, validation logic, and error reporting</expected_output>
</example>
</examples>

## Auto-Generation Workflow

<workflow type="sequential">
<task priority="high">
**Intent Analysis & Type Detection**: Parse command requirements
- Analyze $DESCRIPTION to understand desired functionality
- Validate $TYPE against supported categories (search, analyze, transform, validate, report)
- Identify key patterns, file types, and operations
- Determine optimal implementation approach automatically
</task>

<task priority="high">
**Template Selection & Component Assembly**: Intelligent automation
- **Search commands**: Pattern matching with file filtering using Grep/Glob
- **Analyze commands**: Code examination with quality metrics using Read/Grep
- **Transform commands**: Data conversion with validation using Read/Write/Edit
- **Validate commands**: Input checking with error reporting using validation patterns
- **Report commands**: Data aggregation with formatting using analysis and output tools
</task>

<task priority="high">
**Auto-Component Integration**: Quality assurance inclusion
- Input validation (required for all command types)
- Core processing logic (type-specific implementation)
- Error handling (comprehensive scenarios coverage)
- Output formatting (consistent, actionable results)
- Progress tracking (for operations requiring time)
</task>

<task priority="medium">
**Command Generation & Validation**: Production-ready output
- Generate complete YAML frontmatter with v2.0 metadata
- Implement functional command logic with best practices
- Include comprehensive error handling and edge cases
- Add usage examples and documentation
- Validate generated command for immediate usability
</task>
</workflow>

## 🧠 Intelligent Auto-Generation System

### **Command Type Intelligence Matrix:**

#### **Search Commands** (`search`)
- **Detection Pattern**: Pattern search + file filtering requirements
- **Generated Components**: Grep patterns, file globbing, result formatting
- **Automatic Inclusions**: Input validation, search logic, output structuring
- **Example Output**: `/find-js-todos` command ready for immediate execution

#### **Analysis Commands** (`analyze`)
- **Detection Pattern**: Code analysis + language-specific examination
- **Generated Components**: File discovery, analysis patterns, report generation
- **Automatic Inclusions**: Quality metrics, pattern recognition, recommendation engine
- **Example Output**: `/analyze-python-quality` command with comprehensive reporting

#### **Transform Commands** (`transform`)
- **Detection Pattern**: Format conversion + batch processing requirements
- **Generated Components**: File discovery, transformation logic, backup systems
- **Automatic Inclusions**: Data validation, conversion algorithms, safety mechanisms
- **Example Output**: `/convert-json-yaml` command with backup and validation

#### **Validation Commands** (`validate`)
- **Detection Pattern**: Input checking + integrity verification needs
- **Generated Components**: Validation rules, error detection, reporting systems
- **Automatic Inclusions**: Rule engines, compliance checking, detailed error output
- **Example Output**: `/validate-api-responses` command with comprehensive validation

#### **Report Commands** (`report`)
- **Detection Pattern**: Data aggregation + summary generation requirements
- **Generated Components**: Data collection, analysis engines, formatting systems
- **Automatic Inclusions**: Statistics calculation, visualization, executive summaries
- **Example Output**: `/summarize-test-results` command with actionable insights

## 🎯 Layer 1 Success Metrics

### **30-Second Success Guarantee:**
- **Zero Learning Curve**: No documentation reading required
- **Instant Productivity**: Working command in 30 seconds or less
- **High Success Rate**: >95% user satisfaction with generated commands
- **Quality Results**: Production-ready commands with comprehensive error handling

### **Quality Assurance Features:**
- **Automatic Error Handling**: File not found, permissions, invalid inputs, format issues
- **Input Validation**: Parameter checking, path sanitization, type verification, safety checks
- **Output Quality**: Consistent formatting, clear indicators, actionable messages, progress tracking
- **Best Practices**: Claude Code conventions, security considerations, performance optimization

## 🔄 Progressive Disclosure Navigation

### **Current Layer (Layer 1):**
**Perfect for**: Newcomers, quick tasks, immediate results, zero complexity

### **Next Level Options:**

#### **Layer 2: Guided Customization**
```
/build-command [type] [description] --customize
```
- **When to use**: Generated command is close but needs specific adjustments
- **Time investment**: 5 minutes guided customization
- **User experience**: 3-5 relevant options, no overwhelming complexity

#### **Layer 3: Professional Assembly**
```
/assemble-command --interactive
```
- **When to use**: Complex workflows, enterprise requirements, maximum control
- **Time investment**: 15-30 minutes professional assembly
- **User experience**: Full component library access with organized tools

<automation trigger="completion">
- Generate complete, functional command with proper YAML frontmatter and v2.0 enhancements
- Validate command syntax and logic for immediate usability
- Provide clear usage instructions and escalation paths to Layer 2/3
- Update auto-generation intelligence based on successful command patterns
</automation>