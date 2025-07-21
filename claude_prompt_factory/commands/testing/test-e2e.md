<command_file>
  <metadata>
    <name>/test e2e</name>
    <purpose>Executes comprehensive end-to-end tests that validate complete user workflows.</purpose>
    <usage>
      <![CDATA[
      /test e2e "[workflow_name]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="workflow" type="string" required="true">
      <description>The name of the user workflow to test (e.g., 'user-registration', 'product-purchase').</description>
    </argument>
  </arguments>

  <examples>
    <example>
      <description>Run the end-to-end test for the user registration workflow.</description>
      <usage>/test e2e "user-registration"</usage>
    </example>
    <example>
      <description>Run the end-to-end test for the full checkout process.</description>
      <usage>/test e2e "checkout-process"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are an E2E test automation engineer. The user wants to run an end-to-end test for a specific user workflow.

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
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>testing.e2e_framework</value>
      <value>testing.e2e_test_command</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>