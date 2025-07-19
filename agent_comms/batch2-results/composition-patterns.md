# Command Composition Patterns

## Overview

Command composition transforms 8 essential commands into a powerful workflow orchestration system. Commands can be chained, run in parallel, and conditionally executed to create sophisticated development workflows.

## 🔗 Composition Operators

### Sequential Chaining (`|`)
Commands execute in order, with output flowing from one to the next.

```bash
# Research → Implement → Deploy pipeline
/analyze "payment system" | /feature "add stripe integration" | /deploy --staging

# Understand → Fix → Test workflow  
/analyze "slow queries" | /task "optimize database indexes" | /analyze --performance
```

### Parallel Execution (`&`)
Commands run simultaneously for maximum efficiency.

```bash
# Parallel refactoring across modules
/team "refactor auth" & /team "refactor API" & /team "refactor database"

# Analysis + Documentation in parallel
/analyze "system architecture" & /setup docs --architecture
```

### Conditional Execution (`&&`)
Next command only runs if previous succeeds.

```bash
# Deploy only if tests pass
/task "fix critical bug" && /deploy --hotfix

# Feature → Deploy pipeline with safety gates
/feature "payment processing" && /deploy --staging && /deploy --production
```

### Grouped Execution (`()`)
Group commands for complex workflows.

```bash
# Complete feature with parallel sub-tasks
/feature "user dashboard" && (/task "UI components" & /task "API endpoints" & /task "database schema")

# Multi-stage deployment
(/deploy --staging && /analyze --performance) && /deploy --production
```

## 📋 Common Composition Patterns

### 1. Research-Driven Development
**Pattern**: Understand before implementing
```bash
# Basic research → implement
/analyze "authentication flow" | /task "fix auth bug"

# Deep analysis → feature development
/analyze --deep "payment system" | /feature "add subscription billing"

# Performance optimization workflow
/analyze --performance "API endpoints" | /task "add caching layer" | /analyze --performance
```

### 2. Test-Driven Feature Development
**Pattern**: Progressive feature implementation with validation
```bash
# Feature with immediate testing
/feature "user registration" && /analyze --coverage

# Feature with staging validation
/feature "shopping cart" && /deploy --staging && /analyze --e2e

# Full TDD cycle
/task --tdd "payment validator" | /analyze --coverage | /task --refactor
```

### 3. Safe Production Deployment
**Pattern**: Multi-stage deployment with rollback capability
```bash
# Standard deployment pipeline
/analyze --risks | /deploy --staging && /analyze --smoke-test && /deploy --production

# Hotfix deployment
/task "critical fix" && /deploy --hotfix --with-rollback

# Canary deployment
/deploy --canary=10% && /analyze --metrics --wait=30m && /deploy --production
```

### 4. Parallel Development Coordination
**Pattern**: Distribute work across multiple agents
```bash
# Frontend/Backend parallel development
/team "frontend" --scope="UI components" & /team "backend" --scope="API endpoints"

# Microservices parallel update
/team "update services" --distribute="auth,payment,notification"

# Parallel testing
/team "test suite" --parallel="unit,integration,e2e"
```

### 5. Long-Running Session Management
**Pattern**: Extended work with checkpoints
```bash
# Feature development session
/session "major refactor" && /feature "new architecture" | /session --checkpoint

# Research session with documentation
/session "codebase analysis" && (/analyze "all modules" | /setup docs)

# Interrupted work resumption
/session --resume=abc123 | /task --continue
```

## 🎯 Advanced Composition Techniques

### Context Propagation
Commands share context automatically:

```bash
# Context flows through pipeline
/analyze "user service" | /task "refactor user service"
# The /task command knows we're working on user service

# Explicit context passing
/analyze "database" --export=db-analysis | /feature "optimize queries" --import=db-analysis
```

### Progressive Enhancement
Commands can enhance based on previous results:

```bash
# Adaptive complexity
/auto "improve performance" | /analyze --suggested | /task --comprehensive

# Risk-based deployment
/analyze --risk-assessment | /deploy --safety={risk_level}
```

### Failure Handling
Built-in error recovery and fallbacks:

```bash
# Fallback on failure
/deploy --production || /deploy --rollback

# Retry with backoff
/deploy --staging --retry=3 --backoff=exponential

# Alternative paths
/feature "oauth" || (/analyze "auth requirements" | /feature "basic auth")
```

### State Management
Commands can save and restore state:

```bash
# Save state for later
/analyze "architecture" --save-state=arch-v1

# Branch based on state
/analyze --load-state=arch-v1 | /feature "microservices migration"

# State-based conditionals
/analyze --check="test coverage > 80%" && /deploy --production
```

## 🔄 Workflow Templates

### Template 1: Complete Feature Lifecycle
```bash
# Research → Design → Implement → Test → Deploy
/analyze "{feature_area}" --comprehensive |
/feature "{feature_name}" --with-prd |
/analyze --coverage --security |
/deploy --staging &&
/analyze --e2e &&
/deploy --production
```

