# /code clean - Code Cleaning Command

**Purpose**: Remove dead code, optimize imports, eliminate debug statements, and clean build artifacts to improve code maintainability.

## Usage
```bash
/code clean [path] [--preview]
```

## Workflow

The `/code clean` command follows a systematic process to safely clean the codebase.

```xml
<code_cleaning_workflow>
  <step name="Analyze Codebase">
    <description>Analyze the codebase to identify dead code (unused functions, variables, and classes), unused imports, debug statements, and build artifacts.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase for cleaning opportunities.</description>
    </tool_usage>
  </step>
  
  <step name="Preview & Confirm Changes">
    <description>Present a preview of the proposed changes to the user and request confirmation before applying them. If the `--preview` flag is used, the command will exit after this step.</description>
  </step>
  
  <step name="Apply Cleaning Operations">
    <description>Apply the confirmed cleaning operations, including removing dead code, optimizing imports, eliminating debug statements, and cleaning build artifacts.</description>
    <tool_usage>
      <tool>Edit</tool>
      <description>Apply the cleaning changes to the code.</description>
      <tool>Bash</tool>
      <description>Remove build artifacts.</description>
    </tool_usage>
  </step>
  
  <step name="Verify & Report">
    <description>Verify that the cleaning operations were applied correctly and did not introduce any regressions. Generate a report summarizing the changes made.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the test suite to verify the changes.</description>
    </tool_usage>
    <output>A summary of the cleaning changes.</output>
  </step>
</code_cleaning_workflow>
```

### Language-Specific Cleaning
- **Python**: Removes unused imports, cleans `__pycache__`, and optimizes with `black` and `isort`.
- **JavaScript/TypeScript**: Cleans `node_modules` artifacts, removes unused variables, and eliminates `console.log` statements.
- **Java**: Removes unused imports, cleans `target` directories, and optimizes package structure.
- **Go**: Runs `gofmt`, removes unused imports, and cleans the mod cache.
- **Rust**: Removes unused code, cleans the `target` directory, and formats with `rustfmt`.