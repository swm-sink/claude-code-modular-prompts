---
command: project
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
version: "2.0"
author: "lusaka-template-library"
last_updated: "2025-07-31"
allowed-tools:
- Read
- Write
- Edit
- Bash
- Grep
---
# /project - Comprehensive Project Management Suite v2.0

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