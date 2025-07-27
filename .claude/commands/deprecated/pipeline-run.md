---
name: /pipeline-run
description: Intelligent pipeline execution with automated trigger management, real-time monitoring, and comprehensive error handling
argument-hint: "[pipeline_name] [trigger_type]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
removal_date: "2025-08-25"
replacement: "/pipeline run"
---
# /pipeline run - Intelligent Pipeline Execution

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/pipeline run`

This standalone command has been consolidated into the unified `/pipeline` command. The new command provides the same functionality with improved consistency and maintainability.

**Migration Guide:**
- `/pipeline-run "Pipeline Name" --trigger manual` → `/pipeline run "Pipeline Name" --trigger manual`
- `/pipeline-run --schedule "cron:0 0 * * *"` → `/pipeline run --schedule "cron:0 0 * * *"`
- `/pipeline-run --monitor --parallel` → `/pipeline run --monitor --parallel`
- All functionality has been preserved in the unified command

---

Advanced pipeline execution system with automated trigger management, real-time monitoring, and comprehensive error handling and recovery.
## Usage
```bash
/pipeline run "My CI/CD Pipeline" --trigger "manual" # Manually trigger a CI/CD pipeline
/pipeline run --data-flow "Daily ETL Job" --schedule "cron" # Run a data flow pipeline on a schedule
/pipeline run --monitor "true" "My Deployment Pipeline" # Run and monitor a deployment pipeline in real-time
```
<command_file>
  <metadata>
    <n>/pipeline run</n>
    <purpose>Intelligent pipeline execution with automated trigger management, real-time monitoring, and comprehensive error handling</purpose>
    <usage>
      <![CDATA[
      /pipeline run "[pipeline_name]" --trigger "[trigger_type]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="pipeline_name" type="string" required="true">
      <description>The name of the pipeline to execute</description>
    </argument>
    <argument name="trigger_type" type="string" required="false" default="manual">
      <description>The type of trigger for pipeline execution (e.g., manual, schedule, webhook)</description>
    </argument>
    <argument name="monitor" type="boolean" required="false" default="true">
      <description>Whether to enable real-time monitoring during pipeline execution</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Manually trigger a CI/CD pipeline</description>
      <usage>/pipeline run "My CI/CD Pipeline" --trigger "manual"</usage>
    </example>
    <example>
      <description>Run a data flow pipeline on a schedule</description>
      <usage>/pipeline run --data-flow "Daily ETL Job" --schedule "cron:0 0 * * *"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are an advanced pipeline execution specialist. The user wants to run a pipeline with automated trigger management and real-time monitoring.
**Pipeline Execution Process:**
1. **Trigger Management**: Manage pipeline triggers (manual, scheduled, event-driven)
2. **Execution Orchestration**: Orchestrate the execution of pipeline stages and tasks
3. **Real-time Monitoring**: Provide real-time monitoring and status updates during execution
4. **Error Handling &amp; Recovery**: Implement comprehensive error handling and recovery mechanisms
5. **Post-Execution Reporting**: Generate detailed reports on pipeline execution outcomes
**Implementation Strategy:**
- Implement flexible trigger mechanisms to initiate pipeline execution based on various events or schedules
- Orchestrate the execution of pipeline stages in parallel or sequentially, managing dependencies and retries
- Provide real-time visibility into pipeline progress, logs, and resource utilization through integrated monitoring
- Design robust error handling, including automatic retries, fallbacks, and notification systems
- Generate comprehensive post-execution reports with performance metrics, success/failure status, and detailed logs
<include component="components/orchestration/dag-orchestrator.md" />
<include component="components/workflow/error-handling.md" />
<include component="components/interaction/progress-reporting.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/orchestration/dag-orchestrator.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
    </includes_components>
    <uses_config_values>
      <value>pipeline.execution.default_trigger</value>
      <value>monitoring.real_time.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file>
## Core Logic
```yaml
execution:
  load: pipeline definition from .claude/pipelines/
  validate: stage dependencies and prerequisites  
  initialize: execution context with stage tracking
  execute: stages in dependency order with parallelization
  enforce: quality gates between stages
  monitor: progress, timing, and resource usage
stage_management:
  dependencies: resolve and validate stage order
  parallel: execute independent stages simultaneously
  gates: enforce quality checkpoints between stages
  rollback: atomic recovery on stage failures
monitoring:
  visibility: real-time stage progress and status
  metrics: execution time, resource usage, success rates
  logs: detailed stage execution traces
  alerts: quality gate failures and error conditions
```
## Parameters
- `pipeline-name`: Pipeline configuration to execute
- `--stage`: Start from specific stage (resume capability)
- `--parallel`: Enable parallel execution for independent stages
- `--params`: Runtime parameters (key=value pairs)
## Pipeline Format
```yaml
name: ci-cd-pipeline
stages:
  - name: test
    command: /test --coverage
    quality_gate: coverage >= 80%
    parallel_group: validation
  - name: security-scan
    command: /security scan
    parallel_group: validation
  - name: build
    command: /build --optimize
    depends_on: [test, security-scan]
  - name: deploy
    command: /deploy --env staging
    depends_on: [build]
    quality_gate: deployment_success
```
## Error Handling
- Stage-level checkpoints with atomic rollback
- Quality gate enforcement with detailed failure reports
- Parallel execution with coordinated error propagation
- Comprehensive pipeline status visibility 