# Data Engineering Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Data Engineering domain template provides specialized framework configuration for data pipeline development, ETL/ELT processing, and data platform engineering. This template optimizes the Claude Code Framework for large-scale data processing, real-time streaming, and data infrastructure workflows.

## Domain Configuration

```xml
<data_engineering_domain>
  <purpose>Specialized framework configuration for data engineering and platform development</purpose>
  
  <data_processing_types>
    <batch_processing>Large-scale batch data processing and transformation</batch_processing>
    <stream_processing>Real-time data streaming and event processing</stream_processing>
    <data_warehousing>Data warehouse and analytics platform development</data_warehousing>
    <data_lakes>Data lake architecture and data mesh implementation</data_lakes>
  </data_processing_types>
  
  <development_characteristics>
    <scalability_first>Scalable data processing architecture</scalability_first>
    <performance_critical>High-performance data transformation</performance_critical>
    <reliability_focused>Fault-tolerant and resilient data pipelines</reliability_focused>
    <observability_driven>Comprehensive data pipeline monitoring</observability_driven>
    <quality_assured>Data quality validation and governance</quality_assured>
  </development_characteristics>
</data_engineering_domain>
```

## Template Variables

```xml
<template_variables>
  <data_platform_configuration>
    <processing_engine>{{PROCESSING_ENGINE:spark|flink|beam|dask|ray}}</processing_engine>
    <orchestration_tool>{{ORCHESTRATION_TOOL:airflow|prefect|dagster|kubeflow|argo}}</orchestration_tool>
    <storage_system>{{STORAGE_SYSTEM:s3|hdfs|gcs|azure_blob|delta_lake}}</storage_system>
    <streaming_platform>{{STREAMING_PLATFORM:kafka|kinesis|pulsar|pubsub|eventhub}}</streaming_platform>
  </data_platform_configuration>
  
  <project_configuration>
    <project_name>{{PROJECT_NAME:string}}</project_name>
    <data_domain>{{DATA_DOMAIN:analytics|ml_platform|real_time|data_mesh|lakehouse}}</data_domain>
    <processing_pattern>{{PROCESSING_PATTERN:batch|streaming|hybrid|micro_batch}}</processing_pattern>
    <deployment_target>{{DEPLOYMENT_TARGET:cloud|on_premise|hybrid|edge}}</deployment_target>
  </project_configuration>
  
  <technical_settings>
    <primary_language>{{PRIMARY_LANGUAGE:python|scala|java|sql|go}}</primary_language>
    <data_format>{{DATA_FORMAT:parquet|avro|json|csv|orc|delta}}</data_format>
    <catalog_system>{{CATALOG_SYSTEM:hive|glue|unity_catalog|atlas|datahub}}</catalog_system>
    <compute_platform>{{COMPUTE_PLATFORM:kubernetes|yarn|mesos|databricks|emr}}</compute_platform>
  </technical_settings>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <data_engineering_thinking>
      <scalability_assessment>Evaluate data processing scalability and performance</scalability_assessment>
      <data_quality_validation>Ensure data quality and validation mechanisms</data_quality_validation>
      <pipeline_reliability>Assess pipeline fault tolerance and error handling</pipeline_reliability>
      <resource_optimization>Optimize resource utilization and cost efficiency</resource_optimization>
    </data_engineering_thinking>
    
    <quality_gates>
      <data_quality_testing>Comprehensive data quality and validation testing</data_quality_testing>
      <performance_testing>Data processing performance and scalability testing</performance_testing>
      <reliability_testing>Pipeline reliability and fault tolerance testing</reliability_testing>
      <integration_testing>End-to-end data pipeline integration testing</integration_testing>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <data_engineering_planning>
      <data_architecture>Design scalable and efficient data architecture</data_architecture>
      <pipeline_design>Design robust and maintainable data pipelines</pipeline_design>
      <quality_framework>Implement comprehensive data quality framework</quality_framework>
      <monitoring_observability>Design data pipeline monitoring and observability</monitoring_observability>
    </data_engineering_planning>
    
    <development_workflow>
      <data_driven_development>Data-driven development with quality validation</data_driven_development>
      <testing_automation>Automated testing for data pipelines and quality</testing_automation>
      <performance_optimization>Performance optimization and resource tuning</performance_optimization>
      <operational_excellence>Operational excellence and monitoring implementation</operational_excellence>
    </development_workflow>
  </feature_command>
  
  <validate_command>
    <data_engineering_validation>
      <pipeline_validation>Data pipeline functionality and reliability validation</pipeline_validation>
      <quality_validation>Data quality and validation rule verification</quality_validation>
      <performance_validation>Performance benchmarking and optimization validation</performance_validation>
      <operational_validation>Operational readiness and monitoring validation</operational_validation>
    </data_engineering_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates Configuration

```xml
<quality_gates_configuration>
  <data_quality>
    <completeness_validation>
      <rule>Data completeness meets quality standards</rule>
      <validation>Automated data completeness monitoring and alerting</validation>
      <threshold>95% data completeness for critical datasets</threshold>
    </completeness_validation>
    
    <accuracy_validation>
      <rule>Data accuracy verified through validation rules</rule>
      <validation>Data accuracy testing and anomaly detection</validation>
      <threshold>99% data accuracy for business-critical fields</threshold>
    </accuracy_validation>
    
    <consistency_validation>
      <rule>Data consistency maintained across all pipeline stages</rule>
      <validation>Cross-reference validation and consistency checking</validation>
      <threshold>Zero critical data consistency violations</threshold>
    </consistency_validation>
  </data_quality>
  
  <pipeline_quality>
    <reliability_validation>
      <rule>Data pipelines are fault-tolerant and resilient</rule>
      <validation>Fault injection testing and error handling validation</validation>
      <threshold>99.9% pipeline reliability with automated recovery</threshold>
    </reliability_validation>
    
    <performance_validation>
      <rule>Pipeline performance meets processing requirements</rule>
      <validation>Performance benchmarking and load testing</validation>
      <threshold>Processing latency within SLA requirements</threshold>
    </performance_validation>
    
    <scalability_validation>
      <rule>Pipelines scale efficiently with data volume growth</rule>
      <validation>Scalability testing and resource utilization monitoring</validation>
      <threshold>Linear scaling with data volume increase</threshold>
    </scalability_validation>
  </pipeline_quality>
  
  <operational_quality>
    <monitoring_coverage>
      <rule>Comprehensive monitoring for all data pipelines</rule>
      <validation>Monitoring coverage analysis and alerting validation</validation>
      <threshold>100% critical pipeline monitoring coverage</threshold>
    </monitoring_coverage>
    
    <data_lineage>
      <rule>Complete data lineage tracking and documentation</rule>
      <validation>Data lineage validation and impact analysis</validation>
      <threshold>100% data lineage coverage for critical datasets</threshold>
    </data_lineage>
    
    <security_compliance>
      <rule>Data security and privacy compliance maintained</rule>
      <validation>Security scanning and compliance validation</validation>
      <threshold>100% compliance with data governance policies</threshold>
    </security_compliance>
  </operational_quality>
