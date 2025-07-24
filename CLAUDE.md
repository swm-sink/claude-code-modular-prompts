# Claude Code Modular Prompts

50 curated commands for Claude Code, with 90% test coverage.

## Current Structure
```
/
├── .claude/
│   ├── commands/     # 50 commands (currently: 171)
│   ├── context/      # Engineering guides
│   └── settings.json # Tool permissions
├── .main/            # TO BE REMOVED - duplicate of everything
└── tests/            # Target: 90% coverage (currently: 0%)
```

## Immutable Rules
1. Maximum 3 directory levels
2. No files in .main (remove entire directory)
3. Tests before implementation
4. Commands execute in <100ms
5. One atomic commit per task

## Status
| Metric | Current | Target |
|--------|---------|--------|
| MD files | 341 | <50 |
| Commands | 171 | 50 |
| Test coverage | 0% | 90% |
| Max dir depth | 6+ | 3 |

## Context Engineering
- Principles: `.claude/context/principles.md`
- Anti-patterns: `.claude/context/llm-antipatterns.md`
- Development: `.claude/context/development.md`
- Commands: `.claude/context/commands.md`