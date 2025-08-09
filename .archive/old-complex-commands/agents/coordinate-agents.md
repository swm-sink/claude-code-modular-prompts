---
name: coordinate-agents
description: Orchestrate specialized agents for complex multi-step workflows and tasks
usage: "coordinate-agents [workflow-type] [--agents=list] [--interactive] [--save-workflow]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite]
category: agents
argument-hint: "[tdd|bug-fix|feature|refactor|deployment] [--options]"
version: "1.0"
---

# Coordinate Agents: Multi-Agent Workflow Orchestration

## Purpose: Intelligent Multi-Agent Collaboration System

The `/coordinate-agents` command orchestrates multiple specialized agents to work together on complex tasks, managing handoffs, preventing conflicts, and ensuring each agent contributes their unique expertise at the optimal time. This creates a seamless team of AI specialists working collaboratively on your project.

**Agent Coordination Philosophy**: Intelligent task decomposition, specialized agent routing, conflict-free collaboration, measurable workflow outcomes, user control over agent teams.

## 🎯 Multi-Agent Orchestration System

### Intelligent Task Decomposition
- **Workflow Analysis**: Break complex tasks into agent-specific subtasks
- **Dependency Mapping**: Identify task dependencies and optimal execution order
- **Agent Assignment**: Route subtasks to agents with appropriate specialization
- **Conflict Prevention**: Ensure agents don't work at cross-purposes

### Advanced Coordination Features
- **Real-Time Handoffs**: Seamless information transfer between specialized agents
- **Quality Gates**: Each agent validates inputs from other agents within their expertise
- **Progress Synchronization**: All agents stay informed about overall progress
- **User Oversight**: Approve key decisions and direction changes

## 🔄 Pre-Built Workflow Templates

### TDD Development Workflow
**Use Case**: Feature development with strict test-driven development
```bash
/coordinate-agents tdd --feature="user authentication"
```

**Agent Coordination Flow**:
1. **🏗️ Architecture Agent** (2-3 min)
   - Analyzes feature requirements against current system architecture
   - Defines integration points and design patterns
   - Identifies potential architectural impacts and constraints

2. **🧪 Testing Agent** (3-4 min) *[Primary Lead]*
   - Creates comprehensive test suite based on requirements
   - Enforces RED-GREEN-REFACTOR cycle with code deletion penalty
   - Validates test coverage meets project standards (>85%)
   - Coordinates with other agents to ensure testability

3. **⚙️ Code Generation Agent** (4-5 min)
   - Generates minimal code to pass tests (GREEN phase)
   - Follows established project patterns and conventions
   - Maintains architectural consistency per Architecture Agent guidance

4. **♻️ Refactoring Agent** (2-3 min)
   - Improves code quality while maintaining test passage (REFACTOR phase)
   - Applies code quality standards and performance optimizations
   - Validates no functionality regression

5. **👥 Review Agent** (1-2 min)
   - Performs final code review against project standards
   - Validates TDD process compliance and quality criteria
   - Confirms documentation requirements are met

**Success Criteria**: Feature implemented with 100% TDD compliance, >95% test coverage, passes all quality gates

### Bug Fix Workflow
**Use Case**: Systematic problem resolution with root cause analysis
```bash
/coordinate-agents bug-fix --issue="authentication timeout errors"
```

**Agent Coordination Flow**:
1. **🔍 Debugging Agent** (3-4 min) *[Primary Lead]*
   - Analyzes error patterns and reproduces issue systematically
   - Identifies root cause using project-specific debugging strategies
   - Maps issue impact across system components

2. **🏗️ Architecture Agent** (2-3 min)
   - Assesses architectural implications of potential fixes
   - Identifies system-wide impacts and integration considerations
   - Recommends solution approaches that align with system design

3. **🧪 Testing Agent** (2-3 min)
   - Creates tests that reproduce the bug (RED state)
   - Validates fix effectiveness with comprehensive test coverage
   - Ensures regression prevention with ongoing test monitoring

4. **⚙️ Code Generation Agent** (2-3 min)
   - Implements fix following architecture recommendations
   - Ensures solution follows project coding standards
   - Maintains consistency with existing codebase patterns

5. **⚡ Performance Agent** (1-2 min)
   - Validates fix doesn't introduce performance regressions
   - Monitors impact on system performance metrics
   - Recommends optimizations if needed

6. **👥 Review Agent** (1-2 min)
   - Reviews fix implementation against project standards
   - Validates testing adequacy and documentation updates
   - Confirms issue resolution meets quality criteria

**Success Criteria**: Root cause identified, fix implemented with test coverage, no performance regression, issue resolved

### Feature Development Workflow
**Use Case**: Complete feature implementation from requirements to deployment
```bash
/coordinate-agents feature --spec="shopping cart functionality"
```

