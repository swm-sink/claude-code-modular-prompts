# Usage Guide

## Getting Started

After installation, open Claude Code in your project directory and try:

```
/help                                # See all available commands
/task "add user authentication"      # Execute any development task
```

## The 88 Commands

### `/help` - Command Guide
Shows all available commands with descriptions and examples.

```
/help           # Show all commands
/help task      # Get detailed help for /task command
```

### `/task` - Execute Development Tasks
Handles any development work - automatically adapts to your programming language and framework.

```
/task "implement JWT authentication"
/task "optimize database queries" 
/task "add real-time chat functionality"
/task "set up CI/CD pipeline"
/task "fix memory leak in user service"
```

### `/analyze` - Analyze Code & Problems
Analyzes code, architecture, or problems in your project.

```
/analyze "why is my app slow?"
/analyze src/components/UserDashboard.jsx
/analyze "memory usage keeps growing"
/analyze "API response times are inconsistent"
```

### `/review` - Code Review
Provides code review with suggestions for improvement.

```
/review src/auth/login.js
/review "my payment processing implementation"  
/review components/PaymentForm.tsx
/review --security src/api/routes.js
```

### `/debug` - Debug Issues
Helps debug issues and errors in your code.

```
/debug "users can't log in"
/debug "TypeError: Cannot read property 'name' of undefined"
/debug "database connection timeout"
/debug "React component not rendering"
```

### `/test` - Testing Assistance
Generates tests and helps with testing strategies.

```
/test --generate src/utils/validation.js
/test --run --coverage
/test --fix "failing authentication tests"
/test --e2e "user registration flow"
```

### `/docs` - Documentation
Creates and maintains documentation for your code.

```
/docs --generate README
/docs --api src/controllers/users.js
/docs --update "installation instructions"
/docs src/utils/helpers.js
```

## Language & Framework Support

Commands automatically adapt to your tech stack:

**Languages**: JavaScript, TypeScript, Python, Java, Go, Rust, C#, PHP, Ruby, Swift
**Frameworks**: React, Vue, Angular, Django, Spring, Laravel, Rails, Express, Next.js, Flask
**Project Types**: Web apps, APIs, mobile apps, desktop apps, scripts, microservices

## Real Usage Examples

### Adding a Feature
```
/task "add password reset functionality"
# Claude analyzes your project structure and provides step-by-step implementation
```

### Debugging Performance
```
/analyze "API endpoints are slow"
# Claude examines your code and suggests specific optimizations
```

### Code Review
```
/review src/authentication/auth.js
# Claude provides security, performance, and maintainability feedback
```

### Writing Tests
```
/test --generate src/services/user-service.js
# Claude creates comprehensive test suite matching your testing framework
```

## Tips for Best Results

**Be specific**: Instead of "fix my code", try "fix authentication error in login function"
**Include context**: "debug database connection in production environment"
**Ask follow-ups**: Use /help if any command isn't clear

## Customizing Commands

Commands work as-is, but you can modify them:

1. Edit files in `.claude/commands/` directory
2. Add project-specific examples 
3. Adjust command descriptions for your team

## Advanced Usage

**Chain commands**:
```
/analyze src/api/auth.js
# Review the analysis, then:
/review src/api/auth.js
# Review the suggestions, then:
/task "implement the security improvements suggested"
```

**Project-specific workflows**:
```
/task "deploy to staging environment"
# Commands learn your deployment process and provide specific guidance
```

The commands get smarter as you use them - they learn your project structure, coding patterns, and preferences.