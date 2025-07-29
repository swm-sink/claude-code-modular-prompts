---
name: /pipeline
description: Unified intelligent pipeline orchestration with creation, execution, monitoring, deployment, and CI/CD integration
argument-hint: "[mode] [pipeline_name] [options]"
allowed-tools: Task, TodoWrite, Read, Write, Edit, Bash, Grep, Glob
test_coverage: 0%
---
# /pipeline - Unified Pipeline Orchestration for [INSERT_PROJECT_NAME]
Comprehensive pipeline orchestration for [INSERT_PROJECT_NAME] combining creation, execution, monitoring, deployment, [INSERT_CI_CD_PLATFORM] setup, and build automation optimized for [INSERT_TECH_STACK] and [INSERT_TEAM_SIZE] teams.

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

# Deployment Mode to [INSERT_DEPLOYMENT_TARGET]
/pipeline deploy production --blue-green            # Blue-green to [INSERT_DEPLOYMENT_TARGET]
/pipeline deploy --canary --rollback-ready          # Canary for [INSERT_USER_BASE] users
/pipeline deploy --zero-downtime --health-check     # Zero-downtime for [INSERT_PERFORMANCE_PRIORITY]

# Rollback Mode
/pipeline rollback "v1.2.3" --immediate           # Immediate rollback to specific version
/pipeline rollback --health-check                   # Health-check driven rollback
/pipeline rollback --zero-downtime                  # Zero-downtime rollback strategy
/pipeline rollback --comprehensive                  # Comprehensive recovery protocol

# CI/CD Setup Mode for [INSERT_CI_CD_PLATFORM]
/pipeline setup [INSERT_CI_CD_PLATFORM] --repo "[INSERT_PROJECT_NAME]"  # Setup [INSERT_CI_CD_PLATFORM]
/pipeline setup [INSERT_CI_CD_PLATFORM] --template [INSERT_PRIMARY_LANGUAGE]  # With language template
/pipeline setup [INSERT_CI_CD_PLATFORM] --custom-config config.xml  # Custom configuration

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
      
      Modes: orchestrate, create, run, build, deploy, setup, rollback
      Options: --trigger, --monitor, --parallel, --template, --config, --dry-run, --watch, --quality-gates
      ]]>
    </usage>
  </metadata>
  
  <arguments>
    <argument name="mode" type="string" required="false" default="orchestrate">
      <description>Pipeline operation mode: orchestrate, create, run, build, deploy, setup, rollback</description>
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
    <argument name="monitor" type="boolean" required="false" default="true">
      <description>Whether to enable real-time monitoring during pipeline execution</description>
    </argument>
    <argument name="ci_tool" type="string" required="false" default="github-actions">
      <description>CI/CD tool for setup: github-actions, gitlab-ci, jenkins</description>
    </argument>
    <argument name="repo_url" type="string" required="false">
      <description>Repository URL for CI/CD integration</description>
    </argument>
    <argument name="version" type="string" required="false">
      <description>Specific version or tag to roll back to</description>
    </argument>
    <argument name="rollback_strategy" type="string" required="false" default="immediate">
      <description>Rollback strategy: immediate, health-check, zero-downtime, comprehensive</description>
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
      <description>Create a data flow pipeline for a Spark job</description>
      <usage>/pipeline create --data-flow "spark_job_definition.py"</usage>
    </example>
    <example>
      <description>Execute pipeline with parallel processing</description>
      <usage>/pipeline run "Build Pipeline" --parallel --monitor</usage>
    </example>
    <example>
      <description>Run a data flow pipeline on a schedule</description>
      <usage>/pipeline run --data-flow "Daily ETL Job" --schedule "cron:0 0 * * *"</usage>
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
    <example>
      <description>Immediate rollback to specific version</description>
      <usage>/pipeline rollback "v1.2.3" --immediate</usage>
    </example>
    <example>
      <description>Zero-downtime rollback with health checks</description>
      <usage>/pipeline rollback --zero-downtime --health-check</usage>
    </example>
  </examples>
  
  <claude_prompt>
    <prompt>
<!-- Include Security Wrapper for Command Injection Prevention -->
<include>components/security/command-security-wrapper.md</include>

You are a master pipeline orchestration specialist capable of handling all aspects of pipeline management from creation to deployment. Based on the specified mode, you will execute comprehensive pipeline operations.

