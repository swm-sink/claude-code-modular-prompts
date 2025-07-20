# /docs generate - Documentation Generation Command

**Purpose**: Automatically generate comprehensive documentation from code, with intelligent content extraction and formatting.

## Usage
```bash
/docs generate [target] [--type=api|readme|guide] [--format=md|html]
```

## Workflow

The `/docs generate` command follows a systematic process to generate high-quality documentation.

```xml
<doc_generation_workflow>
  <step name="Analyze Code">
    <description>Recursively scan the target directory to analyze the code and extract all relevant information for documentation, including function signatures, class structures, comments, and dependencies.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob</tool>
      <description>Find all source code files in the target directory and extract relevant information.</description>
    </tool_usage>
  </step>
  
  <step name="Extract Content & Generate Examples">
    <description>Extract the core content for the documentation and intelligently generate usage examples based on the code's structure and any existing tests.</description>
  </step>
  
  <step name="Generate Documentation">
    <description>Assemble the extracted content and generated examples into a structured, readable documentation file, using the appropriate format and style as defined in `PROJECT_CONFIG.xml`.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create the new documentation file in the project's designated docs directory.</description>
    </tool_usage>
  </step>
</doc_generation_workflow>
```

## Configuration

The behavior of the `/docs generate` command is configured in the `PROJECT_CONFIG.xml` file.

```xml
<project_config>
  <documentation>
    <style>google</style>
    <output_format>markdown</output_format>
    <include_private_members>false</include_private_members>
  </documentation>
</project_config>
```

## Examples
- `/docs generate src/` - Generate docs for source directory
- `/docs generate --type=api` - Create API documentation  
- `/docs generate components/ --format=html` - HTML format docs