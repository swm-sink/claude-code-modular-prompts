| version | last_updated | status |
|---------|--------------|--------|
| 2.6.0   | 2025-07-08   | stable |

# /feature - SOAR/CLEAR autonomous feature development with strategic planning

────────────────────────────────────────────────────────────────────────────────

**PURPOSE**: Autonomous feature development with SOAR/CLEAR framework integration for strategic planning and comprehensive execution

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Autonomous PRD-driven feature development with SOAR/CLEAR framework orchestration">
  
  <delegation target="modules/planning/feature-workflow.md">
    SOAR strategic planning → CLEAR comprehensive requirements → Generate PRD → Analyze complexity → Plan MVP → Execute autonomously → Validate
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/critical-thinking-pattern.md">Strategic analysis and decision-making</uses_pattern>
    <uses_pattern from="patterns/research-analysis-pattern.md">Context analysis before development</uses_pattern>
    <uses_pattern from="patterns/tdd-cycle-pattern.md">Test-driven feature development</uses_pattern>
    <uses_pattern from="patterns/implementation-pattern.md">Autonomous feature implementation</uses_pattern>
    <uses_pattern from="patterns/quality-validation-pattern.md">Feature validation and testing</uses_pattern>
    <uses_pattern from="patterns/integration-pattern.md">System integration coordination</uses_pattern>
    <uses_pattern from="patterns/documentation-pattern.md">PRD generation and documentation</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Apply SOAR framework - Analyze Situation and context</action>
      <critical_thinking>
        - What is the current situation requiring this feature development?
        - What business context and user needs drive this feature request?
        - What technical constraints and opportunities exist in the current system?
        - How does this feature align with overall product strategy and vision?
        - What contextual factors influence the strategic approach to this feature?
      </critical_thinking>
      <output_format>SOAR_SITUATION_ANALYSIS: 
        - Business context: [business_driver]
        - User needs: [user_requirements]
        - Technical landscape: [system_constraints_and_opportunities]
        - Strategic alignment: [product_vision_alignment]</output_format>
      <validation>Situation comprehensively analyzed with strategic context understanding</validation>
      <enforcement>BLOCK if situation analysis insufficient for strategic feature planning</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Apply SOAR framework - Define Objectives with strategic goals</action>
      <critical_thinking>
        - What are the specific strategic objectives this feature should achieve?
        - How do these objectives align with broader business goals and OKRs?
        - What success metrics and KPIs will validate feature achievement?
        - What are the primary, secondary, and stretch objectives for this feature?
        - How do objectives guide technical and design decision-making?
      </critical_thinking>
      <output_format>SOAR_OBJECTIVES_DEFINITION:
        - Primary objective: [core_goal_with_metrics]
        - Secondary objectives: [supporting_goals]
        - Success criteria: [measurable_outcomes]
        - Business alignment: [okr_and_strategic_connection]</output_format>
      <validation>Objectives clearly defined with measurable success criteria and strategic alignment</validation>
      <enforcement>BLOCK if objectives lack clarity, metrics, or strategic connection</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Apply SOAR framework - Plan Actions and strategic execution</action>
      <critical_thinking>
        - What strategic actions are required to achieve the defined objectives?
        - How should development phases be structured for optimal strategic value delivery?
        - What resource allocation and timeline support objective achievement?
        - What action priorities maximize strategic impact and minimize risk?
        - How do actions connect situation analysis to desired results?
      </critical_thinking>
      <output_format>SOAR_ACTION_PLAN:
        - Strategic phases: [development_phases_with_strategic_value]
        - Resource requirements: [timeline_and_allocation]
        - Priority actions: [critical_path_activities]
        - Risk mitigation: [strategic_risk_actions]</output_format>
      <validation>Action plan strategically sound with clear phase structure and resource planning</validation>
      <enforcement>BLOCK if action plan lacks strategic coherence or feasibility assessment</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Apply SOAR framework - Define Results and strategic outcomes</action>
      <critical_thinking>
        - What strategic results will validate successful feature delivery?
        - How will results be measured and validated against objectives?
        - What downstream impacts and benefits are expected from the feature?
        - How do results connect back to situation analysis and business context?
        - What learning and improvement opportunities emerge from expected results?
      </critical_thinking>
      <output_format>SOAR_RESULTS_FRAMEWORK:
        - Expected outcomes: [strategic_benefits_and_impact]
        - Measurement plan: [validation_approach_and_metrics]
        - Success validation: [objective_fulfillment_criteria]
        - Learning opportunities: [improvement_and_iteration_potential]</output_format>
      <validation>Results framework aligned with objectives and provides clear success validation</validation>
      <enforcement>BLOCK if results definition doesn't align with objectives or lacks measurement clarity</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Apply CLEAR framework - Comprehensive Context analysis</action>
      <critical_thinking>
        - What comprehensive technical context affects feature implementation?
        - What codebase patterns, architecture, and existing systems constrain design?
        - What development environment, tooling, and process context applies?
        - How does organizational context and team capability influence approach?
        - What external context (regulations, compliance, integrations) applies?
      </critical_thinking>
      <output_format>CLEAR_CONTEXT_ANALYSIS:
        - Technical context: [architecture_patterns_constraints_and_opportunities]
        - Development context: [tools_processes_and_team_capabilities]
        - Business context: [organizational_requirements_and_constraints]
        - External context: [compliance_integrations_and_dependencies]</output_format>
      <validation>Context comprehensively analyzed across all relevant dimensions</validation>
      <enforcement>BLOCK if context analysis misses critical technical or business factors</enforcement>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING">
      <action>Apply CLEAR framework - Identify Limitations and constraints</action>
      <critical_thinking>
        - What technical limitations constrain feature implementation approaches?
        - What resource limitations (time, budget, expertise) affect scope?
        - What business limitations (policies, compliance, priorities) apply?
        - What system limitations (performance, scalability, security) must be addressed?
        - How do limitations influence strategic decisions and trade-offs?
      </critical_thinking>
      <output_format>CLEAR_LIMITATIONS_ASSESSMENT:
        - Technical limitations: [system_and_architecture_constraints]
        - Resource limitations: [time_budget_and_expertise_constraints]
        - Business limitations: [policy_compliance_and_priority_constraints]
        - Risk limitations: [security_performance_and_scalability_bounds]</output_format>
      <validation>Limitations comprehensively identified with impact assessment on strategic approach</validation>
      <enforcement>BLOCK if limitation analysis incomplete or lacks strategic impact consideration</enforcement>
    </checkpoint>
    <checkpoint id="7" verify="true" enforcement="BLOCKING">
      <action>Apply CLEAR framework - Provide Examples and patterns</action>
      <critical_thinking>
        - What existing patterns and examples guide optimal implementation approach?
        - What similar features or systems provide implementation guidance?
        - What industry best practices and proven patterns apply to this feature?
        - What anti-patterns and failure examples should be avoided?
        - How do examples inform strategic technical decisions and architecture?
      </critical_thinking>
      <output_format>CLEAR_EXAMPLES_AND_PATTERNS:
        - Implementation patterns: [proven_approaches_and_architectures]
        - Industry examples: [best_practices_and_reference_implementations]
        - Codebase examples: [existing_similar_implementations]
        - Anti-patterns to avoid: [known_failure_modes_and_risks]</output_format>
      <validation>Examples and patterns provide clear implementation guidance aligned with strategic objectives</validation>
      <enforcement>BLOCK if examples insufficient to guide strategic technical decision-making</enforcement>
    </checkpoint>
    <checkpoint id="8" verify="true" enforcement="BLOCKING">
      <action>Apply CLEAR framework - Define Actions with comprehensive planning</action>
      <critical_thinking>
        - What comprehensive actions bridge analysis to implementation?
        - How do actions integrate SOAR strategic planning with CLEAR technical requirements?
        - What GitHub session structure supports comprehensive tracking and coordination?
        - How do actions address both strategic objectives and technical limitations?
        - What TDD approach aligns with comprehensive strategic and technical requirements?
      </critical_thinking>
      <output_format>CLEAR_COMPREHENSIVE_ACTIONS:
        - Implementation actions: [detailed_technical_implementation_steps]
        - Coordination actions: [github_session_and_tracking_setup]
        - Quality actions: [tdd_approach_and_validation_strategy]
        - Strategic actions: [objective_fulfillment_and_results_validation]</output_format>
      <validation>Actions comprehensively planned with strategic and technical integration</validation>
      <enforcement>BLOCK if actions don't integrate SOAR strategy with CLEAR technical requirements</enforcement>
    </checkpoint>
    <checkpoint id="9" verify="true" enforcement="BLOCKING">
      <action>Apply CLEAR framework - Role definition and execution approach</action>
      <critical_thinking>
        - What expert role and perspective optimizes feature development quality?
        - How does role definition align with strategic objectives and technical complexity?
        - What expertise level and domain knowledge supports optimal execution?
        - How does role influence decision-making, quality standards, and approaches?
        - What delegation decisions (task vs swarm) align with role capabilities and scope?
      </critical_thinking>
      <output_format>CLEAR_ROLE_AND_EXECUTION:
        - Expert role: [domain_expertise_and_perspective]
        - Quality standards: [role_appropriate_excellence_criteria]
        - Execution approach: [methodology_and_framework_integration]
        - Delegation decision: [task_vs_swarm_with_complexity_assessment]</output_format>
      <validation>Role clearly defined with execution approach optimized for strategic and technical success</validation>
      <enforcement>BLOCK if role definition insufficient for complexity or lacks strategic alignment</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <soar_framework_integration enforcement="MANDATORY">
    <situation_analysis>Comprehensive business and technical context analysis for strategic feature positioning</situation_analysis>
    <objective_definition>Clear strategic objectives with measurable success criteria and business alignment</objective_definition>
    <action_planning>Strategic development phases with resource allocation and timeline optimization</action_planning>
    <results_framework>Expected outcomes with measurement plans and success validation approaches</results_framework>
    <strategic_alignment>Feature development aligned with business objectives and product strategy</strategic_alignment>
    <validation>Reference frameworks/soar.md for complete SOAR framework implementation in feature development</validation>
  </soar_framework_integration>
  
  <clear_framework_integration enforcement="MANDATORY">
    <context_comprehension>Technical, business, and organizational context analysis for informed decision-making</context_comprehension>
    <limitation_identification>Comprehensive constraint analysis across technical, resource, and business dimensions</limitation_identification>
    <example_guidance>Industry patterns, best practices, and anti-patterns for optimal implementation approaches</example_guidance>
    <action_specification>Detailed technical actions integrating strategic objectives with implementation requirements</action_specification>
    <role_optimization>Expert role definition aligned with feature complexity and strategic objectives</role_optimization>
    <comprehensive_planning>Integration of strategic SOAR planning with detailed CLEAR technical requirements</comprehensive_planning>
    <validation>Reference frameworks/clear.md for complete CLEAR framework implementation in comprehensive feature development</validation>
  </clear_framework_integration>
  
  <enforcement_verification enforcement="REQUIRED">
    <checkpoint name="SOAR_SITUATION_ANALYSIS">
      <verify>SOAR situation analysis completed with comprehensive business and technical context</verify>
      <output>Display business context, user needs, technical landscape, and strategic alignment</output>
      <validate>Situation analysis provides strategic foundation for feature development</validate>
    </checkpoint>
    
    <checkpoint name="SOAR_OBJECTIVES_DEFINITION">
      <verify>SOAR objectives clearly defined with measurable success criteria and business alignment</verify>
      <output>Display primary objectives, success criteria, and strategic connection to business goals</output>
      <validate>Objectives provide clear direction for strategic feature development</validate>
    </checkpoint>
    
    <checkpoint name="SOAR_ACTION_PLANNING">
      <verify>SOAR action plan strategically structured with phases and resource allocation</verify>
      <output>Display strategic phases, timeline, priorities, and risk mitigation approaches</output>
      <validate>Action plan provides feasible path from situation to desired results</validate>
    </checkpoint>
    
    <checkpoint name="SOAR_RESULTS_FRAMEWORK">
      <verify>SOAR results framework defined with measurement and validation approaches</verify>
      <output>Display expected outcomes, measurement plan, and learning opportunities</output>
      <validate>Results framework enables objective validation and continuous improvement</validate>
    </checkpoint>
    
    <checkpoint name="CLEAR_CONTEXT_ANALYSIS">
      <verify>CLEAR context analysis comprehensive across technical, business, and external dimensions</verify>
      <output>Display technical context, development environment, organizational factors, and external constraints</output>
      <validate>Context analysis enables informed decision-making and optimal approach selection</validate>
    </checkpoint>
    
    <checkpoint name="CLEAR_LIMITATIONS_ASSESSMENT">
      <verify>CLEAR limitations identified across technical, resource, business, and risk dimensions</verify>
      <output>Display constraint analysis with strategic impact assessment</output>
      <validate>Limitations analysis guides realistic scope and approach selection</validate>
    </checkpoint>
    
    <checkpoint name="CLEAR_EXAMPLES_AND_PATTERNS">
      <verify>CLEAR examples and patterns provide implementation guidance aligned with strategic objectives</verify>
      <output>Display implementation patterns, best practices, existing examples, and anti-patterns to avoid</output>
      <validate>Examples enable optimal technical decisions and architecture selection</validate>
    </checkpoint>
    
    <checkpoint name="CLEAR_COMPREHENSIVE_ACTIONS">
      <verify>CLEAR actions integrate SOAR strategy with comprehensive technical planning</verify>
      <output>Display implementation actions, coordination setup, quality strategy, and strategic validation</output>
      <validate>Actions bridge strategic objectives to practical implementation with quality assurance</validate>
    </checkpoint>
    
    <checkpoint name="CLEAR_ROLE_AND_EXECUTION">
      <verify>CLEAR role definition optimized for strategic and technical success</verify>
      <output>Display expert role, quality standards, execution approach, and delegation decision</output>
      <validate>Role and execution approach align with feature complexity and strategic objectives</validate>
    </checkpoint>
  </enforcement_verification>
  
  <decision_registry enforcement="REQUIRED">
    <decision_format>
      <id>FEATURE-{timestamp}-{decision_type}</id>
      <type>ARCHITECTURE | TECHNOLOGY | SECURITY | PERFORMANCE | DESIGN</type>
      <context>What prompted this decision</context>
      <options_considered>List of alternatives evaluated</options_considered>
      <decision>The chosen approach with rationale</decision>
      <consequences>Downstream impacts and tradeoffs</consequences>
      <reversibility>HIGH | MEDIUM | LOW</reversibility>
    </decision_format>
    
    <mandatory_decisions>
      <decision type="ARCHITECTURE">Framework and pattern selection</decision>
      <decision type="TECHNOLOGY">Language, libraries, and tools</decision>
      <decision type="SECURITY">Authentication and authorization approach</decision>
      <decision type="PERFORMANCE">Caching and optimization strategy</decision>
      <decision type="DESIGN">API structure and data models</decision>
    </mandatory_decisions>
    
    <propagation_rules>
      <rule>All decisions MUST be recorded in GitHub session</rule>
      <rule>Child agents inherit parent decision context</rule>
      <rule>Conflicting decisions require explicit resolution</rule>
      <rule>Decision changes require impact analysis</rule>
    </propagation_rules>
  </decision_registry>
  
  <critical_thinking_validation enforcement="REQUIRED">
    <pre_action_analysis duration="30_seconds_minimum">
      <step>1. PAUSE: Take 30 seconds to analyze the full request</step>
      <step>2. CHALLENGE: Question assumptions in the feature request</step>
      <step>3. RESEARCH: Check for existing similar implementations</step>
      <step>4. CONSEQUENCES: Map out If X → Y → Z implications</step>
      <step>5. ALTERNATIVES: Consider at least 3 different approaches</step>
    </pre_action_analysis>
    
    <duplication_prevention>
      <scan>Search entire codebase for similar functionality</scan>
      <analyze>Identify reusable components and patterns</analyze>
      <decide>Justify new implementation vs extending existing</decide>
      <document>Record duplication analysis in decision registry</document>
    </duplication_prevention>
    
    <validation_outputs enforcement="MANDATORY">
      <output>Display: "⏸️ CRITICAL THINKING: Analyzing for 30 seconds..."</output>
      <output>Show discovered assumptions and challenges</output>
      <output>List existing similar implementations found</output>
      <output>Present consequence map with downstream effects</output>
      <output>Compare 3+ alternative approaches with tradeoffs</output>
    </validation_outputs>
  </critical_thinking_validation>
  
  <module_integration>
    <primary_module>modules/planning/feature-workflow.md</primary_module>
    <execution_flow>
      <phase name="SOAR Strategy">frameworks/soar.md → Strategic situation analysis and objective definition</phase>
      <phase name="CLEAR Analysis">frameworks/clear.md → Comprehensive context and limitation analysis</phase>
      <phase name="Framework Selection">frameworks/framework-selector.md → Intelligent framework optimization</phase>
      <phase name="Context">patterns/context-preservation.md → Load comprehensive project context</phase>
      <phase name="PRD">planning/feature-workflow.md → Generate SOAR/CLEAR integrated requirements</phase>
      <phase name="Session">patterns/session-management.md → Create GitHub tracking with strategic context</phase>
      <phase name="Analysis">patterns/intelligent-routing.md → Framework-aware complexity scoring</phase>
      <phase name="Delegation">IF score>15: patterns/multi-agent.md → SOAR/CLEAR coordinated swarm execution</phase>
      <phase name="Development">development/task-management.md → Framework-integrated TDD implementation</phase>
      <phase name="Quality">quality/production-standards.md → Strategic and technical gate enforcement</phase>
      <phase name="Security">security/threat-modeling.md → Threat analysis with strategic context</phase>
      <phase name="Docs">development/documentation.md → SOAR/CLEAR guided auto-documentation</phase>
    </execution_flow>
  </module_integration>
  
  <usage_examples>
    <example>/feature "User authentication system with JWT" # SOAR strategic analysis → CLEAR comprehensive security implementation</example>
    <example>/feature "Real-time chat with WebSockets"     # SOAR business objectives → CLEAR technical coordination → /swarm delegation</example>
    <example>/feature "Payment processing with Stripe"     # SOAR compliance objectives → CLEAR security constraints → Strategic implementation</example>
    <example>/feature "High-performance API"               # SOAR performance objectives → CLEAR optimization patterns → Technical excellence</example>
    <example>/feature "User dashboard redesign"            # SOAR user experience objectives → CLEAR design patterns → Strategic UX implementation</example>
    <example>/feature "AI-powered recommendation engine"   # SOAR business intelligence → CLEAR ML constraints → Complex strategic implementation</example>
  </usage_examples>
  
  <persona_integration>
    <auto_detection>
      <rule>Security keywords (auth, payment, encryption) → security-specialist</rule>
      <rule>Performance keywords (optimize, scale, fast) → performance-engineer</rule>
      <rule>Architecture keywords (system, design, pattern) → senior-architect</rule>
      <rule>User keywords (dashboard, UX, experience) → product-engineer</rule>
      <rule>Quality keywords (test, coverage, standards) → quality-advocate</rule>
    </auto_detection>
    
    <explicit_selection>
      <flag>--persona {persona_name} # Override auto-detection</flag>
      <flag>--auto-persona # Enable intelligent auto-selection</flag>
      <validation>Persona must exist in .claude/personas/ directory</validation>
    </explicit_selection>
    
    <swarm_enhancement>
      <lead_persona>Primary persona guides overall feature direction</lead_persona>
      <specialist_agents>Each agent gets domain-appropriate persona assignment</specialist_agents>
      <cross_validation>Personas review each other's work through their expertise lens</cross_validation>
    </swarm_enhancement>
    
    <context_propagation>
      <inheritance>All child agents automatically inherit persona context</inheritance>
      <consistency>Persona decisions remain consistent throughout development</consistency>
      <tracking>GitHub sessions track persona assignments and decisions</tracking>
    </context_propagation>
  </persona_integration>
  
  <tdd_integration enforcement="MANDATORY">
    <strategic_testing>TDD approach aligned with SOAR strategic objectives and CLEAR comprehensive requirements</strategic_testing>
    <red_phase>Write failing tests for all feature acceptance criteria using quality/tdd.md#red_phase_compliance</red_phase>
    <green_phase>Implement minimal viable feature to make tests pass using quality/tdd.md#green_phase_compliance</green_phase>
    <refactor_phase>Improve feature design while maintaining green tests using quality/tdd.md#refactor_phase_compliance</refactor_phase>
    <framework_alignment>TDD cycle must align with SOAR/CLEAR framework expectations and strategic objectives</framework_alignment>
    <validation>Reference quality/tdd.md#quality_gates for strict enforcement</validation>
    
    <feature_checkpoint_enforcement>
      <soar_requirements_testing>
        <tdd_validation>BLOCK unless tests exist for ALL strategic objectives and success criteria</tdd_validation>
        <strategic_coverage>ENSURE tests validate feature alignment with business objectives</strategic_coverage>
        <quality_gate>Reference quality/tdd.md#strategic_test_validation</quality_gate>
      </soar_requirements_testing>
      
      <clear_comprehensive_testing>
        <tdd_validation>BLOCK unless comprehensive tests cover all CLEAR framework requirements</tdd_validation>
        <context_coverage>ENSURE tests validate feature behavior across all contexts and limitations</context_coverage>
        <quality_gate>Reference quality/tdd.md#comprehensive_test_validation</quality_gate>
      </clear_comprehensive_testing>
      
      <mvp_implementation_testing>
        <tdd_validation>BLOCK unless MVP implementation passes all strategic and comprehensive tests</tdd_validation>
        <scope_validation>VERIFY implementation stays within defined MVP boundaries</scope_validation>
        <quality_gate>Reference quality/tdd.md#mvp_validation</quality_gate>
      </mvp_implementation_testing>
      
      <feature_integration_testing>
        <tdd_validation>BLOCK unless integration tests validate feature system interaction</tdd_validation>
        <system_impact>VERIFY feature integration doesn't break existing functionality</system_impact>
        <quality_gate>Reference quality/tdd.md#integration_validation</quality_gate>
      </feature_integration_testing>
    </feature_checkpoint_enforcement>
    
    <blocking_conditions>
      <condition>Implementation attempted before SOAR strategic analysis</condition>
      <condition>Feature development bypassed CLEAR comprehensive requirements</condition>
      <condition>Tests written without strategic objective alignment</condition>
      <condition>Implementation exceeds MVP scope defined in strategic planning</condition>
      <condition>Integration testing skipped for system-level feature</condition>
      <condition>Test coverage below 90% for new feature code</condition>
      <condition>Feature quality below strategic standards defined in objectives</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <rules enforcement="STRICT">
    <rule priority="CRITICAL">ALWAYS apply SOAR framework for strategic analysis and objectives</rule>
    <rule priority="CRITICAL">ALWAYS apply CLEAR framework for comprehensive context and requirements</rule>
    <rule priority="CRITICAL">ALWAYS integrate frameworks before PRD generation and GitHub session creation</rule>
    <rule priority="HIGH">Calculate complexity with framework overhead - delegate to /swarm if >15</rule>
    <rule priority="HIGH">TDD mandatory with framework-aligned test strategies</rule>
    <rule priority="HIGH">Quality gates from production-standards.md with strategic validation</rule>
    <rule priority="MEDIUM">Framework selection intelligence for optimization opportunities</rule>
  </rules>
  
  <pattern_usage>
    • Uses soar_framework_integration pattern for strategic feature planning and objective definition
    • Implements clear_framework_integration pattern for comprehensive context analysis and technical requirements
    • Applies framework_selection_intelligence pattern for optimal coordination strategies
    • Uses prd_first pattern with SOAR/CLEAR framework integration for enhanced requirements
    • Implements issue_tracking pattern for GitHub session creation with strategic context
    • Applies tdd_cycle with framework-aligned test-first enforcement and strategic validation
    • Leverages parallel_execution when delegating to framework-coordinated swarm
    • Uses graceful_degradation from error-recovery.md with framework awareness
    • Implements consequence_mapping for strategic and technical architecture decisions
    • Integrates git-operations.md for framework-optimized branch strategies
    
    See modules/frameworks/soar.md for SOAR framework strategic planning implementation
    See modules/frameworks/clear.md for CLEAR framework comprehensive analysis implementation
    See modules/frameworks/framework-selector.md for intelligent framework optimization
    See modules/patterns/pattern-library.md for pattern details
    See modules/planning/feature-workflow.md for SOAR/CLEAR integrated full implementation
  </pattern_usage>
  

  <prompt_construction>
    <assembly_preview>
      SOAR/CLEAR FRAMEWORK WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. SOAR        │ → Strategic situation analysis
      │    Situation   │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. SOAR        │ → Strategic objectives definition
      │    Objectives  │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. SOAR        │ → Strategic action planning
      │    Actions     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. SOAR        │ → Strategic results framework
      │    Results     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 5. CLEAR       │ → Comprehensive context analysis
      │    Context     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 6. CLEAR       │ → Limitation and constraint analysis
      │    Limitations │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 7. CLEAR       │ → Examples and pattern guidance
      │    Examples    │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 8. CLEAR       │ → Comprehensive action specification
      │    Actions     │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 9. CLEAR       │ → Role definition and execution
      │    Role        │
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~25,000
      - SOAR strategic framework: 8,000
      - CLEAR comprehensive framework: 10,000
      - Framework integration: 3,000
      - PRD generation with frameworks: 2,000
      - Session setup and execution: 2,000
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /feature "User notifications"
      [00:15] 🎯 SOAR SITUATION: Business context and user needs analyzed
      [00:30] 📊 SOAR OBJECTIVES: Strategic goals and success metrics defined
      [00:45] 📋 SOAR ACTIONS: Strategic development phases planned
      [01:00] 🎯 SOAR RESULTS: Expected outcomes and measurement framework set
      [01:15] 🌐 CLEAR CONTEXT: Comprehensive technical and business context analyzed
      [01:30] ⚠️ CLEAR LIMITATIONS: Constraints and technical boundaries identified
      [01:45] 📚 CLEAR EXAMPLES: Implementation patterns and best practices selected
      [02:00] 🚀 CLEAR ACTIONS: Strategic and technical integration completed
      [02:15] 👤 CLEAR ROLE: Expert role and execution approach optimized
      [02:30] 📋 PRD: SOAR/CLEAR integrated comprehensive requirements generated
      [02:45] 🎯 SESSION: GitHub issue with strategic context tracking
      [03:00] ✅ COMPLETE: Strategic feature development ready for execution
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Reads SOAR/CLEAR framework integrated checkpoint structure sequentially
      2. Executes critical_thinking questions with strategic and comprehensive analysis internally
      3. Formats output according to framework-aligned output_format specifications
      4. Validates against SOAR/CLEAR framework compliance and enforcement rules before proceeding
      5. Applies parallel execution optimization with framework coordination where possible
      6. Integrates framework selection intelligence for strategic and technical optimization
    </parsing_behavior>

    <decision_points>
      - SOAR framework strategic analysis guides business and objective decision-making
      - CLEAR framework comprehensive analysis guides technical and implementation decisions
      - Checkpoint failures trigger framework-aware enforcement and strategic reassessment
      - Module selection based on framework requirements and contextual conditions
      - Parallel execution optimized for framework-coordinated independent operations
      - Quality gate validation at completion boundaries with strategic and technical criteria
      - Error recovery through framework-aware graceful degradation paths
      - Framework selection intelligence guides strategic optimization decisions
    </decision_points>
  </claude_4_interpretation>

