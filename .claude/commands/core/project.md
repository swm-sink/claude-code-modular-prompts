---
name: project
description: Comprehensive project management suite with setup, provisioning, workflow orchestration, scheduling, tracking, and deployment operations
category: core
parameters: 
  - name: MODE
    type: string
    required: true
    description: Operation mode (setup, provision, workflow, schedule, track, rollback, run)
  - name: TARGET
    type: string
    required: false
    description: Target for the operation (environment, workflow name, etc.)
  - name: OPTIONS
    type: string
    required: false
    description: Additional options and flags for the operation
usage_examples:
  - "/project setup development - Setup development environment"
  - "/project provision cloud - Cloud infrastructure provisioning"
  - "/project workflow start 'Feature Development' - Start development workflow"
  - "/project track --dashboard - Real-time progress dashboard"
prerequisites: 
  - "Project configuration files present"
  - "Required cloud/infrastructure credentials configured"
  - "Development environment dependencies available"
output_format: structured
tags: [project-management, infrastructure, deployment, workflow, orchestration, v2-enhanced]
version: "1.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
---

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>command</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>yaml_frontmatter</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/.claude/commands/core/project.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<command_metadata>
  <command_id>project</command_id>
  <command_count>88</command_count>
  <progressive_disclosure_layer>N/A</progressive_disclosure_layer>
  
  <component_dependencies>
    <required_components>
      <component ref="parameter-parser" role="mode_and_target_processing"/>
      <component ref="workflow-coordinator" role="project_orchestration"/>
      <component ref="state-manager" role="project_state_tracking"/>
      <component ref="progress-tracking" role="operation_monitoring"/>
    </required_components>
    <optional_components>
      <component ref="git-operations" benefit="version_control_integration"/>
      <component ref="api-caller" benefit="cloud_infrastructure_management"/>
      <component ref="task-execution" benefit="automated_deployment"/>
      <component ref="progress-reporting" benefit="dashboard_generation"/>
    </optional_components>
  </component_dependencies>
  
  <orchestration_capability>
    <can_invoke_commands>true</can_invoke_commands>
    <invokable_commands>
      <command ref="deploy" context="deployment_operations"/>
      <command ref="ci-setup" context="infrastructure_provisioning"/>
      <command ref="dev-setup" context="environment_setup"/>
      <command ref="monitor-setup" context="project_monitoring"/>
      <command ref="test-integration" context="quality_assurance"/>
    </invokable_commands>
    <orchestration_patterns>sequential|parallel|conditional|workflow_driven</orchestration_patterns>
  </orchestration_capability>
  
  <v2_features>
    <task_description>Comprehensive project lifecycle management with setup, provisioning, workflow orchestration, and deployment automation</task_description>
    <implementation_strategy>mode_analysis|target_identification|operation_planning|resource_provisioning|execution_monitoring|status_reporting</implementation_strategy>
    <command_chaining_enabled>true</command_chaining_enabled>
  </v2_features>
</command_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>project_management_suite</primary_discovery_path>
    <alternative_paths>
      <path>infrastructure_management</path>
      <path>deployment_orchestration</path>
      <path>development_workflow_management</path>
    </alternative_paths>
  </discovery_metadata>
  
  <relationship_map>
    <upstream_dependencies>
      <file type="context" ref=".claude/context/project-management-patterns.md" relation="management_guidance"/>
      <file type="component" ref=".claude/components/orchestration/workflow-coordinator.md" relation="core_orchestration"/>
    </upstream_dependencies>
    <downstream_consumers>
      <file type="command" ref="deploy" relation="deployment_integration"/>
      <file type="command" ref="ci-setup" relation="infrastructure_setup"/>
      <file type="command" ref="monitor-setup" relation="monitoring_integration"/>
    </downstream_consumers>
    <peer_alternatives>
      <file type="command" ref="project-task" similarity="0.80"/>
      <file type="command" ref="global-deploy" similarity="0.65"/>
      <file type="command" ref="pipeline" similarity="0.70"/>
    </peer_alternatives>
  </relationship_map>
  
  <usage_context>
    <when_to_use>
      <scenario>comprehensive_project_lifecycle_management</scenario>
      <scenario>infrastructure_provisioning_and_setup</scenario>
      <scenario>workflow_orchestration_and_tracking</scenario>
      <scenario>deployment_and_monitoring_automation</scenario>
    </when_to_use>
    <when_not_to_use>
      <scenario>simple_single_task_operations</scenario>
      <scenario>exploratory_development_work</scenario>
      <scenario>quick_prototyping_activities</scenario>
    </when_not_to_use>
  </usage_context>
  
  <ai_search_optimization>
    <keywords>project management setup provisioning workflow deployment orchestration infrastructure</keywords>
    <semantic_tags>project_lifecycle infrastructure_management deployment_automation comprehensive_management</semantic_tags>
    <functionality_vectors>[0.8, 0.9, 0.8, 0.9, 0.9]</functionality_vectors>
  </ai_search_optimization>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>persistent</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <knowledge_dependencies>
    <required_context>
      <context_file ref=".claude/context/project-management-patterns.md" importance="high"/>
      <context_file ref=".claude/context/deployment-strategies.md" importance="high"/>
    </required_context>
    <helpful_context>
      <context_file ref=".claude/context/infrastructure-patterns.md" importance="medium"/>
      <context_file ref=".claude/context/workflow-optimization.md" importance="medium"/>
    </helpful_context>
  </knowledge_dependencies>
  
  <workflow_integration>
    <workflow_stage>project_management</workflow_stage>
    <integration_patterns>
      <pattern>lifecycle_orchestration</pattern>
      <pattern>infrastructure_provisioning</pattern>
      <pattern>deployment_automation</pattern>
      <pattern>progress_monitoring</pattern>
    </integration_patterns>
  </workflow_integration>
  
  <ai_learning_markers>
    <concept_introduction>comprehensive_project_management</concept_introduction>
    <skill_progression>advanced</skill_progression>
    <mastery_indicators>
      <indicator>successful_project_lifecycle_management</indicator>
      <indicator>effective_infrastructure_provisioning</indicator>
      <indicator>streamlined_deployment_processes</indicator>
    </mastery_indicators>
  </ai_learning_markers>
