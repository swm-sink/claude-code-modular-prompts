---
name: welcome
description: Adaptive learning journey for Claude Code mastery
usage: "/welcome [--level beginner|intermediate|expert]"
allowed-tools: [Read, Glob, WebSearch, Task]
---

# Welcome to Claude Code Mastery

I'll create a personalized learning path based on your experience level and project needs.

## Adaptive Assessment Phase

First, I'll understand your context through parallel analysis:

**Task 1: Experience Detection** (via sub-agent)
- Scan for existing Claude files (.claude/, CLAUDE.md)
- Check git history for Claude Code usage
- Identify your development patterns

**Task 2: Project Complexity** (via sub-agent)  
- Analyze codebase size and structure
- Detect frameworks and technologies
- Assess architectural patterns

**Task 3: Learning Style** (interactive)
- Quick questions about your preferences
- Previous AI tool experience
- Specific goals with Claude Code

## Personalized Learning Path

Based on assessment, I'll provide:

**Beginner Path:**
- Core concepts with examples from YOUR code
- Interactive exercises using your project
- Common pitfalls specific to your stack

**Intermediate Path:**
- Advanced techniques for your use cases
- Performance optimization strategies
- Integration with your workflow

**Expert Path:**
- Cutting-edge patterns and research
- Custom agent orchestration
- Meta-prompting techniques

## Interactive Learning Mode

I'll demonstrate concepts using your actual code:
- Live examples from your project
- Before/after comparisons
- Immediate practice opportunities

Starting adaptive assessment now...