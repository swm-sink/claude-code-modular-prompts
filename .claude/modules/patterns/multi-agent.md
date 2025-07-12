| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# Multi-Agent Pattern Module

────────────────────────────────────────────────────────────────────────────────

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="multi_agent" category="patterns">
  
  <purpose>
    Multi-agent coordination patterns for complex development tasks requiring specialized agents and git worktree isolation for the /swarm command.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>complex_task_specification, coordination_requirements, agent_specialization_needs</required>
      <optional>worktree_isolation_requirements, performance_targets, quality_constraints</optional>
    </inputs>
    <outputs>
      <success>coordinated_solution, agent_performance_metrics, worktree_management_results</success>
      <failure>coordination_failures, agent_conflicts, worktree_issues</failure>
    </outputs>
  </interface_contract>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Analyze complex task and determine optimal agent specialization
      2. Set up git worktree isolation for parallel development
      3. Coordinate specialized agents with defined responsibilities
      4. Monitor progress and resolve conflicts through intelligent mediation
      5. Integrate results with comprehensive validation and quality assurance
    </claude_4_behavior>
  </execution_pattern>
  
  <trigger_conditions>
    <condition type="automatic">/swarm command invoked for complex coordination</condition>
    <condition type="explicit">Multi-system features requiring specialized agents</condition>
    <condition type="explicit">High coordination complexity requiring orchestration</condition>
    <condition type="explicit">Parallel development requiring git worktree isolation</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="task_decomposition" order="1">
      <requirements>
        Complex task must be analyzed and decomposed
        Agent specialization needs must be identified
        Coordination requirements must be established
        MANDATORY: Apply critical thinking for optimal decomposition
      </requirements>
      <actions>
        Analyze task complexity and identify decomposition opportunities
        Determine optimal agent specialization for task components
        Map dependencies and coordination requirements
        Plan parallel execution with worktree isolation
        Define integration points and quality gates
        MANDATORY: Use 30s critical thinking for complex decomposition
        ENFORCEMENT: Use ../../system/../../system/quality/critical-thinking.md for analysis depth
      </actions>
      <validation>
        Task decomposition enables parallel execution
        Agent specializations align with task requirements
        Coordination requirements clearly defined
        Integration strategy established with quality gates
        VERIFICATION: Decomposition plan documented with rationale
      </validation>
      <blocking_conditions>
        <condition>Task decomposition incomplete or illogical</condition>
        <condition>Agent specializations don't align with requirements</condition>
        <condition>Coordination requirements undefined</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="worktree_setup" order="2">
      <requirements>
        Task decomposition from phase 1 must be completed
        Git worktree isolation must be established
        Agent workspaces must be configured
        MANDATORY: Worktree isolation for parallel development
      </requirements>
      <actions>
        Create isolated git worktrees for parallel agent development
        Set up agent-specific development environments
        Configure branch strategies and merge policies
        Establish communication channels between agents
        Initialize shared resources and coordination mechanisms
        MANDATORY: Use git worktree isolation patterns
        ENFORCEMENT: Use ../../../../../../system/git/worktree-isolation.md for setup
      </actions>
      <validation>
        Worktrees successfully created and isolated
        Agent workspaces properly configured
        Branch strategies support parallel development
        Communication channels established
        VERIFICATION: Worktree setup verified with test operations
      </validation>
      <blocking_conditions>
        <condition>Worktree creation fails or incomplete</condition>
        <condition>Agent workspaces not properly isolated</condition>
        <condition>Branch strategies don't support parallel work</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="agent_coordination" order="3">
      <requirements>
        Worktree setup from phase 2 must be completed
        Agent specializations must be activated
        Coordination protocols must be established
        MANDATORY: TDD enforcement across all agents
      </requirements>
      <actions>
        Activate specialized agents with defined responsibilities
        Establish coordination protocols and communication patterns
        Monitor agent progress and performance metrics
        Facilitate inter-agent communication and collaboration
        Resolve conflicts through intelligent mediation
        MANDATORY: Enforce TDD compliance across all agents
        ENFORCEMENT: Use system/../../system/../../system/quality/tdd.md for agent TDD requirements
      </actions>
      <validation>
        Agents operating within defined specializations
        Coordination protocols functioning effectively
        Progress monitoring provides actionable insights
        Conflicts resolved through systematic mediation
        VERIFICATION: Agent coordination metrics documented
      </validation>
      <blocking_conditions>
        <condition>Agent specializations not functioning correctly</condition>
        <condition>Coordination protocols break down</condition>
        <condition>TDD requirements not enforced</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="integration_validation" order="4">
      <requirements>
        Agent coordination from phase 3 must be active
        Integration points must be monitored
        Quality gates must be enforced
        MANDATORY: Comprehensive validation before integration
      </requirements>
      <actions>
        Monitor integration points and resolve conflicts
        Validate agent outputs against quality standards
        Coordinate integration testing and validation
        Ensure comprehensive test coverage across agents
        Perform final integration with conflict resolution
        MANDATORY: Apply universal quality gates
        ENFORCEMENT: Use system/../../system/../../system/quality/universal-quality-gates.md
      </actions>
      <validation>
        Integration conflicts identified and resolved
        Agent outputs meet quality standards
        Integration testing comprehensive and passing
        Final integration successful with validation
        VERIFICATION: Integration results documented with metrics
      </validation>
      <blocking_conditions>
        <condition>Integration conflicts unresolved</condition>
        <condition>Agent outputs fail quality standards</condition>
        <condition>Integration testing incomplete or failing</condition>
      </blocking_conditions>
    </phase>
    
  </implementation>
  
  <agent_specializations>
    <agent_type name="architect_agent">
      <specialization>System design and architectural planning</specialization>
      <responsibilities>
        Design system architecture and component boundaries
        Define interface contracts and integration points
        Make architectural decisions and trade-off analysis
        Ensure architectural consistency and best practices
      </responsibilities>
      <quality_requirements>
        Architecture documentation with clear rationale
        Interface contracts with validation criteria
        Design patterns applied consistently
        Architectural decisions justified with evidence
      </quality_requirements>
    </agent_type>
    <agent_type name="implementation_agent">
      <specialization>Code generation and feature implementation</specialization>
      <responsibilities>
        Generate high-quality code based on specifications
        Implement design patterns and best practices
        Ensure code quality and maintainability
        Optimize performance and efficiency
      </responsibilities>
      <quality_requirements>
        TDD compliance with comprehensive test coverage
        Code quality metrics meeting standards
        Performance benchmarks achieved
        Documentation and comments for maintainability
      </quality_requirements>
    </agent_type>
    <agent_type name="testing_agent">
      <specialization>Quality assurance and comprehensive testing</specialization>
      <responsibilities>
        Design comprehensive test suites and scenarios
        Validate code quality and compliance
        Identify and test edge cases and failure modes
        Conduct performance testing and optimization
      </responsibilities>
      <quality_requirements>
        Test coverage minimum 90% with meaningful tests
        Edge case coverage with failure mode testing
        Performance tests with benchmarks
        Quality gate validation with blocking enforcement
      </quality_requirements>
    </agent_type>
    <agent_type name="integration_agent">
      <specialization>System integration and coordination</specialization>
      <responsibilities>
        Integrate components and resolve conflicts
        Ensure consistency across integrated components
        Optimize integrated system performance
        Validate end-to-end functionality
      </responsibilities>
      <quality_requirements>
        Integration conflicts resolved systematically
        End-to-end testing comprehensive and passing
        Performance optimization with measurable improvements
        System consistency validation with evidence
      </quality_requirements>
    </agent_type>
  </agent_specializations>
  
  <coordination_patterns>
    <pattern name="parallel_development">
      <description>Agents work in parallel on different components</description>
      <implementation>
        Separate git worktrees for isolated development
        Regular synchronization points for integration
        Conflict resolution through automated mediation
        Continuous integration with quality gates
      </implementation>
      <benefits>
        Maximized parallel execution efficiency
        Reduced coordination overhead
        Isolated development environments
        Faster overall development cycles
      </benefits>
    </pattern>
    <pattern name="hierarchical_coordination">
      <description>Architect agent leads with implementation agents</description>
      <implementation>
        Architect defines specifications and interfaces
        Implementation agents work within defined boundaries
        Testing agent validates across all components
        Integration agent coordinates final assembly
      </implementation>
      <benefits>
        Clear responsibility boundaries
        Architectural consistency maintained
        Quality assurance integrated throughout
        Systematic integration approach
      </benefits>
    </pattern>
    <pattern name="collaborative_validation">
      <description>Agents collaborate on validation and quality</description>
      <implementation>
        Cross-agent code review and validation
        Collaborative testing and quality assurance
        Shared responsibility for final quality
        Continuous improvement through feedback
      </implementation>
      <benefits>
        Higher quality through collaboration
        Shared knowledge and learning
        Reduced defects through multiple perspectives
        Continuous improvement culture
      </benefits>
    </pattern>
  </coordination_patterns>
  
  <worktree_management>
    <worktree_strategy>
      <setup>
        Create feature-specific worktrees for each agent
        Establish branch naming conventions
        Configure merge strategies and policies
        Set up continuous integration hooks
      </setup>
      <coordination>
        Regular sync points for integration
        Conflict resolution through automated tools
        Shared branch for integration testing
        Final merge with comprehensive validation
      </coordination>
      <cleanup>
        Automated worktree cleanup after integration
        Branch cleanup with history preservation
        Artifact archival for future reference
        Performance metrics collection
      </cleanup>
    </worktree_strategy>
    <isolation_benefits>
      Parallel development without conflicts
      Independent testing and validation
      Reduced coordination overhead
      Faster development cycles
      Easier rollback and recovery
    </isolation_benefits>
  </worktree_management>
  
  <conflict_resolution>
    <conflict_types>
      <type name="code_conflicts">Merge conflicts in code changes</type>
      <type name="design_conflicts">Conflicting design decisions</type>
      <type name="resource_conflicts">Competing resource usage</type>
      <type name="priority_conflicts">Conflicting task priorities</type>
    </conflict_types>
    <resolution_strategies>
      <strategy name="automated_resolution">
        Use intelligent merge tools for code conflicts
        Apply design pattern consistency checks
        Implement resource allocation algorithms
        Use priority matrices for task conflicts
      </strategy>
      <strategy name="mediated_resolution">
        Escalate to architect agent for design conflicts
        Use integration agent for resource mediation
        Apply framework rules for priority resolution
        Document resolution rationale for learning
      </strategy>
    </resolution_strategies>
  </conflict_resolution>
  
  <performance_optimization>
    <optimization_targets>
      <target name="coordination_efficiency">95% coordination efficiency</target>
      <target name="parallel_execution">80% parallel execution ratio</target>
      <target name="integration_success">99% integration success rate</target>
      <target name="quality_compliance">100% quality gate compliance</target>
    </optimization_targets>
    <monitoring_metrics>
      <metric name="agent_utilization">Percentage of time agents are actively working</metric>
      <metric name="coordination_overhead">Time spent on coordination vs development</metric>
      <metric name="conflict_resolution_time">Average time to resolve conflicts</metric>
      <metric name="integration_cycles">Number of integration attempts needed</metric>
    </monitoring_metrics>
  </performance_optimization>
  
  <quality_enforcement>
    <universal_requirements>
      All agents must comply with TDD requirements
      Quality gates enforced at every integration point
      Comprehensive testing across all agent outputs
      Documentation standards maintained consistently
    </universal_requirements>
    <agent_specific_requirements>
      <architect>Architecture documentation and decision rationale</architect>
      <implementer>Code quality metrics and test coverage</implementer>
      <tester>Comprehensive test suites and validation</tester>
      <integrator>Integration success metrics and validation</integrator>
    </agent_specific_requirements>
  </quality_enforcement>
  
  <integration_points>
    <depends_on>
      system/../../system/../../system/quality/tdd.md for TDD enforcement across agents
      ../../../../../../system/git/worktree-isolation.md for worktree management
      system/../../system/../../system/quality/universal-quality-gates.md for quality enforcement
      ../../system/../../system/quality/critical-thinking.md for complex task decomposition
      meta/multi-agent-swarm-orchestrator.md for advanced coordination
    </depends_on>
    <provides_to>
      /swarm command for multi-agent coordination capabilities
      ../../prompt_eng/../../prompt_eng/patterns/orchestration/coordination-patterns.md for reusable coordination approaches
      ../../development/feature-development.md for large-scale development
      All commands for complex task decomposition patterns
    </provides_to>
  </integration_points>
  
  <quality_gates enforcement="strict">
    <gate name="task_decomposition" requirement="Task properly decomposed with clear agent responsibilities"/>
    <gate name="worktree_isolation" requirement="Git worktrees properly isolated for parallel development"/>
    <gate name="agent_coordination" requirement="Agent coordination functioning with measurable progress"/>
    <gate name="integration_validation" requirement="Integration successful with comprehensive validation"/>
  </quality_gates>
  
