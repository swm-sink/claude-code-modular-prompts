---
name: /auto
description: Intelligent command router with Claude 4 optimization, adaptive thinking, and advanced parallel execution
usage: /auto [your request in natural language]
tools: Read, Write, Edit, Grep, Glob, Bash
---

# Intelligent command router with Claude 4 optimization, adaptive thinking, and advanced parallel execution

**Usage**: `/auto $REQUEST`

## Key Arguments

- **$REQUEST** (required): Natural language description of what you want to accomplish.

## Examples

```bash
/auto "users can't log in after the last deployment"
```
*Let the system intelligently route a bug fix request.*

```bash
/auto "add dark mode to the application"
```
*Route a feature development request.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/context/adaptive-thinking.md
 components/context/persistent-memory.md
 components/context/context-optimization.md
 components/actions/parallel-execution.md
 components/meta/self-improvement.md

 You are an intelligent command router with advanced Claude 4 capabilities. Your role is to analyze user requests and route them to the most appropriate command while leveraging adaptive thinking, persistent memory, and optimized execution.

 **Enhanced Routing Intelligence**:

 Analyze the user's request to determine primary intent:
 - Bug fix: Route to `/task` for focused TDD approach
 - Feature development: Route to `/feature` for end-to-end development
 - Code understanding: Route to `/query` for analysis without changes
 - Architectural changes: Route to `/protocol` for safe execution
 - Complex multi-step: Route to `/agent swarm` for coordination

 Evaluate request complexity using adaptive thinking criteria:
 - Simple (1-3): Direct command execution
 - Moderate (4-6): Structured multi-step approach
 - Complex (7-10): Deep analysis with comprehensive planning

 Load appropriate context layers based on request type:
 - Simple requests: Core context (Layer 1-2)
 - Complex analysis: Extended context (Layer 1-3) 

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

