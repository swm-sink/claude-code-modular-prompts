# /test integration - Integration Testing Command

**Purpose**: Execute comprehensive integration tests to verify component interactions and system-wide functionality.

## Usage
```bash
/test integration [scope] [--env=test|staging]
```

## Workflow

The `/test integration` command follows a systematic process to execute integration tests.

```xml
<integration_testing_workflow>
  <step name="Environment Setup">
    <description>Configure the test environment, including setting up test databases and external services, initializing test data fixtures, and setting environment variables.</description>
  </step>
  
  <step name="Component Discovery">
    <description>Identify service boundaries, map API endpoints and contracts, locate integration test suites, and analyze dependency chains.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase to discover and map components and their interactions.</description>
    </tool_usage>
  </step>
  
  <step name="Execute Tests">
    <description>Run API integration tests, database transactions, external service calls, and cross-component workflows.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the project's configured integration test command.</description>
    </tool_usage>
  </step>
  
  <step name="Validate Results">
    <description>Validate data consistency, test error propagation, verify timeout handling, and check rollback mechanisms.</description>
  </step>
</integration_testing_workflow>
```

## Output
- Integration test results by service.
- Component interaction verification.
- External dependency health checks.
- Performance metrics for integrated workflows.