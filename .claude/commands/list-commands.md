---
name: list-commands
description: List all available Claude Context Architect commands
usage: "list-commands [category]"
allowed-tools: [Read, LS, Glob]
category: core
---

# List Available Commands

## Purpose
Display all available commands in the Claude Context Architect system, organized by category.

## Command Categories

### 🎯 Core Commands (Getting Started)
- `/welcome` - Welcome guide and getting started
- `/deep-discovery` - Master orchestrator for 30-60 minute consultation
- `/discover-project` - Analyze project and extract DNA
- `/generate-commands` - Generate custom commands from DNA
- `/list-commands` - This command (list all available commands)

### 🗣️ Consultation Commands (Interactive Analysis)
- `/consult-interactive` - Interactive Q&A about your project
- `/consult-technical` - Technical architecture deep dive
- `/consult-domain` - Domain and business logic exploration  
- `/consult-workflow` - Workflow and process analysis
- `/begin-consultation` - Start consultation session

### 🔬 Research & Analysis Commands
- `/analyze-repository` - Deep repository analysis
- `/research-patterns` - Research patterns from leading repositories
- `/extract-patterns` - Extract patterns from codebase
- `/validate-evidence` - Validate discovered patterns

### 🤖 Agent Commands
- `/coordinate-agents` - Manage specialized agents
- `/develop-agents` - Create project-specific agents
- `/session-manage` - Manage agent sessions

### 🔧 Generation Commands
- `/generate-commands` - Generate custom commands
- `/generate-context` - Generate context files
- `/generate-agents` - Generate specialized agents

### 📊 Management Commands
- `/manage-session-state` - Save/resume consultation sessions
- `/validate-integration` - Check system integration
- `/config-hierarchy` - Manage configuration hierarchy

### 🏗️ Architecture Commands  
- `/foundation-system-overview` - System architecture overview
- `/deep-discovery-real` - Production discovery implementation

## Usage Examples

### List All Commands
```
/list-commands
```
Shows this complete list of all available commands.

### List by Category
```
/list-commands core
/list-commands consultation
/list-commands research
```
Filter commands by specific category.

### Get Help for Specific Command
After finding a command, get detailed help:
```
/help deep-discovery
/help discover-project
```

## Command Status Indicators

- ✅ **Fully Integrated** - Command is wired to backend and tested
- ⚠️ **Partially Integrated** - Command works but missing some features
- 🔧 **In Development** - Command structure exists but not fully functional
- 📝 **Documentation Only** - Command documented but not implemented

## Current Integration Status

### Fully Integrated (✅)
- `/discover-project` - Integrated with research backend
- `/generate-commands` - Integrated with command-forge backend
- `/validate-integration` - Validation script functional

### Partially Integrated (⚠️)
- `/deep-discovery` - Orchestration partially complete
- `/consult-interactive` - Backend exists, integration pending
- `/manage-session-state` - Infrastructure exists, needs wiring

### In Development (🔧)
- `/generate-context` - Backend exists, not integrated
- `/develop-agents` - Agent factory exists, not wired
- `/coordinate-agents` - Orchestration pending

## Quick Start Sequence

For new users, we recommend this sequence:
1. `/welcome` - Get oriented
2. `/deep-discovery start` - Begin consultation
3. `/discover-project` - Analyze your project
4. `/generate-commands` - Create custom commands

## Need More Information?

- Check `PROJECT-STATE-VERIFICATION.md` for detailed status
- Review `CLAUDE.md` for system documentation
- Run `/help [command]` for specific command help

---
*Use `/welcome` if you're just getting started!*