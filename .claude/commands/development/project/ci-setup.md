---
description: Intelligent CI/CD setup with automated pipeline creation, configuration management, and comprehensive integration with version control systems
argument-hint: "[ci_tool] [repo_url]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
removal_date: "2025-08-25"
replacement: "/pipeline setup"
---
# /ci setup - Intelligent CI/CD Setup

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/pipeline setup`

This standalone command has been consolidated into the unified `/pipeline` command. The new command provides the same functionality with improved consistency and maintainability.

---

Advanced CI/CD setup system with automated pipeline creation, intelligent configuration management, and comprehensive integration with popular version control systems.
## Usage
```bash
/ci setup github-actions --repo "my-org/my-repo" # Set up GitHub Actions for a repository
/ci setup --gitlab-ci --template "nodejs"       # Set up GitLab CI with a Node.js template
/ci setup --jenkins --custom-config "path/to/config.xml" # Set up Jenkins with a custom configuration
```
<command_file>
  <metadata>
    <n>/ci setup</n>
    <purpose>Intelligent CI/CD setup with automated pipeline creation, configuration management, and comprehensive integration with version control systems</purpose>
    <usage>
      <![CDATA[
      /ci setup [ci_tool] --repo "[repo_url]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="ci_tool" type="string" required="true" default="github-actions">
      <description>The CI/CD tool to set up (e.g., github-actions, gitlab-ci, jenkins)</description>
    </argument>
    <argument name="repo_url" type="string" required="true">
      <description>The URL of the repository to integrate with CI/CD</description>
    </argument>
    <argument name="template" type="string" required="false">
      <description>A template to use for the CI/CD pipeline configuration</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Set up GitHub Actions for a repository</description>
      <usage>/ci setup github-actions --repo "my-org/my-repo"</usage>
    </example>
    <example>
      <description>Set up GitLab CI with a Node.js template</description>
      <usage>/ci setup --gitlab-ci --template "nodejs"</usage>
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
You are an advanced CI/CD setup specialist. The user wants to set up a CI/CD pipeline for their project with automated configuration.
**CI/CD Setup Process:**
1. **Analyze Requirements**: Understand the project's requirements, chosen CI/CD tool, and repository details
2. **Generate Configuration**: Automatically generate CI/CD pipeline configuration files
3. **Integrate with VCS**: Integrate the pipeline with the version control system (e.g., GitHub, GitLab)
4. **Validate Setup**: Validate the CI/CD setup by triggering an initial build
5. **Provide Guidance**: Provide guidance on common CI/CD workflows and best practices
**Implementation Strategy:**
- Analyze the project structure, language, and deployment targets to recommend optimal CI/CD practices
- Generate boilerplate CI/CD configuration files (e.g., .github/workflows/*.yml, .gitlab-ci.yml, Jenkinsfile)
- Automate the integration with the version control system, including webhook setup and access token management
- Trigger an initial build to ensure the pipeline is correctly configured and functional
- Provide clear instructions and examples for customizing and extending the CI/CD pipeline
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/integration/cicd-integration.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
    </includes_components>
    <uses_config_values>
      <value>ci_cd.default_tool</value>
      <value>ci_cd.repo_credentials</value>
    </uses_config_values>
  </dependencies>
</command_file>