---
name: activate-agent
description: Enable and configure specific specialized agents for immediate use
usage: "activate-agent [agent-name] [--interactive] [--batch] [--with-dependencies]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS]
category: agents
argument-hint: "[agent-name|all] [--options]"
version: "1.0"
---

# Activate Agent: Enable Specialized Project Intelligence

## Purpose: Smart Agent Activation with Dependency Management

The `/activate-agent` command intelligently enables specialized agents for immediate use, handling prerequisites, dependencies, and configuration automatically. This ensures agents are ready to provide expert-level assistance with your specific project context and requirements.

**Agent Activation Philosophy**: Intelligent dependency resolution, seamless context integration, user-controlled activation with guided recommendations, transparent readiness validation.

## 🎯 Smart Activation System

### Intelligent Agent Selection
- **Context-Aware Recommendations**: Suggests agents based on current project activity and needs
- **Dependency Resolution**: Automatically identifies and activates prerequisite agents
- **Performance Validation**: Ensures agents meet quality thresholds before activation
- **Integration Testing**: Validates agent compatibility with current project state

### User Control and Transparency
- **Interactive Mode**: Guided agent selection with clear capability explanations
- **Batch Activation**: Enable multiple agents simultaneously with conflict resolution
- **Preview Mode**: See what will be activated before committing changes
- **Rollback Safety**: Easy deactivation if agent doesn't meet expectations

## 🤖 Available Agents for Activation

### Core Coordination Agents (Always Recommended)
These agents provide foundational project intelligence and coordination:

**🏗️ Architecture Agent** - *Essential for all projects*
```
Prerequisites: Project consultation Phase 1 completed
Dependencies: None (foundational agent)
Activation Time: ~30 seconds
Ready State: Can analyze system design and guide technical decisions

Capabilities After Activation:
  ✓ Real-time architectural guidance
  ✓ Technical decision support
  ✓ Design pattern recommendations
  ✓ Performance trade-off analysis
```

**🧪 Testing Agent** - *Critical for quality assurance*
```
Prerequisites: Project testing framework detected or configured
Dependencies: Architecture Agent (for understanding system design)
Activation Time: ~45 seconds
Ready State: TDD enforcement active with code deletion penalty

Capabilities After Activation:
  ✓ Automatic test generation and validation
  ✓ TDD workflow enforcement
  ✓ Test coverage monitoring
  ✓ Quality gate validation
```

**⚙️ Code Generation Agent** - *High-value for development speed*
```
Prerequisites: Project patterns and conventions analyzed
Dependencies: Architecture Agent (for design consistency)
Activation Time: ~60 seconds
Ready State: Can generate project-specific code following your conventions

Capabilities After Activation:
  ✓ Code generation following project standards
  ✓ Component creation with architectural consistency
  ✓ Boilerplate reduction and automation
  ✓ Pattern-based code suggestions
```

**🔍 Debugging Agent** - *Essential for problem resolution*
```
Prerequisites: Project error patterns and logging analyzed
Dependencies: Architecture Agent (for system understanding)
Activation Time: ~45 seconds
Ready State: Can diagnose issues specific to your project architecture

Capabilities After Activation:
  ✓ Project-aware error diagnosis
  ✓ Debugging strategy recommendations
  ✓ Historical pattern-based solutions
  ✓ Monitoring and logging guidance
```

### Specialized Function Agents (Activate as Needed)

**📝 Documentation Agent** - *Recommended for team projects*
```
Prerequisites: Documentation standards and audience defined
Dependencies: Domain Expert Agent (for accurate terminology)
Activation Time: ~40 seconds
Ready State: Can create documentation following your project style

Best Used When: Creating API docs, updating guides, onboarding materials
```

**👥 Review Agent** - *Essential for team development*
```
Prerequisites: Code review standards and quality gates defined
Dependencies: Testing Agent (for quality validation)
Activation Time: ~35 seconds
Ready State: Can review code against your team's standards

Best Used When: Code reviews, quality validation, standards enforcement
```