**CRITICAL SECURITY ENFORCEMENT - NO EXCEPTIONS:**
- ALL user inputs MUST be validated using security wrapper functions before any bash execution
- ALL pipeline commands MUST be validated against PIPELINE_ALLOWED_COMMANDS allowlist
- ALL repository URLs MUST be validated using validateRepositoryURL()
- ALL version numbers MUST be validated using validateVersionNumber()
- ALL environment names MUST be validated using validateEnvironmentName()
- ALL file paths MUST be validated using validateFilePath() to prevent path traversal
- ALL bash executions MUST use executeSecureCommand() wrapper
- ALL error messages MUST be sanitized using sanitizeErrorMessage()

**Pipeline Modes and Strategies:**

## 1. ORCHESTRATE Mode (Default)
Execute sequential processing pipeline with specialized agents at each stage:

### Pipeline Definition Framework
```json
{
  "pipeline_id": "unique_identifier", // SECURITY: Validate against alphanumeric pattern
  "stages": [
    {
      "stage_id": "stage_name", // SECURITY: Sanitize stage names
      "agent_role": "specialized_agent_type",
      "input_schema": {
        "required": ["field1", "field2"], // SECURITY: Validate all field names
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
Intelligent pipeline creation with automated definition, modular component integration, and comprehensive validation:

### Creation Process (from pipeline-create) - SECURITY ENHANCED
1. **SECURITY INPUT VALIDATION**: Validate ALL user inputs using sanitizeShellInput()
2. **Requirement Analysis**: Analyze pipeline requirements, type, and components
3. **SECURITY COMMAND VALIDATION**: Validate pipeline type against allowed templates
4. **Automated Definition**: Automatically define the pipeline structure and stages
5. **SECURITY PATH VALIDATION**: Validate all configuration file paths using validateFilePath()
6. **Component Integration**: Integrate modular components and tasks into the pipeline
7. **SECURITY CONFIGURATION VALIDATION**: Validate pipeline configuration against security policies
8. **Validation**: Validate the pipeline configuration and dependencies
9. **SECURITY DEPLOYMENT VALIDATION**: Apply security checks before deployment
10. **Deployment & Activation**: Deploy and activate the created pipeline using secure execution

### Implementation Strategy
- Analyze pipeline requirements to determine optimal structure and orchestration
- Automatically generate pipeline definitions using YAML, JSON, or DSLs (e.g., Jenkinsfile, GitLab CI config)
- Integrate modular components into the pipeline, ensuring proper data flow and execution order
- Validate the pipeline configuration for correctness, syntax, and dependency resolution
- Deploy the pipeline to the target CI/CD or workflow orchestration system and activate it for execution

### Pipeline Types
- **CI/CD Pipelines**: Build, test, deploy workflows from Jenkinsfile or config
- **Data Flow Pipelines**: ETL, stream processing, batch jobs (Spark, etc.)
- **Deployment Pipelines**: Infrastructure, application, configuration deployment
- **Custom Pipelines**: User-defined workflows with custom templates

## 3. RUN Mode
Advanced pipeline execution with automated trigger management, real-time monitoring, and comprehensive error handling:

### Pipeline Execution Process (from pipeline-run) - SECURITY ENHANCED
1. **SECURITY VALIDATION**: Validate pipeline name and all parameters using security wrapper
2. **SECURITY COMMAND ALLOWLIST**: Validate ALL commands against PIPELINE_ALLOWED_COMMANDS
3. **Trigger Management**: Manage pipeline triggers (manual, scheduled, event-driven)
4. **SECURITY PARAMETER SANITIZATION**: Sanitize all execution parameters
5. **Execution Orchestration**: Orchestrate execution using secure command wrappers
6. **Real-time Monitoring**: Provide real-time monitoring with sanitized status updates
7. **SECURITY ERROR HANDLING**: Implement secure error handling with sanitized messages
8. **Error Handling & Recovery**: Implement comprehensive error handling and recovery mechanisms
9. **SECURITY AUDIT LOGGING**: Log all security-relevant events for audit
10. **Post-Execution Reporting**: Generate detailed reports with sanitized execution outcomes

### Implementation Strategy
- Implement flexible trigger mechanisms to initiate pipeline execution based on various events or schedules
- Orchestrate the execution of pipeline stages in parallel or sequentially, managing dependencies and retries
- Provide real-time visibility into pipeline progress, logs, and resource utilization through integrated monitoring
- Design robust error handling, including automatic retries, fallbacks, and notification systems
- Generate comprehensive post-execution reports with performance metrics, success/failure status, and detailed logs

### Core Logic (from pipeline-run)
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

### Pipeline Format
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

### Error Handling (from pipeline-run)
- Stage-level checkpoints with atomic rollback
- Quality gate enforcement with detailed failure reports
- Parallel execution with coordinated error propagation
- Comprehensive pipeline status visibility

### Monitoring and Reporting
- Stage-by-stage execution tracking with real-time status
- Performance metrics and resource usage monitoring
- Error tracking and automated recovery actions
- Quality gate validation results and failure analysis
- Comprehensive execution reports with timing and logs

## 4. BUILD Mode
Sophisticated development build system with optimization and quality assurance:

### Build Process - SECURITY ENHANCED
1. **SECURITY CONFIGURATION VALIDATION**: Validate PROJECT_CONFIG.xml against security schema
2. **Configuration Reading**: Parse PROJECT_CONFIG.xml and build specifications with path validation
3. **SECURITY BUILD PARAMETER VALIDATION**: Validate all build parameters using sanitizeShellInput()
4. **Build Planning**: Generate optimized build execution plan with security constraints
5. **SECURITY COMMAND VALIDATION**: Validate all build commands against PIPELINE_ALLOWED_COMMANDS
6. **Parallel Processing**: Execute independent build tasks using secure command wrappers
7. **Quality Checks**: Run automated quality assurance during build with security scanning
8. **SECURITY ARTIFACT VALIDATION**: Validate all artifacts before packaging
9. **Artifact Management**: Package, validate, and prepare build outputs with secure operations

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

### Deployment Process - SECURITY ENHANCED
1. **SECURITY ENVIRONMENT VALIDATION**: Validate environment name using validateEnvironmentName()
2. **Environment Validation**: Verify target environment readiness with security checks
3. **SECURITY CREDENTIAL VALIDATION**: Validate deployment credentials and permissions
4. **Pre-deployment Checks**: Health checks, dependency validation with security scanning
5. **SECURITY DEPLOYMENT COMMAND VALIDATION**: Validate all deployment commands against allowlist
6. **Deployment Execution**: Strategy-specific deployment steps using secure command wrappers
7. **SECURITY MONITORING**: Real-time monitoring with sanitized logging
8. **Health Monitoring**: Real-time application and infrastructure monitoring
9. **SECURITY ROLLBACK VALIDATION**: Validate rollback mechanisms and triggers
10. **Rollback Planning**: Automated rollback triggers and execution with security auditing

## 6. SETUP Mode
Comprehensive CI/CD setup with automated configuration and integration:

### Setup Process - SECURITY ENHANCED
1. **SECURITY PROJECT PATH VALIDATION**: Validate project paths using validateFilePath()
2. **Project Analysis**: Understand structure, language, deployment targets with security scanning
3. **SECURITY CONFIGURATION VALIDATION**: Validate all configuration parameters
4. **Tool Configuration**: Generate CI/CD configuration files with secure templates
5. **SECURITY REPOSITORY URL VALIDATION**: Validate repository URLs using validateRepositoryURL()
6. **VCS Integration**: Setup webhooks, access tokens, repository integration with credential protection
7. **SECURITY PIPELINE VALIDATION**: Validate pipeline configuration against security policies
8. **Pipeline Validation**: Trigger initial builds to validate setup with security scanning
9. **SECURITY DOCUMENTATION**: Generate security-focused customization guidance
10. **Documentation**: Provide customization guidance and best practices

### Supported CI/CD Tools
- **GitHub Actions**: Workflow files, secrets management, marketplace actions
- **GitLab CI**: Pipeline configuration, runners, registry integration
- **Jenkins**: Jenkinsfile, plugins, distributed builds
- **Custom Tools**: Extensible setup for other CI/CD platforms

## 7. ROLLBACK Mode
Advanced deployment rollback with intelligent recovery, automated health checks, and zero-downtime restoration:

### Rollback Strategies
- **Immediate**: Fast rollback execution with minimal validation
- **Health-Check**: Health-driven rollback with comprehensive validation
- **Zero-Downtime**: Rolling rollback maintaining service availability
- **Comprehensive**: Full recovery protocol with data integrity checks

### Rollback Process - SECURITY ENHANCED
1. **SECURITY VERSION VALIDATION**: Validate rollback version using validateVersionNumber()
2. **Risk Assessment**: Present severe warnings about rollback operations
3. **User Confirmation**: Require explicit confirmation for high-risk operations
4. **SECURITY TARGET VALIDATION**: Verify rollback version with additional security checks
5. **Target Validation**: Verify rollback version is valid and available
6. **Pre-rollback Backup**: Automated database and configuration backup
7. **SECURITY COMMAND VALIDATION**: Validate rollback commands against allowlist
8. **Platform-Specific Rollback**: Execute deployment platform rollback commands using secure wrapper
9. **Health Verification**: Post-rollback health checks and validation
10. **SECURITY AUDIT TRAIL**: Create detailed security audit trail
11. **Incident Reporting**: Generate comprehensive post-mortem reports with sanitized data

### Platform Support
- **Kubernetes**: kubectl rollout undo and deployment management
- **Docker Swarm**: Service update and rollback operations
- **Serverless**: Function version management and traffic routing
- **Custom Platforms**: Extensible rollback for additional deployment targets

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
        'setup': SetupStrategy(),
        'rollback': RollbackStrategy()
    }
    return mode_strategies.get(mode, mode_strategies['orchestrate'])
```

