# Data & Analytics Engineering R&D Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Data & Analytics Engineering R&D domain template provides specialized framework configuration for building modern data platforms, real-time analytics systems, and scalable data processing pipelines. This template optimizes the Claude Code Framework for data engineering workflows, analytics automation, and data-driven innovation.

## Domain Configuration

```xml
<data_analytics_engineering_domain>
  <purpose>Advanced data and analytics engineering for scalable, real-time data systems</purpose>
  
  <core_capabilities>
    <data_pipeline_engineering>ETL/ELT pipelines, stream processing, batch processing, data orchestration</data_pipeline_engineering>
    <real_time_analytics>Stream processing, event-driven architectures, low-latency analytics</real_time_analytics>
    <data_platform_architecture>Data lakes, data warehouses, lakehouses, data mesh architectures</data_platform_architecture>
    <analytics_automation>Automated reporting, self-service analytics, data product development</analytics_automation>
    <data_quality_engineering>Data validation, monitoring, lineage tracking, quality metrics</data_quality_engineering>
  </core_capabilities>
  
  <data_technologies>
    <storage_systems>Data lakes (S3, ADLS), data warehouses (Snowflake, BigQuery, Redshift), NoSQL (MongoDB, Cassandra)</storage_systems>
    <processing_engines>Apache Spark, Apache Flink, Apache Kafka, Apache Beam, dbt</processing_engines>
    <orchestration_tools>Apache Airflow, Prefect, Dagster, Azure Data Factory, AWS Step Functions</orchestration_tools>
    <analytics_platforms>Looker, Tableau, Power BI, Databricks, Jupyter, Apache Superset</analytics_platforms>
  </data_technologies>
  
  <rd_characteristics>
    <scalability_focus>Petabyte-scale processing, distributed computing, auto-scaling pipelines</scalability_focus>
    <real_time_processing>Stream processing, event-driven architectures, low-latency analytics</real_time_processing>
    <data_quality_excellence>Automated data quality monitoring, lineage tracking, data observability</data_quality_excellence>
    <self_service_analytics>Enable business users with self-service data access and analytics</self_service_analytics>
  </rd_characteristics>
</data_analytics_engineering_domain>
```

## Template Variables

```xml
<template_variables>
  <data_architecture>
    <architecture_pattern>{{ARCHITECTURE_PATTERN:data_lake|data_warehouse|lakehouse|data_mesh}}</architecture_pattern>
    <processing_model>{{PROCESSING_MODEL:batch|streaming|hybrid|real_time}}</processing_model>
    <storage_strategy>{{STORAGE_STRATEGY:cloud_native|hybrid|multi_cloud|on_premises}}</storage_strategy>
    <analytics_approach>{{ANALYTICS_APPROACH:self_service|centralized|federated|embedded}}</analytics_approach>
  </data_architecture>
  
  <technology_stack>
    <data_warehouse>{{DATA_WAREHOUSE:snowflake|bigquery|redshift|synapse}}</data_warehouse>
    <processing_engine>{{PROCESSING_ENGINE:spark|flink|beam|databricks}}</processing_engine>
    <orchestration_tool>{{ORCHESTRATION_TOOL:airflow|prefect|dagster|azure_data_factory}}</orchestration_tool>
    <streaming_platform>{{STREAMING_PLATFORM:kafka|kinesis|event_hubs|pub_sub}}</streaming_platform>
  </technology_stack>
  
  <data_quality>
    <validation_framework>{{VALIDATION_FRAMEWORK:great_expectations|deequ|monte_carlo|custom}}</validation_framework>
    <monitoring_solution>{{MONITORING_SOLUTION:datadog|monte_carlo|bigeye|custom}}</monitoring_solution>
    <lineage_tracking>{{LINEAGE_TRACKING:datahub|apache_atlas|openlineage|custom}}</lineage_tracking>
    <testing_approach>{{TESTING_APPROACH:unit_tests|integration_tests|data_tests|all}}</testing_approach>
  </data_quality>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <data_engineering_thinking>
      <data_quality_first>Prioritize data quality, validation, and monitoring</data_quality_first>
      <scalability_design>Design for petabyte-scale processing and growth</scalability_design>
      <real_time_consideration>Consider real-time processing requirements</real_time_consideration>
      <cost_optimization>Optimize for processing costs and resource utilization</cost_optimization>
      <user_experience>Focus on end-user analytics experience and self-service</user_experience>
    </data_engineering_thinking>
    
    <quality_gates>
      <data_quality_validation>Automated data quality checks and validation</data_quality_validation>
      <performance_benchmarks>Processing performance and latency requirements</performance_benchmarks>
      <schema_validation>Schema evolution and compatibility testing</schema_validation>
      <pipeline_reliability>Pipeline monitoring, alerting, and failure recovery</pipeline_reliability>
      <cost_efficiency>Cost optimization and resource utilization monitoring</cost_efficiency>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <data_feature_planning>
      <data_requirements>Define data sources, schemas, and quality requirements</data_requirements>
      <processing_requirements>Define processing, transformation, and analytics needs</processing_requirements>
      <scalability_planning>Plan for data volume growth and processing scale</scalability_planning>
      <real_time_needs>Assess real-time processing and analytics requirements</real_time_needs>
      <user_interface>Design user-friendly analytics interfaces and dashboards</user_interface>
    </data_feature_planning>
    
    <development_workflow>
      <data_modeling>Design dimensional models and analytics schemas</data_modeling>
      <pipeline_development>Build robust, scalable data pipelines</pipeline_development>
      <testing_automation>Automated testing for data quality and pipeline reliability</testing_automation>
      <observability_integration>Built-in monitoring, logging, and alerting</observability_integration>
    </development_workflow>
  </feature_command>
  
  <validate_command>
    <data_validation>
      <data_quality_testing>Validate data quality, completeness, and accuracy</data_quality_testing>
      <performance_testing>Test processing performance and scalability</performance_testing>
      <schema_compatibility>Validate schema evolution and backward compatibility</schema_compatibility>
      <pipeline_reliability>Test pipeline failure scenarios and recovery</pipeline_reliability>
      <end_to_end_testing>End-to-end validation of data flows and analytics</end_to_end_testing>
    </data_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates

```xml
<quality_gates>
  <data_quality_standards>
    <completeness>Data completeness checks for all critical fields</completeness>
    <accuracy>Data accuracy validation against business rules</accuracy>
    <consistency>Data consistency checks across systems and time</consistency>
    <timeliness>Data freshness and latency requirements</timeliness>
    <validity>Data format and constraint validation</validity>
  </data_quality_standards>
  
  <performance_requirements>
    <processing_latency>Batch processing SLA < 4 hours, streaming < 1 minute</processing_latency>
    <throughput>Handle expected data volume with 50% headroom</throughput>
    <availability>99.9% uptime for critical data pipelines</availability>
    <scalability>Auto-scaling based on data volume and processing needs</scalability>
    <cost_efficiency>Cost per GB processed within budget constraints</cost_efficiency>
  </performance_requirements>
  
  <reliability_standards>
    <pipeline_monitoring>Comprehensive monitoring and alerting for all pipelines</pipeline_monitoring>
    <failure_recovery>Automated retry and failure recovery mechanisms</failure_recovery>
    <data_lineage>Complete data lineage tracking and documentation</data_lineage>
    <backup_strategy>Data backup and disaster recovery procedures</backup_strategy>
    <schema_management>Schema version management and evolution</schema_management>
  </reliability_standards>
