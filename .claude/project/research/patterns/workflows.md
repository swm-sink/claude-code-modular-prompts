# Workflow Patterns for Claude Code

## Overview
Workflow patterns demonstrate how Claude Code can autonomously plan, execute, and adapt complex multi-step development tasks.

## Core Workflow Patterns

### 1. Plan-Execute-Review Cycle

**Pattern**: Separate planning from execution for complex tasks.

**Implementation** (from ClaudeFlow):
```markdown
## Phase 1: Planning
/plan Build complete authentication system with JWT

## Phase 2: Execution
/act
- Implement phase 1 of plan
- Run tests
- Review results

## Phase 3: Memory & Continuation
/memory  # Save state
# New session
/recall  # Load state
/act     # Continue next phase
```

**Benefits**:
- Clear separation of concerns
- Reviewable plans before execution
- State persistence across sessions

### 2. Milestone-Based Development

**Pattern**: Break work into measurable milestones.

**Example** (from Task Workflow):
```markdown
## Issue Implementation
Milestone 1: Setup & Types (25%)
- Create type definitions
- Set up file structure
- Configure dependencies

Milestone 2: Core Logic (50%)
- Implement main functionality
- Basic error handling
- Unit tests

Milestone 3: Integration (75%)
- Connect to existing systems
- Integration tests
- Documentation

Milestone 4: Polish (100%)
- Performance optimization
- Comprehensive tests
- Final documentation
```

### 3. Quality Gate Workflow

**Pattern**: Enforce quality checks between phases.

```bash
# Phase 1: Implementation
implement_feature()

# Quality Gate 1
npm run lint || exit 1
npm run typecheck || exit 1

# Phase 2: Testing
write_tests()

# Quality Gate 2
npm run test || exit 1
npm run test:coverage || exit 1

# Phase 3: Integration
integrate_feature()

# Final Gate
npm run build || exit 1
npm run test:e2e || exit 1
```

### 4. Autonomous Error Recovery

**Pattern**: Detect and recover from errors automatically.

```python
# Workflow with error handling
try:
    result = execute_task()
except CompilationError as e:
    diagnose_error(e)
    fix_compilation_error()
    result = retry_task()
except TestFailure as e:
    analyze_test_failure(e)
    fix_failing_tests()
    result = retry_task()
```

### 5. Context-Aware Workflow

**Pattern**: Adapt workflow based on project context.

```markdown
## Detect Project Type
- If package.json exists: Node.js workflow
- If requirements.txt exists: Python workflow  
- If Cargo.toml exists: Rust workflow

## Apply Type-Specific Workflow
- Node.js: npm install → test → build
- Python: pip install → pytest → package
- Rust: cargo build → cargo test → cargo package
```

### 6. Parallel Task Execution

**Pattern**: Execute independent tasks simultaneously.

**From System Prompt**:
```python
# Parallel execution for efficiency
tasks = [
    analyze_codebase(),
    check_dependencies(),
    run_linter(),
    generate_docs()
]
results = await Promise.all(tasks)
```

### 7. Incremental Development

**Pattern**: Build features incrementally with continuous validation.

```markdown
## Incremental Workflow
1. Implement minimal viable feature
2. Test minimal implementation
3. Add enhancement
4. Test enhancement
5. Repeat until complete

## Benefits
- Early failure detection
- Continuous progress
- Easier debugging
- Clear progress tracking
```

## Advanced Workflow Patterns

### 1. Multi-Agent Orchestration

**Pattern**: Coordinate multiple specialized agents.

**Example** (conceptual):
```yaml
agents:
  planner:
    role: Create detailed implementation plan
    output: structured_plan.json
  
  implementer:
    role: Execute plan steps
    input: structured_plan.json
    output: implementation_status.json
  
  tester:
    role: Validate implementation
    input: implementation_status.json
    output: test_results.json
  
  reviewer:
    role: Final quality check
    input: all_outputs
    output: approval_status
```

### 2. Adaptive Workflow

**Pattern**: Modify workflow based on results.

```python
def adaptive_workflow(task):
    complexity = assess_complexity(task)
    
    if complexity < 5:
        return simple_workflow(task)
    elif complexity < 10:
        return standard_workflow(task)
    else:
        # Break into subtasks
        subtasks = decompose_task(task)
        return complex_workflow(subtasks)
```

