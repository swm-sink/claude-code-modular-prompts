# /task - General Development Command

**Purpose**: Handle all single-component development tasks with automatic quality enforcement.

## When to Use

Use `/task` for:
- Feature implementation
- Bug fixes
- Refactoring
- Documentation
- Single-component changes
- General development work

## Session Management

- **Prompts for session** on multi-step tasks
- **Links to active session** if one exists
- **Optional for simple fixes**
- Use `/session start` to explicitly create one

## Core Parameters

```bash
/task "description" [options]

Options:
--fix          # Bug fix mode (includes regression tests)
--refactor     # Clean code without changing behavior  
--docs         # Generate/update documentation
--issue #123   # Link to GitHub issue
--ci           # Setup CI/CD pipeline
--quick        # Rapid prototyping (relaxed standards)
```

## Execution Flow

### 1. Analysis Phase
- Understand requirements
- Search relevant code
- Identify dependencies
- Plan implementation
- Check if session needed (multi-step work)

### 2. Implementation Phase  
- Follow TDD cycle (RED-GREEN-REFACTOR)
- Write minimal code to pass tests
- Refactor for clarity
- Update documentation

### 3. Verification Phase
- Run all tests
- Check linting (ruff, mypy)
- Verify coverage (>90%)
- Validate requirements

## Mode-Specific Behavior

### Bug Fix Mode (--fix)
```bash
/task "Fix login timeout issue" --fix
```
- Reproduces bug with failing test
- Implements minimal fix
- Adds regression tests
- Updates changelog

### Refactor Mode (--refactor)
```bash
/task "Refactor user service to SOLID principles" --refactor
```
- Maintains all existing tests
- Improves code structure
- Enhances readability
- No behavior changes

### Documentation Mode (--docs)
```bash
/task "Document the authentication API" --docs
```
- Generates from code
- Includes examples
- Updates README
- Creates diagrams if needed

### Issue Mode (--issue)
```bash
/task "Implement user preferences" --issue #45
```
- Links commits to issue
- Updates issue progress
- Follows issue requirements
- Closes on completion
- Can work alongside session tracking

## Quality Standards

### Mandatory Checks
1. **Tests pass** (pytest)
2. **Linting clean** (ruff check)
3. **Types valid** (mypy)
4. **Coverage >90%** (pytest-cov)

### Code Standards
- SOLID principles
- DRY (Don't Repeat Yourself)
- Clear naming
- Comprehensive docstrings
- Type hints

## Multi-Agent Escalation

Automatically escalates to `/swarm` when detecting:
- Multiple components affected
- System-wide changes needed
- Complex integration required
- Performance optimization across services

**Note**: Escalation to `/swarm` auto-creates a session

## Examples

### Simple Feature
```bash
/task "Add email validation to registration"
# Single component, straightforward implementation
# No session needed for simple task
```

### Bug Fix
```bash
/task "Fix memory leak in image processor" --fix
# Focuses on reproduction, fix, and prevention
```

### Refactoring
```bash
/task "Refactor database queries for better performance" --refactor
# Improves code without changing functionality
```

### GitHub Integration
```bash
/task "Add OAuth2 support" --issue #89
# Links all work to GitHub issue #89
# Prompts: "This looks complex. Create session? (y/n)"
# If yes: Creates session #90 linked to issue #89
```

## Best Practices

1. **One component** per task invocation
2. **Clear description** of desired outcome
3. **Use parameters** for specific modes
4. **Trust TDD** process - tests first!
5. **Session tracking** for multi-step work
6. **Link to issues** when applicable

## Common Patterns

### Feature Development
```python
# 1. Write failing test for new feature
# 2. Implement minimal code to pass
# 3. Refactor for clarity
# 4. Document the feature
```

### Bug Fixing
```python
# 1. Reproduce with failing test
# 2. Fix the bug minimally
# 3. Add regression tests
# 4. Document the fix
```

### Performance Optimization
```python
# 1. Benchmark current performance
# 2. Identify bottlenecks
# 3. Optimize with tests
# 4. Verify improvements
```

## Token Optimization
- Focused on single components
- Max 10k tokens per response
- Delegates complex work to /swarm