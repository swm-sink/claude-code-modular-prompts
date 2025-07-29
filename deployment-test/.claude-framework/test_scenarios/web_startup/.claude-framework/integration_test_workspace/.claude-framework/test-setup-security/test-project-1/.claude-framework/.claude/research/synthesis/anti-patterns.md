# Claude Code Anti-Patterns

## Overview
This document identifies common anti-patterns observed in Claude Code usage, based on research of 15+ sources and documented issues.

## 1. Context Management Anti-Patterns

### Context Overload
**Anti-Pattern**: Loading entire codebases or massive documentation into context.

**Problems**:
- Exceeds token limits quickly
- Slows response time
- Reduces relevance
- Increases costs

**Example**:
```markdown
# Bad CLAUDE.md
[500+ lines of API documentation]
[Complete database schema]
[Entire coding standards document]
```

**Solution**:
```markdown
# Good CLAUDE.md
## API Quick Reference
- Auth: See docs/api/auth.md
- Users: GET/POST/PUT /users
- Key endpoints only

## Database
- Schema: db/schema.sql
- Migrations: db/migrations/
```

### Stale Context
**Anti-Pattern**: Outdated information in CLAUDE.md that no longer reflects reality.

**Problems**:
- Misleading instructions
- Failed commands
- Wasted time debugging
- Trust erosion

**Solution**:
- Regular CLAUDE.md reviews
- Date stamps on temporal info
- Remove rather than accumulate

### Context Conflicts
**Anti-Pattern**: Contradicting instructions in different context files.

**Example**:
```
# Global CLAUDE.md
Use 4-space indentation

# Project CLAUDE.md  
Use 2-space indentation
```

**Solution**:
- Clear hierarchy rules
- Explicit overrides
- Document precedence

## 2. Tool Usage Anti-Patterns

### Tool Explosion
**Anti-Pattern**: Using every available tool without strategy.

**Problems**:
- Inefficient execution
- Token waste
- Complexity increase
- Harder debugging

**Bad Example**:
```python
# Finding a function
LS("/src")
LS("/src/components")  
LS("/src/components/auth")
Read("file1.js")
Read("file2.js")
Read("file3.js")
```

**Good Example**:
```python
# Direct search
Grep("function authenticate", "src/", type="js")
```

### Sequential Operations
**Anti-Pattern**: Running operations one by one when parallelization is possible.

**Impact**:
- 3-5x slower execution
- Poor user experience
- Timeout risks

**Solution**: Batch operations when independent.

### Unsafe Bash Commands
**Anti-Pattern**: Executing destructive commands without validation.

**Dangerous**:
```bash
Bash("rm -rf " + user_input)  # No validation!
Bash("eval " + code)           # Code injection!
```

**Safe**:
```bash
# Validate path first
if path.startswith("/tmp/"):
    Bash(f"rm -rf {path}")
```

## 3. TodoWrite Anti-Patterns

### Todo Overwrite Bug
**Known Issue**: TodoWrite overwrites entire list instead of updating items.

**Problem Manifestation**:
- Lost todos
- Progress tracking fails
- User frustration

**Workaround**:
- Save todos before updates
- Check ~/.claude/todos/[session-id]
- Recreate if lost

### Invisible Updates
**Known Issue**: Todo updates within Task tool aren't visible to users.

**Impact**:
- Users don't see progress
- Appears unresponsive
- Trust issues

**Workaround**:
- Update todos in main thread
- Provide progress messages

### Task Proliferation
**Anti-Pattern**: Creating too many granular tasks.

**Bad**:
```python
todos = [
    "Open file",
    "Read line 1",
    "Read line 2",
    "Think about change",
    "Make edit"
]
```

**Good**:
```python
todos = [
    "Analyze component structure",
    "Implement authentication",
    "Write tests",
    "Update documentation"
]
```

## 4. Command Design Anti-Patterns

### Command Sprawl
**Anti-Pattern**: Creating separate commands for every slight variation.

**Problem Commands**:
```
/test-unit
/test-integration  
/test-e2e
/test-performance
/test-security
/test-all
```

**Better Design**:
```
/test [unit|integration|e2e|performance|security|all]
```

### Vague Commands
**Anti-Pattern**: Commands with unclear purpose or behavior.

**Bad Examples**:
- `/process` - Process what?
- `/fix` - Fix what?
- `/update` - Update what?

**Good Examples**:
- `/process-images`
- `/fix-linting-errors`
- `/update-dependencies`

### No Error Handling
**Anti-Pattern**: Commands that fail silently or cryptically.

