---
description: Advanced CI execution with intelligent pipeline optimization, parallel processing, and automated quality gates
argument-hint: "[execution_mode] [optimization_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /deploy ci-run - Advanced CI Execution

Sophisticated CI execution system with intelligent pipeline optimization, parallel processing, and automated quality gates.

## Usage
```bash
/deploy ci-run optimized                     # Optimized CI execution
/deploy ci-run --parallel                    # Parallel pipeline execution
/deploy ci-run --quality-gates               # Quality-gated CI execution
/deploy ci-run --comprehensive               # Comprehensive CI orchestration
```

<command_file>
  <metadata>
    <name>/ci run</name>
    <purpose>Executes a CI/CD pipeline, with support for progress tracking and failure handling.</purpose>
    <usage>
      <![CDATA[
      /ci run <pipeline_name>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="pipeline_name" type="string" required="true">
      <description>The name of the CI pipeline to execute as defined in the project's CI configuration.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Run the 'main-build' pipeline.</description>
      <usage>/ci run "main-build"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a CI/CD orchestrator. The user wants to run a specific CI pipeline.

      1.  **Read Configuration**: Read `PROJECT_CONFIG.xml` and the CI configuration file (e.g., `.github/workflows/main.yml`) to understand the available pipelines and the CI platform.
      2.  **Validate Pipeline**: Verify that the requested `pipeline_name` is a valid pipeline.
      3.  **Generate Execution Command**: Construct the platform-specific command to trigger the pipeline (e.g., using `gh workflow run`, `glab ci run`).
      4.  **Monitor Progress**: Propose commands to monitor the pipeline's progress and fetch the results.
      5.  **Report Results**: After completion, generate a report on the outcome.

      <include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <uses_config_values>
      <value>deployment.ci_platform</value>
      <value>deployment.ci_config_file</value>
    </uses_config_values>
    <includes_components>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
  </dependencies>
</command_file>