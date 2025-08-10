---
name: anti-pattern-audit
description: Find and fix common anti-patterns in your code
usage: "/anti-pattern-audit [--fix]"
allowed-tools: [Read, Glob, Grep, Edit]
---

# Anti-Pattern Audit

I'll scan for common issues and suggest fixes.

## Quick Scan

Checking for anti-patterns...

### Code Issues
- **Long functions**: > 50 lines
- **Deep nesting**: > 4 levels  
- **Code duplication**: Similar blocks
- **Dead code**: Unused functions
- **Complex conditions**: Hard to read

### Architecture Issues
- **God objects**: Classes doing too much
- **Circular dependencies**: A→B→A
- **Missing abstractions**: Repeated patterns
- **Tight coupling**: Hard dependencies

### Security Issues
- **Hardcoded secrets**: API keys, passwords
- **SQL injection**: Unescaped queries
- **Missing validation**: User input

## Found Issues

<if-issues-found>
### Priority 1: Critical
- [Issue]: [file:line]
  **Fix**: [suggested solution]

### Priority 2: Important
- [Issue]: [file:line]
  **Fix**: [suggested solution]

### Priority 3: Nice to fix
- [Issue]: [file:line]
  **Fix**: [suggested solution]
</if-issues-found>

<if-no-issues>
✅ No major anti-patterns detected!

Minor suggestions:
- [Improvement opportunity]
- [Code style suggestion]
</if-no-issues>

## Fix Options

**Manual review**: See issues above
**Auto-fix** (with --fix): I'll apply safe fixes
**Detailed report**: Use `/analyze --depth deep`

## Summary
- **Critical issues**: [count]
- **Total issues**: [count]
- **Files affected**: [count]

*Next steps*: Fix critical issues first, then run tests.