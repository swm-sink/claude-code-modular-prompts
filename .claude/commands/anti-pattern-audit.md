---
name: anti-pattern-audit
description: Find and fix anti-patterns in your codebase
usage: "/anti-pattern-audit [--severity critical|high|medium]"
allowed-tools: [Read, Glob, Grep, WebSearch]
---

# Anti-Pattern Audit

I'll scan your codebase for common anti-patterns and provide fixes.

## What I'll Check For

**Architecture Anti-Patterns:**
- God objects (classes doing too much)
- Circular dependencies
- Distributed monolith (fake microservices)
- Anemic domain models

**Performance Anti-Patterns:**
- N+1 queries
- Memory leaks
- Synchronous operations that should be async
- Missing database indexes

**Security Anti-Patterns:**
- Hardcoded secrets
- SQL injection vulnerabilities
- Missing input validation
- Exposed sensitive data

**Code Quality Anti-Patterns:**
- Copy-paste code duplication
- Dead code
- Long methods (>50 lines)
- Deep nesting (>4 levels)

## How I'll Find Them

1. Use `Grep` to search for problematic patterns
2. Use `Read` to analyze suspicious files
3. Use `WebSearch` to verify current best practices
4. Provide specific file locations and line numbers

## What You'll Get

- **Priority list** of issues (Critical → High → Medium)
- **Evidence** showing exactly where problems exist  
- **Fix recommendations** with code examples and effort estimates

Let me start scanning your codebase...