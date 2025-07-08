# Contributing to Claude Code Modular Agents Framework

Thank you for your interest in contributing to the Claude Code Modular Agents Framework! This guide will help you get started with contributing to our project.


# Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Contribution Guidelines](#contribution-guidelines)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Module Development](#module-development)
- [Documentation Standards](#documentation-standards)


# Code of Conduct

We are committed to fostering a welcoming and inclusive community. Please be respectful, constructive, and professional in all interactions.


# Getting Started

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/claude-code-modular-agents.git
   cd claude-code-modular-agents
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set Up Development Environment**
   - Ensure you have Claude Code installed
   - Install GitHub CLI: `brew install gh` (macOS) or see [installation guide](https://cli.github.com/)
   - Familiarize yourself with [CLAUDE.md](CLAUDE.md) framework rules


# Development Process


# 1. Understanding the Framework

Before contributing, ensure you understand:
- The AWARE process (Assess → Watch → Architect → Run → Evaluate)
- Command delegation pattern (commands delegate, modules implement)
- Token budgets (Foundation <3k, commands <4k, modules <2k)
- XML structure requirements for Claude 4


# 2. Planning Your Contribution

- **For New Features**: Create an issue first to discuss the approach
- **For Bug Fixes**: Reference the existing issue or create one
- **For New Modules**: Ensure it follows the modular architecture pattern


# 3. Following Framework Standards

All contributions must adhere to:
- **DRY Principle**: No redundancy between files
- **Single Source of Truth**: Each concept in exactly one location
- **Token Optimization**: Stay within token budgets
- **Quality Gates**: TDD, security review, performance validation


# Contribution Guidelines


# Code Style

1. **Markdown Files**
   - Use clear, descriptive headers
   - Include XML structure for Claude 4 optimization
   - Follow existing formatting patterns

2. **Module Structure**
   ```xml
   <module_definition>
     <metadata>
       <name>module-name</name>
       <category>category-name</category>
       <description>Clear description</description>
     </metadata>
     <implementation>
       <!-- Module implementation -->
     </implementation>
   </module_definition>
   ```

3. **Command Structure**
   ```xml
   <command purpose = "Command purpose">
     <delegation target = "modules/category/module.md">
       Delegation description
     </delegation>
   </command>
   ```


# Naming Conventions

- **Commands**: Lowercase, action-oriented (e.g., `task.md`, `swarm.md`)
- **Modules**: Descriptive, hyphenated (e.g., `tdd-enforcement.md`, `security-audit.md`)
- **Test Files**: `test_[component_name].py`


# Testing Requirements


# Mandatory Tests

1. **Unit Tests**: Minimum 90% coverage
2. **Integration Tests**: For module interactions
3. **Quality Assertions**: Performance, security, behavior validation


# Running Tests

```bash

# Run all tests
pytest tests/


# Run specific test category
pytest tests/framework/


# Run with coverage
pytest --cov=.claude tests/
```


# Test Structure

```python
def test_module_loading():
    """Test that modules load correctly"""
    # Arrange
    module_path = ".claude/modules/quality/tdd.md"
    
    # Act
    result = load_module(module_path)
    
    # Assert
    assert result is not None
    assert result.metadata.name == "tdd"
```


# Pull Request Process


# 1. Pre-PR Checklist

- [ ] All tests passing with 90%+ coverage
- [ ] Documentation updated
- [ ] No token budget violations
- [ ] Follows framework patterns
- [ ] Security review completed
- [ ] Performance validated


# 2. PR Template

Your PR should include:

```markdown

# Description
Brief description of changes


# Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] New module
- [ ] Documentation update


# Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] All tests passing


# Checklist
- [ ] Follows CLAUDE.md rules
- [ ] No redundancy introduced
- [ ] Token budgets maintained
- [ ] Documentation updated
```


# 3. Review Process

1. Automated checks must pass
2. Code review by maintainer
3. Testing validation
4. Documentation review
5. Merge upon approval


# Module Development


# Creating a New Module

1. **Choose Appropriate Category**
   - `security/` - Security-related functionality
   - `quality/` - Quality enforcement patterns
   - `development/` - Core development operations
   - `patterns/` - Reusable architectural patterns

2. **Follow Module Template**
   ```xml
   <module>
     <metadata>
       <name>your-module-name</name>
       <version>1.0.0</version>
       <category>category-name</category>
       <dependencies>
         <dependency>other-module</dependency>
       </dependencies>
     </metadata>
     
     <implementation>
       <!-- Your implementation here -->
     </implementation>
     
     <usage_examples>
       <!-- Provide clear examples -->
     </usage_examples>
   </module>
   ```

3. **Validate Token Budget**
   - Modules must be <2k tokens
   - Use token counter to verify


# Module Quality Requirements

- Clear single responsibility
- Well-documented interface
- Comprehensive examples
- No external dependencies without justification
- Performance considerations documented


# Documentation Standards


# Required Documentation

1. **Module Documentation**
   - Purpose and capabilities
   - Interface definition
   - Usage examples
   - Performance characteristics

2. **Command Documentation**
   - Delegation targets
   - Usage patterns
   - Integration points

3. **Code Comments**
   - Only where necessary for clarity
   - Focus on "why" not "what"


# Documentation Format

```markdown

# Module/Command Name


# Purpose
Clear description of what this does


# Interface
- Input requirements
- Output format
- Error conditions


# Usage Examples
```example
/command "Real world example"
```


# Performance Considerations
- Token usage
- Execution time
- Resource requirements
```


# Getting Help

- **Questions**: Open a [GitHub Discussion](https://github.com/swm-sink/claude-code-modular-agents/discussions)
- **Bugs**: Create an [Issue](https://github.com/swm-sink/claude-code-modular-agents/issues)
- **Ideas**: Start a discussion or create a feature request issue


# Recognition

Contributors will be recognized in:
- GitHub contributors list
- Release notes
- Special mentions for significant contributions

Thank you for helping make Claude Code Modular Agents better! 🚀