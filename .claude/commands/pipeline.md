---
description: Unified intelligent pipeline orchestration with creation, execution, monitoring, deployment, and CI/CD integration
argument-hint: "[mode] [pipeline_name] [options]"
allowed-tools: Task, TodoWrite, Read, Write, Edit, Bash, Grep, Glob
test_coverage: 0%
---
# /pipeline - Unified Pipeline Orchestration Framework
Comprehensive pipeline orchestration solution combining creation, execution, monitoring, deployment, CI/CD setup, and build automation in a single unified command.

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

# Execution Mode
/pipeline run "My CI/CD Pipeline" --trigger manual  # Execute specific pipeline
/pipeline run --schedule "cron:0 0 * * *"          # Scheduled execution
/pipeline run --monitor --parallel                  # Monitored parallel execution

# Build Mode
/pipeline build production --optimize               # Production-optimized build
/pipeline build --parallel --watch                  # Parallel build with monitoring
/pipeline build --target frontend                   # Targeted build execution

# Deployment Mode
/pipeline deploy production --blue-green            # Blue-green deployment
/pipeline deploy --canary --rollback-ready          # Canary deployment with rollback
/pipeline deploy --zero-downtime --health-check     # Zero-downtime deployment

# CI/CD Setup Mode
/pipeline setup github-actions --repo "my-repo"     # Setup GitHub Actions
/pipeline setup gitlab-ci --template nodejs         # Setup GitLab CI with template
/pipeline setup jenkins --custom-config config.xml # Setup Jenkins with custom config

