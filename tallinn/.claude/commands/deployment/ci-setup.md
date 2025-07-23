---
name: /ci-setup
description: Intelligent CI/CD setup with automated pipeline creation, configuration management, and comprehensive integration with version control systems
usage: /ci-setup [ci_tool] [repo_url]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent CI/CD setup with automated pipeline creation, configuration management, and comprehensive integration with version control systems

**Usage**: `/ci-setup $CI_TOOL $REPO_URL $TEMPLATE`

## Key Arguments

- **$CI_TOOL** (required): The CI/CD tool to set up (e.g., github-actions, gitlab-ci, jenkins)
- **$REPO_URL** (required): The URL of the repository to integrate with CI/CD
- **$TEMPLATE** (optional): A template to use for the CI/CD pipeline configuration

## Examples

```bash
/ci setup github-actions --repo "my-org/my-repo"
```
*Set up GitHub Actions for a repository*

```bash
/ci setup --gitlab-ci --template "nodejs"
```
*Set up GitLab CI with a Node.js template*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md

 components/integration/cicd-integration.md
 components/planning/create-step-by-step-plan.md
 components/deployment/pipeline-templates.md
 components/security/secrets-management.md
 components/quality/best-practices-enforcement.md
 
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

## Essential Component Logic

### Input Validation

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