### Phase 2: Context Preparation - SECURITY ENHANCED
- **SECURITY VALIDATION**: Apply security wrapper to ALL user inputs before processing
- **SECURITY FILE VALIDATION**: Validate all configuration file paths using validateFilePath()
- Load relevant configuration files and templates with path traversal prevention
- **SECURITY PARAMETER VALIDATION**: Validate input parameters using appropriate security functions
- Validate input parameters and dependencies against security policies
- **SECURITY ENVIRONMENT PREPARATION**: Prepare execution environment with security constraints
- Prepare execution environment and tools with command allowlist validation
- **SECURITY AUDIT INITIALIZATION**: Initialize security audit logging and monitoring
- Initialize monitoring and logging systems with sanitized output handling

### Phase 3: Mode-Specific Execution
Execute the selected mode with comprehensive error handling, progress tracking, and quality validation.

### Special Mode: ROLLBACK Implementation
When mode is 'rollback', execute advanced deployment rollback protocol:

#### Rollback Safety Protocol
1. **EXTREME WARNING**: Present clear, severe warning about rollback risks
2. **User Confirmation**: Require explicit confirmation to proceed with high-risk operation
3. **Configuration Reading**: Read PROJECT_CONFIG.xml to determine deployment platform
4. **Target Validation**: Verify specified version is valid and available rollback target
5. **Pre-rollback Backup**: Initiate database backup via `/db backup` command chain
6. **Platform-Specific Rollback**: Execute appropriate rollback commands:
   - Kubernetes: SECURITY VALIDATED: `kubectl rollout undo deployment/app --to-revision=N` (N validated)
   - Docker Swarm: SECURITY VALIDATED: `docker service update --rollback service-name` (service-name validated)
   - Serverless: Platform-specific version rollback commands (ALL COMMANDS VALIDATED AGAINST ALLOWLIST)
