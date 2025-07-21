# Core Commands

The fundamental building blocks of the factory for initialization, routing, and safe execution.

## Available Commands

*   **`/auto`**: Intelligent command router that analyzes requests and selects optimal commands.
*   **`/existing`**: Initialize the factory for an existing project by scanning the codebase.
*   **`/new`**: Initialize the factory for a new project through guided setup.
*   **`/protocol`**: Rigorous EPICCC protocol for safe, high-stakes changes.
*   **`/query`**: Intelligent code analysis and search without modifications.
*   **`/task`**: Focused TDD workflow for single components with comprehensive testing.
*   **`/research`**: Initialize for research-focused projects with specialized structure.

## Core Concepts

### Intelligent Routing
The `/auto` command serves as the main entry point, analyzing natural language requests and routing to appropriate specialized commands.

### Project Initialization
- `/existing`: Scans codebase and auto-generates PROJECT_CONFIG.xml
- `/new`: Interactive setup for new projects
- `/research`: Specialized setup for research workflows

### Safety Protocols
The `/protocol` command implements EPICCC (Evaluate, Plan, Implement, Check, Commit) for critical changes.

## Usage Examples

```bash
# Let the system choose the best approach
/auto "fix the login authentication bug"

# Initialize existing project
/existing

# Safe protocol for critical changes
/protocol "refactor database connection logic"

# Research and analyze without changes
/query "how does the payment processing work?"
```

## Configuration

Core commands read from `PROJECT_CONFIG.xml` to customize behavior for your specific tech stack and requirements. 