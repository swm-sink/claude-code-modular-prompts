# Development Workflow

## Test-Driven Development (TDD)

### Mandatory Process

1. **RED** - Write failing test first
   ```python
   def test_command_functionality():
       result = execute_command("/example", "input")
       assert result.success == True
       assert result.performance < 100  # ms
   ```

2. **GREEN** - Minimal implementation to pass
   ```markdown
   ---
   name: /example
   description: Does one thing well
   tests: tests/unit/test_example.py
   ---
   ```

3. **REFACTOR** - Improve with tests as safety net

## Quality Gates

### Pre-commit Checks
```bash
# All must pass before commit
pytest --cov=. --cov-fail-under=90
bandit -r . --severity-level medium
performance-test --max-time=100ms
```

### Per-Commit Checklist
- [ ] No new directories beyond 3 levels
- [ ] No duplicate files created
- [ ] Tests written and passing
- [ ] <100ms command execution
- [ ] No meta-documentation added
- [ ] Atomic, focused change

## Agent Orchestration

### Simple DAG Pattern
```json
{
  "orchestrator": {
    "max_workers": 3,
    "timeout": 300,
    "pattern": "simple-dag"
  },
  "workers": [
    {"id": "analyzer", "role": "analyze_code"},
    {"id": "executor", "role": "execute_task"},
    {"id": "validator", "role": "validate_result"}
  ]
}
```

### Agent Communication Protocol
```json
{
  "message": {
    "id": "uuid",
    "from_agent": "agent_id",
    "status": "pending|working|done|failed",
    "task_id": "uuid",
    "files_modified": ["path1", "path2"],
    "errors": []
  }
}
```

## Security Requirements

- Input validation mandatory
- Output sanitization required
- No hardcoded secrets
- Permission checks enforced