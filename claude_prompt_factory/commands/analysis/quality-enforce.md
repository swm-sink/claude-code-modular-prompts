# /quality enforce - Quality Gate Enforcement Command

**Purpose**: Enforce code quality standards by applying a set of configurable quality gates. This command can be used to block commits, merges, or deployments if the code does not meet the required quality thresholds.

## Usage
```bash
/quality enforce [scope] [--strict]
```

## Workflow

The `/quality enforce` command follows a systematic process to validate the codebase against a set of quality gates.

```xml
<enforcement_workflow>
  <step name="Load Quality Gates">
    <description>Load the project's quality gates from the `PROJECT_CONFIG.xml` file. This includes thresholds for test coverage, code complexity, and security vulnerabilities.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read the `<quality_standards>` section of `PROJECT_CONFIG.xml`.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Codebase">
    <description>Perform a comprehensive analysis of the codebase to measure the current state of the code against the defined quality gates.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase to collect all necessary metrics.</description>
    </tool_usage>
  </step>
  
  <step name="Evaluate Quality Gates">
    <description>Compare the measured metrics against the configured thresholds to determine if the code passes or fails the quality gates.</description>
  </step>
  
  <step name="Generate Report & Enforce">
    <description>Generate a detailed report of the quality gate evaluation. If any of the gates have failed, and the command is run in strict mode, it will exit with a non-zero status code, which can be used to block a CI/CD pipeline.</description>
    <output>A detailed report of the quality gate evaluation and a pass/fail status.</output>
  </step>
</enforcement_workflow>
```

## Quality Gates

The following quality gates can be configured in `PROJECT_CONFIG.xml`:

*   **Test Coverage**: Minimum line and branch coverage.
*   **Code Complexity**: Maximum cyclomatic and cognitive complexity.
*   **Security**: Maximum number of critical, high, and medium severity vulnerabilities.
*   **Coding Standards**: Adherence to linting rules, naming conventions, and documentation standards.