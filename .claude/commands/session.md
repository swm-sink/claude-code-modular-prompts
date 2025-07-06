# /session Command - AI Session Management via GitHub Issues

Elegant session management using GitHub's native issue tracking system.

## Usage
```
/session [action] [options]
```

## Actions

### `/session start [title]`
Creates a new GitHub issue for the current AI coding session.

Example:
```
/session start "Implement OAuth2 authentication"
```

This will:
1. Create a new issue with the AI session template
2. Add labels: `ai-session`, `active`
3. Return the issue number for reference in commits

### `/session update [message]`
Updates the current active session with progress.

Example:
```
/session update "Completed user model, starting on auth middleware"
```

### `/session link [pr_number]`
Links a PR to the current session.

Example:
```
/session link 123
```

### `/session complete [outcome]`
Completes the current session with an outcome.

Example:
```
/session complete successful
/session complete partial "Blocked by API rate limits"
```

### `/session list [filter]`
Lists AI sessions with optional filters.

Examples:
```
/session list              # All sessions
/session list active       # Active sessions only
/session list completed    # Completed sessions
/session list today        # Today's sessions
```

### `/session view [issue_number]`
Views a specific session's details.

Example:
```
/session view 123
```

## Workflow Integration

### Starting Development
```bash
# 1. Start a new session
/session start "Refactor payment processing"

# 2. The command returns: "Created session #456"

# 3. Reference in commits
git commit -m "refactor: extract payment gateway interface [#456]"
```

### During Development
```bash
# Update with progress
/session update "Extracted interface, writing tests"

# Link related work
/session link 789  # Links PR #789 to session
```

### Completing Work
```bash
# Mark as complete with outcome
/session complete successful
```

## Advanced Usage

### Batch Operations
```bash
# Start session and create branch
/session start "Feature: User notifications" --branch feature/notifications

# Update with code metrics
/session update --metrics "Added 5 files, 87% test coverage"
```

### Search Sessions
```bash
# Find sessions by content
/session search "authentication"

# Find sessions by label
/session list --label "context:backend"

# Find sessions by date range
/session list --since "2024-01-01" --until "2024-01-31"
```

## Implementation Details

The command uses GitHub CLI (`gh`) to:
1. Create issues with the AI session template
2. Manage labels programmatically
3. Link commits and PRs automatically
4. Search and filter sessions

## Benefits

1. **Zero Setup** - Works with any GitHub repository
2. **Native Integration** - Automatic linking to code changes
3. **Team Visibility** - All sessions visible to collaborators
4. **Searchable History** - Full-text search across all sessions
5. **No External Dependencies** - Uses only GitHub's built-in features

## Examples

### Complex Feature Development
```bash
# Start session for major feature
/session start "Implement real-time collaboration"

# Break down into sub-tasks
/session update "Phase 1: WebSocket infrastructure"
# ... development work ...
/session update "Phase 2: Conflict resolution"
# ... more work ...

# Complete with detailed outcome
/session complete successful "All features implemented, 95% test coverage"
```

### Bug Fix Session
```bash
# Quick bug fix session
/session start "Fix: Memory leak in image processor"
# ... investigation and fix ...
/session complete successful "Leak fixed, added memory profiling tests"
```

### Research Session
```bash
# Research and exploration
/session start "Research: Evaluate caching strategies"
/session update "Benchmarked Redis vs Memcached"
/session update "Tested hybrid approach"
/session complete successful "Recommendation: Redis for our use case"
```