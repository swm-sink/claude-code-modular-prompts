---
name: /auto
description: Intelligent command router with context-aware selection and automatic parameter detection (v2.0)
version: 2.0
usage: '/auto "[your request in natural language]"'
allowed-tools:
- Read
- Write
- Edit
- Grep
- Glob
- Bash
dependencies:
- /help
- /quick-command
- /task
validation:
  pre-execution: Parse request and identify intent with confidence scoring
  during-execution: Monitor command execution and provide fallback options
  post-execution: Verify request was fulfilled and suggest follow-up commands
progressive-disclosure:
  layer-integration: Automatically routes to appropriate layer based on request complexity
  escalation-path: Simple routing → parameter inference → multi-command orchestration
  de-escalation: Suggests simpler alternatives when appropriate
safety-measures:
  - Confirm destructive operations
  - Validate command parameters
  - Prevent infinite routing loops
  - Show routing decisions transparently
error-recovery:
  ambiguous-request: Provide clarification options with examples
  no-match: Suggest closest commands and ask for refinement
  execution-failure: Offer alternative approaches
category: core
---

# /auto - Intelligent Command Router for lusaka

I'll analyze your request and automatically route it to the most appropriate command for your software-development project using Python.

## How It Works

This command analyzes your natural language request and routes it to the best available command in your lusaka prompt library.
## Usage
```bash
/auto "fix the authentication bug in the login system"
/auto "add user profile editing functionality"  
/auto "analyze the performance bottleneck in our API"
/auto "refactor the database connection logic safely"
```

## Examples

**Development Tasks:**
- `/auto "implement user authentication"`
- `/auto "fix the database connection issue"`

**Analysis & Research:**
- `/auto "analyze performance bottlenecks"`
- `/auto "research best practices for Python"`

I'll route your request to the most appropriate command and provide you with the best implementation approach for your lusaka project.
