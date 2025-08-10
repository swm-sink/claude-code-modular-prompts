---
name: start
description: Adaptive initialization based on project complexity
usage: "/start [--mode auto|minimal|full]"
allowed-tools: [Read, Write, Glob, Grep, Task]
---

# Adaptive Project Initialization

I'll set up Claude Code for your project with the right level of sophistication.

## Quick Complexity Assessment

Let me check your project structure:
- Checking for existing .claude/ configuration
- Detecting project type and size
- Identifying frameworks and conventions

<minimal-mode>
<!-- For empty/tiny projects or --mode minimal -->

## Minimal Setup (< 1 minute)

Creating basic Claude Code structure:
1. `.claude/commands/` directory for your commands
2. Simple `settings.json` with essential permissions
3. Basic `CLAUDE.md` for project context

No analysis needed for this simple setup.
</minimal-mode>

<standard-mode>
<!-- For typical projects with detectable framework -->

## Standard Setup (2-3 minutes)

I detected: [project type, framework, size]

I'll create a tailored setup:
1. **Commands**: Relevant to your [detected stack]
2. **Settings**: Optimized for [project type]
3. **Context**: Comprehensive CLAUDE.md with project insights

*Quick check*: Is this primarily for [detected purpose]? (Y/n)

If yes or no response, I'll adjust accordingly.
</standard-mode>

<full-mode>
<!-- For complex projects or --mode full -->

## Comprehensive Setup (5 minutes)

This looks like a substantial project. Let me gather key information:

**Essential question**: What's the primary goal for using Claude Code?
- Feature development
- Debugging and maintenance  
- Code review and refactoring
- Testing and quality
- Other: [specify]

Based on your answer, I'll:
1. Analyze codebase patterns with focused agents
2. Create custom commands for your workflow
3. Configure advanced settings
4. Generate detailed documentation

*I'll intelligently handle everything else based on detected patterns.*
</full-mode>

## Execution

Based on assessment, using [minimal|standard|full] approach:

### Creating Structure
- Setting up .claude/ directory
- Adding appropriate commands
- Configuring settings.json
- Generating CLAUDE.md

### Smart Defaults Applied
- **Framework**: [detected or "generic"]
- **Testing**: [detected or "jest/pytest"]
- **Style**: [detected from existing code]
- **Workflow**: [inferred from git history]

## Complete!

Claude Code is now configured for your project.

**Quick start**:
- `/help` - See available commands
- `/build <feature>` - Start building
- `/analyze` - Understand your codebase

*Setup used [mode] mode based on project complexity.*