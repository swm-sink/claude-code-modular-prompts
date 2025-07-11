# Site Reliability Engineering R&D Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Site Reliability Engineering (SRE) R&D domain template provides specialized framework configuration for building highly reliable, scalable, and maintainable systems. This template optimizes the Claude Code Framework for SRE workflows, reliability engineering, and operational excellence with focus on automation and observability.

## Domain Configuration

```xml
<site_reliability_engineering_domain>
  <purpose>Advanced site reliability engineering for scalable, fault-tolerant systems</purpose>
  
  <core_principles>
    <reliability_engineering>Systematic approach to reliability through engineering practices</reliability_engineering>
    <toil_reduction>Automation of repetitive operational tasks</toil_reduction>
    <error_budgets>Quantitative approach to balancing reliability and velocity</error_budgets>
    <monitoring_observability>Comprehensive observability with actionable alerts</monitoring_observability>
    <incident_response>Structured incident response and post-mortem analysis</incident_response>
  </core_principles>
  
  <sre_practices>
    <service_level_objectives>Define and monitor SLOs for service reliability</service_level_objectives>
    <capacity_planning>Proactive capacity planning and resource optimization</capacity_planning>
    <change_management>Safe, gradual rollout of changes with rollback capabilities</change_management>
    <emergency_response>Rapid response to incidents with clear escalation procedures</emergency_response>
    <automation_engineering>Build tools and automation to reduce manual work</automation_engineering>
  </sre_practices>
  
  <rd_characteristics>
    <reliability_science>Data-driven approach to reliability engineering</reliability_science>
    <scalability_engineering>Design systems for horizontal and vertical scaling</scalability_engineering>
    <performance_optimization>Continuous performance monitoring and optimization</performance_optimization>
    <fault_tolerance>Design for failure scenarios and graceful degradation</fault_tolerance>
    <operational_excellence>Continuous improvement of operational processes</operational_excellence>
  </rd_characteristics>
</site_reliability_engineering_domain>
```

## Template Variables

```xml
<template_variables>
  <sre_configuration>
    <reliability_targets>{{RELIABILITY_TARGETS:99.9|99.95|99.99|99.999}}</reliability_targets>
    <monitoring_strategy>{{MONITORING_STRATEGY:sli_slo|golden_signals|use_method|red_method}}</monitoring_strategy>
    <incident_response_model>{{INCIDENT_RESPONSE_MODEL:follow_the_sun|on_call_rotation|escalation_only}}</incident_response_model>
    <automation_level>{{AUTOMATION_LEVEL:basic|advanced|full_automation}}</automation_level>
  </sre_configuration>
  
  <system_architecture>
    <deployment_model>{{DEPLOYMENT_MODEL:blue_green|canary|rolling|feature_flags}}</deployment_model>
    <scalability_approach>{{SCALABILITY_APPROACH:horizontal|vertical|auto_scaling}}</scalability_approach>
    <disaster_recovery>{{DISASTER_RECOVERY:active_passive|active_active|multi_region}}</disaster_recovery>
    <data_consistency>{{DATA_CONSISTENCY:eventual|strong|causal}}</data_consistency>
  </system_architecture>
  
  <observability_setup>
    <metrics_platform>{{METRICS_PLATFORM:prometheus|datadog|newrelic|custom}}</metrics_platform>
    <logging_solution>{{LOGGING_SOLUTION:elk|splunk|fluentd|cloudwatch}}</logging_solution>
    <tracing_system>{{TRACING_SYSTEM:jaeger|zipkin|datadog|aws_xray}}</tracing_system>
    <alerting_channels>{{ALERTING_CHANNELS:pagerduty|slack|email|webhook}}</alerting_channels>
  </observability_setup>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <sre_thinking>
      <reliability_first>Prioritize system reliability and availability</reliability_first>
      <automation_mindset>Automate repetitive tasks and reduce toil</automation_mindset>
      <data_driven_decisions>Use metrics and data to drive reliability decisions</data_driven_decisions>
      <failure_preparation>Design for failure scenarios and graceful degradation</failure_preparation>
      <continuous_improvement>Iterate and improve based on incidents and feedback</continuous_improvement>
    </sre_thinking>
    
    <quality_gates>
      <slo_compliance>Service Level Objectives met consistently</slo_compliance>
      <error_budget_management>Error budget consumption within acceptable limits</error_budget_management>
      <monitoring_coverage>Comprehensive monitoring for all critical services</monitoring_coverage>
      <incident_response_readiness>Incident response procedures tested and documented</incident_response_readiness>
      <automation_validation>Automation tools tested and validated</automation_validation>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <sre_feature_planning>
      <reliability_impact>Assess impact on service reliability and availability</reliability_impact>
      <performance_implications>Evaluate performance impact and optimization opportunities</performance_implications>
      <monitoring_requirements>Define monitoring and alerting requirements</monitoring_requirements>
      <rollout_strategy>Plan safe rollout with canary deployment and rollback</rollout_strategy>
      <capacity_planning>Assess capacity requirements and scaling needs</capacity_planning>
    </sre_feature_planning>
    
    <development_workflow>
      <sli_slo_definition>Define Service Level Indicators and Objectives</sli_slo_definition>
      <observability_integration>Build in monitoring, logging, and tracing</observability_integration>
      <chaos_engineering>Implement chaos engineering practices for resilience</chaos_engineering>
      <automated_testing>Comprehensive testing including failure scenarios</automated_testing>
    </development_workflow>
  </feature_command>
  
  <validate_command>
    <sre_validation>
      <reliability_testing>Test system reliability under various conditions</reliability_testing>
      <performance_benchmarking>Validate performance against established benchmarks</performance_benchmarking>
      <disaster_recovery_testing>Test backup, recovery, and failover procedures</disaster_recovery_testing>
      <capacity_validation>Validate system capacity and scaling capabilities</capacity_validation>
      <monitoring_validation>Ensure monitoring and alerting work correctly</monitoring_validation>
    </sre_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates

```xml
<quality_gates>
  <reliability_standards>
    <availability_target>Meet or exceed defined availability targets (99.9%+)</availability_target>
    <error_budget_compliance>Stay within error budget consumption limits</error_budget_compliance>
    <mttr_target>Mean Time To Recovery (MTTR) < 1 hour for P1 incidents</mttr_target>
    <mttd_target>Mean Time To Detection (MTTD) < 5 minutes for critical issues</mttd_target>
    <change_success_rate>Change success rate > 95%</change_success_rate>
  </reliability_standards>
  
  <observability_requirements>
    <golden_signals>Monitor latency, traffic, errors, and saturation</golden_signals>
    <sli_coverage>All critical services have defined SLIs and SLOs</sli_coverage>
    <alert_quality>Alerts are actionable and have low false positive rate</alert_quality>
    <dashboard_completeness>Comprehensive dashboards for all critical metrics</dashboard_completeness>
    <runbook_availability>Runbooks available for all critical procedures</runbook_availability>
  </observability_requirements>
  
  <operational_excellence>
    <incident_response_time>Initial response to P1 incidents < 5 minutes</incident_response_time>
    <post_mortem_completion>Post-mortems completed within 5 days of incidents</post_mortem_completion>
    <automation_coverage>90% of toil automated or scheduled for automation</automation_coverage>
    <capacity_planning>Capacity planning updated quarterly with growth projections</capacity_planning>
    <disaster_recovery_tested>DR procedures tested quarterly</disaster_recovery_tested>
  </operational_excellence>
