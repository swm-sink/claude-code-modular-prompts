# /test mutation - Mutation Testing Command

**Purpose**: Perform advanced mutation testing to assess the effectiveness of existing test suites and identify gaps in test coverage.

## Usage
```bash
/test mutation [target] [--threshold=85] [--fix-survivors]
```

## Workflow

The `/test mutation` command follows a systematic process to perform mutation testing.

```xml
<mutation_testing_workflow>
  <step name="Identify Testable Code">
    <description>Identify the testable code within the specified target, excluding non-functional code or third-party libraries.</description>
  </step>
  
  <step name="Generate Intelligent Mutations">
    <description>Generate a variety of intelligent mutations (e.g., conditional boundary changes, boolean negations, return value modifications) within the testable code.</description>
  </step>
  
  <step name="Run Tests Against Mutants">
    <description>Execute the existing test suite against each generated mutant. A successful test suite should "kill" (fail) the mutant, indicating effective test coverage.</description>
    <tool_usage>
      <tool>Bash</tool>
      <description>Run the test command against each mutant.</description>
    </tool_usage>
  </step>
  
  <step name="Identify Surviving Mutants & Generate Killing Tests">
    <description>Identify any "surviving" mutants (those that did not cause a test failure). If the `--fix-survivors` flag is used, generate new tests designed to kill these surviving mutants.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create new tests for surviving mutants.</description>
    </tool_usage>
  </step>
  
  <step name="Report Mutation Score">
    <description>Generate a detailed report of the mutation testing results, including the mutation score, a list of killed and surviving mutants, and suggestions for improving test effectiveness.</description>
    <output>A comprehensive mutation testing report.</output>
  </step>
</mutation_testing_workflow>
```

## Mutation Types
- Conditional boundary (< to <=)
- Boolean negation (!condition)
- Return value mutation
- Exception throwing removal
- Mathematical operator changes
- String literal modifications

## Output Format
```
MUTATION TESTING REPORT
━━━━━━━━━━━━━━━━━━━━━
Mutation Score: 87.3% (Target: 85%)

Mutants: 156 total
  Killed: 136 (87.2%)
  Survived: 18 (11.5%)
  Timeout: 2 (1.3%)

Top Survivors:
1. auth.js:45 - Boundary condition
   Suggestion: Add edge case test
2. utils.js:23 - Return value
   Suggestion: Test null return
```