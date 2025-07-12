# Commands Reference - Complete Guide

> **Quick Reference**: See [Command Selection Guide](../user-guide/commands/command-selection.md) for choosing the right command.

This is the complete reference for all framework commands with detailed parameters, examples, and usage patterns.

## 🎯 Core Commands

### `/query` - Research and Analysis
**Purpose**: Analyze, investigate, and understand without making changes.

**Syntax**: `/query "description of what you want to understand"`

**Characteristics**:
- ✅ Read-only operation
- ✅ No file modifications
- ✅ Analysis and reporting
- ❌ Never creates or modifies files

**Examples**:
```bash
# Code analysis
/query "how does user authentication work in this project?"
/query "find all components that use React hooks"
/query "analyze database schema and relationships"

# Issue investigation
/query "identify potential security vulnerabilities"
/query "find performance bottlenecks in the API"
/query "analyze test coverage gaps"

# Pattern discovery
/query "show me all API endpoints and their purposes"
/query "find examples of error handling patterns"
/query "analyze code organization and architecture"
```

**Best Practices**:
- Always start with `/query` to understand before making changes
- Use for investigating bugs before fixing them
- Great for onboarding and understanding legacy code
- Perfect for code reviews and audits

---

### `/task` - Focused Development
**Purpose**: Implement specific, focused changes to individual components or files.

**Syntax**: `/task "specific description of what to implement"`

**Characteristics**:
- ✅ Focused scope (1-3 files typically)
- ✅ TDD enforcement (RED→GREEN→REFACTOR)
- ✅ Quality gates
- ✅ Specific, actionable changes

**Examples**:
```bash
# Bug fixes
/task "fix password validation error in UserForm.tsx"
/task "resolve memory leak in data processing function"
/task "correct timezone handling in DatePicker component"

# Small features
/task "add email validation to contact form"
/task "implement dark mode toggle in header"
/task "create utility function for currency formatting"

# Focused refactoring
/task "extract reusable logic from PaymentForm component"
/task "optimize slow search algorithm in utils/search.js"
/task "update deprecated API calls in user service"
```

**Quality Requirements**:
- Must follow TDD cycle (tests first)
- Must pass all quality gates
- Must include appropriate error handling
- Must maintain test coverage thresholds

**Best Practices**:
- Keep scope focused and specific
- Include the specific file/component name when known
- Describe the exact behavior you want
- Perfect for bug fixes and small enhancements

---

### `/feature` - Complete Feature Development
**Purpose**: Develop complete, user-facing features with PRD-driven approach.

**Syntax**: `/feature "user story or feature description"`

**Characteristics**:
- ✅ Multi-component scope
- ✅ PRD generation and MVP planning
- ✅ Complete user functionality
- ✅ Comprehensive testing
- ✅ Documentation included

**Examples**:
```bash
# User stories
/feature "user can reset password via email"
/feature "admin can manage user permissions"
/feature "customers can save items to wishlist"

# Complete features
/feature "shopping cart with persistent storage"
/feature "real-time chat between users"
/feature "advanced search with filters and sorting"

# Business capabilities
/feature "payment processing with multiple gateways"
/feature "notification system with email and SMS"
/feature "analytics dashboard for admin users"
```

**Development Process**:
1. **PRD Creation**: Generates Product Requirements Document
2. **MVP Planning**: Defines minimal viable product approach
3. **Implementation**: Multi-component development with TDD
4. **Testing**: Comprehensive test coverage
5. **Documentation**: User and technical documentation

**Best Practices**:
- Frame as user stories when possible
- Include business value and acceptance criteria
- Let framework generate PRD first
- Perfect for sprint-sized features

---

### `/auto` - Intelligent Routing
**Purpose**: Let framework analyze your request and route to the optimal command.

**Syntax**: `/auto "description of what you want to accomplish"`

**Characteristics**:
- ✅ Intelligent analysis and routing
- ✅ Adapts approach based on complexity
- ✅ Meta-prompting capabilities
- ✅ Self-improving decision making

**Examples**:
```bash
# Complex improvements
/auto "modernize our authentication system"
/auto "improve API performance and reliability"
/auto "add comprehensive error handling"

# Mixed analysis and implementation
/auto "analyze current security and fix issues"
/auto "review testing strategy and improve coverage"
/auto "optimize our build and deployment process"

# Uncertain scope
/auto "improve user experience in checkout flow"
/auto "make our application more accessible"
/auto "add monitoring and observability"
```

