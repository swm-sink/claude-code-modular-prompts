---
name: /flow-schedule
description: Intelligent workflow scheduling with automated trigger management, dynamic resource allocation, and comprehensive dependency resolution
usage: /flow-schedule [schedule_type] [workflow_name]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent workflow scheduling with automated trigger management, dynamic resource allocation, and comprehensive dependency resolution

**Usage**: `/flow-schedule $SCHEDULE_TYPE $WORKFLOW_NAME $CRON_EXPRESSION`

## Key Arguments

- **$SCHEDULE_TYPE** (required): The type of schedule (e.g., daily, hourly, cron, event)
- **$WORKFLOW_NAME** (required): The name of the workflow to schedule
- **$CRON_EXPRESSION** (optional): Cron expression if schedule_type is 'cron'

## Examples

```bash
/flow schedule daily "Data Ingestion Workflow"
```
*Schedule a workflow to run daily*

```bash
/flow schedule --cron "0 0 * * *" "Nightly Report Generation"
```
*Schedule a workflow using a cron expression*

## Core Logic

You are an advanced workflow scheduling specialist. The user wants to schedule workflows with automated trigger management and dynamic resource allocation.

**Scheduling Process:**
1. **Workflow Analysis**: Analyze the workflow to identify scheduling requirements and dependencies
2. **Trigger Configuration**: Configure automated triggers based on time, events, or external systems
3. **Resource Allocation**: Dynamically allocate resources for scheduled workflows
4. **Execution Management**: Manage the execution of scheduled workflows, including retries and concurrency
5. **Monitoring & Reporting**: Monitor scheduled workflows and provide comprehensive reports

**Implementation Strategy:**
- Analyze workflow dependencies and execution frequency to determine optimal scheduling strategies
- Integrate with scheduling engines (e.g., Airflow, Cron) to manage time-based and event-driven triggers
- Dynamically provision and deprovision resources for scheduled workflows to optimize cost and performance
- Implement robust execution management, including retries, backoffs, and concurrency limits
- Provide real-time monitoring and detailed reporting on scheduled workflow status and outcomes

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

