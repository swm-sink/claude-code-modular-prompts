# Usage Examples

## Core Commands

### Task Execution
```
/task "add form validation to the signup page"
/task "refactor database connection pool"
/task "implement Redis caching layer"
```

### Code Analysis
```
/analyze-code                    # Full codebase analysis
/analyze-code security          # Security-focused analysis
/analyze-code performance       # Performance bottlenecks
```

### Quick Development
```
/quick-dev --review auth.py     # Review specific file
/quick-dev --debug "login fails" # Debug an issue
/quick-dev --optimize queries   # Optimize database queries
```

## Context-Aware Command System

### Quick Commands (30 seconds)
```
/quick-command search "find all TODO comments"
/quick-command analyze "check for security issues"
/quick-command transform "convert callbacks to async/await"
```

### Guided Development (5 minutes)
```
/build-command search --with-context --recursive
/build-command analyze --security-focus --output-json
/build-command validate --strict --auto-fix
```

### Advanced Workflows (15-30 minutes)
```
/assemble-command security-audit
/assemble-command data-pipeline
/assemble-command code-migration
```

## Specialized Workflows

### Database Operations
```
/db-migrate create users_table
/db-backup production
/db-seed test-data
/db-restore backup-2025-08-01
```

### Testing
```
/test-unit user-service
/test-integration api
/test-e2e checkout-flow
/mutation UserModel
```

### DevOps
```
/ci-setup github-actions
/deploy staging
/pipeline status
/cd-rollback production
```

## Meta Commands

### Project Adaptation
```
/adapt-to-project               # Get customization checklist
/replace-placeholders           # List all placeholders
/validate-adaptation            # Verify setup
```

### Command Discovery
```
/help                          # General help
/help task                     # Specific command help
/find-commands testing         # Find testing-related commands
/help --all                    # List all commands
```

## Real-World Scenarios

### Starting a New Feature
```
# 1. Plan the feature
/task "plan user notifications feature"

# 2. Create the database schema
/db-migrate create notifications_table

# 3. Implement the backend
/task "implement notification service"

# 4. Add tests
/test-unit NotificationService
/test-integration notifications-api

# 5. Deploy
/deploy staging
```

### Debugging Production Issue
```
# 1. Analyze the problem
/analyze-code performance

# 2. Check monitoring
/monitor-alerts production

# 3. Debug specific area
/quick-dev --debug "high memory usage"

# 4. Implement fix
/task "optimize memory usage in image processing"

# 5. Test the fix
/test-integration image-processor

# 6. Deploy with rollback plan
/deploy production --with-rollback
```

### Code Quality Improvement
```
# 1. Initial assessment
/quality

# 2. Security audit
/secure-audit

# 3. Find code smells
/analyze-code quality

# 4. Refactor systematically
/task "refactor user authentication module"

# 5. Validate changes
/validate-component auth
/test
```

## Tips

1. **Start Simple**: Use `/quick-*` commands for immediate productivity
2. **Customize Gradually**: Replace placeholders as you discover needs
3. **Combine Commands**: Chain commands for complex workflows
4. **Use Help**: `/help [command]` shows detailed usage
5. **Validate Often**: `/validate-adaptation` ensures correctness

## Advanced Patterns

### Multi-Stage Processing
```
# Stage 1: Discovery
/find-commands data

# Stage 2: Analysis
/analyze-system data-flow

# Stage 3: Transformation
/assemble-command data-pipeline
```

### Team Collaboration
```
# Share your customizations
/share-adaptation

# Import patterns from teammates
/import-pattern colleague-patterns.md

# Sync with upstream changes
/sync-from-reference
```

For more examples, see the template files in `.claude/commands/`