</module>
```

## Multi-Agent Coordination Examples

### Example 1: Authentication System Development
**Task**: Implement complete authentication system with SSO, API keys, and RBAC
**Decomposition**: 
- Architect: Design auth architecture and security model
- Implementation: Parallel development of auth components
- Testing: Security testing and edge case validation
- Integration: Component integration and end-to-end testing
**Worktree Strategy**: Feature branches for each component with isolated development
**Result**: Complete authentication system with 95% coordination efficiency

### Example 2: Performance Optimization Project
**Task**: Optimize application performance across database, API, and frontend
**Decomposition**:
- Architect: Performance architecture and optimization strategy
- Implementation: Parallel optimization across different layers
- Testing: Performance benchmarking and regression testing
- Integration: End-to-end performance validation
**Worktree Strategy**: Component-specific worktrees with performance testing integration
**Result**: 60% performance improvement through coordinated optimization

### Example 3: Microservices Refactoring
**Task**: Refactor monolithic application into microservices architecture
**Decomposition**:
- Architect: Microservices architecture and service boundaries
- Implementation: Parallel service extraction and implementation
- Testing: Service integration and contract testing
- Integration: Service mesh setup and deployment coordination
**Worktree Strategy**: Service-specific worktrees with independent development
**Result**: Successful microservices architecture with maintained functionality

### Example 4: Data Pipeline Development
**Task**: Build comprehensive data pipeline with ETL, monitoring, and analytics
**Decomposition**:
- Architect: Data architecture and pipeline design
- Implementation: Parallel development of pipeline components
- Testing: Data quality validation and performance testing
- Integration: End-to-end pipeline integration and monitoring
**Worktree Strategy**: Component-specific worktrees with data validation integration
**Result**: Robust data pipeline with comprehensive monitoring and quality assurance

## Anti-patterns to Avoid
- Poor task decomposition leading to agent conflicts
- Insufficient worktree isolation causing development conflicts
- Inadequate coordination protocols
- Skipping quality gates for faster integration
- Not enforcing TDD across all agents
- Insufficient conflict resolution mechanisms

## Multi-Agent Success Checklist
- [ ] Task properly decomposed with clear agent responsibilities
- [ ] Git worktrees set up for isolated parallel development
- [ ] Agent specializations activated with defined roles
- [ ] Coordination protocols established and functioning
- [ ] TDD enforced across all agents with quality gates
- [ ] Integration points monitored with conflict resolution
- [ ] Quality standards maintained across all agent outputs
- [ ] Performance metrics collected and optimization applied