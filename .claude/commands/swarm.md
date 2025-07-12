# Swarm Command

Multi-component development with git worktree isolation and agent coordination.

## Instructions

Execute multi-component development for: $ARGUMENTS

1. **Analysis**: Analyze scope and identify components that need coordination.

2. **Worktree Setup**: Create isolated git worktrees for parallel development.

3. **Agent Coordination**: Coordinate multiple development streams with TDD enforcement.

4. **Integration**: Merge components with comprehensive testing and validation.

5. **Quality Gates**: Ensure all components meet production standards.

## When to Use

- Development touches 3+ files across different components
- Multiple features need parallel development
- Complex refactoring affecting multiple systems
- Team coordination required for large features

## Examples

- `/swarm "Implement user authentication system"` - Auth across frontend, backend, database
- `/swarm "Refactor payment processing"` - Multiple services coordination
- `/swarm "Add monitoring to all services"` - Cross-cutting concerns