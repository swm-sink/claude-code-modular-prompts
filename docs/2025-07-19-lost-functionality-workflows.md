# Practical Guide: Achieving Lost Command Functionality

| Date | Author | Version | Type |
|------|--------|---------|------|
| 2025-07-19 | Workflow Documentation | 1.0.0 | Guide |

## Overview

This guide shows how to achieve the functionality of removed commands using the current optimized framework. Each workflow demonstrates practical command combinations that replicate lost capabilities.

## 1. Deployment Workflows (Replacing /deploy)

### Production Deployment
```bash
# Step 1: Analyze deployment readiness
/query "check deployment readiness: test coverage, build status, dependencies"

# Step 2: Run deployment protocol
/protocol "production deployment with safety checks and rollback capability"

# Step 3: Verify deployment
/query "verify deployment health: endpoints, database, services"
```

### Rollback Procedure
```bash
# Emergency rollback workflow
/chain sequential --commands="/protocol rollback-production, /query verify-rollback-status, /docs update-incident-report"
```

### Blue-Green Deployment
```bash
# Complex deployment orchestration
/swarm "coordinate blue-green deployment:
- Agent 1: Prepare green environment
- Agent 2: Run smoke tests
- Agent 3: Switch traffic
- Agent 4: Monitor metrics"
```

## 2. Team Coordination (Replacing /team)

### Distribute Work Among Team
```bash
# Create work distribution plan
/feature "team task distribution system with:
- Task assignment by expertise
- Progress tracking
- Dependency management
- Communication channels"

# Or use swarm for immediate distribution
/swarm "distribute authentication feature:
- Frontend: Login UI components
- Backend: JWT implementation
- Database: User schema
- Testing: Integration tests"
```

### Team Synchronization
```bash
# Long-running team coordination
/session "team sync for sprint planning:
- Review completed tasks
- Identify blockers
- Assign new work
- Update timelines"
```

### Parallel Development
```bash
# Coordinate parallel work streams
/chain parallel --commands="
  /task implement-user-model,
  /task create-auth-middleware,
  /task design-login-ui"
```

## 3. Deep Analysis (Replacing /analyze)

### Performance Analysis
```bash
# Comprehensive performance audit
/context-prime-mega "analyze performance bottlenecks"

# Or targeted analysis
/query "identify performance issues in:
- Database queries
- API response times
- Memory usage patterns
- CPU hotspots"
```

### Architecture Assessment
```bash
# Multi-agent architecture review
/context-prime-mega "comprehensive architecture analysis with:
- Design pattern compliance
- SOLID principles
- Coupling metrics
- Complexity assessment"
```

### Code Quality Analysis
```bash
# Quality metrics assessment
/meta review "code quality metrics:
- Test coverage gaps
- Complexity scores
- Duplication analysis
- Security vulnerabilities"
```

## 4. Framework Setup (Replacing /setup)

### Initial Configuration
```bash
# Use specialized init commands
/init-custom "configure for React/TypeScript project with:
- ESLint rules
- Testing framework
- Build pipeline
- Git hooks"
```

### Performance Tuning
```bash
# Optimize framework performance
/meta optimize "framework performance:
- Token usage
- Response times
- Module loading
- Context efficiency"
```

### Settings Management
```bash
# Configure project settings
/init-validate "verify and update:
- PROJECT_CONFIG.xml
- Quality thresholds
- Tool commands
- Directory structure"
```

## 5. Code Enhancement (Replacing /enhance)

### Refactoring Workflow
```bash
# Systematic refactoring
/task "refactor UserService class:
- Extract interfaces
- Reduce complexity
- Improve naming
- Add documentation"
```

### Pattern Application
```bash
# Apply design patterns
/feature "implement Repository pattern for data access layer"
```

### Performance Enhancement
```bash
# Optimize specific code
/task "optimize database queries in ProductService:
- Add indexes
- Implement caching
- Batch operations
- Query optimization"
```

## 6. Advanced Workflows Using /chain

### Complete Feature Deployment
```bash
/chain "feature-to-production" --sequence="
  /feature 'user authentication system',
  /query 'security review',
  /protocol 'staging deployment',
  /query 'integration tests',
  /protocol 'production deployment',
  /docs 'update API documentation'"
```

### Codebase Modernization
```bash
/chain "modernize-codebase" --parallel="
  /meta review 'identify legacy patterns',
  /query 'list deprecated dependencies',
  /context-prime-mega 'analyze upgrade paths'" \
--then-sequence="
  /task 'update dependencies',
  /task 'refactor legacy code',
  /meta optimize 'performance improvements'"
```

### Incident Response
```bash
/chain "incident-response" --urgent --sequence="
  /query 'diagnose production issue',
  /protocol 'emergency hotfix',
  /task 'implement fix',
  /protocol 'deploy patch',
  /docs 'incident postmortem'"
```

## 7. Meta Command Extensions

The `/meta` command now provides advanced operations:

```bash
# Deep analysis (similar to /analyze)
/meta review "comprehensive codebase analysis with metrics"

# Performance optimization (similar to /enhance)
/meta optimize "identify and implement performance improvements"

# Framework evolution (similar to /setup)
/meta evolve "adapt framework to new project patterns"

# Governance (similar to deployment checks)
/meta govern "enforce production readiness standards"

# Diagnostics (similar to debugging)
/meta fix "diagnose and resolve framework issues"
```

## Best Practices

### 1. Use Command Composition
Instead of wishing for specialized commands, combine existing ones:
- `/query` + `/task` = Research and implement
- `/feature` + `/protocol` = Develop and deploy
- `/swarm` + `/session` = Coordinate and track

### 2. Leverage /chain for Complex Workflows
The `/chain` command is incredibly powerful for orchestrating multi-step processes that previously required specialized commands.

### 3. Utilize Multi-Agent Capabilities
`/swarm` and `/context-prime-mega` can handle complex analysis and coordination tasks that previously required separate commands.

### 4. Document Custom Workflows
Create your own workflow documentation for frequently used command combinations specific to your project.

## Conclusion

While some commands were removed during optimization, their functionality remains accessible through intelligent use of the remaining commands. The key is understanding how to compose and chain commands effectively.

The optimized framework encourages thinking in terms of:
- **Workflows** rather than individual commands
- **Composition** rather than specialization
- **Flexibility** rather than rigid structures

This approach ultimately provides more power with less complexity.