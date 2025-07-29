# The Claude Code Prompt Factory

**A streamlined, modular prompt engineering framework that enhances Claude Code with intelligent, reusable commands.**

## Quick Start

*   **New to the factory?** Start with `/auto "your request"` - it intelligently routes to the best command
*   **Existing project?** Run `/existing` to auto-configure for your codebase
*   **Need help?** Use `/help` for guidance or explore the command categories below

## Core Commands

*   **`/auto "[request]"`** - Smart router that selects optimal commands for your needs
*   **`/task "[description]"`** - Focused TDD workflow for single components
*   **`/feature "[description]"`** - End-to-end feature development
*   **`/protocol "[description]"`** - Safe, rigorous workflow for critical changes
*   **`/query "[question]"`** - Analyze and understand your codebase

## Command Categories

### 🤖 **[Agents](./commands/agents/README.md)**
High-level autonomous agents for complex, multi-step tasks.

### 🔍 **[Analysis](./commands/analysis/README.md)**
Code analysis, quality checks, and pattern recognition.

### 🌐 **[API](./commands/api/README.md)**
API design, testing, and management tools.

### 🧠 **[Context](./commands/context/README.md)**
Prime Claude's understanding of your codebase.

### ⚙️ **[Core](./commands/core/README.md)**
Fundamental commands for initialization and routing.

### 🗄️ **[Database](./commands/database/README.md)**
Database management, migration, and seeding.

### 🚀 **[Deployment](./commands/deployment/README.md)**
CI/CD, deployment, and rollback automation.

### 💻 **[Development](./commands/development/README.md)**
Development acceleration and workflow optimization.

### 📚 **[Documentation](./commands/documentation/README.md)**
Automated documentation generation and management.

### 🚨 **[Error Handling](./commands/error/README.md)**
Robust error management and recovery patterns.

### 🔧 **[Git](./commands/git/README.md)**
Intelligent git operations and workflow automation.

### 🔄 **[Meta](./commands/meta/README.md)**
Framework self-improvement and optimization.

### 📊 **[Monitoring](./commands/monitoring/README.md)**
Application monitoring and observability setup.

### ⚡ **[Performance](./commands/performance/README.md)**
Performance optimization and benchmarking.

### 🔐 **[Security](./commands/security/README.md)**
Security scanning, auditing, and hardening.

### 📋 **[Session](./commands/session/README.md)**
Development session and state management.

### 🧪 **[Testing](./commands/testing/README.md)**
Comprehensive testing support and automation.

### 🛠️ **[Utilities](./commands/utilities/README.md)**
General productivity tools and helpers.

### 🔄 **[Workflow](./commands/workflow/README.md)**
Complex multi-step operation coordination.

---

## Configuration

Commands adapt to your project through `PROJECT_CONFIG.xml`. Run `/existing` to auto-generate this file, or create it manually to specify your tech stack, paths, and preferences.

## Philosophy

This framework embraces **simplicity over complexity**. Each command has a focused purpose, clear interface, and minimal cognitive overhead. Quality through focused execution, not feature bloat.

---
*For detailed documentation, see [docs/GETTING_STARTED.md](../docs/GETTING_STARTED.md)* 