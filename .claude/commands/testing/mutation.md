---
name: /mutation
description: "Performs mutation testing to assess the effectiveness of existing test suites"
usage: "[target_file] [auto_fix]"
tools: Read, Write, Bash, Edit
---
# /test mutation - Mutation Testing
Performs mutation testing to assess the effectiveness of an existing test suite by introducing deliberate bugs.
## Usage
```bash
/test mutation "src/utils/stringUtils.js"              # Basic mutation testing
/test mutation "src/core/authService.js" auto_fix=true # Auto-generate missing tests
```
## Arguments
- `target_file` (required): File containing code to be mutation-tested
- `auto_fix` (optional): Auto-generate tests for surviving mutants (default: false)
## What It Does
1. **Analyze**: Reads target file and corresponding test file
2. **Generate Mutants**: Creates deliberate bugs in source code
3. **Test Mutants**: Runs test suite against each mutant
4. **Report**: Calculates mutation score and lists survivors
5. **Auto-Fix**: Optionally generates tests to kill survivors
<command_file>
  <metadata>
    <name>/test mutation</name>
    <purpose>Performs mutation testing to assess the effectiveness of an existing test suite.</purpose>
    <usage>
      <![CDATA[
      /test mutation "[target_file]" <auto_fix=false>
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="target" type="string" required="true">
      <description>The file containing the code to be mutation-tested.</description>
    </argument>
    <argument name="auto_fix" type="boolean" required="false" default="false">
      <description>If true, automatically generates new tests to kill surviving mutants.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Run mutation testing on a specific utility file.</description>
      <usage>/test mutation "src/utils/stringUtils.js"</usage>
    </example>
    <example>
      <description>Run mutation testing and automatically generate tests for any surviving mutants.</description>
      <usage>/test mutation "src/core/authService.js" auto_fix=true</usage>
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
      <![CDATA[
You are a quality assurance engineer specializing in mutation testing. The user wants to assess the quality of their tests for a specific file.
      1.  **Analyze Code and Tests**:
          *   Read the `target` file and its corresponding test file.
      2.  **Generate Mutants**:
          *   Create a set of "mutants" by introducing small, deliberate bugs into the source code (e.g., changing `<` to `<=`, negating a boolean, changing a `+` to a `-`).
      3.  **Run Tests Against Mutants**:
          *   For each mutant, run the existing test suite against it.
          *   If the tests fail, the mutant is "killed."
          *   If the tests pass, the mutant "survived," indicating a gap in the test suite.
      4.  **Generate Report**:
          *   Calculate the mutation score (percentage of mutants killed).
          *   Provide a report listing all surviving mutants and the specific code change that was not caught by the tests.
          *   
]]>
      <include component="components/reporting/generate-structured-report.md" />
      <![CDATA[
      5.  **Fix Survivors (Optional)**:
          *   If `auto_fix` is true, for each surviving mutant, generate a new test case that specifically "kills" it and add it to the test suite.
          *   
]]>
      <include component="components/actions/apply-code-changes.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <uses_config_values>
      <value>testing.mutation_tool</value>
    </uses_config_values>
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
      <component>components/reporting/generate-structured-report.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>