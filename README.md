# The Claude Code Prompt Factory

**A modular, configurable, and comprehensive library of prompt-based commands that feel native to the Claude Code environment.**

This repository provides a powerful toolkit of generalized, prompt-based commands that can be easily adapted to any project through a central `PROJECT_CONFIG.xml` file. It is not a coded framework; it is a factory for producing high-quality, reusable commands that extend the capabilities of Claude Code.

## 🚀 Core Principles

*   **Modular**: Commands are built from reusable components, ensuring consistency and maintainability.
*   **Configurable**: A central `PROJECT_CONFIG.xml` file allows you to tailor every command to your project's specific tech stack and needs.
*   **Consistent**: All commands follow a standard, predictable XML structure, making them easy to understand and modify.
*   **Transparent**: The prompts are open, readable, and designed to be improved by the user.

## ✨ Key Features

*   **Intelligent Onboarding**: Use `/init existing` to automatically scan your project and generate a tailored configuration.
*   **Autonomous Agents**: Leverage powerful agents like `/agent refactor` or `/agent research` to perform complex, multi-step tasks.
*   **Configurable Safety Protocol**: The `/protocol` command provides a rigorous, step-by-step execution engine for safe, high-stakes changes.
*   **Extensible by Design**: Create your own commands and components to extend the factory.

## 📁 The Prompt Factory

The heart of the project is the `claude_prompt_factory` directory. The central index of all command categories can be found at `claude_prompt_factory/commands/CLAUDE.md`.

## 🔧 Getting Started

1.  **Copy the `claude_prompt_factory` directory** to your project's `.claude` directory.
2.  **Run `/init existing` or `/init new`** to generate your `PROJECT_CONFIG.xml`.
3.  **Explore the available commands** starting with `claude_prompt_factory/commands/CLAUDE.md`.
4.  **Start using the commands!**

For a detailed guide, see the [GETTING_STARTED.md](docs/GETTING_STARTED.md) file.

## 🤝 Contributing

This is an open-source project, and we welcome contributions! If you have a command that you think would be a great addition to the "Prompt Factory," please see our [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) for instructions on how to contribute.