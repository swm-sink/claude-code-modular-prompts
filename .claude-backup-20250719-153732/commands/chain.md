# Chain Command - Run multiple commands in sequence

**Description**: Run multiple commands in sequence

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 1.0.0   | 2025-07-18   | stable | 100%     |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/command-chaining-architecture.md</delegation_target>
  <orchestration_flow>
    1. Parse multi-command workflow requirements
    2. Delegate to command chaining architecture module
    3. Execute commands in sequence with state management
    4. Handle errors and provide atomic rollback capability
  </orchestration_flow>
  <workflow_patterns>
    <sequential>Commands execute in order with state passing</sequential>
    <parallel>Independent commands execute simultaneously</parallel>
    <conditional>Dynamic routing based on execution results</conditional>
    <iterative>Commands repeat until criteria met</iterative>
  </workflow_patterns>
</command_orchestration>
```

## Usage

**Research then implement:**
```
/chain "research user authentication patterns, then implement auth system"
```

**Multi-step workflow:**
```
/chain "analyze performance issues, create optimization plan, implement fixes"
```

**Complex coordination:**
```
/chain "set up project structure, configure CI/CD, deploy to staging"
```

## What This Command Does

- **Sequential execution**: Runs commands in order with state preservation
- **Parallel coordination**: Executes independent commands simultaneously
- **Error handling**: Provides comprehensive error recovery and rollback
- **State management**: Passes context and results between commands
- **Workflow optimization**: Optimizes execution patterns for efficiency

## Examples

- `/chain "query database schema, then design API endpoints"` - Research followed by implementation
- `/chain "create tests, implement feature, deploy to staging"` - Complete development workflow
- `/chain "analyze codebase, document findings, create improvement plan"` - Analysis and planning workflow