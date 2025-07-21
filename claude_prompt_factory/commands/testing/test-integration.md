---
description: Integration testing with service interaction validation, API testing, and system integration verification
argument-hint: "[integration_scope] [test_environment]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /test integration - Integration Testing Framework

Advanced integration testing system with service interaction validation, API testing, and comprehensive system integration verification.

## Usage
```bash
/test integration api                        # Test API integrations
/test integration database                   # Test database integrations
/test integration services                   # Test microservice integrations
/test integration --environment staging     # Run on specific environment
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

<include component="components/analysis/dependency-mapping.md" />
<include component="components/orchestration/dag-orchestrator.md" />
<include component="components/interaction/progress-reporting.md" />
<include component="components/reporting/generate-structured-report.md" />