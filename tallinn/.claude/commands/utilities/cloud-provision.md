---
name: /cloud-provision
description: Intelligent cloud provisioning with automated resource creation, configuration management, and comprehensive cost optimization
usage: /cloud-provision [cloud_provider] [resource_type]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent cloud provisioning with automated resource creation, configuration management, and comprehensive cost optimization

**Usage**: `/cloud-provision $CLOUD_PROVIDER $RESOURCE_TYPE $OPTIMIZE_COST`

## Key Arguments

- **$CLOUD_PROVIDER** (required): The cloud provider to provision resources in (e.g., aws, gcp, azure)
- **$RESOURCE_TYPE** (required): The type of resource to provision (e.g., ec2_instance, s3_bucket, gke_cluster)
- **$OPTIMIZE_COST** (optional): Whether to apply cost optimization strategies during provisioning

## Examples

```bash
/cloud provision aws "ec2_instance --instance-type t3.micro"
```
*Provision an AWS EC2 instance*

```bash
/cloud provision --gcp "gke_cluster --num-nodes 3"
```
*Provision a GCP GKE cluster*

## Core Logic

components/validation/input-validation.md
 components/workflow/command-execution.md
 components/workflow/error-handling.md
 components/interaction/progress-reporting.md
 components/analysis/codebase-discovery.md
 components/analysis/dependency-mapping.md
 components/workflow/report-generation.md

You are an advanced cloud provisioning specialist. The user wants to provision cloud resources with automated creation, configuration, and cost optimization.

**Provisioning Process:**
1. **Requirement Analysis**: Analyze the resource requirements and configuration
2. **Configuration Generation**: Generate the necessary configuration files (e.g., Terraform, CloudFormation)
3. **Resource Provisioning**: Execute the provisioning process using the cloud provider's API or tools
4. **Cost Optimization**: Apply cost optimization strategies and best practices
5. **Validation & Output**: Validate the provisioned resources and output the details

**Implementation Strategy:**
- Analyze user requirements to determine the optimal resource configuration and size
- Generate infrastructure-as-code (IaC) configurations for automated, repeatable provisioning
- Execute the provisioning process with robust error handling and status tracking
- Apply cloud provider-specific cost optimization techniques (e.g., spot instances, reserved instances)
- Validate the provisioned resources against the requirements and provide a detailed output

## Essential Component Logic

### Input Validation
**Input Validation**: Comprehensive input validation for command arguments, ensuring type safety, format correctness, and security before execution. 1. **Type Validation**: - String: Non-empty, length limits, character res...

**Key Criteria**: 1. **Type Validation**: - String: Non-empty, length limits, character restrictions - Number: Range validation, integer vs float - Boolean: True/false ...

*[Additional logic optimized for execution...]*

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

