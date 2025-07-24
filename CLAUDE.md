# Claude Code Modular Prompts

50 curated commands for Claude Code, with 90% test coverage.

## Current Structure
```
/
├── .claude/
│   ├── commands/     # 63 curated commands
│   ├── components/   # Reusable prompt components
│   ├── context/      # Engineering guides & anti-patterns
│   └── templates/    # Command templates
├── .main.archive/    # ARCHIVED - Original tallinn content
└── tests/            # Target: 90% coverage (currently: 0%)
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
| MD files | 169 | <50 | 🔄 50% reduction |
| Commands | 63 | 50 | ✅ Near target |
| Test coverage | 0% | 90% | 🔄 Next phase |
| Max dir depth | 3 | 3 | ✅ Achieved |

## Context Engineering
- Principles: `.claude/context/principles.md`
- Anti-patterns: `.claude/context/llm-antipatterns.md`
- Git History Lessons: `.claude/context/git-history-antipatterns.md`
- Development: `.claude/context/development.md`
- Commands: `.claude/context/commands.md`