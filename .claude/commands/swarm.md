| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 95%      |

# Swarm Command - Multi-Agent Development Coordination

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="swarm" category="coordination" enforcement="BLOCKING">
  
  <purpose>
    Execute multi-component development with intelligent agent coordination, git worktree isolation, parallel TDD enforcement, and comprehensive integration testing optimized for Claude 4 capabilities.
  </purpose>
  
  <scope>
    <includes>Multi-component features, cross-system refactoring, parallel development streams, complex integrations</includes>
    <excludes>Single component tasks, simple modifications, documentation-only changes, prototype development</excludes>
    <boundaries>Tasks affecting 3+ components or requiring coordination across multiple development streams</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Multi-component development description with clear component boundaries and integration requirements</required_arguments>
    <context_requirements>System architecture, component dependencies, integration patterns, testing strategies</context_requirements>
    <preconditions>Git repository ready, component boundaries identified, integration points mapped, testing frameworks available</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Integrated multi-component implementation, comprehensive test coverage, validated integration points, production-ready system</deliverables>
    <success_criteria>All components functioning, integration validated, tests passing, quality gates met, coordination successful</success_criteria>
    <artifacts>Component implementations, integration tests, worktree history, coordination documentation, quality validation reports</artifacts>
  </output_specification>
</command>
```

Multi-component development with intelligent agent coordination and atomic commits.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="extended">
    <action>Multi-Component Analysis and Coordination Strategy: Comprehensive analysis of component boundaries, dependencies, and coordination requirements</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What are the distinct components requiring parallel development?
        - How do component dependencies affect coordination strategy?
        - What integration points require careful management and validation?
      </pre_analysis>
      <critical_thinking minimum_time="45_seconds">
        - [Component Question: What are the logical component boundaries and their individual responsibilities?]
        - [Dependency Question: How do components interact and what are the critical dependency chains?]
        - [Coordination Question: What coordination strategy ensures parallel development without conflicts?]
        - [Integration Question: What integration points require careful design and validation?]
        - [Risk Question: What parallel development risks require mitigation strategies?]
        - [Quality Question: How can quality standards be maintained across all components simultaneously?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this component breakdown optimize parallel development efficiency?
        - What evidence supports the coordination strategy for managing complexity?
        - How does the integration approach ensure system cohesion and reliability?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch component analysis, dependency mapping, and coordination planning for comprehensive assessment</tool_optimization>
      <context_efficiency>Load system architecture, component specifications, and integration patterns concurrently</context_efficiency>
      <dependency_analysis>Identify analysis steps that can be parallelized vs sequential coordination requirements</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>SWARM_ANALYSIS: [components] with [dependencies] requiring [coordination_strategy] and [integration_approach]</output_format>
    <validation>Components clearly identified, dependencies mapped, coordination strategy validated, integration approach confirmed</validation>
    <enforcement>BLOCK swarm execution until comprehensive multi-component analysis validates coordination approach</enforcement>
    <context_transfer>Component specifications, dependency map, coordination strategy, integration plan</context_transfer>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Git Worktree Isolation and Agent Assignment: Set up isolated development environments with strategic agent assignment</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should git worktrees be structured for optimal component isolation?
        - What agent assignment strategy ensures efficient parallel development?
        - How can worktree isolation prevent conflicts while enabling integration?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Isolation Question: Does worktree structure provide proper component isolation with integration capability?]
        - [Assignment Question: Are agents optimally assigned based on component complexity and dependencies?]
        - [Strategy Question: Does branch strategy support parallel development with safe integration paths?]
        - [Rollback Question: Are rollback mechanisms available for each component independently?]
        - [Coordination Question: How will agents coordinate without creating conflicts or duplication?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this worktree structure optimize parallel development efficiency?
        - What evidence supports the agent assignment strategy for component responsibilities?
        - How does isolation design enable safe parallel development with integration capability?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch worktree creation, agent assignment, and branch strategy implementation</tool_optimization>
      <context_efficiency>Set up parallel development environments with concurrent configuration</context_efficiency>
      <dependency_analysis>Identify worktree setup steps that can be parallelized while maintaining isolation integrity</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>SWARM_SETUP: [worktrees_created] with [agent_assignments] using [branch_strategy] enabling [isolation_benefits]</output_format>
    <validation>Worktrees properly isolated, agents strategically assigned, branch strategy implemented, rollback capability confirmed</validation>
    <enforcement>BLOCK parallel development until worktree isolation and agent assignment strategy validated</enforcement>
    <context_transfer>Worktree configuration, agent assignments, branch strategy, isolation validation</context_transfer>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Parallel TDD Execution with Agent Coordination: Execute TDD across components with intelligent agent coordination</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should TDD be coordinated across multiple parallel development streams?
        - What coordination mechanisms ensure agents work harmoniously without conflicts?
        - How can comprehensive testing be maintained across all components simultaneously?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [TDD Question: Is each agent following strict TDD with RED→GREEN→REFACTOR cycles independently?]
        - [Coordination Question: Are coordination mechanisms preventing conflicts while enabling collaboration?]
        - [Quality Question: Is test coverage comprehensive across all components with proper assertions?]
        - [Integration Question: How do component tests validate interface contracts and integration points?]
        - [Performance Question: Are agents working efficiently without creating bottlenecks or dependencies?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this coordination approach ensure quality parallel development?
        - What evidence shows effective agent collaboration without conflicts?
        - How does parallel TDD maintain quality standards across all components?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Execute parallel TDD streams with coordinated testing and validation across agents</tool_optimization>
      <context_efficiency>Optimize agent coordination and component development for maximum parallel efficiency</context_efficiency>
      <dependency_analysis>Identify TDD execution that can be truly parallel vs coordination points requiring synchronization</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>SWARM_EXECUTION: [agents_active] completing [components] with [coordination_status] maintaining [quality_standards]</output_format>
    <validation>All agents following TDD, coordination mechanisms working, quality maintained, no conflicts detected</validation>
    <enforcement>BLOCK integration until parallel TDD execution validates component completion with quality standards</enforcement>
    <context_transfer>Component completion status, TDD compliance, coordination results, quality validation</context_transfer>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Comprehensive Integration and System Validation: Merge components with comprehensive integration testing</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should component integration be orchestrated to ensure system coherence?
        - What comprehensive testing strategy validates integrated system functionality?
        - How can integration risks be mitigated through systematic validation?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Integration Question: Do all components integrate seamlessly with proper interface validation?]
        - [Testing Question: Does comprehensive testing cover all integration points and system interactions?]
        - [Performance Question: Does the integrated system meet performance requirements under load?]
        - [Reliability Question: Is the integrated system stable and reliable across all use cases?]
        - [Rollback Question: Are rollback procedures tested and available for integration failures?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this integration approach ensure system reliability and performance?
        - What evidence demonstrates successful component integration with quality validation?
        - How does comprehensive testing validate end-to-end system functionality?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch integration testing, system validation, and performance benchmarking for comprehensive assessment</tool_optimization>
      <context_efficiency>Execute integration validation and system testing concurrently where possible</context_efficiency>
      <dependency_analysis>Identify integration tests that can be parallelized vs those requiring sequential validation</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>SWARM_INTEGRATION: [components_integrated] with [system_validation] confirming [performance_metrics] and [reliability_standards]</output_format>
    <validation>All components integrated successfully, system validation complete, performance verified, reliability confirmed</validation>
    <enforcement>BLOCK completion until comprehensive integration validates system functionality and performance</enforcement>
    <context_transfer>Integration results, system validation, performance metrics, reliability confirmation</context_transfer>
  </checkpoint>
  
  <checkpoint id="5" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Quality Gates and Production Readiness: Comprehensive quality validation and production readiness assessment</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What quality gates ensure the integrated system meets production standards?
        - How can comprehensive validation confirm system readiness for deployment?
        - What monitoring and operational readiness is required for production?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Quality Question: Do all quality gates pass with measurable evidence across all components?]
        - [Production Question: Is the system ready for production deployment with proper documentation?]
        - [Monitoring Question: Are monitoring and alerting configured for system health and component performance?]
        - [Documentation Question: Is comprehensive documentation available for development, deployment, and operations?]
        - [Maintenance Question: Are maintenance procedures and troubleshooting guides available?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this system meet comprehensive production quality standards?
        - What evidence demonstrates readiness for production deployment and operations?
        - How do quality metrics and validation results support production confidence?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch quality gate validation, production readiness assessment, and documentation verification</tool_optimization>
      <context_efficiency>Execute comprehensive quality validation and production preparation concurrently</context_efficiency>
      <dependency_analysis>Identify quality validation steps that can be parallelized while ensuring comprehensive coverage</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>SWARM_COMPLETE: [quality_gates_passed] with [production_readiness] confirming [system_reliability] and [operational_readiness]</output_format>
    <validation>All quality gates passed, production readiness confirmed, system reliable, operational procedures ready</validation>
    <enforcement>BLOCK completion until comprehensive quality validation confirms production readiness</enforcement>
    <context_transfer>Quality validation results, production readiness confirmation, operational documentation</context_transfer>
  </checkpoint>
  
</thinking_pattern>
```

