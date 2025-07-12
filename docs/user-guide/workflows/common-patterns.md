# Common Workflow Patterns

> **Goal**: Learn the most effective workflow patterns that will make you productive immediately.

These are the patterns that experienced framework users rely on daily.

## 🔄 The Research → Plan → Execute Pattern

### Basic Pattern
```bash
# 1. Research: Understand current state
/query "analyze the current user authentication system"

# 2. Plan: Determine approach
/auto "improve user authentication with modern practices"
# Framework analyzes and suggests approach

# 3. Execute: Implement with appropriate command
/feature "modernized authentication with OAuth and 2FA"
```

**When to use**: Any significant change or improvement.

### Advanced Pattern with Validation
```bash
# 1. Research: Deep understanding
/query "analyze authentication security vulnerabilities"
/query "review current authentication user experience"

# 2. Plan: Multiple approaches
/auto "create comprehensive authentication improvement plan"

# 3. Execute: Staged implementation
/task "implement OAuth integration"
/task "add two-factor authentication"
/task "improve password reset flow"

# 4. Validate: Ensure quality
/query "analyze new authentication implementation for issues"
/docs "update authentication documentation"
```

## 🐛 Bug Investigation and Resolution

### Simple Bug Fix
```bash
# 1. Understand the bug
/query "analyze the login form validation issue"

# 2. Fix it
/task "fix email validation in LoginForm.tsx"

# 3. Verify fix
/query "verify login form validation is working correctly"
```

### Complex Bug Investigation
```bash
# 1. Initial investigation
/query "analyze intermittent payment processing failures"

# 2. Deep dive research
/query "trace payment flow and identify failure points"
/query "analyze error logs and patterns"

# 3. Comprehensive fix
/auto "resolve payment processing reliability issues"

# 4. Post-fix analysis
/query "verify payment system stability"
/docs "update payment troubleshooting guide"
```

## 🚀 Feature Development Workflow

### Small Feature (Single Session)
```bash
# 1. Research requirements
/query "analyze existing shopping cart functionality"

# 2. Implement feature
/feature "add item quantity modification in cart"

# 3. Document changes
/docs "update shopping cart user guide"
```

### Large Feature (Multi-Session)
```bash
# Day 1: Planning and setup
/session "implement comprehensive user notification system"
/query "analyze current notification patterns"
/auto "create notification system architecture plan"

# Day 2-3: Core implementation
/feature "email notification service"
/feature "in-app notification UI"

# Day 4: Integration and testing
/task "integrate notification services"
/query "test notification system end-to-end"

# Day 5: Documentation and deployment
/docs generate "Notification System Guide"
/protocol "deploy notification system to production"
```

## 🏗️ Refactoring Workflows

### Component Refactoring
```bash
# 1. Analyze current state
/query "analyze UserProfile component for refactoring opportunities"

# 2. Plan refactoring
/auto "modernize UserProfile component architecture"

# 3. Execute refactoring
/task "extract reusable hooks from UserProfile"
/task "implement new UserProfile with modern patterns"
/task "update UserProfile tests"

# 4. Verify improvements
/query "compare old vs new UserProfile implementation"
```

### System-Wide Refactoring
```bash
# 1. Assessment
/query "analyze codebase for state management improvements"

# 2. Planning
/swarm "migrate from Redux to Zustand state management"

# 3. Execution (coordinated by swarm)
# Framework manages multiple parallel tasks

# 4. Validation
/query "analyze state management migration success"
/docs "update state management documentation"
```

## 📊 Code Quality Improvement

### Quality Assessment and Improvement
```bash
# 1. Comprehensive analysis
/query "analyze codebase for quality issues"
/query "review test coverage and identify gaps"
/query "find performance bottlenecks"

# 2. Prioritized improvements
/auto "create code quality improvement plan"

# 3. Systematic implementation
/task "fix high-priority linting issues"
/task "add tests for uncovered components"
/task "optimize identified performance bottlenecks"

# 4. Ongoing monitoring
/docs "update code quality standards"
/session "maintain code quality improvement tracking"
```

## 🔍 Investigation and Analysis Workflows

### Security Analysis
```bash
# 1. Security assessment
/query "analyze application for security vulnerabilities"
/query "review authentication and authorization patterns"
/query "check for common security anti-patterns"

# 2. Findings prioritization
/auto "create security improvement action plan"

# 3. Critical fixes
/protocol "implement high-priority security fixes"

# 4. Documentation
/docs generate "Security Best Practices Guide"
```

