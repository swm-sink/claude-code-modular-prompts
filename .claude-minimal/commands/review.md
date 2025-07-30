---
name: /review
description: "Code review with suggestions and improvements"
usage: /review [file-path] or /review "description of code to review"
category: core
tools: Read, Edit, Bash, Grep, Glob
---

# Universal Code Review

**Comprehensive code review with actionable feedback and improvements.**

## Review Types

### File Review
```
/review src/components/UserProfile.jsx
/review backend/api/auth.py
/review database/migrations/001_create_users.sql
```

### Feature Review
```  
/review "user authentication implementation"
/review "payment processing logic"
/review "real-time chat functionality"
```

### Pull Request Review
```
/review "my latest changes for the dashboard feature"
/review "refactoring of the data layer"
/review "API endpoint additions"
```

## What Gets Reviewed

**🔍 Code Quality:**
- **Readability** and naming conventions
- **Structure** and organization  
- **Best practices** adherence
- **Performance** considerations
- **Error handling** completeness

**🛡️ Security & Safety:**
- **Vulnerability** detection
- **Input validation** checks
- **Authentication** and authorization
- **Data exposure** risks
- **Injection** attack prevention

**🧪 Testing & Maintainability:**
- **Test coverage** assessment
- **Documentation** quality
- **Code duplication** identification
- **Dependency** management
- **Future maintenance** considerations

## Review Output Format

### Issue Classification
- **🔴 Critical**: Security vulnerabilities, breaking changes
- **🟡 Important**: Performance issues, maintainability concerns  
- **🟢 Minor**: Style improvements, optional optimizations
- **💡 Suggestions**: Best practices, alternative approaches

### Actionable Feedback
- **Specific line references**
- **Code examples** for improvements
- **Explanation** of why changes are needed
- **Alternative implementations** 
- **Priority ranking** for fixes

## Example Review Sessions

### React Component Review
```
👤 /review src/components/UserDashboard.jsx

🤖 Reviewing UserDashboard.jsx...

📊 REVIEW SUMMARY:
✅ Good: Clean JSX structure, proper prop types
⚠️  Issues found: 4 important, 2 minor

🔴 CRITICAL ISSUES:
❌ Line 45: User data logged to console (security risk)
   Fix: Remove console.log or add production check
   
❌ Line 67: No error boundary for API calls
   Fix: Add try-catch with user-friendly error handling

🟡 IMPORTANT IMPROVEMENTS:
⚠️  Line 23: Heavy computation in render
   Fix: Move to useMemo hook
   
⚠️  Line 89: Inline styles (performance impact)
   Fix: Extract to CSS modules or styled-components

💡 SUGGESTIONS:
• Consider adding loading states
• Add prop validation with PropTypes
• Extract custom hooks for data fetching

🎯 PRIORITY FIXES:
1. Remove console.log (2 min)
2. Add error handling (15 min)  
3. Optimize rendering (10 min)
```

### API Endpoint Review
```
👤 /review "my new user registration endpoint"

🤖 Reviewing user registration implementation...

🛡️ SECURITY ASSESSMENT:
🔴 Critical: Password stored in plain text
🔴 Critical: No rate limiting on registration
🟡 Important: Email validation insufficient

📝 CODE QUALITY:
✅ Good: Clear function structure
⚠️  Issue: No input sanitization
⚠️  Issue: Error messages too revealing

🔧 SPECIFIC FIXES NEEDED:

1. **Password Security** (Critical - 30 min):
```javascript
// Current (unsafe):
user.password = req.body.password;

// Fix (safe):
const bcrypt = require('bcrypt');
user.password = await bcrypt.hash(req.body.password, 12);
```

2. **Rate Limiting** (Critical - 15 min):
```javascript
const rateLimit = require('express-rate-limit');
const registerLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5 // limit each IP to 5 requests per windowMs
});
app.post('/register', registerLimiter, registerUser);
```

🎯 IMPLEMENTATION PLAN:
1. Hash passwords (critical, 30 min)
2. Add rate limiting (critical, 15 min)
3. Improve email validation (important, 10 min)
4. Sanitize error messages (important, 20 min)
```

## Multi-Language Expertise

**Automatically applies language-specific best practices:**

**JavaScript/TypeScript**: React patterns, Node.js security, async/await usage
**Python**: PEP 8 compliance, Django/Flask patterns, type hints
**Java**: SOLID principles, Spring patterns, exception handling
**Go**: Idiomatic Go, error handling, concurrency patterns
**Rust**: Memory safety, ownership patterns, performance optimization

## Review Depth Options

### Quick Review
- Surface-level issues
- Obvious bugs and security problems
- Basic best practices check

### Comprehensive Review  
- Detailed analysis of all aspects
- Performance optimization suggestions
- Architecture and design feedback

### Expert Review
- Strategic technical guidance
- Long-term maintainability assessment
- Industry best practices application

## Integration Workflow

**Development Flow:**
1. Write code
2. Run `/review` for feedback
3. Use `/task` to implement fixes
4. Run `/test` to verify changes
5. Final `/review` before commit

**Team Usage:**
- Pre-commit review automation  
- Pull request preparation
- Code quality gate integration
- Knowledge sharing and learning

## Ready for Review?

Submit your code for comprehensive review:

```
/review src/components/MyComponent.jsx
/review "my authentication system"
/review "database optimization changes"
```

I'll provide detailed, actionable feedback to improve your code quality!