</quality_gates_configuration>
```

## Module Selection

```xml
<module_selection>
  <core_modules>
    <data_engineering>
      <pipeline_orchestration>Data pipeline orchestration and workflow management</pipeline_orchestration>
      <data_processing>Scalable data processing and transformation patterns</data_processing>
      <quality_framework>Comprehensive data quality and validation framework</quality_framework>
      <monitoring_observability>Data pipeline monitoring and observability systems</monitoring_observability>
    </data_engineering>
    
    <domain_specific>
      <batch_processing condition="{{PROCESSING_PATTERN:batch|hybrid}}">
        <etl_patterns>ETL/ELT processing patterns and optimization</etl_patterns>
        <data_warehousing>Data warehouse loading and optimization</data_warehousing>
        <batch_optimization>Batch processing optimization and tuning</batch_optimization>
      </batch_processing>
      
      <stream_processing condition="{{PROCESSING_PATTERN:streaming|hybrid}}">
        <real_time_processing>Real-time stream processing patterns</real_time_processing>
        <event_driven_architecture>Event-driven architecture and messaging</event_driven_architecture>
        <streaming_analytics>Stream analytics and real-time aggregation</streaming_analytics>
      </stream_processing>
      
      <data_platform condition="{{DATA_DOMAIN:ml_platform|data_mesh|lakehouse}}">
        <feature_store>Feature store implementation and management</feature_store>
        <data_mesh>Data mesh architecture and domain-driven design</data_mesh>
        <lakehouse_architecture>Lakehouse architecture and unified analytics</lakehouse_architecture>
      </data_platform>
    </domain_specific>
  </core_modules>
  
  <processing_modules>
    <spark_processing>
      <spark_optimization>Apache Spark optimization and tuning</spark_optimization>
      <spark_streaming>Spark Streaming and structured streaming</spark_streaming>
      <spark_sql>Spark SQL optimization and query tuning</spark_sql>
      <spark_mllib>Spark MLlib integration for machine learning</spark_mllib>
    </spark_processing>
    
    <streaming_processing>
      <kafka_integration>Apache Kafka integration and optimization</kafka_integration>
      <flink_processing>Apache Flink stream processing patterns</flink_processing>
      <beam_pipelines>Apache Beam unified processing model</beam_pipelines>
      <event_processing>Complex event processing and pattern matching</event_processing>
    </streaming_processing>
  </processing_modules>
  
  <infrastructure_modules>
    <data_storage>
      <data_lake_architecture>Data lake architecture and organization</data_lake_architecture>
      <delta_lake_patterns>Delta Lake ACID transactions and versioning</delta_lake_patterns>
      <partitioning_strategies>Data partitioning and optimization strategies</partitioning_strategies>
      <compression_optimization>Data compression and storage optimization</compression_optimization>
    </data_storage>
    
    <orchestration_platforms>
      <airflow_patterns>Apache Airflow DAG patterns and best practices</airflow_patterns>
      <prefect_workflows>Prefect workflow orchestration and management</prefect_workflows>
      <dagster_pipelines>Dagster pipeline development and operations</dagster_pipelines>
      <kubernetes_orchestration>Kubernetes-based data pipeline orchestration</kubernetes_orchestration>
    </orchestration_platforms>
  </infrastructure_modules>
