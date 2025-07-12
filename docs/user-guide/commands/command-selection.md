# Command Selection Guide - Choose the Right Tool

> **TL;DR**: Not sure which command? Use `/auto` - it analyzes your request and routes intelligently.

## 🎯 Quick Decision Tree

```
Do you want to CREATE/UPDATE documentation?
├─ YES → /docs
└─ NO → Do you want to UNDERSTAND without changes?
    ├─ YES → /query  
    └─ NO → Do you know exactly what to implement?
        ├─ YES (single component/file) → /task
        ├─ YES (multiple components) → /feature
        ├─ COMPLEX/UNCERTAIN → /auto
        └─ PRODUCTION CRITICAL → /protocol
```

## 📊 Complete Command Matrix

| Command | Purpose | Scope | Creates Files | Modifies Code | Best For |
|---------|---------|-------|---------------|---------------|----------|
| `/query` | Research & Analysis | Any | ❌ | ❌ | Understanding, investigating, finding |
| `/task` | Focused Development | Single component | ✅ | ✅ | Bug fixes, small features, focused work |
| `/feature` | Complete Features | Multi-component | ✅ | ✅ | New features, user stories, PRD-driven work |
| `/auto` | Intelligent Routing | Adaptive | Depends | Depends | Complex requests, uncertain approach |
| `/docs` | Documentation | Documentation | ✅ | ❌ | Creating guides, references, updating docs |
| `/swarm` | Complex Coordination | System-wide | ✅ | ✅ | Large refactors, architecture changes |
| `/session` | Long-term Tracking | Multi-session | ✅ | ✅ | Complex projects, milestone tracking |
| `/protocol` | Production Critical | Any | ✅ | ✅ | Production deployments, critical fixes |

## 🔍 Detailed Command Breakdown

### `/query` - Read-Only Research
**Perfect for**: Understanding, analyzing, investigating

```bash
# Code investigation
/query "how does user authentication work?"
/query "find all components using React hooks"
/query "analyze database performance bottlenecks"

# Issue discovery
/query "identify potential security vulnerabilities"
/query "find unused imports and dead code"
/query "analyze test coverage gaps"

# Pattern analysis
/query "show me all API endpoints and their purposes"
/query "explain the state management architecture"
/query "find examples of error handling patterns"
```

**Never creates or modifies files** - pure analysis and reporting.

### `/task` - Focused Implementation
**Perfect for**: Single-file changes, specific bugs, focused features

```bash
# Bug fixes
/task "fix validation error in ContactForm.tsx"
/task "resolve memory leak in data processing function"
/task "correct timezone handling in DatePicker"

# Small features
/task "add password strength indicator to registration"
/task "implement dark mode toggle in header"
/task "create utility function for currency formatting"

# Focused refactoring
/task "extract reusable logic from PaymentForm component"
/task "optimize slow search algorithm in utils/search.js"
/task "update deprecated API calls in user service"
```

**Scope**: Usually 1-3 files, focused on specific functionality.

### `/feature` - Complete Feature Development
**Perfect for**: User stories, complete features, multi-component work

```bash
# User stories
/feature "user can reset password via email"
/feature "admin can manage user permissions"
/feature "customers can save items to wishlist"

# Complete features
/feature "shopping cart with persistent storage"
/feature "real-time chat between users"
/feature "advanced search with filters"

# Business capabilities
/feature "payment processing with multiple gateways"
/feature "notification system with email and SMS"
/feature "analytics dashboard for admin users"
```

**Scope**: Multiple files, complete user-facing functionality, includes tests and documentation.

### `/auto` - Intelligent Decision Making
**Perfect for**: Complex requests, uncertain approach, mixed research and implementation

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
/auto "make our app more accessible"
/auto "add monitoring and observability"
```

**Smart routing**: Framework analyzes request and routes to optimal command(s).

### `/docs` - Documentation Management
**Perfect for**: Creating guides, updating documentation, maintaining docs

```bash
# New documentation
/docs generate "API Reference Guide"
/docs generate "Setup Guide for New Developers"
/docs generate "Architecture Decision Records"

# Updates
/docs "update README with new features"
/docs "refresh deployment documentation"
/docs "add examples to component library docs"

# Maintenance
/docs validate "check all docs for completeness"
/docs search "authentication" "find docs needing updates"
```

**Documentation only**: Never use for code analysis (use `/query` instead).

### `/swarm` - Complex System Coordination
**Perfect for**: Large refactors, architecture changes, system-wide modifications

```bash
# Architecture changes
/swarm "migrate from REST to GraphQL"
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

**Multi-agent coordination**: Creates GitHub epics, coordinates multiple work streams.