# Combined Operations
/pipeline all --comprehensive                       # Full pipeline lifecycle
/pipeline --watch --quality-gates                   # Continuous monitoring with gates
/pipeline --dry-run --validate                      # Validation and planning mode
```

<command_file>
  <metadata>
    <n>/pipeline</n>
    <purpose>Unified intelligent pipeline orchestration with creation, execution, monitoring, deployment, and CI/CD integration</purpose>
    <usage>
      <![CDATA[
      /pipeline [mode] [pipeline_name] [options]
      
      Modes: orchestrate, create, run, build, deploy, setup
      Options: --trigger, --monitor, --parallel, --template, --config, --dry-run, --watch, --quality-gates
      ]]>
    </usage>
  </metadata>
  
  <arguments>
    <argument name="mode" type="string" required="false" default="orchestrate">
      <description>Pipeline operation mode: orchestrate, create, run, build, deploy, setup</description>
    </argument>
    <argument name="pipeline_name" type="string" required="false">
      <description>Name or identifier of the pipeline to operate on</description>
    </argument>
    <argument name="target" type="string" required="false" default="staging">
      <description>Target environment or build target (staging, production, frontend, backend)</description>
    </argument>
    <argument name="trigger_type" type="string" required="false" default="manual">
      <description>Pipeline trigger type: manual, schedule, webhook, event</description>
    </argument>
    <argument name="config_file" type="string" required="false">
      <description>Path to pipeline configuration file</description>
    </argument>
    <argument name="template" type="string" required="false">
      <description>Template to use for pipeline creation</description>
    </argument>
    <argument name="ci_tool" type="string" required="false" default="github-actions">
      <description>CI/CD tool for setup: github-actions, gitlab-ci, jenkins</description>
    </argument>
    <argument name="repo_url" type="string" required="false">
      <description>Repository URL for CI/CD integration</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Full pipeline orchestration with monitoring</description>
      <usage>/pipeline orchestrate "E2E CI/CD" --monitor --quality-gates</usage>
    </example>
    <example>
      <description>Create a new CI/CD pipeline from Jenkinsfile</description>
      <usage>/pipeline create ci/cd --config "Jenkinsfile"</usage>
    </example>
    <example>
      <description>Execute pipeline with parallel processing</description>
      <usage>/pipeline run "Build Pipeline" --parallel --monitor</usage>
    </example>
    <example>
      <description>Production build with optimization</description>
      <usage>/pipeline build production --optimize --parallel</usage>
    </example>
    <example>
      <description>Blue-green deployment to production</description>
      <usage>/pipeline deploy production --blue-green --health-check</usage>
    </example>
    <example>
      <description>Setup GitHub Actions for repository</description>
      <usage>/pipeline setup github-actions --repo "my-org/my-repo"</usage>
    </example>
  </examples>
  
  <claude_prompt>
    <prompt>
You are a master pipeline orchestration specialist capable of handling all aspects of pipeline management from creation to deployment. Based on the specified mode, you will execute comprehensive pipeline operations.

**Pipeline Modes and Strategies:**

## 1. ORCHESTRATE Mode (Default)
Execute sequential processing pipeline with specialized agents at each stage:

### Pipeline Definition Framework
```json
{
  "pipeline_id": "unique_identifier",
  "stages": [
    {
      "stage_id": "stage_name",
      "agent_role": "specialized_agent_type",
      "input_schema": {
        "required": ["field1", "field2"],
        "optional": ["field3"]
      },
      "output_schema": {
        "produces": ["result1", "result2"]
      },
      "processing": {
        "timeout": 300,
        "retry_count": 3,
        "error_handling": "fail|skip|default"
      },
      "parallel_group": "validation|build|deploy",
      "quality_gate": "coverage >= 80%",
      "status": "pending|running|complete|failed"
    }
  ],
  "execution_mode": "strict|flexible|parallel"
}
```

### Stage Agent Templates
- **Code Analysis Agent**: Parse structure, identify patterns, generate analysis report
- **Security Scan Agent**: Vulnerability scanning, compliance checking, security reporting
- **Test Generation Agent**: Create test cases, generate fixtures, validate coverage
- **Build Agent**: Compile, optimize, package, validate artifacts
- **Documentation Agent**: Extract needs, generate API docs, create user guides
- **Deployment Agent**: Prepare artifacts, execute deployment, verify success

### Quality Gates and Flow Control
- Input validation against schema for each stage
- Output transformation for next stage compatibility
- Parallel execution for independent stages
- Error handling with retry logic and circuit breakers
- Performance monitoring and resource tracking

## 2. CREATE Mode
Intelligent pipeline creation with automated definition and validation:

### Creation Process
1. **Requirement Analysis**: Analyze pipeline type, components, and integration needs
2. **Automated Definition**: Generate pipeline structure using YAML/JSON/DSL
3. **Component Integration**: Integrate modular components with proper data flow
4. **Validation**: Validate configuration, syntax, and dependency resolution
5. **Deployment**: Deploy to target CI/CD system and activate

### Pipeline Types
- **CI/CD Pipelines**: Build, test, deploy workflows
- **Data Flow Pipelines**: ETL, stream processing, batch jobs
- **Deployment Pipelines**: Infrastructure, application, configuration deployment
- **Custom Pipelines**: User-defined workflows with custom stages

## 3. RUN Mode
Advanced pipeline execution with intelligent monitoring and optimization:

### Execution Framework
- **Trigger Management**: Handle manual, scheduled, webhook, and event-driven triggers
- **Execution Orchestration**: Manage stage dependencies, parallel processing
- **Real-time Monitoring**: Progress tracking, resource utilization, performance metrics
- **Error Handling**: Automatic retries, fallbacks, notification systems
- **Quality Gates**: Enforce checkpoints between stages with validation

### Monitoring and Reporting
- Stage-by-stage execution tracking
- Performance metrics and resource usage
- Error tracking and recovery actions
- Quality gate validation results
- Comprehensive execution reports

## 4. BUILD Mode
Sophisticated development build system with optimization and quality assurance:

### Build Process
1. **Configuration Reading**: Parse PROJECT_CONFIG.xml and build specifications
2. **Build Planning**: Generate optimized build execution plan
3. **Parallel Processing**: Execute independent build tasks simultaneously
4. **Quality Checks**: Run automated quality assurance during build
5. **Artifact Management**: Package, validate, and prepare build outputs

### Build Targets
- **Full Build**: Complete project compilation and packaging
- **Frontend**: Client-side assets, bundling, optimization
- **Backend**: Server-side compilation, API packaging
- **Tests**: Test compilation and execution preparation
- **Production**: Optimized builds with minification and compression

## 5. DEPLOY Mode
Advanced deployment orchestration with intelligent strategies and rollback:

### Deployment Strategies
- **Blue-Green**: Zero-downtime deployments with instant rollback
- **Canary**: Gradual rollout with monitoring and automatic rollback
- **Rolling**: Sequential instance updates with health checking
- **A/B Testing**: Feature flag-based deployments for testing

### Deployment Process
1. **Environment Validation**: Verify target environment readiness
2. **Pre-deployment Checks**: Health checks, dependency validation
3. **Deployment Execution**: Strategy-specific deployment steps
4. **Health Monitoring**: Real-time application and infrastructure monitoring
5. **Rollback Planning**: Automated rollback triggers and execution

## 6. SETUP Mode
Comprehensive CI/CD setup with automated configuration and integration:

### Setup Process
1. **Project Analysis**: Understand structure, language, deployment targets
2. **Tool Configuration**: Generate CI/CD configuration files
3. **VCS Integration**: Setup webhooks, access tokens, repository integration
4. **Pipeline Validation**: Trigger initial builds to validate setup
5. **Documentation**: Provide customization guidance and best practices

### Supported CI/CD Tools
- **GitHub Actions**: Workflow files, secrets management, marketplace actions
- **GitLab CI**: Pipeline configuration, runners, registry integration
- **Jenkins**: Jenkinsfile, plugins, distributed builds
- **Custom Tools**: Extensible setup for other CI/CD platforms

## Universal Implementation Strategy

### Phase 1: Mode Detection and Validation
```python
def detect_and_validate_mode(mode, arguments):
    mode_strategies = {
        'orchestrate': OrchestrateStrategy(),
        'create': CreateStrategy(),
        'run': ExecuteStrategy(),
        'build': BuildStrategy(),
        'deploy': DeployStrategy(),
        'setup': SetupStrategy()
    }
    return mode_strategies.get(mode, mode_strategies['orchestrate'])
