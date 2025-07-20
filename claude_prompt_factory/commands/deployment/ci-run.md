# /ci run - CI Pipeline Execution Command

**Purpose**: Execute a CI/CD pipeline, with support for progress tracking and failure handling.

## Usage
```bash
/ci run [pipeline]
```

## Workflow

The `/ci run` command follows a systematic process to execute a CI/CD pipeline.

```xml
<ci_run_workflow>
  <step name="Detect CI/CD Platform">
    <description>Detect the CI/CD platform (e.g., GitHub Actions, GitLab CI) in use by searching for known configuration files.</description>
  </step>
  
  <step name="Execute Pipeline">
    <description>Execute the specified pipeline using the appropriate platform-specific commands.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate command to trigger the CI/CD pipeline.</description>
    </tool_usage>
  </step>
  
  <step name="Monitor Progress & Handle Results">
    <description>Monitor the progress of the pipeline in real-time. If the pipeline fails, provide debug logs and error analysis. If it succeeds, generate a build report.</description>
  </step>
</ci_run_workflow>
```

## Features
- **Multi-CI Support**: GitHub Actions, GitLab CI, Jenkins, CircleCI
- **Progress Tracking**: Real-time build status updates  
- **Failure Handling**: Debug logs and error analysis
- **Build Reports**: Detailed execution summaries
- **Debug Mode**: Verbose logging for troubleshooting

## Integration
- Links to deployment commands
- Generates test reports
- Updates build badges
- Notifies team channels