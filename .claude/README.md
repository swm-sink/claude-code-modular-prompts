# .claude Directory - Optimized Framework Structure

**Version**: 2.0.0 | **Files**: ~35 (from 157) | **Token-Optimized**: All files <20k tokens

## 📁 Directory Structure

```
.claude/
├── commands/       # 10 core commands (from 33)
├── rules/          # 6 focused rules (from 24)
├── settings/       # 4 config files (from 163KB single file)
├── archive/        # Legacy content for reference
└── README.md       # This file
```

## 🚀 Core Commands

| Command | Purpose | Absorbs |
|---------|---------|---------|
| `/auto` | Intelligent routing | Legacy command mapping |
| `/task` | General development | single-agent, bug-fix, etc. |
| `/swarm` | Multi-agent orchestration | lead_agent, batch |
| `/query` | Research without changes | - |
| `/test` | TDD enforcement | tdd, project:tdd |
| `/security` | Enterprise security | code-audit |
| `/fastapi` | API development | - |
| `/session` | GitHub issue tracking | - |
| `/protocol` | Production standards | production |
| `/commit` | Git operations | commit-and-push, release |

## 📏 Core Rules

1. **aware-framework.md** - The ONE cognitive process (AWARE)
2. **tdd-standards.md** - Test-driven development enforcement
3. **production-standards.md** - Quality, security, performance gates
4. **native-patterns.md** - Task() and Batch() usage
5. **honesty-policy.md** - Evidence-based claims only
6. **claude-code-integration.md** - Native tool usage

## ⚙️ Settings Structure

- **core.json** - Framework configuration
- **permissions.json** - Consolidated permission patterns
- **patterns.json** - Multi-agent and execution patterns
- **commands.json** - Command-specific settings

## 🔄 Migration from v1.x

### For Users
- Old commands still work via `/auto` routing
- 90-day deprecation warnings
- See `MIGRATION_MAPPING.md` for details

### For Developers  
- Update imports from `.claude/docs/` to `.claude/`
- Replace `spawn_agent` with Task() pattern
- Use new simplified rule names

## 🎯 Key Improvements

1. **75% fewer files** - Focused and maintainable
2. **Token-optimized** - All files under 20k tokens
3. **Reality-based** - No theoretical features
4. **Native patterns** - Actual Claude Code capabilities
5. **Clear purpose** - Each file has distinct role

## 📊 Framework Principles

### Cognitive Process
All operations follow AWARE:
- **A**ssess & Analyze
- **W**atch for Assumptions
- **A**rchitect the Approach
- **R**un with Verification
- **E**valuate & Evolve

### Multi-Agent Patterns
- **Task()** for specialized expertise
- **Batch()** for similar parallel work
- Native Claude Code support only

### Quality Standards
- TDD: Mandatory RED-GREEN-REFACTOR
- Security: Threat model first
- Performance: <200ms p95
- Coverage: 90% minimum

## 🚫 What's Removed

- Fantasy `spawn_agent` references
- Theoretical disaster recovery scripts
- Overlapping cognitive frameworks
- Meta-rules about rules
- Redundant commands
- 4,929 individual permissions → ~50 patterns

## 📚 Documentation

- **Commands**: See `/commands/*.md`
- **Rules**: See `/rules/*.md`
- **Migration**: See `MIGRATION_MAPPING.md`
- **Archive**: See `/archive/` for legacy content

---

*Built for Claude Code reality, not theoretical possibilities.*