### Template 2: Bug Investigation & Fix
```bash
# Reproduce → Analyze → Fix → Verify
/analyze "{bug_description}" --reproduce |
/analyze --root-cause |
/task "fix {bug}" --comprehensive |
/analyze --verify-fix &&
/deploy --hotfix
```

### Template 3: Performance Optimization
```bash
# Profile → Identify → Optimize → Validate
/analyze --performance --baseline |
/analyze "bottlenecks" |
/team "optimize" --parallel=3 |
/analyze --performance --compare=baseline &&
/deploy --canary
```

### Template 4: Codebase Refactoring
```bash
# Analyze → Plan → Execute → Validate
/analyze "refactor targets" --technical-debt |
/session "refactoring" &&
/team "refactor" --distributed |
/analyze --regression-test &&
/setup docs --update
```

### Template 5: Security Audit & Fix
```bash
# Scan → Prioritize → Fix → Verify
/analyze --security --full-scan |
/analyze "vulnerabilities" --prioritize |
/team "security fixes" --by-priority |
/analyze --security --verify &&
/deploy --security-patch
```

## 🎮 Interactive Composition

### Dynamic Workflow Building
Commands can build workflows interactively:

```bash
# Interactive workflow builder
/auto --build-workflow "migrate to microservices"
# Returns: suggested workflow with customization options

# Workflow optimization
/auto --optimize-workflow "/analyze | /feature | /deploy"
# Returns: optimized version with parallelization
```

### Workflow Macros
Save and reuse common workflows:

```bash
# Save workflow
/setup workflow --save="feature-dev" "/analyze | /feature | /deploy --staging"

# Execute saved workflow
/setup workflow --run="feature-dev" --params="user authentication"

# List workflows
/setup workflow --list
```

## 📊 Composition Performance

### Optimization Strategies

1. **Parallel by Default**
   ```bash
   # Instead of sequential
   /analyze "module1" | /analyze "module2" | /analyze "module3"
   
   # Use parallel
   /analyze "module1" & /analyze "module2" & /analyze "module3"
   ```

2. **Early Termination**
   ```bash
   # Stop on first failure
   /task "risky change" && /analyze --verify && /deploy
   ```

3. **Resource Allocation**
   ```bash
   # Allocate resources appropriately
   /team "cpu-intensive" --resources=high & /task "simple-fix" --resources=low
   ```

4. **Smart Caching**
   ```bash
   # Cache analysis results
   /analyze "system" --cache=1h | /feature "optimization"
   ```

### Performance Metrics

```yaml
Sequential Pipeline:
  - 3 commands: ~15 seconds total
  - Overhead: <1 second between commands
  - Context transfer: <500ms

Parallel Execution:
  - 3 commands: ~5-7 seconds total (3x faster)
  - Resource usage: Managed by scheduler
  - Conflict resolution: Automatic

Complex Workflows:
  - 10+ commands: Intelligent scheduling
  - Optimization: Automatic parallelization
  - Progress tracking: Real-time updates
```

## 🛡️ Safety and Validation

### Composition Safety Rules

1. **Resource Limits**
   ```bash
   # Automatic resource limiting
   /team "intensive task" --agents=10  # Limited to available resources
   ```

2. **Deployment Gates**
   ```bash
   # Automatic safety checks
   /feature "critical" | /deploy  # Auto-adds staging validation
   ```

3. **Rollback Capability**
   ```bash
   # Every workflow is reversible
   /feature "risky" --with-rollback | /deploy --with-rollback
   ```

### Validation Patterns

```bash
# Pre-validation
/analyze --pre-check | /feature "complex change"

# Post-validation
/task "update API" | /analyze --integration-test

# Continuous validation
/session "long task" --validate-every=30m
```

## 🚀 Best Practices

### DO's
- ✅ Use parallel execution for independent tasks
- ✅ Add validation steps before deployments
- ✅ Save complex workflows as macros
- ✅ Use conditional execution for safety
- ✅ Let context flow naturally through pipelines

### DON'Ts
- ❌ Over-complicate simple tasks
- ❌ Skip validation in production workflows
- ❌ Create circular dependencies
- ❌ Ignore resource constraints
- ❌ Mix incompatible command contexts

### Examples of Good Composition

```bash
# Clear, purposeful, safe
/analyze "payment bugs" | /task "fix payment validation" && /deploy --staging

# Efficient parallel execution
/team "update services" --services="auth,user,payment" --parallel

# Progressive enhancement
/auto "improve search" | /implement --suggested
```

### Examples to Avoid

```bash
# Too complex for simple task
/analyze & /task & /feature & /deploy  # Just use /task

# Missing safety checks
/task "database migration" | /deploy --production  # Add staging!

# Circular workflow
/analyze --suggest | /auto  # Creates infinite loop
```

---
*Composition Patterns v1.0.0 | Generated: 2025-07-19*