| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# Framework-Coordinated Multi-Agent Module with TRACE Integration

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="multi_agent" category="patterns">
  
  <purpose>
    Define and implement native Claude Code multi-agent patterns with TRACE framework coordination using Task() and Batch() for parallel execution with git worktree isolation and framework-aware agent coordination for maximum effectiveness.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>complex_system_requirements, component_breakdown, coordination_context</required>
      <optional>worktree_preferences, agent_specializations, integration_requirements</optional>
    </inputs>
    <outputs>
      <success>coordinated_agents, worktree_isolation, integrated_system, comprehensive_testing</success>
      <failure>coordination_failures, worktree_conflicts, integration_issues, testing_gaps</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Apply TRACE framework for precise multi-agent coordination
      2. Create GitHub session for coordination tracking
      3. Analyze and decompose system into specialized agent responsibilities
      4. Setup isolated git worktrees for conflict-free parallel development
      5. Execute coordinated Task() calls with TRACE specifications and TDD enforcement
      6. Integrate results with comprehensive testing and framework-aware validation
    </claude_4_behavior>
  </execution_pattern>
  
  <thinking_pattern>
    <checkpoint id="1" verify="true" enforcement="MANDATORY">
      <action>Apply TRACE framework - Define Task complexity and multi-agent requirements</action>
      <critical_thinking>
        - What are the precise task boundaries and complexity levels for multi-agent coordination?
        - How many agents will be needed and what are their specialized responsibilities?
        - What are the integration points and dependencies between agents?
        - How does task decomposition align with TRACE framework precision?
        - What coordination overhead should be expected for this complexity level?
      </critical_thinking>
      <output_format>TRACE_TASK_DEFINITION: [complexity_level] requiring [agent_count] agents with [integration_complexity] coordination</output_format>
      <validation>Task complexity and agent requirements clearly defined with TRACE framework</validation>
      <enforcement>BLOCK if task analysis insufficient for multi-agent coordination planning</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="MANDATORY">
      <action>Apply TRACE framework - Specify precise Requests and agent assignments</action>
      <critical_thinking>
        - What are the exact technical specifications each agent must deliver?
        - How do agent deliverables interface with each other?
        - What are the precise quality requirements and acceptance criteria?
        - How will agents coordinate shared contracts and dependencies?
        - What TRACE framework specifications apply to each agent specialization?
      </critical_thinking>
      <output_format>TRACE_REQUEST_SPECIFICATION:
        - [Agent1]: [precise_technical_requirements] + TRACE specifications
        - [Agent2]: [precise_technical_requirements] + TRACE specifications
        - [Agent3]: [precise_technical_requirements] + TRACE specifications
        - Decision precedence: [precedence_order_with_trace_alignment]</output_format>
      <validation>Agent requests specified with TRACE framework precision and clear integration</validation>
      <enforcement>BLOCK if any agent request lacks TRACE framework specification</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="MANDATORY">
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
        - Coordination protocol: [communication_method]
        - WORKTREES_CREATED: [paths_with_trace_context]</output_format>
      <validation>Must output session ID and worktree paths before agent deployment</validation>
      <enforcement>BLOCK if session creation fails - no coordination without TRACE framework tracking</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="MANDATORY">
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
    <checkpoint id="5" verify="true" enforcement="MANDATORY">
      <action>Apply TRACE framework - Set Expectations and execute coordinated Task() calls</action>
      <critical_thinking>
        - What are the precise quality expectations and deliverable specifications?
        - How will TRACE framework expectations be validated across all agents?
        - How do expectation definitions guide agent coordination and final validation?
        - What Task() execution patterns align with TRACE framework specifications?
        - How do expectations integrate with decision coordination protocols?
      </critical_thinking>
      <output_format>TRACE_EXPECTATIONS_WITH_EXECUTION:
        - Quality expectations: [deliverable_standards]
        - Validation criteria: [success_metrics]
        - TASK_EXECUTION_WITH_TRACE:
          Task("[Agent1]", "TRACE precision: [context] → [action] → [expectation]")
          Task("[Agent2]", "TRACE precision: [context] → [action] → [expectation]")
          Task("[Agent3]", "TRACE precision: [context] → [action] → [expectation]")</output_format>
      <validation>Expectations defined and Task() calls include TRACE framework specifications</validation>
      <enforcement>VERIFY each Task() includes TRACE-aligned specifications and coordination requirements</enforcement>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="MANDATORY">
      <action>Verify TRACE framework compliance and agent coordination success</action>
      <critical_thinking>
        - Did each agent fulfill TRACE framework expectations precisely?
        - Are component-level deliverables meeting TRACE specification criteria?
        - How do agent deliverables align with original TRACE context and expectations?
        - Are integration points properly coordinated according to TRACE framework?
        - Is quality validation meeting TRACE framework precision requirements?
      </critical_thinking>
      <output_format>TRACE_COMPLIANCE_VALIDATION:
        - [Agent1]: TRACE COMPLETE - Expectations met: [criteria] - Integration: [status]
        - [Agent2]: TRACE COMPLETE - Expectations met: [criteria] - Integration: [status]
        - [Agent3]: TRACE COMPLETE - Expectations met: [criteria] - Integration: [status]
        - Decision registry: [populated_and_acknowledged]</output_format>
      <validation>Must confirm TRACE framework compliance AND deliverable completion for all agents</validation>
      <enforcement>BLOCK integration if any agent fails TRACE expectations or coordination requirements</enforcement>
    </checkpoint>
    <checkpoint id="7" verify="optional" enforcement="CONDITIONAL">
      <action>Apply TRACE-aware error recovery if failures occur</action>
      <critical_thinking>
        - What type of failure occurred and how does it relate to TRACE framework compliance?
        - Can we recover while maintaining TRACE precision and coordination integrity?
        - Should we restart individual agents or reassess TRACE framework application?
        - How to preserve TRACE-compliant work during recovery?
        - Does failure indicate TRACE framework misapplication or execution issues?
      </critical_thinking>
      <output_format>TRACE_RECOVERY_STATUS: [NONE|TIER_1|TIER_2|TIER_3|TIER_4] - TRACE Framework: [maintained|reassess]</output_format>
      <validation>Only required if errors detected with TRACE framework assessment</validation>
      <enforcement>ESCALATE to next tier if current tier fails, reassess TRACE if systematic failure</enforcement>
    </checkpoint>
  </thinking_pattern>
  
    <checkpoint id="8" verify="true" enforcement="MANDATORY">
      <action>Merge agent work with TRACE validation and comprehensive integration</action>
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
        - Decision consistency: [VERIFIED/CONFLICTS]
        - Integration success: [YES/NO]
        - Worktrees cleaned: [count]</output_format>
      <validation>All TRACE-guided integration tests must pass before merge</validation>
      <enforcement>BLOCK merge if integration fails TRACE framework validation - must resolve conflicts</enforcement>
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
  
  <trigger_conditions>
    <condition type="automatic">Complex tasks requiring 3+ components or specialized expertise</condition>
    <condition type="explicit">User requests /swarm command or multi-agent coordination</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="enhanced_task_breakdown" order="1">
      <requirements>
        Complete task analysis with component identification and dependency mapping
        Complexity estimation with effort sizing (S/M/L/XL scale)
        Success criteria definition for each component and integration point
        Risk assessment with mitigation strategies for high-risk components
      </requirements>
      <actions>
        Identify all components affected by the task (frontend, backend, database, infrastructure)
        Map dependencies between components and identify blocking relationships
        Estimate complexity using story point scale: S(1-3), M(5-8), L(13-21), XL(34+)
        Order tasks by dependency priority and risk level (high-risk tasks first)
        Create detailed subtask checklist with specific deliverables and acceptance criteria
        Define success criteria for each component and overall integration
        Generate GitHub parent issue with subtask issues linked by dependencies
      </actions>
      <validation>
        All affected components identified with clear scope boundaries
        Dependencies mapped with critical path analysis completed
        Complexity estimates align with historical data and team capacity
        Success criteria are measurable and testable
        GitHub issue structure created with proper linking and milestones
      </validation>
    </phase>
    
    <phase name="pattern_selection" order="2">
      <requirements>
        Task complexity assessed for heterogeneous vs homogeneous work
        Component count and expertise diversity evaluated
        GitHub session automatically created for coordination tracking
        Agent assignments optimized based on breakdown analysis
      </requirements>
      <actions>
        Analyze task requirements for specialized expertise diversity using breakdown data
        Count affected system components and integration complexity from analysis
        Select Task() pattern for heterogeneous work or Batch() for homogeneous work
        Create mandatory GitHub session for multi-agent coordination with breakdown summary
        Assign agents based on component ownership and expertise requirements
      </actions>
      <validation>
        Pattern selection justified by task analysis (Task() vs Batch())
        Session created with proper multi-agent tracking labels and breakdown reference
        Agent assignments align with required specialized expertise and component ownership
      </validation>
    </phase>
    
    <phase name="worktree_isolation" order="3">
      <requirements>
        Each agent requires isolated git worktree for parallel development
        Worktrees created before Task() execution for clean environments
        Agent-specific dependencies and build environments maintained
        Worktree assignment matches component breakdown and agent expertise
      </requirements>
      <actions>
        Create dedicated worktree for each agent using git worktree patterns
        Initialize agent-specific environments (venv, node_modules, etc.)
        Configure agent workspace with required tools and dependencies
        Establish worktree naming convention: ../worktrees/swarm-{session}-{agent}
        Map worktrees to component ownership from breakdown analysis
      </actions>
      <validation>
        Each agent has isolated worktree at ../worktrees/swarm-*
        No workspace conflicts between parallel agents
        All agent environments properly initialized
        Worktree assignments align with component breakdown
      </validation>
    </phase>
    
    <phase name="agent_coordination" order="4">
      <requirements>
        All Task() or Batch() calls executed in single message for true parallelism
        Agents have independent, non-dependent work assignments based on breakdown
        Session serves as communication and progress tracking hub with breakdown reference
        Agent assignments respect dependency order from breakdown analysis
      </requirements>
      <actions>
        Execute all agent assignments in parallel using single message
        Ensure agent independence with no sequential dependencies (per breakdown)
        Document agent roles and responsibilities in session with component mapping
        Establish progress tracking and milestone reporting structure using breakdown metrics
        Reference breakdown analysis for agent coordination and progress measurement
      </actions>
      <validation>
        All agents active and working in parallel coordination
        No blocking dependencies between agent assignments (validated against breakdown)
        Session actively tracking progress from all agents with breakdown milestones
        Agent work aligns with original breakdown analysis and success criteria
      </validation>
    </phase>
    
    <phase name="completion_coordination" order="5">
      <requirements>
        All agent work completed successfully with quality verification
        Integration testing completed across all agent deliverables
        Session documentation complete with lessons learned and breakdown retrospective
        Success criteria from breakdown analysis verified and met
      </requirements>
      <actions>
        Verify all agent deliverables meet quality standards and breakdown success criteria
        Execute integration testing across all agent outputs using breakdown integration points
        Document architectural decisions and coordination patterns with breakdown insights
        Complete session with comprehensive outcome documentation and breakdown retrospective
        Analyze breakdown accuracy vs actual implementation for future improvements
      </actions>
      <validation>
        All agent work integrated successfully without conflicts
        Quality standards met across all deliverables per breakdown criteria
        Session documentation complete with reusable patterns and breakdown learnings
        Breakdown analysis accuracy assessed for continuous improvement
      </validation>
    </phase>
    
  </implementation>
  
  <enhanced_task_breakdown>
    <component_identification>
      <frontend_components>
        <scope>User interface, client-side logic, user experience flows</scope>
        <indicators>UI mockups, user stories, interaction design, responsive requirements</indicators>
        <estimation_factors>Component complexity, API integrations, state management, testing scope</estimation_factors>
        <success_criteria>Functional UI components, responsive design, accessibility compliance, user acceptance</success_criteria>
      </frontend_components>
      
      <backend_components>
        <scope>Server-side logic, APIs, business rules, data processing</scope>
        <indicators>API endpoints, business logic, data validation, integration requirements</indicators>
        <estimation_factors>Algorithm complexity, database operations, external integrations, performance requirements</estimation_factors>
        <success_criteria>Functional APIs, performance benchmarks, security compliance, data integrity</success_criteria>
      </backend_components>
      
      <database_components>
        <scope>Data models, migrations, query optimization, data integrity</scope>
        <indicators>Schema changes, new tables, data relationships, migration requirements</indicators>
        <estimation_factors>Schema complexity, migration risk, query performance, data volume</estimation_factors>
        <success_criteria>Schema deployed, data migrated, performance targets met, integrity maintained</success_criteria>
      </database_components>
      
      <infrastructure_components>
        <scope>Deployment, scaling, monitoring, security infrastructure</scope>
        <indicators>Environment changes, scaling requirements, monitoring needs, security updates</indicators>
        <estimation_factors>Configuration complexity, scaling requirements, monitoring scope, security impact</estimation_factors>
        <success_criteria>Environment stability, scaling capability, monitoring coverage, security compliance</success_criteria>
      </infrastructure_components>
    </component_identification>
    
    <dependency_mapping>
      <critical_path_analysis>
        <blocking_dependencies>Tasks that prevent other tasks from starting</blocking_dependencies>
        <parallel_opportunities>Tasks that can be executed simultaneously</parallel_opportunities>
        <integration_points>Points where component work must be coordinated</integration_points>
        <risk_dependencies>Dependencies with high failure risk that need mitigation</risk_dependencies>
      </critical_path_analysis>
      
      <dependency_types>
        <technical_dependencies>Code that must exist before other code can be written</technical_dependencies>
        <data_dependencies>Data structures or migrations required by other components</data_dependencies>
        <interface_dependencies>APIs or contracts that must be defined before implementation</interface_dependencies>
        <infrastructure_dependencies>Environment or deployment requirements</infrastructure_dependencies>
      </dependency_types>
      
      <resolution_strategies>
        <stub_interfaces>Create interface stubs to unblock dependent work</stub_interfaces>
        <mock_services>Use mocked services for early integration testing</mock_services>
        <feature_flags>Use feature flags to deploy incomplete features safely</feature_flags>
        <incremental_delivery>Break large dependencies into smaller, deliverable pieces</incremental_delivery>
      </resolution_strategies>
    </dependency_mapping>
    
    <complexity_estimation>
      <story_point_scale>
        <small_1_3>Simple tasks with clear requirements and low risk</small_1_3>
        <medium_5_8>Moderate complexity with some unknowns or integration points</medium_5_8>
        <large_13_21>Complex tasks with significant unknowns or high integration complexity</large_13_21>
        <extra_large_34_plus>Very complex tasks requiring research or major architectural changes</extra_large_34_plus>
      </story_point_scale>
      
      <estimation_factors>
        <technical_complexity>Algorithm complexity, integration points, performance requirements</technical_complexity>
        <domain_complexity>Business logic complexity, edge cases, validation rules</domain_complexity>
        <risk_factors>Unknown requirements, external dependencies, timeline constraints</risk_factors>
        <team_familiarity>Experience with technologies, domain knowledge, previous similar work</team_familiarity>
      </estimation_factors>
      
      <calibration_data>
        <historical_reference>Use completed similar tasks as estimation baseline</historical_reference>
        <team_velocity>Consider team capacity and historical delivery rates</team_velocity>
        <uncertainty_buffer>Add buffer for unknown requirements and integration challenges</uncertainty_buffer>
        <learning_curve>Account for time needed to learn new technologies or domains</learning_curve>
      </calibration_data>
    </complexity_estimation>
    
    <github_integration>
      <issue_structure>
        <epic_issue>
          <title>Epic: [Feature Name] - Complete Implementation</title>
          <content>
            ## Overview
            [High-level description and business value]
            
            ## Components
            - [ ] Frontend: [Component description] - Assigned to @frontend-agent
            - [ ] Backend: [Component description] - Assigned to @backend-agent
            - [ ] Database: [Component description] - Assigned to @database-agent
            - [ ] Infrastructure: [Component description] - Assigned to @devops-agent
            
            ## Dependencies
            [Critical path and blocking relationships]
            
            ## Success Criteria
            [Measurable outcomes and acceptance criteria]
            
            ## Estimated Effort
            Total: [X] story points across [Y] components
          </content>
        </epic_issue>
        
        <component_issues>
          <title>[Component]: [Specific functionality] - [Story Points]</title>
          <content>
            ## Description
            [Detailed component requirements]
            
            ## Acceptance Criteria
            - [ ] [Specific, testable criterion 1]
            - [ ] [Specific, testable criterion 2]
            - [ ] [Specific, testable criterion 3]
            
            ## Dependencies
            - Blocks: [List of issues that depend on this]
            - Blocked by: [List of issues this depends on]
            
            ## Technical Notes
            [Implementation guidance and constraints]
            
            ## Definition of Done
            - [ ] Implementation complete
            - [ ] Tests written and passing
            - [ ] Code reviewed and approved
            - [ ] Documentation updated
            - [ ] Integrated and deployed
          </content>
        </component_issues>
      </issue_structure>
      
      <linking_strategy>
        <parent_child_links>Epic issue contains child component issues</parent_child_links>
        <dependency_references>Issues reference their dependencies explicitly</dependency_references>
        <milestone_tracking>Component issues linked to delivery milestones</milestone_tracking>
        <label_taxonomy>Consistent labeling for component types and priorities</label_taxonomy>
      </linking_strategy>
    </github_integration>
    
    <success_metrics>
      <breakdown_accuracy>
        <estimation_variance>Actual vs estimated effort within 25% variance</estimation_variance>
        <dependency_prediction>Predicted dependencies match actual blocking relationships</dependency_prediction>
        <scope_stability>Minimal scope changes after breakdown completion</scope_stability>
        <timeline_accuracy>Delivery timelines met within planned buffers</timeline_accuracy>
      </breakdown_accuracy>
      
      <quality_metrics>
        <integration_success>Components integrate without major rework</integration_success>
        <rework_percentage>Less than 15% rework due to breakdown inadequacy</rework_percentage>
        <defect_rate>Lower defect rates due to better upfront analysis</defect_rate>
        <stakeholder_satisfaction>Delivered features meet stakeholder expectations</stakeholder_satisfaction>
      </quality_metrics>
      
      <process_metrics>
        <breakdown_speed>Complete breakdown within 30 minutes for typical features</breakdown_speed>
        <team_understanding>Team clarity on deliverables and dependencies</team_understanding>
        <coordination_efficiency>Reduced coordination overhead during implementation</coordination_efficiency>
        <knowledge_retention>Breakdown artifacts useful for future similar work</knowledge_retention>
      </process_metrics>
    </success_metrics>
  </enhanced_task_breakdown>
  
  <enforcement_verification>
    <purpose>Ensure deterministic multi-agent coordination through verifiable checkpoints</purpose>
    
    <verification_protocol>
      <pre_execution_verification>
        <verify_session>GitHub session exists and is accessible by all agents</verify_session>
        <verify_worktrees>All agent worktrees created successfully</verify_worktrees>
        <verify_registry>Decision registry initialized at .claude/swarm-decisions/</verify_registry>
        <verify_dependencies>Agent dependency order clearly established</verify_dependencies>
      </pre_execution_verification>
      
      <during_execution_verification>
        <agent_critical_thinking>
          Each agent MUST document critical thinking for key decisions:
          - Why this approach over alternatives?
          - What are the downstream consequences?
          - How does this align with previous agent decisions?
          - What constraints am I imposing on subsequent agents?
        </agent_critical_thinking>
        <decision_propagation>
          Agents MUST check decision registry before implementation
          New decisions MUST be written to registry immediately
          Conflicts MUST trigger coordination protocol
        </decision_propagation>
      </during_execution_verification>
      
      <post_execution_verification>
        <decision_completeness>All agents have documented required decisions</decision_completeness>
        <acknowledgment_completeness>All decisions have required acknowledgments</acknowledgment_completeness>
        <implementation_consistency>Code matches documented decisions</implementation_consistency>
        <no_orphaned_decisions>Every decision is either implemented or explicitly deferred</no_orphaned_decisions>
      </post_execution_verification>
    </verification_protocol>
    
    <enforcement_gates>
      <gate name="session_creation" blocking="true">
        <condition>GitHub session must exist before any agent work</condition>
        <failure_action>ABORT - Cannot coordinate without session</failure_action>
      </gate>
      <gate name="worktree_isolation" blocking="true">
        <condition>Each agent has dedicated worktree</condition>
        <failure_action>ABORT - Cannot ensure parallel execution safety</failure_action>
      </gate>
      <gate name="decision_registry" blocking="true">
        <condition>Registry accessible and initialized</condition>
        <failure_action>ABORT - Cannot coordinate decisions</failure_action>
      </gate>
      <gate name="agent_tdd_enforcement" blocking="true">
        <condition>All agents follow TDD enforcement per quality/tdd-enforcement.md</condition>
        <failure_action>BLOCK - TDD violations prevent agent progression</failure_action>
      </gate>
      <gate name="cross_agent_security" blocking="true">
        <condition>Security verification across all agent boundaries</condition>
        <failure_action>BLOCK - Security violations prevent integration</failure_action>
      </gate>
      <gate name="swarm_performance" blocking="true">
        <condition>Integrated system meets performance benchmarks</condition>
        <failure_action>BLOCK - Performance violations prevent deployment</failure_action>
      </gate>
      <gate name="swarm_quality_verification" blocking="true">
        <condition>All agents pass comprehensive quality gates</condition>
        <failure_action>BLOCK - Quality violations prevent completion</failure_action>
      </gate>
      <gate name="critical_thinking" blocking="false">
        <condition>Each agent documents thinking process</condition>
        <failure_action>WARN - Proceed but flag for review</failure_action>
      </gate>
      <gate name="decision_consistency" blocking="true">
        <condition>No conflicting decisions in final merge</condition>
        <failure_action>ROLLBACK - Must resolve conflicts first</failure_action>
      </gate>
    </enforcement_gates>
  </enforcement_verification>
  
  <context_transfer_validation>
    <purpose>Ensure complete and accurate context transfer between agents</purpose>
    
    <context_components>
      <decision_context>
        <format>JSON registry at .claude/swarm-decisions/session-[id].json</format>
        <required_fields>
          - decision_id: Unique identifier (e.g., AUTH_001)
          - decision: One-line summary
          - owner: Agent who made decision
          - rationale: Why this decision
          - impacts: Which agents affected
          - constraints: Technical limitations imposed
          - immutable: Can this be changed?
          - timestamp: When decided
          - acknowledgments: List of agents who acknowledged
        </required_fields>
      </decision_context>
      
      <technical_context>
        <shared_constants>API endpoints, data models, security policies</shared_constants>
        <shared_interfaces>Contract definitions between components</shared_interfaces>
        <shared_dependencies>Common libraries, frameworks, tools</shared_dependencies>
      </technical_context>
      
      <progress_context>
        <session_updates>Regular progress posts to GitHub session</session_updates>
        <milestone_tracking>Completion status of major deliverables</milestone_tracking>
        <blocker_communication>Immediate escalation of blocking issues</blocker_communication>
      </progress_context>
    </context_components>
    
    <transfer_mechanisms>
      <decision_registry_file>
        <location>.claude/swarm-decisions/session-[id].json</location>
        <format>JSON with schema validation</format>
        <access>Read by all agents, write by decision owner</access>
        <versioning>Append-only with timestamp tracking</versioning>
      </decision_registry_file>
      
      <session_artifacts>
        <location>GitHub session comments and artifacts</location>
        <format>Structured markdown with decision tables</format>
        <access>All agents can read and comment</access>
        <notification>Agents tagged when decisions affect them</notification>
      </session_artifacts>
      
      <worktree_handoff>
        <mechanism>Shared branches with clear ownership</mechanism>
        <validation>No direct commits to other agent branches</validation>
        <integration>Pull requests for cross-agent changes</integration>
      </worktree_handoff>
    </transfer_mechanisms>
    
    <validation_rules>
      <rule name="decision_before_implementation">
        No implementation without documented decision
      </rule>
      <rule name="acknowledgment_before_proceeding">
        Agents must acknowledge decisions that impact them
      </rule>
      <rule name="conflict_escalation">
        Decision conflicts must be resolved through session
      </rule>
      <rule name="immutable_enforcement">
        IMMUTABLE decisions cannot be changed without full team consensus
      </rule>
      <rule name="audit_trail">
        All decisions and acknowledgments must be timestamped
      </rule>
    </validation_rules>
  </context_transfer_validation>
  
  <shared_decision_registry>
    <purpose>Coordinate architectural decisions between agents to prevent conflicts and ensure consistent implementation</purpose>
    
    <decision_precedence_order>
      <agent_order>
        <priority_1>Security Expert - defines authentication, authorization, security models</priority_1>
        <priority_2>Backend Developer - acknowledges security, defines data models and APIs</priority_2>
        <priority_3>Frontend Developer - acknowledges security + backend, defines UI contracts</priority_3>
        <priority_4>DevOps Engineer - acknowledges all decisions, implements deployment</priority_4>
      </agent_order>
    </decision_precedence_order>
    
    <decision_artifact_format>
      <template>
        DECISION_ID: [domain]_[number] (e.g., AUTH_001, DB_003, API_007)
        DECISION: [one line summary]
        OWNER: [agent responsible]
        RATIONALE: [why this choice was made]
        IMPACTS: [which agents must follow this]
        ACKNOWLEDGMENTS: [agents that have confirmed understanding]
        IMMUTABLE: [true/false - can this be changed]
      </template>
    </decision_artifact_format>
    
    <coordination_protocol>
      <security_first_rule>
        <requirement>Security Expert documents ALL authentication and authorization decisions FIRST</requirement>
        <output_format>SECURITY_DECISIONS_DOCUMENTED:
          - AUTH_001: JWT with RSA-256 asymmetric signing
          - AUTH_002: OAuth2 + OpenID Connect for SSO
          - SEC_001: RBAC with hierarchical permissions</output_format>
      </security_first_rule>
      
      <acknowledgment_protocol>
        <requirement>Each subsequent agent MUST acknowledge previous decisions before implementing</requirement>
        <output_format>DECISION_ACKNOWLEDGMENTS:
          - Backend: ACKNOWLEDGED AUTH_001, AUTH_002, SEC_001
          - Frontend: ACKNOWLEDGED ALL BACKEND + SECURITY decisions
          - DevOps: ACKNOWLEDGED ALL PREVIOUS decisions</output_format>
      </acknowledgment_protocol>
      
      <conflict_resolution>
        <trigger>When agent cannot implement previous decision</trigger>
        <protocol>
          1. Document specific conflict with previous decision
          2. Propose alternative with technical justification
          3. Escalate to session for resolution
          4. Update decision registry with resolution
        </protocol>
      </conflict_resolution>
    </coordination_protocol>
    
    <decision_categories>
      <authentication>AUTH_* - login methods, session management, token handling</authentication>
      <authorization>AUTHZ_* - permissions, RBAC, access control</authorization>
      <data_models>DB_* - database schema, data relationships, migrations</data_models>
      <api_contracts>API_* - endpoint design, request/response formats</api_contracts>
      <security_policies>SEC_* - security requirements, threat mitigations</security_policies>
      <performance_specs>PERF_* - response times, scalability requirements</performance_specs>
      <deployment>DEPLOY_* - infrastructure, CI/CD, monitoring</deployment>
    </decision_categories>
  </shared_decision_registry>

  <agent_patterns>
    <task_pattern>
      <description>Heterogeneous work requiring different specialized skills WITH decision coordination</description>
      <usage>Task("Security Expert", "Document security architecture decisions FIRST: auth_method, security_model, threat_mitigations")</usage>
      <usage>Task("Backend Developer", "Implement API acknowledging SECURITY decisions: AUTH_001, SEC_001")</usage>
      <usage>Task("Frontend Developer", "Build components acknowledging SECURITY + BACKEND decisions")</usage>
      <usage>Task("DevOps Engineer", "Deploy infrastructure acknowledging ALL architectural decisions")</usage>
      <coordination>All Task() calls in ONE message with explicit decision acknowledgment requirements</coordination>
    </task_pattern>
    <batch_pattern>
      <description>Homogeneous work distributed in parallel</description>
      <usage>Batch(["Refactor UserService to SOLID principles", "Refactor ProductService to SOLID principles"])</usage>
      <coordination>Single Batch() call for similar operations across multiple targets</coordination>
    </batch_pattern>
    <prompt_evaluation_pattern>
      <description>Comprehensive prompt engineering evaluation using specialized agents</description>
      <usage>Task("Prompt Engineer", "Evaluate prompt clarity and specificity metrics")</usage>
      <usage>Task("Quality Specialist", "Assess robustness and error handling")</usage>
      <usage>Task("Performance Analyst", "Benchmark effectiveness and response quality")</usage>
      <coordination>Parallel evaluation from multiple expert perspectives in single message</coordination>
    </prompt_evaluation_pattern>
  </agent_patterns>
  
  <concrete_implementations>
    <git_worktree_task_pattern>
      <description>ACTUAL Claude Code implementation with git worktree isolation</description>
      <implementation>
        ```bash
        # CRITICAL: Create worktrees BEFORE Task() execution
        prepare_swarm_worktrees() {
          local session_id="$1"
          local agents=("frontend" "backend" "devops" "security")
          
          for agent in "${agents[@]}"; do
            local worktree_dir="../worktrees/swarm-${session_id}-${agent}"
            git worktree add "$worktree_dir" -b "swarm/${session_id}/${agent}" origin/main
            echo "✅ Worktree created for $agent: $worktree_dir"
          done
        }
        
        # ACTUAL NATIVE CLAUDE CODE TASK() IMPLEMENTATION
        # Execute ALL Task() calls in ONE message for 70% performance gain
        execute_swarm_with_worktrees() {
          local session_id="$1"
          
          # First create worktrees
          prepare_swarm_worktrees "$session_id"
          
          # Then execute Task() with worktree paths
          # ALL IN ONE MESSAGE FOR TRUE PARALLELISM:
          Task("frontend", {
            objective: "Build React dashboard with real-time updates",
            workspace: "../worktrees/swarm-${session_id}-frontend",
            specifications: {
              framework: "React 18 with TypeScript",
              state: "Redux Toolkit with RTK Query",
              ui: "Material-UI v5 with dark mode"
            }
          })
          
          Task("backend", {
            objective: "Create FastAPI microservices with async operations",
            workspace: "../worktrees/swarm-${session_id}-backend",
            specifications: {
              framework: "FastAPI with Pydantic v2",
              database: "PostgreSQL with asyncpg",
              auth: "OAuth2 with JWT tokens"
            }
          })
          
          Task("devops", {
            objective: "Deploy Kubernetes infrastructure with GitOps",
            workspace: "../worktrees/swarm-${session_id}-devops",
            specifications: {
              orchestration: "Kubernetes with Helm charts",
              ci_cd: "ArgoCD with GitHub Actions",
              monitoring: "Prometheus + Grafana stack"
            }
          })
          
          Task("security", {
            objective: "Implement zero-trust security architecture",
            workspace: "../worktrees/swarm-${session_id}-security",
            specifications: {
              auth: "Keycloak with RBAC",
              secrets: "HashiCorp Vault integration",
              scanning: "OWASP ZAP + Trivy"
            }
          })
        }
        ```
      </implementation>
      <critical_benefits>
        - Each agent works in ISOLATED git worktree preventing conflicts
        - TRUE parallel execution with 70% latency reduction
        - Clean merge process after agent completion
        - No workspace pollution between agents
      </critical_benefits>
    </git_worktree_task_pattern>
    
    <native_batch_implementation>
      <description>ACTUAL Batch() implementation for homogeneous work</description>
      <implementation>
        ```javascript
        // SECURITY IMPORTS: Use secure subprocess execution
        const { execFile } = require('child_process');
        const { promisify } = require('util');
        const execFileAsync = promisify(execFile);
        
        // SECURITY FUNCTION: Sanitize service names to prevent injection attacks
        function sanitizeServiceName(service) {
          // Only allow alphanumeric characters, hyphens, and underscores
          // This prevents shell injection through service names
          const sanitized = service.replace(/[^a-zA-Z0-9\-_]/g, '');
          
          // Ensure the sanitized name is not empty and has reasonable length
          if (!sanitized || sanitized.length === 0 || sanitized.length > 50) {
            return null;
          }
          
          // Prevent directory traversal attempts
          if (sanitized.includes('..') || sanitized.startsWith('-')) {
            return null;
          }
          
          return sanitized;
        }
        
        // NATIVE BATCH() WITH WORKTREE PREPARATION - SECURITY HARDENED
        async function executeBatchRefactoring(services) {
          // Prepare worktrees for batch operations
          const worktrees = await Promise.all(
            services.map(async (service) => {
              // SECURITY: Validate and sanitize service name to prevent code injection
              const sanitizedService = sanitizeServiceName(service);
              if (!sanitizedService) {
                throw new Error(`Invalid service name: ${service}`);
              }
              
              const worktreePath = `../worktrees/batch-refactor-${sanitizedService.toLowerCase()}`;
              const branchName = `refactor/${sanitizedService}`;
              
              // SECURITY: Use subprocess.execFile with array arguments to prevent injection
              await execFileAsync('git', ['worktree', 'add', worktreePath, '-b', branchName]);
              return { service: sanitizedService, worktreePath };
            })
          );
          
          // ACTUAL BATCH() CALL - ALL IN ONE MESSAGE
          const results = await Batch(
            worktrees.map(({ service, worktreePath }) => ({
              task: `Refactor ${service} to SOLID principles`,
              workspace: worktreePath,
              requirements: {
                principles: ["SRP", "OCP", "LSP", "ISP", "DIP"],
                testing: "Maintain 95% coverage with TDD",
                documentation: "Update API docs and architecture diagrams"
              }
            }))
          );
          
          // Results available in parallel - 85% faster than sequential
          return results;
        }
        ```
      </implementation>
      <performance_gains>
        - 85% faster than sequential refactoring
        - Consistent approach across all services
        - Isolated worktrees prevent cross-contamination
        - Automatic progress tracking in session
        - Security hardened against code injection attacks
        - Input validation prevents malicious service names
      </performance_gains>
    </native_batch_implementation>
    
    <error_recovery_integration>
      <description>Multi-agent work with integrated error recovery</description>
      <implementation>
        ```javascript
        // MULTI-AGENT WITH ERROR RECOVERY PATTERNS
        async function executeResilientSwarm(objective, session) {
          try {
            // Primary: Full multi-agent coordination
            const agents = await Promise.all([
              Task("frontend", { objective, fallback: "simplified_ui" }),
              Task("backend", { objective, fallback: "monolithic_api" }),
              Task("database", { objective, fallback: "single_postgres" })
            ]);
            
            return { success: true, mode: "full_swarm", results: agents };
            
          } catch (swarmError) {
            // Tier 2 Recovery: Sequential with reduced scope
            console.warn("Swarm failed, attempting sequential execution");
            
            try {
              const sequential = [];
              for (const agent of ["frontend", "backend", "database"]) {
                const result = await Task(agent, {
                  objective: simplifyObjective(objective),
                  mode: "degraded",
                  timeout: 300000 // 5 minute timeout
                });
                sequential.push(result);
              }
              
              return { success: true, mode: "sequential_recovery", results: sequential };
              
            } catch (sequentialError) {
              // Tier 3 Recovery: Single generalist agent
              console.error("Sequential failed, using generalist agent");
              
              const generalist = await Task("full-stack", {
                objective: createMVPObjective(objective),
                mode: "emergency",
                constraints: ["minimal_viable_product", "core_features_only"]
              });
              
              return { success: true, mode: "generalist_recovery", results: [generalist] };
            }
          }
        }
        ```
      </implementation>
      <resilience_features>
        - Automatic fallback from swarm → sequential → generalist
        - Graceful degradation maintains core functionality
        - Error tracking through session for analysis
        - Recovery patterns from error-recovery.md integrated
      </resilience_features>
    </error_recovery_integration>
  </concrete_implementations>
  
  <security_hardening>
    <code_injection_prevention>
      <vulnerability_description>
        Previous implementation used exec() with string concatenation, allowing code injection
        through malicious service names (e.g., "; rm -rf /; echo ")
      </vulnerability_description>
      <security_measures>
        1. Input sanitization: Only allow alphanumeric chars, hyphens, underscores
        2. Length validation: Prevent excessively long inputs
        3. Directory traversal prevention: Block ".." and leading "-" characters
        4. Secure subprocess execution: Use execFile() with array arguments
        5. Error handling: Fail fast on invalid inputs with clear error messages
      </security_measures>
      <validation_requirements>
        ALL user inputs MUST be validated before subprocess execution
        NO string concatenation in shell commands - use array arguments only
        Service names MUST match pattern: /^[a-zA-Z0-9\-_]{1,50}$/
      </validation_requirements>
    </code_injection_prevention>
  </security_hardening>
  
  <critical_integration_requirements>
    <git_worktree_mandatory>
      ALL multi-agent work MUST use git worktrees for isolation
      Worktrees created BEFORE Task() execution begins
      Naming convention: ../worktrees/swarm-{session}-{agent}
      Automatic cleanup after merge completion
    </git_worktree_mandatory>
    <error_recovery_mandatory>
      ALL multi-agent patterns MUST integrate error recovery
      Use 4-tier recovery from quality/error-recovery.md
      Session tracking for recovery metrics
      Graceful degradation for system resilience
    </error_recovery_mandatory>
    <performance_tracking_mandatory>
      ALL executions MUST track performance metrics
      Verify 70% latency reduction for parallel execution
      Document actual vs theoretical performance
      Optimize based on measured results
    </performance_tracking_mandatory>
  </critical_integration_requirements>
  
  <specialized_roles>
    <system_architect>
      Expertise: Overall system design, technology decisions, integration patterns
      Deliverables: Architecture documentation, technology recommendations, integration specs
      <critical_thinking_requirements>
        - Evaluate 3+ architectural patterns before deciding
        - Map downstream impacts of technology choices
        - Challenge assumptions about scalability needs
        - Document trade-offs explicitly
      </critical_thinking_requirements>
    </system_architect>
    <security_specialist>
      Expertise: Threat modeling, vulnerability assessment, compliance implementation
      Deliverables: Security documentation, threat models, compliance reports
      <critical_thinking_requirements>
        - Assume breach and design accordingly
        - Challenge trust boundaries systematically
        - Evaluate attack vectors beyond OWASP Top 10
        - Document security decisions as IMMUTABLE by default
      </critical_thinking_requirements>
    </security_specialist>
    <performance_engineer>
      Expertise: Optimization, scalability analysis, benchmarking
      Deliverables: Performance reports, optimization recommendations, scalability plans
      <critical_thinking_requirements>
        - Measure before optimizing - no assumptions
        - Challenge perceived vs actual bottlenecks
        - Consider optimization trade-offs (time/space/complexity)
        - Document performance constraints for other agents
      </critical_thinking_requirements>
    </performance_engineer>
    <frontend_architect>
      Expertise: UI/UX implementation, client-side optimization, responsive design
      Deliverables: UI components, frontend architecture, user experience flows
      <critical_thinking_requirements>
        - Challenge UI patterns for accessibility
        - Question component boundaries and reusability
        - Evaluate state management complexity
        - Document UI decisions impacting backend APIs
      </critical_thinking_requirements>
    </frontend_architect>
    <backend_engineer>
      Expertise: Server-side logic, API design, database integration
      Deliverables: Backend services, API documentation, database schemas
      <critical_thinking_requirements>
        - Challenge data model assumptions
        - Evaluate consistency vs availability trade-offs
        - Question API design for future extensibility
        - Document decisions affecting frontend and DevOps
      </critical_thinking_requirements>
    </backend_engineer>
    <devops_engineer>
      Expertise: Infrastructure, deployment, monitoring, CI/CD
      Deliverables: Infrastructure code, deployment pipelines, monitoring systems
      <critical_thinking_requirements>
        - Challenge deployment complexity vs benefits
        - Evaluate failure modes and recovery paths
        - Question monitoring coverage and alert fatigue
        - Document infrastructure constraints for development
      </critical_thinking_requirements>
    </devops_engineer>
    <prompt_engineer>
      Expertise: AI prompt design, evaluation frameworks, testing methodologies
      Deliverables: Optimized prompts, evaluation reports, testing frameworks
      <critical_thinking_requirements>
        - Challenge prompt assumptions with edge cases
        - Evaluate robustness across model variations
        - Question evaluation metrics validity
        - Document prompt constraints and limitations
      </critical_thinking_requirements>
    </prompt_engineer>
  </specialized_roles>
  
  <coordination_rules>
    <decision_based_coordination>
      Agent independence maintained through shared decision registry
      Security decisions established FIRST before any implementation
      Subsequent agents acknowledge previous decisions before proceeding  
      Conflicts resolved through explicit escalation protocol
    </decision_based_coordination>
    <session_communication>
      All agents access same session for shared context and decisions
      Decision registry maintained in session with artifact format
      Progress updates include decision acknowledgment status
      Blocking issues escalated through session for team coordination
      Architectural decisions recorded as immutable artifacts
    </session_communication>
    <parallel_execution_with_decisions>
      All Task() calls execute in parallel after decision documentation
      Security Expert runs first to establish decision foundation
      Other agents proceed in parallel acknowledging security decisions
      Decision consistency verified before final merge
    </parallel_execution_with_decisions>
  </coordination_rules>
  
  <quality_assurance>
    <individual_responsibility>
      Each agent responsible for TDD enforcement per quality/tdd-enforcement.md
      Security verification required per quality/security-gate-verification.md
      Performance benchmarks validated per quality/performance-gates.md
      Comprehensive quality gates per quality/gate-verification.md for all deliverables
    </individual_responsibility>
    <integration_coordination>
      Integration testing validates compatibility between agent outputs
      Cross-agent quality gate verification ensures consistent standards
      End-to-end performance testing confirms system meets p95 <200ms
      Security validation across all agent boundaries and interfaces
      Comprehensive quality evidence collection for audit trail
    </integration_coordination>
    <swarm_level_gates>
      <gate name="agent_tdd_compliance" requirement="All agents complete TDD cycles with evidence" blocking="true"/>
      <gate name="cross_agent_security" requirement="Security verification across agent boundaries" blocking="true"/>
      <gate name="integrated_performance" requirement="System performance meets benchmarks" blocking="true"/>
      <gate name="swarm_quality_verification" requirement="All agents pass comprehensive quality gates" blocking="true"/>
    </swarm_level_gates>
  </quality_assurance>
  
  <session_integration>
    <mandatory_creation>
      All multi-agent work automatically creates GitHub session
      Session provides coordination hub for agent communication
      Progress tracking enables visibility into parallel work streams
    </mandatory_creation>
    <session_documentation>
      Agent assignments and specialized responsibilities
      Progress milestones and completion status tracking
      Architectural decisions requiring cross-agent coordination
      Integration results and quality verification outcomes
    </session_documentation>
  </session_integration>
  
  <integration_points>
    <depends_on>
      patterns/session-management.md for automatic session creation
      patterns/pattern-library.md for proven execution patterns
      quality/tdd-enforcement.md for non-bypassable TDD enforcement across agents
      quality/security-gate-verification.md for cross-agent security verification
      quality/performance-gates.md for swarm-level performance benchmarking
      quality/gate-verification.md for comprehensive quality orchestration
      development/task-management.md for quality standards enforcement
      development/prompt-engineering.md for prompt evaluation workflows
      debugging/reproduce-issue.md for systematic debugging coordination
    </depends_on>
    <provides_to>
      patterns/intelligent-routing.md for multi-agent escalation triggers
      development/prompt-engineering.md for parallel evaluation execution
      planning/feature-workflow.md for enhanced task breakdown capabilities
      patterns/session-management.md for complex project coordination
      All commands for parallel execution coordination patterns
    </provides_to>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">parallel_execution</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">batch_operations</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">issue_tracking</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">consequence_mapping</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">three_x_rule</uses_pattern>
    <implementation_notes>
      Task() and Batch() patterns leverage parallel_execution for 70% performance improvement
      Batch() operations follow batch_operations pattern for 50% API call reduction
      GitHub session creation follows issue_tracking pattern for 100% completion rate
      Agent independence validated through consequence_mapping pattern
      Pattern selection follows three_x_rule for thorough analysis before execution
    </implementation_notes>
  </pattern_usage>
  
  <deterministic_execution_flow>
    <purpose>Ensure predictable and verifiable multi-agent coordination</purpose>
    
    <execution_sequence enforcement="MANDATORY">
      <step order="1" gate="session_creation">
        <action>Create GitHub session with multi-agent labels</action>
        <verification>Session ID returned and accessible</verification>
        <critical_thinking>Is single session sufficient or do we need component sub-sessions?</critical_thinking>
      </step>
      
      <step order="2" gate="agent_assignment">
        <action>Assign agents with explicit precedence order</action>
        <verification>Each agent has clear responsibilities and decision scope</verification>
        <critical_thinking>Have we identified all necessary expertise areas?</critical_thinking>
      </step>
      
      <step order="3" gate="registry_initialization">
        <action>Initialize decision registry at .claude/swarm-decisions/session-[id].json</action>
        <verification>Registry file created with proper schema</verification>
        <critical_thinking>Are all decision categories represented in schema?</critical_thinking>
      </step>
      
      <step order="4" gate="worktree_creation">
        <action>Create isolated worktrees for each agent</action>
        <verification>All worktrees accessible at ../worktrees/swarm-*</verification>
        <critical_thinking>Is worktree isolation necessary for this task complexity?</critical_thinking>
      </step>
      
      <step order="5" gate="security_decisions">
        <action>Security Expert documents all security decisions FIRST</action>
        <verification>AUTH_*, SEC_*, AUTHZ_* decisions in registry</verification>
        <critical_thinking>Have we covered all security attack vectors?</critical_thinking>
      </step>
      
      <step order="6" gate="parallel_execution">
        <action>Execute all other agents in parallel with decision acknowledgment</action>
        <verification>All Task() calls include decision dependencies</verification>
        <critical_thinking>Are agents truly independent or do we need sequencing?</critical_thinking>
      </step>
      
      <step order="7" gate="decision_verification">
        <action>Verify all decisions documented and acknowledged</action>
        <verification>No orphaned or conflicting decisions</verification>
        <critical_thinking>Do implementations match documented decisions?</critical_thinking>
      </step>
      
      <step order="8" gate="integration_merge">
        <action>Merge all agent work with consistency checks</action>
        <verification>No conflicts, all tests pass, decisions honored</verification>
        <critical_thinking>Is the integrated system coherent and maintainable?</critical_thinking>
      </step>
      
      <step order="9" gate="cleanup">
        <action>Clean up worktrees and finalize session</action>
        <verification>Worktrees removed, session marked complete</verification>
        <critical_thinking>Have we captured reusable patterns for future work?</critical_thinking>
      </step>
    </execution_sequence>
    
    <determinism_guarantees>
      <guarantee name="decision_ordering">
        Security decisions always precede implementation decisions
      </guarantee>
      <guarantee name="conflict_prevention">
        Decision precedence prevents architectural conflicts
      </guarantee>
      <guarantee name="audit_trail">
        Every decision and acknowledgment is timestamped
      </guarantee>
      <guarantee name="rollback_capability">
        Failed merges can be rolled back to last consistent state
      </guarantee>
      <guarantee name="verification_gates">
        Each step has explicit verification before proceeding
      </guarantee>
    </determinism_guarantees>
    
    <failure_modes>
      <mode name="session_failure">
        Recovery: Retry session creation or abort
      </mode>
      <mode name="worktree_conflict">
        Recovery: Clean and recreate worktrees
      </mode>
      <mode name="decision_conflict">
        Recovery: Escalate through session for resolution
      </mode>
      <mode name="merge_failure">
        Recovery: Rollback and re-execute affected agents
      </mode>
      <mode name="timeout">
        Recovery: Apply 4-tier degradation strategy
      </mode>
    </failure_modes>
  </deterministic_execution_flow>
  
</module>
```