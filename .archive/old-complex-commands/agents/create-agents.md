---
name: create-agents
description: Generate project-specific specialized agents from deep discovery consultation
usage: "create-agents [all|architecture|code-gen|testing|debug|docs|review|perf|security|integration|domain|refactor|migration|devops|data] [--from-consultation|--from-template]"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, LS, TodoWrite]
category: agents
argument-hint: "[agent-type] [--source-method]"
version: "1.0"
---

# Create Agents: Generate Project-Specific Specialized Agents

## Purpose: Transform Consultation Results into Specialized Agent Team

The `/create-agents` command takes the deep discovery consultation results and generates a team of specialized agents tailored to your specific project's architecture, domain, and workflows. This creates REAL agents with genuine project understanding, not generic templates.

**Agent Creation Philosophy**: Project-specific expertise over generic capabilities, measurable specialization over template theater, validation-proven effectiveness over assumed utility.

## 🎯 How Agent Creation Works

### From Deep Discovery to Specialized Agents
1. **Consultation Analysis**: Process results from `/begin-consultation` phases
2. **Project DNA Extraction**: Identify unique patterns, frameworks, and domain knowledge
3. **Agent Specification**: Define specific capabilities based on project needs
4. **Agent Generation**: Create specialized agents using project-specific knowledge
5. **Validation Testing**: Verify each agent's effectiveness with project scenarios
6. **Team Coordination**: Establish inter-agent protocols and handoff procedures

## 🤖 The 14 Specialized Agent Types

### Core Coordination Agents (4)
**🏗️ Architecture Agent** - *System Design & Patterns Specialist*
- Analyzes your specific architecture (microservices, monolith, serverless, etc.)
- Understands your framework patterns (React/Vue/Angular, Spring/Express/Rails, etc.)
- Guides technical decisions using your project's architectural principles
- Validates system design against your performance requirements

**⚙️ Code Generation Agent** - *Project-Specific Code Creation*
- Generates code following your exact coding standards and conventions
- Understands your project structure and naming patterns
- Creates components using your established architectural patterns
- Maintains consistency with your existing codebase style

**🧪 Testing Agent** - *TDD Enforcement & Quality Assurance*
- Implements your specific testing strategies (unit/integration/e2e)
- Understands your testing frameworks and patterns
- Enforces TDD with code deletion penalty for non-compliant work
- Validates test coverage according to your project standards

**🔍 Debugging Agent** - *Project-Aware Problem Diagnosis*
- Recognizes your project's common error patterns and failure modes
- Understands your logging and monitoring setup
- Provides debugging strategies specific to your architecture
- Suggests fixes based on your project's historical patterns

### Specialized Function Agents (10)
**📝 Documentation Agent** - *Technical Writing & Knowledge Management*
- Writes documentation in your project's established style and format
- Understands your documentation standards and audience
- Creates API docs, code comments, and guides using your conventions
- Maintains consistency with your existing documentation patterns

**👥 Review Agent** - *Code Review & Standards Enforcement*
- Applies your team's specific code review standards and checklists
- Understands your definition of done and quality gates
- Reviews code against your project's architectural principles
- Validates adherence to your team's development workflow

**⚡ Performance Agent** - *Optimization & Scalability Specialist*
- Analyzes performance using your specific metrics and requirements
- Understands your performance bottlenecks and scaling patterns
- Optimizes code according to your performance goals
- Validates improvements against your benchmark standards

**🛡️ Security Agent** - *Vulnerability Detection & Compliance*
- Applies security standards specific to your industry and domain
- Understands your compliance requirements (SOC2, HIPAA, PCI, etc.)
- Identifies vulnerabilities relevant to your technology stack
- Validates security implementations against your threat model

**🔗 Integration Agent** - *External Systems & API Specialist*
- Understands your specific API integrations and external services
- Knows your data flow patterns and integration strategies
- Handles authentication and authorization according to your standards
- Manages your specific error handling and retry patterns

**🏢 Domain Expert Agent** - *Business Logic & Rules Specialist*
- Deeply understands your business domain and terminology
- Implements business rules according to your domain models
- Validates business logic against your requirements
- Guides domain-driven design decisions for your specific industry

**♻️ Refactoring Agent** - *Technical Debt & Code Improvement*
- Identifies technical debt specific to your codebase patterns
- Understands your refactoring priorities and constraints
- Improves code while maintaining your architectural principles
- Plans refactoring strategies that fit your release schedule

**🔄 Migration Agent** - *Framework Transitions & Upgrades*
- Guides migrations specific to your technology stack
- Understands your deployment constraints and rollback procedures
- Plans upgrade strategies that minimize risk to your specific setup
- Handles data migrations according to your data governance policies

**🚀 DevOps Agent** - *CI/CD & Deployment Specialist*
- Understands your specific CI/CD pipeline and deployment process
- Knows your infrastructure patterns and scaling requirements
- Manages deployments according to your release procedures
- Monitors using your specific observability and alerting setup

**📊 Data Agent** - *Database & Analytics Specialist*
- Understands your specific data models and database patterns
- Knows your data pipeline and analytics requirements
- Optimizes queries according to your performance characteristics
- Manages data according to your governance and privacy policies