### 3. Rollback Workflow

**Pattern**: Maintain ability to rollback changes.

```bash
# Create restoration point
git stash save "pre-workflow-state"
create_backup()

# Execute workflow
try:
    execute_workflow()
    commit_changes()
except WorkflowError:
    git stash pop
    restore_backup()
    notify_failure()
```

### 4. Continuous Integration Workflow

**Pattern**: Integrate with CI/CD systems.

```yaml
# .claude/workflows/ci-integration.md
name: /ci-prepare
steps:
  1. Check CI environment
  2. Validate branch protection
  3. Run pre-commit hooks
  4. Generate CI configuration
  5. Create pull request
  6. Monitor CI status
```

### 5. Documentation-Driven Workflow

**Pattern**: Generate and maintain documentation throughout.

```markdown
## Documentation Workflow
1. Before implementation:
   - Document intended behavior
   - Create API documentation
   - Write user guide outline

2. During implementation:
   - Update documentation with changes
   - Add code comments
   - Create examples

3. After implementation:
   - Finalize user documentation
   - Generate API docs from code
   - Create migration guide
```

## Workflow Orchestration Tools

### ClaudeFlow Commands
- `/plan` - Create comprehensive plan
- `/act` - Execute current phase
- `/memory` - Save workflow state
- `/recall` - Restore workflow state

### Git Worktree Pattern
```bash
# Isolated development environment
git worktree add .trees/feature-x
cd .trees/feature-x
# Work in isolation
# Easy cleanup when done
```

### Hook-Based Orchestration
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "command": "validate_syntax.sh"
    }],
    "PostToolUse": [{
      "matcher": "Test",
      "command": "update_coverage.sh"
    }]
  }
}
```

## Workflow Best Practices

### 1. Clear Phase Definition
- Each phase has clear entry/exit criteria
- Phases are independently testable
- Progress is measurable

### 2. State Management
- Save state at phase boundaries
- Include rollback information
- Track decision rationale

### 3. Error Handling
- Anticipate common failures
- Provide recovery mechanisms
- Log detailed error context

### 4. Progress Visibility
- Use TodoWrite for tracking
- Regular status updates
- Clear success indicators

### 5. Reproducibility
- Document all decisions
- Save configuration state
- Enable workflow replay

## Anti-Patterns to Avoid

### 1. Monolithic Workflows
❌ Single massive workflow
✅ Modular, composable phases

### 2. Hidden State
❌ Implicit dependencies
✅ Explicit state management

### 3. No Recovery Path
❌ Failure stops everything
✅ Graceful error handling

### 4. Unclear Progress
❌ Black box execution
✅ Transparent progress tracking

## Real-World Examples

### From Claude Code Action
- Analyzes PR/issue context
- Plans appropriate response
- Executes with progress tracking
- Handles errors gracefully

### From Task Workflow
- Complexity assessment first
- Milestone-based execution
- Quality gates throughout
- Automated git operations

### From ClaudeFlow
- Multi-phase projects
- Session persistence
- Clear planning separation
- Incremental development

## Measuring Workflow Effectiveness

### Metrics
- Time to completion
- Error recovery rate
- Quality gate passage
- User interventions required

### Optimization Opportunities
- Parallel task identification
- Bottleneck analysis
- State size reduction
- Tool call efficiency

## Workflow Templates

### Feature Development
```markdown
1. Understand requirements
2. Plan implementation
3. Set up development branch
4. Implement in milestones
5. Test thoroughly
6. Document changes
7. Create pull request
8. Monitor CI/CD
```

### Bug Fix
```markdown
1. Reproduce issue
2. Identify root cause
3. Plan fix approach
4. Implement fix
5. Test fix and regressions
6. Update documentation
7. Submit for review
```

### Refactoring
```markdown
1. Analyze current state
2. Identify improvements
3. Plan incremental changes
4. Implement with tests
5. Verify behavior unchanged
6. Measure improvements
7. Document changes
```

## Conclusion

Effective workflows in Claude Code combine:
- Clear planning and execution phases
- Robust error handling and recovery
- Progress tracking and visibility
- Quality enforcement throughout
- State management for continuity
- Adaptability to project needs

The most successful workflows are those that balance automation with transparency, allowing developers to trust and verify the AI's work.