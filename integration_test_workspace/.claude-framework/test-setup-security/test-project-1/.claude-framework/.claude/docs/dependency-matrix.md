# File Dependency Matrix & Source of Truth Analysis

## 📊 Discovery Summary

### Directory Structure Analysis
| Directory | Files | Commands | Python Scripts | Tests | Status |
|-----------|-------|----------|----------------|-------|--------|
| `.claude/` | 2 | 0 | 0 | 0 | **New/Empty** |
| `.main/` | 1,159 | 171 | 2 | 0 | **Archive/Legacy** |
| `tallinn/` | 997 | 318 (147+171) | 85 | 27 | **Active Development** |

### Command Repository Analysis
| Repository | Count | Type | Notes |
|------------|-------|------|-------|
| `tallinn/.claude/commands` | 147 | **Simplified/Modern** | Claude Code compliant |
| `tallinn/claude_prompt_factory/commands` | 171 | **Legacy/Modified** | XML-based, evolved from .main |
| `.main/claude_prompt_factory/commands` | 171 | **Legacy/Original** | XML-based, original version |

### Key Findings
1. **Command Evolution**: `.main` → `tallinn/claude_prompt_factory` → `tallinn/.claude` (simplification process)
2. **Active Development**: `tallinn/` has comprehensive testing (27 test files)
3. **Documentation Bloat**: 70 README files across project
4. **Configuration Redundancy**: 4 settings.json files with minimal differences

## 🎯 Source of Truth Determination

### Commands
- **Primary Source**: `tallinn/.claude/commands` (147 files - newest, Claude Code compliant)
- **Secondary Source**: `tallinn/claude_prompt_factory/commands` (171 files - has additional legacy commands)
- **Archive**: `.main/claude_prompt_factory/commands` (171 files - original baseline)

### Components
- **Primary Source**: `tallinn/claude_prompt_factory/components` (most comprehensive)
- **Archive**: `.main/claude_prompt_factory/components` (original baseline)

### Tests
- **Primary Source**: `tallinn/tests/` (27 test files - comprehensive coverage)
- **No tests in other directories**

### Python Scripts
- **Primary Source**: `tallinn/scripts/` (comprehensive utility collection)
- **Minimal**: `.main/` has only 2 Python files

### Configuration
- **Target**: `.claude/settings.local.json` (project root - proper location)
- **Sources**: Multiple scattered settings files to consolidate

### Documentation
- **Target**: Root level README.md, CLAUDE.md
- **Problem**: 70+ scattered documentation files need consolidation

## 📈 Dependency Relationships

### Command Dependencies
```
tallinn/.claude/commands (147) 
    ├── Depends on: tallinn/claude_prompt_factory/components
    ├── References: tallinn/scripts utilities
    └── Tested by: tallinn/tests

tallinn/claude_prompt_factory/commands (171)
    ├── Depends on: tallinn/claude_prompt_factory/components  
    ├── Legacy XML format
    └── Source for: tallinn/.claude/commands (simplified versions)

.main/claude_prompt_factory/commands (171)
    ├── Original baseline
    ├── Legacy XML format
    └── Source for: tallinn/claude_prompt_factory/commands (modified versions)
```

### Component Dependencies
```
tallinn/claude_prompt_factory/components
    ├── Used by: All command repositories
    ├── Contains: Reusable prompt patterns
    └── Most comprehensive collection

.main/claude_prompt_factory/components
    ├── Original baseline
    └── Subset of tallinn components
```

### Test Dependencies
```
tallinn/tests/
    ├── Tests: tallinn/.claude/commands
    ├── Tests: tallinn/claude_prompt_factory functionality
    ├── Uses: tallinn/test_data
    └── Coverage: ~19% (needs improvement)
```

## 🧠 Tree-of-Thought Decision Framework

### Evaluation Criteria
1. **Claude Code Compliance**: Must follow official best practices
2. **Maintainability**: Clean, organized, well-documented
3. **Performance**: Fast loading, efficient context usage
4. **Security**: Defensive patterns, input validation
5. **Completeness**: Comprehensive command coverage
6. **Test Coverage**: >80% test coverage target

### Migration Strategy Options

#### Option A: Selective Merge
- Migrate best 50-70 commands from `tallinn/.claude/commands`
- Supplement with valuable commands from `tallinn/claude_prompt_factory/commands`
- Archive `.main/` and legacy `tallinn/claude_prompt_factory/`

#### Option B: Complete Modernization
- Start fresh with root `.claude/` structure
- Systematically migrate and modernize all valuable commands
- Implement comprehensive TDD from ground up

#### Option C: Hybrid Approach
- Use `tallinn/.claude/commands` as foundation (already Claude Code compliant)
- Selectively integrate missing functionality from legacy sources
- Maintain backward compatibility during transition

## 🎯 Recommended Source of Truth

| Component Type | Primary Source | Rationale |
|----------------|----------------|-----------|
| **Commands** | `tallinn/.claude/commands` | Claude Code compliant, most recent |
| **Components** | `tallinn/claude_prompt_factory/components` | Most comprehensive |
| **Tests** | `tallinn/tests/` | Only comprehensive test suite |
| **Scripts** | `tallinn/scripts/` | Active development utilities |
| **Documentation** | Consolidate to root | Clean structure |
| **Configuration** | Root `.claude/` | Proper Claude Code location |

---
*Generated: 2025-07-23*
*Status: Analysis Complete*
*Next: Tree-of-Thought Strategy Selection*