## 🔧 Agent Creation Process

### Step 1: Consultation Analysis (30 seconds)
```bash
# Analyze consultation results to determine needed agents
create-agents --analyze-consultation /path/to/consultation-results
```

**Process**:
- Read consultation state from `.claude/consultation-state.json`
- Extract technical architecture insights from Phase 1
- Extract domain knowledge from Phase 2
- Extract context patterns from Phase 3
- Identify specific agent needs based on project DNA

### Step 2: Agent Selection & Specification (1-2 minutes)
```bash
# Interactive agent selection based on project needs
create-agents --select-agents
```

**Interactive Selection Process**:
- Present recommended agents based on consultation analysis
- Show capability descriptions for each recommended agent
- Allow user to add/remove agents based on project priorities
- Define success criteria and performance metrics for each agent

### Step 3: Agent Generation (2-3 minutes per agent)
```bash
# Generate specific agents based on project analysis
create-agents architecture --from-consultation
create-agents testing --from-consultation
create-agents domain --from-consultation
```

**Generation Process**:
- Load project-specific knowledge from consultation results
- Apply agent templates with project DNA integration
- Customize capabilities based on technology stack and patterns
- Generate agent-specific context files and knowledge bases
- Validate agent specifications against project requirements

### Step 4: Agent Team Validation (2-3 minutes)
```bash
# Validate complete agent team effectiveness
create-agents --validate-team
```

**Team Validation Process**:
- Test each agent with project-specific scenarios
- Validate inter-agent coordination and handoff protocols
- Measure response quality and specialization accuracy
- Verify no capability gaps or overlaps
- Generate agent effectiveness report

## 📊 Agent Creation Outputs

### Generated Agent Files
```
.claude/agents/
├── architecture-agent.md      # System design specialist
├── code-generation-agent.md   # Project-specific code creator
├── testing-agent.md           # TDD enforcement specialist
├── debugging-agent.md         # Problem diagnosis expert
├── documentation-agent.md     # Technical writing specialist
├── review-agent.md           # Code review standards enforcer
├── performance-agent.md      # Optimization specialist
├── security-agent.md         # Vulnerability detection expert
├── integration-agent.md      # API & external systems specialist
├── domain-expert-agent.md    # Business logic specialist
├── refactoring-agent.md      # Technical debt manager
├── migration-agent.md        # Framework transition expert
├── devops-agent.md          # CI/CD & deployment specialist
├── data-agent.md            # Database & analytics expert
└── agent-coordination.json   # Inter-agent protocols
```

### Agent Metadata
Each generated agent includes:
- **Project-Specific Knowledge**: Understanding of your exact architecture and patterns
- **Capability Boundaries**: Clear definition of what the agent can and cannot do
- **Success Metrics**: Measurable criteria for agent effectiveness
- **Context Integration**: Connection to your project's context hierarchy
- **Coordination Protocols**: How the agent interacts with other specialized agents

## 🎯 Agent Effectiveness Validation

### Real-Time Testing During Creation
- **Scenario Testing**: Each agent tested with realistic project scenarios
- **Knowledge Validation**: Agent knowledge verified against consultation insights
- **Response Quality**: Agent responses measured for accuracy and relevance
- **Specialization Verification**: Agents stay within defined capability boundaries

### Performance Metrics
- **Response Accuracy**: Agent provides correct project-specific guidance (target: >95%)
- **Context Relevance**: Agent responses relevant to your project context (target: >90%)
- **Specialization Compliance**: Agent stays within defined boundaries (target: 100%)
- **Team Coordination**: Effective handoffs between agents (target: >90% success rate)

## 🔗 Integration with Agent Management Commands

### Seamless Workflow Integration
The created agents integrate with:
- **`/list-agents`**: View all created agents and their capabilities
- **`/activate-agent`**: Enable specific agents for use
- **`/coordinate-agents`**: Orchestrate multi-agent workflows
- **`/test-agents`**: Validate ongoing agent effectiveness
- **`/update-agents`**: Refresh agent knowledge from updated context

## ⚡ Usage Examples

### Create All Recommended Agents
```bash
# Generate complete agent team based on consultation
/create-agents all --from-consultation
```

### Create Specific Agent Types
```bash
# Create just the essential agents
/create-agents architecture testing domain --from-consultation

# Create DevOps-focused agent team
/create-agents devops performance security --from-consultation
```

### Validate Agent Team
```bash
# Test complete agent team effectiveness
/create-agents --validate-team --report-performance
```

## 🚀 Success Criteria

**Agent Creation Success**: All selected agents generated with project-specific knowledge and validated effectiveness
**Team Coordination Success**: Agents demonstrate effective handoff protocols and collaboration
**Performance Success**: Agents meet defined performance metrics for accuracy and relevance
**Integration Success**: Agents seamlessly integrate with existing consultation workflow

**🎯 Final Result**: A specialized team of project-aware agents that understand your specific architecture, domain, and workflows, ready to provide expert-level assistance tailored to your unique project needs.