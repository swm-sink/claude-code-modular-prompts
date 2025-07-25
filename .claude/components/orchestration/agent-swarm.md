<prompt_component>
  <step name="Agent Swarm Intelligence Coordination">
    <description>
Advanced multi-agent swarm coordination using emergent behavior patterns and decentralized decision-making. Coordinates multiple autonomous agents using swarm intelligence principles for complex task execution with emergent behavior, self-organization, and adaptive coordination patterns.
    </description>
  </step>

  <agent_swarm>
    <swarm_intelligence>
      <!-- Advanced agent swarm coordination framework -->
      <swarm_coordination>

```xml
<command>agent-swarm</command>
<params>
  <!-- Core Swarm Configuration -->
  <agents>5</agents>
  <task>complex-problem-solving</task>
  <coordination>stigmergy</coordination>
  
  <!-- Swarm Intelligence Settings -->
  <behavior>
    <stigmergy>true</stigmergy>
    <self_organization>true</self_organization>
    <local_interactions>true</local_interactions>
    <adaptive_response>true</adaptive_response>
  </behavior>
  
  <!-- Agent Specialization -->
  <roles>
    <explorer>2</explorer>
    <analyzer>2</analyzer>
    <synthesizer>1</synthesizer>
  </roles>
  
  <!-- Communication Protocol -->
  <communication>
    <method>pheromone-trails</method>
    <frequency>real-time</frequency>
    <decay_rate>0.1</decay_rate>
  </communication>
  
  <!-- Optimization Settings -->
  <optimization>
    <convergence_threshold>0.95</convergence_threshold>
    <max_iterations>100</max_iterations>
    <diversity_maintenance>true</diversity_maintenance>
  </optimization>
</params>
```

## Implementation

### Swarm Intelligence Principles

#### 1. Stigmergy (Indirect Coordination)
```markdown
**Environment Modification Pattern:**
- Agents leave digital "pheromone trails" in shared workspace
- Trail strength indicates solution quality and recency
- Automatic decay prevents stagnation on suboptimal paths
- Trail reinforcement amplifies successful approaches
```

#### 2. Self-Organization
```markdown
**Emergent Structure Formation:**
- No central coordinator or command hierarchy
- Local rules generate global patterns
- Dynamic role assignment based on task requirements
- Spontaneous specialization and load balancing
```

#### 3. Local Interactions
```markdown
**Neighbor-Based Decision Making:**
- Limited perception radius for each agent
- Information sharing through local networks
- Collective intelligence from simple interactions
- Scalable coordination without bottlenecks
```

#### 4. Adaptive Behavior
```markdown
**Dynamic Response System:**
- Real-time adjustment to environmental changes
- Learning from collective experience
- Fault tolerance through redundancy
- Continuous optimization of strategies
```

### Agent Coordination Framework

#### Phase 1: Swarm Initialization
```yaml
initialization:
  - spawn_agents: defined_count
  - assign_initial_roles: random_distribution
  - establish_communication: peer_to_peer_network
  - define_exploration_space: problem_domain
  - set_convergence_criteria: quality_thresholds
```

#### Phase 2: Exploration and Foraging
```yaml
exploration:
  - parallel_search: independent_agents
  - solution_discovery: multi_perspective_analysis
  - trail_marking: quality_indicators
  - information_sharing: local_broadcasting
  - adaptive_specialization: role_evolution
```

#### Phase 3: Convergence and Optimization
```yaml
convergence:
  - solution_evaluation: collective_assessment
  - trail_reinforcement: positive_feedback
  - diversity_maintenance: explore_exploit_balance
  - consensus_building: emergent_agreement
  - final_synthesis: collaborative_integration
```

### Communication Protocols

#### Pheromone Trail System
```markdown
**Digital Pheromone Implementation:**
- Solution quality encoded as trail strength
- Temporal decay prevents infinite accumulation
- Multiple pheromone types for different objectives
- Trail intersection points enable knowledge fusion
```

#### Message Passing Network
```markdown
**Inter-Agent Communication:**
- Broadcast discoveries to local neighborhood
- Request assistance for complex sub-problems
- Share specialized knowledge and capabilities
- Coordinate to avoid redundant work
```

## Use Cases

