# First Commands - Essential Framework Usage

> **Goal**: Learn the 4 essential commands that handle 90% of your daily tasks.

After completing [Quick Start](quick-start.md), these are the commands you'll use every day.

## 🎯 The Essential Four Commands

### 1. `/query` - Understanding and Research (Read-Only)
**Purpose**: Analyze, investigate, and understand without making changes.

```bash
# Understand your codebase
/query "how does authentication work in this project?"
/query "find all components that use state management"
/query "explain the database schema"

# Find issues and patterns
/query "identify potential security vulnerabilities"
/query "analyze test coverage and gaps"
/query "find code that violates our style guide"

# Research and exploration
/query "show me all the API endpoints"
/query "explain the build and deployment process"
/query "find examples of our coding patterns"
```

**When to use**: When you need to understand, analyze, or research without modifying anything.

### 2. `/task` - Focused Development (Single Component)
**Purpose**: Implement specific, focused changes to individual components or files.

```bash
# Fix specific bugs
/task "fix the password validation bug in UserForm.tsx"
/task "resolve the memory leak in data processing"
/task "update the API error handling in auth service"

# Add focused features
/task "add email validation to the contact form"
/task "implement dark mode toggle in header"
/task "create utility function for date formatting"

# Refactor specific code
/task "extract reusable logic from payment component"
/task "optimize the slow search function"
/task "update deprecated API calls in user service"
```

**When to use**: Single file changes, bug fixes, small features, focused refactoring.

### 3. `/auto` - Intelligent Routing (Let Framework Decide)
**Purpose**: Let the framework analyze your request and route to the optimal command.

```bash
# When you're unsure which command to use
/auto "improve our user authentication system"
/auto "add payment processing to our e-commerce site"
/auto "optimize the performance of our dashboard"

# Complex requests that might need multiple approaches
/auto "modernize our legacy code"
/auto "implement comprehensive error handling"
/auto "add monitoring and observability"

# Research + implementation combinations
/auto "analyze current security and fix vulnerabilities"
/auto "review our testing strategy and improve coverage"
/auto "evaluate our API design and suggest improvements"
```

**When to use**: When unsure which command to use, complex requests, or when you want the framework to make smart decisions.

### 4. `/docs` - Documentation Management (Create/Update Docs)
**Purpose**: Create, update, and manage documentation files.

```bash
# Create new documentation
/docs generate "API Reference Guide"
/docs generate "Getting Started Guide for New Developers"
/docs generate "Deployment Instructions"

# Update existing documentation
/docs "update the README with new features"
/docs "refresh the architecture documentation"
/docs "add examples to the component library docs"

# Documentation maintenance
/docs validate "check all docs for completeness"
/docs search "authentication" "find docs needing updates"
```

**When to use**: Creating or updating documentation files. Never use for understanding existing code (use `/query` instead).

## 🤔 Command Selection Made Simple

### "I want to understand something" → `/query`
- How does X work?
- Find all Y in the codebase
- Analyze Z for issues
- **Result**: Analysis and explanation, no files changed

### "I want to fix/add something specific" → `/task`
- Fix bug in specific file
- Add feature to component
- Update single function
- **Result**: Focused changes to specific files

### "I'm not sure what's needed" → `/auto`
- Improve our X system
- Add Y capability
- Optimize Z performance
- **Result**: Framework chooses best approach

### "I want to document something" → `/docs`
- Create guide for X
- Update documentation about Y
- Generate reference for Z
- **Result**: Documentation files created/updated

## 🚀 Practice Exercises

Try these commands in your project to get comfortable:

### Exercise 1: Project Discovery (5 minutes)
```bash
# Learn about your project
/query "what is the main technology stack?"
/query "what are the key components or modules?"
/query "how is the project structured?"
```

### Exercise 2: Make a Small Improvement (10 minutes)
```bash
# Find something to improve
/query "find TODO comments or simple improvements"

# Then implement it
/task "implement the TODO in [specific file]"
```

### Exercise 3: Let Framework Guide You (5 minutes)
```bash
# Try intelligent routing
/auto "help me understand and improve error handling"

# Notice how framework chooses approach
```

### Exercise 4: Document What You Learned (5 minutes)
```bash
# Create documentation about your discoveries
/docs generate "Project Overview for New Team Members"
```

## 💡 Pro Tips for Success

### 1. Start with `/query` for Understanding
```bash
# Before making changes, understand the current state
/query "how does the current login system work?"
# Then make informed changes
/task "add two-factor authentication to login"
```

### 2. Use `/auto` When Uncertain
```bash
# Instead of guessing the right approach
/auto "improve our API performance"
# Framework will analyze and choose optimal strategy
```

### 3. Keep `/task` Focused
```bash
# Good: Specific and focused
/task "fix the date picker validation in ProfileForm"

# Avoid: Too broad for /task
/task "rebuild the entire user management system"  # Use /auto or /feature instead
```

### 4. Use `/docs` Only for Documentation
```bash
# Good: Creating actual documentation
/docs generate "API Usage Guide"

# Avoid: Research that doesn't create docs
/docs "how does authentication work?"  # Use /query instead
```

## 🔄 Typical Daily Workflow

### Morning: Understand Current State
```bash
/query "what changed in the codebase recently?"
/query "are there any failing tests or issues?"
/query "what are the current priorities?"
```

### During Development: Focused Work
```bash
# For each task:
/query "understand the area I'm working on"
/task "implement the specific change"
# Or use /auto if approach isn't clear
```

### End of Day: Documentation and Review
```bash
/query "what did I accomplish today?"
/docs "update documentation for changes made"
```

## 🚧 Common Beginner Mistakes

### ❌ Wrong Command for Task
```bash
# Wrong: Using /docs for research
/docs "explain how authentication works"
# Right: Use /query for research
/query "explain how authentication works"

# Wrong: Using /query for making changes
/query "add login validation"
# Right: Use /task for specific changes
/task "add login validation"
```

### ❌ Too Broad for `/task`
```bash
# Wrong: Too complex for /task
/task "rebuild the entire payment system"
# Right: Use /auto for complex work
/auto "modernize our payment processing"
```

### ❌ Not Starting with Understanding
```bash
# Wrong: Making changes without understanding
/task "fix the bug in user profile"
# Right: Understand first, then fix
/query "what's the bug in user profile?"
/task "fix the specific validation issue in ProfileForm.tsx"
```

## ✅ Success Indicators

You're using commands correctly when:

- [ ] `/query` gives you detailed analysis without creating files
- [ ] `/task` makes focused changes to specific files
- [ ] `/auto` intelligently routes complex requests
- [ ] `/docs` creates or updates documentation files
- [ ] You understand when to use each command
- [ ] Your requests get the results you expect

## 🎯 Next Steps

### Today (30 minutes)
- **Practice all four commands** with your actual project
- **Learn command selection**: [Command Selection Guide](../user-guide/commands/command-selection.md)

### This Week
- **Explore workflows**: [Common Patterns](../user-guide/workflows/common-patterns.md)
- **Customize framework**: [Project Configuration](../user-guide/customization/project-config.md)
- **Try advanced commands**: [Advanced Commands](../user-guide/commands/advanced-commands.md)

### Ongoing
- **Master complex workflows**: Advanced Patterns
- **Optimize your setup**: Performance Optimization

---

**Ready to explore more?** Continue to [Command Selection Guide](../user-guide/commands/command-selection.md) to master when to use each command.

**Want to see real examples?** Check out [Common Workflows](../user-guide/workflows/common-patterns.md) for practical usage patterns.