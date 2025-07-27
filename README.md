# Claude Code Modular Prompts

An experimental library of consolidated slash commands for Claude Code, with prompt engineering components and documented anti-pattern examples.

## Quick Start

This repository contains Claude Code commands that have been consolidated from a larger original set. The project includes 79 commands that have been organized into 30 active commands plus 49 deprecated commands with migration paths.

## 📁 Structure

```
/
├── .claude/
│   ├── commands/     # 30 active commands
│   │   ├── deprecated/   # 49 archived commands with migration paths
│   │   ├── core/         # Essential commands (task, query, auto)
│   │   ├── quality/      # Testing and quality commands
│   │   ├── specialized/  # Security and database commands
│   │   └── development/  # Development and project commands
│   ├── components/   # 63 reusable prompt components
│   ├── context/      # Engineering guides & anti-patterns
│   └── templates/    # Command templates
└── tests/            # Test suite (experimental validation)
```

## Key Features

- **30 Active Commands**: Consolidated from original 79 commands
- **63 Reusable Components**: Prompt engineering patterns
- **49 Deprecated Commands**: Migration paths provided
- **Anti-Pattern Documentation**: Documented examples and lessons
- **Structured Organization**: Clear directory hierarchy
- **Experimental Framework**: Research-focused command design

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

## Quality Standards

- Maximum 3-level directory nesting
- Component reuse where applicable
- Anti-pattern documentation included
- Security considerations documented

## 📖 Documentation

- **Framework Guide**: `.claude/context/experimental-framework-guide.md`
- **Anti-patterns**: `.claude/context/llm-antipatterns.md`
- **Git History Lessons**: `.claude/context/git-history-antipatterns.md`
- **Best Practices**: `.claude/context/prompt-engineering-best-practices.md`
- **Components**: `.claude/context/modular-components.md`
- **Orchestration**: `.claude/context/orchestration-patterns.md`
- **Quality Report**: `.claude/context/quality-assessment-report.md`

## Important Notes

- No sensitive data (keys, tokens, passwords) in this repository
- Commands have structural validation only
- Follows Claude Code structure conventions
- Includes anti-pattern documentation and examples

## 🤝 Contributing

See CLAUDE.md for development guidelines and the PARANOIA MANDATE for security requirements.

## 📄 License

See .main.archive/LICENSE for license information.

---

*Experimental prompt engineering framework with documented anti-pattern examples.*