# Docs vs Examples Consolidation Archive

| consolidation_date | reason | status |
|-------------------|---------|--------|
| 2025-07-16 | Eliminate redundancy - choose single source of truth | complete |

## Consolidation Strategy

**Problem**: Docs and examples contained identical command documentation with ~95% content overlap, violating the "MAKE THIS SIMPLER NOT ADD MORE TO MAINTAIN" directive.

**Solution**: Keep examples/ as PRIMARY learning resource (hands-on, practical), eliminate redundant docs/commands/, redirect all references.

## Files Moved to Archive

### docs/user-guide/commands/ (entire directory)
- `README.md` - Command overview (redundant with examples)
- `auto-command.md` - Identical to examples/01-beginner/basic-commands/auto-command.md
- `task-command.md` - Identical to examples/01-beginner/basic-commands/task-command.md  
- `query-command.md` - Identical to examples/01-beginner/basic-commands/query-command.md
- `feature-command.md` - Redundant with examples/02-intermediate/multi-command-workflows/feature-development.md

## New Single Source of Truth

### Command Documentation → examples/01-beginner/basic-commands/
- `auto-command.md` - Hands-on intelligent routing example
- `task-command.md` - Hands-on focused development example
- `query-command.md` - Hands-on research and analysis example

### Workflow Documentation → examples/02-intermediate/multi-command-workflows/
- `feature-development.md` - Complete feature development workflow
- `bug-investigation.md` - Systematic bug fixing workflow
- `refactoring-workflow.md` - Code improvement workflow

## References Updated

All README files updated to point to examples/ instead of docs/commands/:
- `docs/README.md`
- `docs/user-guide/README.md` 
- `README.md`

## Result

- **Eliminated**: 5 redundant files (4 command docs + 1 overview)
- **Reduced maintenance burden**: Single source of truth for command documentation
- **Improved user experience**: All learning resources in examples/ with hands-on approach
- **Maintained**: Reference docs (API reference, troubleshooting, FAQ, advanced config)

This consolidation implements the user's directive to focus on "THE 20% THAT PROVIDES 80% VALUE" by eliminating redundant documentation while preserving the most valuable learning resources.