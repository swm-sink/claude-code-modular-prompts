---
description: Advanced development environment setup with intelligent automation, dependency resolution, and platform optimization
argument-hint: "[environment_type] [automation_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /dev setup - Advanced Development Setup

Sophisticated development environment setup with intelligent automation, dependency resolution, and platform optimization.

## Usage
```bash
/dev setup full                              # Complete development environment
/dev setup --auto                            # Fully automated setup
/dev setup --docker                          # Containerized development environment
/dev setup --cloud                           # Cloud development environment
```

  <claude_prompt>
    <prompt>
      You are a development environment specialist. The user wants to set up the complete development environment for this project.

      1.  **Read Configuration**: Read the `PROJECT_CONFIG.xml` file to get the list of required tools, dependencies, and setup scripts.
      2.  **Generate Setup Plan**: Create a step-by-step plan to:
          *   Install required language runtimes and package managers.
          *   Install project dependencies (e.g., `npm install`, `pip install -r requirements.txt`).
          *   Configure development tools (linters, formatters).
          *   Set up pre-commit Git hooks.
      3.  **Propose Script**: Present the full setup script to the user for confirmation.
      4.  **Execute and Verify**: Upon approval, execute the script. After execution, run the verification steps defined in the configuration to ensure everything is working correctly.
      5.  **Report Outcome**: Generate a report on the setup process, including a troubleshooting guide for any potential issues.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>development.setup.dependencies</value>
      <value>development.setup.scripts</value>
      <value>development.setup.verification</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>