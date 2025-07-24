# Getting Started with the Claude Code Prompt Factory

Welcome! This guide will get you up and running with the streamlined prompt factory in under 2 minutes.

## 1. Prerequisites

*   Claude Code desktop application
*   A project you want to enhance (existing or new)

## 2. Installation

### Step 1: Copy the Framework

Copy the `claude_prompt_factory` directory to a `.claude` directory in your project's root:

```bash
# From your project root
mkdir -p .claude
cp -r path/to/claude_prompt_factory .claude/
```

### Step 2: Initialize Your Project

From within Claude Code, run the initialization command:

*   **For an existing project:**
    ```
    /existing
    ```
    This scans your codebase, detects your tech stack, and creates `PROJECT_CONFIG.xml`

*   **For a new project:**
    ```
    /new
    ```
    This guides you through interactive setup

**That's it! You're ready to start using the framework.**

## 3. Your First Commands

Start with the intelligent router:

```bash
# Let the system choose the best approach
/auto "analyze the authentication system"

# Fix a specific issue
/auto "there's a bug in the login form validation"

# Add a new feature
/auto "add password reset functionality"
```

### Other Essential Commands

```bash
# Focused development with TDD
/task "create email validation utility"

# Understand your codebase
/query "how does user authentication work?"

# Safe protocol for critical changes  
/protocol "refactor database connection logic"

# Complete feature development
/feature "user profile management system"
```

## 4. Command Categories

Explore organized commands by category:

1.  **[Core Commands](../claude_prompt_factory/commands/core/README.md)**: Initialization, routing, safe protocols
2.  **[Development](../claude_prompt_factory/commands/development/README.md)**: TDD workflows, debugging, setup
3.  **[Analysis](../claude_prompt_factory/commands/analysis/README.md)**: Code analysis and quality checks
4.  **[Agents](../claude_prompt_factory/commands/agents/README.md)**: Autonomous multi-step workflows

## 5. Configuration

Your `PROJECT_CONFIG.xml` adapts all commands to your project:

```xml
<project_config>
  <tech_stack>
    <languages>
      <language name="python" primary="true"/>
    </languages>
    <frameworks>
      <framework name="django" primary="true"/>
    </frameworks>
  </tech_stack>
  <paths>
    <source>src/</source>
    <tests>tests/</tests>
  </paths>
</project_config>
```

## 6. Best Practices

1.  **Start Simple**: Use `/auto` for most tasks - it routes intelligently
2.  **Be Specific**: Clear descriptions get better results
3.  **Use Categories**: Explore specific command categories for specialized needs
4.  **Stay Focused**: Each command excels at its specific domain

## 7. Next Steps

*   **Explore Commands**: Browse the [command reference](../claude_prompt_factory/CLAUDE.md)
*   **Customize Configuration**: Edit `PROJECT_CONFIG.xml` for your needs
*   **Learn Patterns**: Study the [examples](../examples/) directory
*   **Create Commands**: See the [developer guide](DEVELOPER_GUIDE.md) for custom commands

---
*Remember: This framework emphasizes simplicity and effectiveness. Start with basic commands and gradually explore more specialized features as needed.* 