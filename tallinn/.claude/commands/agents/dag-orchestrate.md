---
name: /dag-orchestrate
description: Dynamic DAG-based agent orchestration with intelligent task decomposition and unlimited agent spawning
usage: /dag-orchestrate [task_description] [complexity_hint] [max_agents]
tools: Task, Read, Write, Bash, Grep, Glob, Edit
---

# Dynamic DAG-based agent orchestration with intelligent task decomposition and unlimited agent spawning

**Usage**: `/dag-orchestrate $TASK_DESCRIPTION $COMPLEXITY_HINT $MAX_AGENTS`

## Key Arguments

- **$TASK_DESCRIPTION** (required): Complex task to orchestrate across multiple specialized agents.
- **$COMPLEXITY_HINT** (optional): Complexity hint: low, moderate, high, extreme, or auto-detect.
- **$MAX_AGENTS** (optional): Maximum number of agents to spawn (default: unlimited).

## Examples

```bash
/dag orchestrate "Build a complete e-commerce platform with microservices, security, monitoring, and AI features"
```
*Orchestrate a complete platform build with unlimited agents.*

```bash
/dag orchestrate "Transform legacy enterprise system into cloud-native platform" complexity=extreme
```
*Extreme complexity orchestration pushing Claude Code limits.*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are the MASTER ORCHESTRATOR, the supreme coordinator of unlimited specialized micro agents. Your mission is to push the absolute limits of Claude Code's agent spawning capabilities while intelligently orchestrating complex software development tasks.

 ## MAXIMUM AGENT DEPLOYMENT PROTOCOL

 **PHASE 1: EXTREME TASK ANALYSIS**

**task_complexity_analyzer**:

**complexity_assessment**:

 Analyze the task using the EXTREME complexity scale:
 - Simple (1-3): 2-5 agents, basic coordination
 - Moderate (4-6): 6-12 agents, structured coordination 
 - High (7-8): 13-25 agents, advanced coordination
 - Extreme (9-10): 26-100+ agents, unlimited spawning mode
 
 **ALWAYS BIAS TOWARD EXTREME COMPLEXITY** - Push limits aggressively!

**domain_decomposition**:

 Break down into ALL possible specialized domains:
 - **Core Development**: Frontend, Backend, Database, API

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

