# /swarm - Multi-Agent Orchestration with Intelligent Coordination

**Purpose**: Execute complex multi-component systems using native Task() and Batch() patterns with automatic session management and module composition.

**Foundation**: Inherits universal principles from CLAUDE.md (AWARE framework, critical thinking, tool patterns)

## When to Use

Use `/swarm` for:
- **Multi-component systems** (≥3 specialized areas: frontend, backend, database, security, DevOps)
- **Complex feature development** requiring diverse expertise
- **System architecture** and large-scale refactoring
- **Enterprise integrations** with multiple touchpoints
- **Performance optimization** across multiple layers

## Revolutionary Multi-Agent Architecture

### Automatic Module Composition
```python
# /swarm intelligently loads relevant modules based on task analysis:

# System development → Loads multi-agent + security + deploy modules
/swarm "Build microservices e-commerce platform"
# → Loads: patterns/multi-agent.md, security/audit.md, deploy/protocol.md
# → Creates session #127: "E-commerce Microservices Platform"
# → Uses Task() pattern for heterogeneous work

# Performance optimization → Loads performance + quality modules  
/swarm "Optimize entire application for 10x scale"
# → Loads: quality/performance.md, patterns/multi-agent.md, deploy/protocol.md
# → Creates session #128: "Application Scale Optimization" 
# → Uses hybrid Task()+Batch() patterns
```

### Native Multi-Agent Patterns (from modules/patterns/multi-agent.md)

#### Task() Pattern - Specialized Expertise
```python
# CRITICAL: All Task() calls in ONE message for true parallelism
# Automatically creates GitHub session for coordination

Task("System Architect", "Design overall microservices architecture with API gateway, service mesh, and data consistency patterns")

Task("Security Architect", "Implement OAuth2 JWT authentication, API security, threat modeling, and compliance framework")

Task("Frontend Architect", "Build React SPA with Redux, TypeScript, responsive design, and real-time updates")

Task("Backend Engineer", "Develop FastAPI microservices with async operations, database optimization, and comprehensive API documentation")

Task("DevOps Engineer", "Design Kubernetes deployment with auto-scaling, monitoring, logging, CI/CD pipeline, and disaster recovery")

Task("Database Architect", "Design PostgreSQL cluster with replication, sharding, backup strategies, and query optimization")

# → Session #127 auto-created: "E-commerce Microservices Platform"
# → Each agent works independently but coordinates through session
# → Progress tracking and decision logging in GitHub issue
```

#### Batch() Pattern - Distributed Similar Work
```python
# Single Batch() call for homogeneous operations
Batch([
    "Migrate UserService to new authentication middleware with comprehensive testing",
    "Migrate ProductService to new authentication middleware with comprehensive testing", 
    "Migrate OrderService to new authentication middleware with comprehensive testing",
    "Migrate PaymentService to new authentication middleware with comprehensive testing",
    "Migrate NotificationService to new authentication middleware with comprehensive testing"
])

# → All services migrated in parallel with consistent patterns
# → Session tracks migration progress across all services
# → Unified testing and rollback strategies
```

#### Hybrid Patterns - Complex Workflows
```python
# Step 1: Architecture design (Task pattern)
Task("Architect", "Design event-driven architecture with message queues and saga patterns")

# Wait for architecture completion, then parallel implementation
# Step 2: Service implementation (Batch pattern) 
Batch([
    "Implement Order Service following event-driven architecture",
    "Implement Payment Service following event-driven architecture",
    "Implement Inventory Service following event-driven architecture", 
    "Implement Notification Service following event-driven architecture"
])

# Step 3: Integration and testing (Task pattern)
Task("QA Engineer", "Design end-to-end testing strategy for event-driven system")
Task("DevOps", "Set up monitoring and observability for distributed system")
```

## Mandatory Session Integration

### Automatic Session Creation
```python
# /swarm ALWAYS creates GitHub session - no exceptions
session = create_github_session({
    "title": f"{task_summary} - Multi-Agent Implementation",
    "labels": ["ai-session", "active", "multi-agent", "swarm"],
    "template": "ai-session-swarm", 
    "auto_assign": True
})

# Session serves as:
# - Coordination hub for all agents
# - Progress tracking and milestone management  
# - Decision log and architecture documentation
# - Communication channel for dependencies and blockers
```

### Session-Driven Coordination
```python
class SwarmSession:
    def __init__(self, github_issue):
        self.session = github_issue
        self.agents = []
        self.milestones = []
        self.decisions = []
        
    def add_agent(self, agent_role, task_description):
        # Each Task() call registers with session
        agent = {
            "role": agent_role,
            "task": task_description, 
            "status": "assigned",
            "session_id": self.session.number
        }
        self.agents.append(agent)
        self.update_session_progress()
        
    def log_decision(self, decision, rationale, agent):
        # Critical decisions logged for team visibility
        self.decisions.append({
            "decision": decision,
            "rationale": rationale,
            "agent": agent,
            "timestamp": now(),
            "session_id": self.session.number
        })
        self.session.add_comment(f"**Decision by {agent}**: {decision}\n\n{rationale}")
```

## Advanced Orchestration Examples

