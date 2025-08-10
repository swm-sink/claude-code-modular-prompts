---
name: orchestrate
description: Analyze project and set up Claude Code for your specific needs
usage: "/orchestrate"
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, LS, WebSearch]
---

# Project Setup Orchestration

When this command runs, I will immediately:

## 1. Detect Your Project Type
I'll examine your project files to understand your technology stack:
- Check for package.json, requirements.txt, go.mod, Cargo.toml, etc.
- Identify frameworks and dependencies
- Understand your project structure

## 2. Research Current Best Practices
I'll search for the latest patterns and practices for your stack:
- Search for best practices specific to your framework (2024-2025)
- Find common anti-patterns to avoid
- Identify testing and deployment strategies

## 3. Create Custom Commands
Based on what I find, I'll create commands tailored to your project:
- Build commands that match your workflow
- Test commands suited to your testing framework
- Deployment commands for your infrastructure

## 4. Set Up Project Context
I'll create a CLAUDE.md file that helps me understand your project:
- Document your architecture patterns
- Note team conventions I discover
- Record important technical decisions

## What I'll Actually Do
1. Use `Glob` and `LS` to explore your project structure
2. Use `Read` to examine key configuration files
3. Use `WebSearch` to find current best practices for your stack
4. Use `Write` to create custom commands in .claude/commands/
5. Use `Write` to create your project's CLAUDE.md

This takes about 5-10 minutes and gives you a Claude Code setup that actually understands your specific project.

Ready? I'll start analyzing your project now.