</module_selection>
```

## Framework Integration

```xml
<framework_integration>
  <optimal_frameworks>
    <primary_framework>SPARK - Strategic problem-solving with actionable knowledge creation</primary_framework>
    <secondary_framework>TRACE - Thorough requirements analysis with comprehensive evaluation</secondary_framework>
    <specialized_framework>SCALE - Scalable architecture with comprehensive lifecycle excellence</specialized_framework>
  </optimal_frameworks>
  
  <framework_customization>
    <spark_data_engineering_optimization>
      <situation>Current data landscape, processing requirements, and scale challenges</situation>
      <problem>Specific data engineering challenges and performance requirements</problem>
      <action>Scalable data pipeline implementation with optimization and monitoring</action>
      <result>Efficient, reliable data processing with comprehensive observability</result>
      <knowledge>Transferable data engineering patterns and optimization techniques</knowledge>
    </spark_data_engineering_optimization>
    
    <trace_data_engineering_optimization>
      <task>Data engineering requirements with scalability and reliability focus</task>
      <reasoning>Data architecture and processing strategy rationale</reasoning>
      <action>Pipeline implementation with quality validation and monitoring</action>
      <conclusion>Reliable data platform delivery with comprehensive quality assurance</conclusion>
      <evaluation>Performance testing, quality validation, and operational readiness</evaluation>
    </trace_data_engineering_optimization>
  </framework_customization>
