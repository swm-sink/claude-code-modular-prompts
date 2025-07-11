# System Components

This directory contains core system functionality and infrastructure components.

## Directory Structure

### `/quality/`
Quality gates, validation, and testing frameworks:
- Universal quality gates
- R&D quality gates and integration tests
- TDD enforcement and verification
- Test coverage requirements
- Performance gates and validation

### `/security/`
Security modules and compliance:
- Threat modeling
- Security audits
- Financial compliance
- Security validation and gate verification

### `/context/`
Context management and preservation:
- Project priming
- Context restoration
- Decision artifacts
- Context preservation rules

### `/session/`
Session management infrastructure:
- Session management patterns
- Session compression
- Session storage
- Session reliability

### `/git/`
Git operations and version control:
- Conventional commits
- Git operations patterns
- Worktree isolation

## Key Principles

1. **Infrastructure Focus**: System-level functionality only
2. **No Prompts**: Prompt engineering belongs in `/prompt_eng/`
3. **Reliability**: Critical infrastructure for framework operation
4. **Integration**: Provides services to prompt engineering components

## Usage

System components are used by commands and modules but do not contain prompt templates themselves.
They provide the infrastructure that enables reliable framework operation.