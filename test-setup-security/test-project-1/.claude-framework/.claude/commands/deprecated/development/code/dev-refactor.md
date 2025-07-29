---
name: /dev-refactor
description: "[DEPRECATED] Advanced development refactoring with intelligent code optimization, pattern recognition, and architectural improvements - use /dev refactor instead"
argument-hint: "[refactor_scope] [optimization_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
replacement: "/dev refactor"
removal_date: "2025-08-25"
---
# /dev refactor - Advanced Development Refactoring

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/dev refactor`

```bash
# Old command:
/dev refactor "src/utils.js" strategy="extract-method"

# New command:
/dev refactor "src/utils.js" --strategy extract-method
```

This standalone command has been consolidated into the unified `/dev` command. The new command provides the same functionality with improved consistency and maintainability.

---

Sophisticated development refactoring system with intelligent code optimization, pattern recognition, and comprehensive architectural improvements.
## Usage
```bash
/dev refactor architecture                   # Architectural refactoring
/dev refactor --performance                  # Performance optimization refactoring
/dev refactor --patterns                     # Design pattern improvements
/dev refactor --comprehensive                # Comprehensive code enhancement
```
<command_file>
  <metadata>
    <name>/dev refactor</name>
    <purpose>Systematically refactors code to improve structure, maintainability, and performance.</purpose>
    <usage>
      <![CDATA[
      /dev refactor "[target_file_or_directory]" <strategy="extract-method">
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="target" type="string" required="true">
      <description>The file or directory to analyze for refactoring opportunities.</description>
    </argument>
    <argument name="strategy" type="string" required="false" default="all">
      <description>The specific refactoring strategy to apply (e.g., 'extract-method', 'simplify-conditionals', 'remove-duplication').</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Automatically identify and suggest refactorings in a specific file.</description>
      <usage>/dev refactor "src/utils/helpers.js"</usage>
    </example>
    <example>
      <description>Focus on extracting long methods from a file.</description>
      <usage>/dev refactor "src/core/main.py" strategy="extract-method"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <!-- Command-specific components -->
      <include>components/context/find-relevant-code.md</include>
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/actions/apply-code-changes.md</include>
      <include>components/quality/anti-pattern-detection.md</include>
      <include>components/testing/testing-framework.md</include>
      You are a senior software engineer specializing in code quality. The user wants to refactor a specific part of the codebase.
      1.  **Analyze Code**:
          *   Analyze the provided code for "code smells" (e.g., duplication, long methods, high complexity) based on the chosen `strategy`.
      2.  **Ensure Test Coverage**:
          *   Check for existing tests covering the target code. If tests are insufficient, first generate new tests to lock in the current behavior. Use `/test unit` as a sub-task.
      3.  **Generate Refactoring Plan**:
          *   Propose a specific, step-by-step refactoring plan.
      4.  **Apply Changes Incrementally**:
          *   For each step in the plan, provide the code modification.
      5.  **Final Verification**:
          *   After applying changes, instruct the user to run the full test suite to verify that behavior is preserved.
    </prompt>
  </claude_prompt>
  <dependencies>
    <chain>
      <command>/test unit</command>
    </chain>
    <includes_components>
      <component>components/context/find-relevant-code.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>