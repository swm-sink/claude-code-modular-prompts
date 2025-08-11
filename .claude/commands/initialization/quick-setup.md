---
name: quick-setup
description: Fast initialization with essential project detection and setup
usage: "/quick-setup"
tools: [Read, Write, Glob, LS]
---

# Quick Setup

I'll detect your project type and create a tailored Claude Code configuration.

## What I'll Do

1. **Detect Your Stack**
   - Check for package.json, requirements.txt, go.mod, Cargo.toml
   - Identify frameworks (React, Django, Express, etc.)
   - Determine project structure

2. **Create Configuration**
   - Generate appropriate .claude/settings.json
   - Set up command discovery
   - Configure tool permissions

3. **Initialize CLAUDE.md**
   - Document project context
   - Set up conventions
   - Define workflows

4. **Recommend Commands**
   - Based on your tech stack
   - Tailored to project phase
   - Best practices for your framework

## Output

You'll get:
- Configured Claude Code project
- Project-specific CLAUDE.md
- Recommended next commands
- Setup verification report

Starting project detection now...