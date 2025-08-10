---
name: anti-pattern-audit
description: ML-powered anti-pattern detection with automated fix generation
usage: "/anti-pattern-audit [--depth surface|deep|exhaustive] [--fix-mode suggest|apply]"
allowed-tools: [Read, Glob, Grep, WebSearch, Task, Edit, Bash]
---

# Advanced Anti-Pattern Detection & Remediation

I'll use pattern recognition and parallel analysis to find and fix anti-patterns at scale.

## Phase 1: Multi-Dimensional Pattern Detection (8 Parallel Agents)

**Agent 1: Architectural Anti-Patterns**
- God objects (classes >500 lines, >20 methods)
- Circular dependencies (import cycle detection)
- Layering violations (cross-layer calls)
- Anemic domain models (data-only classes)
- Distributed monoliths (false microservices)

**Agent 2: Performance Anti-Patterns**
- N+1 query patterns in data access
- Synchronous operations in async contexts
- Memory leaks (unclosed resources, event listeners)
- Inefficient algorithms (O(n²) where O(n) possible)
- Missing database indexes on JOIN/WHERE columns

**Agent 3: Security Anti-Patterns**
- Hardcoded secrets/API keys/passwords
- SQL injection vulnerabilities
- XSS attack vectors
- Insecure deserialization
- Missing authentication/authorization

**Agent 4: Code Smell Detection**
- Long methods (>50 lines)
- Deep nesting (>4 levels)
- Code duplication (>10 line similarities)
- Dead code (unreachable/unused)
- Feature envy (methods using other class data)

**Agent 5: Testing Anti-Patterns**
- Missing tests for critical paths
- Test interdependencies
- Slow tests (>1s per unit test)
- Flaky tests (non-deterministic)
- Poor test coverage (<80% for critical code)

**Agent 6: Concurrency Anti-Patterns**
- Race conditions
- Deadlock potential
- Thread-unsafe singletons
- Missing synchronization
- Busy waiting loops

**Agent 7: API Design Anti-Patterns**
- Breaking changes without versioning
- Inconsistent naming conventions
- Missing error handling
- Chatty interfaces (multiple calls needed)
- Missing pagination for lists

**Agent 8: Modern Best Practices Violations**
- WebSearch latest standards for your tech stack
- Check OWASP Top 10 compliance
- Verify accessibility standards
- Check for deprecated API usage
- Identify outdated patterns

## Phase 2: Pattern Correlation & Risk Scoring

**Machine Learning-Inspired Scoring:**
```
Risk Score = Σ(severity × frequency × impact × exposure)

Where:
- Severity: How bad is the anti-pattern (1-10)
- Frequency: How often it appears (count)
- Impact: Business/performance impact (1-10)
- Exposure: Attack surface or user-facing (0-1)
```

**Pattern Clustering:**
- Group related anti-patterns
- Identify systemic issues
- Find root architectural problems
- Detect team knowledge gaps

## Phase 3: Automated Fix Generation

**Fix Strategy Selection:**

**Level 1: Safe Automated Fixes**
- Remove dead code
- Add missing null checks
- Fix obvious typos
- Update deprecated APIs

**Level 2: Guided Refactoring**
- Extract long methods
- Introduce design patterns
- Add abstraction layers
- Implement dependency injection

**Level 3: Architectural Remediation**
- Break circular dependencies
- Introduce async patterns
- Implement caching layers
- Add security middleware

## Phase 4: Fix Validation & Testing

**Automated Verification:**
```bash
# Before applying fixes:
# 1. Create git branch
# 2. Run existing tests
# 3. Apply fixes incrementally
# 4. Run tests after each fix
# 5. Measure performance impact
```

## Phase 5: Continuous Improvement

**Learning from Patterns:**
- Create custom rules for your codebase
- Generate team-specific lint rules
- Build architectural fitness functions
- Create pre-commit hooks

## Output Report Structure

```markdown
# Critical Issues (Fix immediately)
[Issues that could cause data loss, security breaches, or downtime]

# High Priority (This sprint)
[Performance problems, user-facing bugs]

# Medium Priority (This quarter)
[Code quality, maintainability issues]

# Technical Debt Registry
[Long-term improvements, refactoring opportunities]

# Recommended Process Changes
[Team practices, tooling, education needs]
```

Initiating comprehensive anti-pattern detection...