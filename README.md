# The Claude Code Prompt Factory

**A streamlined, modular prompt engineering framework for Claude Code that emphasizes simplicity and effectiveness over complexity.**

This repository provides a focused toolkit of well-crafted prompt-based commands that can be easily adapted to any project through a central `PROJECT_CONFIG.xml` file. It's designed for developers who want powerful AI assistance without complexity bloat.

## 🚀 Core Principles

*   **Simplicity First**: Each command has a single, focused purpose with minimal cognitive overhead
*   **Smart Routing**: The `/auto` command intelligently selects the best approach for any request
*   **Configurable**: Adapt all commands to your specific tech stack through one configuration file
*   **Effective**: Quality through focused execution, not feature proliferation

## ✨ Key Features

*   **Intelligent Onboarding**: Use `/existing` to automatically scan your project and generate configuration
*   **Smart Command Routing**: `/auto "your request"` analyzes intent and routes to optimal commands
*   **Safety Protocols**: The `/protocol` command provides rigorous workflows for critical changes
*   **Focused Commands**: Each command excels at its specific domain rather than trying to do everything

## 📁 Structure

The heart of the project is the `claude_prompt_factory` directory with organized command categories. The main index is at `claude_prompt_factory/CLAUDE.md`.

```
claude_prompt_factory/
├── CLAUDE.md                 # Main command index
├── commands/                 # All command categories
│   ├── agents/              # Autonomous multi-step agents
│   ├── core/                # Fundamental commands
│   ├── development/         # Development workflows
│   └── ...                  # Other categories
└── components/              # Reusable prompt components
```

## 🔧 Quick Start

1.  **Copy the framework** to your project's `.claude` directory:
    ```bash
    mkdir -p .claude
    cp -r claude_prompt_factory .claude/
    ```

2.  **Initialize for your project**:
    ```bash
    /existing    # For existing projects (auto-detects tech stack)
    # OR
    /new         # For new projects (guided setup)
    ```

3.  **Start using commands**:
    ```bash
    /auto "fix the login authentication issue"
    /task "create email validation utility"
    /query "how does user authentication work?"
    ```

## 🎯 Common Usage Patterns

- **Quick fixes**: `/auto "fix bug in user login"`
- **New features**: `/feature "add password reset functionality"`
- **Code analysis**: `/query "how does the payment system work?"`
- **Focused development**: `/task "create input validation helper"`
- **Critical changes**: `/protocol "refactor database connection logic"`

## 📖 Documentation

*   **[Getting Started Guide](docs/GETTING_STARTED.md)** - Detailed setup and first steps
*   **[Developer Guide](docs/DEVELOPER_GUIDE.md)** - Creating custom commands
*   **[Command Reference](claude_prompt_factory/CLAUDE.md)** - All available commands

## 🤝 Contributing

We welcome contributions that align with our **simplicity first** philosophy. Before adding new commands, consider:

1. Does this solve a focused, specific problem?
2. Can existing commands be improved instead?
3. Does it follow our established patterns?

See [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) for contribution guidelines.

---
*Built on the principle that the best AI tools are simple, focused, and intelligently designed rather than feature-heavy.*