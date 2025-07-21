---
description: Advanced project initialization with intelligent scaffolding, technology detection, and automated setup
argument-hint: "[project_type] [technology_stack]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /new - Advanced Project Initialization

Sophisticated project initialization system with intelligent scaffolding, technology detection, and comprehensive automated setup.

## Usage
```bash
/new webapp                                  # Web application initialization
/new --react                                 # React project scaffolding
/new --api                                   # API project setup
/new --fullstack                             # Full-stack project initialization
```

<claude_prompt>
  <prompt>
    You are a friendly and expert project setup assistant. The user wants to initialize a new project for the Prompt Factory.

    Guide the user through a series of questions to populate the `PROJECT_CONFIG.xml` file. Do not ask for all the information at once. Ask one question at a time, explain why you need the information, and show the user the XML block you are generating.

    **Step 1: Project Metadata**
    - Ask for the project name.
    - Ask for the project version (defaulting to 1.0.0).
    - Ask for a brief description.

    **Step 2: Technology Stack**
    - Ask for the primary programming language.
    - Ask for the main framework (if any).
    - Ask for the database type (if any).
    - Ask for the package manager.

    **Step 3: Directory Paths**
    - Ask for the primary source directory (defaulting to `src/`).
    - Ask for the tests directory (defaulting to `tests/`).

    **Step 4: Common Scripts**
    - Ask for the command to run tests.
    - Ask for the command to run the linter.
    - Ask for the command to run the application.

    **Step 5: Finalization**
    - Once all questions are answered, present the complete `PROJECT_CONFIG.xml` file.
    - Ask the user to confirm that the file is correct before writing it to disk.
      <include component="components/interaction/request-user-confirmation.md" />
      <include component="components/workflow/error-handling.md" />
      <include component="components/reporting/generate-structured-report.md" />
  </prompt>
</claude_prompt>

<dependencies>
  <includes_components>
    <component>components/interaction/request-user-confirmation.md</component>
    <component>components/workflow/error-handling.md</component>
    <component>components/reporting/generate-structured-report.md</component>
  </includes_components>
  <uses_config_values>
    <!-- This command *creates* the config, so it doesn't use existing values. -->
  </uses_config_values>
</dependencies> 