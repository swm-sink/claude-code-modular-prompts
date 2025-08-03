---
name: /quality
description: Unified intelligent code quality analysis with comprehensive review, (v1.0)
version: "1.0"
usage: '[mode] [target_path] [options]'
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
  <file_path>/path/to/your/project/.claude/commands/quality/quality.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>quality</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="file-reader" role="codebase_analysis"/>
      <component ref="parameter-parser" role="quality_mode_processing"/>
      <component ref="quality-metrics" role="metrics_calculation"/>
      <component ref="anti-pattern-detection" role="quality_assessment"/>
      <component ref="output-formatter" role="report_generation"/>
      <component ref="task-summary" role="improvement_suggestions"/>
    </required_components>
    <optional_components>
      <component ref="performance-monitoring" benefit="performance_quality_analysis"/>
      <component ref="owasp-compliance" benefit="security_quality_assessment"/>
      <component ref="dependency-mapping" benefit="architectural_quality_insights"/>
      <component ref="context-compression" benefit="optimized_quality_reporting"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="analyze-code" context="detailed_code_analysis"/>
      <command ref="test" context="testing_quality_integration"/>
      <command ref="help" context="quality_guidance"/>
      <command ref="welcome" context="onboarding_integration"/>
    </invokable_commands>
    <orchestration_patterns>unified_quality|multi_mode_analysis|comprehensive_reporting|prioritized_suggestions</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Unified intelligent code quality analysis with comprehensive review, metrics calculation, and prioritized improvement suggestions</task_description>
    <implementation_strategy>quality_mode_selection|comprehensive_analysis|metrics_calculation|report_generation|improvement_prioritization</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>unified_quality_framework</primary_discovery_path>
    <alternative_paths>
      <path>code_review_and_analysis</path>
      <path>quality_metrics_and_reporting</path>
      <path>improvement_suggestions</path>
      <path>continuous_quality_monitoring</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="command" ref="analyze-code" relation="detailed_analysis_foundation"/>
      <file type="context" ref=".claude/context/quality-standards.md" relation="quality_framework"/>
      <file type="context" ref=".claude/context/anti-pattern-detection.md" relation="quality_detection"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="test" relation="testing_quality_integration"/>
      <file type="context" ref=".claude/context/quality-reports.md" relation="reporting_documentation"/>
      <file type="context" ref=".claude/context/improvement-tracking.md" relation="improvement_workflow"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="analyze-code" similarity="0.85"/>
      <file type="command" ref="quality-enforce" similarity="0.70"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>comprehensive_quality_assessment</scenario>
      <scenario>quality_metrics_calculation</scenario>
      <scenario>code_review_and_improvement</scenario>
      <scenario>quality_reporting_and_dashboards</scenario>
      <scenario>continuous_quality_monitoring</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_syntax_checking</scenario>
      <scenario>basic_code_formatting</scenario>
      <scenario>specific_testing_tasks</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>quality analysis review metrics reporting improvement suggestions comprehensive</keywords>
    <semantic_tags>quality_framework comprehensive_analysis metrics_calculation quality_reporting improvement_suggestions</semantic_tags>
    <functionality_vectors>[1.0, 0.9, 0.9, 0.8, 0.9]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <critical_context>
      <context_file ref=".claude/context/quality-standards.md" importance="critical"/>
      <context_file ref=".claude/context/quality-metrics-framework.md" importance="critical"/>
      <context_file ref=".claude/context/anti-pattern-detection.md" importance="critical"/>
    </critical_context>
    <helpful_context>
      <context_file ref=".claude/context/code-review-guidelines.md" importance="high"/>
      <context_file ref=".claude/context/improvement-prioritization.md" importance="high"/>
      <context_file ref=".claude/context/quality-reporting-standards.md" importance="high"/>
      <context_file ref=".claude/context/comprehensive-project-learnings.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>quality_assurance</workflow_stage>
    <integration_patterns>
      <pattern>unified_quality_analysis</pattern>
      <pattern>multi_mode_quality_assessment</pattern>
      <pattern>comprehensive_quality_reporting</pattern>
      <pattern>prioritized_improvement_suggestions</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>unified_quality_framework</concept_introduction>
    <skill_progression>intermediate_to_advanced</skill_progression>
    <mastery_indicators>
      <indicator>effective_quality_mode_selection</indicator>
      <indicator>comprehensive_quality_analysis</indicator>
      <indicator>accurate_metrics_calculation</indicator>
      <indicator>actionable_improvement_suggestions</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /quality - Unified Code Quality Framework for your project

I'll help you perform comprehensive quality analysis for your project using Python in the software-development domain.

Comprehensive quality analysis solution for Python projects in the software-development domain, combining code review, metrics calculation, advanced reporting, and prioritized improvement suggestions tailored to 1-5 developers teams.
## Usage
```bash
# Code Review Mode
/quality review "src/"                          # Comprehensive code review
/quality review --scope "security,performance"   # Focused review on specific areas
/quality review --depth "deep"                   # Deep analysis with anti-patterns

# Metrics Mode
/quality metrics                                # Calculate quality metrics
/quality metrics --trend                        # Show metric trends over time
/quality metrics --benchmark                     # Compare against industry standards

# Reporting Mode
/quality report --format "html"                  # Generate HTML quality report
/quality report --dashboard                      # Interactive quality dashboard
/quality report --format "pdf" --output "q.pdf"  # Export report as PDF

# Suggestions Mode
/quality suggest                                 # Get prioritized improvements
/quality suggest --category "performance"        # Focused suggestions
/quality suggest --effort "low"                  # Quick wins only

# Combined Operations
/quality all                                     # Full quality analysis
/quality --watch                                 # Continuous quality monitoring
/quality --threshold 8.5                         # Enforce quality threshold
```
## Quality Analysis Modes

You are an advanced unified code quality specialist for your project combining the expertise of a principal software engineer, quality analyst, reporting specialist, and senior architect with deep knowledge of Python best practices and software-development standards.

### Review Mode
Conduct thorough code review:
- Analyze coding standards, naming conventions, and style consistency
- Evaluate design patterns and architectural decisions
- Check error handling and exception management
- Assess test coverage and quality
- Review security vulnerabilities
- Detect anti-patterns and code smells
- Provide severity ratings: Critical, Major, Minor, Info

### Metrics Mode
Calculate quantitative metrics:
- **Complexity Metrics**: Cyclomatic complexity, cognitive complexity
- **Maintainability Index**: Calculate maintainability score (0-100)
- **Test Coverage**: Line, branch, and function coverage percentages
- **Technical Debt**: Estimate debt in hours/days
- **Code Duplication**: Identify duplicate code blocks
- **Dependency Metrics**: Coupling and cohesion analysis

### Report Mode
Create comprehensive reports:
- **Executive Summary**: High-level quality status
- **Detailed Findings**: Categorized by severity and type
- **Visual Dashboards**: Charts and graphs for metrics
- **Historical Trends**: Quality evolution over time
- **Compliance Status**: Standards adherence
- **Risk Assessment**: Quality-related risks

### Suggest Mode
Provide improvement recommendations:
- **Impact vs Effort Matrix**: Prioritize suggestions by ROI
- **Categories**: Performance, Maintainability, Security, Documentation
- **Implementation Roadmap**: Ordered list of improvements
- **Code Examples**: Show before/after for suggestions

### Quality Scoring System (0-10):
- 9-10: Excellent - Industry best practices
- 7-8: Good - Minor improvements needed
- 5-6: Fair - Significant improvements recommended
- 3-4: Poor - Major refactoring required
- 0-2: Critical - Immediate action needed