**Agent Coordination Flow**:
1. **🏢 Domain Expert Agent** (3-4 min) *[Primary Lead]*
   - Analyzes feature requirements against business domain
   - Defines business logic and validation rules
   - Identifies data models and business process flows

2. **🏗️ Architecture Agent** (3-4 min)
   - Designs feature architecture and integration patterns
   - Identifies system components and interaction points
   - Plans scalability and performance considerations

3. **🧪 Testing Agent** (4-5 min)
   - Creates comprehensive test strategy and test cases
   - Implements unit, integration, and acceptance tests
   - Establishes quality gates and coverage requirements

4. **⚙️ Code Generation Agent** (5-6 min)
   - Implements feature components following architectural design
   - Generates code adhering to established patterns and standards
   - Creates integration points and API endpoints

5. **📝 Documentation Agent** (2-3 min)
   - Creates feature documentation and API specifications
   - Updates system documentation and user guides
   - Ensures knowledge transfer and maintainability

6. **⚡ Performance Agent** (2-3 min)
   - Validates feature performance against requirements
   - Identifies optimization opportunities and bottlenecks
   - Implements performance monitoring and alerting

7. **🛡️ Security Agent** (2-3 min)
   - Reviews feature for security vulnerabilities
   - Validates authentication and authorization requirements
   - Ensures compliance with security standards

8. **👥 Review Agent** (2-3 min)
   - Performs comprehensive code and design review
   - Validates feature completeness and quality
   - Confirms readiness for deployment

**Success Criteria**: Feature fully implemented with comprehensive testing, documentation, performance validation, and security review

### Refactoring Workflow  
**Use Case**: Technical debt reduction and code quality improvement
```bash
/coordinate-agents refactor --target="payment processing module"
```

**Agent Coordination Flow**:
1. **♻️ Refactoring Agent** (4-5 min) *[Primary Lead]*
   - Analyzes technical debt and improvement opportunities
   - Plans refactoring strategy maintaining functionality
   - Identifies risk mitigation and rollback procedures

2. **🏗️ Architecture Agent** (3-4 min)
   - Reviews refactoring plan against architectural principles
   - Ensures improvements align with system design goals
   - Identifies architectural enhancement opportunities

3. **🧪 Testing Agent** (3-4 min)
   - Creates comprehensive test coverage for existing functionality
   - Implements characterization tests to preserve behavior
   - Validates refactoring maintains functionality throughout process

4. **⚙️ Code Generation Agent** (4-5 min)
   - Implements refactoring changes following established patterns
   - Maintains code quality and consistency standards
   - Applies improved patterns while preserving functionality

5. **⚡ Performance Agent** (2-3 min)
   - Measures performance impact of refactoring changes
   - Validates improvements meet performance goals
   - Identifies additional optimization opportunities

6. **👥 Review Agent** (2-3 min)
   - Reviews refactored code for quality and maintainability
   - Validates improvement objectives are achieved
   - Confirms technical debt reduction goals are met

**Success Criteria**: Technical debt reduced, code quality improved, functionality preserved, performance maintained or improved

### Deployment Workflow
**Use Case**: Production deployment with comprehensive validation and monitoring
```bash
/coordinate-agents deployment --environment="production" --strategy="blue-green"
```

**Agent Coordination Flow**:
1. **🚀 DevOps Agent** (4-5 min) *[Primary Lead]*
   - Plans deployment strategy and rollback procedures
   - Configures infrastructure and deployment pipeline
   - Sets up monitoring and alerting for deployment

2. **🧪 Testing Agent** (3-4 min)
   - Runs comprehensive test suite before deployment
   - Validates deployment readiness and quality gates
   - Prepares post-deployment validation tests

3. **🛡️ Security Agent** (2-3 min)
   - Performs security validation and vulnerability scanning
   - Validates configuration security and compliance
   - Ensures secure deployment practices

4. **⚡ Performance Agent** (2-3 min)
   - Validates performance benchmarks before deployment
   - Sets up performance monitoring and alerting
   - Prepares performance validation post-deployment

5. **📝 Documentation Agent** (1-2 min)
   - Updates deployment documentation and runbooks
   - Documents configuration changes and procedures
   - Creates rollback and troubleshooting guides

6. **👥 Review Agent** (1-2 min)
   - Final deployment readiness review
   - Validates all quality gates and approval criteria
   - Confirms deployment meets standards and requirements

**Success Criteria**: Successful production deployment with monitoring, rollback capability, performance validation, security compliance

## 🤖 Custom Workflow Creation

### Define Your Own Multi-Agent Workflows
```bash
# Create custom workflow with specific agent sequence
/coordinate-agents --custom --save-workflow="api-integration"
```

