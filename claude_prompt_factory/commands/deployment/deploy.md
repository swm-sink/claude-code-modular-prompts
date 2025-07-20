# /deploy - Deployment Pipeline Command

**Purpose**: Execute a structured, multi-stage deployment pipeline for the project, with support for different environments and quality gates.

## Usage
```bash
# Deploy to the staging environment
/deploy --target=staging

# Perform a dry run of the production deployment
/deploy --target=production --dry-run
```

## Workflow

The `/deploy` command executes a robust, multi-stage deployment pipeline. The specific commands for each stage are read from the `PROJECT_CONFIG.xml` file.

```xml
<deployment_workflow>
  <step name="Validation">
    <description>Validate that the project is in a deployable state. This includes checking the git branch, ensuring there are no uncommitted changes, and verifying that the `PROJECT_CONFIG.xml` is present.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run git commands to check branch and status.</description>
    </tool_usage>
  </step>
  
  <step name="Build">
    <description>Run the project's build commands as defined in `PROJECT_CONFIG.xml`.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Execute the build commands (e.g., 'npm run build', 'docker build').</description>
    </tool_usage>
  </step>
  
  <step name="Test">
    <description>Run the project's test suite as defined in `PROJECT_CONFIG.xml`. If the tests fail, the deployment will be aborted.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Execute the test commands (e.g., 'npm test', 'pytest').</description>
    </tool_usage>
  </step>
  
  <step name="Security Scan">
    <description>Perform a security scan of the project, checking for vulnerabilities in dependencies and for any accidentally committed secrets.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run security scanning tools (e.g., 'npm audit', 'pip-audit').</description>
    </tool_usage>
  </step>
  
  <step name="Deploy">
    <description>Run the project's deployment commands as defined in `PROJECT_CONFIG.xml`. This can include advanced rollout strategies such as blue-green or canary deployments.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Execute the deployment commands (e.g., 'kubectl apply', 'docker-compose up').</description>
    </tool_usage>
  </step>
  
  <step name="Health Check">
    <description>Perform a health check on the deployed service to ensure it is running correctly. The health check URL is defined in `PROJECT_CONFIG.xml`.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Use curl or a similar tool to check the health of the deployed service.</description>
    </tool_usage>
  </step>
  
  <step name="Rollback (on failure)">
    <description>If any of the previous steps fail, automatically execute the rollback commands defined in `PROJECT_CONFIG.xml` to restore the previous state.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Execute the rollback commands.</description>
    </tool_usage>
  </step>
</deployment_workflow>
```

## Configuration

The behavior of the `/deploy` command is configured in the `PROJECT_CONFIG.xml` file.

```xml
<project_config>
  <deployment>
    <strategy>ci-cd</strategy>
    <environments>
      <environment name="staging">
        <branch>develop</branch>
        <rollout_strategy>rolling</rollout_strategy> <!-- can be rolling, blue-green, or canary -->
        <build_commands>
          <command>npm run build:staging</command>
          <command>docker build -t my-app:staging .</command>
        </build_commands>
        <test_commands>
          <command>npm test</command>
        </test_commands>
        <deploy_commands>
          <command>kubectl apply -f k8s/staging/</command>
        </deploy_commands>
        <health_check_url>https://staging.myapp.com/health</health_check_url>
        <rollback_commands>
          <command>kubectl rollout undo deployment/my-app</command>
        </rollback_commands>
      </environment>
      <environment name="production">
        <!-- Production environment configuration -->
      </environment>
    </environments>
  </deployment>
</project_config>
```

This prompt-driven approach replaces the complex Python script while retaining all of its robust functionality, making it a true "Claude Code Native" command. 