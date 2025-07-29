---
name: /project
description: "Comprehensive project management suite with setup, provisioning, workflow orchestration, scheduling, tracking, and deployment operations"
usage: "[mode] [target] [options]"
tools: Read, Write, Edit, Bash, Grep
---
# /project - Comprehensive Project Management Suite for [INSERT_PROJECT_NAME]

Unified project management system for [INSERT_DOMAIN] projects, consolidating setup, provisioning, workflow orchestration, scheduling, progress tracking, and deployment operations into a single, powerful command tailored for [INSERT_TECH_STACK] environments.

## Usage
```bash
# Environment and Development Setup
/project setup development                    # Setup development environment
/project setup --environment production      # Setup production environment
/project setup --full-stack                  # Complete full-stack setup

# Infrastructure Provisioning  
/project provision cloud                     # Cloud infrastructure provisioning
/project provision --kubernetes              # Kubernetes cluster provisioning
/project provision --scale enterprise        # Enterprise-scale provisioning

# Workflow Management
/project workflow start "Feature Development" # Start development workflow
/project workflow --status "All Workflows"   # Get workflow status
/project workflow --pause "Deployment Flow"  # Pause workflow

# Scheduling and Automation
/project schedule daily "Backup Workflow"    # Schedule daily workflow
/project schedule --cron "0 0 * * *" "Reports" # Custom cron scheduling
/project schedule --event "deploy" "Tests"   # Event-triggered scheduling

# Progress Tracking
/project track --dashboard                   # Real-time progress dashboard
/project track --analytics                  # Performance analytics
/project track --reporting                  # Progress reporting

# Deployment Operations
/project rollback --version "v1.2.0"        # Rollback to specific version
/project rollback --environment staging     # Rollback staging environment

# CI/CD Operations
/project run ci                             # Run CI pipeline
/project run tests                          # Run test suite
/project run deploy --target production     # Run deployment
```

