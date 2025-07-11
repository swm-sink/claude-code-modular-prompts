| version | last_updated | status |
|---------|--------------|--------|
| 2.0.0   | 2025-07-08   | stable |

# Universal Thinking Pattern Template - Claude 4 Enhanced

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="thinking_pattern_template" category="patterns">
  
  <purpose>
    Provide standardized checkpoint-based thinking patterns optimized for Claude 4's advanced capabilities including interleaved thinking, extended reasoning, and parallel execution with deterministic execution, verifiable validation, and consistent enforcement across all commands.
  </purpose>
  
  <claude_4_enhanced_checkpoint_format>
    <checkpoint id="[number]" verify="[true/false]" enforcement="[BLOCKING/CONDITIONAL/OPTIONAL]" thinking_mode="[interleaved/extended/standard]">
      <action>[Specific action to be taken in this step]</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What exactly needs to be considered before acting?
          - What context and constraints apply to this checkpoint?
          - How does this connect to previous and future checkpoints?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Primary Question: What exactly needs to be accomplished?]
          - [Risk Question: What could go wrong or be missed?]
          - [Alternative Question: What alternatives should be evaluated?]
          - [Quality Question: How does this align with TDD/quality requirements?]
          - [Consequence Question: If this fails, what are the downstream impacts?]
        </critical_thinking>
        <decision_reasoning>
          - Why is the chosen approach optimal for this context?
          - What evidence supports this decision?
          - How will success be measured and validated?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can any tool calls be batched for 70% performance improvement?</tool_optimization>
        <context_efficiency>How can this checkpoint optimize token usage?</context_efficiency>
        <dependency_analysis>What must be sequential vs what can be parallel?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>[Specific format for documenting checkpoint completion with evidence]</output_format>
      <validation>[Criteria that must be met to pass this checkpoint with measurable thresholds]</validation>
      <enforcement>[Action taken if checkpoint fails - BLOCK/VERIFY/ESCALATE with recovery path]</enforcement>
      <context_transfer>[Information passed to next checkpoint for continuity]</context_transfer>
    </checkpoint>
  </claude_4_enhanced_checkpoint_format>
  
  <checkpoint_types>
    <analysis_checkpoint>
      <purpose>Initial understanding and requirement validation</purpose>
      <critical_thinking_focus>
        - What exactly is being requested?
        - Are requirements clear and testable?
        - What are the constraints and dependencies?
        - How does this align with existing architecture?
      </critical_thinking_focus>
      <common_validations>Requirements clarity, testability, feasibility assessment</common_validations>
      <enforcement_patterns>BLOCK if requirements unclear or infeasible</enforcement_patterns>
    </analysis_checkpoint>
    
    <tdd_checkpoint>
      <purpose>Test-driven development validation and enforcement</purpose>
      <critical_thinking_focus>
        - Are tests written BEFORE implementation?
        - Do tests cover all acceptance criteria and edge cases?
        - Is the RED-GREEN-REFACTOR cycle being followed?
        - Will TDD methodology ensure quality outcomes?
      </critical_thinking_focus>
      <common_validations>Failing tests exist, comprehensive coverage, TDD compliance</common_validations>
      <enforcement_patterns>BLOCK implementation until proper tests exist</enforcement_patterns>
    </tdd_checkpoint>
    
    <implementation_checkpoint>
      <purpose>Code development with quality and performance considerations</purpose>
      <critical_thinking_focus>
        - Is implementation minimal and focused on making tests pass?
        - Are performance and security considerations addressed?
        - Does code follow established patterns and conventions?
        - Will implementation meet production standards?
      </critical_thinking_focus>
      <common_validations>Code quality, test passage, convention adherence</common_validations>
      <enforcement_patterns>VERIFY quality standards before proceeding</enforcement_patterns>
    </implementation_checkpoint>
    
    <validation_checkpoint>
      <purpose>Quality gates and comprehensive verification</purpose>
      <critical_thinking_focus>
        - Do all quality gates pass (coverage, security, performance)?
        - Is documentation complete and accurate?
        - Are integration points properly tested?
        - Is the solution ready for production deployment?
      </critical_thinking_focus>
      <common_validations>Quality gates, documentation, integration testing</common_validations>
      <enforcement_patterns>BLOCK completion until all quality standards met</enforcement_patterns>
    </validation_checkpoint>
    
    <coordination_checkpoint>
      <purpose>Multi-agent or cross-component coordination</purpose>
      <critical_thinking_focus>
        - How do components/agents coordinate effectively?
        - Are interfaces and contracts clearly defined?
        - Will coordination mechanisms scale appropriately?
        - Are there potential coordination failures to prevent?
      </critical_thinking_focus>
      <common_validations>Interface clarity, coordination protocols, scalability</common_validations>
      <enforcement_patterns>VERIFY coordination mechanisms before proceeding</enforcement_patterns>
    </coordination_checkpoint>
  </checkpoint_types>
  
  <claude_4_enhanced_checkpoint_types>
    <research_first_checkpoint>
      <purpose>Claude Code research-first methodology with structured analysis</purpose>
      <critical_thinking_focus>
        - What research is needed before implementation decisions?
        - How can parallel analysis improve understanding efficiency?
        - What patterns exist in the codebase that inform this approach?
        - Will research prevent costly iterations and rework?
      </critical_thinking_focus>
      <parallel_execution>Concurrent file analysis, pattern search, documentation review</parallel_execution>
      <common_validations>Comprehensive research completed, patterns identified, approach validated</common_validations>
      <enforcement_patterns>BLOCK implementation until research validates approach</enforcement_patterns>
      <thinking_mode>interleaved</thinking_mode>
    </research_first_checkpoint>
    
    <parallel_optimization_checkpoint>
      <purpose>Optimize for 70% performance improvement through tool batching</purpose>
      <critical_thinking_focus>
        - Which operations can execute in parallel without dependencies?
        - How can tool calls be batched for maximum efficiency?
        - What context window optimization opportunities exist?
        - Will parallel execution maintain accuracy and reliability?
      </critical_thinking_focus>
      <parallel_execution>Mandatory batching of independent Read(), analysis, validation operations</parallel_execution>
      <common_validations>Tool batching plan created, dependencies mapped, efficiency verified</common_validations>
      <enforcement_patterns>VERIFY parallel execution opportunities before sequential fallback</enforcement_patterns>
      <thinking_mode>standard</thinking_mode>
    </parallel_optimization_checkpoint>
    
    <context_optimization_checkpoint>
      <purpose>200K token window optimization with memory management</purpose>
      <critical_thinking_focus>
        - How can context be hierarchically prioritized for efficiency?
        - What information can be loaded conditionally vs upfront?
        - Are we approaching session token limits requiring optimization?
        - Will context organization support sustained productivity?
      </critical_thinking_focus>
      <parallel_execution>Concurrent context analysis, token counting, optimization planning</parallel_execution>
      <common_validations>Context budget managed, hierarchical loading implemented, efficiency improved</common_validations>
      <enforcement_patterns>CONDITIONAL optimization based on context usage patterns</enforcement_patterns>
      <thinking_mode>standard</thinking_mode>
    </context_optimization_checkpoint>
    
    <framework_integration_checkpoint>
      <purpose>Advanced prompting framework integration (RISE, TRACE, CARE)</purpose>
      <critical_thinking_focus>
        - Which 2025 framework best fits this task complexity?
        - How can framework elements be integrated with existing patterns?
        - Will framework application improve accuracy and consistency?
        - Can frameworks be chained or hybridized for better results?
      </critical_thinking_focus>
      <parallel_execution>Framework analysis, pattern matching, integration planning</parallel_execution>
      <common_validations>Framework selected, integration planned, effectiveness assessed</common_validations>
      <enforcement_patterns>CONDITIONAL framework application based on complexity assessment</enforcement_patterns>
      <thinking_mode>extended</thinking_mode>
    </framework_integration_checkpoint>
    
    <security_optimization_checkpoint>
      <purpose>Advanced security patterns with automated validation</purpose>
      <critical_thinking_focus>
        - What security implications require Claude 4 threat analysis?
        - How can security validation be automated and integrated?
        - Are there data protection concerns requiring special handling?
        - Will security measures maintain development velocity?
      </critical_thinking_focus>
      <parallel_execution>Threat analysis, pattern validation, compliance checking</parallel_execution>
      <common_validations>Security analysis complete, threats mitigated, compliance verified</common_validations>
      <enforcement_patterns>BLOCK on critical security issues, VERIFY on medium risks</enforcement_patterns>
      <thinking_mode>interleaved</thinking_mode>
    </security_optimization_checkpoint>
  </claude_4_enhanced_checkpoint_types>
  
  <enforcement_levels>
    <blocking_enforcement>
      <description>Checkpoint failure completely stops execution</description>
      <usage>Critical quality gates, safety requirements, compliance validations</usage>
      <keywords>BLOCK, CRITICAL, STOP, PREVENT</keywords>
      <recovery>Must resolve issue before continuing to next checkpoint</recovery>
    </blocking_enforcement>
    
    <conditional_enforcement>
      <description>Checkpoint failure triggers alternative workflows</description>
      <usage>Error recovery, escalation scenarios, optional optimizations</usage>
      <keywords>CONDITIONAL, IF, ESCALATE, ALTERNATIVE</keywords>
      <recovery>Alternative path available, may continue with degraded functionality</recovery>
    </conditional_enforcement>
    
    <optional_enforcement>
      <description>Checkpoint failure logged but does not stop execution</description>
      <usage>Performance optimizations, nice-to-have features, logging</usage>
      <keywords>OPTIONAL, LOG, WARN, RECOMMEND</keywords>
      <recovery>Continue execution, failure noted for future improvement</recovery>
    </optional_enforcement>
  </enforcement_levels>
  
  <claude_4_thinking_guidelines>
    <interleaved_thinking_integration>
      <purpose>Leverage Claude 4's 16K token thinking capacity for sophisticated reasoning</purpose>
      <structure>
        <pre_analysis>Context gathering and initial assessment (2-3K tokens)</pre_analysis>
        <critical_thinking>Deep analysis with minimum 30-second reflection (8-10K tokens)</critical_thinking>
        <decision_reasoning>Solution selection and justification (3-4K tokens)</decision_reasoning>
        <validation_planning>Success criteria and measurement approach (1-2K tokens)</validation_planning>
      </structure>
      <trigger_conditions>
        <complexity>Activate for tasks requiring >3 logical steps</complexity>
        <uncertainty>Automatic activation when multiple viable options exist</uncertainty>
        <explicit_request>"ultrathink" or "think harder" triggers maximum analysis</explicit_request>
        <quality_gates>Mandatory for BLOCKING enforcement checkpoints</quality_gates>
      </trigger_conditions>
    </interleaved_thinking_integration>
    
    <enhanced_question_structure>
      <primary_question>What exactly needs to be accomplished in this step?</primary_question>
      <context_question>What context and constraints shape this decision?</context_question>
      <risk_question>What could go wrong or be missed, and how likely?</risk_question>
      <alternative_question>What alternatives exist and how do they compare?</alternative_question>
      <quality_question>How does this maintain/improve overall quality?</quality_question>
      <consequence_question>What are the downstream impacts if this fails?</consequence_question>
      <evidence_question>What evidence supports the chosen approach?</evidence_question>
      <measurement_question>How will success be measured and validated?</measurement_question>
    </enhanced_question_structure>
    
    <thinking_depth_requirements>
      <minimum>At least 5 critical thinking questions per checkpoint (enhanced from 3)</minimum>
      <complexity_scaling>Add 2 questions per complexity level for deeper analysis</complexity_scaling>
      <domain_specific>Include domain-specific considerations (security, performance, compliance, cost)</domain_specific>
      <consequence_mapping>Map potential outcomes through 3-level consequence chains (If X → Y → Z)</consequence_mapping>
      <evidence_validation>Cross-reference decisions with available evidence and patterns</evidence_validation>
    </thinking_depth_requirements>
    
    <advanced_quality_considerations>
      <tdd_integration>Every checkpoint should consider TDD implications and test-first approaches</tdd_integration>
      <security_awareness>Security implications evaluated at each step with threat modeling</security_awareness>
      <performance_impact>Performance considerations with specific metrics (200ms p95 target)</performance_impact>
      <maintainability>Long-term maintenance implications with technical debt assessment</maintainability>
      <cost_optimization>Token efficiency and session management optimization</cost_optimization>
      <parallel_execution>Opportunities for 70% performance improvement through tool batching</parallel_execution>
    </advanced_quality_considerations>
    
    <extended_reasoning_triggers>
      <standard_reasoning>Normal checkpoint processing with basic critical thinking</standard_reasoning>
      <enhanced_reasoning>"think more", "think harder", "think longer" for deeper analysis</enhanced_reasoning>
      <maximum_reasoning>"ultrathink" activates deepest analytical capabilities with full token usage</maximum_reasoning>
      <adaptive_reasoning>Automatically scale thinking depth based on checkpoint complexity and risk</adaptive_reasoning>
    </extended_reasoning_triggers>
  </claude_4_thinking_guidelines>
  
  <output_format_standards>
    <consistency_requirements>
      <format>All outputs follow [CATEGORY]: [DETAILS] format</format>
      <specificity>Outputs include specific file names, metrics, or identifiers</specificity>
      <verifiability>Outputs provide concrete evidence of checkpoint completion</verifiability>
      <traceability>Outputs enable tracking of decision history</traceability>
    </consistency_requirements>
    
    <common_output_patterns>
      <analysis_outputs>ANALYSIS: [findings] affecting [components] requiring [approach]</analysis_outputs>
      <tdd_outputs>TDD_STATUS: [phase] with [test_count] tests covering [requirements]</tdd_outputs>
      <implementation_outputs>IMPLEMENTATION: [code_changes] meeting [standards] with [quality_metrics]</implementation_outputs>
      <validation_outputs>VALIDATION: [gates_passed] with [evidence] confirming [compliance]</validation_outputs>
    </common_output_patterns>
  </output_format_standards>
  
  <validation_criteria_patterns>
    <objective_criteria>
      <measurable>Criteria must be objectively measurable (coverage %, response time, etc.)</measurable>
      <binary>Criteria should have clear pass/fail conditions</binary>
      <specific>Criteria include specific thresholds and requirements</specific>
      <time_bound>Criteria include time-based requirements where applicable</time_bound>
    </objective_criteria>
    
    <quality_criteria>
      <tdd_compliance>Tests written first, comprehensive coverage, proper cycles</tdd_compliance>
      <code_quality>Convention adherence, maintainability, readability standards</code_quality>
      <security_standards>Threat modeling complete, vulnerabilities addressed</security_standards>
      <performance_targets>Response times, resource usage, scalability requirements</performance_targets>
    </quality_criteria>
  </validation_criteria_patterns>
  
  <claude_4_command_adaptations>
    <task_command>
      <focus>Single-component TDD enforcement with Claude 4 optimization</focus>
      <checkpoints>Research-First Analysis → Parallel Tool Optimization → TDD RED → TDD GREEN → TDD REFACTOR → Context-Optimized Quality Gates</checkpoints>
      <thinking_modes>interleaved for analysis, extended for complex implementations, standard for TDD cycles</thinking_modes>
      <parallel_execution>Batch file reads, concurrent analysis, parallel testing</parallel_execution>
      <enforcement>BLOCKING on TDD violations, quality gate failures, parallel execution bypasses</enforcement>
      <context_optimization>Token budget management, hierarchical context loading</context_optimization>
    </task_command>
    
    <swarm_command>
      <focus>Multi-agent coordination with Claude 4 advanced orchestration</focus>
      <checkpoints>Session Creation → Research-Based Agent Assignment → Parallel Worktree Setup → Framework-Integrated Coordination → TDD Synchronization → Optimized Integration → Merge</checkpoints>
      <thinking_modes>interleaved for coordination, extended for complex integrations, standard for execution</thinking_modes>
      <parallel_execution>Concurrent agent initialization, parallel worktree creation, simultaneous TDD validation</parallel_execution>
      <enforcement>BLOCKING on coordination failures, TDD violations, context window exhaustion</enforcement>
      <framework_integration>RISE framework for coordination, TRACE for execution planning</framework_integration>
    </swarm_command>
    
    <auto_command>
      <focus>Intelligent routing with 2025 framework integration and TDD-aware complexity scoring</focus>
      <checkpoints>Enhanced Request Analysis → Framework Selection → Parallel Complexity Scoring → Research-First Validation → TDD-Aware Routing → Optimized Execution</checkpoints>
      <thinking_modes>extended for complexity analysis, interleaved for routing decisions, standard for execution</thinking_modes>
      <parallel_execution>Concurrent complexity analysis, parallel framework evaluation, batch routing validation</parallel_execution>
      <enforcement>BLOCKING on unclear requirements, routing to non-TDD commands for code changes, framework misalignment</enforcement>
      <framework_integration>Automatic framework selection based on complexity assessment</framework_integration>
    </auto_command>
    
    <query_command>
      <focus>Research and analysis with Claude 4 enhanced reasoning and parallel search</focus>
      <checkpoints>Query Analysis → Framework-Enhanced Parallel Search → Interleaved Analysis → Advanced Pattern Recognition → Context-Optimized Report Generation</checkpoints>
      <thinking_modes>extended for deep analysis, interleaved for complex reasoning, standard for reporting</thinking_modes>
      <parallel_execution>Concurrent file searches, parallel pattern analysis, batch content processing</parallel_execution>
      <enforcement>BLOCKING on modification attempts, incomplete analysis, context inefficiency</enforcement>
      <framework_integration>LEAP framework for research, CLEAR for comprehensive analysis</framework_integration>
    </query_command>
    
    <session_command>
      <focus>Session management with Claude 4 context optimization and TDD progress tracking</focus>
      <checkpoints>Session Type Analysis → Context-Optimized GitHub Issue → Parallel Progress Tracking → Efficient Artifact Linking → TDD Documentation → Session Boundary Optimization</checkpoints>
      <thinking_modes>standard for setup, interleaved for complex session management, extended for optimization</thinking_modes>
      <parallel_execution>Concurrent artifact processing, parallel progress updates, batch validation</parallel_execution>
      <enforcement>BLOCKING on incomplete TDD tracking, missing artifact links, context window violations</enforcement>
      <context_optimization>40-minute session boundary management, token efficiency tracking</context_optimization>
    </session_command>
    
    <protocol_command>
      <focus>Production standards with Claude 4 advanced security and strictest TDD enforcement</focus>
      <checkpoints>Compliance Session → Enhanced Requirements → Framework-Integrated Strict TDD → Advanced Security → Parallel Performance → Context-Optimized Quality Gates → Comprehensive Documentation</checkpoints>
      <thinking_modes>interleaved for all checkpoints, extended for security analysis, maximum for compliance validation</thinking_modes>
      <parallel_execution>Concurrent compliance checking, parallel security analysis, batch quality validation</parallel_execution>
      <enforcement>BLOCKING on any quality gate failure, compliance violations, security issues, context inefficiency</enforcement>
      <framework_integration>CRISP framework for detailed execution, CARE for evaluation</framework_integration>
    </protocol_command>
    
    <docs_command>
      <focus>Documentation with Claude 4 optimization and TDD methodology integration</focus>
      <checkpoints>Gateway Enforcement → Enhanced Request Parsing → Parallel Search/Generate → Framework-Integrated Standards → Context-Optimized Validation</checkpoints>
      <thinking_modes>standard for gateway, extended for complex documentation, interleaved for validation</thinking_modes>
      <parallel_execution>Concurrent search operations, parallel content generation, batch validation</parallel_execution>
      <enforcement>BLOCKING on documentation creation outside gateway, missing TDD references, context violations</enforcement>
      <framework_integration>TRACE framework for structured documentation, FOCUS for user-centered design</framework_integration>
    </docs_command>
  </claude_4_command_adaptations>
  
  <claude_4_template_usage_guidelines>
    <implementation_requirements>
      <mandatory_elements>All checkpoints must include action, interleaved_thinking, parallel_execution_considerations, output_format, validation, enforcement, context_transfer</mandatory_elements>
      <ordering>Checkpoints must be sequentially numbered and logically ordered with clear dependency chains</ordering>
      <enforcement_consistency>Enforcement levels must be consistent with checkpoint criticality and risk assessment</enforcement_consistency>
      <tdd_integration>TDD considerations must be integrated throughout thinking patterns with blocking enforcement</tdd_integration>
      <thinking_mode>Each checkpoint must specify appropriate thinking mode (interleaved/extended/standard)</thinking_mode>
    </implementation_requirements>
    
    <claude_4_optimization_requirements>
      <parallel_execution>All checkpoints must evaluate opportunities for tool batching and parallel operations</parallel_execution>
      <context_efficiency>Token usage optimization must be considered at each checkpoint</context_efficiency>
      <thinking_integration>Interleaved thinking must be used for BLOCKING and complex checkpoints</thinking_integration>
      <evidence_validation>All decisions must be supported by concrete evidence and reasoning</evidence_validation>
      <session_optimization>Checkpoint execution must optimize for 40-minute session boundaries</session_optimization>
    </claude_4_optimization_requirements>
    
    <advanced_customization_points>
      <domain_specific>Add domain-specific checkpoints with Claude 4 thinking integration</domain_specific>
      <complexity_scaling>Scale thinking depth and checkpoint count based on task complexity</complexity_scaling>
      <enforcement_tuning>Adjust enforcement levels with automatic escalation based on risk profile</enforcement_tuning>
      <validation_criteria>Customize validation with measurable, objective criteria and evidence requirements</validation_criteria>
      <performance_optimization>Integrate 70% improvement patterns through parallel execution design</performance_optimization>
      <framework_integration>Leverage 2025 prompting frameworks (RISE, TRACE, CARE) for complex checkpoints</framework_integration>
    </advanced_customization_points>
    
    <enhanced_quality_assurance>
      <completeness_check>All checkpoints address critical aspects with Claude 4 optimization considerations</completeness_check>
      <consistency_validation>Thinking patterns consistent across commands with framework-wide optimization</consistency_validation>
      <effectiveness_testing>Patterns tested for deterministic Claude 4 interpretation with performance benchmarks</effectiveness_testing>
      <continuous_improvement>Patterns updated based on Claude 4 capabilities, usage feedback, and performance metrics</continuous_improvement>
      <claude_4_compatibility>Regular validation against latest Claude 4 features and capabilities</claude_4_compatibility>
      <performance_monitoring>Track checkpoint execution time, thinking quality, and decision accuracy</performance_monitoring>
    </enhanced_quality_assurance>
  </claude_4_template_usage_guidelines>
  
  <integration_points>
    <depends_on>
      quality/tdd.md for TDD methodology integration
      quality/critical-thinking.md for thinking process standards
      quality/production-standards.md for quality gate requirements
    </depends_on>
    <provides_to>
      All commands for standardized thinking pattern implementation
      quality/framework-metrics.md for pattern effectiveness measurement
      patterns/pattern-library.md for reusable thinking pattern components
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">standardized_interfaces</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">checkpoint_validation</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">enforcement_mechanisms</uses_pattern>
    <implementation_notes>
      Thinking patterns follow standardized_interfaces for consistency across commands
      Checkpoint validation implements checkpoint_validation pattern for reliable execution
      Enforcement mechanisms use enforcement_mechanisms pattern for predictable behavior
      Template provides foundation for deterministic Claude 4 interpretation
    </implementation_notes>
  </pattern_usage>
  
</module>
```