# /test e2e - End-to-End Testing Command

**Purpose**: Execute comprehensive end-to-end tests that validate complete user workflows across the entire system.

## Usage
```bash
/test e2e [workflow] [--browser=chrome|firefox]
```

## Workflow

The `/test e2e` command follows a systematic process to execute end-to-end tests.

```xml
<e2e_testing_workflow>
  <step name="Simulate User Workflow">
    <description>Simulate complete user journeys across the application, testing cross-system interactions, business process flows, and user interface behavior.</description>
    <tool_usage>
      <tool>Browser Automation</tool>
      <description>Launch browser instances, execute UI interactions, and capture screenshots/videos.</description>
    </tool_usage>
  </step>
  
  <step name="Validate System Integration">
    <description>Validate integrations with APIs, databases, and external services, ensuring data consistency and correct behavior across all system components.</description>
  </step>
  
  <step name="Perform Performance Validation">
    <description>Measure page load times, monitor resource usage, and test under realistic load to ensure the system meets performance expectations.</description>
  </step>
  
  <step name="Generate Report">
    <description>Generate a detailed end-to-end test report, including pass/fail status, performance metrics, and any issues found.</description>
    <output>A comprehensive end-to-end test report.</output>
  </step>
</e2e_testing_workflow>
```

## Features
- **User Workflow Simulation**: Simulate complete user journeys and test cross-system interactions.
- **Browser Automation**: Launch browser instances, execute UI interactions, and capture visual evidence.
- **System Integration Testing**: Validate API integrations, database transactions, and external service calls.
- **Performance Validation**: Measure page load times, monitor resource usage, and test under realistic load.

## Quality Gates
- All critical user paths must pass.
- Performance must be within defined SLA thresholds.
- No console errors or warnings should be present.
- Accessibility standards should be met.
- Cross-browser compatibility must be verified.