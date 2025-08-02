# Completion Tracker Component

**Purpose**: Track task completion status and calculate overall progress for multi-task workflows.

**Usage**: 
- Monitor individual task completion status across workflows
- Calculate overall progress percentages and remaining work
- Identify blockers and dependencies preventing completion
- Generate progress reports and completion summaries
- Trigger notifications when milestones are reached

**Compatibility**: 
- **Works with**: progress-indicator, state-manager, task-summary, workflow-coordinator
- **Requires**: Task definitions from workflow-coordinator
- **Conflicts**: user-confirmation (different tracking paradigms)

**Implementation**:
```pseudocode
tasks = get_task_list(workflow)
completed = count_completed_tasks(tasks)
progress = (completed / total_tasks) * 100
blockers = identify_blocked_tasks(tasks)
return {progress: progress, remaining: total_tasks - completed, blockers: blockers}
```

**Category**: atomic | **Complexity**: moderate | **Time**: 15 minutes