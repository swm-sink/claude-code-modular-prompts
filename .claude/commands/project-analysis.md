---
name: project-analysis
description: Analyze your project structure, patterns, and provide actionable insights
usage: "/project-analysis [--focus architecture|performance|security|quality]"
allowed-tools: [Read, Glob, Grep, LS, WebSearch]
---

# Quick Project Analysis

I'll analyze your project and give you immediate, actionable insights.

## What I'll Do Right Now

1. **Scan Your Project Structure**
   - Use `Glob` to map your file organization
   - Use `LS` to understand directory hierarchy
   - Identify your frameworks and dependencies

2. **Detect Patterns & Anti-Patterns**
   - Use `Grep` to find common code patterns
   - Look for performance bottlenecks (N+1 queries, missing indexes)
   - Check for security issues (hardcoded secrets, SQL injection risks)
   - Identify architectural problems (circular dependencies, god objects)

3. **Analyze Code Quality**
   - Check test coverage presence
   - Look for documentation patterns
   - Identify technical debt indicators

4. **Provide Specific Recommendations**
   - List your top 5 issues with evidence
   - Suggest concrete fixes you can implement today
   - Estimate effort for each improvement

## Output Format

I'll give you a concise report with:
- **Quick Wins**: Things you can fix in < 1 hour
- **Major Issues**: Problems that need attention soon
- **Architecture Insights**: Patterns I've detected
- **Next Steps**: Prioritized action items

Let me start analyzing your project now...