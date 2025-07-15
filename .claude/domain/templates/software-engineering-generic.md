# Software Engineering Generic Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-15   | stable |

## Domain Overview

Generic software engineering domain template provides flexible framework configuration for full-stack development, system architecture, and engineering workflows. This template optimizes the Claude Code Framework for comprehensive software development across multiple domains.

## Domain Configuration

```xml
<software_engineering_generic_domain>
  <purpose>Comprehensive software engineering for full-stack development and system architecture</purpose>
  
  <core_capabilities>
    <frontend_development>UI/UX development, component architecture, responsive design</frontend_development>
    <backend_development>API development, microservices, database design, system integration</backend_development>
    <infrastructure>Cloud platforms, containerization, CI/CD, monitoring, scaling</infrastructure>
    <quality_assurance>Testing frameworks, automated testing, performance optimization</quality_assurance>
    <security>Security by design, authentication, authorization, threat modeling</security>
  </core_capabilities>
  
  <technology_flexibility>
    <frontend>React, Vue, Angular, Svelte, or framework-agnostic approaches</frontend>
    <backend>Python, Java, Node.js, Go, Rust, or polyglot architectures</backend>
    <databases>PostgreSQL, MongoDB, Redis, or technology-appropriate choices</databases>
    <infrastructure>AWS, Azure, GCP, Kubernetes, Docker, or platform-agnostic</infrastructure>
  </technology_flexibility>
  
  <engineering_characteristics>
    <scalability_focus>Design for scale, performance optimization, distributed systems</scalability_focus>
    <quality_engineering>TDD, code quality, automated testing, continuous integration</quality_engineering>
    <user_centric_design>UX/UI best practices, accessibility, performance</user_centric_design>
    <maintainability>Clean code, documentation, refactoring, technical debt management</maintainability>
  </engineering_characteristics>
</software_engineering_generic_domain>
```

## Template Variables

```xml
<template_variables>
  <project_architecture>
    <application_type>{{APPLICATION_TYPE:web_app|mobile_app|api|desktop|embedded}}</application_type>
    <architecture_pattern>{{ARCHITECTURE_PATTERN:monolithic|microservices|serverless|hybrid}}</architecture_pattern>
    <deployment_target>{{DEPLOYMENT_TARGET:cloud|on_premise|hybrid|edge}}</deployment_target>
    <scaling_requirements>{{SCALING_REQUIREMENTS:single_instance|horizontal|auto_scaling|global}}</scaling_requirements>
  </project_architecture>
  
  <technology_preferences>
    <frontend_stack>{{FRONTEND_STACK:react|vue|angular|svelte|vanilla|none}}</frontend_stack>
    <backend_language>{{BACKEND_LANGUAGE:python|javascript|java|go|rust|csharp}}</backend_language>
    <database_type>{{DATABASE_TYPE:relational|nosql|graph|timeseries|hybrid}}</database_type>
    <cloud_provider>{{CLOUD_PROVIDER:aws|azure|gcp|multi_cloud|on_premise}}</cloud_provider>
  </technology_preferences>
  
  <quality_requirements>
    <performance_target>{{PERFORMANCE_TARGET:standard|high_performance|real_time|batch}}</performance_target>
    <security_level>{{SECURITY_LEVEL:standard|high_security|compliance_required|public_facing}}</security_level>
    <availability_target>{{AVAILABILITY_TARGET:standard|high_availability|mission_critical|best_effort}}</availability_target>
    <compliance_requirements>{{COMPLIANCE_REQUIREMENTS:none|gdpr|hipaa|sox|custom}}</compliance_requirements>
  </quality_requirements>
</template_variables>

## Framework Customization

```xml
<framework_customization>
  <command_priorities>
    <primary_workflow>{{PRIMARY_WORKFLOW:feature_driven|task_driven|research_driven|maintenance}}</primary_workflow>
    <development_style>{{DEVELOPMENT_STYLE:agile|waterfall|kanban|experimental}}</development_style>
    <team_structure>{{TEAM_STRUCTURE:solo|small_team|large_team|distributed}}</team_structure>
  </command_priorities>
  
  <quality_gates>
    <test_coverage_threshold>{{TEST_COVERAGE_THRESHOLD:80|90|95|custom}}</test_coverage_threshold>
    <performance_benchmarks>{{PERFORMANCE_BENCHMARKS:basic|standard|aggressive|custom}}</performance_benchmarks>
    <security_requirements>{{SECURITY_REQUIREMENTS:basic|standard|strict|custom}}</security_requirements>
    <code_quality_enforcement>{{CODE_QUALITY_ENFORCEMENT:recommended|strict|custom}}</code_quality_enforcement>
  </quality_gates>
  
  <optimization_focus>
    <primary_metric>{{PRIMARY_METRIC:development_speed|code_quality|performance|maintainability}}</primary_metric>
    <trade_off_preference>{{TRADE_OFF_PREFERENCE:speed|quality|flexibility|simplicity}}</trade_off_preference>
    <automation_level>{{AUTOMATION_LEVEL:manual|semi_automated|fully_automated|ai_assisted}}</automation_level>
  </optimization_focus>
</framework_customization>

## Usage Patterns

```xml
<usage_patterns>
  <common_workflows>
    <feature_development>/feature → /task → /validate</feature_development>
    <research_implementation>/query → /feature → /task</research_implementation>
    <bug_fixing>/query → /task → /validate</bug_fixing>
    <architecture_design>/query → /feature → /swarm</architecture_design>
  </common_workflows>
  
  <recommended_commands>
    <exploration>/query for research and understanding</exploration>
    <planning>/feature for comprehensive feature development</planning>
    <implementation>/task for focused development work</implementation>
    <coordination>/swarm for multi-component development</coordination>
    <documentation>/docs for all documentation needs</documentation>
  </recommended_commands>
  
  <quality_integration>
    <tdd_enforcement>Mandatory RED→GREEN→REFACTOR cycle</tdd_enforcement>
    <automated_testing>Unit, integration, and end-to-end test coverage</automated_testing>
    <performance_monitoring>Real-time performance tracking and optimization</performance_monitoring>
    <security_validation>Continuous security scanning and threat assessment</security_validation>
  </quality_integration>
</usage_patterns>