</context_engineering>
<!-- AI_METADATA_END -->

# /project - Comprehensive Project Management Suite v1.0

<context type="project">
Unified project management system for lusaka template library supporting 7 operational modes: setup, provision, workflow, schedule, track, rollback, and run. Handles complete project lifecycle from development environment setup through production deployment and monitoring.
</context>

<instructions>
Execute comprehensive project management operations using $MODE parameter to determine operation type. Process $TARGET for environment/workflow specification and $OPTIONS for additional configuration. Support cross-mode integration and state management.
</instructions>

## Usage Examples

<examples>
<example>
<input>/project setup development</input>
<expected_output>Complete development environment setup with dependencies, tools, and configuration</expected_output>
</example>
<example>
<input>/project provision cloud --scale enterprise</input>
<expected_output>Enterprise-scale cloud infrastructure provisioning with monitoring and security</expected_output>
</example>
<example>
<input>/project workflow start "Feature Development"</input>
<expected_output>Initiated feature development workflow with task orchestration and progress tracking</expected_output>
</example>
<example>
<input>/project track --dashboard</input>
<expected_output>Real-time project dashboard with metrics, progress, and performance analytics</expected_output>
</example>
</examples>

## Project Management Workflow

<workflow type="conditional">
<task priority="high">
**Mode Detection & Validation**: Parse and validate operation mode
- Identify operation mode: setup, provision, workflow, schedule, track, rollback, run
- Validate target environment and options
- Load project context and configuration
- Check prerequisites and permissions
</task>

<task priority="high">
**Setup Mode**: Environment and development setup ($MODE = setup)
- Environment analysis and dependency resolution
- Toolchain installation and configuration
- IDE setup and development workflow configuration
- Environment file generation and validation
</task>

<task priority="high">
**Provision Mode**: Infrastructure provisioning ($MODE = provision)
- Infrastructure assessment and planning
- Cloud resource provisioning with IaC
- Security hardening and compliance setup
- Monitoring and alerting configuration
</task>

<task priority="high">
**Workflow Mode**: Workflow orchestration ($MODE = workflow)
- DAG construction and task orchestration
- Parallel execution and resource management
- State management and progress monitoring
- Error handling and recovery mechanisms
</task>

<task priority="medium">
**Schedule Mode**: Workflow scheduling ($MODE = schedule)
- Time-based and event-driven scheduling
- Resource optimization and conflict management
- Monitoring and performance analytics
- Integration with external scheduling systems
</task>

<task priority="medium">
**Track Mode**: Progress tracking and analytics ($MODE = track)
- Real-time monitoring and dashboard generation
- Performance analytics and predictive insights
- Resource utilization tracking
- Executive reporting and KPI generation
</task>

<task priority="medium">
**Rollback Mode**: Deployment rollback operations ($MODE = rollback)
- Version analysis and impact assessment
- Automated rollback execution with data integrity
- Service continuity and validation testing
- Incident documentation and reporting
</task>

<task priority="medium">
**Run Mode**: CI/CD operations ($MODE = run)
- Pipeline orchestration and quality gates
- Automated testing and deployment execution
- Real-time monitoring and results analysis
- Failure handling and recovery procedures
</task>
</workflow>

## 🚀 Operation Modes Overview

### **Core Modes:**
- **`setup`** - Environment and development setup automation
- **`provision`** - Infrastructure provisioning and management  
- **`workflow`** - Workflow orchestration and task management
- **`schedule`** - Workflow scheduling and automation

### **Monitoring & Operations:**
- **`track`** - Progress monitoring and analytics
- **`rollback`** - Deployment rollback operations
- **`run`** - CI/CD operations and execution

### **Integration Features:**
- **Cross-Mode Integration**: Workflows spanning multiple operational aspects
- **State Management**: Persistent state across mode executions
- **Unified Configuration**: Shared configuration and context management
- **Comprehensive Monitoring**: Unified monitoring across all operational modes

<automation trigger="completion">
- Execute mode-specific cleanup and resource management
- Generate comprehensive operation reports and metrics
- Update project state and configuration as needed
- Provide next-step recommendations and workflow suggestions
</automation>