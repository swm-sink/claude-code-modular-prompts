---
name: list-agents
description: View available specialized agents and their capabilities with performance metrics
usage: "list-agents [--category=all|core|specialized] [--status=all|active|inactive] [--format=table|detailed|json]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS]
category: agents
argument-hint: "[--category] [--status] [--format]"
version: "1.0"
---

# List Agents: View Your Specialized Agent Team

## Purpose: Comprehensive Agent Discovery and Status Dashboard

The `/list-agents` command provides a complete overview of your specialized agent team, showing their capabilities, performance metrics, current status, and integration points. This serves as your agent management dashboard for understanding and monitoring your project-specific AI assistance team.

**Agent Discovery Philosophy**: Clear visibility into agent capabilities, transparent performance metrics, actionable status information, intelligent agent selection guidance.

## 🎯 Agent Dashboard Features

### Comprehensive Agent Visibility
- **Agent Capabilities**: Detailed view of each agent's specialized knowledge and abilities
- **Performance Metrics**: Real-time success rates, response quality, and effectiveness scores
- **Status Monitoring**: Current activation state, recent activity, and health indicators
- **Integration Mapping**: How agents connect with your project context and workflows

### Smart Filtering and Organization
- **Category Filtering**: View by agent type (core coordination vs specialized function)
- **Status Filtering**: Focus on active, inactive, or all agents
- **Performance Sorting**: Order by success rate, usage frequency, or effectiveness
- **Custom Views**: Table, detailed, or JSON formats for different use cases

## 🤖 Agent Categories and Specializations

### Core Coordination Agents (4 agents)
These agents orchestrate and coordinate the consultation and development workflow:

**🏗️ Architecture Agent** - *System Design & Patterns Specialist*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Analyzes system architecture and design patterns
  ✓ Guides technical decisions and trade-offs
  ✓ Validates architectural principles compliance
  ✓ Reviews system scalability and performance implications
Context Focus: Technical architecture, framework patterns, performance requirements
Recent Activity: [Last used | Usage frequency | Success rate]
```

**⚙️ Code Generation Agent** - *Project-Specific Code Creation*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Generates code following project-specific conventions
  ✓ Maintains consistency with existing codebase patterns
  ✓ Creates components using established architectural patterns
  ✓ Applies team coding standards and best practices
Context Focus: Code patterns, naming conventions, project structure
Recent Activity: [Last used | Code generated | Quality score]
```

**🧪 Testing Agent** - *TDD Enforcement & Quality Assurance*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Enforces test-driven development with code deletion penalty
  ✓ Creates comprehensive test suites for project features
  ✓ Validates test coverage against project standards
  ✓ Maintains testing framework consistency
Context Focus: Testing strategies, coverage requirements, quality gates
Recent Activity: [Tests created | TDD compliance rate | Coverage achieved]
```

**🔍 Debugging Agent** - *Project-Aware Problem Diagnosis*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Diagnoses issues using project-specific error patterns
  ✓ Provides debugging strategies for your architecture
  ✓ Suggests fixes based on project history and patterns
  ✓ Guides troubleshooting using your monitoring and logging
Context Focus: Error patterns, debugging procedures, failure modes
Recent Activity: [Issues resolved | Debug sessions | Fix success rate]
```

### Specialized Function Agents (10 agents)
These agents handle specific domains and technical areas:

**📝 Documentation Agent** - *Technical Writing & Knowledge Management*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Creates documentation following project style guides
  ✓ Maintains consistency with existing documentation patterns
  ✓ Writes API docs, code comments, and technical guides
  ✓ Updates documentation as project evolves
Context Focus: Documentation standards, audience needs, information architecture
Recent Activity: [Docs created | Updates made | Reader satisfaction]
```

**👥 Review Agent** - *Code Review & Standards Enforcement*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Applies team-specific code review standards and checklists
  ✓ Validates adherence to definition of done criteria
  ✓ Reviews against architectural principles and quality gates
  ✓ Ensures consistency with development workflow
Context Focus: Review standards, quality criteria, team conventions
Recent Activity: [Reviews completed | Issues found | Standards compliance]
```

**⚡ Performance Agent** - *Optimization & Scalability Specialist*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Analyzes performance against project-specific metrics
  ✓ Identifies optimization opportunities and bottlenecks
  ✓ Validates improvements against benchmark standards
  ✓ Guides scaling decisions based on usage patterns
Context Focus: Performance requirements, optimization patterns, scaling constraints
Recent Activity: [Optimizations applied | Performance gains | Bottlenecks resolved]
```

**🛡️ Security Agent** - *Vulnerability Detection & Compliance*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Scans for vulnerabilities relevant to your technology stack
  ✓ Applies industry-specific compliance requirements
  ✓ Validates security implementations against threat models
  ✓ Reviews authentication and authorization patterns
Context Focus: Security standards, compliance requirements, threat landscape
Recent Activity: [Scans completed | Vulnerabilities found | Fixes implemented]
```

**🔗 Integration Agent** - *External Systems & API Specialist*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Manages API integrations and external service connections
  ✓ Handles authentication and authorization patterns
  ✓ Implements error handling and retry strategies
  ✓ Validates data flow and integration patterns
Context Focus: API patterns, integration strategies, data flow requirements
Recent Activity: [Integrations managed | API calls handled | Error rates]
```

**🏢 Domain Expert Agent** - *Business Logic & Rules Specialist*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Understands business domain terminology and concepts
  ✓ Implements business rules and domain logic correctly
  ✓ Validates requirements against domain models
  ✓ Guides domain-driven design decisions
Context Focus: Business domain, terminology, rules, domain models
Recent Activity: [Rules implemented | Domain validations | Requirements met]
```

