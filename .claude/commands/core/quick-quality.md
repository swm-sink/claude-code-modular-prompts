---
name: /quick-quality
description: "Instant code quality analysis - works with any programming language"
usage: /quick-quality [--scan | --fix | --report] [file-pattern]
category: core
tools: Read, Edit, Bash, Grep, Glob
---

# 🎯 Instant Code Quality Analysis

**Universal code quality checker - works immediately with any language or framework!**

## Quick Quality Checks

### Full Project Scan
```
/quick-quality --scan
/quick-quality --scan src/
```

### Fix Quality Issues
```
/quick-quality --fix src/components/
/quick-quality --fix "fix all ESLint errors"
```

### Quality Report
```
/quick-quality --report
/quick-quality --report --detailed
```

## What Gets Analyzed

**🔍 Code Quality Metrics:**
- Code complexity and readability
- Security vulnerabilities
- Performance anti-patterns
- Error handling completeness
- Code duplication
- Naming conventions

**📊 Best Practice Checks:**
- Language-specific conventions
- Framework best practices
- Architecture patterns
- Testing completeness
- Documentation quality

## Universal Language Support

**Automatically detects and analyzes:**

**Frontend**: JavaScript, TypeScript, React, Vue, Angular, HTML, CSS
**Backend**: Python, Java, Go, Rust, C#, PHP, Ruby, Node.js
**Mobile**: Swift, Kotlin, React Native, Flutter/Dart
**Data**: SQL, R, Jupyter Notebooks, pandas
**Config**: Docker, YAML, JSON, XML

## Smart Analysis Features

**🧠 Context-Aware:**
- Understands your project structure
- Applies framework-specific rules
- Follows your existing patterns
- Considers project size and complexity

**⚡ Instant Results:**
- No configuration needed
- Works with any codebase immediately
- Prioritizes critical issues first
- Provides actionable fixes

## Example Quality Session

```
👤 /quick-quality --scan src/

🤖 Scanning codebase for quality issues...
🤖 Found 12 issues across 8 files:

🔴 HIGH PRIORITY (3 issues):
   • Potential SQL injection in users.py:42
   • Hardcoded credentials in config.js:15  
   • Memory leak in components/DataTable.jsx:89

🟡 MEDIUM PRIORITY (5 issues):
   • Complex function in auth.py:156 (45 lines)
   • Missing error handling in api/orders.js:78
   • Duplicate code in utils/format.js and helpers/format.js

🟢 LOW PRIORITY (4 issues):
   • Long variable name in models/user.py:23
   • TODO comment in dashboard.js:234

🤖 Want me to fix these? Run: /quick-quality --fix
```

## Automated Fixes

**I can automatically fix:**
- Code formatting and style
- Simple security issues
- Performance optimizations
- Remove code duplication
- Add missing error handling
- Improve variable naming

**I'll ask before:**
- Major architectural changes
- Potentially breaking modifications
- Complex refactoring operations

## Quality Report Formats

**Quick Summary**: Overview of issues and recommendations
**Detailed Report**: File-by-file analysis with code examples  
**Action Plan**: Prioritized fix suggestions with effort estimates
**Metrics Dashboard**: Complexity, coverage, and health scores

## Integration Ready

**Works with existing tools:**
- Runs alongside ESLint, Prettier, PyLint, etc.
- Complements your existing CI/CD quality gates
- Provides additional insights beyond standard linters
- Language-agnostic analysis across polyglot codebases

## When to Use Quality Commands

- **`/quick-quality`**: Immediate analysis, any project *(this command)*
- **`/quality`**: Enhanced checks after `/adapt-to-project`
- **`/quality-enforce`**: Automated quality gates (after customization)

## Start Your Quality Check

Choose your analysis type:

```
/quick-quality --scan                    # Analyze entire project
/quick-quality --scan src/               # Analyze specific directory
/quick-quality --fix                     # Fix identified issues
/quick-quality --report --detailed       # Comprehensive quality report
```

Ready to improve your code quality?