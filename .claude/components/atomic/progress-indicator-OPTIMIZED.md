# Progress Indicator Component

**Purpose**: Display clear progress updates and status tracking for long-running tasks and multi-step workflows.

**Usage**: 
- Initialize progress tracking with total step count and task description
- Generate timestamped progress messages at key milestones
- Calculate and display percentage completion for quantifiable tasks
- Provide specific status updates for current operation context
- Handle progress tracking errors with graceful fallback messaging

**Compatibility**: 
- **Works with**: workflow-coordinator, task-summary, error-handler, completion-tracker
- **Requires**: Progress source from workflow coordinator or state manager
- **Conflicts**: user-confirmation (conflicting interface patterns)

**Implementation**:
```pseudocode
total_steps = initialize_progress_tracking(task_name, step_count)
for each milestone:
    current_progress = calculate_percentage(completed_steps, total_steps)
    status_message = generate_timestamped_update(current_progress, operation)
    display_progress_indicator(status_message)
final_summary = generate_completion_summary(elapsed_time, results)
```

**Category**: atomic | **Complexity**: simple | **Time**: 5 minutes