## Instructions

Execute multi-component development workflow for: $ARGUMENTS

1. **Component Analysis**: Analyze scope and identify components needing coordination.
   - **Atomic Checkpoint**: `git add -A && git commit -m "SWARM ANALYSIS: [components] - coordination strategy and dependencies mapped"`

2. **Worktree Setup**: Create isolated git worktrees for parallel development.
   - **Atomic Checkpoint**: `git add -A && git commit -m "SWARM SETUP: [worktrees] - isolated environments and agent assignments created"`
   - **Isolation Safety**: Each worktree operates independently with full rollback capability

3. **Parallel TDD Execution**: Coordinate multiple TDD streams with agent coordination.
   - **Per-Agent Atomic Checkpoints**: `git add -A && git commit -m "SWARM EXECUTION: [component] - TDD cycle completed with coordination"`
   - **TDD Enforcement**: Each agent follows strict RED→GREEN→REFACTOR with atomic commits
   - **Coordination Safety**: Failed components can be rolled back without affecting others

4. **Integration Testing**: Merge components with comprehensive system validation.
   - **Atomic Checkpoint**: `git add -A && git commit -m "SWARM INTEGRATION: [system] - components integrated and validated"`
   - **Integration Validation**: Full system tests and performance validation before commit

5. **Quality Validation**: Comprehensive quality gates and production readiness.
   - **Final Atomic Checkpoint**: `git add -A && git commit -m "SWARM COMPLETE: [system] - production ready with quality validation"`