**Routing Behavior**:
- **Research needed** → Routes to `/query` first
- **Simple focused work** → Routes to `/task`
- **Complete features** → Routes to `/feature`
- **Complex coordination** → Routes to `/swarm`
- **Documentation creation** → Routes to `/docs`

**Best Practices**:
- Use when approach isn't clear
- Great for complex or multi-faceted requests
- Trust the framework's analysis and routing
- Perfect when you're unsure which command to use

---

### `/docs` - Documentation Management
**Purpose**: Create, update, and manage documentation files.

**Syntax**: 
- `/docs generate "type of documentation"`
- `/docs "update existing documentation"`
- `/docs search "topic" "search documentation"`
- `/docs validate "check documentation"`

**Characteristics**:
- ✅ Documentation creation and updates
- ✅ FOCUS framework integration
- ✅ Structured documentation generation
- ❌ Never use for code analysis

**Examples**:
```bash
# Generate new documentation
/docs generate "API Reference Guide"
/docs generate "Setup Guide for New Developers"
/docs generate "Architecture Decision Records"

# Update existing documentation
/docs "update README with new features"
/docs "refresh deployment documentation"
/docs "add examples to component library docs"

# Documentation maintenance
/docs validate "check all docs for completeness"
/docs search "authentication" "find docs needing updates"
```

**Documentation Types**:
- **API Reference**: Complete API documentation
- **User Guides**: How-to and tutorial content
- **Architecture Docs**: System design and decisions
- **Troubleshooting**: Problem-solving guides
- **Process Docs**: Development and deployment procedures

**Best Practices**:
- Only use for creating or updating documentation
- Never use for understanding existing code (use `/query`)
- Specify the type of documentation needed
- Include target audience when relevant

---

## ⚡ Specialized Commands

### `/swarm` - Complex System Coordination
**Purpose**: Coordinate complex, multi-component work with multi-agent patterns.

**Syntax**: `/swarm "large-scale change or complex coordination"`

**Characteristics**:
- ✅ Multi-agent coordination
- ✅ GitHub epic creation
- ✅ Parallel work streams
- ✅ Git worktree isolation
- ✅ Complex project management

**Examples**:
```bash
# Architecture changes
/swarm "migrate from REST API to GraphQL"
/swarm "refactor monolith to microservices"
/swarm "upgrade React 16 to React 18 across all components"

# Large-scale refactoring
/swarm "implement comprehensive TypeScript migration"
/swarm "replace Redux with Zustand state management"
/swarm "modernize CSS from styled-components to Tailwind"

# System-wide improvements
/swarm "implement end-to-end testing framework"
/swarm "add internationalization support"
/swarm "migrate to new deployment infrastructure"
```

**Coordination Features**:
- **Epic Creation**: GitHub epics for project tracking
- **Work Breakdown**: Automated task decomposition
- **Parallel Execution**: Coordinated multi-agent work
- **Progress Tracking**: Real-time coordination dashboard

**Best Practices**:
- Use for system-wide changes
- Perfect for architecture migrations
- Great for large refactoring projects
- Automatically manages project complexity

---

### `/session` - Long-term Project Tracking
**Purpose**: Manage complex, multi-session projects with GitHub integration.

**Syntax**: `/session "description of long-term project"`

**Characteristics**:
- ✅ Multi-session continuity
- ✅ GitHub issue tracking
- ✅ Context preservation
- ✅ Milestone management
- ✅ Progress tracking

**Examples**:
```bash
# Complex projects
/session "implement new user onboarding flow"
/session "migrate database to new provider"
/session "redesign mobile application UI"

# Milestone tracking
/session "prepare for Q2 product launch"
/session "complete security audit remediation"
/session "implement GDPR compliance features"
```

**Session Management**:
- **Context Preservation**: Maintains context across sessions
- **Issue Tracking**: Creates and updates GitHub issues
- **Progress Monitoring**: Tracks completion status
- **Milestone Integration**: Links to project milestones

**Best Practices**:
- Use for multi-day or multi-week projects
- Perfect for complex features requiring planning
- Great for coordinating multiple related tasks
- Automatically manages project context

---

### `/protocol` - Production Critical Operations
**Purpose**: Execute production-critical operations with maximum quality enforcement.

**Syntax**: `/protocol "critical operation description"`

**Characteristics**:
- ✅ Maximum quality enforcement
- ✅ All quality gates active
- ✅ Comprehensive validation
- ✅ Safety-first approach
- ✅ Audit trail creation