</command>
```
────────────────────────────────────────────────────────────────────────────────

## Full Autonomy Directive

```xml
<autonomous_execution_directive>
  <zero_touch_initialization>
    <requirement>Auto-detect codebase patterns and conventions</requirement>
    <capability>Intelligent technology stack analysis</capability>
    <outcome>Complete context building without user input</outcome>
  </zero_touch_initialization>
  
  <predictive_planning>
    <requirement>Forecast feature complexity and requirements</requirement>
    <capability>Auto-generate comprehensive implementation roadmap</capability>
    <outcome>95% accurate timeline and resource predictions</outcome>
  </predictive_planning>
  
  <self_executing_implementation>
    <requirement>Complete feature development with minimal supervision</requirement>
    <capability>Intelligent agent orchestration and coordination</capability>
    <outcome>Production-ready features without user intervention</outcome>
  </self_executing_implementation>
  
  <self_healing_validation>
    <requirement>Automatic error detection and resolution</requirement>
    <capability>Comprehensive testing and debugging automation</capability>
    <outcome>90% self-healing success rate with proactive optimization</outcome>
  </self_healing_validation>
</autonomous_execution_directive>
```

────────────────────────────────────────────────────────────────────────────────

## Implementation Reference

This command delegates ALL implementation to specialized modules:

See modules/planning/feature-workflow.md for master orchestration and PRD-driven development.
See modules/planning/intelligent-prd.md for automatic requirement extraction and analysis.
See modules/planning/mvp-strategy.md for MVP implementation patterns and strategies.
See modules/testing/auto-testing.md for self-healing validation and debugging.
See modules/patterns/multi-agent.md for autonomous multi-agent coordination.

────────────────────────────────────────────────────────────────────────────────

## Input Requirements (MINIMAL)

```xml
<user_input_minimal>
  <initial_request>Single sentence feature description</initial_request>
  <confirmation_points>Binary approve/reject only at key milestones</confirmation_points>
  <business_logic>User confirmation for business rule decisions only</business_logic>
  <security_policies>User validation for security-critical decisions only</security_policies>