## Critical Rules

- ALWAYS analyze component boundaries and dependencies first
- NEVER proceed without proper worktree isolation
- Maintain strict TDD across all parallel development streams
- Use comprehensive integration testing before merging
- **COORDINATION SAFETY**: Each component can be rolled back independently
- **AGENT COORDINATION**: Parallel agents must not create conflicts or dependencies

## Module Integration

```xml
<module_orchestration>
  <core_modules>
    <module>patterns/thinking/critical-thinking-pattern.md</module>
    <module>quality/tdd.md</module>
    <module>patterns/multi-agent.md</module>
    <module>quality/universal-quality-gates.md</module>
    <module>system/session/session-management.md</module>
  </core_modules>
  
  <contextual_modules>
    <module condition="complex_integration">patterns/integration-pattern.md</module>
    <module condition="performance_critical">patterns/performance-optimization.md</module>
    <module condition="security_sensitive">security/threat-modeling.md</module>
    <module condition="long_coordination">development/task-management.md</module>
  </contextual_modules>
  
  <support_modules>
    <module>patterns/comprehensive-error-handling.md</module>
    <module>patterns/error-recovery.md</module>
    <module>patterns/context-management-pattern.md</module>
    <module>patterns/validation-pattern.md</module>
    <module>system/git/git-worktree-management.md</module>
  </support_modules>
</module_orchestration>
```

## Error Handling

```xml
<error_handling>
  <coordination_failures>
    <agent_conflict>Isolate conflicting agents, resolve dependencies, restart coordination</agent_conflict>
    <integration_failure>Rollback to pre-integration state, fix component issues, retry integration</integration_failure>
    <quality_gate_failure>Address quality issues per component, re-validate all gates</quality_gate_failure>
    <worktree_corruption>Restore from backup, recreate worktree, resume from last checkpoint</worktree_corruption>
  </coordination_failures>
  
  <escalation_paths>
    <complex_dependencies>Route to /session for GitHub issue tracking and extended coordination</complex_dependencies>
    <production_deployment>Route to /protocol for maximum quality enforcement</production_deployment>
    <unclear_boundaries>Route to /query for component analysis and boundary clarification</unclear_boundaries>
    <performance_issues>Route to performance optimization modules for systematic improvement</performance_issues>
  </escalation_paths>
  
  <recovery_procedures>
    <component_rollback>git reset --hard to component checkpoint, restart TDD cycle</component_rollback>
    <coordination_reset>Reset coordination state, re-analyze dependencies, restart coordination</coordination_reset>
    <integration_rollback>Return to pre-integration state, validate components individually</integration_rollback>
    <system_recovery>Full system rollback to last known good state, comprehensive re-validation</system_recovery>
  </recovery_procedures>
  
  <comprehensive_error_handling_integration>
    <module>patterns/comprehensive-error-handling.md</module>
    <coordination_specific_enhancements>Multi-agent coordination error patterns, worktree management failures, integration conflicts</coordination_specific_enhancements>
    <graceful_degradation>Agent isolation, sequential fallback, coordination simplification</graceful_degradation>
    <monitoring_integration>Coordination efficiency, agent utilization, integration success rates</monitoring_integration>
  </comprehensive_error_handling_integration>
</error_handling>
```

## When to Use

- Development touches 3+ files across different components
- Multiple features need parallel development
- Complex refactoring affecting multiple systems
- Team coordination required for large features
- Cross-cutting concerns affecting multiple services

## Examples

- `/swarm "Implement user authentication system"` - Auth across frontend, backend, database
- `/swarm "Refactor payment processing"` - Multiple services coordination
- `/swarm "Add monitoring to all services"` - Cross-cutting concerns implementation