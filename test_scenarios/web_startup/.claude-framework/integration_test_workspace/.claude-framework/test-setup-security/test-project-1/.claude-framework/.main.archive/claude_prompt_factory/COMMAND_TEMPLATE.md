# Claude Code Prompt Factory - Command Template

This template ensures all commands follow the hybrid Markdown+XML format for maximum compatibility with both Claude Code and our advanced framework features.

## Template Structure

```markdown
---
description: Brief, clear description of what this command does (appears in Claude Code menu)
argument-hint: "[arg1] [arg2]"  # Optional: shows expected arguments in autocomplete
allowed-tools: Bash, Read, Write, Grep, Glob, Task  # Tools this command can use
---

# /command-name - Display Name

Brief description of the command's purpose and capabilities.

## Usage
```bash
/command-name                    # Basic usage
/command-name arg1="value"       # With arguments
```

## Arguments
- `arg1` (optional): Description of first argument
- `arg2` (required): Description of second argument

## Examples
- `/command-name` → Basic execution
- `/command-name arg1="test"` → With specific argument

<command_file>
  <metadata>
    <name>/command-name</name>
    <purpose>Detailed purpose description for internal framework use.</purpose>
    <usage>
      <![CDATA[
      /command-name [arguments]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="arg1" type="string" required="false" default="default-value">
      <description>Detailed description of the argument.</description>
    </argument>
    <argument name="arg2" type="string" required="true">
      <description>Required argument description.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Example scenario description.</description>
      <usage>/command-name arg1="example"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a [role description]. Your task is to [main objective].

      ## Workflow

      1. **Step 1**: 
         - Action to take
         - Include components if needed: <include component="components/path/component.md" />

      2. **Step 2**:
         - Additional actions
         - Reference config values when needed

      3. **Final Step**:
         - Complete the task
         - Provide appropriate output

      Execute this workflow with attention to [specific requirements].
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <invokes_commands>
      <command>/other-command</command>
    </invokes_commands>
    <uses_config_values>
      <value>config.section.property</value>
    </uses_config_values>
  </dependencies>
</command_file>
```

## Key Guidelines

### Markdown Section (Claude Code Compatibility)
1. **YAML Frontmatter**: Required for Claude Code recognition
   - `description`: Appears in slash command menu
   - `argument-hint`: Shows in autocomplete (optional)
   - `allowed-tools`: Limits tool access for security

2. **Title**: Use format `# /command-name - Display Name`

3. **Usage Section**: Clear examples with bash code blocks

4. **Arguments**: List all arguments with descriptions

### XML Section (Advanced Framework Features)
1. **Metadata**: Detailed command information
2. **Arguments**: Typed argument definitions with validation
3. **Examples**: Rich example scenarios
4. **Claude Prompt**: The actual prompt instructions
5. **Dependencies**: Component/command/config dependencies

### Important Notes
- **Self-closing tags**: Always use `<include component="path" />` (with space before />) 
- **CDATA sections**: Use for complex usage examples
- **Component references**: Must reference actual component files
- **Config values**: Use dot notation for nested config properties

### File Naming
- Use kebab-case: `command-name.md`
- Place in appropriate category directory
- Ensure command name in metadata matches filename

### Testing Checklist
- [ ] Command appears in Claude Code `/` menu
- [ ] Arguments work with `$ARGUMENTS` substitution
- [ ] XML parses without errors
- [ ] Dependencies are valid references
- [ ] Component includes work properly