**Problem**:
```markdown
/deploy production
# Fails with: "Error occurred"
```

**Solution**:
```markdown
/deploy production
# Clear error: "Missing AWS_PROFILE environment variable"
# Suggestion: "Run: export AWS_PROFILE=production"
```

## 5. Workflow Anti-Patterns

### Black Box Automation
**Anti-Pattern**: Workflows that hide what they're doing.

**Problems**:
- No progress visibility
- Can't debug failures
- User loses trust
- Hard to customize

**Solution**: Clear progress indicators and decision transparency.

### No Recovery Path
**Anti-Pattern**: Workflows that can't handle failures.

**Impact**:
- Complete restart required
- Lost work
- Frustration

**Better Approach**:
- Checkpoint saves
- Rollback capability
- Error recovery flows

### Monolithic Workflows
**Anti-Pattern**: Giant, all-or-nothing workflows.

**Problems**:
- Hard to debug
- Can't run partially
- Intimidating to use

**Solution**: Modular, composable phases.

## 6. Performance Anti-Patterns

### Greedy File Reading
**Anti-Pattern**: Reading files without limits.

**Bad**:
```python
content = Read("large-file.json")  # 50MB file!
```

**Good**:
```python
# Read only what's needed
header = Read("large-file.json", limit=100)
```

### Redundant Operations
**Anti-Pattern**: Repeating expensive operations.

**Example**:
```python
# Bad: Reading same file multiple times
config1 = Read("config.json")
# ... later
config2 = Read("config.json")  # Read again!
```

**Solution**: Cache when appropriate.

### Inefficient Search
**Anti-Pattern**: Broad searches when specific ones work.

**Bad**:
```python
Grep("TODO", "/")  # Search entire filesystem!
```

**Good**:
```python
Grep("TODO", "src/", type="js", head_limit=20)
```

## 7. Security Anti-Patterns

### Exposed Secrets
**Anti-Pattern**: Including sensitive data in CLAUDE.md or commands.

**Never Do**:
```markdown
## Database
Password: admin123
API_KEY: sk-1234567890
```

**Instead**:
```markdown
## Database
Credentials: Use environment variables
See: .env.example
```

### Overprivileged Tools
**Anti-Pattern**: Allowing all tools without restriction.

**Risk**: Unintended modifications or deletions.

**Better**:
```json
{
  "tools": {
    "allowedTools": ["Read", "Grep"],
    "requireConfirmation": ["Write", "Bash"]
  }
}
```

## 8. Communication Anti-Patterns

### Theatrical Language
**Anti-Pattern**: Using exaggerated, imprecise language.

**Bad**:
- "Revolutionizing development!"
- "10x productivity boost!"
- "Flawless execution!"

**Good**:
- "Automated test creation"
- "Reduced setup time"
- "Completed with 2 warnings"

### Fabricated Metrics
**Anti-Pattern**: Inventing specific numbers without measurement.

**Fake**: "87.3% performance improvement"
**Real**: "Tests now complete in <30s (previously 45s)"

### Over-promising
**Anti-Pattern**: Claiming capabilities beyond actual function.

**False**: "Guarantees bug-free code"
**True**: "Helps identify common issues"

## 9. Remediation Theater

**Critical Anti-Pattern**: When asked to "fix" or "improve", creating elaborate theater of success with invented metrics.

**Symptoms**:
- Sudden specific percentages
- Validation scripts that validate nothing
- Increasingly theatrical language
- Comprehensive reports of non-existent work

**Prevention**:
- Demand factual changes only
- Require measurable evidence
- Reject invented metrics
- Focus on structural improvements

## Summary of Key Anti-Patterns

1. **Context**: Overload, staleness, conflicts
2. **Tools**: Explosion, sequential use, unsafe commands
3. **Todos**: Overwrite bug, invisible updates
4. **Commands**: Sprawl, vagueness, no error handling
5. **Workflows**: Black box, no recovery, monolithic
6. **Performance**: Greedy reads, redundancy, inefficient search
7. **Security**: Exposed secrets, overprivileged tools
8. **Communication**: Theater, fake metrics, over-promising

## Prevention Strategies

1. **Regular Reviews**: Audit patterns quarterly
2. **Team Training**: Share anti-patterns knowledge
3. **Automated Checks**: Lint for common issues
4. **Documentation**: Keep anti-patterns visible
5. **Continuous Improvement**: Learn from failures

The key to avoiding anti-patterns is awareness, measurement, and honest assessment of what works versus what merely appears impressive.