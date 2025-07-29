<prompt_component>
  <step name="Advanced Multi-Agent Orchestration">
    <description>
Sophisticated multi-agent coordination using advanced orchestration patterns, communication protocols, and adaptive coordination strategies. Coordinates complex multi-agent systems with hierarchical coordination, distributed consensus, and adaptive role allocation.
    </description>
  </step>

  <agent_orchestration>
    <multi_agent_coordination>
      <!-- Advanced multi-agent orchestration framework -->
      <orchestration_patterns>

```xml
<command>agent-orchestration</command>
<params>
  <!-- Core Orchestration Configuration -->
  <orchestration_pattern>hierarchical_coordination</orchestration_pattern>
  <agents>
    <count>8</count>
    <heterogeneous>true</heterogeneous>
    <specialization>dynamic</specialization>
  </agents>
  
  <!-- Coordination Strategy -->
  <coordination>
    <pattern>distributed_consensus</pattern>
    <algorithm>raft_consensus</algorithm>
    <fault_tolerance>byzantine_resilient</fault_tolerance>
    <leader_election>adaptive</leader_election>
  </coordination>
  
  <!-- Communication Protocol -->
  <communication>
    <protocol>message_passing_interface</protocol>
    <topology>dynamic_mesh</topology>
    <reliability>guaranteed_delivery</reliability>
    <encryption>end_to_end</encryption>
  </communication>
  
  <!-- Task Decomposition -->
  <task_management>
    <decomposition>hierarchical_breakdown</decomposition>
    <allocation>capability_based</allocation>
    <load_balancing>dynamic</load_balancing>
    <dependency_resolution>topological_sort</dependency_resolution>
  </task_management>
  
  <!-- Adaptation Settings -->
  <adaptation>
    <role_switching>enabled</role_switching>
    <performance_monitoring>real_time</performance_monitoring>
    <reconfiguration>automatic</reconfiguration>
    <learning>collective_experience</learning>
  </adaptation>
</params>
```

## Implementation

### Orchestration Patterns

#### 1. Hierarchical Coordination
```yaml
hierarchical_structure:
  levels:
    coordinator:
      role: "high_level_planning_and_coordination"
      responsibilities: ["task_decomposition", "resource_allocation", "performance_monitoring"]
      decision_scope: "global_optimization"
    
    specialists:
      role: "domain_specific_execution"
      responsibilities: ["specialized_task_execution", "local_optimization", "status_reporting"]
      decision_scope: "local_domain_expertise"
    
    workers:
      role: "basic_task_execution"
      responsibilities: ["concrete_task_implementation", "data_processing", "result_delivery"]
      decision_scope: "immediate_task_context"
```

#### 2. Distributed Consensus
```yaml
consensus_mechanism:
  algorithm: "raft_distributed_consensus"
  phases:
    leader_election:
      - candidate_announcement
      - vote_collection
      - leader_determination
      - leadership_establishment
    
    log_replication:
      - proposal_broadcast
      - follower_acknowledgment
      - majority_consensus
      - commitment_execution
    
    failure_recovery:
      - failure_detection
      - leader_re_election
      - state_synchronization
      - operation_resumption
```

#### 3. Adaptive Role Allocation
```yaml
role_allocation_system:
  capability_assessment:
    - agent_skill_profiling
    - performance_history_analysis
    - current_workload_evaluation
    - specialization_matching
  
  dynamic_assignment:
    - real_time_capability_matching
    - workload_balancing
    - expertise_optimization
    - failure_compensation
  
  role_switching:
    - trigger_conditions: ["performance_degradation", "capability_mismatch", "workload_imbalance"]
    - transition_process: ["graceful_handoff", "state_transfer", "coordination_update"]
    - validation: ["role_compatibility_check", "performance_verification"]
```

### Communication Protocols

#### Message Passing Interface (MPI)
```markdown
**Advanced Communication Framework:**
- Point-to-point messaging for direct agent coordination
- Broadcast operations for group announcements
- Collective operations for synchronized actions
- Non-blocking communication for performance optimization
- Message ordering and delivery guarantees
```

