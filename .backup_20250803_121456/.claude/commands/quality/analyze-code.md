---
name: /analyze-code
description: Unified code analysis with intelligent pattern detection, quality assessment, (v1.0)
version: "1.0"
usage: '[focus_mode] [target_path]'
category: quality
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate input parameters and execution context
  during-execution: Monitor progress and maintain safety checks
  post-execution: Verify successful completion and cleanup
progressive-disclosure:
  layer-integration: Integrated command for specialized workflows
  escalation-path: Basic usage → advanced options → full customization
  de-escalation: Simplify to essential functionality
safety-measures:
  - Validate all inputs before execution
  - Create backups when modifying files
  - Confirm destructive operations
  - Maintain system integrity
error-recovery:
  input-error: Provide clear usage examples and syntax
  execution-failure: Show detailed context and recovery steps
  system-error: Fallback to safe mode operation
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>high</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/path/to/your/project/.claude/commands/quality/analyze-code.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>analyze-code</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="file-reader" role="codebase_scanning"/>
      <component ref="parameter-parser" role="focus_mode_processing"/>
      <component ref="anti-pattern-detection" role="code_quality_assessment"/>
      <component ref="quality-metrics" role="quantitative_analysis"/>
      <component ref="pattern-extraction" role="design_pattern_identification"/>
      <component ref="task-summary" role="analysis_report_generation"/>
    </required_components>
    <optional_components>
      <component ref="framework-validation" benefit="technology_stack_analysis"/>
      <component ref="dependency-mapping" benefit="architectural_insights"/>
      <component ref="performance-monitoring" benefit="performance_bottleneck_detection"/>
      <component ref="owasp-compliance" benefit="security_analysis"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="help" context="analysis_guidance"/>
      <command ref="welcome" context="onboarding_integration"/>
      <command ref="test" context="testing_integration"/>
    </invokable_commands>
    <orchestration_patterns>focus_mode_selection|comprehensive_analysis|iterative_refinement|multi_dimensional</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Unified code analysis framework with intelligent pattern detection, quality assessment, and configurable focus modes</task_description>
    <implementation_strategy>focus_mode_handling|code_discovery|context_analysis|pattern_detection|quality_assessment|comprehensive_reporting</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>code_analysis_and_quality</primary_discovery_path>
    <alternative_paths>
      <path>quality_assessment</path>
      <path>pattern_detection</path>
      <path>security_analysis</path>
      <path>architectural_analysis</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/code-analysis-patterns.md" relation="analysis_methodology"/>
      <file type="context" ref=".claude/context/quality-metrics-framework.md" relation="quality_standards"/>
      <file type="component" ref="anti-pattern-detection" relation="quality_detection"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="test" relation="testing_workflow"/>
      <file type="context" ref=".claude/context/analysis-reports.md" relation="report_documentation"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="analyze-system" similarity="0.70"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>comprehensive_codebase_analysis</scenario>
      <scenario>quality_assessment_requirements</scenario>
      <scenario>pattern_detection_and_analysis</scenario>
      <scenario>security_vulnerability_assessment</scenario>
      <scenario>performance_bottleneck_identification</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_code_formatting</scenario>
      <scenario>specific_unit_testing</scenario>
      <scenario>basic_syntax_checking</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>analyze code quality patterns security performance architecture assessment</keywords>
    <semantic_tags>code_analysis quality_assessment pattern_detection security_analysis performance_optimization</semantic_tags>
    <functionality_vectors>[1.0, 0.9, 0.8, 0.9, 0.7]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>8</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <critical_context>
      <context_file ref=".claude/context/code-analysis-patterns.md" importance="critical"/>
      <context_file ref=".claude/context/quality-metrics-framework.md" importance="critical"/>
      <context_file ref=".claude/context/anti-pattern-detection.md" importance="critical"/>
    </critical_context>
    <helpful_context>
      <context_file ref=".claude/context/security-analysis-guide.md" importance="high"/>
      <context_file ref=".claude/context/performance-analysis-patterns.md" importance="high"/>
      <context_file ref=".claude/context/architectural-patterns.md" importance="medium"/>
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>analysis_and_assessment</workflow_stage>
    <integration_patterns>
      <pattern>focus_mode_driven_analysis</pattern>
      <pattern>multi_dimensional_assessment</pattern>
      <pattern>pattern_detection_and_classification</pattern>
      <pattern>comprehensive_quality_evaluation</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>unified_code_analysis_framework</concept_introduction>
    <skill_progression>intermediate_to_advanced</skill_progression>
    <mastery_indicators>
      <indicator>effective_focus_mode_selection</indicator>
      <indicator>comprehensive_pattern_detection</indicator>
      <indicator>accurate_quality_assessment</indicator>
      <indicator>actionable_analysis_reporting</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /analyze-code - Unified Code Analysis Framework for your project
Comprehensive code analysis system for Python applications, combining intelligent pattern detection, quality assessment, security review, and architectural insights with configurable focus modes tailored for software-development projects.

## Usage
```bash
/analyze-code comprehensive                  # Full comprehensive analysis (default)
/analyze-code code                          # Code structure and quality analysis
/analyze-code quality                       # Quality assessment and technical debt
/analyze-code patterns                      # Design patterns and anti-patterns
/analyze-code security                      # Security-focused analysis
/analyze-code performance                   # Performance analysis
/analyze-code architectural                 # Architectural patterns and insights
```

## Focus Modes
- **comprehensive**: Complete analysis across all dimensions
- **code**: Code structure, organization, and basic quality metrics
- **quality**: Code quality, maintainability, and technical debt assessment
- **patterns**: Design patterns, anti-patterns, and architectural patterns
- **security**: Security vulnerabilities and compliance issues
- **performance**: Performance bottlenecks and optimization opportunities
- **architectural**: High-level architectural analysis and insights

## Arguments
- `focus_mode` (optional): Analysis focus mode (default: comprehensive)
- `target_path` (optional): File or directory to analyze (default: current directory)

## Analysis Framework

You are an advanced code analysis specialist and software architect for your project with deep expertise in Python architecture and software-development patterns.

### Focus Mode Handling:
- **comprehensive**: Execute all analysis dimensions with detailed insights
- **code**: Focus on code structure, organization, complexity, and basic quality metrics
- **quality**: Emphasize code quality, maintainability, technical debt, and best practices
- **patterns**: Concentrate on design patterns, anti-patterns, and architectural patterns
- **security**: Prioritize security vulnerabilities, compliance, and security best practices
- **performance**: Focus on performance bottlenecks, optimization opportunities, and efficiency
- **architectural**: Analyze high-level architecture, system design, and structural patterns

### Core Analysis Process:
1. **Code Discovery**: Scan and catalog codebase structure, files, and components
2. **Context Analysis**: Understand project structure, Python architecture, and software-development patterns
3. **Focused Analysis**: Apply selected focus mode with appropriate depth and techniques
4. **Pattern Detection**: Identify relevant patterns based on focus mode
5. **Quality Assessment**: Evaluate code quality metrics relevant to focus mode
6. **Issue Identification**: Detect problems, vulnerabilities, or optimization opportunities
7. **Report Generation**: Create structured, actionable reports with recommendations