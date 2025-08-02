# XML and YAML Integration Examples

## Overview

This document provides concrete examples of how XML metadata integrates with existing YAML frontmatter across different file types in the Claude Code Modular Prompts template library.

## Command Integration Examples

### Example 1: Layer 1 Command (Auto-Generation)

**File**: `.claude/commands/core/quick-command.md`

```markdown
---
command: quick-command
description: Layer 1 Progressive Disclosure - Auto-generate complete commands
category: core
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
  <file_path>/Users/project/.claude/commands/core/quick-command.md</file_path>
  <last_modified>2025-07-31T10:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>quick-command</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>1</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="input_processing"/>
      <component ref="intelligent-template-selector" role="template_matching"/>
      <component ref="command-generator" role="output_generation"/>
    </required_components>
    <optional_components>
      <component ref="validation-framework" benefit="quality_assurance"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="validate-command" context="post_generation_validation"/>
    </invokable_commands>
    <orchestration_patterns>sequential</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Auto-generate commands from simple descriptions in 30 seconds</task_description>
    <implementation_strategy>parse_description|select_template|generate_command|validate_output</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>progressive_disclosure_layer_1</primary_discovery_path>
    <alternative_paths>
      <path>search_by_auto_generation</path>
      <path>beginner_user_entry_point</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref="progressive-disclosure-guide"/>
      <file type="template" ref="command-generation-templates"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="build-command"/>
      <file type="command" ref="assemble-command"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="quick-task" similarity="0.75"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>user_needs_command_in_30_seconds</scenario>
      <scenario>beginner_with_no_experience</scenario>
      <scenario>simple_command_requirements</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>complex_multi_step_workflows</scenario>
      <scenario>needs_specific_component_control</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>auto generate quick command creation template instant</keywords>
    <semantic_tags>automation beginner_friendly zero_setup layer_1</semantic_tags>
    <functionality_vectors>[0.9, 0.1, 0.3, 0.7, 0.2]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <workflow_integration>
    <workflow_stage>entry_point</workflow_stage>
    <integration_patterns>
      <pattern>user_intent_capture</pattern>
      <pattern>template_selection</pattern>
      <pattern>command_generation</pattern>
    </integration_patterns>
  </workflow_integration>
</context_engineering>
<!-- AI_METADATA_END -->

# 🚀 Layer 1: Auto-Generation v1.0

[Regular command content continues...]
```

### Example 2: Layer 3 Command (Professional Assembly)

**File**: `.claude/commands/core/assemble-command.md`

```markdown
---
command: assemble-command
description: Layer 3 Progressive Disclosure - Advanced component assembly
category: core
allowed-tools:
- Write
- Read
- Grep
- Glob
- Edit
- MultiEdit
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/Users/project/.claude/commands/core/assemble-command.md</file_path>
  <last_modified>2025-07-31T10:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>assemble-command</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>3</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="component-browser" role="component_discovery"/>
      <component ref="compatibility-validator" role="assembly_validation"/>
      <component ref="workflow-assembler" role="component_integration"/>
    </required_components>
    <optional_components>
      <component ref="performance-analyzer" benefit="optimization"/>
      <component ref="documentation-generator" benefit="user_guidance"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="validate-component" context="component_verification"/>
      <command ref="test-integration" context="assembly_testing"/>
    </invokable_commands>
    <orchestration_patterns>parallel|conditional|iterative</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Professional component assembly with 91 components</task_description>
    <implementation_strategy>browse_components|check_compatibility|assemble_workflow|validate_assembly|generate_command</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>progressive_disclosure_layer_3</primary_discovery_path>
    <alternative_paths>
      <path>expert_user_direct_access</path>
      <path>complex_workflow_requirements</path>
    </alternative_paths>
  </discovery_metadata>
  
  <usage_context>
    <when_to_use>
      <scenario>expert_building_complex_workflow</scenario>
      <scenario>need_precise_component_control</scenario>
      <scenario>15_30_minute_professional_assembly</scenario>
    </when_to_use>
  </usage_context>
</ai_navigation>
<!-- AI_METADATA_END -->

# 🔧 Layer 3: Professional Assembly v1.0

[Regular command content continues...]
```

## Component Integration Examples

### Example 3: Atomic Component

**File**: `.claude/components/atomic/file-reader.md`