```

### Phase 2: Context Preparation
- Load relevant configuration files and templates
- Validate input parameters and dependencies
- Prepare execution environment and tools
- Initialize monitoring and logging systems

### Phase 3: Mode-Specific Execution
Execute the selected mode with comprehensive error handling, progress tracking, and quality validation.

### Phase 4: Unified Reporting
Generate comprehensive reports covering:
- Execution summary with timing and resource usage
- Quality metrics and gate validation results
- Error analysis and recovery actions taken
- Performance benchmarks and optimization suggestions
- Next steps and maintenance recommendations

## Error Handling and Recovery
- **Fail Fast**: Immediate pipeline termination on critical errors
- **Fail Safe**: Graceful degradation with default values
- **Retry Logic**: Exponential backoff for transient failures
- **Circuit Breaker**: Skip stages after repeated failures
- **Rollback Automation**: Automatic rollback triggers and execution

## Quality Gates and Validation
- Input/output schema validation at each stage
- Performance benchmarks and resource limits
- Security scanning and compliance checking
- Test coverage and quality thresholds
- Deployment health and availability validation

Report your pipeline operation with:
- Comprehensive execution summary with all stages and timing
- Quality metrics and validation results
- Performance analysis and resource utilization
- Error tracking and recovery actions
- Recommendations for optimization and improvement
    </prompt>
  </claude_prompt>
  
  <dependencies>
    <includes_components>
      <!-- Core Pipeline Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/orchestration/dag-orchestrator.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      
      <!-- Orchestration and Monitoring -->
      <component>components/orchestration/agent-orchestration.md</component>
      <component>components/workflow/flow-schedule.md</component>
      <component>components/intelligence/multi-agent-coordination.md</component>
      
      <!-- Planning and Execution -->
      <component>components/planning/create-step-by-step-plan.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/actions/parallel-execution.md</component>
      
      <!-- Quality and Security -->
      <component>components/quality/quality-metrics.md</component>
      <component>components/quality/framework-validation.md</component>
      <component>components/security/owasp-compliance.md</component>
      <component>components/security/secure-config.md</component>
      
      <!-- Integration and CI/CD -->
      <component>components/integration/cicd-integration.md</component>
      <component>components/testing/testing-framework.md</component>
      
      <!-- Reporting and Analytics -->
      <component>components/reporting/generate-structured-report.md</component>
      <component>components/optimization/dspy-framework.md</component>
      <component>components/meta/component-loader.md</component>
    </includes_components>
    
    <uses_config_values>
      <!-- Pipeline Configuration -->
      <value>pipeline.default_template</value>
      <value>pipeline.deployment_target</value>
      <value>pipeline.execution.default_trigger</value>
      <value>pipeline.quality.coverage_threshold</value>
      
      <!-- Build Configuration -->
      <value>build.targets.target</value>
      <value>build.optimization.level</value>
      <value>build.parallel.enabled</value>
      
      <!-- Deployment Configuration -->
      <value>deployment.environments.environment</value>
      <value>deployment.strategy.default</value>
      <value>deployment.ci_platform</value>
      <value>deployment.ci_config_file</value>
      
      <!-- CI/CD Configuration -->
      <value>ci_cd.default_tool</value>
      <value>ci_cd.repo_credentials</value>
      
      <!-- Monitoring Configuration -->
      <value>monitoring.real_time.enabled</value>
      <value>monitoring.quality_gates.enabled</value>
    </uses_config_values>
  </dependencies>
</command_file>