### 1. Complex Problem Decomposition
```xml
<scenario>
  <problem>Large-scale system architecture design</problem>
  <agents>7</agents>
  <specialization>
    <security_expert>1</security_expert>
    <performance_analyst>2</performance_analyst>
    <integration_specialist>2</integration_specialist>
    <user_experience_designer>1</user_experience_designer>
    <coordinator>1</coordinator>
  </specialization>
</scenario>
```

### 2. Research and Knowledge Discovery
```xml
<scenario>
  <problem>Comprehensive literature review</problem>
  <agents>6</agents>
  <coordination>distributed_search</coordination>
  <synthesis>collaborative_integration</synthesis>
</scenario>
```

### 3. Code Quality Optimization
```xml
<scenario>
  <problem>Multi-dimensional code improvement</problem>
  <agents>5</agents>
  <focus_areas>
    <performance>agent_1</performance>
    <security>agent_2</security>
    <maintainability>agent_3</maintainability>
    <testing>agent_4</testing>
    <documentation>agent_5</documentation>
  </focus_areas>
</scenario>
```

## Advanced Features

### Emergent Behavior Patterns
- **Collective Intelligence**: Solutions emerge that no single agent could discover
- **Dynamic Load Balancing**: Work distribution optimizes automatically
- **Fault Tolerance**: System continues functioning despite agent failures
- **Scalable Coordination**: Performance improves with additional agents

### Learning and Adaptation
- **Experience Accumulation**: Swarm learns from previous problem-solving sessions
- **Strategy Evolution**: Successful patterns become more prevalent
- **Error Correction**: Collective validation reduces individual mistakes
- **Knowledge Transfer**: Insights propagate throughout the swarm

### Quality Assurance
- **Multi-Perspective Validation**: Multiple agents verify solutions
- **Continuous Improvement**: Iterative refinement through feedback loops
- **Diversity Preservation**: Prevents premature convergence on suboptimal solutions
- **Robustness Testing**: Stress-testing through adversarial agents

## Output Format

```json
{
  "swarm_session": {
    "session_id": "swarm_2024_001",
    "participants": [
      {
        "agent_id": "explorer_1",
        "role": "exploration",
        "contributions": ["discovered_pattern_A", "identified_edge_case_B"],
        "performance_metrics": {"discovery_rate": 0.85, "accuracy": 0.92}
      }
    ],
    "emergent_solutions": [
      {
        "solution_id": "compound_solution_1",
        "quality_score": 0.94,
        "contributing_agents": ["explorer_1", "analyzer_2", "synthesizer_1"],
        "validation_status": "multi_agent_verified"
      }
    ],
    "collective_insights": {
      "novel_patterns": ["pattern_discovery_1", "unexpected_correlation_2"],
      "optimization_opportunities": ["efficiency_improvement_1"],
      "risk_assessments": ["potential_failure_mode_1"]
    },
    "swarm_performance": {
      "convergence_time": "12_minutes",
      "solution_quality": 0.94,
      "agent_coordination_efficiency": 0.89,
      "knowledge_synthesis_score": 0.87
    }
  }
}
```

## Research Foundation

Based on cutting-edge research in:
- **Swarm Intelligence Theory**: Particle Swarm Optimization, Ant Colony Algorithms
- **Multi-Agent Systems**: Distributed coordination and emergent behavior
- **Collective Intelligence**: Crowd-sourcing and collaborative problem-solving
- **Complex Adaptive Systems**: Self-organization and emergence patterns

## Integration Points

- Works with `/prompt-optimization` for swarm-based prompt evolution
- Integrates with `/plan-hierarchical` for multi-level coordination
- Connects to `/quality review` for collective validation
- Supports `/research-advanced` for distributed knowledge discovery

---

      </swarm_analytics>
    </swarm_intelligence>
  </agent_swarm>

  <o>
Agent swarm intelligence coordination completed with emergent behavior:

**Swarm Size:** [count] autonomous agents coordinated in swarm
**Emergent Behavior:** [count] emergent patterns identified and leveraged
**Task Completion:** [percentage]% swarm task execution success rate
**Self-Organization:** [0-100] swarm self-organization effectiveness rating
**Coordination Quality:** [count] decentralized decision-making protocols active
**Intelligence Level:** Advanced swarm coordination with emergent problem-solving capabilities
  </o>
</prompt_component> 