```markdown
# File Reader Component

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/project/.claude/components/atomic/file-reader.md</file_path>
  <last_modified>2025-07-31T10:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>file-reader</component_id>
  <component_count>91</component_count>
  <category>atomic</category>
  <subcategory>io_operations</subcategory>
  
  <complexity_metrics>
    <usage_complexity>simple</usage_complexity>
    <implementation_effort>minutes_5</implementation_effort>
    <prerequisite_knowledge>none</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="data-transformer" strength="strong"/>
      <component ref="format-converter" strength="strong"/>
      <component ref="output-formatter" strength="medium"/>
      <component ref="error-handler" strength="required"/>
      <component ref="path-validation" strength="strong"/>
    </compatible_components>
    <incompatible_components>
      <component ref="file-writer" reason="conflicting_io_operations"/>
    </incompatible_components>
  </assembly_compatibility>
  
  <usage_patterns>
    <common_workflow>data_ingestion</common_workflow>
    <common_workflow>file_processing</common_workflow>
    <common_workflow>content_analysis</common_workflow>
    <typical_position>entry_point</typical_position>
  </usage_patterns>
</component_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>atomic_components_io</primary_discovery_path>
  </discovery_metadata>
  
  <relationship_map>
    <downstream_consumers>
      <component ref="data-transformer"/>
      <component ref="content-sanitizer"/>
      <command ref="analyze-code"/>
    </downstream_consumers>
  </relationship_map>
  
  <ai_search_optimization>
    <keywords>read file input load content access</keywords>
    <semantic_tags>io_operation input_handling file_access</semantic_tags>
    <functionality_vectors>[0.1, 0.0, 0.0, 0.2, 0.9]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>
<!-- AI_METADATA_END -->

```
Read file contents with error handling:
- Validate file path format and accessibility permissions
- Execute Read tool with absolute path and optional line limits
- Parse file content according to detected file type
- Handle file not found errors with specific path recommendations
- Extract and return relevant content sections
- Generate structured report of read operation results
```
```

### Example 4: Orchestration Component

**File**: `.claude/components/orchestration/agent-orchestration.md`

```markdown
<prompt_component>
  <step name="Advanced Multi-Agent Orchestration">
    <description>
Sophisticated multi-agent coordination using advanced orchestration patterns
    </description>
  </step>

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>component</document_type>
  <ai_consumption_priority>medium</ai_consumption_priority>
  <content_structure>xml_enhanced</content_structure>
  <file_path>/Users/project/.claude/components/orchestration/agent-orchestration.md</file_path>
  <last_modified>2025-07-31T10:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<component_metadata>
  <component_id>agent-orchestration</component_id>
  <component_count>91</component_count>
  <category>orchestration</category>
  <subcategory>multi_agent_systems</subcategory>
  
  <complexity_metrics>
    <usage_complexity>advanced</usage_complexity>
    <implementation_effort>hours_2</implementation_effort>
    <prerequisite_knowledge>expert</prerequisite_knowledge>
  </complexity_metrics>
  
  <assembly_compatibility>
    <compatible_components>
      <component ref="task-planning" strength="required"/>
      <component ref="dependency-analysis" strength="required"/>
      <component ref="progress-tracking" strength="strong"/>
      <component ref="multi-agent-coordination" strength="strong"/>
    </compatible_components>
    <incompatible_components>
      <component ref="simple-task-execution" reason="complexity_mismatch"/>
    </incompatible_components>
  </assembly_compatibility>
</component_metadata>

<ai_navigation>
  <usage_context>
    <when_to_use>
      <scenario>complex_multi_step_workflows</scenario>
      <scenario>distributed_task_execution</scenario>
      <scenario>requires_agent_specialization</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_linear_workflows</scenario>
      <scenario>single_agent_sufficient</scenario>
    </when_not_to_use>
  </usage_context>
</ai_navigation>
<!-- AI_METADATA_END -->

  <agent_orchestration>
    [Component implementation continues...]
  </agent_orchestration>
</prompt_component>
```

## Context File Integration Example

### Example 5: Critical Context File

**File**: `.claude/context/comprehensive-project-learnings.md`

```markdown
# Comprehensive Project Learnings - Template Library Development

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>context</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/project/.claude/context/comprehensive-project-learnings.md</file_path>
  <last_modified>2025-07-31T10:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>global</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>10</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <provides_context_for>
      <pattern>anti_pattern_prevention</pattern>
      <pattern>project_maintenance_risks</pattern>
      <pattern>scalability_considerations</pattern>
    </provides_context_for>
  </knowledge_dependencies>
  
  <ai_learning_markers>
    <concept_introduction>llm_hallucination_metrics</concept_introduction>
    <concept_introduction>documentation_accuracy_crisis</concept_introduction>
    <concept_introduction>progress_theater</concept_introduction>
    <mastery_indicators>
      <indicator>recognizes_fake_metrics</indicator>
      <indicator>maintains_documentation_accuracy</indicator>
      <indicator>avoids_theatrical_language</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

## Executive Summary

This document captures critical learnings from extensive project reviews...
[Content continues...]
```

