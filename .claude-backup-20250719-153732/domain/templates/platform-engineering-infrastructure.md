# Platform Engineering & Infrastructure R&D Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Platform Engineering & Infrastructure R&D domain template provides specialized framework configuration for building Internal Developer Platforms (IDPs), infrastructure automation, and developer experience optimization. This template optimizes the Claude Code Framework for platform engineering workflows, infrastructure as code, and developer productivity enhancement.

## Domain Configuration

```xml
<platform_engineering_infrastructure_domain>
  <purpose>Advanced platform engineering and infrastructure automation for developer productivity</purpose>
  
  <core_capabilities>
    <internal_developer_platform>Self-service platform for developers with standardized workflows</internal_developer_platform>
    <infrastructure_automation>Infrastructure as Code, automated provisioning, and configuration management</infrastructure_automation>
    <developer_experience>Streamlined development workflows, reduced cognitive load</developer_experience>
    <scalability_engineering>Horizontal scaling, load balancing, performance optimization</scalability_engineering>
    <observability_platform>Monitoring, logging, alerting, and distributed tracing</observability_platform>
  </core_capabilities>
  
  <target_environments>
    <cloud_native>Kubernetes, Docker, serverless, microservices</cloud_native>
    <multi_cloud>AWS, Azure, GCP, hybrid cloud strategies</multi_cloud>
    <edge_computing>Edge deployments, CDN, distributed systems</edge_computing>
    <on_premises>Traditional infrastructure, hybrid models</on_premises>
  </target_environments>
  
  <rd_characteristics>
    <automation_first>Everything as code, GitOps workflows, self-healing systems</automation_first>
    <developer_productivity>Reduced deployment time, simplified workflows, self-service capabilities</developer_productivity>
    <reliability_engineering>High availability, disaster recovery, fault tolerance</reliability_engineering>
    <performance_optimization>Latency optimization, resource efficiency, cost management</performance_optimization>
  </rd_characteristics>
</platform_engineering_infrastructure_domain>
```

## Template Variables

```xml
<template_variables>
  <platform_configuration>
    <cloud_providers>{{CLOUD_PROVIDERS:aws|azure|gcp|multi_cloud}}</cloud_providers>
    <orchestration_platform>{{ORCHESTRATION_PLATFORM:kubernetes|docker_swarm|nomad|ecs}}</orchestration_platform>
    <infrastructure_approach>{{INFRASTRUCTURE_APPROACH:terraform|pulumi|cloudformation|cdk}}</infrastructure_approach>
    <gitops_enabled>{{GITOPS_ENABLED:boolean}}</gitops_enabled>
  </platform_configuration>
  
  <developer_platform>
    <idp_framework>{{IDP_FRAMEWORK:backstage|port|humanitec|custom}}</idp_framework>
    <ci_cd_platform>{{CI_CD_PLATFORM:github_actions|gitlab_ci|jenkins|tekton}}</ci_cd_platform>
    <service_mesh>{{SERVICE_MESH:istio|linkerd|consul_connect|none}}</service_mesh>
    <secrets_management>{{SECRETS_MANAGEMENT:vault|aws_secrets|azure_keyvault|kubernetes_secrets}}</secrets_management>
  </developer_platform>
  
  <observability_stack>
    <monitoring_solution>{{MONITORING_SOLUTION:prometheus|datadog|newrelic|custom}}</monitoring_solution>
    <logging_platform>{{LOGGING_PLATFORM:elk|fluentd|loki|cloudwatch}}</logging_platform>
    <tracing_system>{{TRACING_SYSTEM:jaeger|zipkin|datadog|aws_xray}}</tracing_system>
    <alerting_system>{{ALERTING_SYSTEM:alertmanager|pagerduty|opsgenie|custom}}</alerting_system>
  </observability_stack>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <platform_engineering_thinking>
      <developer_experience>Optimize for developer productivity and reduced cognitive load</developer_experience>
      <automation_first>Automate repetitive tasks and manual processes</automation_first>
      <scalability_design>Design for horizontal scaling and high availability</scalability_design>
      <security_by_design>Build security into the platform from ground up</security_by_design>
      <cost_optimization>Optimize for resource efficiency and cost management</cost_optimization>
    </platform_engineering_thinking>
    
    <quality_gates>
      <infrastructure_validation>Validate infrastructure changes through automated testing</infrastructure_validation>
      <performance_benchmarks>Meet latency, throughput, and resource utilization targets</performance_benchmarks>
      <security_compliance>Security scanning, compliance validation, vulnerability assessment</security_compliance>
      <disaster_recovery>Backup and recovery procedures, failover testing</disaster_recovery>
      <developer_feedback>Collect and incorporate developer experience feedback</developer_feedback>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <platform_feature_planning>
      <self_service_capability>Enable developers to self-serve common operations</self_service_capability>
      <standardization>Establish consistent patterns and best practices</standardization>
      <observability_integration>Built-in monitoring, logging, and alerting</observability_integration>
      <scalability_consideration>Design for current and future scale requirements</scalability_consideration>
      <developer_adoption>Ensure features are discoverable and easy to use</developer_adoption>
    </platform_feature_planning>
    
    <development_workflow>
      <infrastructure_as_code>Everything versioned, reviewable, and automated</infrastructure_as_code>
      <gitops_workflow>Git-based deployment and configuration management</gitops_workflow>
      <progressive_deployment>Canary deployments, feature flags, rollback capabilities</progressive_deployment>
      <testing_automation>Automated testing for infrastructure and platform changes</testing_automation>
    </development_workflow>
  </feature_command>
  
  <validate_command>
    <platform_validation>
      <infrastructure_testing>Validate infrastructure changes through automated tests</infrastructure_testing>
      <performance_validation>Load testing, stress testing, capacity planning</performance_validation>
      <security_assessment>Security scanning, penetration testing, compliance validation</security_assessment>
      <developer_experience_testing>Validate developer workflows and self-service capabilities</developer_experience_testing>
      <disaster_recovery_testing>Backup, recovery, and failover testing</disaster_recovery_testing>
    </platform_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates

```xml
<quality_gates>
  <infrastructure_standards>
    <infrastructure_as_code>All infrastructure defined and managed as code</infrastructure_as_code>
    <version_control>All configurations in version control with proper branching</version_control>
    <automated_testing>Infrastructure changes validated through automated tests</automated_testing>
    <security_hardening>Security baselines and hardening applied consistently</security_hardening>
    <documentation>Comprehensive documentation for platform capabilities</documentation>
  </infrastructure_standards>
  
  <performance_requirements>
    <deployment_time>Development to production deployment < 30 minutes</deployment_time>
    <availability_target>99.9% uptime for critical platform services</availability_target>
    <recovery_time>Recovery time objective (RTO) < 4 hours</recovery_time>
    <backup_integrity>Recovery point objective (RPO) < 15 minutes</backup_integrity>
    <resource_efficiency>Optimize resource utilization and cost per workload</resource_efficiency>
  </performance_requirements>
  
  <developer_experience_metrics>
    <time_to_productivity>New developer productive within 1 day</time_to_productivity>
    <deployment_frequency>Enable daily deployments for development teams</deployment_frequency>
    <lead_time>Commit to production lead time < 2 hours</lead_time>
    <change_failure_rate>Change failure rate < 5%</change_failure_rate>
    <mean_time_to_recovery>MTTR < 1 hour for platform issues</mean_time_to_recovery>
  </developer_experience_metrics>
