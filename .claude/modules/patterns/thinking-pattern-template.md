| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Universal Thinking Pattern Template

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="thinking_pattern_template" category="patterns">
  
  <purpose>
    Provide standardized checkpoint-based thinking patterns for Claude 4 with deterministic execution, verifiable validation, and consistent enforcement across all commands.
  </purpose>
  
  <standardized_checkpoint_format>
    <checkpoint id="[number]" verify="[true/false]" enforcement="[BLOCKING/CONDITIONAL/OPTIONAL]">
      <action>[Specific action to be taken in this step]</action>
      <critical_thinking>
        - [Question 1: What exactly needs to be considered?]
        - [Question 2: What could go wrong or be missed?]
        - [Question 3: What alternatives should be evaluated?]
        - [Question 4: How does this align with TDD/quality requirements?]
      </critical_thinking>
      <output_format>[Specific format for documenting checkpoint completion]</output_format>
      <validation>[Criteria that must be met to pass this checkpoint]</validation>
      <enforcement>[Action taken if checkpoint fails - BLOCK/VERIFY/ESCALATE]</enforcement>
    </checkpoint>
  </standardized_checkpoint_format>
  
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
  
  <critical_thinking_guidelines>
    <question_structure>
      <primary_question>What exactly needs to be accomplished in this step?</primary_question>
      <risk_question>What could go wrong or be missed?</risk_question>
      <alternative_question>What alternatives should be considered?</alternative_question>
      <quality_question>How does this maintain/improve overall quality?</quality_question>
    </question_structure>
    
    <thinking_depth_requirements>
      <minimum>At least 3 critical thinking questions per checkpoint</minimum>
      <complexity_scaling>Add 1 question per level of complexity (simple/medium/complex/enterprise)</complexity_scaling>
      <domain_specific>Include domain-specific considerations (security, performance, compliance)</domain_specific>
      <consequence_mapping>Map potential outcomes and their impacts</consequence_mapping>
    </thinking_depth_requirements>
    
    <quality_considerations>
      <tdd_integration>Every checkpoint should consider TDD implications</tdd_integration>
      <security_awareness>Security implications evaluated at each step</security_awareness>
      <performance_impact>Performance considerations included in thinking</performance_impact>
      <maintainability>Long-term maintenance implications considered</maintainability>
    </quality_considerations>
  </critical_thinking_guidelines>
  
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
  
  <command_specific_adaptations>
    <task_command>
      <focus>Single-component TDD enforcement with production quality</focus>
      <checkpoints>Analysis → TDD RED → TDD GREEN → TDD REFACTOR → Quality Gates</checkpoints>
      <enforcement>BLOCKING on TDD violations, quality gate failures</enforcement>
    </task_command>
    
    <swarm_command>
      <focus>Multi-agent coordination with TDD synchronization</focus>
      <checkpoints>Session → Agent Assignment → Worktrees → TDD Coordination → Integration → Merge</checkpoints>
      <enforcement>BLOCKING on coordination failures, TDD violations</enforcement>
    </swarm_command>
    
    <auto_command>
      <focus>Intelligent routing with TDD-aware complexity scoring</focus>
      <checkpoints>Request Analysis → Complexity Scoring → Research → TDD-Aware Routing → Execution</checkpoints>
      <enforcement>BLOCKING on unclear requirements, routing to non-TDD commands for code changes</enforcement>
    </auto_command>
    
    <query_command>
      <focus>Research and analysis with TDD pattern recognition</focus>
      <checkpoints>Query Analysis → Parallel Search → Analysis → Pattern Recognition → Report Generation</checkpoints>
      <enforcement>BLOCKING on modification attempts, incomplete analysis</enforcement>
    </query_command>
    
    <session_command>
      <focus>Session management with TDD progress tracking</focus>
      <checkpoints>Session Type → GitHub Issue → Progress Tracking → Artifact Linking → TDD Documentation</checkpoints>
      <enforcement>BLOCKING on incomplete TDD tracking, missing artifact links</enforcement>
    </session_command>
    
    <protocol_command>
      <focus>Production standards with strictest TDD enforcement</focus>
      <checkpoints>Compliance Session → Requirements → Strict TDD → Security → Performance → Quality Gates → Documentation</checkpoints>
      <enforcement>BLOCKING on any quality gate failure, compliance violations</enforcement>
    </protocol_command>
    
    <docs_command>
      <focus>Documentation with TDD methodology integration</focus>
      <checkpoints>Gateway Enforcement → Request Parsing → Search/Generate → Standards Application → Validation</checkpoints>
      <enforcement>BLOCKING on documentation creation outside gateway, missing TDD references</enforcement>
    </docs_command>
  </command_specific_adaptations>
  
  <template_usage_guidelines>
    <implementation_requirements>
      <mandatory_elements>All checkpoints must include action, critical_thinking, output_format, validation, enforcement</mandatory_elements>
      <ordering>Checkpoints must be sequentially numbered and logically ordered</ordering>
      <enforcement_consistency>Enforcement levels must be consistent with checkpoint criticality</enforcement_consistency>
      <tdd_integration>TDD considerations must be integrated throughout thinking patterns</tdd_integration>
    </implementation_requirements>
    
    <customization_points>
      <domain_specific>Add domain-specific checkpoints for specialized commands</domain_specific>
      <complexity_scaling>Scale number of checkpoints based on command complexity</complexity_scaling>
      <enforcement_tuning>Adjust enforcement levels based on command risk profile</enforcement_tuning>
      <validation_criteria>Customize validation criteria for command-specific requirements</validation_criteria>
    </customization_points>
    
    <quality_assurance>
      <completeness_check>All checkpoints address critical aspects of command execution</completeness_check>
      <consistency_validation>Thinking patterns consistent across similar commands</consistency_validation>
      <effectiveness_testing>Patterns tested for deterministic Claude 4 interpretation</effectiveness_testing>
      <continuous_improvement>Patterns updated based on usage feedback and effectiveness</continuous_improvement>
    </quality_assurance>
  </template_usage_guidelines>
  
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