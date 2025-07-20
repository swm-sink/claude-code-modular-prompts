# /flow schedule - Workflow Scheduling Command

**Purpose**: Schedule workflows for future execution with automated triggers and recurring patterns.

## Usage
```bash
/flow schedule [workflow-name] [--at "YYYY-MM-DDTHH:MM:SSZ"] [--cron "* * * * *"]
```

## Workflow

The `/flow schedule` command follows a systematic process to schedule workflows.

```xml
<scheduling_workflow>
  <step name="Create Schedule Entry">
    <description>Create a new schedule entry for the specified workflow, including its trigger conditions (time-based, event-based, or condition-based) and recurring patterns.</description>
  </step>
  
  <step name="Validate & Queue Schedule">
    <description>Validate the timing constraints and dependencies of the schedule, and then add it to the execution scheduler's queue.</description>
  </step>
  
  <step name="Monitor & Notify">
    <description>Monitor upcoming executions, track their status, and provide notifications for status updates and reminders.</description>
  </step>
</scheduling_workflow>
```

## Trigger Types
- **Time-based**: Specific datetime or cron expression.
- **Event-based**: Triggered by events like file changes or Git hooks.
- **Condition-based**: Triggered when specific conditions are met (e.g., tests pass, build succeeds).
- **Recurring**: Predefined patterns such as daily builds, weekly reports, or monthly cleanups.

## Schedule Examples
```bash
# One-time execution
/flow schedule deploy-staging --at "2025-07-21T14:30:00Z"

# Daily builds
/flow schedule nightly-build --cron "0 2 * * *"

# Recurring reports
/flow schedule weekly-report --recurring weekly

# Conditional trigger
/flow schedule integration-tests --trigger "on:push:main"
``` 