# Swarm Command

Multi-component development with git worktree isolation, agent coordination, and atomic commits.

## Instructions

Execute multi-component development for: $ARGUMENTS

1. **Analysis**: Analyze scope and identify components that need coordination.
   - **Atomic Checkpoint**: `git add -A && git commit -m "SWARM INIT: [coordination_strategy] - components analyzed and strategy defined"`
   - **Scope Validation**: Ensure all components and dependencies are identified

2. **Worktree Setup**: Create isolated git worktrees for parallel development.
   - **Atomic Checkpoint**: `git add -A && git commit -m "SWARM SETUP: [worktree_structure] - isolated environments created"`
   - **Isolation Safety**: Each worktree operates independently with atomic commits
   - **Branch Strategy**: Each component gets dedicated branch with full rollback capability

3. **Agent Coordination**: Coordinate multiple development streams with TDD enforcement.
   - **Per-Agent Atomic Checkpoints**: `git add -A && git commit -m "SWARM EXEC: [agent_operation] - parallel completion with validation"`
   - **TDD Compliance**: Each agent follows atomic TDD cycle (RED→commit→GREEN→commit→REFACTOR→commit)
   - **Coordination Safety**: Failed agents can be rolled back without affecting successful ones

4. **Integration**: Merge components with comprehensive testing and validation.
   - **Atomic Checkpoint**: `git add -A && git commit -m "SWARM CONSOLIDATE: [integration_results] - unified output with validation"`
   - **Integration Testing**: Full system tests before integration commit
   - **Rollback Safety**: Integration failures trigger rollback to pre-merge state

5. **Quality Gates**: Ensure all components meet production standards.
   - **Final Atomic Checkpoint**: `git add -A && git commit -m "SWARM COMPLETE: [project_name] - production ready with quality validation"`

## When to Use

- Development touches 3+ files across different components
- Multiple features need parallel development
- Complex refactoring affecting multiple systems
- Team coordination required for large features

## Examples

- `/swarm "Implement user authentication system"` - Auth across frontend, backend, database
- `/swarm "Refactor payment processing"` - Multiple services coordination
- `/swarm "Add monitoring to all services"` - Cross-cutting concerns