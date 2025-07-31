---
name: /pipeline
description: Unified intelligent pipeline orchestration with creation, execution, monitoring, deployment, and CI/CD integration (v2.0)
version: 2.0
usage: /pipeline [mode] [pipeline_name] [options] [--dry-run] [--validate]
category: devops
allowed-tools:
- Task
- TodoWrite
- Read
- Write
- Edit
- MultiEdit
- Bash
- Grep
- Glob
- WebSearch
dependencies:
- /ci-setup
- /ci-run
- /deploy
- /cd-rollback
- /dag-orchestrate
validation:
  pre-execution: Validate pipeline configuration and dependencies
  during-execution: Monitor pipeline stages and resource usage
  post-execution: Verify pipeline success and artifact generation
progressive-disclosure:
  layer-integration: Layer 1 provides simple pipeline runs, Layer 2 offers mode selection, Layer 3 enables full orchestration control
  quick-start: /pipeline (auto-detects and runs appropriate pipeline)
  advanced-usage: Multi-mode orchestration with parallel execution and quality gates
safety-mechanisms:
  - Pipeline validation before execution
  - Resource limit enforcement
  - Stage-level rollback capability
  - Dependency conflict resolution
error-recovery:
  stage-failure: Retry with backoff or skip non-critical stages
  resource-exhaustion: Queue management and priority execution
  dependency-issues: Automatic resolution or clear guidance
  configuration-errors: Validation feedback with examples
---
# /pipeline - Unified Pipeline Orchestration for lusaka (v2.0)

## V2.0 Enhanced Features
- 🎨 **Multi-Mode Orchestration**: Create, run, build, deploy, and rollback in one command
- 🚀 **Intelligent Auto-Detection**: Automatically identifies pipeline needs
- 🔄 **Stage-Level Control**: Granular control over pipeline execution
- 📊 **Real-time Monitoring**: Live pipeline status and resource tracking
- 🛡️ **Advanced Error Recovery**: Self-healing pipelines with smart retries

Comprehensive pipeline orchestration for lusaka combining creation, execution, monitoring, deployment, GitHub Actions setup, and build automation optimized for Python and 1-5 developers teams.

## Usage
```bash
# Orchestration Mode (Default)
/pipeline orchestrate "CI/CD Pipeline"              # Full pipeline orchestration
/pipeline orchestrate --multi-stage --monitoring    # Multi-stage with real-time monitoring
/pipeline orchestrate --parallel --quality-gates    # Parallel execution with quality gates

# Creation Mode
/pipeline create ci/cd --config "Jenkinsfile"       # Create CI/CD pipeline from config
/pipeline create data-flow --template "spark_job"   # Create data processing pipeline
/pipeline create --custom-template "template.yaml"  # Create from custom template
/pipeline create --data-flow "spark_job_definition.py" # Create data flow pipeline for Spark job

# Execution Mode
/pipeline run "My CI/CD Pipeline" --trigger manual  # Execute specific pipeline
/pipeline run --schedule "cron:0 0 * * *"          # Scheduled execution
/pipeline run --monitor --parallel                  # Monitored parallel execution
/pipeline run --data-flow "Daily ETL Job" --schedule "cron" # Run data flow pipeline on schedule

# Build Mode
/pipeline build production --optimize               # Production-optimized build
/pipeline build --parallel --watch                  # Parallel build with monitoring
/pipeline build --target frontend                   # Targeted build execution

# Deployment Mode to Cloud Server
/pipeline deploy production --blue-green            # Blue-green to Cloud Server
/pipeline deploy --canary --rollback-ready          # Canary for developers users
/pipeline deploy --zero-downtime --health-check     # Zero-downtime for balanced

# Rollback Mode
/pipeline rollback "v1.2.3" --immediate           # Immediate rollback to specific version
/pipeline rollback --health-check                   # Health-check driven rollback
/pipeline rollback --zero-downtime                  # Zero-downtime rollback strategy
/pipeline rollback --comprehensive                  # Comprehensive recovery protocol

# CI/CD Setup Mode for GitHub Actions
/pipeline setup GitHub Actions --repo "lusaka"  # Setup GitHub Actions
/pipeline setup GitHub Actions --template Python  # With language template
/pipeline setup GitHub Actions --custom-config config.xml  # Custom configuration

# Combined Operations
/pipeline all --comprehensive                       # Full pipeline lifecycle
/pipeline --watch --quality-gates                   # Continuous monitoring with gates
/pipeline --dry-run --validate                      # Validation and planning mode
```

## Pipeline Orchestration Modes

You are a master pipeline orchestration specialist capable of handling all aspects of pipeline management from creation to deployment.

### ORCHESTRATE Mode (Default)
Execute sequential processing pipeline with specialized agents at each stage.

### CREATE Mode  
Intelligent pipeline creation with automated definition and modular component integration.

### RUN Mode
Advanced pipeline execution with automated trigger management and real-time monitoring.

### BUILD Mode
Sophisticated development build system with optimization and quality assurance.

### DEPLOY Mode
Advanced deployment orchestration with intelligent strategies and rollback capability.

### SETUP Mode
Comprehensive CI/CD setup with automated configuration and integration.

### ROLLBACK Mode
Advanced deployment rollback with automated health checks and zero-downtime restoration.

## V2.0 Progressive Disclosure Examples

### Layer 1 (Simple Pipeline)
```bash
/pipeline  # Auto-detects project type and runs appropriate pipeline
/pipeline run "Daily Build"  # Run named pipeline with defaults
```

### Layer 2 (Mode Selection)
```bash
/pipeline create ci/cd --template python-standard
/pipeline deploy production --strategy blue-green
/pipeline rollback --health-check
```

### Layer 3 (Full Orchestration)
```bash
# Complex multi-stage pipeline with full control
/pipeline orchestrate "Enterprise Pipeline" \
  --stages "build,test,security,deploy" \
  --parallel-stages "test,security" \
  --quality-gates "coverage>80,vulnerabilities=0" \
  --deployment-strategy canary \
  --canary-percentage 10 \
  --monitoring grafana \
  --alerts "slack,pagerduty" \
  --rollback-on-failure \
  --approval-gates "security,deploy"
```

## Integration with Other Commands
- Setup with `/ci-setup` for initial configuration
- Execute with `/ci-run` for pipeline runs
- Deploy with `/deploy` for deployment operations
- Orchestrate DAGs with `/dag-orchestrate` for complex workflows