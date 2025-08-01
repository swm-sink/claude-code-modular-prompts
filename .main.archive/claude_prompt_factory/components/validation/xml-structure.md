<prompt_component>
  <step name="XML Structure Validation">
    <description>
      Ensure all commands have proper XML structure for reliable parsing and execution.
      Validates required elements and enforces consistent command file format.
    </description>
    <validation_rules>
      1. **Root Element**: Must have `<command_file>` as root element
      
      2. **Required Sections**:
         - `<metadata>`: Command metadata including name, purpose, usage
         - `<arguments>`: Argument definitions with types and descriptions
         - `<steps>`: Execution steps with clear instructions
         - `<output>`: Expected output format or structure
      
      3. **Optional Sections**:
         - `<examples>`: Usage examples with descriptions
         - `<dependencies>`: Component dependencies
         - `<error_handling>`: Error scenarios and recovery
         - `<performance>`: Performance considerations
      
      4. **XML Requirements**:
         - Well-formed XML with matching tags
         - Proper CDATA sections for code/scripts
         - No unescaped special characters
         - Consistent indentation (2 spaces)
    </validation_rules>
    <template>
      <command_file_template>
        <metadata>
          <name>{command_name}</name>
          <purpose>{command_purpose}</purpose>
          <usage_pattern>
            {usage_pattern}
            ]]>
          </usage>
        </metadata>
        
        <arguments>
          <argument name="{arg_name}" type="{type}" required="{true/false}">
            <description>{arg_description}</description>
          </argument>
        </arguments>
        
        <steps>
          <step name="{step_name}">
            <description>{step_description}</description>
          </step>
        </steps>
        
        <o>
          {expected_output}
        </o>
      </command_file>
      ```
    </template>
    <common_issues>
      1. **Unescaped Characters**: Use CDATA for code containing <, >, &
      2. **Missing Closing Tags**: Ensure all opened tags are closed
      3. **Invalid Nesting**: Steps must be within <steps> parent
      4. **Empty Elements**: Remove or populate empty elements
    </common_issues>
    <output>
      When implementing XML structure:
      - Place after YAML frontmatter and documentation
      - Use CDATA sections for any code or complex text
      - Maintain consistent 2-space indentation
      - Include all required sections
      - Validate XML before committing
    </output>
  </step>
</prompt_component>