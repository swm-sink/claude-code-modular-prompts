# Claude Code Command Creation Guide

## Quick Start: Create Your First Command

### 1. Create the File
```bash
touch .claude/commands/my-command.md
```

### 2. Add YAML Frontmatter
```yaml
---
name: my-command
description: Brief description of what the command does
usage: "/my-command [arguments]"
allowed-tools: [Read, Write, WebSearch]
---
```

### 3. Write Clear Instructions
```markdown
# Command Title

I'll help you [specific action].

## What I'll Do

1. **First Step**
   - Specific action with tool
   - What I'll look for
   - What I'll create

2. **Second Step**
   - Next action
   - How I'll validate
   - What you'll get

Let me start working on this...
```

## Command Design Principles

### 1. Keep It Simple (40-50 lines)
**Good**: Clear, focused instructions that fit on one screen
**Bad**: 800-line specifications with complex frameworks

### 2. Action Over Description
**Good**: "I'll scan your project with `Glob` and find patterns with `Grep`"
**Bad**: "This command employs sophisticated pattern recognition algorithms"

### 3. Use Tools, Don't Describe Them
**Good**: Direct Claude to use Read, Write, WebSearch
**Bad**: XML pseudo-code that doesn't trigger actual tool use

### 4. Be Specific
**Good**: "I'll search for React best practices 2024-2025"
**Bad**: "I'll research best practices"

## YAML Frontmatter Reference

### Required Fields
```yaml
name: command-name           # No spaces, lowercase
description: What it does     # One line, action-oriented
allowed-tools: [...]         # Tools this command can use
```

### Optional Fields
```yaml
usage: "/command [args]"     # How to invoke the command
category: development        # For organization
argument-hint: "[file]"      # Hint for arguments
model: haiku                # Use specific model (default: current)
```

### Available Tools
- `Read` - Read files
- `Write` - Write/create files
- `Edit` - Edit existing files
- `MultiEdit` - Multiple edits in one file
- `Bash` - Run shell commands
- `Glob` - Find files by pattern
- `Grep` - Search file contents
- `LS` - List directory contents
- `WebSearch` - Search the web
- `WebFetch` - Fetch web content
- `Task` - Spawn sub-agents
- `TodoWrite` - Manage todo lists

## Command Patterns That Work

### Pattern 1: Analysis Command
```markdown
---
name: analyze-x
description: Analyze X and provide insights
allowed-tools: [Read, Glob, Grep]
---

# Analyze [Subject]

I'll analyze your [subject] and identify key patterns.

## Analysis Process
1. Scan structure with `Glob`
2. Read key files with `Read`
3. Find patterns with `Grep`
4. Summarize findings

Starting analysis...
```

### Pattern 2: Creation Command
```markdown
---
name: create-x
description: Create X based on your requirements
allowed-tools: [Read, Write, WebSearch]
---

# Create [Thing]

I'll create [thing] following best practices.

## Creation Steps
1. Research current best practices
2. Read existing code for context
3. Generate appropriate solution
4. Write files with proper structure

Creating your [thing]...
```

### Pattern 3: Fix Command
```markdown
---
name: fix-x
description: Find and fix X issues
allowed-tools: [Read, Edit, Grep]
---

# Fix [Problem]

I'll find and fix [problem] in your code.

## Fix Process
1. Search for problem patterns
2. Analyze each occurrence
3. Apply appropriate fixes
4. Verify improvements

Finding and fixing issues...
```

## Anti-Patterns to Avoid

### ❌ XML Theater
```xml
<bad_example>
<phase_1>
  <step>Do something</step>
  <validation>Check something</validation>
</phase_1>
</bad_example>
```
This doesn't make Claude do anything - it's just documentation.

### ❌ Over-Specification
Don't try to handle every edge case. Claude is smart enough to handle variations.

### ❌ Multi-Phase Complexity
Claude Code is stateless. Don't design commands that require maintaining state across phases.

### ❌ False Promises
Don't claim the command will "automatically enforce" or "continuously monitor" - Claude runs once per invocation.

## Testing Your Command

### 1. Syntax Check
- Valid YAML frontmatter?
- Allowed-tools specified?
- Name follows conventions?

### 2. Clarity Check
- Would a new user understand?
- Single clear purpose?
- Actionable instructions?

### 3. Practical Test
```bash
# In Claude Code, run your command
/my-command test-argument

# Verify:
- Claude uses the right tools
- Output matches intent
- No hallucinations
- Completes quickly
```

## Examples of Good Commands

### Minimal Effective Command
```yaml
---
name: quick-fix
description: Find and fix common issues
allowed-tools: [Read, Edit, Grep]
---

# Quick Fix

I'll find and fix common issues in your code.

I'll check for:
- Unused imports
- Console.log statements
- TODO comments
- Basic formatting issues

Scanning your code now...
```

### Research-Integrated Command
```yaml
---
name: upgrade-deps
description: Upgrade dependencies safely
allowed-tools: [Read, Edit, WebSearch, Bash]
---

# Upgrade Dependencies

I'll upgrade your dependencies safely.

Steps:
1. Check current versions
2. Research breaking changes
3. Update incrementally
4. Run tests after each update

Starting upgrade process...
```

## Command Maintenance

### When to Update
- User feedback indicates confusion
- Command produces unexpected results
- New tools become available
- Best practices change

### How to Update
1. Test current behavior
2. Identify specific issue
3. Make minimal change
4. Test new behavior
5. Document change

## Advanced Tips

### 1. Use Sub-Agents for Complexity
Instead of one complex command, spawn specialized sub-agents:
```yaml
allowed-tools: [Task]
```

### 2. Collect Context with Bash
```markdown
## Context (auto-included)
- Node version: !`node -v`
- Current branch: !`git branch --show-current`
```

### 3. Dynamic Arguments
```markdown
I'll work on: $ARGUMENTS
```

### 4. Conditional Tool Usage
Specify tool permissions precisely:
```yaml
allowed-tools: [Read, Bash(npm test:*), Write(*.test.js)]
```

## Common Questions

**Q: How long should a command be?**
A: 40-50 lines ideally, 100 maximum

**Q: Should I use multiple commands or one complex command?**
A: Multiple simple commands > one complex command

**Q: How do I handle errors?**
A: Claude handles errors naturally - just ensure clear instructions

**Q: Can commands call other commands?**
A: No, but they can spawn sub-agents with Task tool

**Q: Should I version my commands?**
A: Use git for versioning, not version numbers in commands

## Getting Help

- Test commands in Claude Code directly
- Check existing commands for patterns
- Keep commands simple and focused
- Iterate based on actual usage