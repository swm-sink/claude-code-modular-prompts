# Transformation Directory

## ⚠️ IMPORTANT: Stage 1 Only

This directory contains tools and state specific to transforming the Claude Code Modular Prompts project. It is:

- **NOT included** in the git submodule
- **Temporary** - will be removed after transformation
- **Stage 1 specific** - only for THIS project's transformation

## Contents

### /agents/
Transformation-specific agents that orchestrate the 6-week transformation process:
- `transformation-orchestrator.md` - Master coordinator
- `migration-specialist.md` - Converts 88 → 35 commands
- `cleanup-coordinator.md` - Removes obsolete files

### /commands/
Transformation utilities:
- `backup_existing.sh` - Creates timestamped backups
- Migration scripts (to be added)

### /context/
Transformation state and progress:
- Current analysis results
- Migration mappings
- Progress tracking

### /tests/
Tests for transformation tools:
- Mode detection tests
- Migration validation

## Marker Files

- `active` - Indicates transformation mode is active
- `MODE` - Backup mode indicator

## Usage

These tools are used during the 6-week transformation process. Once complete, this entire directory can be removed.