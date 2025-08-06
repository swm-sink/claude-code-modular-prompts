# Migration to claude.todos.yaml - Single Source of Truth

## Summary of Changes (2025-08-05)

### What Changed
- **CONSOLIDATED**: `claude.local.md` + `claude.todos.md` → `claude.todos.yaml`
- **FORMAT**: Changed from Markdown to YAML for better agent operations
- **LOCATION**: All orchestration now in single `claude.todos.yaml` file

### Why YAML?
| Aspect | Markdown | JSON | YAML |
|--------|----------|------|------|
| Human Readable | ✅ Excellent | ⚠️ OK | ✅ Good |
| Machine Parse | ❌ Hard | ✅ Fast | ✅ Good |
| Atomic Updates | ❌ Risky | ✅ Good | ✅ Good |
| Comments | ✅ Yes | ❌ No | ✅ Yes |
| Git Diffs | ✅ Good | ⚠️ OK | ✅ Good |

**YAML provides the optimal balance for agent orchestration.**

## Migration Actions Taken

### 1. Created New File
- `claude.todos.yaml` - Consolidated single source of truth
- Contains all 104 tasks with full context
- Includes orchestration state, protocols, and metrics

### 2. Updated CLAUDE.md
- Changed all references from `claude.local.md` to `claude.todos.yaml`
- Added enforcement for single source of truth
- Explained YAML format benefits

### 3. Archived Old Files
- `claude.local.md` → `.archive-integration-approach/claude.local.md.archived`
- `claude.todos.md` → `.archive-integration-approach/claude.todos.md.archived`

## For Agents: What You Need to Know

### Old Workflow (DEPRECATED)
```
1. Read CLAUDE.md
2. Read claude.local.md
3. Read claude.todos.md
4. Synchronize between files
```

### New Workflow (CURRENT)
```
1. Read CLAUDE.md (for rules)
2. Read claude.todos.yaml (for EVERYTHING else)
3. Update claude.todos.yaml atomically
```

## Key Sections in claude.todos.yaml

```yaml
orchestration:     # Current state and progress
transformation:    # Vision and context
phases:           # All 104 tasks organized by phase
  phase_1:
    tasks:
      1-11:       # Each task with full details
protocols:        # How to claim, update, complete tasks
agent_context:    # Instructions for different agent types
files:            # Tracking created/moved files
validation:       # Gate criteria
metrics:          # Performance tracking
```

## Agent Instructions

### Task Claiming (YAML format)
```yaml
# Find your task
phases:
  phase_1:
    tasks:
      7:
        status: "pending"  # Change to "in_progress"
        assigned_to: "your-agent-id"  # Add your ID
        started_at: "2025-08-05T22:00:00Z"  # Add timestamp
```

### Progress Updates
```yaml
7:
  status: "in_progress"
  progress: 50
  last_updated: "2025-08-05T22:05:00Z"
  current_action: "Running TDD tests"
```

### Task Completion
```yaml
7:
  status: "complete"
  completed_at: "2025-08-05T22:10:00Z"
  commit: "abc123"
  outcome:
    moved_from: "scripts/invoke-agent.sh"
    moved_to: ".archive-integration-approach/scripts/invoke-agent.sh"
```

## Benefits of Consolidation

1. **No Synchronization Issues**: Single file = single truth
2. **Atomic Operations**: YAML supports safe concurrent updates
3. **Better Organization**: Everything in one structured place
4. **Cleaner Git History**: One file to track changes
5. **Faster Agent Operations**: No multi-file reads
6. **Human Friendly**: YAML is readable with comments

## Rollback Plan (If Needed)

If we need to rollback:
1. Archived files are in `.archive-integration-approach/`
2. Git history has all previous versions
3. Can restore with: `git checkout HEAD~1 -- claude.local.md`

## Verification

Check the new system is working:
```bash
# Verify YAML is valid
python -c "import yaml; yaml.safe_load(open('claude.todos.yaml'))"

# Check task count
grep "description:" claude.todos.yaml | wc -l  # Should be 104

# Verify no old files
ls claude.local.md 2>/dev/null || echo "✅ Old file removed"
ls claude.todos.md 2>/dev/null || echo "✅ Old file removed"
```

## Questions?

The consolidated `claude.todos.yaml` is now the ONLY place for:
- Task definitions and status
- Orchestration state
- Progress tracking
- Agent coordination
- File tracking
- Metrics and validation

**DO NOT** create any other tracking files. Everything goes in `claude.todos.yaml`.