</quality_gates>
```

## Data Architecture Patterns

```xml
<data_architecture_patterns>
  <modern_data_stack>
    <ingestion_layer>Fivetran, Stitch, Airbyte, custom connectors</ingestion_layer>
    <storage_layer>Cloud data warehouses, data lakes, object storage</storage_layer>
    <transformation_layer>dbt, Dataform, SQL-based transformations</transformation_layer>
    <analytics_layer>BI tools, self-service analytics, embedded analytics</analytics_layer>
    <orchestration_layer>Airflow, Prefect, cloud-native orchestration</orchestration_layer>
  </modern_data_stack>
  
  <real_time_architecture>
    <event_streaming>Apache Kafka, AWS Kinesis, Azure Event Hubs</event_streaming>
    <stream_processing>Apache Flink, Apache Spark Streaming, Kafka Streams</stream_processing>
    <real_time_storage>Apache Cassandra, Amazon DynamoDB, Redis</real_time_storage>
    <real_time_analytics>Apache Druid, ClickHouse, Amazon Timestream</real_time_analytics>
    <event_driven_patterns>Event sourcing, CQRS, saga patterns</event_driven_patterns>
  </real_time_architecture>
  
  <data_mesh_architecture>
    <domain_ownership>Domain-driven data ownership and governance</domain_ownership>
    <data_products>Self-contained data products with clear interfaces</data_products>
    <self_service_platform>Infrastructure as a platform for data teams</self_service_platform>
    <federated_governance>Federated data governance and standards</federated_governance>
    <interoperability>Standard APIs and data contracts</interoperability>
  </data_mesh_architecture>
