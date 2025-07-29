---
name: /hierarchical
description: "Orchestrate agents in a tree-like hierarchy with parent-child relationships and delegation"
usage: /hierarchical [complex project requiring multi-level coordination]
tools: Task, TodoWrite, Read, Write, Edit, Bash, Grep, Glob
test_coverage: 0%
---
<command_file>
<purpose>
Implement hierarchical agent orchestration where parent agents delegate to child agents, creating a tree-like structure for complex project management.
</purpose>
<arguments>
- project: The complex project requiring hierarchical decomposition
- depth: Optional maximum hierarchy depth
- delegation: Optional delegation strategy
</arguments>
<examples>
/hierarchical Build complete e-commerce platform with teams for frontend, backend, and infrastructure
/hierarchical Migrate legacy system with architectural, implementation, and testing hierarchies
/hierarchical Implement microservices with service owners delegating to feature teams
</examples>
<claude_prompt>
You are implementing a Hierarchical Orchestration pattern. As the root orchestrator, you will create a tree of agents with parent-child relationships, delegation, and result aggregation.
Project: $ARGUMENTS
<include>components/validation/validation-framework.md</include>
## Hierarchical Orchestration Protocol
### Phase 1: Hierarchy Design
Design the agent hierarchy based on project structure:
```json
{
  "hierarchy_id": "unique_identifier",
  "root": {
    "agent_id": "root_orchestrator",
    "role": "project_coordinator",
    "scope": "entire_project",
    "children": [
      {
        "agent_id": "team_lead_1",
        "role": "subsystem_owner",
        "scope": "specific_subsystem",
        "children": [
          {
            "agent_id": "worker_1_1",
            "role": "feature_developer",
            "scope": "specific_feature",
            "children": []
          }
        ]
      }
    ],
    "context": {
      "shared": {},
      "inherited": {},
      "local": {}
    }
  },
  "communication": {
    "mode": "bidirectional|top-down|bottom-up",
    "protocol": "structured_messages"
  }
}
```
### Phase 2: Role Definition
Define roles at each hierarchy level:
#### Level 1: Root Orchestrator
- Overall project coordination
- Strategic decisions
- Resource allocation
- Progress aggregation
#### Level 2: Team Leads
- Subsystem ownership
- Task breakdown
- Team coordination
- Status reporting
#### Level 3: Specialist Agents
- Feature implementation
- Specific task execution
- Direct work output
- Issue escalation
#### Level 4: Worker Agents
- Atomic task completion
- Detailed implementation
- Ground truth reporting
### Phase 3: Delegation Mechanics
Implement parent-child delegation:
```python
def delegate_to_children(parent_agent, task):
    # Analyze task complexity
    subtasks = decompose_task(task)
    # Create child agents based on needs
    children = []
    for subtask in subtasks:
        child = {
            "role": determine_role(subtask),
            "scope": subtask,
            "parent": parent_agent.id,
            "context": inherit_context(parent_agent)
        }
        children.append(child)
    # Delegate with clear instructions
    for child in children:
        spawn_child_agent(child)
```
### Phase 4: Context Management
Manage context inheritance and scoping:
#### Context Inheritance Rules
1. **Global Context**: Available to all agents
2. **Inherited Context**: Passed from parent to child
3. **Local Context**: Specific to individual agent
4. **Shared Context**: Between siblings
```json
{
  "context_management": {
    "global": {
      "project_goals": "...",
      "constraints": "...",
      "standards": "..."
    },
    "inheritance_chain": [
      {
        "level": 1,
        "context": {"strategic_decisions": "..."}
      },
      {
        "level": 2,
        "context": {"team_guidelines": "..."}
      }
    ],
    "access_control": {
      "read": "all_descendants",
      "write": "self_only",
      "share": "siblings"
    }
  }
}
```
### Phase 5: Communication Protocols
Define how agents communicate in the hierarchy:
#### Upward Communication (Child to Parent)
- Status updates
- Issue escalation
- Result reporting
- Resource requests
#### Downward Communication (Parent to Child)
- Task assignment
- Context updates
- Priority changes
- Guidance
#### Lateral Communication (Between Siblings)
- Coordination
- Conflict resolution
- Resource sharing
- Knowledge transfer
### Phase 6: Execution Flow
Orchestrate the hierarchical execution:
```
1. Root Analysis:
   - Understand project scope
   - Create high-level breakdown
   - Spawn team lead agents
2. Recursive Delegation:
   for each level in hierarchy:
     - Parent analyzes assigned scope
     - Determines if further breakdown needed
     - Spawns child agents if necessary
     - Delegates subtasks
     - Monitors progress
3. Bottom-up Execution:
   - Leaf agents complete atomic tasks
   - Report results to parents
   - Parents aggregate and process
   - Bubble up to root
4. Coordination:
   - Manage inter-dependencies
   - Resolve conflicts
   - Rebalance workloads
   - Adapt to changes
```
### Phase 7: Result Aggregation
Aggregate results up the hierarchy:
#### Aggregation Strategies
1. **Simple Collection**: Gather all child results
2. **Synthesis**: Combine into coherent whole
3. **Conflict Resolution**: Resolve inconsistencies
4. **Quality Assurance**: Validate completeness
```python
def aggregate_child_results(parent, child_results):
    aggregated = {
        "completed_tasks": [],
        "issues": [],
        "metrics": {},
        "recommendations": []
    }
    for result in child_results:
        # Merge completed work
        aggregated["completed_tasks"].extend(result["tasks"])
        # Escalate issues if needed
        for issue in result["issues"]:
            if should_escalate(issue):
                aggregated["issues"].append(issue)
        # Combine metrics
        merge_metrics(aggregated["metrics"], result["metrics"])
    return synthesize(aggregated)
```
## Hierarchy Patterns
### Deep Hierarchy (Many Levels)
- Complex projects
- Clear separation of concerns
- Detailed specialization
- Higher coordination overhead
### Shallow Hierarchy (Few Levels)
- Simpler projects
- Faster communication
- Less overhead
- Limited specialization
### Adaptive Hierarchy
- Dynamic depth based on complexity
- Prune unnecessary levels
- Expand as needed
- Optimal resource usage
## Quality Gates
- Clear role definition at each level
- No orphaned agents
- Proper context inheritance
- Efficient communication paths
- Complete result aggregation
- No lost work in hierarchy
Report hierarchical execution with:
- Hierarchy structure visualization
- Agent role distribution
- Communication flow analysis
- Task completion by level
- Performance metrics per branch
- Overall project success metrics
</claude_prompt>
</command_file>