</framework_integration>
```

## Development Workflows

```xml
<development_workflows>
  <data_engineering_cycle>
    <requirements_analysis>
      <step>Define data processing requirements and quality standards</step>
      <step>Analyze data sources and target destinations</step>
      <step>Design data architecture and processing strategy</step>
      <step>Plan monitoring and observability implementation</step>
    </requirements_analysis>
    
    <pipeline_development>
      <step>Develop data processing logic with quality validation</step>
      <step>Implement error handling and fault tolerance</step>
      <step>Add monitoring and observability instrumentation</step>
      <step>Optimize performance and resource utilization</step>
    </pipeline_development>
    
    <testing_validation>
      <step>Unit testing for data transformation logic</step>
      <step>Integration testing for end-to-end pipelines</step>
      <step>Performance testing and load validation</step>
      <step>Data quality testing and validation</step>
    </testing_validation>
    
    <deployment_operations>
      <step>Deploy pipelines with orchestration platform</step>
      <step>Implement monitoring and alerting systems</step>
      <step>Establish operational procedures and runbooks</step>
      <step>Conduct operational readiness and capacity planning</step>
    </deployment_operations>
  </data_engineering_cycle>
  
  <specialized_workflows>
    <data_quality_workflow>
      <profiling_analysis>Data profiling and quality assessment</profiling_analysis>
      <validation_rules>Data validation rule definition and implementation</validation_rules>
      <quality_monitoring>Continuous data quality monitoring and alerting</quality_monitoring>
      <remediation_procedures>Data quality remediation and correction procedures</remediation_procedures>
    </data_quality_workflow>
    
    <streaming_pipeline_workflow>
      <event_modeling>Event schema design and evolution management</event_modeling>
      <stream_processing>Real-time stream processing implementation</stream_processing>
      <state_management>Stream processing state management and recovery</state_management>
      <backpressure_handling>Backpressure handling and flow control</backpressure_handling>
    </streaming_pipeline_workflow>
  </specialized_workflows>
</development_workflows>
```

## Data Architecture Patterns

```xml
<data_architecture_patterns>
  <lakehouse_architecture>
    <unified_storage>
      <data_lake_foundation>Data lake as the single source of truth</data_lake_foundation>
      <acid_transactions>ACID transactions for data consistency</acid_transactions>
      <schema_enforcement>Schema enforcement and evolution management</schema_enforcement>
      <time_travel>Data versioning and time travel capabilities</time_travel>
    </unified_storage>
    
    <processing_layers>
      <bronze_layer>Raw data ingestion and initial processing</bronze_layer>
      <silver_layer>Cleaned and validated data with quality checks</silver_layer>
      <gold_layer>Business-ready data with aggregations and metrics</gold_layer>
      <serving_layer>Optimized data serving for analytics and ML</serving_layer>
    </processing_layers>
  </lakehouse_architecture>
  
  <data_mesh_patterns>
    <domain_oriented>
      <data_products>Domain-specific data products and ownership</data_products>
      <federated_governance>Federated data governance and standards</federated_governance>
      <self_serve_platform>Self-serve data platform capabilities</self_serve_platform>
      <observability_integration>Integrated observability and monitoring</observability_integration>
    </domain_oriented>
    
    <platform_capabilities>
      <data_catalog>Comprehensive data catalog and discovery</data_catalog>
      <quality_framework>Automated data quality and validation</quality_framework>
      <lineage_tracking>End-to-end data lineage and impact analysis</lineage_tracking>
      <access_control>Fine-grained access control and security</access_control>
    </platform_capabilities>
  </data_mesh_patterns>
</data_architecture_patterns>
```

## Performance Optimization

```xml
<performance_optimization>
  <processing_optimization>
    <spark_optimization>
      <memory_management>Spark memory management and garbage collection tuning</memory_management>
      <partition_optimization>Data partitioning and partition pruning optimization</partition_optimization>
      <caching_strategies>Intelligent caching and persistence strategies</caching_strategies>
      <sql_optimization>Spark SQL query optimization and plan analysis</sql_optimization>
    </spark_optimization>
    
    <streaming_optimization>
      <throughput_optimization>Stream processing throughput and latency optimization</throughput_optimization>
      <parallelism_tuning>Parallelism and resource allocation tuning</parallelism_tuning>
      <state_optimization>Stream processing state optimization and checkpointing</state_optimization>
      <windowing_optimization>Windowing and aggregation optimization</windowing_optimization>
    </streaming_optimization>
  </processing_optimization>
  
  <storage_optimization>
    <data_layout>
      <file_formats>Optimized file formats and compression strategies</file_formats>
      <partitioning_schemes>Intelligent partitioning and bucketing schemes</partitioning_schemes>
      <indexing_strategies>Data indexing and search optimization</indexing_strategies>
      <compaction_strategies>Data compaction and optimization strategies</compaction_strategies>
    </data_layout>
    
    <query_optimization>
      <predicate_pushdown>Predicate pushdown and projection optimization</predicate_pushdown>
      <join_optimization>Join optimization and broadcast strategies</join_optimization>
      <aggregation_optimization>Aggregation and grouping optimization</aggregation_optimization>
      <materialized_views>Materialized views and precomputed aggregations</materialized_views>
    </query_optimization>
  </storage_optimization>
