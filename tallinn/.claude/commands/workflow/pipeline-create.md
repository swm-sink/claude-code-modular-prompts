---
name: /pipeline-create
description: Intelligent pipeline creation with automated definition, modular component integration, and comprehensive validation
usage: /pipeline-create [pipeline_type] [config_file]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent pipeline creation with automated definition, modular component integration, and comprehensive validation

**Usage**: `/pipeline-create $PIPELINE_TYPE $CONFIG_FILE $TEMPLATE`

## Key Arguments

- **$PIPELINE_TYPE** (required): The type of pipeline to create (e.g., ci/cd, data_flow, deployment)
- **$CONFIG_FILE** (optional): The path to the pipeline configuration file
- **$TEMPLATE** (optional): A template to use for pipeline creation

## Examples

```bash
/pipeline create ci/cd --config "Jenkinsfile"
```
*Create a CI/CD pipeline from a Jenkinsfile*

```bash
/pipeline create --data-flow "spark_job_definition.py"
```
*Create a data flow pipeline for a Spark job*

## Core Logic

You are an advanced pipeline creation specialist. The user wants to create an intelligent pipeline with automated definition and modular component integration.

**Pipeline Creation Process:**
1. **Requirement Analysis**: Analyze pipeline requirements, type, and components
2. **Automated Definition**: Automatically define the pipeline structure and stages
3. **Component Integration**: Integrate modular components and tasks into the pipeline
4. **Validation**: Validate the pipeline configuration and dependencies
5. **Deployment & Activation**: Deploy and activate the created pipeline

**Implementation Strategy:**
- Analyze pipeline requirements to determine optimal structure and orchestration
- Automatically generate pipeline definitions using YAML, JSON, or DSLs (e.g., Jenkinsfile, GitLab CI config)
- Integrate modular components into the pipeline, ensuring proper data flow and execution order
- Validate the pipeline configuration for correctness, syntax, and dependency resolution
- Deploy the pipeline to the target CI/CD or workflow orchestration system and activate it for execution

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

