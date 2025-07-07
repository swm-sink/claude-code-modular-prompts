# Claude Code Framework

## 1. Overview

This directory contains the core implementation of the Claude Code Framework, a modular system for workflow automation. The framework is designed around a principle of clear separation of concerns:

- **Commands (`commands/`):** Handle user-facing interactions and delegate tasks to modules. They should contain no direct implementation logic.
- **Modules (`modules/`):** Contain all the implementation details for specific functionalities. They are composed by commands to execute complex workflows.

This architecture ensures that the framework is modular, scalable, and easy to maintain.

## 2. Directory Structure

- **`.claude/commands/`**: This directory contains the core slash commands that serve as the primary entry points for user interactions. Each command is responsible for delegating tasks to the appropriate modules.

- **`.claude/modules/`**: This directory houses the reusable implementation modules, which are organized by category (e.g., `security`, `quality`, `development`). These modules provide the logic for all framework operations.

## 3. Guiding Principles

- **Delegation, Not Implementation:** Commands orchestrate, modules execute.
- **Zero Redundancy:** Every piece of logic has a single, authoritative source.
- **Modular Composition:** Complex behaviors are built by combining simple, focused modules.

Refer to the main `CLAUDE.md` file for the complete architectural philosophy and operational requirements. 