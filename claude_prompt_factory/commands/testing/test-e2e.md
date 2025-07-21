---
description: End-to-end testing with user workflow simulation, cross-browser testing, and comprehensive validation
argument-hint: "[test_suite] [browser_target]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /test e2e - End-to-End Testing Framework

Advanced end-to-end testing system with user workflow simulation, cross-browser testing, and comprehensive validation.

## Usage
```bash
/test e2e all                               # Run all E2E tests
/test e2e user-flows                        # Test critical user workflows
/test e2e --browser chrome                  # Run tests in specific browser
/test e2e --headless                        # Run in headless mode
```

## Arguments

```yaml
workflow:
  type: string
  required: true
  description: The name of the user workflow to test (e.g., 'user-registration', 'product-purchase').
```

## Examples

```yaml
workflow:
  type: string
  required: true
  description: The name of the user workflow to test (e.g., 'user-registration', 'product-purchase').
```

## claude_prompt

```yaml
prompt:
  type: string
  required: true
  description: You are an E2E test automation engineer. The user wants to run an end-to-end test for a specific user workflow.

  1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to identify the E2E testing framework (e.g., Cypress, Playwright) and the command to run the tests.
  2.  **Generate Test Script (if needed)**:
      *   Analyze the `workflow` description.
      *   If a test script for this workflow doesn't exist, generate a new one using the configured E2E framework. The script should simulate the user's journey step-by-step.
  3.  **Execute Tests**:
      *   Construct the command to run the specific E2E test for the workflow.
      *   Present the command to the user for execution.
  4.  **Generate Report**:
      *   After execution, create a detailed report summarizing the results.
      *   Include pass/fail status for each step in the workflow, performance metrics (e.g., page load times), and screenshots or videos on failure.
      *   <include component="components/reporting/generate-structured-report.md" />
```

## Dependencies

```yaml
dependencies:
  uses_config_values:
    type: array
    items:
      type: string
    description: The names of the configuration values to use.
  includes_components:
    type: array
    items:
      type: string
    description: The names of the components to include.
```

<include component="components/orchestration/dag-orchestrator.md" />
<include component="components/planning/create-step-by-step-plan.md" />
<include component="components/interaction/progress-reporting.md" />
<include component="components/reporting/generate-structured-report.md" />