## Central AI Index Example

### Example 6: Component-Command Relationship Index

**File**: `.claude/ai-index/component-command-map.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ai_relationship_index version="1.0" last_updated="2025-07-31T10:00:00Z">
  
  <!-- Component to Command Mappings -->
  <component_to_command_mappings>
    <component id="file-reader" category="atomic">
      <used_by_commands>
        <command ref="task" usage="required" role="input_handling"/>
        <command ref="analyze-code" usage="required" role="file_access"/>
        <command ref="quick-command" usage="optional" role="file_operations"/>
        <command ref="test-unit" usage="optional" role="test_file_reading"/>
      </used_by_commands>
      <usage_frequency>high</usage_frequency>
    </component>
    
    <component id="data-transformer" category="atomic">
      <used_by_commands>
        <command ref="transform" usage="required" role="data_processing"/>
        <command ref="quick-command" usage="optional" role="format_conversion"/>
      </used_by_commands>
      <usage_frequency>medium</usage_frequency>
    </component>
    
    <component id="agent-orchestration" category="orchestration">
      <used_by_commands>
        <command ref="swarm" usage="required" role="multi_agent_coordination"/>
        <command ref="dag-orchestrate" usage="required" role="workflow_management"/>
      </used_by_commands>
      <usage_frequency>low</usage_frequency>
    </component>
  </component_to_command_mappings>
  
  <!-- Progressive Disclosure Layer Mapping -->
  <progressive_disclosure_map>
    <layer_1>
      <commands count="5">
        <command ref="quick-command"/>
        <command ref="quick-task"/>
        <command ref="quick-dev"/>
        <command ref="quick-test"/>
        <command ref="quick-quality"/>
      </commands>
      <characteristics>
        <auto_generation_capable>true</auto_generation_capable>
        <average_completion_time>30_seconds</average_completion_time>
        <user_expertise_required>none</user_expertise_required>
      </characteristics>
    </layer_1>
    
    <layer_2>
      <commands count="1">
        <command ref="build-command"/>
      </commands>
      <characteristics>
        <guided_customization>true</guided_customization>
        <average_completion_time>5_minutes</average_completion_time>
        <user_expertise_required>basic</user_expertise_required>
      </characteristics>
    </layer_2>
    
    <layer_3>
      <commands count="1">
        <command ref="assemble-command"/>
      </commands>
      <characteristics>
        <component_access>full</component_access>
        <average_completion_time>15_30_minutes</average_completion_time>
        <user_expertise_required>advanced</user_expertise_required>
      </characteristics>
    </layer_3>
  </progressive_disclosure_map>
  
  <!-- Assembly Templates Registry -->
  <assembly_templates>
    <template id="security-audit" complexity="intermediate">
      <components>
        <component ref="input-validation" order="1"/>
        <component ref="path-validation" order="2"/>
        <component ref="credential-protection" order="3"/>
        <component ref="security-scan" order="4"/>
        <component ref="report-generation" order="5"/>
      </components>
      <compatible_with_layers>2,3</compatible_with_layers>
    </template>
    
    <template id="data-pipeline" complexity="advanced">
      <components>
        <component ref="file-reader" order="1"/>
        <component ref="data-transformer" order="2"/>
        <component ref="format-converter" order="3"/>
        <component ref="response-validator" order="4"/>
        <component ref="output-formatter" order="5"/>
        <component ref="file-writer" order="6"/>
      </components>
      <compatible_with_layers>3</compatible_with_layers>
    </template>
  </assembly_templates>
  
  <!-- Global Statistics -->
  <global_statistics>
    <total_commands>88</total_commands>
    <total_components>91</total_components>
    <total_relationships>247</total_relationships>
    <average_components_per_command>3.2</average_components_per_command>
  </global_statistics>
  
</ai_relationship_index>
```

## Integration Best Practices

### 1. Maintain Separation
- YAML frontmatter remains unchanged
- XML metadata is clearly delimited
- Both formats coexist without conflict

### 2. Progressive Enhancement
- Files work without XML (backward compatible)
- XML adds AI navigation capabilities
- No functionality lost if XML ignored

### 3. Consistent Structure
- Same XML hierarchy across all file types
- Predictable element ordering
- Standardized attribute names

### 4. Validation Points
- XML well-formedness
- Cross-reference validity
- Count accuracy (91 components, 88 commands)
- Timestamp currency

---

These examples demonstrate practical XML and YAML integration patterns that enable effective AI navigation while maintaining Claude Code compatibility and human readability.