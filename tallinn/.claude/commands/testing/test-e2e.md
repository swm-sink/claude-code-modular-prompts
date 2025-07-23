---
name: /test-e2e
description: Intelligent end-to-end (E2E) testing with automated test script generation, browser automation, and comprehensive reporting
usage: /test-e2e [url] [test_scenario]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent end-to-end (E2E) testing with automated test script generation, browser automation, and comprehensive reporting

**Usage**: `/test-e2e $URL $TEST_SCENARIO $BROWSER`

## Key Arguments

- **$URL** (required): The URL of the application to test
- **$TEST_SCENARIO** (required): The user flow or scenario to test
- **$BROWSER** (optional): The browser to run the test on (e.g., chromium, firefox, webkit)

## Examples

```bash
/test e2e "https://my-app.com/login" "User enters valid credentials and is redirected to the dashboard"
```
*Generate and run an E2E test for a user login flow*

```bash
/test e2e --browser "chrome" "https://my-store.com/checkout" "User adds an item to the cart and completes the checkout process"
```
*Run E2E test on Chrome for a checkout process*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are an advanced end-to-end (E2E) testing specialist. The user wants to generate and run E2E tests for their web application.

**E2E Testing Process:**
1. **Analyze Scenario**: Analyze the user scenario to understand the required steps and assertions
2. **Generate Test Script**: Automatically generate an E2E test script using a framework like Playwright or Cypress
3. **Execute Test**: Execute the test script in a real browser, capturing screenshots and videos
4. **Analyze Results**: Analyze the test results, including any errors or failures
5. **Generate Report**: Generate a comprehensive report with test steps, assertions, and visual artifacts

**Implementation Strategy:**
- Parse the user's scenario description to generate a sequence of browser actions and assertions
- Generate a test script using a modern E2E testing framework like Playwright
- Launch a browser, navigate to the specified URL, and execute the generated test script
- Capture screenshots, videos, and browser console logs for debugging and reporting
- Generate a detailed report with a step-by-step breakdown of the test execution, including visual comparisons and performance metrics

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