</user_input_minimal>
```

────────────────────────────────────────────────────────────────────────────────

## Autonomous Decision Domains

```xml
<autonomous_domains>
  <technical_architecture>Framework selects optimal approaches</technical_architecture>
  <implementation_strategy>Self-selection of execution patterns</implementation_strategy>
  <quality_assurance>Auto-enforcement of all quality gates</quality_assurance>
  <testing_strategy>Comprehensive autonomous validation</testing_strategy>
  <performance_optimization>Self-optimizing execution</performance_optimization>
  <error_resolution>Self-healing debugging and fixes</error_resolution>
</autonomous_domains>
```

────────────────────────────────────────────────────────────────────────────────

## Zero-Input Initialization Patterns

```xml
<initialization_automation>
  <codebase_discovery>
    <pattern_recognition>Auto-detect architectural patterns and conventions</pattern_recognition>
    <technology_analysis>Intelligent framework and language identification</technology_analysis>
    <dependency_mapping>Automatic project relationship analysis</dependency_mapping>
    <quality_baseline>Current code quality assessment and benchmarking</quality_baseline>
  </codebase_discovery>
  
  <predictive_session_management>
    <github_integration>Auto-create tracking issues with scope prediction</github_integration>
    <milestone_forecasting>Intelligent prediction of key decision points</milestone_forecasting>
    <resource_estimation>Automated compute and time requirement analysis</resource_estimation>
    <risk_identification>Proactive challenge detection and mitigation planning</risk_identification>
  </predictive_session_management>
