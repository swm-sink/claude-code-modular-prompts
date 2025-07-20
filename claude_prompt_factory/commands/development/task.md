# /task - TDD Development Command

**Purpose**: Execute a focused, test-driven development workflow for creating or modifying a single component.

## Usage
```bash
/task "implement a validation utility for email addresses"
/task "create a string formatting helper"
/task "build a cache manager with TTL support"
```

## Workflow

The `/task` command strictly follows the Test-Driven Development (TDD) Red-Green-Refactor cycle.

```xml
<tdd_workflow>
  <step name="Analyze Requirements">
    <description>Parse the task description to understand the core requirements, identify key functionality, and determine the necessary test cases.</description>
  </step>
  
  <step name="Write Tests First (Red)">
    <description>Create a comprehensive suite of failing tests that define the component's behavior, including edge cases and error conditions.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create the test file in the project's designated test directory.</description>
    </tool_usage>
  </step>
  
  <step name="Implement Solution (Green)">
    <description>Write the minimal amount of code necessary to make the previously written tests pass.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create the implementation file in the project's source directory.</description>
    </tool_usage>
  </step>
  
  <step name="Run Tests & Verify">
    <description>Execute the test suite to confirm that the new implementation passes all tests.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the project's configured test command (e.g., 'npm test', 'pytest').</description>
    </tool_usage>
  </step>
  
  <step name="Refactor">
    <description>Improve the code's structure, clarity, and performance without changing its external behavior. The test suite ensures that no functionality is broken during this phase.</description>
    <tool_usage>
      <tool>Edit</tool>
      <description>Apply refactoring changes to the implementation file.</description>
    </tool_usage>
  </step>
  
  <step name="Final Verification">
    <description>Run the test suite one final time to ensure that the refactored code still passes all tests and meets all quality gates (e.g., test coverage).</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the test command again and check for coverage.</description>
    </tool_usage>
  </step>
</tdd_workflow>
```

## Configuration

Customize behavior via `PROJECT_CONFIG.xml`:
```xml
<project_config>
  <commands>
    <task>
      <test_framework>jest</test_framework>
      <test_directory>__tests__</test_directory>
      <coverage_threshold>90</coverage_threshold>
      <style_guide>airbnb</style_guide>
    </task>
  </commands>
</project_config>
```

## Examples

### Example 1: String Utility
```bash
/task "create a string truncation utility that adds ellipsis"
```

I will:
1. Write tests for truncate(str, length)
2. Test edge cases (empty strings, short strings, exact length)
3. Implement the function
4. Run tests to verify
5. Refactor for clarity

### Example 2: Data Structure
```bash
/task "implement a simple LRU cache with get and put methods"
```

I will:
1. Write tests for cache behavior
2. Test capacity limits and eviction
3. Implement using Map for O(1) operations
4. Verify with comprehensive tests
5. Add documentation

## Best Practices

1.  **Keep It Focused** - Single responsibility per task.
2.  **Test Edge Cases** - Empty inputs, boundaries, errors.
3.  **Iterate Quickly** - Small, verifiable steps.
4.  **Maintain Coverage** - Aim for >90% test coverage.
5.  **Document Behavior** - Tests serve as documentation.

---
*TDD: Write tests first, implement second, quality always*