</performance_optimization>
```

## Data Quality Framework

```xml
<data_quality_framework>
  <quality_dimensions>
    <completeness>
      <null_checking>Null value detection and handling</null_checking>
      <missing_data>Missing data identification and imputation</missing_data>
      <record_completeness>Record-level completeness validation</record_completeness>
      <field_completeness>Field-level completeness monitoring</field_completeness>
    </completeness>
    
    <accuracy>
      <format_validation>Data format and pattern validation</format_validation>
      <range_validation>Value range and boundary validation</range_validation>
      <reference_validation>Reference data validation and lookup</reference_validation>
      <business_rule_validation>Business rule and constraint validation</business_rule_validation>
    </accuracy>
    
    <consistency>
      <cross_field_validation>Cross-field consistency validation</cross_field_validation>
      <temporal_consistency>Temporal data consistency validation</temporal_consistency>
      <referential_integrity>Referential integrity and relationship validation</referential_integrity>
      <duplicate_detection>Duplicate detection and resolution</duplicate_detection>
    </consistency>
  </quality_dimensions>
  
  <validation_framework>
    <rule_engine>
      <configurable_rules>Configurable validation rules and thresholds</configurable_rules>
      <custom_validators>Custom validation functions and logic</custom_validators>
      <rule_versioning>Validation rule versioning and evolution</rule_versioning>
      <exception_handling>Validation exception handling and reporting</exception_handling>
    </rule_engine>
    
    <monitoring_alerting>
      <quality_metrics>Data quality metrics and trend analysis</quality_metrics>
      <threshold_monitoring>Quality threshold monitoring and alerting</threshold_monitoring>
      <anomaly_detection>Data quality anomaly detection and investigation</anomaly_detection>
      <quality_reporting>Comprehensive quality reporting and dashboards</quality_reporting>
    </monitoring_alerting>
  </validation_framework>
</data_quality_framework>
```

## Testing Strategy

```xml
<testing_strategy>
  <data_pipeline_testing>
    <unit_testing>
      <transformation_testing>Data transformation logic unit testing</transformation_testing>
      <validation_testing>Data validation rule unit testing</validation_testing>
      <utility_testing>Data processing utility function testing</utility_testing>
      <coverage_analysis>Code coverage analysis for data processing logic</coverage_analysis>
    </unit_testing>
    
    <integration_testing>
      <pipeline_testing>End-to-end data pipeline integration testing</pipeline_testing>
      <system_integration>External system integration testing</system_integration>
      <data_flow_testing>Data flow and dependency testing</data_flow_testing>
      <performance_testing>Pipeline performance and scalability testing</performance_testing>
    </integration_testing>
  </data_pipeline_testing>
  
  <data_testing_framework>
    <data_validation_testing>
      <schema_testing>Data schema validation and evolution testing</schema_testing>
      <quality_testing>Data quality rule testing and validation</quality_testing>
      <freshness_testing>Data freshness and timeliness testing</freshness_testing>
      <volume_testing>Data volume and throughput testing</volume_testing>
    </data_validation_testing>
    
    <regression_testing>
      <data_drift_testing>Data drift detection and regression testing</data_drift_testing>
      <pipeline_regression>Pipeline behavior regression testing</pipeline_regression>
      <performance_regression>Performance regression testing and monitoring</performance_regression>
      <quality_regression>Data quality regression testing</quality_regression>
    </regression_testing>
  </data_testing_framework>
