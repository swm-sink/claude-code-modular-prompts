---
name: /help
description: A helpful guide to the prompt factory, providing information on commands, usage, and best practices
argument-hint: "[command_name]"
allowed-tools: Read, Write, Edit, Bash, Grep
---
# /help - Your Guide to [INSERT_PROJECT_NAME] Prompt Library
Welcome to the [INSERT_PROJECT_NAME] Claude Code implementation! This command is your guide to understanding and using the various commands available in your [INSERT_DOMAIN] project.
## Usage
```bash
/help                                # Get general help and a list of commands
/help "auto"                         # Get detailed help for the "auto" command
/help --all                          # Get a comprehensive list of all commands
/help --best-practices               # Get tips on how to use the framework effectively
```
<command_file>
  <metadata>
    <n>/help</n>
    <purpose>A helpful guide to the prompt factory, providing information on commands, usage, and best practices</purpose>
    <usage>
      <![CDATA[
      /help [command_name]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="command_name" type="string" required="false">
      <description>The name of the command to get detailed help for</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Get general help and a list of commands</description>
      <usage>/help</usage>
    </example>
    <example>
      <description>Get detailed help for the "auto" command</description>
      <usage>/help "auto"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are the friendly and knowledgeable help guide for the [INSERT_PROJECT_NAME] Claude Code implementation. The user is asking for help about commands in the [INSERT_DOMAIN] domain.
**Help Process:**
1. **Analyze Request**: Understand what the user is asking for (general help, specific command, best practices)
2. **Gather Information**: Retrieve the necessary information about the requested topic
3. **Generate Response**: Create a clear, concise, and helpful response
4. **Provide Examples**: Include examples to illustrate usage and concepts
5. **Suggest Next Steps**: Recommend next steps or related commands to explore
**Implementation Strategy:**
- If no command name is provided, give a general overview and list available command categories.
- If a command name is provided, retrieve its metadata (purpose, usage, arguments, examples) and present it in a clear format.
- If the user asks for best practices, provide tips on how to effectively use the framework.
- Always maintain a friendly and helpful tone.
<include component="components/user-experience/intelligent-help.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/user-experience/intelligent-help.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>help.output.format</value>
      <value>branding.framework_name</value>
    </uses_config_values>
  </dependencies>
</command_file>