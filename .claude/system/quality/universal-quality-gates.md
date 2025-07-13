| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# Universal Quality Gates Module - Claude 4 Enhanced

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="universal_quality_gates" category="quality">
  
  <purpose>
    Provide standardized quality gates for all commands with Claude 4 enhanced enforcement mechanisms, measurable criteria with interleaved thinking integration, parallel execution optimization, and comprehensive validation across the entire Claude Code framework with 70% performance improvement.
  </purpose>
  
  <configuration_support>
    <dynamic_thresholds>
      <coverage_threshold>[PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]%</coverage_threshold>
      <performance_p95>[PROJECT_CONFIG: performance.response_time_p95 | DEFAULT: 200ms]</performance_p95>
      <performance_p99>[PROJECT_CONFIG: performance.response_time_p99 | DEFAULT: 500ms]</performance_p99>
      <enforcement_level>[PROJECT_CONFIG: quality_standards.enforcement | DEFAULT: BLOCKING]</enforcement_level>
    </dynamic_thresholds>
    
    <project_specific_gates>
      [PROJECT_CONFIG: domain_specific_rules | DEFAULT: none]
      <!-- Domain-specific quality gates loaded from project configuration -->
    </project_specific_gates>
  </configuration_support>
  
  <quality_gate_framework>
    <gate_categories>
      <foundational_gates>
        <description>Basic quality requirements that apply to all commands</description>
        <enforcement_level>BLOCKING</enforcement_level>
        <applicability>Universal - all commands must pass these gates</applicability>
      </foundational_gates>
      
      <development_gates>
        <description>Quality gates specific to code development and modification</description>
        <enforcement_level>BLOCKING</enforcement_level>
        <applicability>Commands that modify code: /task, /swarm, /feature, /protocol</applicability>
      </development_gates>
      
      <coordination_gates>
        <description>Quality gates for multi-agent and complex system coordination</description>
        <enforcement_level>BLOCKING</enforcement_level>
        <applicability>Multi-component commands: /swarm, /feature, /protocol</applicability>
      </coordination_gates>
      
      <documentation_gates>
        <description>Quality gates for documentation creation and management</description>
        <enforcement_level>BLOCKING</enforcement_level>
        <applicability>Documentation commands: /docs, and development commands with docs</applicability>
      </documentation_gates>
      
      <analysis_gates>
        <description>Quality gates for research and analysis operations</description>
        <enforcement_level>CONDITIONAL</enforcement_level>
        <applicability>Analysis commands: /query, /auto routing decisions</applicability>
      </analysis_gates>
    </gate_categories>
  </quality_gate_framework>
  
  <claude_4_quality_enhancements>
    <enhanced_gate_framework>
      <interleaved_thinking_integration>
        <description>Quality gates leverage Claude 4's 16K thinking capacity for sophisticated validation</description>
        <benefits>Enhanced decision-making, deeper analysis, better error prevention</benefits>
        <implementation>Gates trigger interleaved thinking for complex validation scenarios</implementation>
        <triggers>Blocking enforcement, complex criteria, error conditions, optimization opportunities</triggers>
      </interleaved_thinking_integration>
      
      <parallel_execution_optimization>
        <description>Quality validation optimized for 70% performance improvement through tool batching</description>
        <benefits>Faster validation, efficient context usage, parallel analysis capabilities</benefits>
        <implementation>Batch validation operations, parallel quality checks, concurrent analysis</implementation>
        <performance_targets>70% validation time reduction, sub-second gate evaluation, real-time feedback</performance_targets>
      </parallel_execution_optimization>
      
      <context_optimization>
        <description>200K token window optimization for comprehensive quality analysis</description>
        <benefits>Hierarchical quality assessment, efficient token usage, sustained quality validation</benefits>
        <implementation>Context-aware gate selection, hierarchical validation loading, token-efficient quality analysis</implementation>
        <monitoring>Real-time context usage tracking, quality complexity assessment, optimization triggers</monitoring>
      </context_optimization>
      
      <advanced_validation_patterns>
        <description>Claude 4 enhanced validation with predictive quality assessment</description>
        <benefits>Proactive quality issue detection, intelligent quality recommendations, adaptive standards</benefits>
        <implementation>Pattern recognition for quality issues, predictive validation, adaptive enforcement</implementation>
        <learning>Quality pattern learning, validation effectiveness tracking, continuous improvement</learning>
      </advanced_validation_patterns>
    </enhanced_gate_framework>
    
    <claude_4_enforcement_mechanisms>
      <intelligent_blocking>
        <description>Enhanced blocking with Claude 4 thinking for sophisticated failure analysis</description>
        <implementation>BLOCK triggers interleaved thinking for failure analysis and recovery planning</implementation>
        <recovery>Thinking-enhanced recovery strategy selection with multiple options</recovery>
        <escalation>Intelligent escalation based on failure pattern analysis</escalation>
      </intelligent_blocking>
      
      <adaptive_conditional>
        <description>Smart conditional enforcement with context-aware decision making</description>
        <implementation>CONDITIONAL triggers Claude 4 analysis for alternative path evaluation</implementation>
        <adaptation>Dynamic enforcement adjustment based on context and performance</adaptation>
        <optimization>Performance-aware conditional logic with efficiency considerations</optimization>
      </adaptive_conditional>
      
      <predictive_warning>
        <description>Proactive warning system with quality trend analysis</description>
        <implementation>WARN enhanced with predictive analysis and trend identification</implementation>
        <prediction>Quality issue prediction based on pattern recognition</prediction>
        <prevention>Proactive quality improvement recommendations</prevention>
      </predictive_warning>
    </claude_4_enforcement_mechanisms>
  </claude_4_quality_enhancements>
  
  <foundational_quality_gates>
    <gate name="claude_4_critical_thinking_validation" enforcement="BLOCKING">
      <description>Verify comprehensive Claude 4 enhanced critical thinking analysis completed with interleaved thinking integration</description>
      <criteria>
        <requirement>Minimum 30-second critical thinking analysis with Claude 4 interleaved thinking</requirement>
        <requirement>Enhanced 5+ critical questions (up from 3) with deeper analysis per decision</requirement>
        <requirement>Alternative approaches evaluated with consequence mapping (If X → Y → Z)</requirement>
        <requirement>Risk assessment with sophisticated threat analysis and mitigation strategies</requirement>
        <requirement>Context optimization considerations for token efficiency</requirement>
        <requirement>Parallel execution opportunities identified and evaluated</requirement>
      </criteria>
      <claude_4_enhancements>
        <interleaved_thinking>Activate 16K thinking capacity for complex validation scenarios</interleaved_thinking>
        <thinking_depth>Adaptive thinking depth based on complexity assessment</thinking_depth>
        <consequence_mapping>Three-level consequence analysis with impact assessment</consequence_mapping>
        <pattern_recognition>Leverage Claude 4 pattern recognition for quality insights</pattern_recognition>
      </claude_4_enhancements>
      <validation_method>
        <check>Critical thinking blocks demonstrate Claude 4 enhanced analysis depth</check>
        <check>Questions leverage enhanced reasoning capabilities and show sophisticated analysis</check>
        <check>Risk analysis includes predictive assessment and advanced mitigation strategies</check>
        <check>Context optimization and parallel execution opportunities properly evaluated</check>
        <check>Thinking quality meets Claude 4 enhanced standards with evidence-based reasoning</check>
      </validation_method>
      <failure_response>BLOCK with Claude 4 enhanced failure analysis until critical thinking requirements met</failure_response>
    </gate>
    
    <gate name="requirement_clarity" enforcement="BLOCKING">
      <description>Ensure requirements are clear, testable, and achievable</description>
      <criteria>
        <requirement>Requirements clearly defined with success criteria</requirement>
        <requirement>Acceptance criteria are measurable and verifiable</requirement>
        <requirement>Dependencies and constraints identified</requirement>
        <requirement>Scope appropriately bounded for command capabilities</requirement>
      </criteria>
      <validation_method>
        <check>Requirements can be objectively evaluated as complete</check>
        <check>Success criteria include specific metrics or outcomes</check>
        <check>Dependencies mapped to existing capabilities</check>
      </validation_method>
      <failure_response>BLOCK until requirements clarified and validated</failure_response>
    </gate>
    
    <gate name="module_integration_compliance" enforcement="BLOCKING">
      <description>Verify proper module usage and integration patterns</description>
      <criteria>
        <requirement>Required modules explicitly loaded and executed</requirement>
        <requirement>Module dependencies satisfied in correct order</requirement>
        <requirement>Module interfaces used correctly</requirement>
        <requirement>Module execution patterns followed</requirement>
      </criteria>
      <validation_method>
        <check>All required modules referenced in execution plan</check>
        <check>Module execution order respects dependencies</check>
        <check>Module outputs properly consumed by subsequent steps</check>
      </validation_method>
      <failure_response>BLOCK until module integration corrected</failure_response>
    </gate>
    
    <gate name="error_handling_completeness" enforcement="BLOCKING">
      <description>Ensure comprehensive error handling and recovery mechanisms</description>
      <criteria>
        <requirement>Error conditions identified and handled</requirement>
        <requirement>Recovery mechanisms defined for failure scenarios</requirement>
        <requirement>Escalation paths available for complex failures</requirement>
        <requirement>User feedback provided for error conditions</requirement>
      </criteria>
      <validation_method>
        <check>Error scenarios documented with specific recovery actions</check>
        <check>Escalation triggers clearly defined</check>
        <check>User communication plan for error conditions</check>
      </validation_method>
      <failure_response>BLOCK until error handling requirements satisfied</failure_response>
    </gate>
  </foundational_quality_gates>
  
  <development_quality_gates>
    <gate name="claude_4_enhanced_tdd_compliance" enforcement="BLOCKING">
      <description>Strict Test-Driven Development methodology enforcement with Claude 4 optimization and enhanced validation</description>
      <criteria>
        <requirement>Failing tests written BEFORE any implementation with Claude 4 test design thinking</requirement>
        <requirement>Implementation makes tests pass with minimal code optimized for parallel execution</requirement>
        <requirement>Refactoring improves design while maintaining green tests with context efficiency</requirement>
        <requirement>Test coverage meets or exceeds [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% for new code with intelligent coverage analysis</requirement>
        <requirement>Tests include unit, integration, and edge case coverage with Claude 4 enhanced test scenarios</requirement>
        <requirement>TDD cycle documented with thinking patterns and optimization opportunities</requirement>
        <requirement>Parallel test execution optimized for 70% performance improvement where applicable</requirement>
      </criteria>
      <claude_4_enhancements>
        <test_design_thinking>Leverage interleaved thinking for comprehensive test scenario design</test_design_thinking>
        <parallel_test_optimization>Optimize test execution for parallel performance improvements</parallel_test_optimization>
        <intelligent_coverage>Claude 4 enhanced coverage analysis with gap identification</intelligent_coverage>
        <adaptive_tdd>Context-aware TDD cycle adaptation based on complexity assessment</adaptive_tdd>
      </claude_4_enhancements>
      <validation_method>
        <check>Test files created before implementation files with enhanced test design</check>
        <check>Tests initially fail with expected error messages and comprehensive scenarios</check>
        <check>Implementation focused on making tests pass with parallel execution optimization</check>
        <check>Coverage reports meet minimum thresholds with intelligent gap analysis</check>
        <check>Refactoring preserves all test passing states with context optimization</check>
        <check>TDD cycle demonstrates Claude 4 enhanced methodology</check>
      </validation_method>
      <failure_response>BLOCK implementation until Claude 4 enhanced TDD compliance verified</failure_response>
    </gate>
    
    <gate name="test_coverage_tool_enforcement" enforcement="BLOCKING">
      <description>Mandatory test coverage tool usage and measurement validation</description>
      <criteria>
        <requirement>Coverage tools installed and configured (pytest-cov, nyc, c8, etc.)</requirement>
        <requirement>Coverage measurement executed and reported for all code changes</requirement>
        <requirement>Coverage threshold enforcement at [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% minimum for new code</requirement>
        <requirement>Coverage reports generated and reviewed for completeness</requirement>
        <requirement>Missing coverage identified and addressed</requirement>
        <requirement>Coverage validation integrated into quality gates</requirement>
      </criteria>
      <claude_4_enhancements>
        <intelligent_coverage_analysis>Claude 4 enhanced coverage gap identification and priority assessment</intelligent_coverage_analysis>
        <adaptive_threshold>Context-aware coverage threshold adjustment based on code complexity</adaptive_threshold>
        <predictive_coverage>Predictive analysis of coverage impact on code quality</predictive_coverage>
        <optimization_guidance>Intelligent guidance for coverage optimization strategies</optimization_guidance>
      </claude_4_enhancements>
      <validation_method>
        <check>Coverage tools properly configured and executable</check>
        <check>Coverage reports generated with detailed metrics</check>
        <check>Coverage percentage meets or exceeds [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% threshold</check>
        <check>Missing coverage lines identified and documented</check>
        <check>Coverage validation commands successfully execute</check>
      </validation_method>
      <failure_response>BLOCK until coverage tool requirements satisfied and [PROJECT_CONFIG: test_coverage.threshold | DEFAULT: 90]% threshold achieved</failure_response>
    </gate>
    
    <gate name="code_quality_standards" enforcement="BLOCKING">
      <description>Code quality, conventions, and maintainability requirements</description>
      <criteria>
        <requirement>Code follows established project conventions</requirement>
        <requirement>Functions are focused, well-named, and properly sized</requirement>
        <requirement>Complexity metrics within acceptable limits</requirement>
        <requirement>Code is readable and self-documenting</requirement>
        <requirement>Dependencies are minimized and properly managed</requirement>
      </criteria>
      <validation_method>
        <check>Linting rules pass without errors</check>
        <check>Cyclomatic complexity below threshold (typically 10)</check>
        <check>Function length appropriate (typically <50 lines)</check>
        <check>Naming conventions followed consistently</check>
      </validation_method>
      <failure_response>BLOCK until code quality standards met</failure_response>
    </gate>
    
    <gate name="security_requirements" enforcement="BLOCKING">
      <description>Security considerations and vulnerability prevention</description>
      <criteria>
        <requirement>Security threat model completed for changes</requirement>
        <requirement>Input validation and sanitization implemented</requirement>
        <requirement>Authentication and authorization properly handled</requirement>
        <requirement>Sensitive data protected and not exposed</requirement>
        <requirement>Dependencies scanned for known vulnerabilities</requirement>
      </criteria>
      <validation_method>
        <check>Threat model documents security considerations</check>
        <check>Security scanning tools report no critical issues</check>
        <check>Code review confirms security best practices</check>
        <check>Sensitive data handling follows security protocols</check>
      </validation_method>
      <failure_response>BLOCK until security requirements satisfied</failure_response>
    </gate>
    
    <gate name="performance_validation" enforcement="BLOCKING">
      <description>Performance requirements and optimization validation</description>
      <criteria>
        <requirement>Performance requirements defined and measurable</requirement>
        <requirement>Performance tests validate against requirements</requirement>
        <requirement>Resource usage within acceptable limits</requirement>
        <requirement>Scalability considerations addressed</requirement>
        <requirement>Performance regression testing in place</requirement>
      </criteria>
      <validation_method>
        <check>Performance benchmarks meet specified targets</check>
        <check>Memory usage and CPU utilization acceptable</check>
        <check>Response times within required thresholds</check>
        <check>Load testing validates scalability assumptions</check>
      </validation_method>
      <failure_response>BLOCK until performance requirements verified</failure_response>
    </gate>
    
    <gate name="claude_4_parallel_execution_optimization" enforcement="BLOCKING">
      <description>Ensure 70% performance improvement through proper parallel execution and tool batching</description>
      <criteria>
        <requirement>Independent operations identified and batched for parallel execution</requirement>
        <requirement>Tool calls (Read, Grep, analysis) properly batched where applicable</requirement>
        <requirement>Context window optimization implemented with hierarchical loading</requirement>
        <requirement>Performance improvement measured and validated against 70% target</requirement>
        <requirement>Parallel execution maintains accuracy and reliability</requirement>
      </criteria>
      <claude_4_enhancements>
        <tool_batching_analysis>Intelligent identification of batch optimization opportunities</tool_batching_analysis>
        <performance_measurement>Real-time performance tracking and optimization validation</performance_measurement>
        <context_efficiency>Token usage optimization with predictive loading</context_efficiency>
        <quality_preservation>Ensure parallel execution maintains quality standards</quality_preservation>
      </claude_4_enhancements>
      <validation_method>
        <check>Tool batching properly implemented for independent operations</check>
        <check>Performance metrics demonstrate measurable improvement</check>
        <check>Context optimization reduces token usage without quality loss</check>
        <check>Parallel execution accuracy verified against sequential results</check>
      </validation_method>
      <failure_response>BLOCK until parallel execution optimization requirements satisfied</failure_response>
    </gate>
    
    <gate name="claude_4_context_window_efficiency" enforcement="BLOCKING">
      <description>200K token window optimization with intelligent context management</description>
      <criteria>
        <requirement>Context usage monitored and optimized throughout execution</requirement>
        <requirement>Hierarchical content loading implemented for efficiency</requirement>
        <requirement>Token budget allocation optimized for sustained productivity</requirement>
        <requirement>Context efficiency improvements measurable and documented</requirement>
        <requirement>Session boundary optimization for 40-minute performance windows</requirement>
      </criteria>
      <claude_4_enhancements>
        <context_monitoring>Real-time token usage tracking with optimization triggers</context_monitoring>
        <hierarchical_loading>Priority-based content loading with lazy evaluation</hierarchical_loading>
        <budget_management>Intelligent token allocation across execution phases</budget_management>
        <session_optimization>40-minute boundary management with context preservation</session_optimization>
      </claude_4_enhancements>
      <validation_method>
        <check>Context usage stays within optimal efficiency bounds</check>
        <check>Hierarchical loading properly prioritizes critical content</check>
        <check>Token budget allocation demonstrates intelligent resource management</check>
        <check>Session boundary optimization maintains productivity</check>
      </validation_method>
      <failure_response>BLOCK until context window efficiency requirements satisfied</failure_response>
    </gate>
    
    <gate name="claude_4_thinking_pattern_integration" enforcement="BLOCKING">
      <description>Proper integration of Claude 4 thinking patterns with interleaved thinking capabilities</description>
      <criteria>
        <requirement>Thinking patterns properly structured with Claude 4 checkpoints</requirement>
        <requirement>Interleaved thinking activated for complex scenarios and BLOCKING enforcement</requirement>
        <requirement>Thinking depth adaptive based on complexity assessment</requirement>
        <requirement>Enhanced critical thinking questions demonstrate sophisticated analysis</requirement>
        <requirement>Thinking quality meets Claude 4 enhanced standards</requirement>
      </criteria>
      <claude_4_enhancements>
        <checkpoint_optimization>Advanced checkpoint design with thinking mode integration</checkpoint_optimization>
        <adaptive_thinking>Dynamic thinking depth based on complexity and risk assessment</adaptive_thinking>
        <quality_analysis>Enhanced thinking quality validation with pattern recognition</quality_analysis>
        <integration_validation>Proper thinking pattern integration across execution flow</integration_validation>
      </claude_4_enhancements>
      <validation_method>
        <check>Thinking patterns follow Claude 4 enhanced checkpoint format</check>
        <check>Interleaved thinking properly activated for appropriate scenarios</check>
        <check>Thinking depth demonstrates adaptive sophistication</check>
        <check>Critical thinking quality meets enhanced standards</check>
      </validation_method>
      <failure_response>BLOCK until thinking pattern integration requirements satisfied</failure_response>
    </gate>
  </development_quality_gates>
  
  <coordination_quality_gates>
    <gate name="multi_agent_synchronization" enforcement="BLOCKING">
      <description>Multi-agent coordination and synchronization validation</description>
      <criteria>
        <requirement>Agent responsibilities clearly defined and non-overlapping</requirement>
        <requirement>Coordination mechanisms prevent conflicts</requirement>
        <requirement>Shared interfaces properly specified and tested</requirement>
        <requirement>Integration testing validates agent coordination</requirement>
        <requirement>Error handling covers coordination failures</requirement>
      </criteria>
      <validation_method>
        <check>Agent assignment matrix shows clear boundaries</check>
        <check>Coordination protocols tested and verified</check>
        <check>Integration tests pass for all agent combinations</check>
        <check>Conflict resolution mechanisms proven effective</check>
      </validation_method>
      <failure_response>BLOCK until coordination requirements satisfied</failure_response>
    </gate>
    
    <gate name="session_tracking_completeness" enforcement="BLOCKING">
      <description>Comprehensive session and progress tracking validation</description>
      <criteria>
        <requirement>Session tracking properly initialized for complex work</requirement>
        <requirement>Progress milestones clearly defined and tracked</requirement>
        <requirement>Artifact linking maintains traceability</requirement>
        <requirement>Context preservation enables resumption</requirement>
        <requirement>Completion documentation provides closure</requirement>
      </criteria>
      <validation_method>
        <check>GitHub session created with proper template</check>
        <check>Progress updates include concrete milestones</check>
        <check>All artifacts properly linked and accessible</check>
        <check>Context sufficient for session resumption</check>
      </validation_method>
      <failure_response>BLOCK until session tracking requirements met</failure_response>
    </gate>
    
    <gate name="integration_validation" enforcement="BLOCKING">
      <description>System integration and end-to-end validation</description>
      <criteria>
        <requirement>Component integration tested and verified</requirement>
        <requirement>End-to-end workflows function correctly</requirement>
        <requirement>Data flow validated across component boundaries</requirement>
        <requirement>Error propagation handled appropriately</requirement>
        <requirement>System behavior meets overall requirements</requirement>
      </criteria>
      <validation_method>
        <check>Integration tests cover all component interfaces</check>
        <check>End-to-end test scenarios validate user workflows</check>
        <check>Data consistency maintained across integrations</check>
        <check>Error scenarios tested and handled correctly</check>
      </validation_method>
      <failure_response>BLOCK until integration validation complete</failure_response>
    </gate>
  </coordination_quality_gates>
  
  <documentation_quality_gates>
    <gate name="documentation_standards_compliance" enforcement="BLOCKING">
      <description>Documentation quality, consistency, and completeness validation</description>
      <criteria>
        <requirement>Documentation follows Framework 3.0 standards</requirement>
        <requirement>Content is accurate, current, and complete</requirement>
        <requirement>Cross-references and links are valid</requirement>
        <requirement>Documentation structure is logical and navigable</requirement>
        <requirement>Examples and code snippets are tested and working</requirement>
      </criteria>
      <validation_method>
        <check>Format validation against Framework 3.0 template</check>
        <check>Content review for accuracy and completeness</check>
        <check>Link validation ensures all references work</check>
        <check>Structure review for logical organization</check>
      </validation_method>
      <failure_response>BLOCK until documentation standards satisfied</failure_response>
    </gate>
    
    <gate name="tdd_methodology_documentation" enforcement="BLOCKING">
      <description>TDD methodology properly documented in development guides</description>
      <criteria>
        <requirement>TDD principles clearly explained and referenced</requirement>
        <requirement>Testing workflows documented with examples</requirement>
        <requirement>Quality standards linked to TDD modules</requirement>
        <requirement>Best practices and patterns included</requirement>
        <requirement>Common pitfalls and solutions documented</requirement>
      </criteria>
      <validation_method>
        <check>TDD references accurate and comprehensive</check>
        <check>Workflow documentation includes practical examples</check>
        <check>Links to TDD modules functional and current</check>
        <check>Best practices align with established patterns</check>
      </validation_method>
      <failure_response>BLOCK until TDD documentation requirements met</failure_response>
    </gate>
  </documentation_quality_gates>
  
  <analysis_quality_gates>
    <gate name="research_comprehensiveness" enforcement="CONDITIONAL">
      <description>Research and analysis depth and accuracy validation</description>
      <criteria>
        <requirement>Analysis covers all relevant aspects of the query</requirement>
        <requirement>Sources are comprehensive and current</requirement>
        <requirement>Findings are accurate and well-supported</requirement>
        <requirement>Patterns and relationships clearly identified</requirement>
        <requirement>Conclusions are logical and evidence-based</requirement>
      </criteria>
      <validation_method>
        <check>Analysis scope matches query requirements</check>
        <check>Source coverage includes all relevant files/systems</check>
        <check>Findings verified against actual code/documentation</check>
        <check>Pattern identification supported by evidence</check>
      </validation_method>
      <failure_response>WARN if analysis incomplete, recommend deeper investigation</failure_response>
    </gate>
    
    <gate name="routing_decision_quality" enforcement="BLOCKING">
      <description>Intelligent routing decisions based on sound analysis</description>
      <criteria>
        <requirement>Complexity scoring methodology correctly applied</requirement>
        <requirement>Routing decision aligns with complexity assessment</requirement>
        <requirement>Target command capabilities match requirements</requirement>
        <requirement>TDD enforcement needs properly considered</requirement>
        <requirement>Alternative routing options evaluated</requirement>
      </criteria>
      <validation_method>
        <check>Complexity score calculation verified</check>
        <check>Routing thresholds applied correctly</check>
        <check>Target command capabilities sufficient</check>
        <check>TDD requirements matched to command capabilities</check>
      </validation_method>
      <failure_response>BLOCK until routing decision justified and optimal</failure_response>
    </gate>
  </analysis_quality_gates>
  
  <quality_gate_enforcement>
    <enforcement_mechanisms>
      <blocking_enforcement>
        <description>Completely prevent progression until gate requirements satisfied</description>
        <implementation>BLOCK keyword triggers immediate halt of execution</implementation>
        <recovery>Must address gate failure before continuing</recovery>
        <escalation>Persistent failures escalate to error recovery protocols</escalation>
      </blocking_enforcement>
      
      <conditional_enforcement>
        <description>Allow alternative paths or degraded functionality</description>
        <implementation>CONDITIONAL triggers alternative workflow evaluation</implementation>
        <recovery>Alternative path available, may continue with limitations</recovery>
        <escalation>Document limitation for future improvement</escalation>
      </conditional_enforcement>
      
      <warning_enforcement>
        <description>Log concerns but allow progression</description>
        <implementation>WARN keyword logs issue without blocking</implementation>
        <recovery>Continue execution, address warning in future iteration</recovery>
        <escalation>Accumulating warnings trigger review process</escalation>
      </warning_enforcement>
    </enforcement_mechanisms>
    
    <gate_sequencing>
      <pre_execution_gates>
        <gate>critical_thinking_validation</gate>
        <gate>requirement_clarity</gate>
        <gate>module_integration_compliance</gate>
      </pre_execution_gates>
      
      <during_execution_gates>
        <gate>tdd_cycle_compliance</gate>
        <gate>code_quality_standards</gate>
        <gate>multi_agent_synchronization</gate>
        <gate>session_tracking_completeness</gate>
      </during_execution_gates>
      
      <post_execution_gates>
        <gate>security_requirements</gate>
        <gate>performance_validation</gate>
        <gate>integration_validation</gate>
        <gate>documentation_standards_compliance</gate>
      </post_execution_gates>
    </gate_sequencing>
    
    <command_specific_gate_sets>
      <task_command_gates>
        <required>foundational_gates + development_gates</required>
        <optional>documentation_gates (if docs modified)</optional>
        <enforcement_level>BLOCKING for all required gates</enforcement_level>
      </task_command_gates>
      
      <swarm_command_gates>
        <required>foundational_gates + development_gates + coordination_gates</required>
        <optional>documentation_gates (if docs involved)</optional>
        <enforcement_level>BLOCKING for all required gates</enforcement_level>
      </swarm_command_gates>
      
      <auto_command_gates>
        <required>foundational_gates + analysis_gates</required>
        <optional>development_gates (if routing to development command)</optional>
        <enforcement_level>BLOCKING for foundational, CONDITIONAL for analysis</enforcement_level>
      </auto_command_gates>
      
      <query_command_gates>
        <required>foundational_gates + analysis_gates</required>
        <optional>none</optional>
        <enforcement_level>BLOCKING for foundational, CONDITIONAL for analysis</enforcement_level>
      </query_command_gates>
      
      <session_command_gates>
        <required>foundational_gates + coordination_gates</required>
        <optional>development_gates (for development sessions)</optional>
        <enforcement_level>BLOCKING for all required gates</enforcement_level>
      </session_command_gates>
      
      <protocol_command_gates>
        <required>ALL gate categories</required>
        <optional>none (strictest enforcement)</optional>
        <enforcement_level>BLOCKING for all gates</enforcement_level>
      </protocol_command_gates>
      
      <docs_command_gates>
        <required>foundational_gates + documentation_gates</required>
        <optional>analysis_gates (if research involved)</optional>
        <enforcement_level>BLOCKING for all required gates</enforcement_level>
      </docs_command_gates>
    </command_specific_gate_sets>
  </quality_gate_enforcement>
  
  <integration_template>
    <universal_quality_gates_block>
      <structure>
        &lt;universal_quality_gates enforcement="MANDATORY"&gt;
          &lt;gate_set&gt;[command_specific_gate_set]&lt;/gate_set&gt;
          &lt;validation&gt;Reference quality/universal-quality-gates.md#[command]_gates&lt;/validation&gt;
          &lt;blocking_conditions&gt;
            &lt;condition&gt;[gate_1] requirements not satisfied&lt;/condition&gt;
            &lt;condition&gt;[gate_2] validation fails&lt;/condition&gt;
            &lt;condition&gt;[gate_n] enforcement triggered&lt;/condition&gt;
          &lt;/blocking_conditions&gt;
          &lt;enforcement_sequence&gt;
            &lt;pre_execution&gt;[foundational_gates]&lt;/pre_execution&gt;
            &lt;during_execution&gt;[development/coordination_gates]&lt;/during_execution&gt;
            &lt;post_execution&gt;[validation/documentation_gates]&lt;/post_execution&gt;
          &lt;/enforcement_sequence&gt;
        &lt;/universal_quality_gates&gt;
      </structure>
      
      <implementation_guidelines>
        <gate_selection>Select appropriate gate set based on command type and requirements</gate_selection>
        <customization>Add command-specific gates as needed for unique requirements</customization>
        <enforcement_tuning>Adjust enforcement levels based on command risk profile</enforcement_tuning>
        <integration_order>Place quality gates block after TDD integration, before examples</integration_order>
      </implementation_guidelines>
    </universal_quality_gates_block>
  </integration_template>
  
  <metrics_and_monitoring>
    <gate_effectiveness_metrics>
      <metric name="gate_pass_rate">Percentage of executions passing each gate</metric>
      <metric name="gate_failure_frequency">Most common gate failures by command</metric>
      <metric name="resolution_time">Average time to resolve gate failures</metric>
      <metric name="quality_improvement">Quality trends over time with gate enforcement</metric>
    </gate_effectiveness_metrics>
    
    <continuous_improvement>
      <feedback_collection>Gather data on gate effectiveness and user experience</feedback_collection>
      <threshold_tuning>Adjust gate criteria based on effectiveness data</threshold_tuning>
      <gate_evolution>Add new gates based on emerging quality requirements</gate_evolution>
      <automation_enhancement">Improve automated validation mechanisms</automation_enhancement>
    </continuous_improvement>
  </metrics_and_monitoring>
  
  <integration_points>
    <depends_on>
      quality/tdd.md for TDD-specific quality requirements
      quality/production-standards.md for production-level quality standards
      quality/critical-thinking.md for critical thinking validation standards
      security/threat-modeling.md for security gate requirements
    </depends_on>
    <provides_to>
      All commands for standardized quality gate enforcement
      quality/framework-metrics.md for quality measurement and tracking
      patterns/pattern-library.md for quality gate implementation patterns
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">quality_gates</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">enforcement_mechanisms</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">checkpoint_validation</uses_pattern>
    <implementation_notes>
      Quality gates implement quality_gates pattern for consistent enforcement
      Enforcement mechanisms use enforcement_mechanisms pattern for predictable behavior
      Gate validation follows checkpoint_validation pattern for reliable assessment
      Universal application ensures consistent quality standards across all commands
    </implementation_notes>
  </pattern_usage>
  
</module>
</module>
</development_quality_gates>
</gate>
</validation_method>
</check>
</50>
</metrics_and_monitoring>
</continuous_improvement>
</automation_enhancement">
```