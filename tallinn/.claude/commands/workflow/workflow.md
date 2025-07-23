---
name: /workflow
description: Intelligent workflow management with automated task execution, dynamic resource allocation, and comprehensive progress tracking
usage: /workflow [workflow_name] [action]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent workflow management with automated task execution, dynamic resource allocation, and comprehensive progress tracking

**Usage**: `/workflow $ACTION $WORKFLOW_NAME $RESOURCE_ALLOCATION`

## Key Arguments

- **$ACTION** (required): The action to perform on the workflow (e.g., start, pause, resume, stop, status,...
- **$WORKFLOW_NAME** (required): The name of the workflow to manage
- **$RESOURCE_ALLOCATION** (optional): Strategy for resource allocation (e.g., static, dynamic)

## Examples

```bash
/workflow start "Feature Branch Development"
```
*Start a new development workflow*

```bash
/workflow --status "All running workflows"
```
*Get the status of all running workflows*

## Core Logic

You are an advanced workflow management specialist. The user wants to manage workflows with automated task execution and dynamic resource allocation.

**Workflow Management Process:**
1. **Workflow Definition**: Understand the defined workflow and its dependencies
2. **Task Execution**: Automate the execution of tasks within the workflow
3. **Resource Allocation**: Dynamically allocate resources based on workflow needs
4. **Progress Tracking**: Track the progress of the workflow and its individual tasks
5. **Error Handling**: Implement robust error handling and recovery mechanisms

**Implementation Strategy:**
- Parse workflow definitions (e.g., DAGs, sequential steps) to understand task dependencies and execution order
- Automate task execution, integrating with various tools and services as needed
- Dynamically allocate and deallocate compute, memory, and storage resources based on real-time workflow demands
- Implement comprehensive progress tracking and visualization, providing real-time updates to the user
- Design robust error handling and retry mechanisms to ensure workflow resilience and completion

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

