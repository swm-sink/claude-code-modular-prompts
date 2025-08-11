---
name: anti-pattern-audit
description: Find and fix common anti-patterns in your code
usage: "/anti-pattern-audit [--fix]"
tools: [Read, Glob, Grep, Edit]
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

## Scanning Process

1. **Use Grep and Glob** to search for common anti-patterns
2. **Read suspicious files** to confirm issues
3. **Categorize findings** by priority level
4. **Provide specific fixes** with file locations

If issues are found, I'll present them in priority order.
If no major issues exist, I'll note minor improvements.

## Fix Options

**Manual review**: See issues above
**Auto-fix** (with --fix): I'll apply safe fixes
**Detailed report**: Use `/analyze --depth deep`

After scanning, I'll provide a summary with specific counts and actionable next steps.