| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

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
    <step>1. Generate comprehensive PRD using feature-workflow.md patterns</step>
    <step>2. Auto-detect tech stack and existing patterns in codebase</step>
    <step>3. Create GitHub session for tracking (ALWAYS)</step>
    <step>4. Define MVP with clear phases and acceptance criteria</step>
    <step>5. Calculate complexity: >15 score triggers /swarm delegation</step>
    <step>6. Execute with TDD: Write ALL tests FIRST</step>
    <step>7. Apply quality gates from production-standards.md</step>
    <step>8. Auto-generate documentation via /docs patterns</step>
  </thinking_pattern>
  
  <module_integration>
    <primary_module>modules/planning/feature-workflow.md</primary_module>
    <execution_flow>
      <phase name="PRD">planning/feature-workflow.md → Generate requirements</phase>
      <phase name="Session">patterns/session-management.md → Create GitHub tracking</phase>
      <phase name="Analysis">patterns/intelligent-routing.md → Complexity scoring</phase>
      <phase name="Delegation">IF score>15: patterns/multi-agent.md → Swarm execution</phase>
      <phase name="Development">development/task-management.md → TDD implementation</phase>
      <phase name="Quality">quality/production-standards.md → Gate enforcement</phase>
      <phase name="Security">security/threat-modeling.md → Threat analysis</phase>
      <phase name="Docs">development/documentation.md → Auto-documentation</phase>
    </execution_flow>
  </module_integration>
  
  <usage_examples>
    <example>/feature "User authentication system with JWT" # Creates PRD, session, TDD tests</example>
    <example>/feature "Real-time chat with WebSockets"     # Complex→delegates to /swarm</example>
    <example>/feature "Payment processing with Stripe"     # Security-first, threat model</example>
  </usage_examples>
  
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