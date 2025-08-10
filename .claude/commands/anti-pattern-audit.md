---
name: anti-pattern-audit
description: Find and fix anti-patterns in your codebase
usage: "/anti-pattern-audit [--severity critical|high|medium]"
allowed-tools: [Read, Glob, Grep, WebSearch]
---

# Anti-Pattern Audit

I'll scan for critical issues and provide actionable fixes.

## Scan Coverage

**Architecture**: God objects, circular deps, fake microservices
**Performance**: N+1 queries, memory leaks, sync bottlenecks  
**Security**: Hardcoded secrets, SQL injection, missing validation
**Quality**: Duplication, dead code, long methods (>50 lines)

## Process

1. Grep problematic patterns
2. Read suspicious files
3. WebSearch best practices
4. Generate fix recommendations

## Output

Prioritized report with:
- Issue location (file:line)
- Severity rating
- Fix with code example
- Effort estimate

Scanning your codebase now...