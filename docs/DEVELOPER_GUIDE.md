# Developer & Contributor Guide

Welcome to the Claude Code Prompt Factory! This guide provides everything you need to know to create your own commands and contribute them to the factory.

## Core Philosophy

Our goal is to create a powerful, modular, and shareable library of prompt-based commands that feel native to the Claude Code environment. We prioritize simplicity, clarity, and reusability. Before you start, please read our [ARCHITECTURAL_PRINCIPLES.md](../ARCHITECTURAL_PRINCIPLES.md) to understand the core concepts of the "Prompt Factory."

## Creating a New Command: A Step-by-Step Guide

Creating a new command is designed to be a simple and straightforward process.

### Step 1: Identify a Need

The first step is to identify a need for a new command. Good commands are:

*   **Focused**: They do one thing well.
*   **Reusable**: They can be used in a variety of contexts.
*   **Helpful**: They automate a common or complex task.

### Step 2: Choose a Category

Our commands are organized into categories in the `claude_prompt_factory/commands/` directory. Choose the category that best fits your new command. If a suitable category doesn't exist, you can propose a new one.

### Step 3: Create the Command File

Create a new markdown file in the appropriate category directory. The file name should be descriptive and use kebab-case (e.g., `generate-api-docs.md`).

### Step 4: Write the Command Prompt

This is the most important step. Your command file is a prompt that will guide the LLM's behavior. It should be structured, clear, and easy for both the LLM and a human to understand.

#### Command Template

Use this template as a starting point for your new command:

```markdown
# /[command-name] - [A brief, human-readable title]

**Purpose**: [A clear, one-sentence description of what the command does.]

## Usage
`​`​`​bash
/[command-name] [arguments]
`​`​`​

## Workflow
<[command_name]_workflow>
  <step name="[Step 1]">
    <description>[Description of what happens in this step.]</description>
    <tool_usage>
      <tool>[Tool to use, e.g., Bash, Grep, Read, Write]</tool>
      <description>[Description of how the tool is used.]</description>
    </tool_usage>
  </step>
  <step name="[Step 2]">
    <description>[Description of what happens in this step.]</description>
  </step>
</[command_name]_workflow>

## Configuration
<command name="/[command-name]">
  <setting name="[setting_name]" value="[default_value]" description="[Description of the setting.]" />
</command>

## Use Cases
*   [A use case for the command.]
*   [Another use case for the command.]
```

#### Best Practices for Writing Prompts

*   **Be Explicit**: Don't assume the LLM knows what you want. Provide clear, step-by-step instructions.
*   **Use Structure**: Use headings, lists, and XML tags to structure your prompt and make it easy to parse.
*   **Provide Examples**: Examples are one of the best ways to guide the LLM's behavior.
*   **Think Like a "Claude Code Native"**: Design your command to leverage the native tools of Claude Code, such as `Bash`, `Grep`, `Read`, and `Write`.

### Step 5: Test Your Command

Test your new command thoroughly in Claude Code. Make sure it behaves as you expect and that the output is accurate and helpful.

## Contributing to the Prompt Factory

We welcome contributions! If you've created a command that you think would be a valuable addition to the factory, please follow these steps to contribute:

1.  **Fork the repository.**
2.  **Create a new branch** for your command.
3.  **Add your command** to the appropriate category directory.
4.  **Update the `claude_prompt_factory/CLAUDE.md` file** to include your new command.
5.  **Submit a pull request.**

We will review your contribution and work with you to get it merged.

Thank you for helping to make the Claude Code Prompt Factory even better! 