</quality_gates>
```

## SRE Practices & Methodologies

```xml
<sre_practices>
  <service_level_management>
    <sli_definition>Define meaningful Service Level Indicators</sli_definition>
    <slo_setting>Set realistic and business-aligned Service Level Objectives</slo_setting>
    <error_budgets>Implement error budget policy for balancing reliability and velocity</error_budgets>
    <sla_management>Manage Service Level Agreements with clear consequences</sla_management>
  </service_level_management>
  
  <incident_management>
    <incident_classification>Clear incident severity levels and escalation procedures</incident_classification>
    <incident_response>Structured incident response with defined roles</incident_response>
    <communication_plan>Clear communication during incidents with stakeholders</communication_plan>
    <post_mortem_process>Blameless post-mortems with actionable improvements</post_mortem_process>
  </incident_management>
  
  <change_management>
    <gradual_rollouts>Canary deployments, feature flags, and gradual rollouts</gradual_rollouts>
    <rollback_procedures>Quick rollback capabilities for failed changes</rollback_procedures>
    <change_approval>Risk-based change approval process</change_approval>
    <change_monitoring>Monitor changes for impact on reliability</change_monitoring>
  </change_management>
  
  <capacity_planning>
    <demand_forecasting>Predict future capacity needs based on growth</demand_forecasting>
    <resource_optimization>Optimize resource utilization and costs</resource_optimization>
    <scalability_testing>Test system scalability limits regularly</scalability_testing>
    <capacity_alerting>Alert on capacity utilization thresholds</capacity_alerting>
  </capacity_planning>
</sre_practices>
```

## Technology Stack

```xml
<technology_stack>
  <monitoring_observability>
    <metrics>Prometheus, Grafana, InfluxDB, Datadog</metrics>
    <logging>Elasticsearch, Fluentd, Kibana, Splunk</logging>
    <tracing>Jaeger, Zipkin, AWS X-Ray, Datadog APM</tracing>
    <alerting>Alertmanager, PagerDuty, OpsGenie, Slack</alerting>
  </monitoring_observability>
  
  <automation_tools>
    <infrastructure_automation>Terraform, Ansible, Puppet, Chef</infrastructure_automation>
    <deployment_automation>Jenkins, GitLab CI, GitHub Actions, Spinnaker</deployment_automation>
    <configuration_management>Kubernetes, Docker, Helm, Kustomize</configuration_management>
    <chaos_engineering>Chaos Monkey, Litmus, Gremlin, Chaos Toolkit</chaos_engineering>
  </automation_tools>
  
  <reliability_tools>
    <load_testing>JMeter, K6, Artillery, Gatling</load_testing>
    <synthetic_monitoring>Pingdom, New Relic, Datadog Synthetics</synthetic_monitoring>
    <error_tracking>Sentry, Rollbar, Bugsnag, Airbrake</error_tracking>
    <performance_profiling>Pyroscope, Continuous Profiler, APM tools</performance_profiling>
  </reliability_tools>
  
  <incident_response>
    <incident_management>PagerDuty, Opsgenie, VictorOps, Slack</incident_management>
    <communication_tools>Slack, Microsoft Teams, Zoom, Status pages</communication_tools>
    <documentation>Confluence, Notion, GitBook, Runbook automation</documentation>
    <post_mortem_tools>Incident.io, Blameless, Post-mortem templates</post_mortem_tools>
  </incident_response>
