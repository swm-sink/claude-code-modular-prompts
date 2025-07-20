# /help - Comprehensive Help Command

**Purpose**: Provide context-sensitive help, command discovery, tutorials, and examples to guide users.

## Usage
```bash
/help [command|topic] [--search <term>]
```

## Workflow

The `/help` command acts as an intelligent guide, following this process:

```xml
<help_workflow>
  <step name="Parse Request">
    <description>Parse the user's request to identify the help context (a specific command, a topic, or a search query).</description>
  </step>
  
  <step name="Gather Information">
    <description>Gather all relevant information, including command descriptions from the command library, documentation files, and pre-defined help topics.</description>
    <tool_usage>
      <tool>Parallel Grep/Read</tool>
      <description>Scan command and documentation files for relevant information.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Formatted Help">
    <description>Format the gathered information into a clear and helpful response, tailored to the user's request. This can include command syntax, examples, best practices, and links to related commands or tutorials.</description>
    <output>A comprehensive help message.</output>
  </step>
</help_workflow>
```

## Help Topics
- **Getting Started**: First steps with the Claude Code Prompt Factory.
- **Commands**: A full list of all available commands, organized by category.
- **Workflows**: Common development workflows and how to use them.
- **Best Practices**: Recommended patterns for effective use of the Prompt Factory.
- **Troubleshooting**: Common issues and their solutions.

## Examples
```bash
# Show a list of all available command categories
/help

# Get detailed help for a specific command
/help task

# Get help on a specific topic
/help workflows

# Search for help on a specific term
/help --search "test coverage"
```

## Output Format
```
HELP: /task - TDD Development Command
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Execute a focused, test-driven development workflow for creating or modifying a single component.

USAGE:
  /task "[description of task]"

EXAMPLE WORKFLOW:
  1. /task "implement a validation utility for email addresses"
     - I will write a comprehensive suite of failing tests first.
     - Then, I will write the minimal amount of code to make the tests pass.
     - Finally, I will refactor the code for clarity and performance.

TIP: Use `/task` for small, focused units of work. For larger features, use the `/feature` command.

RELATED: /feature, /test unit
```