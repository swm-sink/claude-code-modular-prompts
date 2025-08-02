# Task Summary Component

**Purpose**: Generate comprehensive task completion summaries with measurable results and actionable next steps.

**Usage**: 
- Review task completion status and document specific measurable results
- Identify and categorize issues, blockers, and incomplete tasks
- Provide clear, prioritized next steps based on current status
- Validate summary completeness against original objectives
- Format output as structured report with clear sections

**Compatibility**: 
- **Works with**: completion-tracker, error-handler, progress-indicator, output-formatter
- **Requires**: Task list and completion status data
- **Conflicts**: None (universal reporting component)

**Implementation**:
```pseudocode
tasks = get_task_completion_data()
completed = analyze_completed_tasks_with_results(tasks)
issues = categorize_blockers_and_problems(tasks)
next_steps = generate_prioritized_action_items(tasks)
report = format_structured_summary(completed, issues, next_steps)
return {summary: report, completion_rate: percentage, next_actions: prioritized}
```

**Category**: atomic | **Complexity**: simple | **Time**: 30 minutes