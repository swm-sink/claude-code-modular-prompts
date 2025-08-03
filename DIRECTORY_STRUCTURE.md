# Directory Structure

## Claude Code Context Engineering Framework

This document describes the dual-purpose directory structure that supports both Stage 1 (transformation) and Stage 2 (framework) operations.

```
cairo/                              # Project root
├── .transformation/                # Stage 1 only (NOT in git submodule)
│   ├── active                     # Marker file for transformation mode
│   ├── agents/                    # Transformation-specific agents
│   │   ├── transformation-orchestrator.md
│   │   ├── migration-specialist.md
│   │   └── cleanup-coordinator.md
│   ├── commands/                  # Transformation utilities
│   │   └── backup_existing.sh    # Backup script
│   ├── context/                   # Transformation state and progress
│   ├── tests/                     # Transformation tests
│   │   ├── test_mode_detection.sh
│   │   └── test_integration.sh
│   └── README.md                  # Transformation documentation
│
├── .claude/                       # Claude Code configuration
│   ├── framework/                 # Stage 2 content (IN git submodule)
│   │   ├── agents/               # 5 framework agents
│   │   │   ├── context-engineer.md
│   │   │   ├── research-validator.md
│   │   │   ├── pattern-extractor.md
│   │   │   ├── discovery-navigator.md
│   │   │   └── integration-assistant.md
│   │   ├── commands/             # 35 numbered scaffolding commands
│   │   │   ├── -1_context/      # Context foundation (5 commands)
│   │   │   ├── 0_verify/        # Environment verification (3 commands)
│   │   │   ├── 1_research/      # Research patterns (5 commands)
│   │   │   ├── 2_context/       # Context engineering (5 commands)
│   │   │   ├── 3_agent/         # Agent architecture (5 commands)
│   │   │   ├── 4_command/       # Command engineering (3 commands)
│   │   │   ├── 5_integrate/     # Integration (4 commands)
│   │   │   ├── 6_team/          # Team collaboration (2 commands)
│   │   │   └── 7_maintain/      # Maintenance (2 commands)
│   │   ├── context/              # Framework context templates
│   │   │   ├── templates/       # Reusable patterns
│   │   │   ├── research/        # Research protocols
│   │   │   └── validation/      # VERIFY protocol
│   │   ├── docs/                # Framework documentation
│   │   │   ├── DEVELOPER_GUIDE.md
│   │   │   ├── MODE_DETECTION.md
│   │   │   ├── TROUBLESHOOTING.md
│   │   │   └── ENVIRONMENT_VARIABLES.md
│   │   └── README.md            # Framework overview
│   │
│   └── project/                  # Preserved existing content
│       ├── commands/             # Original 88 commands
│       ├── components/           # Original 96 components
│       ├── context/              # Original context files
│       └── [other existing dirs] # All original content
│
├── .submodule/                    # Integration helpers (IN git submodule)
│   ├── detect_mode.sh            # Core mode detection script
│   ├── setup.sh                  # Setup for parent projects
│   ├── templates/                # Integration templates
│   │   ├── .gitmodules.template
│   │   └── .gitignore.template
│   └── README.md                 # Integration documentation
│
└── [project files]               # Your existing project files
```

## Directory Purposes

### .transformation/ (Stage 1 Only)
- **Purpose**: Contains transformation-specific tools and state
- **Lifetime**: Temporary, removed after 6-week transformation
- **In Submodule**: NO - specific to THIS project's transformation
- **Contents**: Migration agents, backup tools, progress tracking

### .claude/framework/ (Stage 2 Content)
- **Purpose**: The new research-driven framework
- **Lifetime**: Permanent, distributed via git submodule
- **In Submodule**: YES - this is what other projects receive
- **Contents**: 35 commands, 5 agents, context templates

### .claude/project/ (Preserved Content)
- **Purpose**: Original Claude Code Modular Prompts content
- **Lifetime**: During transformation only
- **In Submodule**: NO - being transformed/migrated
- **Contents**: 88 commands, 96 components, original context

### .submodule/ (Integration Layer)
- **Purpose**: Enables dual-mode operation
- **Lifetime**: Permanent
- **In Submodule**: YES - needed for integration
- **Contents**: Mode detection, setup scripts, templates

## Mode-Specific Access

### In Transformation Mode
Can access:
- ✅ .transformation/
- ✅ .claude/framework/
- ✅ .claude/project/
- ✅ .submodule/

### In Framework Mode (as submodule)
Can access:
- ❌ .transformation/ (not included)
- ✅ .claude/framework/
- ❌ .claude/project/ (not included)
- ✅ .submodule/

## Key Files

### Mode Detection
- `.transformation/active` - Presence indicates transformation mode
- `.submodule/detect_mode.sh` - Detects and configures mode

### Entry Points
- `.submodule/setup.sh` - Initial setup for parent projects
- `.transformation/commands/backup_existing.sh` - Backup utility

### Documentation
- `DIRECTORY_STRUCTURE.md` - This file
- `.claude/framework/docs/` - Framework documentation
- `.transformation/README.md` - Transformation guide

## Environment Variables

Set by `.submodule/detect_mode.sh`:

| Variable | Purpose |
|----------|---------|
| `CLAUDE_MODE` | Current mode (transformation/framework) |
| `CLAUDE_ROOT` | Root of Claude system |
| `CLAUDE_SCOPE` | Project being operated on |
| `CLAUDE_CONTEXT_DIR` | Active context directory |

## Integration Flow

### For Parent Projects (Stage 2)
```bash
parent-project/
├── .claude-context/              # Git submodule
│   ├── .claude/framework/       # Framework content
│   └── .submodule/              # Integration scripts
└── [parent project files]
```

### During Transformation (Stage 1)
All directories present, transformation tools active.

## File Patterns

### Included in Git Submodule
```
.claude/framework/**
.submodule/**
LICENSE
README.md
```

### Excluded from Git Submodule
```
.transformation/**
.claude/project/**
.backup_*
*.log
```

## Maintenance Notes

1. **Never commit** `.transformation/` to submodule
2. **Always preserve** `.submodule/` for mode detection
3. **Framework commands** must use `detect_mode.sh`
4. **Backup before** major structural changes

This structure enables the same codebase to transform itself (Stage 1) and then serve as a framework for other projects (Stage 2).