</data_architecture_patterns>
```

## Technology Stack

```xml
<technology_stack>
  <data_storage>
    <cloud_warehouses>Snowflake, Google BigQuery, Amazon Redshift, Azure Synapse</cloud_warehouses>
    <data_lakes>Amazon S3, Azure Data Lake Storage, Google Cloud Storage</data_lakes>
    <nosql_databases>MongoDB, Apache Cassandra, Amazon DynamoDB, Redis</nosql_databases>
    <time_series_databases>InfluxDB, Amazon Timestream, Apache Druid</time_series_databases>
  </data_storage>
  
  <processing_engines>
    <batch_processing>Apache Spark, Apache Beam, Databricks, Google Dataflow</batch_processing>
    <stream_processing>Apache Flink, Apache Kafka Streams, Apache Storm</stream_processing>
    <sql_engines>Presto, Trino, Apache Drill, Dremio</sql_engines>
    <transformation_tools>dbt, Dataform, Apache Airflow, Prefect</transformation_tools>
  </processing_engines>
  
  <orchestration_platforms>
    <workflow_orchestration>Apache Airflow, Prefect, Dagster, Flyte</workflow_orchestration>
    <cloud_orchestration>AWS Step Functions, Azure Data Factory, Google Cloud Composer</cloud_orchestration>
    <event_orchestration>Apache Kafka, AWS EventBridge, Azure Service Bus</event_orchestration>
    <container_orchestration>Kubernetes, Docker Swarm, AWS ECS</container_orchestration>
  </orchestration_platforms>
  
  <analytics_visualization>
    <business_intelligence>Tableau, Power BI, Looker, Apache Superset</business_intelligence>
    <data_science_platforms>Jupyter, Databricks, SageMaker, Azure ML</data_science_platforms>
    <embedded_analytics>Apache Superset, Grafana, Metabase, Chartio</embedded_analytics>
    <real_time_dashboards>Grafana, Kibana, DataDog, New Relic</real_time_dashboards>
  </analytics_visualization>
</technology_stack>
```

## Best Practices

```xml
<best_practices>
  <data_engineering_principles>
    <data_quality_first>Implement data quality checks at every stage</data_quality_first>
    <schema_evolution>Design for schema evolution and backward compatibility</schema_evolution>
    <idempotent_processing>Ensure data processing is idempotent and replayable</idempotent_processing>
    <monitoring_observability>Comprehensive monitoring and observability</monitoring_observability>
    <cost_optimization>Optimize for processing costs and resource utilization</cost_optimization>
  </data_engineering_principles>
  
  <pipeline_development>
    <modular_design>Build modular, reusable data pipeline components</modular_design>
    <error_handling>Robust error handling and failure recovery</error_handling>
    <testing_strategy>Comprehensive testing including unit, integration, and data tests</testing_strategy>
    <documentation>Clear documentation for data lineage and business logic</documentation>
    <version_control>Version control for all data pipeline code and configurations</version_control>
  </pipeline_development>
  
  <data_governance>
    <data_cataloging>Maintain comprehensive data catalog and metadata</data_cataloging>
    <access_control>Role-based access control and data security</access_control>
    <compliance_management>Automated compliance monitoring and reporting</compliance_management>
    <data_lineage>Complete data lineage tracking and impact analysis</data_lineage>
    <privacy_protection>Data privacy and anonymization practices</privacy_protection>
  </data_governance>
</best_practices>
```

## Research & Innovation Focus

```xml
<research_innovation>
  <emerging_technologies>
    <real_time_ml>Real-time machine learning and feature serving</real_time_ml>
    <edge_analytics>Edge computing and distributed analytics</edge_analytics>
    <quantum_computing>Quantum computing for data processing</quantum_computing>
    <blockchain_data>Blockchain and distributed ledger data processing</blockchain_data>
  </emerging_technologies>
  
  <data_innovation>
    <automated_data_discovery>AI-powered data discovery and cataloging</automated_data_discovery>
    <intelligent_pipeline_optimization>AI-driven pipeline optimization</intelligent_pipeline_optimization>
    <federated_learning>Federated learning and privacy-preserving analytics</federated_learning>
    <graph_analytics>Graph databases and network analysis</graph_analytics>
  </data_innovation>
  
  <performance_optimization>
    <query_optimization>Advanced query optimization and cost reduction</query_optimization>
    <resource_efficiency>Intelligent resource allocation and scaling</resource_efficiency>
    <compression_techniques>Advanced data compression and storage optimization</compression_techniques>
    <parallel_processing>Massively parallel processing and distributed computing</parallel_processing>
  </performance_optimization>
</research_innovation>
```

## Usage Instructions

```xml
<usage_instructions>
  <initialization>
    <setup_command>Use `/init` command with data-analytics-engineering-rd template</setup_command>
    <data_architecture_design>Design data architecture and processing patterns</data_architecture_design>
    <technology_selection>Select appropriate technologies and tools</technology_selection>
    <quality_framework_setup>Configure data quality and monitoring frameworks</quality_framework_setup>
  </initialization>
  
  <development_workflow>
    <data_modeling_phase>Design data models and schemas</data_modeling_phase>
    <pipeline_development_phase>Build and test data pipelines</pipeline_development_phase>
    <quality_validation_phase>Implement data quality checks and monitoring</quality_validation_phase>
    <analytics_development_phase>Develop analytics and visualization layers</analytics_development_phase>
  </development_workflow>
  
  <operational_management>
    <pipeline_monitoring>Continuous monitoring of data pipelines</pipeline_monitoring>
    <quality_monitoring>Automated data quality monitoring and alerting</quality_monitoring>
    <performance_optimization>Regular performance tuning and optimization</performance_optimization>
    <cost_management>Cost monitoring and optimization strategies</cost_management>
  </operational_management>
</usage_instructions>
```

**Usage**: Apply this template for data and analytics engineering projects focused on building scalable, reliable data platforms and real-time analytics systems. Optimized for data engineers working on modern data stacks, streaming analytics, and data quality engineering.