</initialization_automation>
```

────────────────────────────────────────────────────────────────────────────────

## Self-Healing Error Recovery

```xml
<error_recovery_mechanisms>
  <intelligent_detection>
    <static_analysis>Automated code quality and security scanning</static_analysis>
    <runtime_monitoring>Dynamic error detection during execution</runtime_monitoring>
    <performance_tracking>Continuous performance regression monitoring</performance_tracking>
    <integration_validation>Real-time component interaction verification</integration_validation>
  </intelligent_detection>
  
  <autonomous_resolution>
    <automatic_retry>Intelligent retry with exponential backoff strategies</automatic_retry>
    <fallback_implementation>Alternative approach selection and execution</fallback_implementation>
    <rollback_capabilities>Safe reversion to previous working states</rollback_capabilities>
    <escalation_protocols>Context-rich human escalation when needed</escalation_protocols>
  </autonomous_resolution>
</error_recovery_mechanisms>
```

────────────────────────────────────────────────────────────────────────────────

## Intelligent Agent Orchestration

```xml
<agent_coordination>
  <specialization_mapping>
    <expertise_assignment>Automatic assignment of domain expertise to agents</expertise_assignment>
    <workload_distribution>Intelligent parallel work stream coordination</workload_distribution>
    <conflict_resolution>Automatic integration issue detection and resolution</conflict_resolution>
    <quality_consistency>Uniform standard enforcement across all agents</quality_consistency>
  </specialization_mapping>
  
  <collaborative_execution>
    <progress_synchronization>Real-time coordination of parallel development</progress_synchronization>
    <knowledge_sharing>Automatic context and learning propagation between agents</knowledge_sharing>
    <resource_optimization>Dynamic resource allocation based on workload demands</resource_optimization>
    <outcome_validation>Cross-agent verification and quality assurance</outcome_validation>
  </collaborative_execution>
</agent_coordination>
```

────────────────────────────────────────────────────────────────────────────────

## Success Criteria

- **95% Self-Sufficiency**: Features completed without user intervention
- **Intelligent Strategy Selection**: Optimal implementation approaches chosen automatically
- **90% Self-Healing**: Automatic resolution of encountered issues
- **Predictive Accuracy**: Timeline and resource predictions within 10% variance
- **Framework Evolution**: Continuous improvement through execution learnings

────────────────────────────────────────────────────────────────────────────────

## Quality Gates (AUTONOMOUS)

- **TDD Enforcement**: Mandatory RED-GREEN-REFACTOR cycle
- **Security First**: Automatic threat modeling and validation
- **Performance**: <200ms p95 with automatic optimization
- **Test Coverage**: 90% minimum with quality assertions
- **Documentation**: Comprehensive auto-generated documentation

────────────────────────────────────────────────────────────────────────────────

*Zero-touch feature delivery with maximum intelligence and minimum user intervention.*