**♻️ Refactoring Agent** - *Technical Debt & Code Improvement*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Identifies technical debt and improvement opportunities
  ✓ Plans refactoring strategies within project constraints
  ✓ Maintains architectural principles during improvements
  ✓ Coordinates refactoring with release schedules
Context Focus: Code quality, technical debt, refactoring priorities
Recent Activity: [Refactoring tasks | Code improvements | Debt reduction]
```

**🔄 Migration Agent** - *Framework Transitions & Upgrades*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Guides framework upgrades and technology migrations
  ✓ Plans migration strategies that minimize disruption
  ✓ Handles data migrations and schema changes
  ✓ Validates migration completeness and rollback procedures
Context Focus: Migration strategies, compatibility requirements, rollback procedures
Recent Activity: [Migrations planned | Upgrades completed | Rollbacks needed]
```

**🚀 DevOps Agent** - *CI/CD & Deployment Specialist*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Manages CI/CD pipeline optimization and troubleshooting
  ✓ Guides deployment strategies and release procedures
  ✓ Monitors infrastructure and application performance
  ✓ Handles scaling and capacity planning decisions
Context Focus: CI/CD processes, deployment patterns, infrastructure requirements
Recent Activity: [Deployments managed | Pipeline optimizations | Monitoring alerts]
```

**📊 Data Agent** - *Database & Analytics Specialist*
```
Status: [Active/Inactive]     Performance Score: XX/100
Capabilities:
  ✓ Optimizes database queries and data access patterns
  ✓ Manages data pipelines and analytics workflows
  ✓ Implements data governance and privacy requirements
  ✓ Validates data integrity and consistency
Context Focus: Data models, query optimization, analytics requirements
Recent Activity: [Queries optimized | Data pipelines managed | Governance validations]
```

## 📊 Performance Metrics Dashboard

### Agent Performance Indicators
For each agent, view comprehensive performance data:

**📈 Success Metrics**
- **Response Accuracy**: Percentage of correct and helpful responses (target: >95%)
- **Context Relevance**: How well responses match project context (target: >90%)
- **Specialization Compliance**: Agent stays within defined boundaries (target: 100%)
- **User Satisfaction**: Approval ratings for agent contributions (target: >4.5/5)

**⚡ Efficiency Metrics**
- **Response Time**: Average time to provide useful guidance (target: <2 seconds)
- **Task Completion**: Percentage of tasks completed successfully (target: >90%)
- **Integration Success**: Effective handoffs with other agents (target: >90%)
- **Knowledge Currency**: How up-to-date agent knowledge remains (target: <7 days old)

**🎯 Usage Analytics**
- **Activation Frequency**: How often agent is used per week/month
- **Task Distribution**: Types of tasks most commonly handled
- **Peak Usage Times**: When agent is most active
- **Collaboration Patterns**: Which other agents this agent works with most

## 🔄 Agent Status Management

### Status Categories
**🟢 Active**: Agent is enabled and ready for use
- Fully integrated with project context
- Performance metrics within acceptable ranges
- Recent usage shows effective contribution

**🟡 Inactive**: Agent is available but not currently enabled
- May need activation via `/activate-agent` command
- Context may need refresh via `/update-agents`
- Performance history available for review

**🔴 Needs Attention**: Agent requires maintenance or updates
- Performance below acceptable thresholds
- Context knowledge may be outdated
- Integration issues detected

**⚪ Not Created**: Agent type available but not yet generated
- Can be created via `/create-agents` command
- Would benefit from current project context
- Recommended based on project analysis

## 🎯 Smart Agent Recommendations

### Context-Aware Suggestions
Based on your project analysis and recent activity patterns:

**🔧 Recommended for Activation**
- Agents that would benefit your current development focus
- Agents with high success rates in similar projects
- Agents that complement your currently active agent team

**📈 Performance Optimization Opportunities**
- Agents showing declining performance that could benefit from updates
- Agents with unused capabilities that could provide more value
- Agent combinations that could improve overall workflow efficiency

**🆕 Missing Capabilities**
- Agent types not yet created that could address current project needs
- Specialized agents that could fill gaps in your current team coverage
- Emerging needs based on project evolution and growth patterns

## ⚡ Usage Examples

### View All Agents with Performance Data
```bash
/list-agents --format=detailed
```

### Focus on Active Agents Only
```bash
/list-agents --status=active --format=table
```

### View Core Coordination Agents
```bash
/list-agents --category=core --format=detailed
```

### Export Agent Data for Analysis
```bash
/list-agents --format=json > my-agent-team.json
```

### View Agents Needing Attention
```bash
/list-agents --status=needs-attention --format=detailed
```

## 🔗 Integration with Agent Workflow

### Seamless Command Integration
The agent list integrates with other agent management commands:
- **Click to Activate**: Direct links to `/activate-agent` for inactive agents
- **Performance Details**: Links to `/test-agents` for detailed performance analysis
- **Update Triggers**: Notifications when `/update-agents` would improve performance
- **Coordination Setup**: Links to `/coordinate-agents` for multi-agent workflows

### Real-Time Updates
- Agent status updates in real-time as you use other commands
- Performance metrics refresh after each agent interaction
- Notifications when agents need attention or updates
- Integration with consultation workflow state

## 🚀 Success Criteria

**Dashboard Clarity**: Complete visibility into your agent team's capabilities and performance
**Decision Support**: Clear information to guide agent activation and workflow decisions
**Performance Transparency**: Honest metrics showing agent effectiveness and areas for improvement
**Workflow Integration**: Seamless connection to other agent management and usage commands

**🎯 Final Result**: A comprehensive, real-time view of your specialized agent team with actionable insights for optimizing your project-specific AI assistance capabilities.