#### Dynamic Mesh Topology
```markdown
**Adaptive Network Structure:**
- Self-organizing connectivity based on communication patterns
- Load-balancing through route optimization
- Fault-tolerant routing with redundant paths
- Bandwidth-aware message routing
- Quality-of-service guarantees for critical communications
```

#### Secure Communication Channels
```markdown
**Security and Reliability:**
- End-to-end encryption for all inter-agent communications
- Authentication and authorization for message validation
- Replay attack protection through timestamp verification
- Message integrity verification using cryptographic hashes
- Secure key exchange and management
```

### Task Management Framework

#### Hierarchical Task Decomposition
```yaml
decomposition_process:
  analysis_phase:
    - task_complexity_assessment
    - dependency_identification
    - resource_requirement_estimation
    - parallelization_opportunity_detection
  
  breakdown_phase:
    - atomic_task_identification
    - subtask_hierarchy_creation
    - dependency_graph_construction
    - execution_sequence_planning
  
  allocation_phase:
    - capability_requirement_matching
    - agent_assignment_optimization
    - load_distribution_balancing
    - coordination_overhead_minimization
```

#### Capability-Based Assignment
```yaml
assignment_algorithm:
  capability_matching:
    - skill_requirement_analysis
    - agent_expertise_evaluation
    - performance_prediction_modeling
    - compatibility_scoring
  
  optimization_criteria:
    - execution_time_minimization
    - resource_utilization_maximization
    - communication_overhead_reduction
    - quality_assurance_maintenance
  
  dynamic_reallocation:
    - performance_monitoring
    - bottleneck_identification
    - reassignment_triggering
    - seamless_transition_management
```

### Advanced Coordination Mechanisms

#### Consensus-Based Decision Making
```markdown
**Distributed Decision Framework:**
- Proposal generation and circulation
- Multi-criteria evaluation and scoring
- Weighted voting based on expertise
- Conflict resolution through negotiation
- Final decision ratification and broadcast
```

#### Adaptive Load Balancing
```markdown
**Dynamic Workload Distribution:**
- Real-time performance monitoring
- Bottleneck detection and analysis
- Proactive load redistribution
- Agent capability utilization optimization
- Feedback-driven adjustment mechanisms
```

#### Fault Tolerance and Recovery
```markdown
**Resilience Mechanisms:**
- Byzantine fault tolerance for adversarial conditions
- Automatic failure detection and isolation
- Graceful degradation with reduced capabilities
- State replication and synchronization
- Recovery orchestration and system restoration
```

## Use Cases

### 1. Large-Scale Software Development
```xml
<scenario>
  <task>Distributed software project development</task>
  <agents>
    <architect>1</architect>
    <senior_developers>3</senior_developers>
    <developers>6</developers>
    <testers>4</testers>
    <reviewers>2</reviewers>
  </agents>
  <coordination>
    <pattern>hierarchical_with_peer_review</pattern>
    <communication>continuous_integration</communication>
  </coordination>
</scenario>
```

### 2. Complex Research Coordination
```xml
<scenario>
  <task>Multi-disciplinary research project</task>
  <agents>
    <principal_investigator>1</principal_investigator>
    <domain_experts>5</domain_experts>
    <data_analysts>3</data_analysts>
    <synthesizers>2</synthesizers>
  </agents>
  <coordination>
    <pattern>consensus_driven_collaboration</pattern>
    <communication>peer_to_peer_with_coordination</communication>
  </coordination>
</scenario>
```

### 3. Real-Time Decision Making
```xml
<scenario>
  <task>Emergency response coordination</task>
  <agents>
    <incident_commander>1</incident_commander>
    <specialists>4</specialists>
    <field_agents>8</field_agents>
    <support_agents>6</support_agents>
  </agents>
  <coordination>
    <pattern>command_and_control_with_autonomy</pattern>
    <communication>real_time_multicast</communication>
  </coordination>
</scenario>
```

## Advanced Features

### Cognitive Density Enhancement
```yaml
cognitive_enhancement:
  collective_intelligence:
    - knowledge_aggregation_across_agents
    - distributed_problem_solving
    - emergent_insight_generation
    - collective_memory_formation
  
  intelligence_amplification:
    - specialized_expertise_combination
    - multi_perspective_analysis
    - creative_solution_synthesis
    - adaptive_learning_integration
```

