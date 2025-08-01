# Context File XML Template

This template provides the standardized XML metadata structure for all context files (.claude/context/ directory).

## Template Structure

```xml
<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>context</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>[FULL_FILE_PATH]</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<context_metadata>
  <context_type>[CONTEXT_TYPE]</context_type>
  <context_scope>[global|project|local]</context_scope>
  <importance_level>[critical|high|medium|low]</importance_level>
  <content_focus>[CONTENT_FOCUS]</content_focus>
</context_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>[CONTEXT_PATH]</primary_discovery_path>
    <usage_priority>[must_read_before_generation|helpful_background|reference_material]</usage_priority>
  </discovery_metadata>
  
  <relationship_map>
    <related_contexts>
      <file type="context" ref="[FILE_REFERENCE]" relation="[RELATIONSHIP]"/>
    </related_contexts>
    <prevents_issues_in>
      <file type="[TYPE]" ref="[FILE_REFERENCE]" scope="[SCOPE]"/>
    </prevents_issues_in>
    <enhances_understanding_of>
      <file type="[TYPE]" ref="[FILE_REFERENCE]" aspect="[ASPECT]"/>
    </enhances_understanding_of>
  </relationship_map>
  
  <ai_search_optimization>
    <keywords>[KEYWORD_LIST]</keywords>
    <semantic_tags>[SEMANTIC_TAG_LIST]</semantic_tags>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>[global|project|local]</scope_level>
    <context_retention>[persistent|session|temporary]</context_retention>
    <memory_priority>[1-10]</memory_priority>
  </ai_understanding_scope>
  
  <application_guidance>
    <when_to_reference>
      <scenario>[SCENARIO_DESCRIPTION]</scenario>
    </when_to_reference>
    <integration_patterns>
      <pattern>[PATTERN_NAME]</pattern>
    </integration_patterns>
  </application_guidance>
  
  <quality_impact>
    <prevents_antipatterns>[ANTIPATTERN_LIST]</prevents_antipatterns>
    <enhances_capabilities>[CAPABILITY_LIST]</enhances_capabilities>
    <critical_for>[FUNCTIONALITY_LIST]</critical_for>
  </quality_impact>
</context_engineering>
<!-- AI_METADATA_END -->
```

## Context Types

### Valid Context Types
- `anti_pattern_documentation`: Documents patterns to avoid
- `best_practices`: Recommended approaches and techniques
- `framework_guide`: How-to guides for framework usage
- `project_learnings`: Insights from project development
- `prompt_engineering`: Prompt optimization techniques
- `quality_standards`: Quality assurance guidelines
- `architectural_patterns`: System design patterns
- `integration_guide`: Integration and composition patterns

### Context Scope Levels
- `global`: Applies across all projects and contexts
- `project`: Specific to this template library project
- `local`: Specific to certain commands or components

### Usage Priority Levels
- `must_read_before_generation`: Critical context that should always be considered
- `helpful_background`: Useful context that improves quality
- `reference_material`: Available for specific needs or questions

## Field Descriptions

### Context-Specific Fields
- `context_type`: The type of contextual information provided
- `context_scope`: How broadly the context applies
- `importance_level`: Priority for AI consumption
- `content_focus`: Main topic or area of focus
- `prevents_antipatterns`: Specific antipatterns this context helps avoid
- `enhances_capabilities`: Areas where this context improves AI performance
- `critical_for`: Functionality that depends on this context

### Usage Notes
- Use `ai_consumption_priority: critical` for anti-patterns and core guides
- Context files should have high `memory_priority` (8-10)
- Include comprehensive relationship mapping to show context dependencies
- Focus on practical application guidance for AI systems