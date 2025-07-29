---
name: /dag-orchestrate
description: "Execute tasks using Directed Acyclic Graph orchestration with adaptive agent spawning"
usage: /dag-orchestrate [task with dependencies and conditional paths]
tools: Task, TodoWrite, Read, Write, Edit, Bash, Grep, Glob
test_coverage: 0%
---
<command_file>
<purpose>
Orchestrate complex workflows using DAG patterns where agents are dynamically spawned based on task dependencies and runtime conditions.
</purpose>
<arguments>
- workflow: Description of the workflow with dependencies
- conditions: Optional conditions for adaptive spawning
</arguments>
<examples>
/dag-orchestrate Build and deploy system with conditional testing based on code changes
/dag-orchestrate Analyze → Plan → Implement → Test → Deploy pipeline with parallel branches
/dag-orchestrate Multi-stage data processing with dynamic scaling based on data volume
</examples>
<claude_prompt>
You are implementing a DAG-based orchestration system with adaptive agent spawning. Your role is to analyze dependencies, create an execution graph, and dynamically spawn agents based on conditions.
Workflow: $ARGUMENTS
<include>components/validation/validation-framework.md</include>
<include>components/orchestration/dependency-analysis.md</include>
## DAG Orchestration Protocol
### Phase 1: Workflow Analysis
Analyze the workflow to create a Directed Acyclic Graph:
1. **Identify Nodes**: Each discrete task becomes a node
2. **Map Dependencies**: Determine prerequisite relationships
3. **Detect Parallelism**: Find tasks that can run concurrently
4. **Define Conditions**: Identify branching logic and adaptive rules
### Phase 2: DAG Construction
Build the execution graph:
```json
{
  "dag_id": "unique_identifier",
  "nodes": [
    {
      "id": "node_id",
      "task": "task_description",
      "agent_type": "specialized_agent",
      "dependencies": ["parent_node_ids"],
      "conditions": {
        "spawn_if": "condition_expression",
        "skip_if": "condition_expression",
        "scale_factor": "adaptive_scaling_rule"
      },
      "status": "pending|ready|running|complete|skipped",
      "results": {}
    }
  ],
  "edges": [
    {"from": "node_id", "to": "node_id", "condition": "optional"}
  ],
  "execution_state": {
    "completed_nodes": [],
    "active_nodes": [],
    "pending_nodes": []
  }
}
```
### Phase 3: Adaptive Execution Engine
Implement the DAG execution with adaptive spawning:
1. **Initialization**:
   - Mark all nodes with no dependencies as "ready"
   - Initialize execution state tracking
2. **Execution Loop**:
   ```
   while (pending or active nodes exist):
     - Identify ready nodes (dependencies satisfied)
     - Evaluate spawn conditions for each ready node
     - Spawn agents for nodes meeting conditions
     - Monitor active agents for completion
     - Update node status and propagate to dependents
     - Check for adaptive scaling needs
   ```
3. **Adaptive Spawning Rules**:
   - **Load-based**: Spawn more agents if workload exceeds threshold
   - **Time-based**: Spawn parallel agents if deadline approaches
   - **Resource-based**: Adjust based on available resources
   - **Quality-based**: Spawn verification agents if quality drops
<include>components/orchestration/task-execution.md</include>
### Phase 4: Dynamic Graph Modification
Support runtime DAG modifications:
1. **Add Nodes**: Insert new tasks based on discoveries
2. **Skip Nodes**: Bypass tasks based on conditions
3. **Modify Dependencies**: Adjust based on results
4. **Scale Nodes**: Spawn multiple agents for bottlenecks
### Phase 5: Progress Monitoring
Track and report execution state:
1. **Visual Progress**: Show DAG with node states
2. **Performance Metrics**: Execution time per node
3. **Resource Usage**: Agent utilization
4. **Bottleneck Detection**: Identify slow paths
## Execution Strategies
### Topological Sort Execution
- Process nodes in dependency order
- Maximize parallelism at each level
- Ensure no circular dependencies
### Critical Path Optimization
- Identify longest execution path
- Prioritize critical path nodes
- Allocate more resources to bottlenecks
### Fault Tolerance
- Checkpoint completed nodes
- Retry failed nodes with backoff
- Provide alternative execution paths
## Quality Gates
- All dependencies properly resolved
- No circular dependencies in DAG
- All required nodes complete successfully
- Adaptive spawning within resource limits
- Execution time within acceptable bounds
Report the DAG execution with:
- Execution graph visualization
- Node execution times and statuses
- Adaptive spawning decisions made
- Overall workflow performance metrics
- Any optimizations for future runs
</claude_prompt>
</command_file>