</technology_stack>
```

## Best Practices

```xml
<best_practices>
  <reliability_engineering>
    <design_for_failure>Assume components will fail and design accordingly</design_for_failure>
    <gradual_rollouts>Use canary deployments and feature flags</gradual_rollouts>
    <circuit_breakers>Implement circuit breakers for service dependencies</circuit_breakers>
    <graceful_degradation>Design services to degrade gracefully under load</graceful_degradation>
    <idempotency>Design operations to be idempotent and repeatable</idempotency>
  </reliability_engineering>
  
  <observability_practices>
    <structured_logging>Use structured logging with consistent formats</structured_logging>
    <meaningful_metrics>Collect metrics that matter for business and operations</meaningful_metrics>
    <distributed_tracing>Implement tracing for complex distributed systems</distributed_tracing>
    <actionable_alerts>Create alerts that are actionable and have low noise</actionable_alerts>
    <dashboard_design>Design dashboards that tell a story and aid troubleshooting</dashboard_design>
  </observability_practices>
  
  <operational_practices>
    <automation_first>Automate repetitive tasks and reduce manual work</automation_first>
    <documentation_culture>Maintain up-to-date documentation and runbooks</documentation_culture>
    <blameless_culture>Foster blameless post-mortems and continuous learning</blameless_culture>
    <regular_reviews>Conduct regular reviews of SLOs, incidents, and processes</regular_reviews>
    <knowledge_sharing>Share knowledge through documentation and training</knowledge_sharing>
  </operational_practices>
</best_practices>
```

## Research & Innovation Focus

```xml
<research_innovation>
  <emerging_technologies>
    <ai_ops>AI-powered operations, predictive analytics, automated remediation</ai_ops>
    <edge_computing>Edge reliability, distributed systems, latency optimization</edge_computing>
    <quantum_computing>Quantum-resistant systems, quantum networking</quantum_computing>
    <serverless_reliability>Serverless monitoring, cold start optimization</serverless_reliability>
  </emerging_technologies>
  
  <reliability_research>
    <predictive_failure>Machine learning for failure prediction and prevention</predictive_failure>
    <automated_remediation>Self-healing systems and automated incident response</automated_remediation>
    <chaos_engineering>Advanced chaos engineering and resilience testing</chaos_engineering>
    <observability_innovation>Next-generation observability and monitoring</observability_innovation>
  </reliability_research>
  
  <performance_optimization>
    <latency_optimization>Ultra-low latency systems and optimization techniques</latency_optimization>
    <resource_efficiency>Resource optimization and sustainable computing</resource_efficiency>
    <cost_optimization>FinOps practices and cost-aware reliability</cost_optimization>
    <global_scale>Global-scale reliability and distributed systems</global_scale>
  </performance_optimization>
</research_innovation>
```

## Usage Instructions

```xml
<usage_instructions>
  <initialization>
    <setup_command>Use `/init` command with site-reliability-engineering template</setup_command>
    <sli_slo_definition>Define Service Level Indicators and Objectives</sli_slo_definition>
    <monitoring_setup>Configure comprehensive monitoring and alerting</monitoring_setup>
    <incident_response_setup>Establish incident response procedures</incident_response_setup>
  </initialization>
  
  <operational_workflow>
    <monitoring_phase>Continuous monitoring of service health and performance</monitoring_phase>
    <incident_response_phase>Rapid response to incidents with clear procedures</incident_response_phase>
    <post_incident_phase>Post-mortem analysis and improvement implementation</post_incident_phase>
    <continuous_improvement>Regular review and optimization of SRE practices</continuous_improvement>
  </operational_workflow>
  
  <reliability_engineering>
    <chaos_engineering>Regular chaos engineering exercises</chaos_engineering>
    <capacity_planning>Quarterly capacity planning and optimization</capacity_planning>
    <disaster_recovery>Regular DR testing and procedure updates</disaster_recovery>
    <automation_development>Continuous development of automation tools</automation_development>
  </reliability_engineering>
</usage_instructions>
```

**Usage**: Apply this template for site reliability engineering projects focused on building and maintaining highly reliable, scalable systems. Optimized for SRE teams working on production systems, reliability engineering, and operational excellence with emphasis on automation and data-driven decision making.