**⚡ Performance Agent** - *Activate when optimization needed*
```
Prerequisites: Performance requirements and metrics defined
Dependencies: Architecture Agent (for system understanding)
Activation Time: ~50 seconds
Ready State: Can analyze and optimize performance for your specific requirements

Best Used When: Performance bottlenecks, optimization planning, scaling decisions
```

**🛡️ Security Agent** - *Critical for production systems*
```
Prerequisites: Security requirements and compliance standards defined
Dependencies: Architecture Agent (for threat model understanding)
Activation Time: ~55 seconds
Ready State: Can scan for vulnerabilities and validate security implementations

Best Used When: Security reviews, compliance validation, vulnerability assessment
```

**🔗 Integration Agent** - *Activate when working with external systems*
```
Prerequisites: API documentation and integration patterns available
Dependencies: Domain Expert Agent (for data flow understanding)
Activation Time: ~45 seconds
Ready State: Can manage API integrations and external service connections

Best Used When: API integrations, third-party services, data flow management
```

**🏢 Domain Expert Agent** - *High value for business logic*
```
Prerequisites: Business domain knowledge and terminology extracted from consultation
Dependencies: None (provides domain foundation for other agents)
Activation Time: ~40 seconds
Ready State: Can guide business logic implementation and domain decisions

Best Used When: Business logic, domain modeling, requirements clarification
```

**♻️ Refactoring Agent** - *Activate during code improvement phases*
```
Prerequisites: Technical debt analysis and refactoring priorities identified
Dependencies: Architecture Agent, Code Generation Agent
Activation Time: ~60 seconds
Ready State: Can plan and execute refactoring strategies

Best Used When: Technical debt reduction, code improvement, architectural evolution
```

**🔄 Migration Agent** - *Use for framework transitions*
```
Prerequisites: Migration requirements and constraints defined
Dependencies: Architecture Agent, Testing Agent
Activation Time: ~70 seconds
Ready State: Can guide framework migrations and technology transitions

Best Used When: Framework upgrades, technology migrations, system transitions
```

**🚀 DevOps Agent** - *Essential for deployment and operations*
```
Prerequisites: CI/CD pipeline and infrastructure patterns analyzed
Dependencies: Performance Agent (for optimization), Security Agent (for compliance)
Activation Time: ~65 seconds
Ready State: Can manage deployment strategies and operational concerns

Best Used When: CI/CD optimization, deployment planning, infrastructure scaling
```

**📊 Data Agent** - *Activate for data-intensive applications*
```
Prerequisites: Data models and database patterns analyzed
Dependencies: Performance Agent (for optimization), Domain Expert Agent (for modeling)
Activation Time: ~55 seconds
Ready State: Can optimize database queries and manage data workflows

Best Used When: Database optimization, data pipeline management, analytics implementation
```

## 🔧 Activation Process

### Step 1: Agent Selection (Interactive Mode)
```bash
# Interactive agent selection with recommendations
/activate-agent --interactive
```

**Interactive Selection Process**:
1. **Current State Analysis**: Show currently active agents and project activity
2. **Smart Recommendations**: Suggest agents based on recent work patterns and project needs
3. **Capability Preview**: Display what each agent can do once activated
4. **Dependency Mapping**: Show which other agents will be activated automatically
5. **Impact Estimation**: Predict performance improvement and resource usage

### Step 2: Prerequisite Validation (Automatic)
```bash
# System automatically validates prerequisites
Checking prerequisites for Architecture Agent...
✓ Project consultation Phase 1 completed
✓ Technical architecture analysis available
✓ Framework patterns identified
✓ Performance requirements documented

Prerequisite validation: PASSED
```

### Step 3: Dependency Resolution (Automatic)
```bash
# System resolves and activates dependencies
Activating Testing Agent requires:
  → Architecture Agent (foundational understanding)
  
Dependency resolution plan:
1. Activate Architecture Agent (30s)
2. Validate integration (10s)  
3. Activate Testing Agent (45s)

Total activation time: ~85 seconds
Continue? [Y/n]
```

