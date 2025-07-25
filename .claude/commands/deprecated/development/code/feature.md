---
description: [DEPRECATED] Orchestrates end-to-end development of complete features from requirements to implementation - use /dev feature instead
argument-hint: "[feature_description]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
deprecated: true
deprecation_date: "2025-07-25"
replacement: "/dev feature"
removal_date: "2025-08-25"
---
# /feature - Complete Feature Development

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/dev feature`

```bash
# Old command:
/feature "User profile management with avatar upload"

# New command:
/dev feature "User profile management with avatar upload"
```

This standalone command has been consolidated into the unified `/dev` command. The new command provides the same functionality with improved consistency and maintainability.

---

Orchestrates the end-to-end development of a complete feature, from requirements to implementation and testing.
## Usage
```bash
/feature "User profile management with avatar upload"
/feature "Shopping cart with persistent sessions"
```
## Arguments
- `feature_description` (required): Clear, high-level description of the feature to be built
## What It Does
1. **Requirements Analysis**: Clarifies scope and requirements
2. **Architecture & Planning**: Designs full feature architecture  
3. **Request Confirmation**: Presents plan for user approval
4. **Parallel Implementation**: Generates all necessary code
5. **Integration & Verification**: Provides setup and testing instructions
<command_file>
  <metadata>
    <name>/feature</name>
    <purpose>Orchestrates the end-to-end development of a complete feature, from requirements to implementation and testing.</purpose>
    <usage>
      <![CDATA[
      /feature "[feature_description]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="feature_description" type="string" required="true">
      <description>A clear, high-level description of the feature to be built.</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Develop a complete user profile management feature.</description>
      <usage>/feature "User profile management with ability to edit display name, bio, and upload an avatar."</usage>
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
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/actions/apply-code-changes.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>
      <![CDATA[
You are a principal engineer leading a feature development team. Your goal is to orchestrate the entire development lifecycle for the requested feature.
      1.  **Requirements Analysis**:
          *   Clarify the feature requirements with the user. Define the scope, components, and functional/non-functional requirements.
      2.  **Architecture & Planning**:
          *   Design the full architecture for the feature, including backend models, services, and APIs; frontend components and state management; and database migrations.
          *   Create a detailed, step-by-step implementation plan.
      3.  **Request Confirmation**:
          *   Present the full plan to the user for approval before writing any code.
      4.  **Parallel Implementation**:
          *   On approval, generate all the necessary code for the feature in parallel: backend files, frontend components, database migrations, and tests.
      5.  **Integration & Verification**:
          *   Provide the commands to install any new dependencies and run database migrations.
          *   Instruct the user to run the new tests to verify the feature's correctness.
      ]]>
    </prompt>
  </claude_prompt>
  <dependencies>
    <chain>
      <command>/test unit</command>
      <command>/test integration</command>
      <command>/db migrate</command>
    </chain>
    <includes_components>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/workflow/report-generation.md</component>
    </includes_components>
  </dependencies>
</command_file>