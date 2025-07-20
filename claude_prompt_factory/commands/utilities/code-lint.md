# /code lint - Code Linting Command

**Purpose**: Perform comprehensive code linting with style checking, issue detection, and automated fixing capabilities.

## Usage
```bash
/code lint [path] [--fix]
```

## Workflow

The `/code lint` command follows a systematic process to lint code.

```xml
<code_linting_workflow>
  <step name="Detect Language & Linter">
    <description>Analyze the files to detect the programming language and any project-specific linter configurations (e.g., `.eslintrc`, `pyproject.toml`).</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read configuration files to identify the linter and its rules.</description>
    </tool_usage>
  </step>
  
  <step name="Run Linter & Analyze Issues">
    <description>Run the appropriate linter on the target files, performing static analysis and style checks to identify violations. Violations are categorized by severity (error, warning, info).</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate linter (e.g., ESLint, Pylint, Go vet) on the target files.</description>
    </tool_usage>
  </step>
  
  <step name="Apply Fixes & Generate Report">
    <description>If the `--fix` flag is used, apply any safe, automatic fixes. Generate a comprehensive report of the results, including a list of all violations, their severity, and any fixes that were applied.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the linter with the `--fix` flag.</description>
    </tool_usage>
    <output>A comprehensive linting report.</output>
  </step>
</code_linting_workflow>
```

## Linting Areas
- **Syntax Errors**: Invalid code structure.
- **Style Violations**: Formatting and naming conventions.
- **Code Smells**: Complexity, duplication, and dead code.
- **Type Issues**: Type annotation and compatibility problems.
- **Import Problems**: Unused, circular, or missing imports.
- **Security Issues**: Basic vulnerability patterns.