# /patterns/multi-agent - Multi-Agent Coordination Module

**Purpose**: Define and implement native Claude Code multi-agent patterns using Task() and Batch() for parallel execution.

## Module Interface
- **Trigger**: Complex tasks requiring ≥3 components or specialized expertise
- **Dependencies**: Automatically creates GitHub sessions via patterns/session-mgmt.md
- **Session**: MANDATORY session creation for all multi-agent work
- **Output**: Coordinated parallel execution with progress tracking

## Native Multi-Agent Patterns

### Task() Pattern - Specialized Expertise
**Use Case**: Heterogeneous work requiring different specialized skills

```python
# CRITICAL: All Task() calls in ONE message for true parallelism
# Auto-creates GitHub session for coordination and tracking

Task("Frontend Architect", "Design React component architecture with TypeScript, Redux state management, and responsive design patterns")

Task("Backend Architect", "Design FastAPI microservices with PostgreSQL, async operations, and comprehensive API documentation") 

Task("Security Specialist", "Implement OAuth2 JWT authentication, role-based access control, and comprehensive threat model")

Task("DevOps Engineer", "Design Kubernetes deployment with auto-scaling, monitoring, logging, and CI/CD pipeline")

Task("Database Architect", "Design optimized PostgreSQL schema with indexing, migrations, and query performance analysis")

# → Session #123 created automatically
# → Each agent updates progress independently  
# → All work coordinated through GitHub issue
```

### Batch() Pattern - Distributed Work
**Use Case**: Homogeneous work that can be distributed in parallel

```python
# Single Batch() call for similar operations
Batch([
    "Refactor UserService to SOLID principles with comprehensive unit tests and documentation",
    "Refactor ProductService to SOLID principles with comprehensive unit tests and documentation", 
    "Refactor OrderService to SOLID principles with comprehensive unit tests and documentation",
    "Refactor PaymentService to SOLID principles with comprehensive unit tests and documentation"
])

# → All services refactored in parallel
# → Consistent patterns applied across all services
# → Unified testing and documentation standards
```

## Intelligent Pattern Selection

### Decision Matrix
```python
def select_pattern(task_complexity, component_count, expertise_diversity):
    if expertise_diversity == "high" and component_count >= 3:
        return "Task()"  # Different specialists needed
    elif expertise_diversity == "low" and component_count >= 3:  
        return "Batch()" # Similar work, different targets
    elif component_count < 3:
        return "single_agent"  # Use /task command
    else:
        return "hybrid"  # Combination of patterns
```

### Task() Scenarios
- **System Architecture**: Frontend + Backend + Database + Security + DevOps
- **Feature Development**: UI + API + Tests + Documentation + Deployment
- **Migration Projects**: Data + Code + Infrastructure + Testing + Rollback

### Batch() Scenarios  
- **Code Refactoring**: Multiple similar services/modules
- **Test Coverage**: Adding tests to multiple components
- **Documentation**: Updating docs across multiple packages
- **Migration Tasks**: Converting multiple files/databases

## Multi-Agent Coordination Rules

### No Dependencies Between Agents
```python
# CORRECT: Independent parallel work
Task("Frontend", "Build user dashboard")
Task("Backend", "Create user API endpoints") 
Task("Database", "Design user tables")

# INCORRECT: Sequential dependencies
Task("Database", "Create tables FIRST")  
Task("Backend", "THEN create APIs using those tables")
Task("Frontend", "FINALLY build UI using the APIs")
```

### Session Management Integration
- **Auto-Creation**: Multi-agent work always creates GitHub session
- **Progress Tracking**: Each agent updates session with milestones
- **Coordination**: Session serves as communication hub
- **Completion**: Session closed when all agents finish

### Communication Patterns
- **Shared Context**: All agents access same session
- **Progress Updates**: Regular status updates in session comments
- **Blocking Issues**: Document blockers for team coordination
- **Decision Log**: Record architectural decisions in session

## Advanced Multi-Agent Patterns

### Hybrid Execution
```python
# Combine Task() and Batch() for complex workflows
Task("Architect", "Design overall system architecture")
# → Wait for architecture completion
Batch([
    "Implement auth service based on architecture",
    "Implement user service based on architecture", 
    "Implement payment service based on architecture"
])
```

### Specialized Roles
- **Architect**: System design, technology decisions
- **Security**: Threat modeling, vulnerability assessment
- **Performance**: Optimization, scalability analysis
- **Quality**: Testing strategies, code review
- **DevOps**: Infrastructure, deployment, monitoring

## Session Integration Examples

```bash
# Complex system development
/swarm "Build e-commerce platform with microservices"
# → Creates session #123: "E-commerce Platform Development"
# → Automatically uses Task() pattern for heterogeneous work
# → Progress tracked across all agents

# Distributed refactoring  
/swarm "Refactor all services to use new authentication middleware"
# → Creates session #124: "Authentication Middleware Migration"
# → Automatically uses Batch() pattern for similar work
# → Consistent implementation across all services
```

## Quality Assurance

### Multi-Agent Testing
- Each agent responsible for testing their components
- Integration testing coordinates between agents
- End-to-end testing validates complete system

### Documentation Standards
- Shared documentation repository
- API contracts defined upfront
- Architecture decisions recorded
- Implementation notes shared across agents

**Token Budget**: <5k tokens (efficient multi-agent coordination)