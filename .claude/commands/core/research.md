---
name: /research
description: Comprehensive research framework with source validation and actionable insights (v1.0)
version: "1.0"
usage: '/research [topic] [--depth shallow|standard|comprehensive] [--focus technical|business|competitive] [--sources web|codebase|both]'
category: core
allowed-tools:
- Read
- Write
- Grep
- WebSearch
- WebFetch
dependencies:
- /analyze-code
- /query
- /validate-component
validation:
  pre-execution: Validate topic scope and research parameters
  during-execution: Verify source credibility and information accuracy
  post-execution: Ensure actionable recommendations are provided
progressive-disclosure:
  layer-integration: Layer 1 quick answers, Layer 2 detailed analysis, Layer 3 comprehensive research reports
  escalation-path: Quick lookup → detailed research → academic-level analysis
  de-escalation: Cached results speed up repeated research
safety-measures:
  - Verify source credibility
  - Cross-reference information
  - Flag outdated content
  - Highlight biases
error-recovery:
  no-results: Broaden search scope and suggest alternatives
  conflicting-info: Present multiple viewpoints with analysis
  source-unavailable: Use cached data with freshness warnings
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/commands/core/research.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>research</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="research_parameter_processing"/>
      <component ref="search-files" role="codebase_research"/>
      <component ref="intelligent-summarization" role="information_synthesis"/>
      <component ref="validation-framework" role="source_validation"/>
    </required_components>
    <optional_components>
      <component ref="context-optimization" benefit="research_focus"/>
      <component ref="generate-structured-report" benefit="actionable_insights"/>
      <component ref="progress-tracking" benefit="research_progress"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="analyze-code" context="codebase_analysis"/>
      <command ref="query" context="information_lookup"/>
      <command ref="validate-component" context="research_validation"/>
    </invokable_commands>
    <orchestration_patterns>multi_source|depth_adaptive|validation_focused</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Comprehensive research framework with multi-source validation, depth control, and actionable insights generation</task_description>
    <implementation_strategy>topic_analysis|source_selection|information_gathering|cross_validation|synthesis|actionable_recommendations</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>comprehensive_research_framework</primary_discovery_path>
    <alternative_paths>
      <path>information_gathering_system</path>
      <path>knowledge_synthesis_engine</path>
      <path>multi_source_validation</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/research-methodologies.md" relation="research_guidance"/>
      <file type="component" ref=".claude/components/intelligence/intelligent-summarization.md" relation="synthesis_engine"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="analyze-code" relation="technical_analysis"/>
      <file type="command" ref="query" relation="information_lookup"/>
      <file type="workflow" ref="research_reports" relation="generates"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="query" similarity="0.70"/>
      <file type="command" ref="analyze-code" similarity="0.60"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>comprehensive_topic_investigation</scenario>
      <scenario>multi_source_information_gathering</scenario>
      <scenario>competitive_analysis_and_benchmarking</scenario>
      <scenario>technology_evaluation_and_selection</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_factual_lookups</scenario>
      <scenario>time_critical_quick_answers</scenario>
      <scenario>already_well_understood_topics</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>research comprehensive analysis investigation validation sources insights</keywords>
    <semantic_tags>research_framework information_synthesis multi_source_validation actionable_insights</semantic_tags>
    <functionality_vectors>[0.7, 0.9, 0.8, 0.8, 0.9]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>8</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref=".claude/context/research-methodologies.md" importance="high"/>
      <context_file ref=".claude/context/source-validation-patterns.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref=".claude/context/information-synthesis-techniques.md" importance="medium"/>
      <context_file ref=".claude/context/competitive-analysis-frameworks.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>investigation</workflow_stage>
    <integration_patterns>
      <pattern>multi_source_research</pattern>
      <pattern>credibility_validation</pattern>
      <pattern>information_synthesis</pattern>
      <pattern>actionable_recommendations</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>comprehensive_research_methodology</concept_introduction>
    <skill_progression>intermediate</skill_progression>
    <mastery_indicators>
      <indicator>thorough_multi_source_analysis</indicator>
      <indicator>effective_source_validation</indicator>
      <indicator>actionable_insights_generation</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# Research Framework for lusaka

I'll help you research topics relevant to your software-development project, providing comprehensive analysis and actionable insights for Python implementation.

## Usage

```bash
/research "authentication best practices"
/research "API design patterns" --depth comprehensive
/research "database optimization" --focus technical
/research "competitor analysis" --focus business
```

## Research Approach

1. **Topic Analysis**: Break down the research question
2. **Source Gathering**: Find relevant technical documentation and best practices
3. **Analysis**: Evaluate options and trade-offs
4. **Recommendations**: Provide specific guidance for lusaka
5. **Implementation Notes**: Connect research to practical next steps

I'll tailor the research to your Python environment and swm-sink's context.

## Depth Levels

- **Shallow**: Quick overview and key points
- **Standard**: Comprehensive analysis with examples
- **Comprehensive**: Deep dive with multiple perspectives and detailed implementation guidance