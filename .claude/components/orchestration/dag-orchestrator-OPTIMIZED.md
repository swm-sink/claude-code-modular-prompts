# DAG Orchestrator

**Purpose**: Advanced workflow orchestration using Directed Acyclic Graphs with dependency modeling, parallel optimization, and real-time monitoring.

**Usage**: 
- Model complex workflows as DAG structures with task dependencies
- Validate workflow integrity and detect circular dependencies
- Execute tasks in parallel using topological sorting optimization
- Monitor real-time performance with bottleneck detection
- Handle failures with automatic recovery and rescheduling

**Compatibility**: 
- **Works with**: task-planning, dependency-analysis, task-execution, progress-tracking
- **Requires**: Complex multi-command workflows with dependencies
- **Conflicts**: quick-command (complexity mismatch), user-confirmation (automation conflict)

**Implementation**:
```python
# Build DAG from workflow definition
def create_workflow_dag(tasks, dependencies):
    dag = build_dependency_graph(tasks, dependencies)
    validate_acyclic_property(dag)
    return optimize_for_parallel_execution(dag)

# Execute workflow with orchestration
def execute_dag_workflow(dag):
    execution_order = topological_sort(dag)
    parallel_batches = identify_parallelizable_tasks(execution_order)
    for batch in parallel_batches:
        execute_tasks_concurrently(batch)
        monitor_progress_and_handle_failures()
    return workflow_completion_report()
```

**Category**: orchestration | **Complexity**: very_high | **Time**: 2 days