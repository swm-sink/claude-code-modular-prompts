---
name: /quick-dev
description: "Instant development assistance - works with any codebase"
usage: /quick-dev [--review | --debug | --optimize | --explain] [file-path]
category: core
allowed-tools: Read, Edit, Bash, Grep, Glob
---

# 🛠️ Instant Development Assistance

**Universal development help - works immediately with any codebase!**

## Quick Actions

### Code Review
```
/quick-dev --review src/components/UserForm.js
/quick-dev --review "review this entire directory"
```

### Debugging Help  
```
/quick-dev --debug "my app crashes on login"
/quick-dev --debug src/auth/login.py
```

### Performance Optimization
```
/quick-dev --optimize "slow API endpoints"
/quick-dev --optimize database/queries.sql
```

### Code Explanation
```
/quick-dev --explain src/utils/encryption.js
/quick-dev --explain "how does authentication work here?"
```

## Universal Development Support

**🔍 What I'll analyze:**
- Code quality and best practices
- Performance bottlenecks
- Security vulnerabilities  
- Architecture patterns
- Testing coverage gaps

**🚀 What I'll provide:**
- Specific, actionable suggestions
- Code examples and fixes
- Architecture recommendations
- Performance improvements
- Security enhancements

## Language & Framework Agnostic

**Works with any tech stack:**
- Frontend: React, Vue, Angular, Svelte, vanilla JS
- Backend: Node.js, Python, Java, Go, Rust, C#, PHP
- Mobile: React Native, Flutter, Swift, Kotlin
- Databases: SQL, NoSQL, Redis, etc.
- DevOps: Docker, Kubernetes, AWS, Azure, GCP

## Example Sessions

**Code Review:**
```
👤 /quick-dev --review src/payment/checkout.js
🤖 Analyzing checkout.js...
🤖 Found 3 issues:
   1. Missing error handling for API calls
   2. Sensitive data logging in line 45
   3. Consider extracting validation logic
🤖 Here are the fixes...
```

**Debugging:**
```
👤 /quick-dev --debug "users can't log in"
🤖 Let me examine your authentication flow...
🤖 Found the issue: session timeout is too short
🤖 Here's the fix and why it happens...
```

## Smart Context Detection

I'll automatically:
- **Detect** your programming language and framework
- **Read** relevant files to understand context
- **Apply** language-specific best practices
- **Suggest** framework-appropriate solutions
- **Follow** your existing code patterns

## When to Use Different Dev Commands

- **`/quick-dev`**: Immediate help, any project *(this command)*
- **`/dev`**: Enhanced features after `/adapt-to-project`
- **`/dev-setup`**: Environment and tooling setup (after customization)

## Ready for Development Help?

Just specify what you need help with:

```
/quick-dev --review [file-or-description]
/quick-dev --debug [problem-description]  
/quick-dev --optimize [area-to-improve]
/quick-dev --explain [code-or-concept]
```

I'll analyze your code and provide specific, actionable guidance!