7. **Health Verification**: Execute comprehensive post-rollback health checks
8. **Incident Documentation**: Generate detailed post-mortem incident report

#### Rollback Strategy Implementation - SECURITY ENHANCED
```python
def execute_rollback(version, strategy):
    # SECURITY: Validate version number format
    validated_version = validateVersionNumber(version)
    
    # SECURITY: Validate strategy against allowed options
    allowed_strategies = ['immediate', 'health-check', 'zero-downtime', 'comprehensive']
    if strategy not in allowed_strategies:
        raise SecurityError(f'Invalid rollback strategy: {strategy}')
    
    strategies = {
        'immediate': immediate_rollback(validated_version),
        'health-check': health_driven_rollback(validated_version),
        'zero-downtime': zero_downtime_rollback(validated_version),
        'comprehensive': comprehensive_recovery(validated_version)
    }
    
    # SECURITY: Execute with secure wrapper and audit logging
    return executeSecureCommand(strategies.get(strategy, strategies['immediate']))
```

### Phase 4: Unified Reporting - SECURITY ENHANCED
Generate comprehensive reports covering:
- **SECURITY AUDIT SUMMARY**: Complete security audit trail with all validation results
- Execution summary with timing and resource usage (sanitized)
- **SECURITY METRICS**: Security validation metrics and compliance status
- Quality metrics and gate validation results with security context
- **SECURITY ERROR ANALYSIS**: Sanitized error analysis and recovery actions taken
- Error analysis and recovery actions taken with information disclosure prevention
- Performance benchmarks and optimization suggestions
- **SECURITY RECOMMENDATIONS**: Security-focused maintenance and improvement recommendations
- Next steps and maintenance recommendations with security considerations

