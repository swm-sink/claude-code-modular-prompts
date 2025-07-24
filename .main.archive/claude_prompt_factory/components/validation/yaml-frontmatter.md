<prompt_component>
  <step name="YAML Frontmatter Validation">
    <description>
      Ensure all commands have proper YAML frontmatter for Claude Code discoverability.
      Validates required fields and enforces consistent structure across all commands.
    </description>
    <validation_rules>
      1. **Required Fields**:
         - `description`: Clear, concise command description (5-15 words)
         - `argument-hint`: User-friendly argument format (e.g., "[feature_description]")
         - `allowed-tools`: Comma-separated list of allowed Claude Code tools
      
      2. **Optional Fields**:
         - `tags`: Comma-separated list of searchable tags
         - `complexity`: low, medium, or high
         - `category`: Primary category for organization
      
      3. **Format Requirements**:
         - Must start with `---` on first line
         - Must end with `---` on its own line
         - Valid YAML syntax between delimiters
         - No trailing spaces or tabs
    </validation_rules>
    <template>
      ```yaml
      ---
      description: {command_description}
      argument-hint: "{argument_format}"
      allowed-tools: {tools_list}
      ---
      ```
    </template>
    <examples>
      ```yaml
      ---
      description: Orchestrates end-to-end feature development
      argument-hint: "[feature_description]"
      allowed-tools: Read, Write, Edit, Bash, Grep, Glob
      ---
      ```
      
      ```yaml
      ---
      description: Analyzes codebase for performance issues
      argument-hint: "[target_path] [options]"
      allowed-tools: Read, Grep, Glob, Bash
      tags: performance, analysis, optimization
      complexity: medium
      ---
      ```
    </examples>
    <output>
      When implementing YAML frontmatter:
      - Place at the very beginning of the file
      - Ensure description is actionable and specific
      - Use square brackets for required arguments in hint
      - Use angle brackets for optional arguments in hint
      - List only tools actually used by the command
    </output>
  </step>
</prompt_component>