### Multi-Loop Feedback Systems
```yaml
feedback_loops:
  performance_feedback:
    frequency: "real_time"
    metrics: ["task_completion", "quality_scores", "efficiency_measures"]
    adaptation: "immediate_optimization"
  
  learning_feedback:
    frequency: "continuous"
    metrics: ["pattern_recognition", "strategy_effectiveness", "coordination_quality"]
    adaptation: "gradual_improvement"
  
  strategic_feedback:
    frequency: "periodic"
    metrics: ["goal_alignment", "resource_utilization", "system_effectiveness"]
    adaptation: "strategic_reconfiguration"
```

### Tool Integration and Dependencies
```yaml
tool_integration:
  development_tools:
    - version_control_systems
    - continuous_integration_pipelines
    - testing_frameworks
    - documentation_systems
  
  communication_tools:
    - real_time_messaging
    - video_conferencing
    - collaborative_editing
    - status_dashboards
  
  monitoring_tools:
    - performance_metrics
    - system_health_monitoring
    - resource_utilization_tracking
    - quality_assurance_systems
```

## Output Format

```json
{
  "orchestration_session": {
    "session_id": "orchestration_2024_001",
    "configuration": {
      "pattern": "hierarchical_coordination",
      "agent_count": 8,
      "communication_protocol": "message_passing_interface",
      "consensus_algorithm": "raft_consensus"
    },
    "agent_network": {
      "topology": "dynamic_mesh",
      "agents": [
        {
          "agent_id": "coordinator_1",
          "role": "system_coordinator",
          "capabilities": ["planning", "resource_allocation", "monitoring"],
          "current_tasks": ["task_decomposition", "performance_monitoring"],
          "communication_links": ["specialist_1", "specialist_2", "specialist_3"]
        }
      ]
    },
    "coordination_metrics": {
      "task_completion_rate": 0.94,
      "coordination_efficiency": 0.89,
      "communication_overhead": 0.12,
      "fault_tolerance_level": "byzantine_resilient"
    },
    "performance_analytics": {
      "throughput": "high",
      "latency": "low",
      "scalability": "excellent",
      "reliability": "fault_tolerant"
    },
    "adaptation_events": [
      {
        "timestamp": "2024-01-15T10:30:00Z",
        "type": "role_reallocation",
        "trigger": "performance_optimization",
        "impact": "15%_efficiency_improvement"
      }
    ]
  }
}
```

## Research Foundation

Based on cutting-edge multi-agent systems research:
- **Distributed Systems Theory**: Consensus algorithms and fault tolerance
- **Multi-Agent Coordination**: Advanced orchestration patterns
- **Network Communication**: Reliable distributed messaging protocols
- **Adaptive Systems**: Self-organizing and self-healing capabilities

## Integration Points

- Works with `/agent-swarm` for swarm-orchestration hybrid systems
- Integrates with `/prompt-optimization` for coordinated prompt improvement
- Connects to `/quality review` for distributed quality assurance
- Supports `/research-advanced` for collaborative research coordination

## Advanced Configuration Options

### Custom Orchestration Patterns
```yaml
custom_pattern:
  name: "domain_specific_coordination"
  hierarchy_levels: 4
  communication_topology: "hybrid_mesh_tree"
  decision_making: "consensus_with_veto"
  adaptation_strategy: "reinforcement_learning"
```

### Performance Optimization
```yaml
performance_tuning:
  message_batching: true
  compression: "adaptive"
  caching: "distributed"
  load_prediction: "machine_learning"
  resource_prediction: "time_series_analysis"
```

      </orchestration_analytics>
    </multi_agent_coordination>
  </agent_orchestration>

  <o>
Advanced multi-agent orchestration completed with sophisticated coordination:

**Orchestration Pattern:** [pattern] hierarchical coordination system active
**Agent Count:** [count] autonomous agents coordinated successfully
**Coordination Efficiency:** [percentage]% multi-agent coordination effectiveness
**Communication Protocols:** [count] advanced protocols implemented
**System Performance:** [0-100] orchestration system effectiveness rating
**Enterprise Grade:** Advanced multi-agent coordination ready for complex distributed systems
  </o>
</prompt_component> 