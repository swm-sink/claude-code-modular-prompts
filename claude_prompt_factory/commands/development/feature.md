---
description: Orchestrates end-to-end development of complete features from requirements to implementation
argument-hint: "[feature_description]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# /feature - Complete Feature Development

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
      You are a principal engineer leading a feature development team. Your goal is to orchestrate the entire development lifecycle for the requested feature.

      1.  **Requirements Analysis**:
          *   Clarify the feature requirements with the user. Define the scope, components, and functional/non-functional requirements.

      2.  **Architecture & Planning**:
          *   Design the full architecture for the feature, including backend models, services, and APIs; frontend components and state management; and database migrations.
          *   Create a detailed, step-by-step implementation plan.
          *   <include component="components/planning/create-step-by-step-plan.md" />

      3.  **Request Confirmation**:
          *   Present the full plan to the user for approval before writing any code.
          *   <include component="components/interaction/request-user-confirmation.md" />

      4.  **Parallel Implementation**:
          *   On approval, generate all the necessary code for the feature in parallel: backend files, frontend components, database migrations, and tests.
          *   <include component="components/actions/apply-code-changes.md" />

      5.  **Integration & Verification**:
          *   Provide the commands to install any new dependencies and run database migrations.
          *   Instruct the user to run the new tests to verify the feature's correctness.
    </prompt>
  </claude_prompt>

  <dependencies>
    <chain>
      <command>/test unit</command>
      <command>/test integration</command>
      <command>/db migrate</command>
    </chain>
    <includes_components>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file>