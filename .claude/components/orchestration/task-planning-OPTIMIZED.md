# Task Planning

**Purpose**: Analyze and plan complex multi-step tasks with dependency analysis, parallel group identification, and execution strategy optimization.

**Usage**: 
- Decompose complex tasks into atomic, manageable components
- Identify task dependencies and create execution ordering
- Discover parallel execution opportunities and resource optimization
- Estimate resource requirements and completion timelines
- Generate optimized execution strategies for multi-agent coordination

**Compatibility**: 
- **Works with**: agent-orchestration, dependency-analysis, task-execution, agent-swarm
- **Requires**: Complex multi-step tasks requiring strategic decomposition
- **Conflicts**: simple-command (planning overhead not needed)

**Implementation**:
```python
# Analyze and decompose complex task
def create_task_plan(complex_task):
    atomic_tasks = decompose_into_atomic_components(complex_task)
    dependencies = analyze_task_dependencies(atomic_tasks)
    parallel_groups = identify_parallelizable_tasks(atomic_tasks, dependencies)
    resource_estimates = calculate_resource_requirements(atomic_tasks)
    execution_strategy = optimize_execution_order(atomic_tasks, dependencies, parallel_groups)
    return TaskPlan(atomic_tasks, dependencies, parallel_groups, execution_strategy)

# Execute planned workflow
def execute_task_plan(plan):
    for execution_phase in plan.execution_strategy:
        execute_parallel_group(execution_phase.parallel_tasks)
        validate_dependencies_satisfied()
    return completion_report()
```

**Category**: orchestration | **Complexity**: high | **Time**: 2 hours