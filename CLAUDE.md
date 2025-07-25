# Claude Code Modular Prompts

Production Claude Code library with 75 slash commands and comprehensive agent orchestration.

## Current Structure
```
/
├── .claude/
│   ├── commands/     # 75 commands (target: 50)
│   ├── components/   # 85 reusable prompt components
│   ├── context/      # Engineering guides & anti-patterns
│   └── templates/    # Command templates
├── .main.archive/    # ARCHIVED - Original tallinn content (332 files)
└── tests/            # MISSING - Target: 90% coverage (currently: 0%)
```

## Immutable Rules
1. Maximum 3 directory levels
2. No new files in .main.archive (archived content)
3. Tests before implementation
4. Commands execute in <100ms
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
| Commands | 75 | 50 | ❌ Need 25 reduction |
| Test coverage | 0% | 90% | ❌ Tests missing |
| Max dir depth | 4 | 3 | ❌ VIOLATION - 1 level over |

## Context Engineering
- Principles: `.claude/context/principles.md`
- Anti-patterns: `.claude/context/llm-antipatterns.md`
- Git History Lessons: `.claude/context/git-history-antipatterns.md`
- Development: `.claude/context/development.md`
- Commands: `.claude/context/commands.md`