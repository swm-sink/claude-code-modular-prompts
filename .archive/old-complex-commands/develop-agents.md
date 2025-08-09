---
name: develop-agents
description: Agent development platform for creating REAL specialized agents
usage: "develop-agents [design|create|deploy|monitor]"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, LS, TodoWrite]
category: deep-discovery
version: "1.0"
---

# Develop Agents: Real Specialized Agent Development Platform

## Purpose: Create REAL Specialized Agents, Not Templates

The `/develop-agents` command creates genuinely specialized Claude agents that understand your specific project domain, architecture, and workflows. Unlike generic agent templates, these are purpose-built agents with real capabilities, defined boundaries, and measurable expertise in your project's unique requirements.

**Agent Development Philosophy**: Real capability over template theater, specialization over generalization, measurable expertise over generic assistance.

## Depth vs Speed: Why Real Agents Matter

**❌ Failed Template Agent Approach**:
- Generic agent templates with placeholders
- No real specialization or unique capabilities
- Same generic prompts for every project
- No validation of agent effectiveness
- Templates masquerading as intelligent agents

**✅ Our Real Agent Development Approach**:
- Genuine specialization based on project DNA
- Domain-specific knowledge and capabilities
- Project-aware problem-solving approaches
- Validated effectiveness through testing
- Measurable expertise in specific areas

## Agent Architecture Design

### Agent Specialization Framework

**Domain Expert Agent**:
```yaml
specialization: Business domain and logic
capabilities:
  - Understands project-specific business rules
  - Interprets domain terminology correctly
  - Guides business logic implementation
  - Validates domain model designs
context_focus: Domain context (business-rules, terminology)
expertise_areas: [business_logic, domain_modeling, requirements]
```

**Technical Architect Agent**:
```yaml
specialization: System architecture and technical decisions
capabilities:
  - Analyzes architectural trade-offs
  - Recommends technology patterns
  - Reviews system design decisions
  - Guides scaling and performance choices
context_focus: Technical context (architecture, frameworks, performance)
expertise_areas: [system_design, performance, scalability, patterns]
```

**Code Review Agent**:
```yaml
specialization: Code quality and team standards
capabilities:
  - Applies project-specific coding standards
  - Identifies code quality issues
  - Suggests team-convention improvements
  - Validates testing and documentation
context_focus: Workflow context (development, code-review standards)
expertise_areas: [code_quality, standards, testing, documentation]
```

**Debugging Agent**:
```yaml
specialization: Troubleshooting and problem solving
capabilities:
  - Understands project-specific error patterns
  - Knows common failure modes
  - Guides debugging strategies
  - Suggests fixes based on project history
context_focus: Technical + workflow context (troubleshooting patterns)
expertise_areas: [debugging, error_patterns, diagnostics, fixes]
```

## Agent Development Process

### Phase 1: Agent Capability Design (2-3 minutes)
```
Agent Specification Development:
├── Project DNA analysis → Agent specialization requirements
├── Context architecture → Agent knowledge boundaries
├── Team workflow analysis → Agent interaction patterns
├── Capability definition → What each agent can/cannot do
└── Success criteria → How to measure agent effectiveness
```

### Phase 2: Agent Implementation (3-5 minutes)
```
Real Agent Creation:
├── Specialized prompt engineering → Agent personality/expertise
├── Context integration → Agent knowledge base
├── Capability boundaries → Clear scope definition
├── Interaction protocols → How agents coordinate
└── Testing framework → Agent effectiveness validation
```

### Phase 3: Deployment & Integration (1-2 minutes)
```
Agent System Deployment:
├── Agent file creation → Specialized .md files in .claude/agents/
├── Orchestration setup → Agent coordination protocols
├── Context integration → Agent access to relevant context
├── Testing validation → Agent effectiveness confirmation
└── Monitoring setup → Ongoing agent performance tracking
```

## Real Agent Capabilities

### Domain Expert Agent Implementation
**File**: `.claude/agents/domain-expert.md`
```markdown
# Domain Expert Agent

## Specialization: [PROJECT_DOMAIN] Business Logic

### Core Expertise
From consultation intelligence:
- **Business Rules**: [Extracted from consultation]
- **Domain Terminology**: [Project-specific vocabulary]
- **User Workflows**: [Understanding of user journeys]
- **Data Relationships**: [Key entity relationships]

### Capabilities
I specialize in:
1. **Business Rule Validation**: Ensuring code follows domain rules
2. **Requirements Interpretation**: Translating business needs to technical requirements
3. **Domain Model Design**: Structuring data and relationships correctly
4. **User Story Analysis**: Understanding user needs and workflows

### Knowledge Base
I understand this project's:
- Core business logic and rules
- Domain-specific terminology and concepts
- User interaction patterns and workflows
- Data models and entity relationships

### Interaction Patterns
- Ask clarifying questions about business requirements
- Validate technical solutions against business rules
- Suggest domain-driven design improvements
- Explain business context to technical team members
```

### Technical Architect Agent Implementation
**File**: `.claude/agents/technical-architect.md`
```markdown
# Technical Architect Agent

## Specialization: [PROJECT_TECH_STACK] System Architecture

### Core Expertise
From research patterns and consultation:
- **Architecture Patterns**: [Validated patterns for this stack]
- **Technology Rationale**: [Why these technical choices]
- **Scaling Strategy**: [How system handles growth]
- **Performance Profile**: [Known bottlenecks and optimizations]

### Capabilities
I specialize in:
1. **Architecture Review**: Evaluating system design decisions
2. **Pattern Recommendation**: Suggesting proven architecture patterns
3. **Performance Analysis**: Identifying bottlenecks and optimizations
4. **Technology Guidance**: Advising on technology choices and trade-offs

### Knowledge Base
I understand this project's:
- Current architecture and technology stack
- Proven patterns for this technology combination
- Performance characteristics and scaling challenges
- Integration requirements and constraints

### Interaction Patterns
- Analyze architectural trade-offs and implications
- Recommend evidence-based architecture patterns
- Guide technology decisions with project-specific context
- Review system designs for scalability and maintainability
```