### Performance Analysis
```bash
# 1. Performance profiling
/query "analyze application performance bottlenecks"
/query "review database query efficiency"
/query "identify client-side performance issues"

# 2. Optimization planning
/auto "create performance optimization strategy"

# 3. Targeted improvements
/task "optimize slow database queries"
/task "implement component memoization"
/task "add lazy loading for large components"

# 4. Measurement
/query "measure performance improvements"
```

## 📚 Documentation Workflows

### Comprehensive Documentation Update
```bash
# 1. Audit current docs
/query "analyze documentation completeness"
/docs search "outdated" "find documentation needing updates"

# 2. Systematic updates
/docs "update API documentation"
/docs "refresh getting started guide"
/docs "update deployment instructions"

# 3. New documentation
/docs generate "Architecture Decision Records"
/docs generate "Troubleshooting Guide"

# 4. Validation
/docs validate "ensure documentation completeness"
```

## 🔄 Daily Development Workflows

### Morning Startup Routine
```bash
# 1. Catch up on changes
/query "what changed in the codebase since yesterday?"
/query "are there any failing tests or CI issues?"

# 2. Plan today's work
/session "continue work on user dashboard feature"
/query "review current progress and next steps"

# 3. Start development
# Use appropriate commands based on planned work
```

### End-of-Day Routine
```bash
# 1. Review accomplishments
/query "summarize changes made today"

# 2. Update documentation
/docs "update progress in feature documentation"

# 3. Plan tomorrow
/session "update project status and plan next steps"

# 4. Quality check
/query "verify all changes meet quality standards"
```

## 🎯 Project Milestone Workflows

### Sprint Planning
```bash
# 1. Sprint setup
/session "plan Q2 feature development sprint"

# 2. Work breakdown
/query "analyze sprint backlog and dependencies"
/auto "create implementation strategy for sprint goals"

# 3. Task creation
# Framework creates GitHub issues for tracking

# 4. Documentation
/docs "update sprint planning documentation"
```

### Release Preparation
```bash
# 1. Release readiness
/query "analyze codebase readiness for release"
/query "verify all features meet acceptance criteria"

# 2. Quality validation
/protocol "execute comprehensive release quality checks"

# 3. Documentation
/docs generate "Release Notes v2.1.0"
/docs "update deployment runbook"

# 4. Deployment
/protocol "deploy v2.1.0 to production"
```

## 🔧 Troubleshooting Workflows

### Development Environment Issues
```bash
# 1. Problem identification
/query "analyze development environment configuration"
/query "identify dependency and setup issues"

# 2. Resolution
/auto "fix development environment problems"

# 3. Documentation
/docs "update setup troubleshooting guide"
```

### Production Issue Response
```bash
# 1. Immediate assessment
/query "analyze production error logs and symptoms"

# 2. Emergency response
/protocol "implement critical production fix"

# 3. Root cause analysis
/query "conduct post-incident analysis"

# 4. Prevention
/task "implement monitoring to prevent recurrence"
/docs "update incident response procedures"
```

## 💡 Pro Tips for Workflow Efficiency

### 1. Always Start with Understanding
```bash
# Before any changes, understand the current state
/query "analyze current implementation"
# Then make informed decisions
```

### 2. Use `/auto` for Complex Decisions
```bash
# When approach isn't clear
/auto "improve our testing strategy"
# Framework will analyze and route optimally
```

### 3. Combine Commands for Complex Workflows
```bash
# Research phase
/query "understand current state"
# Planning phase  
/auto "determine best approach"
# Execution phase
/task "implement specific changes"
# Documentation phase
/docs "update relevant documentation"
```

### 4. Leverage Session Management
```bash
# For multi-day work
/session "implement complex feature X"
# Framework tracks progress across sessions
```

### 5. Use Appropriate Quality Gates
```bash
# For production-critical work
/protocol "deploy critical security fix"
# For regular development
/task "add new utility function"
```

## ✅ Workflow Success Indicators

You're using workflows effectively when:

- [ ] You consistently start with `/query` to understand
- [ ] You choose the right command for the task scope
- [ ] You combine commands for complex workflows
- [ ] You document changes appropriately
- [ ] You use session management for complex projects
- [ ] Your workflows produce predictable, quality results

## 🎯 Next Steps

### Master These Patterns First
1. **Research → Plan → Execute** - The foundation of all good development
2. **Bug Investigation** - Essential for maintaining code quality
3. **Feature Development** - Core development workflow

### Then Explore Advanced Patterns
- [Advanced Workflows](advanced-patterns.md) - Complex coordination patterns
- [Team Workflows](team-patterns.md) - Collaborative development patterns
- [Production Workflows](production-patterns.md) - Deployment and maintenance patterns

---

**Ready for more complex patterns?** Continue to [Advanced Workflows](advanced-patterns.md).

**Want to see team collaboration?** Check out [Team Patterns](team-patterns.md).