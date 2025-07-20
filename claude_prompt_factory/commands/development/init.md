# /init - Intelligent Project Initialization Wizard

**Purpose**: Analyze an existing project or set up a new one by detecting the tech stack, generating a `PROJECT_CONFIG.xml`, and configuring the Claude Code Prompt Factory.

## Usage
```bash
# Analyze the current project and start an interactive setup
/init

# Initialize for a specific technology (non-interactive)
/init --tech_stack=python --framework=django
```

## Workflow

The `/init` command acts as an intelligent wizard, following this process:

```xml
<initialization_workflow>
  <step name="Project Analysis">
    <description>Analyze the current directory to detect the project's tech stack, existing configuration, and structure. This is done by searching for key files and patterns in parallel.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob</tool>
      <description>
        - Search for `package.json`, `requirements.txt`, `pom.xml`, etc. to detect language.
        - Search for `manage.py`, `react`, `vue`, etc. to detect framework.
        - Search for database drivers and connection strings.
      </description>
    </tool_usage>
  </step>
  
  <step name="Generate Recommendations">
    <description>Based on the analysis, generate a set of recommendations for the project, including the optimal configuration for the Prompt Factory.</description>
    <output>A summary of the detected tech stack and a list of recommended setup actions.</output>
  </step>
  
  <step name="Interactive Configuration">
    <description>Present the findings and recommendations to the user and allow them to confirm or customize the configuration. If the user runs the command non-interactively, use the detected settings.</description>
    <interaction>
      <prompt>Present the detected language, framework, and database, and ask for confirmation.</prompt>
      <prompt>Ask if the user wants to set up git hooks, create directories, and generate examples.</prompt>
    </interaction>
  </step>
  
  <step name="Generate `PROJECT_CONFIG.xml`">
    <description>Create a new `PROJECT_CONFIG.xml` file tailored to the project's specific tech stack and the user's choices.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Generate the `PROJECT_CONFIG.xml` file with the appropriate settings for language, framework, database, testing, etc.</description>
    </tool_usage>
  </step>
  
  <step name="Framework Setup">
    <description>Create the necessary directories, git hooks, and example files to complete the setup of the Prompt Factory.</description>
    <tool_usage>
      <tool>Parallel Bash</tool>
      <description>
        - Create `src`, `tests`, `docs` directories.
        - Set up pre-commit git hooks.
        - Generate example files and a basic test setup.
      </description>
    </tool_usage>
  </step>
  
  <step name="Final Summary">
    <description>Provide a summary of the completed setup and instructions on how to get started using the Prompt Factory.</description>
    <output>A confirmation message with next steps.</output>
  </step>
</initialization_workflow>
```

## Example Analysis & Interaction

**Claude's Internal Monologue:**
*   *Okay, the user ran `/init`. I need to figure out what kind of project this is.*
*   *I'll run a bunch of searches in parallel: `find . -name "package.json"`, `find . -name "requirements.txt"`, `grep -r "django" .`, etc.*
*   *Results are in: I see a `requirements.txt` with `django` and `psycopg2`. This is a Python/Django project with a PostgreSQL database.*
*   *Now I'll present this to the user and ask for confirmation.*

**Claude's Output to User:**
> 🤖 **Project Analysis Complete!**
>
> I've analyzed your project and detected the following tech stack:
> *   **Language**: Python
> *   **Framework**: Django
> *   **Database**: PostgreSQL
>
> **Is this correct? (Y/n)**

This prompt-driven approach replaces the complex Python script while retaining all of its intelligent functionality, making it a true "Claude Code Native" command. 