</quality_gates>
```

## Platform Architecture

```xml
<platform_architecture>
  <developer_platform_components>
    <developer_portal>Self-service portal for developers with API catalog</developer_portal>
    <service_templates>Standardized service templates and scaffolding</service_templates>
    <deployment_pipelines>Automated CI/CD pipelines with quality gates</deployment_pipelines>
    <environment_management>Automated environment provisioning and management</environment_management>
    <secrets_management>Centralized secrets and configuration management</secrets_management>
  </developer_platform_components>
  
  <infrastructure_layer>
    <compute_orchestration>Kubernetes, container orchestration, serverless</compute_orchestration>
    <networking>Service mesh, load balancing, ingress controllers</networking>
    <storage>Persistent storage, backup solutions, data management</storage>
    <security>Network security, identity management, policy enforcement</security>
  </infrastructure_layer>
  
  <observability_platform>
    <metrics_collection>Prometheus, custom metrics, business metrics</metrics_collection>
    <logging_aggregation>Centralized logging with search and analysis</logging_aggregation>
    <distributed_tracing>Request tracing across microservices</distributed_tracing>
    <alerting_system>Intelligent alerting with escalation policies</alerting_system>
  </observability_platform>
</platform_architecture>
```

## Technology Stack

```xml
<technology_stack>
  <infrastructure_automation>
    <iac_tools>Terraform, Pulumi, CloudFormation, Azure Resource Manager</iac_tools>
    <configuration_management>Ansible, Chef, Puppet, SaltStack</configuration_management>
    <container_orchestration>Kubernetes, Docker Swarm, Amazon ECS</container_orchestration>
    <gitops_tools>ArgoCD, Flux, Jenkins X, GitLab CI/CD</gitops_tools>
  </infrastructure_automation>
  
  <platform_tools>
    <developer_portals>Backstage, Port, Humanitec, OpsLevel</developer_portals>
    <service_mesh>Istio, Linkerd, Consul Connect, AWS App Mesh</service_mesh>
    <api_gateways>Kong, Ambassador, Istio Gateway, AWS API Gateway</api_gateways>
    <secrets_management>HashiCorp Vault, AWS Secrets Manager, Azure Key Vault</secrets_management>
  </platform_tools>
  
  <observability_stack>
    <monitoring>Prometheus, Grafana, Datadog, New Relic</monitoring>
    <logging>Elasticsearch, Fluentd, Kibana, Loki</logging>
    <tracing>Jaeger, Zipkin, AWS X-Ray, Datadog APM</tracing>
    <alerting>Alertmanager, PagerDuty, OpsGenie, Slack</alerting>
  </observability_stack>
  
  <security_tools>
    <vulnerability_scanning>Twistlock, Aqua, Clair, Snyk</vulnerability_scanning>
    <policy_enforcement>Open Policy Agent, Falco, Gatekeeper</policy_enforcement>
    <identity_management>Keycloak, Auth0, AWS IAM, Azure AD</identity_management>
    <compliance_monitoring>Chef InSpec, AWS Config, Azure Policy</compliance_monitoring>
  </security_tools>
