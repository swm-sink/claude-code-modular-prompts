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

<command_file>
  <metadata>
    <n>/new</n>
    <purpose>Advanced project initialization with intelligent scaffolding, technology detection, and automated setup</purpose>
    <usage>
      <![CDATA[
      /new [project_type]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="project_type" type="string" required="false" default="webapp">
      <description>Type of project to initialize</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Initialize a new web application</description>
      <usage>/new webapp</usage>
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
      <include>components/planning/create-step-by-step-plan.md</include>
      <include>components/actions/apply-code-changes.md</include>
      <include>components/interaction/request-user-confirmation.md</include>
      <include>components/validation/validation-framework.md</include>

You are a friendly and expert project setup assistant. The user wants to initialize a new project for the Prompt Factory.

Guide the user through a series of questions to populate the `PROJECT_CONFIG.xml` file. Do not ask for all the information at once. Ask one question at a time, explain why you need the information, and show the user the XML block you are generating.

**Step 1: Project Metadata**
- Ask for the project name.
- Ask for the project version (defaulting to 1.0.0).
- Ask for a brief description.

**Step 2: Technology Stack**
- Ask what type of project this is (web app, API, mobile app, desktop app, library, etc.).
- Based on the project type, ask for the primary programming language/framework.
- Ask for any additional frameworks or tools they want to use.

**Step 3: Development Environment**
- Ask about their preferred IDE/editor.
- Ask about version control preferences (Git is default).
- Ask about package manager preferences.

**Step 4: Deployment and Infrastructure**
- Ask about their preferred deployment target (cloud provider, on-premise, etc.).
- Ask about any specific infrastructure requirements.

**Final Step: Generate Configuration**
- Show the complete `PROJECT_CONFIG.xml` configuration.
- Offer to create the initial project structure.
- Explain next steps for using the Prompt Factory with their project.

Always be encouraging and explain the benefits of each configuration choice. Make the process feel collaborative and educational.
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/actions/apply-code-changes.md</component>
    </includes_components>
  </dependencies>
</command_file> 