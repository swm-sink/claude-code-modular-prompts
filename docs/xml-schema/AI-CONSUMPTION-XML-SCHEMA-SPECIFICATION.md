# AI-Consumption XML Schema Specification for Claude Code Modular Prompts

## Overview

This document defines a comprehensive XML tagging system designed specifically for AI consumption across the Claude Code Modular Prompts template library. The schema complements existing YAML frontmatter and enables AI to effectively navigate, understand, and assemble modular prompts from 91 components into 88 commands.

## Core Design Principles

1. **AI-First**: Tags optimized for machine understanding, not human readability
2. **Relationship-Centric**: Emphasizes component-to-command mappings and dependencies
3. **Progressive Discovery**: Supports 3-layer Progressive Disclosure navigation
4. **Context-Aware**: Preserves project context across AI sessions
5. **Non-Invasive**: Complements existing YAML without modification

## Schema Structure

### 1. Document Type Classification

```xml
<ai_document_metadata>
  <document_type>command|component|context|documentation|report</document_type>
  <ai_consumption_priority>critical|high|medium|low</ai_consumption_priority>
  <content_structure>yaml_frontmatter|markdown_body|xml_enhanced|mixed</content_structure>
  <file_path>/absolute/path/to/file.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>
```

### 2. Component Metadata System

```xml
<component_metadata>
  <component_id>file-reader</component_id>
  <component_count>91</component_count>
  <category>atomic|analysis|orchestration|security|performance|intelligence</category>
  <subcategory>io_operations|data_processing|workflow_control|system_operations|user_interface|validation</subcategory>
  
  <complexity_metrics>
    <usage_complexity>simple|intermediate|advanced</usage_complexity>
    <implementation_effort>minutes_5|minutes_30|hours_2|days_1</implementation_effort>
    <prerequisite_knowledge>none|basic|intermediate|expert</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="data-transformer" strength="strong"/>
      <component ref="output-formatter" strength="medium"/>
      <component ref="error-handler" strength="required"/>
    </compatible_components>
    <incompatible_components>
      <component ref="file-writer" reason="conflicting_io_operations"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>data_ingestion</common_workflow>
    <common_workflow>file_processing</common_workflow>
    <typical_position>entry_point|processing|validation|output</typical_position>
  </usage_patterns>
</component_metadata>
```

### 3. Command Metadata System

```xml
<command_metadata>
  <command_id>task</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>1|2|3</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="file-reader" role="input_handling"/>
      <component ref="data-transformer" role="processing"/>
      <component ref="output-formatter" role="result_presentation"/>
    </required_components>
    <optional_components>
      <component ref="progress-indicator" benefit="user_feedback"/>
      <component ref="error-handler" benefit="robustness"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="project" context="project_initialization"/>
      <command ref="test-unit" context="quality_assurance"/>
    </invokable_commands>
    <orchestration_patterns>sequential|parallel|conditional|iterative</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Execute focused development task with best practices</task_description>
    <implementation_strategy>analyze_requirements|implement_solution|test_implementation|document_results</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>
```

### 4. AI Navigation and Discovery

```xml
<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>progressive_disclosure_layer_1</primary_discovery_path>
    <alternative_paths>
      <path>direct_search_by_functionality</path>
      <path>component_assembly_recommendation</path>
      <path>workflow_template_suggestion</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="component" ref="file-reader"/>
      <file type="context" ref="prompt-engineering-best-practices"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="quick-test"/>
      <file type="workflow" ref="data-pipeline-template"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="quick-task" similarity="0.85"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>user_needs_focused_task_execution</scenario>
      <scenario>development_workflow_automation</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_one_liner_operations</scenario>
      <scenario>requires_human_decision_making</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>task execution development workflow automation testing</keywords>
    <semantic_tags>implementation coding productivity quality_assurance</semantic_tags>
    <functionality_vectors>[0.8, 0.2, 0.6, 0.9, 0.3]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>
```

### 5. Context Engineering Tags

```xml
<context_engineering>
  <ai_understanding_scope>
    <scope_level>local|project|global</scope_level>
    <context_retention>session|persistent|temporary</context_retention>
    <memory_priority>1-10</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref="llm-antipatterns.md" importance="critical"/>
      <context_file ref="git-history-antipatterns.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref="prompt-engineering-best-practices.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>entry_point|processing|validation|output</workflow_stage>
    <integration_patterns>
      <pattern>component_selection</pattern>
      <pattern>command_assembly</pattern>
      <pattern>validation_checkpoint</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>progressive_disclosure</concept_introduction>
    <skill_progression>beginner|intermediate|advanced|expert</skill_progression>
    <mastery_indicators>
      <indicator>successful_command_generation</indicator>
      <indicator>component_compatibility_understanding</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
```

### 6. Assembly and Orchestration Metadata

