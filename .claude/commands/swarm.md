| version | last_updated | status |
|---------|--------------|--------|
| 2.6.0   | 2025-07-08   | stable |

# /swarm - Multi-agent coordination with TRACE framework and advanced TDD orchestration

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Multi-agent coordination with TRACE framework for complex system development and TDD orchestration">
  
  <delegation target="modules/patterns/multi-agent.md">
    TRACE framework → Create session → Setup worktrees → Decompose work → Execute Task() calls → Merge results → Quality validation
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Apply TRACE framework - Define Task complexity and coordination requirements</action>
      <critical_thinking>
        - What are the precise task boundaries and complexity levels for multi-agent coordination?
        - How many agents will be needed and what are their specialized responsibilities?
        - What are the integration points and dependencies between agents?
        - How does task decomposition align with TRACE framework precision?
        - What coordination overhead should be expected for this complexity level?
      </critical_thinking>
      <output_format>TRACE_TASK_DEFINITION: [complexity_level] requiring [agent_count] agents with [integration_complexity] coordination</output_format>
      <validation>Task complexity and agent requirements clearly defined</validation>
      <enforcement>BLOCK if task analysis insufficient for multi-agent coordination planning</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Apply TRACE framework - Specify precise Requests and agent assignments</action>
      <critical_thinking>
        - What are the exact technical specifications each agent must deliver?
        - How do agent deliverables interface with each other?
        - What are the precise quality requirements and acceptance criteria?
        - How will agents coordinate shared contracts and dependencies?
        - What TDD requirements apply to each agent specialization?
      </critical_thinking>
      <output_format>TRACE_REQUEST_SPECIFICATION:
        - [Agent1]: [precise_technical_requirements] + TDD obligations
        - [Agent2]: [precise_technical_requirements] + TDD obligations
        - [Agent3]: [precise_technical_requirements] + TDD obligations</output_format>
      <validation>Agent requests specified with precision and clear TDD integration</validation>
      <enforcement>BLOCK if any agent request lacks precision or TDD specification</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Apply TRACE framework - Define Actions and create coordination session</action>
      <critical_thinking>
        - What specific actions enable coordinated multi-agent execution?
        - Why is GitHub session creation critical for TRACE framework coordination?
        - How will session structure support precision tracking and agent coordination?
        - What session organization optimizes agent communication and progress tracking?
        - How does session setup align with TRACE framework action specifications?
      </critical_thinking>
      <output_format>TRACE_ACTIONS_WITH_SESSION: 
        - SESSION_CREATED: #[number] - [title] for multi-agent coordination
        - Action sequence: [ordered_actions_list]
        - Coordination protocol: [communication_method]</output_format>
      <validation>Must output session ID and action sequence before agent deployment</validation>
      <enforcement>BLOCK if session creation fails - no coordination without TRACE framework tracking</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Apply TRACE framework - Define Context and integration requirements</action>
      <critical_thinking>
        - What is the technical context and environment for multi-agent coordination?
        - What shared dependencies, constraints, and integration points must agents consider?
        - How do agents maintain context awareness while working in isolation?
        - What context synchronization is needed between agent worktrees?
        - How does TRACE framework context specification improve coordination quality?
      </critical_thinking>
      <output_format>TRACE_CONTEXT_DEFINITION:
        - Technical environment: [stack_requirements]
        - Shared constraints: [limitation_list]
        - Integration context: [coordination_requirements]
        - Worktree context: [isolation_specifications]</output_format>
      <validation>Context comprehensively defined for optimal agent coordination</validation>
      <enforcement>BLOCK if context specification insufficient for agent coordination planning</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Apply TRACE framework - Set Expectations and create git worktrees</action>
      <critical_thinking>
        - What are the precise quality expectations and deliverable specifications?
        - How will TRACE framework expectations be validated across all agents?
        - Why are isolated worktrees critical for meeting coordination expectations?
        - What worktree structure optimizes agent independence while enabling integration?
        - How do expectation definitions guide agent coordination and final validation?
      </critical_thinking>
      <output_format>TRACE_EXPECTATIONS_WITH_WORKTREES:
        - Quality expectations: [deliverable_standards]
        - Validation criteria: [success_metrics]
        - WORKTREES_CREATED:
          - ../worktrees/swarm-[session]-[agent1] (TDD isolation confirmed)
          - ../worktrees/swarm-[session]-[agent2] (TDD isolation confirmed)</output_format>
      <validation>Expectations defined and worktree paths confirmed with TDD isolation</validation>
      <enforcement>VERIFY expectation clarity and worktree creation success before Task() execution</enforcement>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING">
      <action>Execute TRACE-guided Task() calls with advanced coordination protocol</action>
      <critical_thinking>
        - How do TRACE expectations translate to precise Task() specifications?
        - How do agents coordinate shared interfaces without breaking TDD isolation?
        - What parallel execution patterns optimize multi-agent coordination efficiency?
        - How does TRACE framework precision improve agent coordination quality?
        - What validation ensures each agent follows TRACE-aligned TDD cycles?
      </critical_thinking>
      <output_format>TRACE_GUIDED_TASK_EXECUTION:
        Task("[Agent1]", "TRACE precision: [context] → [action] → [expectation] + TDD cycle in [worktree]")
        Task("[Agent2]", "TRACE precision: [context] → [action] → [expectation] + TDD cycle in [worktree]")
        Task("[Agent3]", "TRACE precision: [context] → [action] → [expectation] + TDD cycle in [worktree]")</output_format>
      <validation>All Task() calls must include TRACE framework precision and explicit TDD requirements</validation>
      <enforcement>VERIFY each Task() includes TRACE-aligned specifications and TDD cycle enforcement</enforcement>
    </checkpoint>
    <checkpoint id="7" verify="true" enforcement="BLOCKING">
      <action>Verify TRACE framework compliance and agent coordination success</action>
      <critical_thinking>
        - Did each agent fulfill TRACE framework expectations precisely?
        - Are component-level deliverables meeting TRACE specification criteria?
        - How do agent deliverables align with original TRACE context and expectations?
        - Are integration points properly coordinated according to TRACE framework?
        - Is quality validation meeting TRACE framework precision requirements?
      </critical_thinking>
      <output_format>TRACE_COMPLIANCE_VALIDATION:
        - [Agent1]: TRACE COMPLETE - Expectations met: [criteria] - TDD: [status] - Coverage: [%]
        - [Agent2]: TRACE COMPLETE - Expectations met: [criteria] - TDD: [status] - Coverage: [%]
        - [Agent3]: TRACE COMPLETE - Expectations met: [criteria] - TDD: [status] - Coverage: [%]</output_format>
      <validation>Must confirm TRACE framework compliance AND TDD deliverable completion for all agents</validation>
      <enforcement>BLOCK integration if any agent fails TRACE expectations or coverage <90%</enforcement>
    </checkpoint>
    <checkpoint id="8" verify="true" enforcement="BLOCKING">
      <action>Execute TRACE-guided integration testing across agent boundaries</action>
      <critical_thinking>
        - Do components integrate according to TRACE framework context specifications?
        - Are there interface mismatches or TRACE expectation violations?
        - Do end-to-end scenarios meet original TRACE framework requirements?
        - Are performance criteria from TRACE expectations satisfied?
        - How does integration quality compare to TRACE framework standards?
      </critical_thinking>
      <output_format>TRACE_INTEGRATION_VALIDATION:
        - TRACE Context Compliance: [PASS/FAIL] - [context_validation_details]
        - TRACE Expectation Fulfillment: [PASS/FAIL] - [expectation_details]  
        - Integration Testing: [PASS/FAIL] - [technical_details]
        - Performance Validation: [PASS/FAIL] - [performance_metrics]</output_format>
      <validation>All TRACE-guided integration tests must pass before merge</validation>
      <enforcement>BLOCK merge if integration fails TRACE framework validation - must resolve conflicts</enforcement>
    </checkpoint>
    <checkpoint id="9" verify="optional" enforcement="CONDITIONAL">
      <action>Apply TRACE-aware 4-tier error recovery if failures occur</action>
      <critical_thinking>
        - What type of failure occurred and how does it relate to TRACE framework compliance?
        - Can we recover while maintaining TRACE precision and TDD integrity?
        - Should we restart individual agents or reassess TRACE framework application?
        - How to preserve TRACE-compliant work during recovery?
        - Does failure indicate TRACE framework misapplication or execution issues?
      </critical_thinking>
      <output_format>TRACE_RECOVERY_STATUS: [NONE|TIER_1|TIER_2|TIER_3|TIER_4] - TRACE Framework: [maintained|reassess]</output_format>
      <validation>Only required if errors detected with TRACE framework assessment</validation>
      <enforcement>ESCALATE to next tier if current tier fails, reassess TRACE if systematic failure</enforcement>
    </checkpoint>
    <checkpoint id="10" verify="true" enforcement="BLOCKING">
      <action>Merge agent work with TRACE validation, TDD compliance, and cleanup</action>
      <critical_thinking>
        - Are all tests still passing after merge and meeting TRACE expectations?
        - Is the integrated codebase properly tested and meeting TRACE framework standards?
        - Have we maintained both TRACE precision and TDD discipline throughout?
        - Is the final system ready for production and meeting original TRACE requirements?
        - Does final deliverable exceed expectations set by TRACE framework?
      </critical_thinking>
      <output_format>TRACE_MERGE_VALIDATION:
        - TRACE Framework Compliance: [COMPLETE/PARTIAL] - [compliance_details]
        - Merge Status: [SUCCESS/CONFLICTS] - [merge_details]
        - Final Test Suite: [PASS/FAIL] - Total tests: [count] - TRACE aligned: [%]
        - Coverage: [%] (target: ≥90%) - Quality: [TRACE_standards_met]
        - Worktrees Cleaned: [count] - Coordination artifacts preserved: [status]</output_format>
      <validation>Must verify TRACE compliance, TDD success, and integration quality before completion</validation>
      <enforcement>ROLLBACK if final tests fail, coverage drops below 90%, or TRACE expectations unmet</enforcement>
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