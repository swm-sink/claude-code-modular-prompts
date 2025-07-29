---
description: Intelligent cloud provisioning with automated resource creation, configuration management, and comprehensive cost optimization
argument-hint: "[cloud_provider] [resource_type]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /cloud provision - Intelligent Cloud Provisioning

Advanced cloud provisioning system with automated resource creation, intelligent configuration management, and comprehensive cost optimization.

## Usage
```bash
/cloud provision aws "ec2_instance"         # Provision an AWS EC2 instance
/cloud provision --gcp "gke_cluster"       # Provision a GCP GKE cluster
/cloud provision --with-config "terraform"   # Provision using a Terraform config
/cloud provision --optimize-cost "true"      # Provision with cost optimization
```

<command_file>
  <metadata>
    <n>/cloud provision</n>
    <purpose>Intelligent cloud provisioning with automated resource creation, configuration management, and comprehensive cost optimization</purpose>
    <usage>
      <![CDATA[
      /cloud provision [cloud_provider] "[resource_type]"
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="cloud_provider" type="string" required="true" default="aws">
      <description>The cloud provider to provision resources in (e.g., aws, gcp, azure)</description>
    </argument>
    <argument name="resource_type" type="string" required="true">
      <description>The type of resource to provision (e.g., ec2_instance, s3_bucket, gke_cluster)</description>
    </argument>
    <argument name="optimize_cost" type="boolean" required="false" default="true">
      <description>Whether to apply cost optimization strategies during provisioning</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Provision an AWS EC2 instance</description>
      <usage>/cloud provision aws "ec2_instance --instance-type t3.micro"</usage>
    </example>
    <example>
      <description>Provision a GCP GKE cluster</description>
      <usage>/cloud provision --gcp "gke_cluster --num-nodes 3"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      <include>components/analysis/codebase-discovery.md</include>
      <include>components/analysis/dependency-mapping.md</include>
      <include>components/workflow/report-generation.md</include>

You are an advanced cloud provisioning specialist. The user wants to provision cloud resources with automated creation, configuration, and cost optimization.

**Provisioning Process:**
1. **Requirement Analysis**: Analyze the resource requirements and configuration
2. **Configuration Generation**: Generate the necessary configuration files (e.g., Terraform, CloudFormation)
3. **Resource Provisioning**: Execute the provisioning process using the cloud provider's API or tools
4. **Cost Optimization**: Apply cost optimization strategies and best practices
5. **Validation &amp; Output**: Validate the provisioned resources and output the details

**Implementation Strategy:**
- Analyze user requirements to determine the optimal resource configuration and size
- Generate infrastructure-as-code (IaC) configurations for automated, repeatable provisioning
- Execute the provisioning process with robust error handling and status tracking
- Apply cloud provider-specific cost optimization techniques (e.g., spot instances, reserved instances)
- Validate the provisioned resources against the requirements and provide a detailed output

<include component="components/deployment/auto-provision.md" />
<include component="components/performance/cost-optimization.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <!-- Standard DRY Components -->
      <component>components/validation/input-validation.md</component>
      <component>components/workflow/command-execution.md</component>
      <component>components/workflow/error-handling.md</component>
      <component>components/interaction/progress-reporting.md</component>
      <component>components/analysis/codebase-discovery.md</component>
      <component>components/analysis/dependency-mapping.md</component>
      <component>components/workflow/report-generation.md</component>
      <!-- Command-specific components -->
      <component>components/deployment/auto-provision.md</component>
      <component>components/performance/cost-optimization.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>cloud.provider.credentials</value>
      <value>cost_optimization.strategy</value>
    </uses_config_values>
  </dependencies>
</command_file>