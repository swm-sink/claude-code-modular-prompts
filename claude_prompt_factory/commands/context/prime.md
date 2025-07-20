# /context prime - Standard Codebase Analysis

**Purpose**: Perform a standard analysis of the codebase to provide a high-level overview of the project.

## Usage
```bash
/context prime
```

## Workflow

The `/context prime` command follows a systematic process to perform a standard codebase analysis.

```xml
<context_prime_workflow>
  <step name="Analyze Codebase Structure">
    <description>Scan the project to understand its overall structure, including the primary language, framework, and key directories.</description>
    <tool_usage>
      <tool>Codebase Analysis</tool>
      <description>Analyze the codebase to understand the project's structure.</description>
    </tool_usage>
  </step>
  
  <step name="Analyze Dependencies">
    <description>Analyze the project's dependencies to identify key libraries and potential vulnerabilities.</description>
    <tool_usage>
      <tool>Dependency Analysis</tool>
      <description>Analyze the project's dependencies.</description>
    </tool_usage>
  </step>
  
  <step name="Identify Key Patterns">
    <description>Identify the key design patterns and coding conventions used in the project.</description>
    <tool_usage>
      <tool>Pattern Analysis</tool>
      <description>Analyze the codebase to identify key patterns.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Summary Report">
    <description>Generate a summary report of the findings, providing a high-level overview of the project.</description>
    <output>A standard codebase analysis report.</output>
  </step>
</context_prime_workflow>
```

## Use Cases

*   **New Developer Onboarding**: Quickly get a high-level overview of a new project.
*   **Project Health Check**: Perform a quick check of a project's overall health and structure.
*   **Refactoring Planning**: Get a high-level understanding of a codebase before planning a major refactoring. 