### `/session` - Long-term Project Tracking
**Perfect for**: Multi-day projects, milestone tracking, complex coordination

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

**GitHub integration**: Creates issues, tracks progress, manages context across sessions.

### `/protocol` - Production Critical Work
**Perfect for**: Production deployments, critical fixes, high-stakes changes

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

**Maximum quality enforcement**: All quality gates, extensive testing, careful validation.

## 🤔 Common Decision Scenarios

### "I want to understand how X works"
```bash
# Always use /query for understanding
/query "how does user authentication work?"
/query "explain the payment processing flow"
/query "analyze the database design"
```

### "I need to fix a bug"
```bash
# Single component bug → /task
/task "fix validation error in LoginForm"

# Complex or unclear bug → /auto
/auto "fix the intermittent payment failures"

# Production critical bug → /protocol
/protocol "fix critical security vulnerability in auth"
```

### "I want to add a feature"
```bash
# Small, focused feature → /task
/task "add password strength indicator"

# Complete user-facing feature → /feature
/feature "shopping cart functionality"

# Complex or architectural feature → /auto
/auto "add real-time capabilities to our app"

# Production deployment → /protocol
/protocol "deploy new payment gateway integration"
```

### "I need documentation"
```bash
# Always use /docs for documentation
/docs generate "API Usage Guide"
/docs "update installation instructions"

# Never use /query for doc creation
# ❌ /query "create setup guide"  # This won't create files
# ✅ /docs generate "Setup Guide" # This creates documentation
```

### "I'm not sure what approach to take"
```bash
# Always use /auto when uncertain
/auto "improve our testing strategy"
/auto "make our app more performant"
/auto "modernize our tech stack"

# Framework will analyze and route appropriately
```

## 🎯 Command Selection Best Practices

### 1. Start with Understanding
```bash
# Before making changes, understand current state
/query "analyze current authentication implementation"
# Then make informed changes
/task "add two-factor authentication"
```

### 2. Match Scope to Command
```bash
# Single file changes
/task "fix bug in UserProfile.tsx"

# Multiple related files
/feature "user profile management"

# System-wide changes
/swarm "migrate to new authentication provider"
```

### 3. Use `/auto` for Complex Decisions
```bash
# Instead of guessing
/auto "improve our API performance"
# Framework analyzes and chooses optimal approach
```

### 4. Documentation vs Research
```bash
# Creating documentation
/docs generate "Architecture Guide"

# Understanding existing code
/query "explain our current architecture"
```

## 🚧 Common Mistakes to Avoid

### ❌ Wrong Command for Purpose
```bash
# Wrong: Using /docs for research
/docs "how does authentication work?"
# Right: Use /query for understanding
/query "how does authentication work?"

# Wrong: Using /query for creating docs
/query "create API documentation"
# Right: Use /docs for documentation
/docs generate "API Documentation"
```

### ❌ Scope Mismatch
```bash
# Wrong: Too complex for /task
/task "rebuild the entire user management system"
# Right: Use /feature or /swarm
/feature "comprehensive user management"

# Wrong: Too simple for /swarm
/swarm "fix typo in button text"
# Right: Use /task for simple fixes
/task "fix typo in submit button"
```

### ❌ Skipping Understanding Phase
```bash
# Wrong: Making changes without understanding
/task "fix the performance issue"
# Right: Understand first, then fix
/query "analyze performance bottlenecks"
/task "optimize identified slow database queries"
```

## 🎮 Interactive Command Selector

Answer these questions to find the right command:

1. **Do you want to create or update documentation?**
   - Yes → `/docs`
   - No → Continue to question 2

2. **Do you want to understand or analyze without making changes?**
   - Yes → `/query`
   - No → Continue to question 3

3. **Do you know exactly what needs to be implemented?**
   - Yes, single component/file → `/task`
   - Yes, multiple components → `/feature`
   - No, or it's complex → `/auto`
   - Production critical → `/protocol`

4. **Is this a large, system-wide change?**
   - Yes → `/swarm`
   - Multi-day project → `/session`

## ✅ Success Indicators

You're choosing commands correctly when:

- [ ] `/query` gives you understanding without creating files
- [ ] `/task` makes focused changes to 1-3 files
- [ ] `/feature` delivers complete user-facing functionality
- [ ] `/auto` routes complex requests appropriately
- [ ] `/docs` creates or updates documentation files
- [ ] You get the scope and type of result you expected

---

**Master command selection?** Move on to [Command Basics](basics.md) for detailed usage patterns.

**Want real examples?** Check [Common Workflows](../workflows/common-patterns.md) for practical scenarios.