</technology_stack>
```

## Best Practices

```xml
<best_practices>
  <platform_design_principles>
    <self_service_first>Enable developers to self-serve common operations</self_service_first>
    <automation_by_default>Automate repetitive tasks and manual processes</automation_by_default>
    <observability_built_in>Built-in monitoring, logging, and alerting</observability_built_in>
    <security_by_design>Security controls integrated into platform</security_by_design>
    <cost_consciousness>Resource optimization and cost visibility</cost_consciousness>
  </platform_design_principles>
  
  <infrastructure_management>
    <immutable_infrastructure>Immutable servers and containers</immutable_infrastructure>
    <version_everything>Version control for all infrastructure code</version_everything>
    <automated_testing>Test infrastructure changes before deployment</automated_testing>
    <gradual_rollouts>Canary deployments and feature flags</gradual_rollouts>
    <disaster_recovery>Regular backup and recovery testing</disaster_recovery>
  </infrastructure_management>
  
  <developer_experience>
    <consistent_interfaces>Standardized APIs and interfaces</consistent_interfaces>
    <comprehensive_documentation>Self-service documentation and guides</comprehensive_documentation>
    <fast_feedback_loops>Quick feedback on platform changes</fast_feedback_loops>
    <error_handling>Clear error messages and troubleshooting guides</error_handling>
    <continuous_improvement>Regular platform capability enhancement</continuous_improvement>
  </developer_experience>
</best_practices>
```

## Research & Innovation Focus

```xml
<research_innovation>
  <emerging_technologies>
    <edge_computing>Edge infrastructure, distributed computing</edge_computing>
    <serverless_platforms>Function-as-a-Service, event-driven architectures</serverless_platforms>
    <ai_ml_platforms>MLOps platforms, model serving infrastructure</ai_ml_platforms>
    <quantum_computing>Quantum computing infrastructure preparation</quantum_computing>
  </emerging_technologies>
  
  <platform_evolution>
    <developer_experience>Next-generation developer tools and workflows</developer_experience>
    <automated_optimization>AI-driven resource optimization and scaling</automated_optimization>
    <predictive_operations>Predictive failure detection and auto-remediation</predictive_operations>
    <policy_as_code>Automated compliance and governance enforcement</policy_as_code>
  </platform_evolution>
  
  <performance_research>
    <resource_optimization>Advanced resource scheduling and allocation</resource_optimization>
    <network_optimization>Software-defined networking, performance tuning</network_optimization>
    <cost_optimization>FinOps practices, cost prediction and optimization</cost_optimization>
    <environmental_impact>Green computing, carbon footprint reduction</environmental_impact>
  </performance_research>
</research_innovation>
```

## Usage Instructions

```xml
<usage_instructions>
  <initialization>
    <setup_command>Use `/init` command with platform-engineering-infrastructure template</setup_command>
    <configuration>Configure cloud providers, orchestration platform, and tooling</configuration>
    <validation>Validate platform setup with comprehensive testing</validation>
  </initialization>
  
  <development_workflow>
    <planning_phase>Define platform capabilities and developer requirements</planning_phase>
    <design_phase>Design platform architecture and developer experience</design_phase>
    <implementation_phase>Implement platform components with automation</implementation_phase>
    <validation_phase>Validate platform through developer feedback and metrics</validation_phase>
  </development_workflow>
  
  <operational_excellence>
    <monitoring_setup>Implement comprehensive monitoring and alerting</monitoring_setup>
    <incident_response>Establish incident response procedures</incident_response>
    <capacity_planning>Regular capacity planning and optimization</capacity_planning>
    <continuous_improvement>Regular platform enhancement based on usage metrics</continuous_improvement>
  </operational_excellence>
</usage_instructions>
```

**Usage**: Apply this template when building Internal Developer Platforms, infrastructure automation, or developer experience optimization projects. Optimized for platform engineering teams focused on developer productivity, infrastructure reliability, and operational excellence.