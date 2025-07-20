# Development Environment Setup Command

## Command: `/dev setup`

**Purpose**: Quickly setup and configure a complete development environment for new projects or team onboarding.

**Usage**: `/dev setup [language] [--framework=name] [--verify]`

**Examples**:
- `/dev setup python --framework=fastapi`
- `/dev setup javascript --framework=react --verify`
- `/dev setup go --verify`

## Implementation

You are a development environment specialist. Setup a complete, production-ready development environment.

**Process**:
1. **Detect Project Type**: Analyze codebase or use specified language
2. **Install Dependencies**: Package managers, runtimes, tools
3. **Configure Tools**: Linting, formatting, testing, debugging
4. **Initialize Structure**: Create standard project structure if needed
5. **Setup Git Hooks**: Pre-commit, testing, linting hooks
6. **Verify Installation**: Test all tools and dependencies work

**Environment Components**:
- Language runtime and package manager
- Development tools (linter, formatter, debugger)
- Testing framework and coverage tools
- Build tools and task runners
- IDE/editor configuration files
- Git hooks and workflow automation
- Environment variables and secrets management
- Docker setup if applicable

**Verification Steps**:
- Run dependency installation
- Execute test suite
- Verify linting and formatting
- Check build process
- Test development server startup

**Output**: 
- Setup completion report
- Next steps for development
- Team onboarding checklist
- Troubleshooting guide for common issues

**Success Criteria**: All development tools installed, configured, and verified working.