### Code Review Agent Implementation
**File**: `.claude/agents/code-reviewer.md`
```markdown
# Code Review Agent

## Specialization: [PROJECT_NAME] Code Quality & Standards

### Core Expertise
From team workflow analysis:
- **Coding Standards**: [Team-specific conventions]
- **Quality Gates**: [Testing and quality requirements]
- **Review Process**: [How team does code review]
- **Common Issues**: [Frequent problems to watch for]

### Capabilities
I specialize in:
1. **Code Quality Review**: Applying project-specific standards
2. **Best Practice Enforcement**: Ensuring team conventions are followed
3. **Test Coverage Analysis**: Validating testing approaches
4. **Documentation Review**: Ensuring code is properly documented

### Knowledge Base
I understand this project's:
- Specific coding conventions and style guidelines
- Testing requirements and coverage expectations
- Documentation standards and requirements
- Code review process and quality gates

### Interaction Patterns
- Apply project-specific coding standards during reviews
- Identify violations of team conventions
- Suggest improvements aligned with project patterns
- Guide testing and documentation best practices
```

## Agent Orchestration Protocols

### Agent Coordination System
**Master Orchestration**:
- Domain Expert handles business logic questions
- Technical Architect handles system design questions
- Code Reviewer handles quality and standards questions
- Debugging Agent handles troubleshooting and problems

**Agent Handoffs**:
- Complex questions route to multiple agents
- Agents coordinate on overlapping concerns
- Clear boundaries prevent agent conflicts
- User controls which agent(s) to engage

**Context Sharing**:
- All agents share foundation context (CLAUDE.md)
- Each agent has specialized context subset
- Context updates propagate to relevant agents
- Agent feedback improves context quality

## Agent Testing & Validation

### Agent Effectiveness Testing
**Domain Expert Testing**:
- Business rule interpretation accuracy
- Domain terminology usage correctness
- Requirements translation effectiveness
- User workflow understanding validation

**Technical Architect Testing**:
- Architecture recommendation appropriateness
- Technology choice reasoning quality
- Performance analysis accuracy
- Pattern suggestion relevance

**Code Review Agent Testing**:
- Standard enforcement consistency
- Quality issue detection accuracy
- Improvement suggestion usefulness
- Team convention adherence validation

### Agent Performance Metrics
**Specialization Effectiveness**: Does agent provide better responses in their domain vs generic Claude?
**Knowledge Accuracy**: Does agent understand project-specific concepts correctly?
**Boundary Respect**: Does agent stay within defined expertise areas?
**User Satisfaction**: Do users prefer specialized agent responses?
**Coordination Effectiveness**: Do agents work well together on complex issues?

## Usage Examples

### Agent System Design
```bash
/develop-agents design
# Analyzes project DNA and context architecture
# Proposes agent specializations and capabilities
# Defines agent boundaries and coordination protocols
# Gets user approval for agent system design
```

### Agent Creation & Development
```bash
/develop-agents create
# Creates specialized agent implementations
# Integrates agents with context system
# Sets up agent coordination protocols
# Implements agent testing framework
```

### Agent Deployment
```bash
/develop-agents deploy
# Deploys agents to .claude/agents/ directory
# Integrates agents with context system
# Sets up orchestration protocols
# Validates agent effectiveness
```

### Agent Performance Monitoring
```bash
/develop-agents monitor
# Tracks agent usage and effectiveness
# Identifies improvement opportunities
# Monitors agent coordination success
# Provides optimization recommendations
```

## Integration with Deep Discovery System

### Input from Context Generation
**Context-Informed Agent Design**:
- Domain context shapes Domain Expert capabilities
- Technical context informs Architect Agent expertise
- Workflow context defines Code Reviewer standards
- All context layers inform debugging knowledge

### Agent Specialization Based on Project DNA
**From Consultation Intelligence**:
- Business domain expertise → Domain Expert Agent knowledge
- Technical architecture choices → Architect Agent patterns
- Team workflow preferences → Code Reviewer standards
- Problem areas identified → Debugging Agent focus areas

## Session State Management

**Agent Development Tracking**:
- Agent creation progress in `.claude-architect/agent-state.json`
- Agent effectiveness metrics and feedback
- Agent coordination improvements over time
- User preference learning for agent interactions

**Evolution and Improvement**:
- Agents improve based on user feedback
- Agent knowledge expands with project evolution
- Agent coordination protocols refine over time
- Agent effectiveness measurements guide improvements

## User Control & Customization

**Agent Capability Review**:
- User reviews each agent's proposed capabilities
- Modifications to agent expertise areas
- Adjustments to agent boundaries and scope
- Custom agent types for unique project needs

**Agent Interaction Preferences**:
- Control which agents activate for different questions
- Preference settings for agent coordination patterns
- Custom workflows for agent collaboration
- Override capabilities for specific situations

## Success Metrics

**Agent System Effectiveness**:
- Specialized responses vs generic Claude (before/after testing)
- User satisfaction with agent-specific expertise
- Time savings from having specialized help
- Quality improvements in domain-specific guidance

**Agent Coordination Success**:
- Effective collaboration between agents
- Clear handoffs and boundary respect
- User satisfaction with multi-agent responses
- Reduced confusion and conflicting advice

---

**Remember**: Real agents have genuine specialization and measurable expertise. Every agent should provide demonstrably better responses in their domain than generic Claude assistance.