**Custom Workflow Builder**:
1. **Task Definition**: Define the overall objective and success criteria
2. **Agent Selection**: Choose which specialized agents should participate
3. **Sequence Planning**: Define the order and dependencies between agents
4. **Handoff Points**: Specify what information passes between agents
5. **Quality Gates**: Define validation checkpoints throughout the workflow
6. **Save Template**: Save custom workflow for future reuse

### Advanced Coordination Features

**🔄 Dynamic Agent Routing**
- **Conditional Branching**: Different agent paths based on analysis results
- **Parallel Processing**: Multiple agents working simultaneously on independent tasks
- **Adaptive Workflows**: Workflow adjusts based on intermediate results and findings

**⚡ Real-Time Conflict Resolution**
- **Conflict Detection**: Automatically identify when agents provide contradictory guidance
- **Expert Arbitration**: Route conflicts to most specialized agent for resolution
- **User Override**: Allow user to resolve conflicts when agents disagree

**📊 Progress Monitoring and Control**
- **Real-Time Dashboard**: Live view of agent progress and intermediate results
- **Pause and Resume**: Stop workflow at any point and resume later
- **Quality Checkpoints**: Validate agent outputs before proceeding to next steps

## 🎛️ Coordination Control Options

### Interactive Mode
```bash
/coordinate-agents feature --interactive
```
- **Agent Selection**: Choose specific agents for the workflow
- **Approval Gates**: Approve each agent's contribution before proceeding
- **Real-Time Adjustments**: Modify workflow based on intermediate results
- **Quality Control**: Review and edit agent outputs before handoffs

### Autonomous Mode
```bash
/coordinate-agents tdd --autonomous --quality-threshold=95
```
- **Full Automation**: Agents work together with minimal user intervention
- **Quality Thresholds**: Automatic validation against defined quality criteria
- **Exception Handling**: User intervention only when conflicts or failures occur
- **Progress Reports**: Regular status updates without requiring user action

### Hybrid Mode (Default)
```bash
/coordinate-agents bug-fix --hybrid
```
- **Smart Checkpoints**: User approval required only at key decision points
- **Automatic Handoffs**: Routine information transfer happens automatically
- **Quality Gates**: User review when quality thresholds aren't met
- **Flexible Control**: Switch between autonomous and interactive as needed

## 📊 Coordination Outcomes and Quality Assurance

### Multi-Agent Success Metrics
- **Workflow Completion**: Percentage of workflows completed successfully (target: >90%)
- **Agent Collaboration**: Effective handoffs and information sharing (target: >95%)
- **Quality Consistency**: All agents maintain specialization boundaries (target: 100%)
- **User Satisfaction**: Approval ratings for coordinated outcomes (target: >4.5/5)

### Real-Time Quality Monitoring
- **Agent Performance**: Individual agent contribution quality during workflows
- **Handoff Success**: Effectiveness of information transfer between agents
- **Conflict Resolution**: Speed and accuracy of resolving agent disagreements
- **Workflow Efficiency**: Time to complete workflows compared to manual approaches

## ⚡ Usage Examples

### Start Pre-Built Workflow
```bash
# TDD feature development
/coordinate-agents tdd --feature="user profile management"

# Bug fix with root cause analysis  
/coordinate-agents bug-fix --issue="database connection timeouts"

# Production deployment
/coordinate-agents deployment --environment=production
```

### Custom Agent Combination
```bash
# Specific agents for performance optimization
/coordinate-agents --custom --agents="architecture,performance,testing,review"

# Security-focused feature development
/coordinate-agents feature --agents="domain,architecture,code-gen,security,testing,review"
```

### Advanced Coordination
```bash
# Save custom workflow for reuse
/coordinate-agents --create-template="microservice-development" --interactive

# Resume paused workflow
/coordinate-agents --resume --workflow-id="tdd-auth-feature-20240805"
```

## 🔗 Integration with Agent Ecosystem

### Seamless Integration
- **Active Agent Detection**: Only coordinates with currently active agents
- **Context Synchronization**: All agents work with current project state
- **Performance Monitoring**: Coordination outcomes feed back into agent improvement
- **Workflow Templates**: Successful workflows become reusable templates

## 🚀 Success Criteria

**Orchestration Success**: Multiple agents work together without conflicts or overlaps
**Quality Outcomes**: Coordinated work meets or exceeds single-agent quality
**Efficiency Gains**: Multi-agent workflows complete complex tasks faster than sequential approaches
**User Control**: Clear oversight and control over multi-agent processes

**🎯 Final Result**: A seamless team of specialized AI agents working together on complex projects, each contributing their unique expertise while maintaining quality and consistency throughout the entire workflow.