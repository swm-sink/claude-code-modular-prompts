| version | last_updated | status |
|---------|--------------|--------|
| 2.4.0   | 2025-01-08   | stable |

# Autonomous Feature Development

────────────────────────────────────────────────────────────────────────────────

**PURPOSE**: Autonomous feature development with 95% self-sufficiency and intelligent orchestration

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Autonomous PRD-driven feature development with intelligent orchestration">
  
  <delegation target="modules/planning/feature-workflow.md">
    Generate PRD → Analyze complexity → Plan MVP → Execute autonomously → Validate
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <step>0. CONTEXT PRIMING: Load comprehensive project context BEFORE any planning begins
      - Repository structure analysis via Glob(**/*.{js,ts,py,java,go,rs})
      - Key file identification (README, package.json, requirements.txt, go.mod, Cargo.toml)
      - Technology stack detection from dependencies and file extensions
      - Coding standards extraction from .eslintrc, .prettierrc, pyproject.toml, etc.
      - Recent commit history review via git log --oneline -20
      - Architecture patterns from existing code structure
      - Test framework detection from test files and config</step>
    <step>1. PERSONA: Load persona context from patterns/persona-manager.md (auto-detect or --persona flag)</step>
    <step>2. Generate comprehensive PRD using feature-workflow.md patterns enhanced with persona perspective and context insights</step>
    <step>3. Auto-detect tech stack and existing patterns in codebase through persona lens AND context analysis</step>
    <step>4. Create GitHub session for tracking (ALWAYS) with persona assignments and context summary logged</step>
    <step>5. Define MVP with clear phases and acceptance criteria using persona-specific quality gates</step>
    <step>6. Calculate complexity: >15 score triggers /swarm delegation with specialized personas</step>
    <step>7. Execute with TDD: Write ALL tests FIRST using persona-enhanced testing approach and detected test framework</step>
    <step>8. Apply quality gates from production-standards.md augmented with persona standards</step>
    <step>9. Auto-generate documentation via /docs patterns with persona-specific documentation style</step>
  </thinking_pattern>
  
  <enforcement_verification enforcement="REQUIRED">
    <checkpoint name="CONTEXT_PRIMING">
      <verify>Project context fully loaded and analyzed</verify>
      <output>Display detected: tech stack, test framework, coding standards, architecture patterns</output>
      <validate>Repository structure understood, key files identified, patterns detected</validate>
    </checkpoint>
    
    <checkpoint name="PRD_GENERATION">
      <verify>PRD document created with all sections populated AND context insights integrated</verify>
      <output>Display PRD summary with key decisions informed by context analysis</output>
      <validate>User story, acceptance criteria, technical approach defined using existing patterns</validate>
    </checkpoint>
    
    <checkpoint name="TECH_ANALYSIS">
      <verify>Codebase patterns detected and documented</verify>
      <output>List detected frameworks, patterns, and conventions</output>
      <validate>Technology stack compatibility confirmed</validate>
    </checkpoint>
    
    <checkpoint name="SESSION_CREATION">
      <verify>GitHub issue created with proper structure</verify>
      <output>Show issue URL and initial task breakdown</output>
      <validate>All phases mapped with checkboxes</validate>
    </checkpoint>
    
    <checkpoint name="COMPLEXITY_ASSESSMENT">
      <verify>Complexity score calculated using deterministic rules</verify>
      <output>Display score breakdown: files={n}, patterns={n}, integrations={n}</output>
      <validate>Routing decision made: /task or /swarm</validate>
    </checkpoint>
    
    <checkpoint name="TDD_COMPLIANCE">
      <verify>All tests written BEFORE implementation</verify>
      <output>Show test file paths and RED test results</output>
      <validate>Tests fail for the right reasons</validate>
    </checkpoint>
    
    <checkpoint name="QUALITY_GATES">
      <verify>All gates from production-standards.md passed</verify>
      <output>Display gate results: security=✓, performance=✓, coverage=✓</output>
      <validate>No gate bypassed without explicit justification</validate>
    </checkpoint>
    
    <checkpoint name="DOCUMENTATION">
      <verify>Documentation generated via /docs command</verify>
      <output>List created/updated documentation files</output>
      <validate>All code changes have corresponding docs</validate>
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
      <phase name="Context">patterns/context-preservation.md → Load comprehensive project context</phase>
      <phase name="PRD">planning/feature-workflow.md → Generate requirements with context insights</phase>
      <phase name="Session">patterns/session-management.md → Create GitHub tracking with context summary</phase>
      <phase name="Analysis">patterns/intelligent-routing.md → Complexity scoring</phase>
      <phase name="Delegation">IF score>15: patterns/multi-agent.md → Swarm execution</phase>
      <phase name="Development">development/task-management.md → TDD implementation</phase>
      <phase name="Quality">quality/production-standards.md → Gate enforcement</phase>
      <phase name="Security">security/threat-modeling.md → Threat analysis</phase>
      <phase name="Docs">development/documentation.md → Auto-documentation</phase>
    </execution_flow>
  </module_integration>
  
  <usage_examples>
    <example>/feature "User authentication system with JWT" # Auto-detects security-specialist persona</example>
    <example>/feature "Real-time chat with WebSockets"     # Complex→delegates to /swarm with specialized personas</example>
    <example>/feature "Payment processing with Stripe" --persona security-specialist # Explicit security-first approach</example>
    <example>/feature "High-performance API" --persona performance-engineer # Optimization-focused development</example>
    <example>/feature "User dashboard redesign" --persona product-engineer # User-value focused approach</example>
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
  
  <rules enforcement="STRICT">
    <rule priority="CRITICAL">ALWAYS generate PRD first using patterns</rule>
    <rule priority="CRITICAL">ALWAYS create GitHub session for tracking</rule>
    <rule priority="HIGH">Calculate complexity - delegate to /swarm if >15</rule>
    <rule priority="HIGH">TDD mandatory - tests before implementation</rule>
    <rule priority="HIGH">Quality gates from production-standards.md</rule>
  </rules>
  
  <pattern_usage>
    • Implements prd_first pattern EXPLICITLY with PRD generation
    • Uses issue_tracking pattern for GitHub session creation
    • Applies tdd_cycle with test-first enforcement
    • Leverages parallel_execution when delegating to swarm
    • Uses graceful_degradation from error-recovery.md
    • Implements consequence_mapping for architecture decisions
    • Integrates git-operations.md for branch strategies
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/planning/feature-workflow.md for full implementation
  </pattern_usage>
  
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