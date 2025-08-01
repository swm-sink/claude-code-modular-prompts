---
command: build-command
description: Layer 2 Progressive Disclosure - Generate commands with intelligent guided customization options and 5-minute success guarantee
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
  - name: OPTIONS
    type: string
    required: false
    description: Customization flags (--customize, --interactive, --with [settings])
usage_examples:
  - "/build-command search 'find TODO comments' --customize"
  - "/build-command analyze 'check code quality' --with file-types=js,ts output=detailed"
  - "/build-command transform 'convert files' --interactive"
  - "/build-command validate 'API responses' --customize"
prerequisites: 
  - "Understanding of desired command functionality"
  - "Basic familiarity with customization needs"
output_format: structured
tags: [guided-customization, progressive-disclosure, layer-2, smart-options, v2-enhanced]
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
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/commands/core/build-command.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>build-command</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>2</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="input_handling"/>
      <component ref="option-filter" role="smart_filtering"/>
      <component ref="customization-engine" role="guided_customization"/>
      <component ref="command-generator" role="output_creation"/>
    </required_components>
    <optional_components>
      <component ref="interactive-prompt" benefit="user_interaction"/>
      <component ref="validation-framework" benefit="quality_assurance"/>
      <component ref="preview-generator" benefit="user_confirmation"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="assemble-command" context="layer_3_escalation"/>
      <command ref="validate-command" context="quality_check"/>
      <command ref="preview-command" context="output_preview"/>
    </invokable_commands>
    <orchestration_patterns>sequential|conditional|interactive</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Generate customized commands with guided option selection</task_description>
    <implementation_strategy>parse_input|analyze_context|filter_options|guide_customization|generate_command|validate_output</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>progressive_disclosure_layer_2</primary_discovery_path>
    <alternative_paths>
      <path>guided_customization_entry_point</path>
      <path>intermediate_command_creation</path>
      <path>5_minute_success_path</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/customization-patterns.md"/>
      <file type="component" ref=".claude/components/atomic/option-filter.md"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="assemble-command" layer="3"/>
      <file type="workflow" ref="customization-workflow"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="customize-command" similarity="0.80"/>
      <file type="command" ref="interactive-build" similarity="0.75"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>user_needs_customization_guidance</scenario>
      <scenario>intermediate_user_with_specific_needs</scenario>
      <scenario>5_minute_customization_window</scenario>
      <scenario>smart_option_filtering_required</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_standard_use_case</scenario>
      <scenario>expert_needing_full_control</scenario>
      <scenario>time_critical_30_second_need</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>build command customize guided layer 2 progressive disclosure 5 minute options</keywords>
    <semantic_tags>guided_customization smart_filtering intermediate_complexity option_selection</semantic_tags>
    <functionality_vectors>[0.5, 0.7, 0.6, 0.8, 0.7]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>local</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref=".claude/context/progressive-disclosure-guide.md" importance="critical"/>
      <context_file ref=".claude/context/customization-patterns.md" importance="high"/>
      <context_file ref=".claude/context/option-filtering-rules.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref=".claude/context/user-experience-patterns.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>customization</workflow_stage>
    <integration_patterns>
      <pattern>option_analysis</pattern>
      <pattern>smart_filtering</pattern>
      <pattern>guided_selection</pattern>
      <pattern>command_generation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>progressive_disclosure_layer_2</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>successful_guided_customization</indicator>
      <indicator>5_minute_completion</indicator>
      <indicator>appropriate_option_selection</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# 🛠️ Layer 2: Guided Customization v2.0

<context type="project">
Progressive Disclosure System Layer 2 for lusaka template library providing intelligent guided customization with smart option filtering. Bridges the gap between Layer 1 auto-generation and Layer 3 professional assembly with 5-minute success guarantee and maximum 5 customization options.
</context>

<instructions>
Generate customized commands from $TYPE and $DESCRIPTION using guided customization process. Apply smart option filtering to show only 3-5 relevant choices, provide preview functionality, and enable iterative customization. Process $OPTIONS for customization mode (--customize, --interactive, --with settings).
</instructions>

