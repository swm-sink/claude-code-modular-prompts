# /init existing - Initialize for an Existing Project

**Purpose**: Initialize the Prompt Factory in an existing project, with a focus on deep analysis and intelligent configuration.

## Usage
```bash
/init existing
```

## Workflow

The `/init existing` command follows a systematic process to set up the Prompt Factory in an existing project.

```xml
<init_existing_workflow>
  <step name="Deep Codebase Analysis">
    <description>Perform a deep analysis of the existing codebase by running the `/context prime-mega` command. This will provide a comprehensive understanding of the project's architecture, dependencies, security, performance, and quality.</description>
    <tool_usage>
      <tool>/context prime-mega</tool>
      <description>Run a deep analysis of the codebase.</description>
    </tool_usage>
  </step>
  
  <step name="Intelligent Configuration">
    <description>Based on the deep analysis, I will generate a highly tailored `PROJECT_CONFIG.xml` file that is optimized for the project's specific needs. This will include detailed configurations for the testing framework, security policies, performance monitoring, and more.</description>
    <tool_usage>
      <tool>File System</tool>
      <description>Create the tailored `PROJECT_CONFIG.xml` file.</description>
    </tool_usage>
  </step>
  
  <step name="Onboarding & Recommendations">
    <description>I will provide a detailed onboarding guide for the Prompt Factory, including a set of recommendations for how to best use the commands to improve the existing codebase.</description>
    <output>A fully initialized and configured Prompt Factory, with a tailored onboarding guide and a set of actionable recommendations.</output>
  </step>
</init_existing_workflow>
```

## Use Cases

*   **Legacy Modernization**: Onboard the Prompt Factory to a legacy codebase to help with a modernization effort.
*   **Team Onboarding**: Quickly get a new team up to speed on an existing project by providing them with a powerful set of tools for analysis and development.
*   **Project Rescue**: Use the Prompt Factory to help rescue a project that is struggling with technical debt, performance issues, or a lack of clear direction. 