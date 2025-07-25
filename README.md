# Claude Code Modular Prompts

A production-ready library of 63 curated slash commands for Claude Code, with comprehensive prompt engineering components and anti-pattern prevention.

## 🚀 Quick Start

This repository contains high-quality, tested commands for Claude Code that follow best practices and avoid common LLM anti-patterns.

## 📁 Structure

```
/
├── .claude/
│   ├── commands/     # 63 curated slash commands
│   ├── components/   # 81 reusable prompt components
│   ├── context/      # Engineering guides & anti-patterns
│   └── templates/    # Command templates
└── tests/            # Test suite (90% coverage target)
```

## 🎯 Key Features

- **63 Curated Commands**: Carefully selected and validated
- **81 Reusable Components**: DRY prompt engineering
- **Anti-Pattern Prevention**: Documented lessons from 200+ commits
- **Quality Validated**: All commands pass validation
- **Production Ready**: Clean structure, no sensitive data

## 📋 Command Categories

- **Core** (7): Essential commands like `/task`, `/query`, `/auto`
- **Development** (7): `/debug`, `/refactor`, `/build`, etc.
- **Security** (5): `/secure-assess`, `/secure-manage`, etc.
- **Testing** (2): `/test` (unified testing), `/test-e2e` (browser automation)
- **Analysis** (10): `/analyze-code`, `/analyze-system`, etc.
- **Database** (4): `/db-admin`, etc.
- **Deployment** (6): `/deploy`, `/ci-setup`, etc.
- **Utilities** (8): `/help`, `/project`, `/dev`, etc.
- **Workflow** (7): `/project`, `/pipeline`, etc.
- **Monitoring** (3): `/monitor`, etc.

## 🛡️ Quality Standards

- Maximum 3-level directory nesting
- Commands execute in <100ms
- Comprehensive component reuse
- Anti-pattern prevention built-in
- Security-first design

## 📖 Documentation

- **Principles**: `.claude/context/principles.md`
- **Anti-patterns**: `.claude/context/llm-antipatterns.md`
- **Git History Lessons**: `.claude/context/git-history-antipatterns.md`
- **Development Guide**: `.claude/context/development.md`
- **Command Reference**: `.claude/context/commands.md`

## 🚨 Important Notes

- No sensitive data (keys, tokens, passwords) in this repository
- All commands validated with included validation script
- Follows Claude Code best practices
- Includes comprehensive anti-pattern documentation

## 🤝 Contributing

See CLAUDE.md for development guidelines and the PARANOIA MANDATE for security requirements.

## 📄 License

See .main.archive/LICENSE for license information.

---

*Built with lessons learned from 200+ commits of LLM anti-pattern examples.*