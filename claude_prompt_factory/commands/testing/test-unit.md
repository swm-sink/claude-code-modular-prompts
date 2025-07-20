# /test unit - Unit Test Generation Command

**Purpose**: Automatically generate a comprehensive suite of unit tests for a given component, focusing on isolation, mocking, and edge case coverage.

## Usage
```bash
/test unit [file_path]
/test unit "the user validation service"
```

## Workflow

The `/test unit` command follows a systematic process to generate high-quality unit tests.

```xml
<unit_test_generation_workflow>
  <step name="Analyze Component">
    <description>Analyze the target component to understand its public API, dependencies, and logic.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read the contents of the target component's file.</description>
    </tool_usage>
  </step>
  
  <step name="Identify Test Cases">
    <description>Identify a comprehensive set of test cases to cover the component's functionality, including happy paths, edge cases, and error conditions.</description>
  </step>
  
  <step name="Generate Test Suite">
    <description>Generate a new test file with a full suite of unit tests, using the appropriate testing framework and mocking libraries as defined in `PROJECT_CONFIG.xml`.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create the new test file in the project's designated test directory.</description>
    </tool_usage>
  </step>
  
  <step name="Verify Tests">
    <description>Run the newly created tests to ensure they are working correctly. The tests should fail initially (as per TDD), and then pass once the implementation is complete.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the project's test command.</description>
    </tool_usage>
  </step>
</unit_test_generation_workflow>
```

## Configuration

The behavior of the `/test unit` command is configured in the `PROJECT_CONFIG.xml` file.

```xml
<project_config>
  <testing_strategy>
    <test_framework>
      <name>pytest</name>
      <config_file>pytest.ini</config_file>
    </test_framework>
    <mocking_library>unittest.mock</mocking_library>
  </testing_strategy>
</project_config>
```

## Output
- A new test file containing a comprehensive suite of unit tests.
- A summary of the generated tests and their coverage.

**Focus**: Generating high-quality, isolated unit tests for individual components.