```xml
<assembly_metadata>
  <assembly_templates>
    <template name="security-audit">
      <component_sequence>
        <step order="1" component="input-validation" required="true"/>
        <step order="2" component="path-validation" required="true"/>
        <step order="3" component="security-scan" required="true"/>
        <step order="4" component="report-generation" required="true"/>
      </component_sequence>
      <estimated_complexity>intermediate</estimated_complexity>
      <typical_duration>30_minutes</typical_duration>
    </template>
  </assembly_templates>
  
  <orchestration_rules>
    <rule type="compatibility">
      <if component="file-reader" then_compatible="data-transformer,output-formatter"/>
      <if component="file-writer" then_incompatible="file-reader"/>
    </rule>
    <rule type="performance">
      <if components_count=">10" then_recommend="parallel-execution"/>
    </rule>
  </orchestration_rules>
</assembly_metadata>
```

### 7. Quality and Validation Metadata

```xml
<quality_metadata>
  <validation_status>
    <structural_validation>passed|failed|pending</structural_validation>
    <functional_validation>passed|failed|pending|not_applicable</functional_validation>
    <last_validated>2025-07-31T12:00:00Z</last_validated>
  </validation_status>
  
  <quality_indicators>
    <documentation_completeness>0.95</documentation_completeness>
    <example_coverage>complete|partial|minimal</example_coverage>
    <anti_pattern_compliance>verified|unverified</anti_pattern_compliance>
  </quality_indicators>
  
  <maintenance_metadata>
    <maintenance_risk>low|medium|high</maintenance_risk>
    <scaling_threshold>150_commands</scaling_threshold>
    <deprecation_status>active|deprecated|legacy</deprecation_status>
  </maintenance_metadata>
</quality_metadata>
```

## Integration Standards

### 1. File Structure Integration

Commands and components should integrate XML tags within their existing markdown structure:

```markdown
---
command: task
description: Execute a focused development task
allowed-tools:
- Read
- Write
- Edit
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
</ai_document_metadata>

<command_metadata>
  <command_id>task</command_id>
  <progressive_disclosure_layer>1</progressive_disclosure_layer>
  <!-- Additional metadata -->
</command_metadata>
<!-- AI_METADATA_END -->

# /task - Focused Development Workflow

[Regular markdown content continues...]
```

### 2. Component Relationship Index

Create a central index file for AI navigation:

```xml
<!-- .claude/ai-index/component-command-map.xml -->
<ai_relationship_index>
  <component_to_command_mappings>
    <component id="file-reader">
      <used_by_commands>
        <command ref="task" usage="required"/>
        <command ref="analyze-code" usage="required"/>
        <command ref="quick-command" usage="optional"/>
      </used_by_commands>
    </component>
  </component_to_command_mappings>
  
  <progressive_disclosure_map>
    <layer_1>
      <commands>quick-command,quick-task,quick-dev,quick-test,quick-quality</commands>
      <auto_generation_capable>true</auto_generation_capable>
    </layer_1>
    <layer_2>
      <commands>build-command</commands>
      <guided_customization>true</guided_customization>
    </layer_2>
    <layer_3>
      <commands>assemble-command</commands>
      <component_access>full</component_access>
    </layer_3>
  </progressive_disclosure_map>
</ai_relationship_index>
```

## AI Navigation Reference

### How AI Should Use These Tags

1. **Initial Discovery**: Start with `ai_consumption_priority="critical"` documents
2. **Component Selection**: Use `assembly_compatibility` to find compatible components
3. **Command Assembly**: Follow `component_dependencies` for required components
4. **Workflow Creation**: Reference `assembly_templates` for proven patterns
5. **Quality Assurance**: Check `validation_status` and `quality_indicators`

### Navigation Workflow

```
User Request → Identify Layer (1/2/3) → Find Relevant Commands → 
Analyze Component Dependencies → Check Compatibility → 
Assemble Components → Validate Assembly → Generate Result
```

## Implementation Roadmap for Agent 3

1. **Phase 1: Core Infrastructure**
   - Create XML parsing utilities
   - Establish metadata injection points
   - Build central AI index

2. **Phase 2: Metadata Population**
   - Tag all 88 commands with command_metadata
   - Tag all 91 components with component_metadata
   - Create relationship mappings

3. **Phase 3: Navigation Implementation**
   - Build AI discovery algorithms
   - Implement compatibility checking
   - Create assembly validation

4. **Phase 4: Integration Testing**
   - Test component-to-command workflows
   - Validate Progressive Disclosure paths
   - Ensure backward compatibility

## Success Metrics

- AI can discover relevant components in <3 steps
- Component compatibility checks prevent 95% of invalid assemblies
- Command generation from components succeeds 90% of time
- Context preservation across sessions maintains project understanding

This schema provides a comprehensive framework for AI to navigate, understand, and effectively use the Claude Code Modular Prompts template library while maintaining the project's modular philosophy and Progressive Disclosure System.