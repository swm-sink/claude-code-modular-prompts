<command_file>
  <metadata>
    <name>/task</name>
    <purpose>Executes a focused, test-driven development workflow for creating or modifying a single component.</purpose>
    <usage>
      <![CDATA[
      /task "[task_description]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="task_description" type="string" required="true">
      <description>A clear description of the component to be built or modified.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Create a validation utility for email addresses using TDD.</description>
      <usage>/task "Create a validation utility for email addresses."</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a software developer practicing Test-Driven Development (TDD). The user wants you to complete a focused development task.

      Follow the Red-Green-Refactor cycle strictly:

      1.  **Analyze Requirements**:
          *   Break down the `task_description` into specific requirements and test cases.

      2.  **RED - Write Failing Tests**:
          *   First, write a comprehensive suite of tests that define the desired functionality. These tests should fail initially.
          *   Use `/test unit` to generate the test file.

      3.  **GREEN - Make Tests Pass**:
          *   Next, write the simplest possible implementation code to make all the tests pass.

      4.  **REFACTOR - Improve Code**:
          *   With the safety of the passing tests, refactor the implementation for clarity, performance, and maintainability.

      5.  **Final Verification**:
          *   Run the tests one last time to ensure everything still passes.
          *   Propose the final code for both the tests and the implementation.
          *   <include component="components/actions/apply-code-changes.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <chain>
      <command>/test unit</command>
    </chain>
    <includes_components>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>