# /pipeline run - Multi-Stage Pipeline Execution

Execute complex multi-stage pipelines with parallel execution, quality gates, and comprehensive monitoring.

## Usage
```
/pipeline run <pipeline-name> [--stage=<stage>] [--parallel] [--params key=value]
```

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