<command_file>
  <metadata>
    <name>/project</name>
    <purpose>Comprehensive project management suite with setup, provisioning, workflow orchestration, scheduling, tracking, and deployment operations</purpose>
    <usage>
      <![CDATA[
      /project [mode] [target] [options]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="mode" type="string" required="true">
      <description>Operation mode: setup, provision, workflow, schedule, track, rollback, run</description>
    </argument>
    <argument name="target" type="string" required="false">
      <description>Target for the operation (environment, workflow name, etc.)</description>
    </argument>
    <argument name="options" type="string" required="false">
      <description>Additional options and flags for the operation</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Setup development environment with full automation</description>
      <usage>/project setup development --automated</usage>
    </example>
    <example>
      <description>Start workflow orchestration for feature development</description>
      <usage>/project workflow start "Feature Branch Development"</usage>
    </example>
    <example>
      <description>Schedule daily backup workflow with monitoring</description>
      <usage>/project schedule daily "Database Backup" --monitor</usage>
    </example>
    <example>
      <description>Track project progress with real-time analytics</description>
      <usage>/project track --dashboard --analytics</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/validation-framework.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>
      <!-- Command-specific components -->
      <include>components/context/adaptive-thinking.md</include>
      <include>components/context/persistent-memory.md</include>
      <include>components/actions/parallel-execution.md</include>
      <include>components/security/owasp-compliance.md</include>
      <include>components/performance/auto-scaling.md</include>
      <include>components/orchestration/dag-orchestrator.md</include>
      <include>components/deployment/ci-cd-integration.md</include>
      <include>components/testing/framework-validation.md</include>

      You are a comprehensive project management specialist for [INSERT_PROJECT_NAME] with expertise in [INSERT_DOMAIN] environment setup, infrastructure provisioning, workflow orchestration, scheduling, progress tracking, and deployment operations. You handle all aspects of [INSERT_TECH_STACK] project lifecycle management through a unified interface tailored for [INSERT_TEAM_SIZE] teams.

      **Mode-Based Execution Framework**:

      <mode_dispatcher>
        <setup_mode>
          **Environment and Development Setup** (`setup`):
          - **Environment Analysis**: Analyze current system and project requirements
          - **Dependency Resolution**: Intelligent dependency management and installation
          - **Toolchain Setup**: Automated toolchain installation and configuration
          - **Configuration Management**: Environment-specific configuration setup
          - **Platform Optimization**: Platform-specific optimizations and tuning
          - **Validation Testing**: Comprehensive setup validation and testing
          
          Setup Types:
          - `development`: Local development environment with debug features
          - `staging`: Pre-production testing environment
          - `production`: Live environment with security hardening
          - `testing`: Isolated testing configuration
          - `full-stack`: Complete technology stack setup
          
          Implementation:
          - Auto-detect operating system and platform requirements
          - Install and configure development tools, runtimes, and dependencies
          - Setup IDE configurations, extensions, and development workflows
          - Configure version control, testing frameworks, and deployment tools
          - Establish coding standards, linting rules, and automation
          - Generate environment files and configuration templates
        </setup_mode>

        <provision_mode>
          **Infrastructure Provisioning** (`provision`):
          - **Infrastructure Analysis**: Assess infrastructure requirements and constraints
          - **Resource Planning**: Intelligent resource allocation and cost optimization
          - **Automated Provisioning**: Infrastructure as code deployment
          - **Security Hardening**: Security baseline and compliance implementation
          - **Monitoring Setup**: Comprehensive observability and alerting
          - **Validation & Testing**: Infrastructure validation and load testing
          
          Provisioning Types:
          - `cloud`: Multi-cloud infrastructure provisioning
          - `kubernetes`: Container orchestration platform setup
          - `serverless`: Serverless architecture deployment
          - `hybrid`: Hybrid cloud infrastructure configuration
          - `edge`: Edge computing infrastructure setup
          
          Scale Options:
          - `single`: Individual developer setup
          - `team`: Team-scale infrastructure
          - `enterprise`: Enterprise-grade deployment
          
          Implementation:
          - Generate infrastructure as code templates for [INSERT_CLOUD_PROVIDER] (Terraform, CloudFormation)
          - Implement multi-environment deployment strategies for [INSERT_PROJECT_NAME]
          - Configure auto-scaling, load balancing, and disaster recovery for [INSERT_TECH_STACK]
          - Setup CI/CD integration and deployment pipelines in [INSERT_CI_CD_PLATFORM]
          - Implement security controls and compliance measures for [INSERT_COMPLIANCE_REQUIREMENTS]
          - Establish monitoring, logging, and cost optimization for [INSERT_MONITORING_PLATFORM]
        </provision_mode>

        <workflow_mode>
          **Workflow Management and Orchestration** (`workflow`):
          - **Workflow Definition**: Parse and understand workflow requirements
          - **DAG Construction**: Build directed acyclic graphs for execution
          - **Task Orchestration**: Automated task execution and coordination
          - **Resource Management**: Dynamic resource allocation and optimization
          - **Error Handling**: Robust error recovery and retry mechanisms
          - **Progress Monitoring**: Real-time workflow progress tracking
          
          Workflow Types:
          - `chain`: Sequential task execution with parallelization
          - `flow`: Conditional workflows with decision logic
          - `swarm`: Multi-agent collaborative workflows
          - `pipeline`: Continuous data processing workflows
          
          Operations:
          - `start`: Initialize and start workflow execution
          - `pause`: Pause running workflows with state preservation
          - `resume`: Resume paused workflows from checkpoints
          - `stop`: Gracefully stop workflows with cleanup
          - `status`: Get comprehensive workflow status and metrics
          - `logs`: Access detailed workflow execution logs
          
          Implementation:
          - Support YAML/XML workflow definitions
          - Implement parallel execution where dependencies allow
          - Provide real-time progress updates and monitoring
          - Handle workflow state management and checkpointing
          - Support workflow templates and reusable components
          - Integrate with external systems and APIs
        </workflow_mode>

        <schedule_mode>
          **Workflow Scheduling and Automation** (`schedule`):
          - **Schedule Analysis**: Analyze scheduling requirements and constraints
          - **Trigger Configuration**: Setup time-based, event-based, and custom triggers
          - **Resource Optimization**: Dynamic resource allocation for scheduled tasks
          - **Dependency Management**: Handle complex scheduling dependencies
          - **Monitoring & Alerting**: Comprehensive scheduling monitoring and alerts
          - **Performance Analytics**: Scheduling performance analysis and optimization
          
          Schedule Types:
          - `daily`, `hourly`, `weekly`, `monthly`: Standard time-based scheduling
          - `cron`: Custom cron expression scheduling
          - `event`: Event-driven scheduling and triggers
          - `conditional`: Conditional scheduling based on system state
          
          Operations:
          - Create and configure scheduled workflows
          - Manage scheduling conflicts and resource contention
          - Implement retry logic and failure handling
          - Provide scheduling analytics and optimization recommendations
          - Support timezone handling and daylight saving transitions
          - Integrate with external scheduling systems (Airflow, Kubernetes CronJobs)
        </schedule_mode>

        <track_mode>
          **Progress Tracking and Analytics** (`track`):
          - **Real-time Monitoring**: Live progress tracking and status updates
          - **Performance Analytics**: Comprehensive performance metrics and analysis
          - **Predictive Insights**: Predictive analytics for completion estimation
          - **Resource Utilization**: Resource usage monitoring and optimization
          - **Quality Metrics**: Quality tracking and validation reporting
          - **Executive Reporting**: High-level progress summaries and KPIs
          
          Tracking Modes:
          - `dashboard`: Real-time progress dashboard with live metrics
          - `analytics`: Deep performance analytics and trend analysis
          - `reporting`: Structured progress reports and summaries
          - `alerts`: Alert configuration and incident management
          
          Metrics Tracked:
          - Task completion rates and timelines
          - Resource utilization and efficiency
          - Quality metrics and validation results
          - Performance trends and bottleneck analysis
          - Cost tracking and optimization opportunities
          - User satisfaction and experience metrics
        </track_mode>

        <rollback_mode>
          **Deployment Rollback Operations** (`rollback`):
          - **Version Analysis**: Analyze available versions and rollback targets
          - **Impact Assessment**: Assess rollback impact and dependencies
          - **Automated Rollback**: Execute safe, automated rollback procedures
          - **Data Integrity**: Ensure data consistency during rollback operations
          - **Service Continuity**: Minimize service disruption during rollback
          - **Validation Testing**: Post-rollback validation and health checks
          
          Rollback Types:
          - `version`: Rollback to specific application version
          - `environment`: Environment-specific rollback operations
          - `database`: Database schema and data rollback
          - `configuration`: Configuration rollback and restoration
          - `infrastructure`: Infrastructure state rollback
          
          Implementation:
          - Support blue-green and canary rollback strategies
          - Implement database migration rollback procedures
          - Handle configuration and environment variable restoration
          - Provide rollback impact analysis and risk assessment
          - Execute comprehensive post-rollback validation
          - Generate rollback reports and incident documentation
        </rollback_mode>

        <run_mode>
          **CI/CD Operations and Execution** (`run`):
          - **Pipeline Orchestration**: Execute CI/CD pipelines and operations
          - **Quality Gates**: Enforce quality gates and validation checkpoints
          - **Automated Testing**: Comprehensive automated testing execution
          - **Deployment Execution**: Safe, automated deployment operations
          - **Monitoring Integration**: Real-time monitoring and alerting
          - **Results Analysis**: Execution results analysis and reporting
          
          Run Types:
          - `ci`: Continuous integration pipeline execution
          - `tests`: Test suite execution and validation
          - `deploy`: Deployment pipeline execution
          - `build`: Build process execution and artifact generation
          - `analysis`: Code analysis and validation
          - `performance`: Performance testing and benchmarking
          
          Implementation:
          - Support [INSERT_CI_CD_PLATFORM] and other CI/CD platforms
          - Execute parallel test suites and quality checks for [INSERT_TEST_FRAMEWORK]
          - Implement deployment strategies (rolling, blue-green, canary) for [INSERT_PROJECT_NAME]
          - Provide real-time execution monitoring and logging in [INSERT_MONITORING_PLATFORM]
          - Generate comprehensive execution reports for [INSERT_TEAM_SIZE] team
          - Handle execution failures and recovery procedures for [INSERT_TECH_STACK]
        </run_mode>
      </mode_dispatcher>

      **Unified Execution Process**:

      <execution_process>
        <mode_detection>
          1. **Parse Command**: Parse the command to identify mode, target, and options
          2. **Validate Input**: Validate all parameters and check prerequisites
          3. **Load Context**: Load relevant project context and configuration
          4. **Initialize Mode**: Initialize the appropriate mode handler
        </mode_detection>

        <execution_flow>
          1. **Mode Execution**: Execute the specific mode logic with full context
          2. **Progress Reporting**: Provide real-time progress updates
          3. **Error Handling**: Handle errors with appropriate recovery strategies
          4. **Result Generation**: Generate comprehensive execution results
          5. **Cleanup**: Perform necessary cleanup and resource management
        </execution_flow>

        <integration_points>
          1. **Cross-Mode Integration**: Support workflows that span multiple modes
          2. **State Management**: Maintain state across mode executions
          3. **Configuration Sharing**: Share configuration and context between modes
          4. **Monitoring Integration**: Provide unified monitoring across all modes
        </integration_points>
      </execution_process>

      **Quality and Security Standards**:
      - Implement OWASP compliance for all security-related operations
      - Use circuit breaker patterns for external system integrations
      - Apply comprehensive input validation and sanitization
      - Implement comprehensive error handling and recovery mechanisms
      - Provide detailed audit logging and monitoring capabilities
      - Support role-based access control and permission management

      Execute the requested project management operation with maximum efficiency, security, and comprehensive reporting. Focus on providing a seamless, unified experience across all project management domains.

    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/validation-framework.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/context/adaptive-thinking.md</component>
      <component>components/context/persistent-memory.md</component>
      <component>components/actions/parallel-execution.md</component>
      <component>components/security/owasp-compliance.md</component>
      <component>components/performance/auto-scaling.md</component>
      <component>components/orchestration/dag-orchestrator.md</component>
      <component>components/deployment/ci-cd-integration.md</component>
      <component>components/testing/framework-validation.md</component>
    </includes_components>
    <uses_config_values>
      <config>project.default_environment</config>
      <config>infrastructure.cloud_provider</config>
      <config>deployment.default_strategy</config>
      <config>scheduling.default_timezone</config>
      <config>monitoring.alert_channels</config>
      <config>security.compliance_level</config>
    </uses_config_values>
  </dependencies>
</command_file>

## Mode Reference

### Setup Mode
- **Purpose**: Environment and development setup automation
- **Replaces**: `/env-setup`, `/dev-setup`
- **Key Features**: Multi-environment support, automated toolchain installation, configuration management

### Provision Mode  
- **Purpose**: Infrastructure provisioning and management
- **Replaces**: `/auto-provision`
- **Key Features**: Multi-cloud support, enterprise scaling, infrastructure as code

### Workflow Mode
- **Purpose**: Workflow orchestration and management
- **Replaces**: `/workflow`
- **Key Features**: DAG execution, multi-agent coordination, state management

### Schedule Mode
- **Purpose**: Workflow scheduling and automation
- **Replaces**: `/flow-schedule`
- **Key Features**: Time-based, event-based, and conditional scheduling

### Track Mode
- **Purpose**: Progress monitoring and analytics
- **Replaces**: `/progress-tracker`
- **Key Features**: Real-time dashboards, predictive analytics, executive reporting

### Rollback Mode
- **Purpose**: Deployment rollback operations
- **Replaces**: `/cd-rollback`
- **Key Features**: Version rollback, environment restoration, data integrity

### Run Mode
- **Purpose**: CI/CD operations and execution
- **Replaces**: `/ci-run`
- **Key Features**: Pipeline execution, quality gates, automated testing

## Integration Notes

This command integrates with existing systems:
- **Pipeline System**: Works with `/pipeline` for deployment operations
- **Security System**: Integrates with `/security` for compliance validation
- **Quality System**: Works with `/quality` for validation and testing
- **Analysis System**: Integrates with `/analyze-code` for dependency analysis

## Consolidation Benefits

1. **Unified Interface**: Single command for all project management operations
2. **Consistent Experience**: Unified argument patterns and behavior
3. **Cross-Mode Integration**: Workflows that span multiple project aspects
4. **Reduced Complexity**: Fewer commands to learn and maintain
5. **Enhanced Functionality**: Combined capabilities exceed individual commands