# /ci setup - CI Pipeline Setup Command

**Purpose**: Initialize a CI/CD pipeline for the project, with support for multiple platforms, automated testing, and deployment.

## Usage
```bash
/ci setup [platform]
```

## Workflow

The `/ci setup` command follows a systematic process to create a new CI/CD pipeline.

```xml
<ci_setup_workflow>
  <step name="Detect Project Type & Platform">
    <description>Detect the project's technology stack (e.g., Node.js, Python) and the target CI/CD platform (e.g., GitHub Actions, GitLab CI).</description>
  </step>
  
  <step name="Generate Pipeline Configuration">
    <description>Generate a new pipeline configuration file (e.g., `.github/workflows/ci.yml`) with a standard set of stages: checkout, install dependencies, lint, test, build, and deploy.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create the new pipeline configuration file.</description>
    </tool_usage>
  </step>
  
  <step name="Configure Notifications">
    <description>Add configuration for notifications to the pipeline, with support for Slack, email, and GitHub status checks.</description>
  </step>
</ci_setup_workflow>
```

## Features
- **Multi-Platform**: GitHub Actions, GitLab CI, CircleCI support
- **Language Detection**: Auto-configures for Node.js, Python, Go, Rust
- **Test Integration**: Coverage reporting and quality gates
- **Docker Support**: Containerized builds and deployments
- **Artifact Management**: Build outputs and dependency caching
- **Notification Setup**: Team alerts and status updates