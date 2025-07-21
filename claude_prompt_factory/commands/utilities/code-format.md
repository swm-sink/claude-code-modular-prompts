---
description: Advanced code formatting with intelligent styling, consistency enforcement, and automated quality improvements
argument-hint: "[format_scope] [style_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /code format - Advanced Code Formatting

Sophisticated code formatting system with intelligent styling, consistency enforcement, and automated quality improvements.

## Usage
```bash
/code format project                         # Project-wide formatting
/code format --style-guide                   # Style guide enforcement
/code format --intelligent                   # Intelligent formatting optimization
/code format --comprehensive                 # Comprehensive formatting and cleanup
```

## Workflow

The `/code format` command follows a systematic process to format code.

```xml
<code_formatting_workflow>
  <step name="Detect Language & Style Guide">
    <description>Analyze the files to detect the programming language and any project-specific style guide configurations (e.g., `.prettierrc`, `pyproject.toml`).</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read configuration files to identify the style guide.</description>
    </tool_usage>
  </step>
  
  <step name="Apply Formatting">
    <description>Apply language-specific formatting rules to the target files, fixing indentation, sorting imports, and enforcing the detected style guide.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate formatting tool (e.g., Prettier, Black, gofmt) on the target files.</description>
    </tool_usage>
  </step>
  
  <step name="Verify & Report">
    <description>Verify that the formatting was applied correctly and generate a report summarizing the changes made.</description>
    <output>A summary of the formatting changes.</output>
  </step>
</code_formatting_workflow>
```

### Language-Specific Formatting
- **Python**: Applies Black for formatting, isort for imports, and ensures PEP 8 compliance.
- **JavaScript/TypeScript**: Uses Prettier and ESLint auto-fix capabilities.
- **Java**: Applies Google or Oracle style guides and organizes imports.
- **Go**: Runs `gofmt` and `goimports`.
- **Rust**: Applies `rustfmt`.
- **C/C++**: Applies `clang-format`.