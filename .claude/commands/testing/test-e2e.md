---
name: /test-e2e
description: "Intelligent end-to-end (E2E) testing with automated test script generation, browser automation, and comprehensive reporting"
usage: "[url] [test_scenario]"
tools: Read, Write, Edit, Bash, Grep
---
# /test e2e - Intelligent End-to-End Testing
Advanced end-to-end (E2E) testing system with automated test script generation, browser automation, and comprehensive, actionable reporting.
## Usage
```bash
/test e2e "https://example.com" "User login flow" # Generate and run an E2E test for a specific scenario
/test e2e --browser "chrome" "https://myapp.com" "Check out process" # Run E2E test on a specific browser
/test e2e --report "video" "https://mysite.com" # Generate a video report of the E2E test
```
<command_file>
  <metadata>
    <n>/test e2e</n>
    <purpose>Intelligent end-to-end (E2E) testing with automated test script generation, browser automation, and comprehensive reporting</purpose>
    <usage>
      <![CDATA[
      /test e2e "[url]" "[test_scenario]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="url" type="string" required="true">
      <description>The URL of the application to test</description>
    </argument>
    <argument name="test_scenario" type="string" required="true">
      <description>The user flow or scenario to test</description>
    </argument>
    <argument name="browser" type="string" required="false" default="chromium">
      <description>The browser to run the test on (e.g., chromium, firefox, webkit)</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Generate and run an E2E test for a user login flow</description>
      <usage>/test e2e "https://my-app.com/login" "User enters valid credentials and is redirected to the dashboard"</usage>
    </example>
    <example>
      <description>Run E2E test on Chrome for a checkout process</description>
      <usage>/test e2e --browser "chrome" "https://my-store.com/checkout" "User adds an item to the cart and completes the checkout process"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>
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
<include component="components/testing/testing-framework.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/testing/testing-framework.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>testing.e2e.framework</value>
      <value>testing.e2e.video_recording</value>
    </uses_config_values>
  </dependencies>
</command_file>