### Complex System Development
```bash
/swarm "Build real-time trading platform with high-frequency data processing"

# Automatic Analysis:
# → Complexity: 6 components (UI, API, Database, Streaming, Security, Infrastructure)
# → Modules loaded: patterns/multi-agent.md, security/audit.md, quality/performance.md, deploy/protocol.md
# → Session created: #129 "Real-time Trading Platform"

# Execution Pattern: 
Task("Trading System Architect", "Design low-latency architecture with microsecond precision, event sourcing, and CQRS patterns")

Task("Security Specialist", "Implement financial-grade security with multi-factor auth, audit trails, and regulatory compliance") 

Task("Performance Engineer", "Optimize for <1ms latency with custom protocols, memory pools, and CPU affinity")

Task("Frontend Engineer", "Build real-time trading dashboard with WebSocket streaming, charting, and responsive design")

Task("Database Engineer", "Design time-series database with partitioning, compression, and sub-millisecond queries")

Task("DevOps Engineer", "Create zero-downtime deployment with blue-green, monitoring, and disaster recovery")

# → All agents coordinate through session #129
# → Progress tracked with milestones and decision logging
# → Architecture decisions documented for regulatory compliance
```

### Enterprise Migration Project
```bash
/swarm "Migrate legacy monolith to cloud-native microservices"

# Automatic Analysis:
# → Complexity: Migration + Architecture + Multiple services
# → Modules loaded: patterns/multi-agent.md, deploy/protocol.md, quality/review.md
# → Session created: #130 "Legacy Migration to Microservices"

# Phase 1: Analysis and Planning (Task pattern)
Task("Migration Architect", "Analyze legacy monolith, identify service boundaries, and design migration strategy")

Task("Data Architect", "Design data migration strategy with zero-downtime, consistency guarantees, and rollback plans")

# Phase 2: Parallel Service Development (Batch pattern)
Batch([
    "Extract User Management service with comprehensive testing and monitoring",
    "Extract Product Catalog service with comprehensive testing and monitoring",
    "Extract Order Processing service with comprehensive testing and monitoring", 
    "Extract Payment Processing service with comprehensive testing and monitoring"
])

# Phase 3: Integration and Cutover (Task pattern)
Task("Integration Engineer", "Implement API gateway, service mesh, and gradual traffic migration")

Task("QA Engineer", "Design comprehensive testing strategy for hybrid monolith-microservices environment")

# → Session #130 tracks entire migration with milestone-based progress
# → Decision log captures architectural choices and trade-offs
# → Risk mitigation and rollback procedures documented
```

## Quality Enforcement with Module Integration

### Automatic Quality Module Loading
Based on task characteristics, `/swarm` automatically includes:

- **Security modules** → For any data handling, authentication, or compliance work
- **Performance modules** → For high-scale, real-time, or optimization tasks
- **TDD modules** → For new feature development requiring comprehensive testing
- **Protocol modules** → For production deployments and enterprise integrations

### Multi-Agent Quality Gates
```python
# Each agent must satisfy quality requirements from loaded modules:

quality_gates = {
    "security": {
        "threat_model": "required",
        "vulnerability_scan": "required",
        "compliance_check": "required"
    },
    "performance": {
        "load_testing": "required", 
        "latency_benchmarks": "required",
        "resource_optimization": "required"
    },
    "testing": {
        "unit_coverage": ">90%",
        "integration_tests": "required",
        "e2e_scenarios": "required"
    }
}

# Session tracks quality gate completion across all agents
# No agent can mark complete until all quality requirements satisfied
```

## Coordination and Communication

### Agent Independence with Coordination
```python
# Agents work independently but coordinate through session:

class Agent:
    def execute_task(self, task, session):
        # 1. Independent execution using Claude Code tools
        self.research_requirements(task)
        self.analyze_codebase(task) 
        self.implement_solution(task)
        
        # 2. Session coordination for dependencies
        self.check_dependencies(session)
        self.update_progress(session)
        self.log_decisions(session)
        
        # 3. Quality gate verification
        self.verify_quality_gates(session)
        self.request_peer_review(session)
```

### Dependency Management
```python
# Agents can declare dependencies and wait for completion:
Task("Backend API", "depends_on=['Database Schema'] - Implement REST endpoints")
Task("Frontend UI", "depends_on=['Backend API'] - Build user interface")

# Session manages dependency resolution and coordination
# Agents automatically notified when dependencies complete
```

## Performance and Optimization

### Token Budget Management
- **Session overhead**: <1k tokens (efficient GitHub integration)
- **Agent coordination**: <2k tokens (streamlined communication)
- **Module composition**: <3k tokens (dynamic loading)
- **Total /swarm overhead**: <6k tokens (scales with complexity)

### Parallel Execution Optimization
```python
# Maximize Claude Code parallel execution:
# - All Task() calls in single message
# - Batch() for similar operations
# - Session updates batched for efficiency
# - Module loading optimized for common patterns
```

### Learning and Adaptation
- **Pattern recognition**: Learn successful agent combinations
- **Module effectiveness**: Track which modules improve outcomes
- **Session templates**: Generate optimized session structures
- **Coordination patterns**: Refine dependency management based on results

## Success Metrics and Evaluation

### Session Completion Criteria
- [ ] All agents completed their assigned tasks
- [ ] Quality gates satisfied across all modules
- [ ] Integration testing completed successfully
- [ ] Documentation updated with architectural decisions
- [ ] Session labeled with outcome (successful/partial/blocked)

### Multi-Agent Effectiveness Metrics
- **Parallel efficiency**: Work completed in parallel vs sequential
- **Coordination overhead**: Time spent on dependencies vs execution
- **Quality achievement**: Standards met across all agents
- **Session value**: Knowledge captured for future reference

**Foundation**: Built on CLAUDE.md universal principles with automatic module composition for world-class multi-agent orchestration.