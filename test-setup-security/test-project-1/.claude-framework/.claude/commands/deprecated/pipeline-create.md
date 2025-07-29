---
name: /pipeline-create
description: "Intelligent pipeline creation with automated definition, modular component integration, and comprehensive validation"
argument-hint: "[pipeline_type] [config_file]"
allowed-tools: Read, Write, Edit, Bash, Grep
deprecated: true
deprecation_date: "2025-07-25"
removal_date: "2025-08-25"
replacement: "/pipeline create"
---
# /pipeline create - Intelligent Pipeline Creation

## ⚠️ DEPRECATION NOTICE

**This command is deprecated as of 2025-07-25 and will be removed on 2025-08-25.**

**Use instead:** `/pipeline create`

This standalone command has been consolidated into the unified `/pipeline` command. The new command provides the same functionality with improved consistency and maintainability.

**Migration Guide:**
- `/pipeline-create ci/cd --config "file"` → `/pipeline create ci/cd --config "file"`
- `/pipeline-create data-flow --template "spark"` → `/pipeline create data-flow --template "spark"`
- All functionality has been preserved in the unified command

---

Advanced pipeline creation system with automated definition, modular component integration, and comprehensive validation of workflow orchestration.
## Usage
```bash
/pipeline create ci/cd --config "jenkinsfile" # Create a CI/CD pipeline from a Jenkinsfile
/pipeline create --data-flow "spark_job"     # Create a data flow pipeline for a Spark job
/pipeline create --custom-template "template.yaml" # Create a pipeline from a custom template
```
<command_file>
  <metadata>
    <n>/pipeline create</n>
    <purpose>Intelligent pipeline creation with automated definition, modular component integration, and comprehensive validation</purpose>
    <usage>
      <![CDATA[
      /pipeline create [pipeline_type] --config "[config_file]"
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="pipeline_type" type="string" required="true" default="ci/cd">
      <description>The type of pipeline to create (e.g., ci/cd, data_flow, deployment)</description>
    </argument>
    <argument name="config_file" type="string" required="false">
      <description>The path to the pipeline configuration file</description>
    </argument>
    <argument name="template" type="string" required="false">
      <description>A template to use for pipeline creation</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Create a CI/CD pipeline from a Jenkinsfile</description>
      <usage>/pipeline create ci/cd --config "Jenkinsfile"</usage>
    </example>
    <example>
      <description>Create a data flow pipeline for a Spark job</description>
      <usage>/pipeline create --data-flow "spark_job_definition.py"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are an advanced pipeline creation specialist. The user wants to create an intelligent pipeline with automated definition and modular component integration.
**Pipeline Creation Process:**
1. **Requirement Analysis**: Analyze pipeline requirements, type, and components
2. **Automated Definition**: Automatically define the pipeline structure and stages
3. **Component Integration**: Integrate modular components and tasks into the pipeline
4. **Validation**: Validate the pipeline configuration and dependencies
5. **Deployment &amp; Activation**: Deploy and activate the created pipeline
**Implementation Strategy:**
- Analyze pipeline requirements to determine optimal structure and orchestration
- Automatically generate pipeline definitions using YAML, JSON, or DSLs (e.g., Jenkinsfile, GitLab CI config)
- Integrate modular components into the pipeline, ensuring proper data flow and execution order
- Validate the pipeline configuration for correctness, syntax, and dependency resolution
- Deploy the pipeline to the target CI/CD or workflow orchestration system and activate it for execution
<include component="components/orchestration/dag-orchestrator.md" />
<include component="components/integration/cicd-integration.md" />
<include component="components/planning/create-step-by-step-plan.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/orchestration/dag-orchestrator.md</component>
      <component>components/integration/cicd-integration.md</component>
      <component>components/planning/create-step-by-step-plan.md</component>
    </includes_components>
    <uses_config_values>
      <value>pipeline.default_template</value>
      <value>pipeline.deployment_target</value>
    </uses_config_values>
  </dependencies>
</command_file> 