## Usage Examples

<examples>
<example>
<input>/build-command search "find TODO comments" --customize</input>
<expected_output>Generated search command with 3-5 relevant customization options: file types, output format, search scope, pattern matching</expected_output>
</example>
<example>
<input>/build-command analyze "check code quality" --with file-types=js,ts output=detailed</input>
<expected_output>Analysis command with immediate customizations applied: JavaScript/TypeScript focus with detailed reporting</expected_output>
</example>
<example>
<input>/build-command transform "convert files" --interactive</input>
<expected_output>Step-by-step interactive customization experience with preview and modification options</expected_output>
</example>
<example>
<input>/build-command validate "API responses" --customize</input>
<expected_output>Validation command with customization options: validation rules, error handling, report format, compliance checks</expected_output>
</example>
</examples>

## Guided Customization Workflow

<workflow type="sequential">
<task priority="high">
**Auto-Generation Foundation**: Create working baseline command
- Generate functional command using intelligent template analysis
- Establish baseline functionality that works immediately
- Identify customization opportunities based on command type and description
- Prepare smart option filtering for relevant customization categories
</task>

<task priority="high">
**Smart Option Filtering**: Present only relevant customization choices
- **Maximum 5 options** to prevent overwhelming complexity
- Filter options based on command type, description patterns, and context
- Group related options logically (File Filtering, Search Patterns, Output Format, etc.)
- Provide clear explanations of what each option accomplishes
</task>

<task priority="high">
**Interactive Customization Process**: Guide user through modifications
- Present customization options with current defaults clearly marked
- Allow multiple selection patterns (1,2,3 or specific option names)
- Show exactly what changes when options are selected
- Provide preview functionality before final command generation
</task>

<task priority="medium">
**Command Generation & Validation**: Create customized command
- Apply selected customizations to baseline command
- Generate complete YAML frontmatter with v2.0 enhancements
- Include comprehensive error handling and validation
- Provide usage examples and integration guidance
</task>
</workflow>

## 🎯 Smart Customization Categories by Command Type

### **Search Commands** - Pattern Matching & File Discovery
**Intelligent Options (3-5 maximum):**
- **File Filtering**: JavaScript only, Python only, All code files, Specific extensions, Location scope
- **Pattern Matching**: Exact match, Regular expressions, Case insensitive, Fuzzy matching, Context inclusion
- **Output Format**: File list only, With line numbers, Content preview, Full context, Grouping options
- **Search Scope**: Current folder, Include subdirectories, Exclude test files, Hidden files handling

### **Analysis Commands** - Code Quality & Metrics
**Intelligent Options (3-5 maximum):**
- **Analysis Scope**: Language-specific focus, All code files, Include config files, Analysis depth
- **Quality Metrics**: Complexity metrics, Size metrics, Quality checks, Documentation coverage
- **Report Format**: Executive summary, Detailed findings, Technical deep-dive, Output style preferences
- **Focus Areas**: Security only, Performance only, Quality metrics, Code style compliance

### **Transform Commands** - File Processing & Conversion
**Intelligent Options (3-5 maximum):**
- **Input Handling**: Source patterns, Validation strictness, Backup strategy, File type filtering
- **Transform Options**: Conversion type, Processing mode, Quality control, Progress reporting
- **Output Control**: Destination handling, Naming conventions, Verification methods, Safety checks
- **Processing Mode**: Single file, Batch processing, Parallel processing, Error handling

### **Validation Commands** - Compliance & Quality Assurance
**Intelligent Options (3-5 maximum):**
- **Validation Rules**: Strictness levels, Rule sets, Scope definition, Framework-specific rules
- **Error Handling**: Error response strategy, Reporting detail, Fix suggestions, Auto-fix options
- **Output Format**: Console output, File reports, JSON results, Integration formats
- **Compliance Focus**: Syntax only, Semantic validation, Best practices, Security checks

