| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-08   | stable |

# /swarm - Multi-agent coordination with TRACE framework and advanced TDD orchestration

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Multi-agent coordination with TRACE framework for complex system development and TDD orchestration">
  
  <delegation target="modules/patterns/multi-agent.md">
    TRACE framework → Create session → Setup worktrees → Decompose work → Execute Task() calls → Merge results → Quality validation
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/critical-thinking-pattern.md">TRACE framework coordination decisions</uses_pattern>
    <uses_pattern from="patterns/session-management-pattern.md">Multi-agent session coordination</uses_pattern>
    <uses_pattern from="patterns/integration-pattern.md">Agent coordination and merging</uses_pattern>
    <uses_pattern from="patterns/tdd-cycle-pattern.md">Distributed TDD enforcement</uses_pattern>
    <uses_pattern from="patterns/quality-validation-pattern.md">Multi-agent quality assurance</uses_pattern>
    <uses_pattern from="patterns/error-recovery-pattern.md">Coordination failure handling</uses_pattern>
    <uses_pattern from="patterns/performance-optimization-pattern.md">Parallel execution coordination</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply TRACE framework - Define Task complexity and coordination requirements</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What task complexity analysis is needed for optimal multi-agent coordination?
          - What context and constraints apply to TRACE framework application?
          - How does task decomposition connect to agent specialization and coordination efficiency?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Complexity Question: What are the precise task boundaries and complexity levels for multi-agent coordination?]
          - [Agent Question: How many agents will be needed and what are their specialized responsibilities?]
          - [Integration Question: What are the integration points and dependencies between agents?]
          - [Framework Question: How does task decomposition align with TRACE framework precision?]
          - [Coordination Question: What coordination overhead should be expected for this complexity level?]
          - [Optimization Question: Can agent coordination be optimized for parallel execution efficiency?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this task decomposition optimal for TRACE framework application?
          - What evidence supports the agent count and specialization strategy?
          - How will this coordination approach maximize multi-agent effectiveness?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can task analysis be combined with initial agent specification for 70% improvement?</tool_optimization>
        <context_efficiency>How can TRACE framework application optimize context window usage?</context_efficiency>
        <dependency_analysis>What task analysis can be done in parallel vs sequential for coordination setup?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_TASK_DEFINITION: [complexity_level] requiring [agent_count] agents with [integration_complexity] coordination</output_format>
      <validation>Task complexity and agent requirements clearly defined with enhanced reasoning</validation>
      <enforcement>BLOCK if task analysis insufficient for multi-agent coordination planning</enforcement>
      <context_transfer>Task complexity and agent requirements for TRACE request specification</context_transfer>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply TRACE framework - Specify precise Requests and agent assignments</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What request specification approach will optimize agent coordination?
          - What technical precision is needed for TRACE framework success?
          - How does request specification connect to agent specialization and TDD integration?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Specification Question: What are the exact technical specifications each agent must deliver?]
          - [Interface Question: How do agent deliverables interface with each other?]
          - [Quality Question: What are the precise quality requirements and acceptance criteria?]
          - [Coordination Question: How will agents coordinate shared contracts and dependencies?]
          - [TDD Question: What TDD requirements apply to each agent specialization?]
          - [Precision Question: Does specification detail meet TRACE framework standards?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this request specification optimal for TRACE framework coordination?
          - What evidence supports the agent assignment strategy?
          - How will this specification ensure multi-agent coordination success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can agent specification be combined with technical analysis for efficiency?</tool_optimization>
        <context_efficiency>How can request specification optimize context window usage?</context_efficiency>
        <dependency_analysis>What specification tasks can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_REQUEST_SPECIFICATION:
        - [Agent1]: [precise_technical_requirements] + TDD obligations
        - [Agent2]: [precise_technical_requirements] + TDD obligations
        - [Agent3]: [precise_technical_requirements] + TDD obligations</output_format>
      <validation>Agent requests specified with precision and clear TDD integration with enhanced reasoning</validation>
      <enforcement>BLOCK if any agent request lacks precision or TDD specification</enforcement>
      <context_transfer>Agent specifications and TDD requirements for action coordination</context_transfer>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply TRACE framework - Define Actions and create coordination session</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What action definition approach will optimize TRACE framework coordination?
          - What session creation strategy supports multi-agent tracking?
          - How does action sequencing connect to coordination protocol success?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Action Question: What specific actions enable coordinated multi-agent execution?]
          - [Session Question: Why is GitHub session creation critical for TRACE framework coordination?]
          - [Structure Question: How will session structure support precision tracking and agent coordination?]
          - [Organization Question: What session organization optimizes agent communication and progress tracking?]
          - [Alignment Question: How does session setup align with TRACE framework action specifications?]
          - [Protocol Question: What coordination protocol ensures maximum efficiency?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this action definition optimal for TRACE framework coordination?
          - What evidence supports the session creation strategy?
          - How will this coordination protocol maximize multi-agent success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can session creation be combined with action definition for efficiency?</tool_optimization>
        <context_efficiency>How can action coordination optimize context window usage?</context_efficiency>
        <dependency_analysis>What action setup can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_ACTIONS_WITH_SESSION: 
        - SESSION_CREATED: #[number] - [title] for multi-agent coordination
        - Action sequence: [ordered_actions_list]
        - Coordination protocol: [communication_method]</output_format>
      <validation>Must output session ID and action sequence before agent deployment with enhanced reasoning</validation>
      <enforcement>BLOCK if session creation fails - no coordination without TRACE framework tracking</enforcement>
      <context_transfer>Session ID and action sequence for context definition</context_transfer>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply TRACE framework - Define Context and integration requirements</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What context definition approach will optimize multi-agent coordination?
          - What integration requirements need comprehensive specification?
          - How does context definition connect to agent isolation and coordination success?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Environment Question: What is the technical context and environment for multi-agent coordination?]
          - [Dependencies Question: What shared dependencies, constraints, and integration points must agents consider?]
          - [Isolation Question: How do agents maintain context awareness while working in isolation?]
          - [Synchronization Question: What context synchronization is needed between agent worktrees?]
          - [Framework Question: How does TRACE framework context specification improve coordination quality?]
          - [Integration Question: What integration context ensures maximum coordination efficiency?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this context definition optimal for TRACE framework coordination?
          - What evidence supports the integration requirements strategy?
          - How will this context specification maximize multi-agent coordination success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can context definition be combined with integration analysis for efficiency?</tool_optimization>
        <context_efficiency>How can context specification optimize context window usage?</context_efficiency>
        <dependency_analysis>What context definition can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_CONTEXT_DEFINITION:
        - Technical environment: [stack_requirements]
        - Shared constraints: [limitation_list]
        - Integration context: [coordination_requirements]
        - Worktree context: [isolation_specifications]</output_format>
      <validation>Context comprehensively defined for optimal agent coordination with enhanced reasoning</validation>
      <enforcement>BLOCK if context specification insufficient for agent coordination planning</enforcement>
      <context_transfer>Context definition and integration requirements for expectation setting</context_transfer>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Apply TRACE framework - Set Expectations and create git worktrees</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What expectation setting approach will optimize TRACE framework coordination?
          - What worktree creation strategy supports agent isolation and integration?
          - How does expectation definition connect to validation and coordination success?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Expectations Question: What are the precise quality expectations and deliverable specifications?]
          - [Validation Question: How will TRACE framework expectations be validated across all agents?]
          - [Isolation Question: Why are isolated worktrees critical for meeting coordination expectations?]
          - [Structure Question: What worktree structure optimizes agent independence while enabling integration?]
          - [Guidance Question: How do expectation definitions guide agent coordination and final validation?]
          - [Optimization Question: What expectations ensure maximum coordination efficiency?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this expectation setting optimal for TRACE framework coordination?
          - What evidence supports the worktree creation strategy?
          - How will these expectations maximize multi-agent coordination success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can expectation setting be combined with worktree creation for efficiency?</tool_optimization>
        <context_efficiency>How can expectation definition optimize context window usage?</context_efficiency>
        <dependency_analysis>What expectation setup can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_EXPECTATIONS_WITH_WORKTREES:
        - Quality expectations: [deliverable_standards]
        - Validation criteria: [success_metrics]
        - WORKTREES_CREATED:
          - ../worktrees/swarm-[session]-[agent1] (TDD isolation confirmed)
          - ../worktrees/swarm-[session]-[agent2] (TDD isolation confirmed)</output_format>
      <validation>Expectations defined and worktree paths confirmed with TDD isolation and enhanced reasoning</validation>
      <enforcement>VERIFY expectation clarity and worktree creation success before Task() execution</enforcement>
      <context_transfer>Expectations and worktree paths for TRACE-guided task execution</context_transfer>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Execute TRACE-guided Task() calls with advanced coordination protocol</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What task execution approach will optimize TRACE framework coordination?
          - What parallel execution strategy supports multi-agent efficiency?
          - How does task specification connect to TDD isolation and coordination success?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Translation Question: How do TRACE expectations translate to precise Task() specifications?]
          - [Coordination Question: How do agents coordinate shared interfaces without breaking TDD isolation?]
          - [Efficiency Question: What parallel execution patterns optimize multi-agent coordination efficiency?]
          - [Quality Question: How does TRACE framework precision improve agent coordination quality?]
          - [Validation Question: What validation ensures each agent follows TRACE-aligned TDD cycles?]
          - [Execution Question: What task execution ensures maximum coordination success?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this task execution optimal for TRACE framework coordination?
          - What evidence supports the parallel execution strategy?
          - How will this execution approach maximize multi-agent coordination success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can task execution be optimized for 70% performance improvement through parallel calls?</tool_optimization>
        <context_efficiency>How can task specification optimize context window usage?</context_efficiency>
        <dependency_analysis>What task execution can be done in parallel vs sequential for coordination?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_GUIDED_TASK_EXECUTION:
        Task("[Agent1]", "TRACE precision: [context] → [action] → [expectation] + TDD cycle in [worktree]")
        Task("[Agent2]", "TRACE precision: [context] → [action] → [expectation] + TDD cycle in [worktree]")
        Task("[Agent3]", "TRACE precision: [context] → [action] → [expectation] + TDD cycle in [worktree]")</output_format>
      <validation>All Task() calls must include TRACE framework precision and explicit TDD requirements with enhanced reasoning</validation>
      <enforcement>VERIFY each Task() includes TRACE-aligned specifications and TDD cycle enforcement</enforcement>
      <context_transfer>Task execution results for TRACE compliance verification</context_transfer>
    </checkpoint>
    <checkpoint id="7" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Verify TRACE framework compliance and agent coordination success</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What compliance verification approach will validate TRACE framework success?
          - What coordination assessment strategy ensures multi-agent quality?
          - How does compliance verification connect to integration readiness and success?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Fulfillment Question: Did each agent fulfill TRACE framework expectations precisely?]
          - [Deliverables Question: Are component-level deliverables meeting TRACE specification criteria?]
          - [Alignment Question: How do agent deliverables align with original TRACE context and expectations?]
          - [Integration Question: Are integration points properly coordinated according to TRACE framework?]
          - [Quality Question: Is quality validation meeting TRACE framework precision requirements?]
          - [Compliance Question: What compliance verification ensures maximum integration success?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this compliance verification optimal for TRACE framework validation?
          - What evidence supports the coordination assessment strategy?
          - How will this verification approach maximize integration success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can compliance verification be parallelized for efficiency improvement?</tool_optimization>
        <context_efficiency>How can verification optimize context window usage?</context_efficiency>
        <dependency_analysis>What compliance checks can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_COMPLIANCE_VALIDATION:
        - [Agent1]: TRACE COMPLETE - Expectations met: [criteria] - TDD: [status] - Coverage: [%]
        - [Agent2]: TRACE COMPLETE - Expectations met: [criteria] - TDD: [status] - Coverage: [%]
        - [Agent3]: TRACE COMPLETE - Expectations met: [criteria] - TDD: [status] - Coverage: [%]</output_format>
      <validation>Must confirm TRACE framework compliance AND TDD deliverable completion for all agents with enhanced reasoning</validation>
      <enforcement>BLOCK integration if any agent fails TRACE expectations or coverage <90%</enforcement>
      <context_transfer>Compliance verification results for integration testing</context_transfer>
    </checkpoint>
    <checkpoint id="8" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Execute TRACE-guided integration testing across agent boundaries</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What integration testing approach will validate TRACE framework success?
          - What boundary testing strategy ensures multi-agent integration quality?
          - How does integration testing connect to merge readiness and success?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Integration Question: Do components integrate according to TRACE framework context specifications?]
          - [Mismatch Question: Are there interface mismatches or TRACE expectation violations?]
          - [Scenarios Question: Do end-to-end scenarios meet original TRACE framework requirements?]
          - [Performance Question: Are performance criteria from TRACE expectations satisfied?]
          - [Quality Question: How does integration quality compare to TRACE framework standards?]
          - [Validation Question: What integration testing ensures maximum merge success?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this integration testing optimal for TRACE framework validation?
          - What evidence supports the boundary testing strategy?
          - How will this testing approach maximize merge success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can integration testing be parallelized for efficiency improvement?</tool_optimization>
        <context_efficiency>How can testing optimize context window usage?</context_efficiency>
        <dependency_analysis>What integration tests can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_INTEGRATION_VALIDATION:
        - TRACE Context Compliance: [PASS/FAIL] - [context_validation_details]
        - TRACE Expectation Fulfillment: [PASS/FAIL] - [expectation_details]  
        - Integration Testing: [PASS/FAIL] - [technical_details]
        - Performance Validation: [PASS/FAIL] - [performance_metrics]</output_format>
      <validation>All TRACE-guided integration tests must pass before merge with enhanced reasoning</validation>
      <enforcement>BLOCK merge if integration fails TRACE framework validation - must resolve conflicts</enforcement>
      <context_transfer>Integration testing results for error recovery assessment</context_transfer>
    </checkpoint>
    <checkpoint id="9" verify="optional" enforcement="CONDITIONAL" thinking_mode="interleaved">
      <action>Apply TRACE-aware 4-tier error recovery if failures occur</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What error recovery approach will maintain TRACE framework integrity?
          - What recovery strategy preserves multi-agent coordination quality?
          - How does error recovery connect to TRACE framework compliance and success?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Failure Question: What type of failure occurred and how does it relate to TRACE framework compliance?]
          - [Recovery Question: Can we recover while maintaining TRACE precision and TDD integrity?]
          - [Restart Question: Should we restart individual agents or reassess TRACE framework application?]
          - [Preservation Question: How to preserve TRACE-compliant work during recovery?]
          - [Cause Question: Does failure indicate TRACE framework misapplication or execution issues?]
          - [Strategy Question: What recovery strategy ensures maximum coordination success?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this error recovery optimal for TRACE framework maintenance?
          - What evidence supports the recovery strategy?
          - How will this recovery approach maximize coordination success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can error recovery be optimized for efficiency while maintaining quality?</tool_optimization>
        <context_efficiency>How can recovery optimize context window usage?</context_efficiency>
        <dependency_analysis>What recovery tasks can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_RECOVERY_STATUS: [NONE|TIER_1|TIER_2|TIER_3|TIER_4] - TRACE Framework: [maintained|reassess]</output_format>
      <validation>Only required if errors detected with TRACE framework assessment and enhanced reasoning</validation>
      <enforcement>ESCALATE to next tier if current tier fails, reassess TRACE if systematic failure</enforcement>
      <context_transfer>Recovery status and TRACE framework assessment for merge validation</context_transfer>
    </checkpoint>
    <checkpoint id="10" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Merge agent work with TRACE validation, TDD compliance, and cleanup</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What merge validation approach will ensure TRACE framework success?
          - What cleanup strategy preserves coordination artifacts and quality?
          - How does merge completion connect to TRACE framework compliance and excellence?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Testing Question: Are all tests still passing after merge and meeting TRACE expectations?]
          - [Integration Question: Is the integrated codebase properly tested and meeting TRACE framework standards?]
          - [Discipline Question: Have we maintained both TRACE precision and TDD discipline throughout?]
          - [Readiness Question: Is the final system ready for production and meeting original TRACE requirements?]
          - [Excellence Question: Does final deliverable exceed expectations set by TRACE framework?]
          - [Completion Question: What final validation ensures maximum TRACE framework success?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this merge validation optimal for TRACE framework completion?
          - What evidence supports the cleanup and quality strategy?
          - How will this completion approach maximize TRACE framework success?
        </decision_reasoning>
      </interleaved_thinking>
      <parallel_execution_considerations>
        <tool_optimization>Can merge validation be parallelized for efficiency improvement?</tool_optimization>
        <context_efficiency>How can completion optimize context window usage?</context_efficiency>
        <dependency_analysis>What merge validation can be done in parallel vs sequential?</dependency_analysis>
      </parallel_execution_considerations>
      <output_format>TRACE_MERGE_VALIDATION:
        - TRACE Framework Compliance: [COMPLETE/PARTIAL] - [compliance_details]
        - Merge Status: [SUCCESS/CONFLICTS] - [merge_details]
        - Final Test Suite: [PASS/FAIL] - Total tests: [count] - TRACE aligned: [%]
        - Coverage: [%] (target: ≥90%) - Quality: [TRACE_standards_met]
        - Worktrees Cleaned: [count] - Coordination artifacts preserved: [status]</output_format>
      <validation>Must verify TRACE compliance, TDD success, and integration quality before completion with enhanced reasoning</validation>
      <enforcement>ROLLBACK if final tests fail, coverage drops below 90%, or TRACE expectations unmet</enforcement>
      <context_transfer>Complete TRACE framework validation with coordination success confirmation</context_transfer>
    </checkpoint>
  </thinking_pattern>
  
  <trace_framework_integration enforcement="MANDATORY">
    <task_definition>Define precise task complexity and multi-agent coordination requirements</task_definition>
    <request_specification>Specify exact technical requirements and agent deliverables with precision</request_specification>
    <action_coordination>Orchestrate agents through precise action sequences and coordination protocols</action_coordination>
    <context_management>Maintain comprehensive context awareness across isolated agent worktrees</context_management>
    <expectation_validation>Validate agent deliverables against TRACE framework precision standards</expectation_validation>
    <framework_compliance>Ensure all coordination meets TRACE framework quality and precision criteria</framework_compliance>
    <validation>Reference frameworks/trace.md for complete TRACE framework implementation in multi-agent scenarios</validation>
  </trace_framework_integration>
  
  <tdd_integration enforcement="MANDATORY">
    <trace_aligned_tdd>Each agent follows TRACE-aligned TDD cycles with precision specifications in isolated worktrees</trace_aligned_tdd>
    <multi_agent_coordination>Agents coordinate shared interfaces through TRACE-specified tests-first contracts</multi_agent_coordination>
    <integration_testing>TRACE-guided integration testing validates all agent work against framework expectations</integration_testing>
    <expectation_validation>TDD cycles must align with TRACE framework expectation criteria and quality standards</expectation_validation>
    <validation>Reference quality/tdd.md#quality_gates for per-agent enforcement and frameworks/trace.md for precision requirements</validation>
    <blocking_conditions>
      <condition>TRACE framework application incomplete before agent deployment</condition>
      <condition>Any agent starts implementation before writing TRACE-aligned tests</condition>
      <condition>Integration attempted before all agents complete TRACE-compliant TDD cycles</condition>
      <condition>Final merge proceeds with failing tests, coverage <90%, or TRACE expectation failures</condition>
      <condition>Agent worktrees have conflicting TRACE specifications or test requirements</condition>
      <condition>Agent coordination lacks TRACE framework precision and context awareness</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <critical_features>
    <git_worktree_isolation>
      <requirement>Create worktrees BEFORE Task() execution</requirement>
      <verification>Each agent must confirm isolated workspace access</verification>
      <pattern>../worktrees/swarm-{session}-{agent}</pattern>
      <cleanup>Clean merge process required for completion</cleanup>
      <output_format>WORKTREE_VERIFICATION: [agent] = [path] = [status]</output_format>
    </git_worktree_isolation>
    <parallel_execution>
      <requirement>ALL Task() calls in SINGLE message</requirement>
      <performance>True parallelism = 70% faster execution</performance>
      <verification>Must show all Task() calls in single tool invocation</verification>
      <example>Task("frontend", {...}), Task("backend", {...}), Task("database", {...})</example>
      <output_format>PARALLEL_CONFIRMED: [count] agents in single message</output_format>
    </parallel_execution>
  </critical_features>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before multi-agent coordination</module>
      <module>frameworks/trace.md - TRACE framework precision for multi-agent specification</module>
      <module>patterns/session-management.md - GitHub session creation for TRACE-guided coordination tracking</module>
      <module>patterns/multi-agent.md - Task() and Batch() coordination with TRACE precision and worktrees</module>
      <module>quality/tdd.md - Multi-agent TDD coordination with TRACE framework alignment</module>
      <module>patterns/git-operations.md - Git worktree isolation and TRACE-compliant merge protocols</module>
      <module>quality/production-standards.md - Quality gate validation across all agents with TRACE criteria</module>
    </core_stack>
    <contextual_modules>
      <conditional module="frameworks/framework-selector.md" condition="complex_coordination_requirements"/>
      <conditional module="frameworks/advanced-frameworks.md" condition="specialized_framework_needs"/>
      <conditional module="quality/error-recovery.md" condition="agent_failures OR coordination_issues"/>
      <conditional module="git/conventional-commits.md" condition="merge_complete"/>
      <conditional module="quality/pre-commit.md" condition="final_integration"/>
      <conditional module="development/code-review.md" condition="complex_integration"/>
    </contextual_modules>
  </module_execution>
  
  <depends_on>
    frameworks/trace.md for TRACE framework precision and multi-agent specification patterns
    frameworks/framework-selector.md for intelligent framework selection and coordination optimization
    patterns/multi-agent.md for Task() and Batch() coordination with TRACE precision and worktrees
    patterns/git-operations.md for git worktree management patterns with TRACE compliance
    patterns/pattern-library.md for proven execution patterns with framework integration
    patterns/session-management.md for automatic session creation with TRACE coordination
    quality/error-recovery.md for 4-tier recovery hierarchy with TRACE framework awareness
    quality/tdd.md for TRACE-aligned TDD enforcement across multi-agent scenarios
    docs/framework/native-patterns.md for Task()/Batch() documentation with framework integration
  </depends_on>
  
  <examples>
    /swarm "Build e-commerce platform"     # TRACE precision → Multi-service system with isolated worktrees
    /swarm "Optimize for 10x scale"        # TRACE coordination → Performance across layers in parallel  
    /swarm "Migrate monolith to microservices" # TRACE framework → Architecture shift with clean isolation
    /swarm "Implement payment system"      # TRACE specification → Complex integration with compliance requirements
    /swarm "Build AI-powered analytics"    # TRACE precision → Multi-component ML system with coordination
  </examples>
  
  <tdd_integration enforcement="MANDATORY">
    <multi_agent_testing>TDD approach coordinated across all agents using TRACE framework precision</multi_agent_testing>
    <red_phase>Each agent writes failing tests for their component using quality/tdd.md#red_phase_compliance</red_phase>
    <green_phase>Agents implement minimal solutions to pass tests using quality/tdd.md#green_phase_compliance</green_phase>
    <refactor_phase>Coordinated refactoring while maintaining green tests using quality/tdd.md#refactor_phase_compliance</refactor_phase>
    <integration_testing>Cross-agent integration tests with TRACE framework alignment</integration_testing>
    <validation>Reference quality/tdd.md#quality_gates for strict enforcement across all agents</validation>
    
    <swarm_checkpoint_enforcement>
      <agent_coordination_testing>
        <tdd_validation>BLOCK unless each agent has failing tests for their component responsibilities</tdd_validation>
        <coordination_coverage>ENSURE tests validate agent coordination and interface contracts</coordination_coverage>
        <quality_gate>Reference quality/tdd.md#multi_agent_test_validation</quality_gate>
      </agent_coordination_testing>
      
      <component_integration_testing>
        <tdd_validation>BLOCK unless integration tests validate cross-component interactions</tdd_validation>
        <system_coverage>ENSURE tests validate system-wide behavior and data flow</system_coverage>
        <quality_gate>Reference quality/tdd.md#integration_test_validation</quality_gate>
      </component_integration_testing>
      
      <parallel_execution_testing>
        <tdd_validation>BLOCK unless tests validate parallel execution safety and coordination</tdd_validation>
        <concurrency_coverage>ENSURE tests validate concurrent operations and race conditions</concurrency_coverage>
        <quality_gate>Reference quality/tdd.md#parallel_execution_validation</quality_gate>
      </parallel_execution_testing>
      
      <merge_validation_testing>
        <tdd_validation>BLOCK unless tests validate successful component merging</tdd_validation>
        <system_integrity>ENSURE tests validate system integrity after component integration</system_integrity>
        <quality_gate>Reference quality/tdd.md#merge_validation</quality_gate>
      </merge_validation_testing>
    </swarm_checkpoint_enforcement>
    
    <blocking_conditions>
      <condition>Agent implementation attempted before TRACE framework task definition</condition>
      <condition>Component development bypassed multi-agent coordination requirements</condition>
      <condition>Tests written without agent coordination and interface validation</condition>
      <condition>Implementation exceeds agent component boundaries defined in TRACE planning</condition>
      <condition>Integration testing skipped for multi-component system</condition>
      <condition>Test coverage below 90% for new multi-component code</condition>
      <condition>Agent quality below TRACE framework standards and precision requirements</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <rules>
    • ALWAYS applies TRACE framework for precision coordination
    • AUTO-creates GitHub session for TRACE-guided coordination tracking
    • AUTO-creates git worktrees for each agent with TRACE context isolation
    • For ≥3 component systems requiring TRACE precision and isolation
    • Native Task() and Batch() patterns with TRACE specifications and error recovery
    • TRACE-compliant worktree cleanup after successful merge with validation
    • Framework selection intelligence for complex coordination scenarios
  </rules>
  
  <pattern_usage>
    • Uses trace_framework_integration pattern for precision coordination
    • Implements parallel_execution pattern with TRACE specifications
    • Applies batch_operations for homogeneous work with framework alignment
    • Leverages issue_tracking pattern for GitHub sessions with TRACE coordination
    • Uses three_x_rule for planning agent assignments with framework precision
    • Integrates git_worktree_patterns from git-operations.md with TRACE compliance
    • Implements error_recovery patterns with TRACE framework awareness
    • Applies framework_selection intelligence for optimal coordination strategies
    
    See modules/frameworks/trace.md for TRACE framework implementation
    See modules/patterns/multi-agent.md for TRACE-integrated coordination
    See modules/patterns/git-operations.md for TRACE-compliant worktree patterns
    See modules/frameworks/framework-selector.md for coordination optimization
  </pattern_usage>
  

  <prompt_construction>
    <assembly_preview>
      TRACE-GUIDED WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. TRACE Task  │ → Define complexity & coordination requirements
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. TRACE       │ → Specify precise technical requirements
      │    Request     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. TRACE       │ → Define actions & create coordination session
      │    Actions     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. TRACE       │ → Define context & integration requirements
      │    Context     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 5. TRACE       │ → Set expectations & create worktrees
      │    Expectations│
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 6. TRACE-Guided│ → Parallel Task() execution with precision
      │    Execution   │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 7. TRACE       │ → Framework compliance validation
      │    Validation  │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 8. TRACE       │ → Integration testing with framework criteria
      │    Integration │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 9. TRACE       │ → Final merge with framework validation
      │    Merge       │
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~30,000
      - TRACE framework application: 5,000
      - Session coordination: 3,000
      - Component analysis with precision: 6,000
      - Worktree operations: 2,000
      - Parallel task execution: 10,000
      - TRACE validation & integration: 4,000
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /swarm "E-commerce platform"
      [00:15] 🎯 TRACE TASK: Complexity HIGH, 4 agents required, integration COMPLEX
      [00:30] 📋 TRACE REQUEST: Precise technical specs defined for all components
      [00:45] 🎯 TRACE ACTIONS: GitHub session #156 created for coordination
      [01:00] 🌐 TRACE CONTEXT: Technical environment and constraints mapped
      [01:15] ✅ TRACE EXPECTATIONS: Quality standards set, worktrees created
      [01:30] 🚀 TRACE EXECUTION: 4 specialized Task() agents with precision specs
      [02:15] 🔍 TRACE VALIDATION: All agents meeting framework compliance
      [02:30] 🔗 TRACE INTEGRATION: Components validated against expectations
      [02:45] ✅ TRACE COMPLETE: Platform deployed meeting all TRACE criteria
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Reads TRACE framework integrated checkpoint structure sequentially
      2. Executes critical_thinking questions with TRACE precision internally
      3. Formats output according to TRACE-aligned output_format specifications
      4. Validates against TRACE framework compliance and enforcement rules before proceeding
      5. Applies parallel execution optimization with TRACE coordination where possible
      6. Integrates framework selection intelligence for optimal coordination strategies
    </parsing_behavior>

    <decision_points>
      - TRACE framework compliance validation triggers precision enforcement actions
      - Checkpoint failures trigger TRACE-aware enforcement and recovery actions
      - Module selection based on TRACE requirements and contextual conditions
      - Parallel execution optimized for TRACE-guided independent operations
      - Quality gate validation at completion boundaries with TRACE criteria
      - Error recovery through TRACE-aware graceful degradation paths
      - Framework selection intelligence guides coordination optimization decisions
    </decision_points>
  </claude_4_interpretation>

</command>
```