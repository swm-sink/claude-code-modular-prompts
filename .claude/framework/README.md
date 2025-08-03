# Claude Code Context Engineering Framework

## 📦 Stage 2: Git Submodule Content

This directory contains the core framework that will be distributed as a git submodule. It provides a research-driven context engineering system for Claude Code projects.

## Structure

### /agents/
5 specialized agents for context engineering:
- `context-engineer.md` - Manages context structures
- `research-validator.md` - Validates sources and evidence
- `pattern-extractor.md` - Extracts patterns from codebases
- `discovery-navigator.md` - Helps find relevant context
- `integration-assistant.md` - Assists with framework integration

### /commands/
35 numbered scaffolding commands organized by phase:
- `-1_context/` - Context engineering foundation (5 commands)
- `0_verify/` - Environment verification (3 commands)
- `1_research/` - Research-driven patterns (5 commands)
- `2_context/` - Context engineering (5 commands)
- `3_agent/` - Agent architecture (5 commands)
- `4_command/` - Command engineering (3 commands)
- `5_integrate/` - Integration & validation (4 commands)
- `6_team/` - Team collaboration (2 commands)
- `7_maintain/` - Continuous improvement (2 commands)

### /context/
Framework context templates:
- `templates/` - Reusable context patterns
- `research/` - Research protocols and templates
- `validation/` - VERIFY protocol implementation

### /docs/
Developer documentation:
- `DEVELOPER_GUIDE.md` - How to use the framework
- `MODE_DETECTION.md` - Understanding execution modes
- `TROUBLESHOOTING.md` - Common issues and solutions
- `ENVIRONMENT_VARIABLES.md` - Variable reference

## Usage

When included as a git submodule in a parent project:

```bash
cd your-project
git submodule add https://github.com/USER/claude-code-modular-prompts.git .claude-context
cd .claude-context
./setup.sh
```

Then follow the numbered commands starting with Phase -1 to build your context engineering system.