### **Report Commands** - Data Analysis & Visualization
**Intelligent Options (3-5 maximum):**
- **Content Selection**: Data sources, Time range, Scope definition, Change tracking
- **Report Format**: Output type, Detail level, Visualization options, Export formats
- **Analysis Depth**: Current state, Historical trends, Comparative analysis, Trend indicators
- **Delivery Method**: Markdown, HTML, PDF, JSON, CSV, Dashboard integration

## 💡 Interactive Customization Examples

### **Security Vulnerability Search Example:**
```
🔍 Search Patterns [Current: basic security keywords]
   • Basic security keywords (current) - Common vulnerability terms
   • Advanced vulnerability patterns - Regex patterns for complex issues  
   • Framework-specific - Patterns for React, Express, etc.

📁 File Scope [Current: all code files]
   • All code files (current) - JavaScript, Python, Java, etc.
   • Security-critical files only - Auth, config, API files
   • Include configuration files - .env, config files, etc.

📊 Report Detail [Current: file list with line numbers]
   • File list with line numbers (current)
   • Detailed context extraction - Show surrounding code
   • Risk assessment summary - Severity and impact analysis  

Choose options to customize (1,2,3) or press Enter for current settings:
```

### **JSON to YAML Transform Example:**
```
📁 Input Selection [Current: all .json files]
   • All .json files (current)
   • Config files only - package.json, tsconfig.json, etc.
   • Specific directory - Choose which folder to convert

🔄 Conversion Options [Current: standard conversion]
   • Standard conversion (current) - Direct JSON→YAML conversion
   • Format optimization - Clean formatting and consistent indentation
   • Validation included - Verify YAML syntax after conversion

💾 Backup & Safety [Current: create .bak files]
   • Create .bak files (current) - Simple backup before conversion
   • Git staging - Use git to track changes
   • Timestamped backups - Keep multiple backup versions

Choose options to customize (1,2,3) or press Enter for current settings:
```

## 🔄 Progressive Disclosure Navigation

### **Current Layer (Layer 2):**
**Perfect for**: Users who need specific adjustments, controlled complexity, 5-minute customization

### **Layer Transitions:**

#### **Progressive Discovery Path**:
```
"Need customization options? Use: /build-command search 'find API calls' --customize"
```

#### **To Layer 3** (Professional Assembly Escalation):
```
/build-command analyze "complex workflow analysis" --customize
→ "Need maximum control? Try: /assemble-command --interactive"
```

## 🎯 Layer 2 Success Metrics

### **5-Minute Success Guarantee:**
- **90% user success rate** achieving desired customization in under 5 minutes
- **Maximum 5 options** presented to prevent overwhelming complexity
- **Clear preview functionality** showing exactly what each option accomplishes
- **Iterative refinement** without starting over from scratch

### **Smart Filtering Principles:**
- **Context-aware options** based on command type and description analysis
- **Relevant choices only** - no generic options that don't apply
- **Clear explanations** of what each customization accomplishes
- **Default fallbacks** for immediate usability without customization

### **Quality Assurance Features:**
- **Preview before generation** with execution time estimates and impact analysis
- **Customization validation** ensuring selected options work together properly
- **Progressive complexity** with natural escalation paths to Layer 3
- **Integration guidance** for using generated commands effectively

## 📋 Command Type Specializations

### **Search Customization**: File patterns, Component types, Export formats, Documentation inclusion
### **Analysis Customization**: Profiling depth, Metrics focus, Report format, Threshold settings  
### **Transform Customization**: Target versions, Transform scope, Safety checks, Output styling
### **Validation Customization**: Schema validation, Error handling, Compliance rules, Report detail
### **Report Customization**: Metrics inclusion, Time range, Visualization options, Export formats

<automation trigger="completion">
- Generate customized command with selected options applied to baseline functionality
- Provide preview with execution estimates and customization impact analysis
- Offer clear escalation paths to Layer 3 for complex requirements beyond guided customization
- Update smart filtering algorithms based on successful customization patterns and user feedback
</automation>