# Developer & Contributor Guide

This guide provides everything you need to know to create your own commands and components and contribute them to the Prompt Factory.

## Core Architecture

Our architecture is designed to be modular, configurable, and consistent. Before you start, it's essential to understand the three main concepts:

1.  **Standard Command Files**: Every command is a single `.md` file that follows a strict XML schema: `<command_file>`. This ensures consistency and provides rich metadata.
2.  **Reusable Components**: Common patterns (like finding files or generating reports) are extracted into reusable components in the `claude_prompt_factory/components/` directory. Commands should use these components with the `<include/>` tag whenever possible to avoid duplicating logic.
3.  **Configuration-Driven**: Commands are made generic by reading project-specific details from the `PROJECT_CONFIG.xml` file. Prompts should reference these values using the `${...}` syntax.

## Creating a New Command: A Step-by-Step Guide

### Step 1: Identify a Need & Choose a Category

Good commands are focused and reusable. Once you have an idea, choose the category in `claude_prompt_factory/commands/` that best fits your new command.

### Step 2: Create the Command File

Create a new `.md` file in the category directory. The file name should be descriptive and use kebab-case (e.g., `generate-api-docs.md`).

### Step 3: Use the Official Template

Your command file **must** conform to the standard `<command_file>` XML structure. The best way to start is by copying an existing command file, or by using this template:

```xml
<command_file>
  <metadata>
    <name>/command-name</name>
    <purpose>A brief, one-sentence description of the command.</purpose>
    <usage><![CDATA[/command-name [arg] <opt_arg>]]></usage>
  </metadata>
  <arguments>
    <argument name="arg" type="string" required="true">
      <description>Description of this argument.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>A basic use case.</description>
      <usage>/command-name "value"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      Your prompt logic goes here.
      <include component="components/context/find-relevant-code.md" />
      Use config value: ${paths.source}
    </prompt>
  </claude_prompt>
  <dependencies>
    <!-- Add all invoked commands, included components, and config values here -->
  </dependencies>
</command_file>
```

### Step 4: Write the Prompt & Add Dependencies

This is the core of your command.
- Write clear, step-by-step instructions inside the `<prompt>` tag.
- **Use Components**: Before writing new logic, check if a reusable component in `claude_prompt_factory/components/` already does what you need.
- **Make it Configurable**: Use `${...}` variables to pull project-specific details from `PROJECT_CONFIG.xml` instead of hardcoding them.
- **Document Dependencies**: Meticulously list every command, component, and config value your command uses in the `<dependencies>` block. This is critical for system analysis.

### Step 5: Test Your Command

Test your new command thoroughly in Claude Code.

## Creating a New Component

If you find yourself writing the same prompt logic in multiple commands, it's time to create a component.
1.  Create a new `.md` file in the appropriate subdirectory of `claude_prompt_factory/components/`.
2.  Write the reusable prompt snippet inside a `<prompt_component>` tag.
3.  Refactor any commands that were using that logic to now use `<include component="..." />`.

## Contribution Process

1.  **Fork the repository.**
2.  **Create a new branch** for your feature.
3.  **Add your command/component** and ensure it follows the template.
4.  **Update the category `README.md`** if you've added a command.
5.  **Submit a pull request.** 