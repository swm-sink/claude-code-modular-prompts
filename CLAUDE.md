# Claude Code Modular Prompts

**Experimental** Claude Code library with 67 slash commands and comprehensive agent orchestration for prompt engineering research.

## Current Structure
```
/
├── .claude/
│   ├── commands/     # 67 commands (all unique, no duplicates)
│   ├── components/   # 85 reusable prompt components
│   ├── context/      # Engineering guides & anti-patterns
│   └── templates/    # Command templates
├── .main.archive/    # ARCHIVED - Original tallinn content (332 files)
└── tests/            # MISSING - Target: 90% coverage (currently: 0%)
```

## Immutable Rules
1. Maximum 3 directory levels
2. No new files in .main.archive (archived content)
3. Tests before implementation (experimental validation focus)
4. No duplicate commands (each must be unique)
5. One atomic commit per task
6. **PARANOIA MANDATE**: Triple-check everything before commits
   - Verify no sensitive data (keys, tokens, passwords)
   - Check all file paths are correct
   - Validate directory structure integrity
   - Ensure .claude is never in .gitignore
   - Scan for accidental duplicates or leftovers

## Status
| Metric | Current | Target | Progress |
|--------|---------|--------|----------|
| MD files | 178 active | <50 | ❌ Need 128+ reduction |
| Commands | 67 | 67 unique | ✅ No duplicates found |
| Test coverage | 0% | 90% | ❌ Experimental validation needed |
| Max dir depth | 3 | 3 | ✅ Achieved |

## Experimental Framework Notice
This is an **experimental prompt engineering framework** for research and development:
- Performance benchmarks are not required
- Focus is on prompt effectiveness, not execution speed
- Commands are tested for correctness, not performance
- All 75 commands are maintained as unique implementations

## Context Engineering

### ⚠️ MANDATORY CONTEXT LOADING
**CRITICAL**: The following context file MUST be loaded for all Claude Code sessions:
- **Git History Anti-Patterns**: `.claude/context/git-history-antipatterns.md` 
  - Documents 10 severe LLM anti-patterns from 500+ commits
  - REQUIRED to prevent: theatrical commits, fake metrics, reorganization addiction
  - Load this FIRST before any development work

### Additional Context Files
- Principles: `.claude/context/principles.md`
- Anti-patterns: `.claude/context/llm-antipatterns.md`
- Development: `.claude/context/development.md`
- Commands: `.claude/context/commands.md`