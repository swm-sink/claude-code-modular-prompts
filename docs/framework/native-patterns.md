| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-07   | stable |

# Native Patterns - Task() and Batch()

────────────────────────────────────────────────────────────────────────────────

**Purpose**: Define correct usage of Claude Code's native multi-agent patterns for optimal parallel execution.

## Task() Pattern

### When to Use
```
✓ Different expertise needed
✓ Heterogeneous components
✓ Specialized analysis
✓ Architectural decisions
```

### Session Management
- **Always creates session** for multi-agent Task() work
- Each agent updates session progress automatically
- Session links all agent outputs together

### Correct Usage
```python
# Multiple Task() calls in ONE message
# Auto-creates GitHub issue session
Task("Frontend Expert", "Design React component architecture with TypeScript")
Task("Backend Expert", "Design FastAPI service with authentication")  
Task("Database Expert", "Design PostgreSQL schema with optimization")
Task("Security Expert", "Implement OAuth2 and threat modeling")
Task("DevOps Expert", "Design Kubernetes deployment")
# Session #123 created, all work tracked
```

### Key Rules
1. **One Message**: All Task() calls in single message
2. **Clear Roles**: Specific expertise for each agent
3. **Defined Scope**: Clear deliverables per agent
4. **No Dependencies**: Agents work independently

## Batch() Pattern

### When to Use
```
✓ Similar operations
✓ Homogeneous work
✓ Parallel processing
✓ Bulk updates
```

### Session Management
- **Creates session** for complex batch work
- Progress tracked as batch completes
- Summary added to session on completion

### Correct Usage
```python
# Single Batch() call for similar tasks
# Creates session for batch refactoring
Batch([
    "Refactor UserService to SOLID principles",
    "Refactor ProductService to SOLID principles",
    "Refactor OrderService to SOLID principles",
    "Refactor PaymentService to SOLID principles"
])
# Session #124 tracks all refactoring progress
```

### Key Rules
1. **One Call**: Single Batch() with array
2. **Similar Work**: Tasks are homogeneous
3. **Independent**: No inter-dependencies
4. **Clear Pattern**: Same operation type

## Pattern Selection

### Decision Matrix
```
HETEROGENEOUS WORK → Task()
- Frontend + Backend + Database
- Different expertise required
- Varied deliverables

HOMOGENEOUS WORK → Batch()  
- Multiple similar refactors
- Same operation repeated
- Uniform deliverables
```

### Anti-Patterns

#### ❌ Sequential Task() Calls
```python
# WRONG: Multiple messages
Task("Frontend Dev", "Build UI")
# Wait for response...
Task("Backend Dev", "Build API")
```

#### ❌ Batch() for Different Work
```python
# WRONG: Heterogeneous tasks
Batch([
    "Design database schema",
    "Implement authentication",
    "Write documentation"
])
```

#### ❌ Dependencies Between Agents
```python
# WRONG: Agent 2 needs Agent 1's output
Task("Agent 1", "Create API spec")
Task("Agent 2", "Implement API from Agent 1's spec")
```

## Coordination Patterns

### Full-Stack Feature
```python
# Correct: Independent specialized work
# Creates session "Dashboard Implementation #125"
Task("UI Designer", "Design dashboard mockups and user flow")
Task("Frontend Dev", "Build dashboard components with React")
Task("Backend Dev", "Create dashboard API endpoints")
Task("Data Engineer", "Design dashboard analytics schema")
Task("QA Engineer", "Create dashboard test scenarios")
# All agents update session #125 with progress
```

### System Refactoring  
```python
# Correct: Similar parallel work
Batch([
    "Refactor auth module: extract interfaces, add tests",
    "Refactor user module: extract interfaces, add tests",
    "Refactor payment module: extract interfaces, add tests",
    "Refactor notification module: extract interfaces, add tests"
])
```

### Mixed Pattern
```python
# Phase 1: Architecture (heterogeneous)
Task("System Architect", "Design microservice boundaries")
Task("Data Architect", "Design data flow between services")
Task("Security Architect", "Design service authentication")

# Phase 2: Implementation (homogeneous)
Batch([
    "Implement user microservice with tests",
    "Implement order microservice with tests",
    "Implement payment microservice with tests"
])
```

## Performance Optimization

### Maximize Parallelism
```python
# Good: 5 parallel agents
Task("Agent1", "Task 1")
Task("Agent2", "Task 2")
Task("Agent3", "Task 3")
Task("Agent4", "Task 4")
Task("Agent5", "Task 5")
```

### Minimize Context
```python
# Good: Focused instructions
Task("API Expert", "Design REST endpoints for user management")

# Bad: Vague instructions  
Task("Developer", "Build the system")
```

## Integration with Commands

### /swarm Command
```bash
/swarm "Build notification system"
# Automatically creates optimal Task() calls
# Always creates GitHub issue session
# Returns: "Created session #126"
```

### /auto Command
```bash
/auto "Refactor all services"
# Detects pattern and uses Batch()
# Creates session if complexity warrants
# Links work to session automatically
```

## Results Synthesis

### Task() Results
- Each agent provides specialized output
- Synthesis identifies integration points
- Conflicts resolved intelligently
- Unified solution presented

### Batch() Results
- Consistent format across results
- Summary of all completions
- Aggregate metrics provided
- Common patterns identified

## Best Practices

1. **Clear Scope**: Define exact deliverables
2. **Independent Work**: No blocking dependencies
3. **Appropriate Pattern**: Task() vs Batch()
4. **Single Message**: All agents launched together
5. **Trust the System**: Let agents work independently
6. **Session Tracking**: All multi-agent work tracked in GitHub issues
7. **Progress Updates**: Agents automatically update sessions
8. **Completion**: Sessions closed with outcomes documented

Remember: These are native Claude Code patterns, not theoretical constructs.