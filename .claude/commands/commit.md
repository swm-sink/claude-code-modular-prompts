---
name: commit
description: Create a well-structured git commit with proper message
usage: "/commit [--type feat|fix|docs|style|refactor|test|chore]"
allowed-tools: [Bash, WebSearch]
---

# Create Git Commit

I'll help you create a professional git commit with a clear message.

## What I'll Do

1. **Check Your Changes**
   - Run `git status` to see modified files
   - Run `git diff` to understand what changed
   - Identify the type of change (feature, fix, refactor, etc.)

2. **Research Commit Best Practices**
   - Search for commit message conventions for your project type
   - Look for your team's existing commit patterns
   - Apply conventional commit standards if appropriate

3. **Create the Commit**
   - Stage appropriate files
   - Write a clear, descriptive commit message
   - Follow the pattern: `type(scope): description`
   - Add body if changes are complex

## Commit Message Format

```
type(scope): subject

body (optional)

footer (optional)
```

Examples:
- `feat(auth): add OAuth2 integration`
- `fix(api): resolve N+1 query in user endpoint`
- `refactor(tests): simplify test fixtures`

Let me analyze your changes and create a commit...