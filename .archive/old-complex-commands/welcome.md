---
name: welcome
description: Welcome guide and getting started with Claude Context Architect
usage: "welcome"
allowed-tools: [Read, Write]
category: core
---

# Welcome to Claude Context Architect

## 👋 Welcome!

Welcome to **Claude Context Architect** - a deep discovery generation engine that transforms Claude into YOUR project expert through comprehensive analysis and custom generation.

## What This System Does

Claude Context Architect performs a **30-60 minute deep consultation** to:
- 🔍 **Analyze** your project's unique architecture and patterns
- 🧬 **Extract** your project's DNA (technical choices, conventions, workflows)
- 🛠️ **Generate** custom commands specific to YOUR codebase
- 🤖 **Create** specialized agents that understand YOUR domain
- 📚 **Build** context systems that make Claude truly useful for YOUR project

## Getting Started

### Step 1: Begin Deep Discovery
Start your consultation journey:
```
/deep-discovery start
```
This initiates the complete 30-60 minute consultation process.

### Step 2: Project Analysis (Alternative)
Or run individual phases:
```
/discover-project      # Analyze your codebase and extract DNA
/generate-commands     # Generate custom commands from DNA
```

### Step 3: Interactive Consultation
For deeper understanding:
```
/consult-interactive   # Answer questions about your project
/consult-technical     # Technical architecture discussion
/consult-domain        # Domain and business logic exploration
```

## Current System Status

**Integration Level**: 48% Complete
- ✅ Core commands integrated with backend
- ✅ Project discovery functional
- ✅ Command generation ready
- ⚠️ Consultation partially integrated
- ⚠️ Full end-to-end flow in testing

## Available Commands

### Core Orchestration
- `/deep-discovery` - Master orchestrator for complete consultation
- `/discover-project` - Analyze project and extract DNA
- `/generate-commands` - Generate custom commands from DNA

### Consultation Commands
- `/consult-interactive` - Interactive Q&A session
- `/consult-technical` - Technical deep dive
- `/consult-domain` - Domain expertise extraction
- `/consult-workflow` - Workflow analysis

### Management Commands
- `/manage-session-state` - Save/resume consultation sessions
- `/coordinate-agents` - Manage specialized agents
- `/validate-evidence` - Validate discoveries

## What to Expect

### Time Investment
- **Full Consultation**: 30-60 minutes
- **Project Analysis**: 15-20 minutes
- **Command Generation**: 10-15 minutes

### Outputs
- `PROJECT-DNA.md` - Complete analysis of your project
- Custom commands in `.claude/commands/generated/`
- Specialized agents configured for your domain
- Multi-file context system

## Need Help?

### Quick Help
- `/help` - General help information
- `/list-commands` - See all available commands
- `/deep-discovery status` - Check consultation progress

### Troubleshooting
If you encounter issues:
1. Check `PROJECT-STATE-VERIFICATION.md` for current status
2. Run `/validate-integration` to verify setup
3. Review logs in `.claude-architect/logs/`

## Ready to Begin?

Start your deep discovery journey:
```
/deep-discovery start
```

Welcome to a new level of AI-assisted development where Claude truly understands YOUR project!

---
*Claude Context Architect v1.0 - Transforming Claude into YOUR project expert*