### Step 4: Agent Configuration (Guided)
```bash
# System configures agent with project-specific knowledge
Configuring Testing Agent with project context...
✓ Loading test framework patterns (Jest/Mocha detected)
✓ Applying test coverage requirements (85% minimum)
✓ Configuring TDD enforcement rules
✓ Setting up quality gates and validation criteria

Configuration complete. Testing Agent ready.
```

### Step 5: Activation Validation (Automatic)
```bash
# System validates successful activation
Testing Agent activation validation...
✓ Context integration successful
✓ Response quality test passed (96% accuracy)
✓ Specialization boundaries verified
✓ Integration with Architecture Agent successful

Agent Status: ACTIVE and ready for use
Performance Baseline: 96% accuracy, <2s response time
```

## ⚡ Activation Options and Modes

### Single Agent Activation
```bash
# Activate specific agent with full validation
/activate-agent architecture
/activate-agent testing --with-dependencies
/activate-agent domain --interactive
```

### Batch Agent Activation
```bash
# Activate multiple agents simultaneously
/activate-agent architecture testing domain --batch
/activate-agent all --core-only
/activate-agent performance security devops --for-production
```

### Conditional Activation
```bash
# Activate based on project activity patterns
/activate-agent --auto-recommend    # Activate based on recent work
/activate-agent --for-phase=development    # Activate for specific work phase
/activate-agent --performance-focused      # Activate optimization-focused agents
```

## 📊 Activation Status and Feedback

### Real-Time Progress Updates
```bash
Activating Architecture Agent...
[████████████████████████████████] 100% Complete

Configuration Details:
  ✓ Framework Analysis: React + Node.js detected and configured
  ✓ Architecture Pattern: Microservices with API Gateway recognized  
  ✓ Performance Profile: High-traffic web application optimizations loaded
  ✓ Integration Points: 3 external APIs and 2 databases mapped

Agent Ready: Architecture guidance now available for your specific React + Node.js microservices setup
Response Quality: 98% accuracy based on project validation tests
Specialization: System design, technical decisions, performance trade-offs
```

### Post-Activation Validation Report
```bash
Activation Summary Report:
┌─────────────────────┬──────────┬───────────────┬─────────────────┐
│ Agent               │ Status   │ Response Time │ Accuracy Score  │
├─────────────────────┼──────────┼───────────────┼─────────────────┤
│ Architecture        │ ACTIVE   │ 1.2s         │ 98%            │
│ Testing             │ ACTIVE   │ 1.8s         │ 95%            │
│ Domain Expert       │ ACTIVE   │ 1.5s         │ 97%            │
└─────────────────────┴──────────┴───────────────┴─────────────────┘

Ready for Use: 3 agents active and performing above baseline thresholds
Next Recommendations: Consider activating Code Generation Agent for development speed improvement
```

## 🔗 Integration with Agent Ecosystem

### Seamless Workflow Integration
Activated agents automatically integrate with:
- **`/coordinate-agents`**: Available for multi-agent workflows
- **`/test-agents`**: Included in ongoing performance monitoring
- **`/update-agents`**: Eligible for knowledge refresh and improvement
- **Project Commands**: Available to assist with any project-related tasks

### Context Synchronization
- **Real-Time Context**: Agents stay synchronized with current project state
- **Cross-Agent Communication**: Activated agents can collaborate and hand off tasks
- **Performance Monitoring**: Continuous monitoring ensures agents maintain effectiveness
- **Auto-Updates**: Agents automatically refresh knowledge as project evolves

## 🚀 Success Criteria

**Activation Speed**: Agents ready for use in under 2 minutes with full validation
**Quality Assurance**: All activated agents meet performance baselines (>95% accuracy)
**Integration Success**: Agents seamlessly work with existing project workflow
**User Confidence**: Clear understanding of agent capabilities and readiness state

**🎯 Final Result**: Your selected specialized agents are active, validated, and ready to provide expert-level assistance tailored to your specific project's architecture, domain, and development workflow.