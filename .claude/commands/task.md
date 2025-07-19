# Task Command - Build a single feature with tests

**Description**: Build a single feature with tests

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-18   | stable | 95%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/tdd-cycle-pattern.md</delegation_target>
  <orchestration_flow>
    1. Validate task scope (single component, <3 files)
    2. Delegate to TDD cycle pattern module
    3. Enforce quality gates and atomic commits
    4. Validate completion criteria
  </orchestration_flow>
  <escalation_conditions>
    <multi_component>Route to /swarm for coordination</multi_component>
    <complex_feature>Route to /feature for PRD development</complex_feature>
    <production_deploy>Route to /protocol for safety validation</production_deploy>
  </escalation_conditions>
</command_orchestration>
```

## Usage

**Single feature development with TDD:**
```
/task "Add email validation to user registration"
```

**Bug fix with regression test:**
```
/task "Fix memory leak in image processing component"
```

**Performance optimization:**
```
/task "Optimize database query performance in user search"
```

## What This Command Does

- **Enforces TDD**: Red-Green-Refactor cycle through module delegation
- **Single focus**: Works on one component or feature at a time
- **Quality gates**: Ensures 90%+ test coverage and production standards
- **Atomic commits**: Creates safe rollback points at each TDD phase
- **Scope validation**: Escalates to appropriate command for larger tasks

## Future Enhancements

*Note: The following features are planned but not yet implemented:*
- Auto-fix capabilities for linting and formatting
- Automated test failure analysis
- Coverage gap identification
- Pattern-based fixes for common issues

## Examples

- `/task "Add input validation"` - Creates validation with comprehensive tests
- `/task "Fix race condition"` - Creates regression test first, then fix
- `/task "Add logging to API endpoints"` - Adds logging with proper test coverage