</testing_strategy>
```

## Deployment Configuration

```xml
<deployment_configuration>
  <pipeline_deployment>
    <orchestration_deployment>
      <airflow_deployment>Apache Airflow deployment and configuration</airflow_deployment>
      <kubernetes_deployment>Kubernetes-based pipeline deployment</kubernetes_deployment>
      <containerized_deployment>Containerized pipeline deployment and scaling</containerized_deployment>
      <serverless_deployment>Serverless data processing deployment</serverless_deployment>
    </orchestration_deployment>
    
    <environment_management>
      <multi_environment>Development, staging, and production environments</multi_environment>
      <configuration_management>Environment-specific configuration management</configuration_management>
      <data_isolation>Data isolation and environment security</data_isolation>
      <promotion_pipeline>Automated pipeline promotion and validation</promotion_pipeline>
    </environment_management>
  </pipeline_deployment>
  
  <monitoring_deployment>
    <observability_stack>
      <metrics_collection>Pipeline metrics collection and aggregation</metrics_collection>
      <logging_aggregation>Centralized logging and log analysis</logging_aggregation>
      <distributed_tracing>Distributed tracing for data lineage</distributed_tracing>
      <alerting_systems>Comprehensive alerting and notification systems</alerting_systems>
    </observability_stack>
    
    <data_governance>
      <catalog_deployment>Data catalog deployment and configuration</catalog_deployment>
      <lineage_tracking>Data lineage tracking and visualization</lineage_tracking>
      <access_control>Data access control and security policies</access_control>
      <compliance_monitoring>Data compliance monitoring and reporting</compliance_monitoring>
    </data_governance>
  </monitoring_deployment>
</deployment_configuration>
```

## Documentation Templates

```xml
<documentation_templates>
  <data_engineering_documentation>
    <architecture_documentation>
      <data_architecture>Data architecture and flow diagrams</data_architecture>
      <pipeline_architecture>Pipeline architecture and processing flow</pipeline_architecture>
      <system_integration>System integration and data source documentation</system_integration>
      <technology_stack>Technology stack and component documentation</technology_stack>
    </architecture_documentation>
    
    <operational_documentation>
      <pipeline_runbooks>Data pipeline operational runbooks</pipeline_runbooks>
      <monitoring_procedures>Monitoring and alerting procedures</monitoring_procedures>
      <troubleshooting_guides>Pipeline troubleshooting and debugging guides</troubleshooting_guides>
      <incident_response>Data incident response and recovery procedures</incident_response>
    </operational_documentation>
  </data_engineering_documentation>
  
  <data_documentation>
    <data_catalog>
      <dataset_documentation>Dataset documentation and metadata</dataset_documentation>
      <schema_documentation>Data schema documentation and evolution</schema_documentation>
      <lineage_documentation>Data lineage and dependency documentation</lineage_documentation>
      <quality_documentation>Data quality metrics and validation documentation</quality_documentation>
    </data_catalog>
    
    <user_guides>
      <data_consumer_guide>Data consumer usage guide and best practices</data_consumer_guide>
      <api_documentation>Data API documentation and usage examples</api_documentation>
      <query_guide>Data querying guide and optimization tips</query_guide>
      <troubleshooting_guide>Data access troubleshooting and support guide</troubleshooting_guide>
    </user_guides>
  </data_documentation>
</documentation_templates>
```

## Success Metrics

```xml
<success_metrics>
  <pipeline_metrics>
    <reliability_metrics>Pipeline reliability and uptime metrics</reliability_metrics>
    <performance_metrics>Processing performance and throughput metrics</performance_metrics>
    <quality_metrics>Data quality scores and validation metrics</quality_metrics>
    <efficiency_metrics>Resource utilization and cost efficiency metrics</efficiency_metrics>
  </pipeline_metrics>
  
  <data_metrics>
    <freshness_metrics>Data freshness and timeliness metrics</freshness_metrics>
    <completeness_metrics>Data completeness and coverage metrics</completeness_metrics>
    <accuracy_metrics>Data accuracy and validation success metrics</accuracy_metrics>
    <usage_metrics>Data usage and adoption metrics</usage_metrics>
  </data_metrics>
  
  <operational_metrics>
    <deployment_metrics>Pipeline deployment frequency and success rate</deployment_metrics>
    <incident_metrics>Data incident response time and resolution metrics</incident_metrics>
    <scalability_metrics>System scalability and performance under load</scalability_metrics>
    <governance_metrics>Data governance compliance and audit metrics</governance_metrics>
  </operational_metrics>
</success_metrics>
```

---

**Reference**: This template provides comprehensive data engineering domain configuration, enabling specialized framework adaptation for scalable data pipelines, real-time streaming, and data platform engineering with comprehensive quality validation, monitoring, and governance capabilities.