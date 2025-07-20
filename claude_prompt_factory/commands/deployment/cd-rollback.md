# /cd rollback - Deployment Rollback Command

**Purpose**: Safely roll back a deployment to a previous version, with support for data integrity verification and automated incident reporting.

## Usage
```bash
/cd rollback [version]
```

## Workflow

The `/cd rollback` command follows a systematic process to safely roll back a deployment.

```xml
<rollback_workflow>
  <step name="Validate Rollback Target">
    <description>Validate that the specified rollback version is valid and available for rollback.</description>
  </step>
  
  <step name="Perform Pre-Rollback Checks">
    <description>Perform a series of pre-rollback checks to ensure that the system is in a safe state for rollback. This includes backing up the database and verifying dependencies.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run pre-rollback check scripts.</description>
    </tool_usage>
  </step>
  
  <step name="Execute Rollback">
    <description>Execute the rollback to the specified version, using the appropriate platform-specific commands (e.g., 'kubectl rollout undo', 'docker service update').</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the appropriate rollback command for the target platform.</description>
    </tool_usage>
  </step>
  
  <step name="Verify Rollback Health">
    <description>After the rollback is complete, perform a health check to verify that the system is stable and running correctly on the previous version.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run health check scripts.</description>
    </tool_usage>
  </step>
  
  <step name="Generate Incident Report">
    <description>Automatically generate an incident report that documents the rollback, including the timestamp, the target version, the reason for the rollback, and the final health status.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create the incident report file.</description>
    </tool_usage>
  </step>
</rollback_workflow>
```

## Features
- **Safe Execution**: Database backup before rollback
- **Multi-Platform**: Kubernetes, Docker, Serverless, Heroku
- **Health Verification**: Post-rollback system validation
- **Data Protection**: Maintains data integrity during rollback
- **Incident Tracking**: Automated incident report generation