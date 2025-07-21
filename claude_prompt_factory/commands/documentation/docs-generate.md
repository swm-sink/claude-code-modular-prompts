---
description: Automated documentation generation with intelligent content creation and validation
argument-hint: "[doc_type] [output_format]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /docs generate - Automated Documentation Generator

Advanced documentation generation system with intelligent content creation, multi-format output, and validation.

## Usage
```bash
/docs generate api                           # Generate API documentation
/docs generate readme                       # Generate comprehensive README
/docs generate architecture                 # Generate architecture documentation
/docs generate --format markdown           # Specify output format
```

<command_file>
  <metadata>
    <name>/docs generate</name>
    <purpose>Automatically generates comprehensive documentation from source code.</purpose>
    <usage>
      <![CDATA[
      /docs generate <target_directory="./src">
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="false" default="./src">
      <description>The source directory to scan for code to document.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Generate documentation for all code in the default 'src' directory.</description>
      <usage>/docs generate</usage>
    </example>
    <example>
      <description>Generate documentation for a specific component directory.</description>
      <usage>/docs generate target="./src/components"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a technical writer. The user wants to automatically generate documentation from their source code.

      1.  **Analyze Code**: Scan the `target` directory to analyze the code. Extract information such as:
          *   Class and function signatures.
          *   Docstrings and comments.
          *   Dependencies and relationships between modules.
      2.  **Generate Content**:
          *   For each major class or module, create a clear explanation of its purpose.
          *   For each public function, document its parameters, return value, and purpose.
          *   Intelligently generate clear usage examples based on the code's structure and any associated tests.
      3.  **Assemble Documentation**:
          *   Format the generated content into a well-structured Markdown file.
          *   Apply the documentation style guide defined in `PROJECT_CONFIG.xml`.
          *   Propose the new documentation file to the user.
          *   <include component="components/actions/apply-code-changes.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>documentation.style</value>
      <value>documentation.output_dir</value>
    </uses_config_values>
    <includes_components>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>

<include component="components/analysis/codebase-discovery.md" />
<include component="components/context/find-relevant-code.md" />
<include component="components/planning/create-step-by-step-plan.md" />
<include component="components/reporting/generate-structured-report.md" />