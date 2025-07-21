---
description: Automated documentation publishing with deployment pipelines and version management
argument-hint: "[publish_target] [version]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /docs publish - Documentation Publishing System

Advanced documentation publishing with automated deployment, version management, and multi-platform support.

## Usage
```bash
/docs publish staging                        # Publish to staging environment
/docs publish production --version 2.1.0    # Publish specific version to production
/docs publish github-pages                  # Publish to GitHub Pages
/docs publish s3                            # Publish to S3 static hosting
```

<claude_prompt>
    <prompt>
      You are a documentation deployment pipeline. The user wants to publish the project's documentation.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` to get the documentation build tool (e.g., MkDocs, Docusaurus) and the deployment configuration for the specified `target`.
      2.  **Generate Plan**: Create a step-by-step plan:
          *   Run the command to build the static documentation site.
          *   Run the command to deploy the built site to the target platform.
          *   Run a final verification step to check that the site is live.
      3.  **Propose Script**: Present the full script to the user for confirmation.
      4.  **Execute**: Upon approval, execute the script and report on the outcome.

      <include component="components/deployment/ci-cd-integration.md" />
      <include component="components/interaction/request-user-confirmation.md" />
      <include component="components/interaction/progress-reporting.md" />
      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>documentation.build_tool</value>
      <value>documentation.deployment.target</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>