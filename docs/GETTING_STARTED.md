# Getting Started with the Claude Code Prompt Factory

Welcome! This guide will get you set up and running in under 2 minutes.

## 1. Prerequisites

*   You have the Claude Code desktop application installed.
*   You have a project you want to work with.

## 2. Installation

There are two steps to get started:

### Step 1: Copy the `claude_prompt_factory`

Copy the `claude_prompt_factory` directory from this repository into a `.claude` directory in your project's root. If the `.claude` directory does not exist, create it.

```bash
# From the root of your project
mkdir -p .claude
cp -r path/to/claude_prompt_factory .claude/
```

### Step 2: Initialize Your Project

Now, from within Claude Code, run the appropriate `/init` command. This is the most important step, as it will generate the `PROJECT_CONFIG.xml` file that tailors the entire factory to your project.

*   **For an existing project:**
    ```
    /init existing
    ```
    This command will scan your codebase, detect your tech stack automatically, and propose a configuration for you to approve.

*   **For a new, empty project:**
    ```
    /init new
    ```
    This command will guide you through a series of questions to create your configuration interactively.

**That's it! You're ready to start using the Prompt Factory.**

## 3. Your First Commands

Now that you're set up, you can start exploring.

1.  **Explore the Command Library**: Open `claude_prompt_factory/commands/CLAUDE.md`. This is the main index of all available command categories.
2.  **Try an Agent**: Run one of the powerful autonomous agents, like `/agent research "what are the best practices for api design?"`.
3.  **Analyze Your Code**: Get a feel for the analysis tools by running `/analyze code`.

## 4. Next Steps

*   **Review Your `PROJECT_CONFIG.xml`**: See how the factory has been configured for your project and make any desired tweaks.
*   **Create Your Own Commands**: The factory is designed to be extended. See the `DEVELOPER_GUIDE.md` to learn how.
*   **Improve Existing Commands**: Use the `/meta-improve` command to provide feedback on any command and help improve the prompts in the factory. 