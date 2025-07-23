---
name: /new
description: Advanced project initialization with intelligent scaffolding, technology detection, and automated setup
usage: /new [project_type] [technology_stack]
tools: Read, Write, Edit, Bash, Grep
---

# Advanced project initialization with intelligent scaffolding, technology detection, and automated setup

**Usage**: `/new $PROJECT_TYPE`

## Key Arguments

- **$PROJECT_TYPE** (optional): Type of project to initialize

## Examples

```bash
/new webapp
```
*Initialize a new web application*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/planning/create-step-by-step-plan.md
 components/actions/apply-code-changes.md
 components/interaction/request-user-confirmation.md
 components/validation/yaml-frontmatter.md

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

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

