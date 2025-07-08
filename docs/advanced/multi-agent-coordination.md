| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Multi-Agent Coordination Guide

────────────────────────────────────────────────────────────────────────────────

**PURPOSE**: Master parallel development with multiple AI agents working simultaneously

────────────────────────────────────────────────────────────────────────────────

## Overview

The Claude Code framework's multi-agent coordination enables multiple AI agents to work on different parts of your codebase simultaneously, dramatically reducing development time while maintaining code quality and preventing conflicts.

────────────────────────────────────────────────────────────────────────────────

## Core Concepts

### Worktree Isolation

Each agent operates in its own git worktree, providing complete file system isolation:

```xml
<worktree_structure>
  main-repo/
  ├── .git/
  └── code...
  
  ../worktrees/
  ├── swarm-185-backend/     # Agent 1 workspace
  ├── swarm-185-frontend/    # Agent 2 workspace
  └── swarm-185-testing/     # Agent 3 workspace
</worktree_structure>
```

### File Ownership Domains

Agents are assigned ownership domains to prevent conflicts:

- **Backend Agent**: `/api/**`, `/services/**`, `/models/**`
- **Frontend Agent**: `/src/components/**`, `/src/pages/**`, `/public/**`
- **Testing Agent**: `/tests/**`, `/e2e/**` (read-only access to all)
- **DevOps Agent**: `/infrastructure/**`, `/.github/**`, `Dockerfile*`

────────────────────────────────────────────────────────────────────────────────

## Using the /swarm Command

### Basic Multi-Agent Task

```bash
/swarm "Add user authentication with login page and tests"
```

This automatically:
1. Creates GitHub session for coordination
2. Analyzes task complexity
3. Spawns appropriate agents (backend, frontend, testing)
4. Sets up isolated worktrees
5. Coordinates parallel execution
6. Merges results seamlessly

### Complex Feature Development

```bash
/swarm "Implement real-time chat feature with WebSocket support"
```

Results in:
- **Backend Agent**: WebSocket server, message handling
- **Frontend Agent**: Chat UI components, real-time updates
- **Database Agent**: Schema updates, message persistence
- **Testing Agent**: Integration tests, E2E scenarios

────────────────────────────────────────────────────────────────────────────────

## Practical Examples

### Example 1: API with Frontend Integration

```bash
/swarm "Create REST API for product catalog with React frontend"
```

**Agent Coordination:**
```xml
<execution_timeline>
  <phase time="0-5min">
    Backend: Design API schema
    Frontend: Setup component structure
  </phase>
  <phase time="5-15min">
    Backend: Implement endpoints
    Frontend: Create UI components
    Testing: Write API tests
  </phase>
  <phase time="15-20min">
    Integration: Connect frontend to API
    Testing: E2E validation
  </phase>
</execution_timeline>
```

### Example 2: Database Migration with Full Stack Updates

```bash
/swarm "Migrate user schema to support multi-tenancy"
```

**Agent Assignments:**
- **Database Agent**: Schema migration scripts
- **Backend Agent**: Model and service updates
- **Frontend Agent**: UI adjustments for tenant selection
- **Testing Agent**: Migration validation tests

────────────────────────────────────────────────────────────────────────────────

## Conflict Resolution Strategies

### Automatic Resolution

Most conflicts are prevented through domain ownership:

```xml
<conflict_prevention>
  <ownership_based>
    Backend owns /api/*, Frontend owns /src/components/*
  </ownership_based>
  <temporal_isolation>
    Critical files accessed sequentially
  </temporal_isolation>
  <merge_coordination>
    Dependency-ordered merging
  </merge_coordination>
</conflict_prevention>
```

### Manual Resolution

When conflicts occur:

1. **Early Detection**: Pre-merge analysis identifies conflicts
2. **Clear Presentation**: Shows exactly what conflicts exist
3. **Guided Resolution**: Provides resolution options
4. **Validation**: Ensures resolution maintains functionality

────────────────────────────────────────────────────────────────────────────────

## Performance Optimization

### Parallel Execution Benefits

- **70% faster** than sequential development
- **Resource efficient** through shared git objects
- **Scalable** to 5+ agents simultaneously

### Best Practices

```xml
<optimization_tips>
  <tip>Use shallow clones for faster worktree creation</tip>
  <tip>Implement sparse checkout for large repos</tip>
  <tip>Batch similar operations across agents</tip>
  <tip>Monitor resource usage and adjust agent count</tip>
</optimization_tips>
```

────────────────────────────────────────────────────────────────────────────────

## Troubleshooting

### Common Issues

#### Worktree Creation Fails
```bash
# Error: fatal: could not create work tree dir
# Solution: Check disk space and permissions
df -h
git worktree prune  # Clean stale worktrees
```

#### Agent Domain Violations
```
# Error: Agent-Frontend attempting to modify /api/users.js
# Solution: Reassign task or adjust domain boundaries
```

#### Merge Conflicts
```bash
# Use pre-merge detection
git merge-tree $(git merge-base HEAD agent-branch) HEAD agent-branch

# If conflicts exist, use guided resolution
/swarm resolve-conflicts
```

### Performance Issues

```xml
<performance_solutions>
  <issue name="Slow worktree creation">
    Use --depth=1 for shallow clones
  </issue>
  <issue name="High memory usage">
    Reduce concurrent agent count
  </issue>
  <issue name="Network bottlenecks">
    Use local references: --reference main-repo
  </issue>
</performance_solutions>
```

────────────────────────────────────────────────────────────────────────────────

## Advanced Patterns

### Microservices Development

```bash
/swarm "Split monolith into user-service, product-service, order-service"
```

Each service gets dedicated agents for:
- Service extraction
- API gateway updates
- Inter-service communication
- Deployment configuration

### Cross-Platform Features

```bash
/swarm "Implement offline sync for web, iOS, and Android"
```

Coordinates:
- Shared sync protocol design
- Platform-specific implementations
- Cross-platform testing
- Documentation updates

────────────────────────────────────────────────────────────────────────────────

## Integration with Quality Gates

All multi-agent work enforces:

- **TDD**: Each agent follows RED-GREEN-REFACTOR
- **Security**: Threat modeling across components
- **Performance**: Integrated performance testing
- **Documentation**: Automatic cross-references

────────────────────────────────────────────────────────────────────────────────

## Monitoring and Metrics

Track multi-agent efficiency:

```xml
<metrics>
  <execution_time>Total time vs sequential estimate</execution_time>
  <conflict_rate>Conflicts per swarm execution</conflict_rate>
  <merge_success>Automatic vs manual merges</merge_success>
  <quality_score>Combined agent quality metrics</quality_score>
</metrics>
```

────────────────────────────────────────────────────────────────────────────────

## Best Practices Summary

1. **Clear Task Definition**: Well-defined tasks enable better agent coordination
2. **Appropriate Scope**: Tasks should be complex enough to benefit from parallelization
3. **Domain Boundaries**: Respect file ownership to prevent conflicts
4. **Integration Points**: Plan where agents' work will integrate
5. **Quality First**: Every agent maintains quality standards

────────────────────────────────────────────────────────────────────────────────

**Reference**: See `.claude/modules/patterns/multi-agent.md` for implementation details

*Multi-agent coordination: Parallel development without the chaos.*