## Error Handling and Recovery - SECURITY ENHANCED
- **SECURITY ERROR SANITIZATION**: All error messages sanitized to prevent information disclosure
- **Fail Fast**: Immediate pipeline termination on critical errors with secure cleanup
- **Fail Safe**: Graceful degradation with default values (validated against security policies)
- **SECURITY AUDIT LOGGING**: All failures logged with security context
- **Retry Logic**: Exponential backoff for transient failures (with security validation on retry)
- **Circuit Breaker**: Skip stages after repeated failures with security state preservation
- **SECURITY ROLLBACK VALIDATION**: Validate all rollback operations against security policies
- **Rollback Automation**: Automatic rollback triggers and execution using secure wrappers

## Quality Gates and Validation
- Input/output schema validation at each stage
- Performance benchmarks and resource limits
- Security scanning and compliance checking
- Test coverage and quality thresholds
- Deployment health and availability validation

Report your pipeline operation with:
- **SECURITY COMPLIANCE VERIFICATION**: Confirm all security validations passed
- Comprehensive execution summary with all stages and timing (sanitized)
- **SECURITY AUDIT RESULTS**: Complete security audit trail and compliance status
- Quality metrics and validation results with security context
- Performance analysis and resource utilization (with sensitive data filtered)
- **SECURITY INCIDENT TRACKING**: Sanitized error tracking and recovery actions
- Error tracking and recovery actions with information disclosure prevention
- **SECURITY RECOMMENDATIONS**: Security-focused optimization and improvement recommendations
- Recommendations for optimization and improvement with security considerations

**MANDATORY SECURITY EXECUTION CHECKLIST:**
✓ All user inputs validated using security wrapper functions
✓ All commands validated against PIPELINE_ALLOWED_COMMANDS allowlist
✓ All file paths validated using validateFilePath()
✓ All repository URLs validated using validateRepositoryURL()
✓ All version numbers validated using validateVersionNumber()
✓ All environment names validated using validateEnvironmentName()
✓ All bash executions use executeSecureCommand() wrapper
✓ All error messages sanitized using sanitizeErrorMessage()
✓ Complete security audit trail maintained
✓ No information disclosure in outputs or error messages
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
      
      <!-- Components from pipeline-create -->
      <component>components/integration/cicd-integration.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
      
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
      
      <!-- Rollback Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/interaction/request-user-confirmation.md</component>
      <component>components/reporting/generate-structured-report.md</component>
      
      <!-- Reporting and Analytics -->
      <component>components/reporting/generate-structured-report.md</component>
      <component>components/optimization/dspy-framework.md</component>
      <component>components/meta/component-loader.md</component>
    </includes_components>
    
    <chain>
      <command>/db backup</command>
    </chain>
    
    <uses_config_values>
      <!-- Pipeline Configuration -->
      <value>pipeline.default_template</value>
      <value>pipeline.deployment_target</value>
      <value>pipeline.execution.default_trigger</value>
      <value>pipeline.quality.coverage_threshold</value>
      
      <!-- Configuration from pipeline-create -->
      <value>pipeline.default_template</value>
      <value>pipeline.deployment_target</value>
      
      <!-- Configuration from pipeline-run -->
      <value>pipeline.execution.default_trigger</value>
      <value>monitoring.real_time.enabled</value>
      
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
      
      <!-- Rollback Configuration -->
      <value>deployment.platform</value>
      <value>rollback.default_strategy</value>
      <value>rollback.backup_required</value>
    </uses_config_values>
  </dependencies>
</command_file>