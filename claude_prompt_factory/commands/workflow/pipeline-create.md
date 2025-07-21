---
description: Advanced pipeline creation with DAG orchestration, dependency management, and automated execution
argument-hint: "[pipeline_type] [orchestration_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /pipeline create - Advanced Pipeline Builder

Sophisticated pipeline creation system with DAG orchestration, dependency management, and intelligent execution strategies.

## Usage
```bash
/pipeline create ci-cd                       # Create CI/CD pipeline
/pipeline create data-processing             # Data processing pipeline
/pipeline create --dag                       # DAG-based workflow pipeline
/pipeline create --parallel                  # Parallel execution optimization
```

## Templates
```yaml
templates:
  ci-cd:
    stages: [build, test, security-scan, deploy]
    gates: [coverage-80%, security-pass, performance-ok]
  
  feature:
    stages: [design, implement, test, review, integrate]
    gates: [design-approval, tests-pass, code-review]
  
  hotfix:
    stages: [patch, test, approve, deploy]
    gates: [critical-tests-pass, security-check]
```

## Core Logic
```yaml
creation:
  template: load predefined structure
  customize: stages and gates per requirements
  validate: dependencies and gate logic
  version: pipeline definition for tracking
  save: to .claude/pipelines/<name>.yml

stage_types:
  sequential: execute in order
  parallel: execute simultaneously
  conditional: based on gate results
  manual: require approval

quality_gates:
  automated: test coverage, security scans
  manual: code review, design approval
  performance: benchmarks, load tests
  compliance: security, legal requirements
```

## Examples
- `/pipeline create deploy-prod --template ci-cd --gates security-pass,performance-ok`
- `/pipeline create feature-auth --template feature --parallel test,security-scan`
- `/pipeline create emergency-patch --template hotfix --stages patch,test,deploy`

## Pipeline Definition
```yaml
name: deploy-prod
version: 1.0
stages:
  - name: build
    type: sequential
    commands: [/test, /build]
  - name: security
    type: parallel
    commands: [/security scan, /deps audit]
    gates: [no-high-vulns]
  - name: deploy
    type: manual
    requires: [build, security]
    gates: [approval-required]
```

## Related Commands
- `/pipeline run` - Execute pipeline
- `/flow create` - Simple workflows
- `/swarm pipeline` - Multi-agent execution 