# Swarm Command - Coordinate multiple development tasks in parallel

**Description**: Coordinate multiple development tasks in parallel

────────────────────────────────────────────────────────────────────────────────

| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-18   | stable | 85%      |

────────────────────────────────────────────────────────────────────────────────

## Command Orchestration

```xml
<command_orchestration>
  <delegation_target>modules/patterns/multi-agent.md</delegation_target>
  <orchestration_flow>
    1. Decompose complex task into parallel components
    2. Delegate to multi-agent coordination module
    3. Manage parallel agent execution with git isolation
    4. Coordinate integration and quality validation
  </orchestration_flow>
  <parallel_coordination>
    <git_isolation>Each agent works in isolated git worktrees</git_isolation>
    <dependency_management>Coordinate component dependencies</dependency_management>
    <quality_gates>Enforce quality standards across all agents</quality_gates>
    <integration_testing>Validate component integration</integration_testing>
  </parallel_coordination>
</command_orchestration>
```

## Usage

**Multi-component development:**
```
/swarm "Build frontend, backend, and database components for user system"
```

**Parallel feature development:**
```
/swarm "Implement authentication, authorization, and user profile features"
```

**Complex system coordination:**
```
/swarm "Set up CI/CD pipeline, testing infrastructure, and deployment scripts"
```

## What This Command Does

- **Parallel execution**: Coordinates multiple development tasks simultaneously
- **Git isolation**: Each component developed in separate worktrees for safety
- **Dependency management**: Handles component interactions and dependencies
- **Quality coordination**: Ensures all components meet quality standards
- **Integration focus**: Validates that components work together properly

## Examples

- `/swarm "API endpoints and frontend components"` - Develops backend and frontend in parallel
- `/swarm "Database schema and data access layer"` - Coordinates database and code changes
- `/swarm "Testing suite and documentation"` - Develops tests and docs simultaneously