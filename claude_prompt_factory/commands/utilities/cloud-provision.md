---
description: Advanced cloud provisioning with intelligent resource optimization, multi-cloud management, and automated scaling
argument-hint: "[cloud_provider] [provisioning_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /cloud provision - Advanced Cloud Provisioning

Sophisticated cloud provisioning system with intelligent resource optimization, multi-cloud management, and automated scaling capabilities.

## Usage
```bash
/cloud provision aws                         # AWS cloud provisioning
/cloud provision --multi-cloud              # Multi-cloud provisioning strategy
/cloud provision --cost-optimized           # Cost-optimized resource provisioning
/cloud provision --auto-scale               # Auto-scaling infrastructure setup
```

## Workflow

The `/cloud provision` command follows a systematic process to provision cloud infrastructure.

```xml
<provisioning_workflow>
  <step name="Analyze Requirements">
    <description>Analyze the user's description of the desired infrastructure to understand the core components, services, and constraints.</description>
  </step>
  
  <step name="Generate IaC Templates">
    <description>Generate the appropriate Infrastructure as Code (IaC) templates (e.g., Terraform, CloudFormation) to define the required resources.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Create the IaC template files.</description>
    </tool_usage>
  </step>
  
  <step name="Apply Security Hardening & Estimate Costs">
    <description>Apply security best practices and compliance rules to the generated IaC templates. Also, generate a detailed cost analysis and provide optimization recommendations.</description>
  </step>
  
  <step name="Generate Deployment Plan">
    <description>Create a staged deployment plan, including rollback procedures, to ensure a safe and reliable provisioning process.</description>
  </step>
</provisioning_workflow>
```

## Key Features
- **Infrastructure as Code Generation**: Creates templates for Terraform, CloudFormation, and Pulumi.
- **Security Compliance Scanning**: Validates against CIS benchmarks and compliance standards like SOC2.
- **Cost Optimization**: Provides cost estimates and budget alerts.
- **Zero-Downtime Deployment**: Supports strategies for zero-downtime deployments.
- **Disaster Recovery Planning**: Includes recommendations for disaster recovery.
- **Auto-Scaling Configuration**: Sets up auto-scaling for relevant resources.