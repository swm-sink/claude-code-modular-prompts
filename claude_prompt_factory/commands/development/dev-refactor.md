# /dev refactor - Code Refactoring Command

**Purpose**: Systematically refactor code to improve its structure, maintainability, and performance, while preserving its functionality.

## Usage
```bash
/dev refactor [target] [--strategy=extract-method]
```

## Workflow

The `/dev refactor` command follows a systematic process to safely refactor code.

```xml
<refactoring_workflow>
  <step name="Analyze Code & Identify Opportunities">
    <description>Analyze the target code to identify refactoring opportunities. This includes searching for code smells, duplication, long methods, and complex conditionals.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase for refactoring opportunities.</description>
    </tool_usage>
  </step>
  
  <step name="Plan Refactoring">
    <description>Create a detailed refactoring plan that outlines the chosen refactoring techniques, the steps involved, and the potential risks.</description>
  </step>
  
  <step name="Preserve Behavior with Tests">
    <description>Before making any changes, ensure that the code is covered by a comprehensive suite of tests. If the code is not well-tested, create new tests to lock in the current behavior.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create new tests if necessary.</description>
    </tool_usage>
  </step>
  
  <step name="Apply Changes Incrementally">
    <description>Apply the refactoring changes incrementally, running the test suite after each change to ensure that the functionality remains unchanged.</description>
    <tool_usage>
      <tool>Edit</tool>
      <description>Apply the refactoring changes.</description>
      <tool>Bash</tool>
      <description>Run the test suite.</description>
    </tool_usage>
  </step>
  
  <step name="Final Verification">
    <description>After all refactoring changes have been applied, run the full test suite one final time to verify that the code is still working correctly and that the quality has been improved.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the full test suite.</description>
    </tool_usage>
  </step>
</refactoring_workflow>
```

## Refactoring Strategies
- Extract methods/functions from long procedures
- Remove code duplication through abstraction
- Simplify complex conditional logic
- Improve naming and readability
- Optimize data structures and algorithms
- Reduce coupling and increase cohesion