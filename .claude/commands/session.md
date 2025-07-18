# Session Command - Work on long projects with context tracking

**Description**: Work on long projects with context tracking

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-18   | stable | 85%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/session-management-pattern.md</delegation_target>
  <orchestration_flow>
    1. Initialize or resume long-running development session
    2. Delegate to session management pattern module
    3. Track progress with GitHub issues and context preservation
    4. Manage session state and resumption capability
  </orchestration_flow>
  <session_features>
    <github_integration>Creates GitHub issues for >10 step tasks</github_integration>
    <context_preservation>Maintains context across session boundaries</context_preservation>
    <progress_tracking>Tracks completion and milestone progress</progress_tracking>
    <resume_capability>Resumes interrupted sessions with full context</resume_capability>
  </session_features>
</command_orchestration>
```

## Usage

**Start long-running project:**
```
/session "Implement complete e-commerce platform"
```

**Resume interrupted work:**
```
/session "Continue payment system development"
```

**Track complex development:**
```
/session "Migrate legacy system to microservices"
```

## What This Command Does

- **Context tracking**: Maintains development context across sessions
- **GitHub integration**: Creates issues for complex tasks with progress tracking
- **Resume capability**: Picks up where you left off with full context
- **Progress management**: Tracks milestones and completion status
- **Long-term focus**: Perfect for multi-day or multi-week development

## Examples

- `/session "Build mobile app"` - Manages complete mobile app development with progress tracking
- `/session "Refactor monolith"` - Tracks complex refactoring with multiple phases
- `/session "Performance optimization"` - Manages systematic performance improvements