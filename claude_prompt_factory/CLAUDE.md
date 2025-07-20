# The Claude Code Prompt Factory

**The Claude Code Prompt Factory** is a modular, shareable, and comprehensive library of prompt-based commands that feel native to the Claude Code environment. Thisxx file is the central entry point and guide to the entire system.

## Guiding Principles

The Prompt Factory is built on a set of core principles:

*   **Simplicity**: Each command has a single, well-defined purpose.
*   **Consistency**: All commands follow a standard, predictable structure.
*   **Modularity**: Commands are self-contained and easy to understand and modify.
*   **Prompt-Driven**: The entire system is built on the power of prompts, making it easy to extend and adapt.

## Command Library

The Prompt Factory provides a comprehensive library of commands, organized into logical categories.

### Init (`/init`)
*   `/init`: Advanced, context-aware initialization of the Prompt Factory.

### Auto (`/auto`)
*   `/auto`: Intelligently route a natural language request to the most appropriate command.

### Agentic Workflows (`/agentic`)
*   `/dag-orchestrator`: Adaptive DAG-based agent orchestration.
*   `/swarm`: Multi-agent swarm intelligence.

### Analysis (`/analyze`)
*   `/analyze code`: Analyze code for quality, patterns, and structure.
*   `/analyze dependencies`: Analyze project dependencies for vulnerabilities and updates.
*   `/analyze performance`: Analyze the performance of an application.

### API (`/api`)
*   `/api design`: Design a new API.
*   `/api mock`: Create a mock API server.
*   `/api test`: Test an API endpoint.
*   `/api version`: Manage API versions.

### Context (`/context`)
*   `/context prime`: Standard codebase analysis.
*   `/context prime-mega`: Deep, multi-agent codebase analysis.

### Database (`/db`)
*   `/db migrate`: Safely migrate a database schema.
*   `/db seed`: Seed a database with test data.
*   `/db backup`: Backup a database.
*   `/db restore`: Restore a database from a backup.

### Deployment (`/deploy`)
*   `/deploy`: Deploy an application to a specified environment.
*   `/ci setup`: Set up a new CI/CD pipeline.
*   `/ci run`: Run a CI/CD pipeline.
*   `/cd rollback`: Roll back a deployment.

### Development (`/dev`)
*   `/dev setup`: Set up a new development environment.
*   `/dev build`: Build the application.
*   `/dev test`: Run the full test suite.
*   `/dev refactor`: Refactor a section of code.
*   `/dev debug`: Interactively debug a piece of code.

### Documentation (`/docs`)
*   `/docs generate`: Generate documentation from source code.
*   `/docs update`: Update existing documentation to match code changes.
*   `/docs check`: Check documentation for completeness and accuracy.
*   `/docs publish`: Publish documentation to a hosting platform.

### Error (`/error`)
*   `/error diagnose`: Diagnose an error.
*   `/error fix`: Automatically fix an error.
*   `/error handle`: Add error handling to code.
*   `/error report`: Generate an error report.
*   `/error trace`: Trace the path of an error.

### Feature (`/feature`)
*   `/feature`: A comprehensive command for end-to-end feature development.

### Git (`/git`)
*   `/git commit`: Generate an intelligent commit message.
*   `/git history`: Analyze Git history.
*   `/git merge`: Safely merge a Git branch.
*   `/git pr`: Create a new pull request.

### Meta (`/meta`)
*   `/meta improve`: Improve the behavior of a command.

### Performance (`/perf`)
*   `/perf benchmark`: Run performance benchmarks.
*   `/perf monitor`: Monitor application performance.
*   `/perf optimize`: Optimize application performance.
*   `/perf profile`: Profile application performance.
*   `/perf report`: Generate a performance report.

### Protocol (`/protocol`)
*   `/protocol`: EPICCC development & deployment protocol.

### Security (`/secure`)
*   `/secure scan`: Scan for security vulnerabilities.
*   `/secure audit`: Audit security configurations.
*   `/secure config`: Harden security configurations.
*   `/secure fix`: Automatically fix security vulnerabilities.
*   `/secure report`: Generate a security report.

### Task (`/task`)
*   `/task`: A comprehensive command for test-driven development of a single component.

### Testing (`/test`)
*   `/test unit`: Generate unit tests for a component.
*   `/test integration`: Run integration tests.
*   `/test e2e`: Run end-to-end tests.
*   `/test coverage`: Analyze test coverage.
*   `/test mutation`: Perform mutation testing.
*   `/test report`: Generate a test report.

### Utilities
*   `/code clean`: Clean up code by removing dead code, optimizing imports, etc.
*   `/code format`: Format code according to project standards.
*   `/code lint`: Lint code to identify potential issues.
*   `/cost analyze`: Analyze cloud costs.
*   `/deps update`: Safely update project dependencies.
*   `/env setup`: Set up environment variables.
*   `/help`: Get help with any command.
*   `/monitor setup`: Set up monitoring for an application.
*   `/monitor alerts`: Manage monitoring alerts.
*   `/monitor dashboard`: Create a monitoring dashboard.
*   `/monitor health`: Check the health of an application.
*   `/monitor logs`: View application logs.
*   `/query`: A powerful command for codebase analysis and understanding.
*   `/think deep`: Use advanced AI for deep thinking and analysis.

### Workflow (`/workflow`)
*   `/workflow run`: Execute a series of commands defined in a workflow file.

## Configuration

The Prompt Factory is configured through a single, user-facing file: `PROJECT_CONFIG.xml`. This file allows you to adapt the behavior of the commands to your specific project needs.

## Documentation

*   **Getting Started**: `docs/GETTING_STARTED.md`
*   **Developer Guide**: `docs/DEVELOPER_GUIDE.md`

---
*This project is built on the principle that the best way to extend an LLM-powered tool is with the LLM's own language: prompts.* 