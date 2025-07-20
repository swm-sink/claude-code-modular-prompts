# Getting Started with the Claude Code Prompt Factory

Welcome to the Claude Code Prompt Factory! This guide will get you set up and running in under 5 minutes.

## 1. Prerequisites

*   You have the Claude Code desktop application installed.
*   You have a project that you want to use the Prompt Factory with.

## 2. Installation

The "Prompt Factory" is designed to be incredibly simple to install.

### Step 1: Copy the `claude_prompt_factory`

Copy the `claude_prompt_factory` directory from this repository into a `.claude` directory in your project's root.

```bash
# From the root of your project
cp -r path/to/claude_prompt_factory .claude
```

### Step 2: Create a `PROJECT_CONFIG.xml`

Create a `PROJECT_CONFIG.xml` file in the root of your project. This file is how you will adapt the Prompt Factory's commands to your specific project.

You can start with this minimal template:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project_config>
  <!-- PROJECT IDENTIFICATION -->
  <project_metadata>
    <name>your-project-name</name>
    <version>1.0.0</version>
    <description>Brief description of your project</description>
  </project_metadata>

  <!-- TECHNOLOGY STACK -->
  <tech_stack>
    <primary_language>python</primary_language>
    <framework>django</framework>
    <database>postgresql</database>
  </tech_stack>

  <!-- DEVELOPMENT COMMANDS -->
  <commands>
    <test>python -m pytest</test>
    <lint>flake8 .</lint>
    <build>python -m build</build>
  </commands>
</project_config>
```

**That's it! You're ready to start using the Prompt Factory.**

## 3. Your First Commands

Now that you're set up, you can start using the commands in Claude Code.

### Explore the Command Library

The single source of truth for all commands is the `claude_prompt_factory/CLAUDE.md` file. This file provides a comprehensive overview of all available commands, organized by category.

Here are a few examples to get you started:

*   **Analysis**: `/query "how is authentication handled?"`
*   **Development**: `/task "create a utility function to validate email addresses"`
*   **Testing**: `/test unit "for the new email validation function"`
*   **Documentation**: `/docs generate "for the user authentication module"`

## 4. Next Steps

*   **Customize Your `PROJECT_CONFIG.xml`**: Tailor the `PROJECT_CONFIG.xml` to your project's specific needs. This is the key to unlocking the full power of the Prompt Factory.
*   **Explore the Command Library**: Read through the `claude_prompt_factory/CLAUDE.md` file to discover all the available commands.
*   **Create Your Own Commands**: The "Prompt Factory" is designed to be extensible. See the `docs/DEVELOPER_GUIDE.md` to learn how to create your own commands.
*   **Improve Existing Commands**: Use the `/meta-improve` command to provide feedback and help improve the prompts in the factory. 