**Examples**:
```bash
# Production deployments
/protocol "deploy payment system update to production"
/protocol "release critical security patch"
/protocol "migrate production database"

# Critical fixes
/protocol "fix critical payment processing bug"
/protocol "resolve production API outage"
/protocol "implement emergency security fix"

# High-stakes changes
/protocol "update production infrastructure"
/protocol "deploy compliance-critical features"
/protocol "perform data migration for 1M+ users"
```

**Quality Enforcement**:
- **All Quality Gates**: Every quality check enforced
- **Comprehensive Testing**: Full test suite execution
- **Security Validation**: Complete security review
- **Performance Verification**: Performance impact assessment
- **Rollback Planning**: Automatic rollback procedures

**Best Practices**:
- Use for production-critical changes
- Perfect for security updates
- Essential for data migrations
- Automatically enforces maximum quality

---

## 🔧 Setup and Utility Commands

### `/init` - Framework Initialization
**Purpose**: Initialize framework for new or existing projects.

**Syntax**: `/init` (interactive setup)

**Variants**:
- `/init-new` - Interactive setup for new projects
- `/init-custom` - Auto-configure based on existing codebase
- `/init-research` - Research-driven configuration
- `/init-validate` - Comprehensive validation

**Best Practices**:
- Use during initial framework setup
- Choose variant based on project state
- Run validation after setup

---

### Meta-Commands (Framework Evolution)

**Purpose**: Framework self-improvement and optimization.

**Commands**:
- `/meta-review` - Framework audit and analysis
- `/meta-evolve` - Intelligent framework evolution  
- `/meta-optimize` - Performance and workflow optimization
- `/meta-govern` - Governance and compliance
- `/meta-fix` - Self-correction and issue resolution

**Examples**:
```bash
# Framework optimization
/meta-review "analyze framework performance on this project"
/meta-optimize "improve command response times"
/meta-evolve "adapt to our team's coding patterns"
```

**Best Practices**:
- Use periodically for framework optimization
- Perfect for adapting framework to team patterns
- Great for performance tuning

---

## 📊 Command Comparison Matrix

| Aspect | `/query` | `/task` | `/feature` | `/auto` | `/docs` | `/swarm` | `/protocol` |
|--------|----------|---------|------------|---------|---------|----------|-------------|
| **File Changes** | ❌ | ✅ | ✅ | Varies | ✅ | ✅ | ✅ |
| **Scope** | Any | 1-3 files | Multi-component | Adaptive | Docs only | System-wide | Any |
| **Quality Gates** | N/A | Standard | Full | Adaptive | Standard | Full | Maximum |
| **TDD Required** | N/A | ✅ | ✅ | Varies | N/A | ✅ | ✅ |
| **GitHub Integration** | ❌ | ❌ | Optional | Varies | ❌ | ✅ | ✅ |
| **Documentation** | Analysis | Inline | Included | Varies | Primary | Included | Comprehensive |
| **Best For** | Research | Focused work | Features | Complex requests | Documentation | Large changes | Production |

## 🎯 Command Selection Guidelines

### By Purpose
- **Understanding** → `/query`
- **Focused changes** → `/task`  
- **Complete features** → `/feature`
- **Complex/uncertain** → `/auto`
- **Documentation** → `/docs`
- **Large coordination** → `/swarm`
- **Production critical** → `/protocol`

### By Scope
- **Single file** → `/task`
- **Multiple files** → `/feature`
- **System-wide** → `/swarm`
- **Multi-session** → `/session`
- **Read-only** → `/query`

### By Risk Level
- **Low risk** → `/task`
- **Medium risk** → `/feature`
- **High risk** → `/protocol`
- **Uncertain risk** → `/auto`

## ✅ Command Usage Validation

You're using commands correctly when:

- [ ] `/query` provides understanding without file changes
- [ ] `/task` makes focused changes with TDD
- [ ] `/feature` delivers complete user functionality
- [ ] `/auto` routes complex requests appropriately  
- [ ] `/docs` creates or updates documentation
- [ ] `/swarm` coordinates complex multi-component work
- [ ] `/protocol` enforces maximum quality for critical operations

---

**Need help choosing?** Use the [Command Selection Guide](../user-guide/commands/command-selection.md).

**Want to see examples?** Check [Common Workflows](../user-guide/workflows/common-patterns.md) for real usage patterns.