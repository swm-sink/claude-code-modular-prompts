| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

# Domain Classification System

────────────────────────────────────────────────────────────────────────────────

## Purpose

The Domain Classification System provides intelligent, automated domain detection based on project characteristics, technology stack, and development patterns. This system enables accurate framework customization and optimization for specific development domains.

## Classification Framework

```xml
<domain_classification_system>
  <purpose>Intelligent domain detection with confidence scoring and customization recommendations</purpose>
  
  <classification_methodology>
    <analysis_dimensions>
      <technology_stack>Programming languages, frameworks, libraries, tools</technology_stack>
      <project_structure>Directory patterns, file organization, architectural indicators</project_structure>
      <domain_artifacts>Domain-specific files, configurations, documentation</domain_artifacts>
      <development_patterns>Workflow indicators, testing patterns, deployment strategies</development_patterns>
      <business_context>Industry indicators, compliance requirements, scaling patterns</business_context>
    </analysis_dimensions>
    
    <scoring_algorithm>
      <weight_factors>
        <technology_stack_weight>35%</technology_stack_weight>
        <project_structure_weight>25%</project_structure_weight>
        <domain_artifacts_weight>20%</domain_artifacts_weight>
        <development_patterns_weight>15%</development_patterns_weight>
        <business_context_weight>5%</business_context_weight>
      </weight_factors>
      
      <confidence_thresholds>
        <high_confidence>85%+ - Strong domain indicators across multiple dimensions</high_confidence>
        <medium_confidence>70-84% - Clear domain indicators with some ambiguity</medium_confidence>
        <low_confidence>50-69% - Weak domain indicators, manual review recommended</low_confidence>
        <unclear>Below 50% - Insufficient indicators for classification</unclear>
      </confidence_thresholds>
    </scoring_algorithm>
  </classification_methodology>
</domain_classification_system>
```

## Domain Definitions

### Mobile Development
```xml
<mobile_development_domain>
  <primary_indicators>
    <technology_stack>
      <ios>Swift, Objective-C, Xcode projects, CocoaPods, Swift Package Manager</ios>
      <android>Kotlin, Java, Android Studio, Gradle, Android SDK</android>
      <cross_platform>React Native, Flutter, Xamarin, Ionic, PhoneGap</cross_platform>
    </technology_stack>
    
    <project_structure>
      <ios_patterns>*.xcodeproj, *.xcworkspace, Podfile, Info.plist</ios_patterns>
      <android_patterns>build.gradle, AndroidManifest.xml, res/, src/main/</android_patterns>
      <cross_platform_patterns>metro.config.js, pubspec.yaml, package.json with RN/Flutter</cross_platform_patterns>
    </project_structure>
    
    <domain_artifacts>
      <configuration>App store configurations, certificate management, device provisioning</configuration>
      <assets>Image assets for multiple screen densities, app icons, splash screens</assets>
      <platform_specific>Platform-specific native modules, bridging code</platform_specific>
    </domain_artifacts>
  </primary_indicators>
  
  <secondary_indicators>
    <development_patterns>Push notifications, offline data sync, biometric authentication</development_patterns>
    <testing_patterns>Device testing, simulator testing, UI automation</testing_patterns>
    <deployment_patterns>App store deployment, TestFlight, Google Play Console</deployment_patterns>
  </secondary_indicators>
  
  <confidence_modifiers>
    <boost_factors>Multiple platform support, native module development, app store artifacts</boost_factors>
    <reduction_factors>Web-only components, server-side only code, desktop-only patterns</reduction_factors>
  </confidence_modifiers>
</mobile_development_domain>
```

### Data Analytics
```xml
<data_analytics_domain>
  <primary_indicators>
    <technology_stack>
      <python>pandas, numpy, scikit-learn, matplotlib, seaborn, plotly</python>
      <r>ggplot2, dplyr, tidyr, caret, shiny</r>
      <sql>Data warehouse connections, complex queries, reporting views</sql>
      <visualization>Tableau, Power BI, D3.js, Grafana</visualization>
    </technology_stack>
    
    <project_structure>
      <notebooks>*.ipynb, Jupyter notebooks, R Markdown files</notebooks>
      <data_directories>data/, datasets/, raw/, processed/, cleaned/</data_directories>
      <analysis_structure>analysis/, reports/, visualizations/, models/</analysis_structure>
    </project_structure>
    
    <domain_artifacts>
      <data_sources>CSV files, database connections, API integrations</data_sources>
      <analysis_outputs>Reports, dashboards, statistical models</analysis_outputs>
      <documentation>Data dictionaries, analysis methodologies, findings</documentation>
    </domain_artifacts>
  </primary_indicators>
  
  <secondary_indicators>
    <development_patterns>Exploratory data analysis, statistical modeling, hypothesis testing</development_patterns>
    <workflow_patterns>Data cleaning, feature engineering, model validation</workflow_patterns>
    <reporting_patterns>Automated reporting, dashboard creation, stakeholder presentations</reporting_patterns>
  </secondary_indicators>
  
  <confidence_modifiers>
    <boost_factors>Multiple data sources, statistical analysis, visualization libraries</boost_factors>
    <reduction_factors>Production ML pipelines, real-time processing, API development</reduction_factors>
  </confidence_modifiers>
</data_analytics_domain>
```

### Financial Technology
```xml
<financial_technology_domain>
  <primary_indicators>
    <technology_stack>
      <languages>Java, C#, Python, Go, Rust (performance-critical)</languages>
      <frameworks>Spring Boot, .NET, Django, FastAPI</frameworks>
      <databases>PostgreSQL, Oracle, SQL Server, MongoDB</databases>
      <security>OAuth, JWT, encryption libraries, HSM integration</security>
    </technology_stack>
    
    <project_structure>
      <compliance_dirs>compliance/, audit/, security/, regulatory/</compliance_dirs>
      <financial_modules>payments/, transactions/, accounts/, risk/</financial_modules>
      <integration_patterns>apis/, integrations/, third-party/, banks/</integration_patterns>
    </project_structure>
    
    <domain_artifacts>
      <compliance_files>SOX compliance, PCI-DSS, GDPR documentation</compliance_files>
      <financial_configs>Payment gateway configs, banking APIs, regulatory settings</financial_configs>
      <security_artifacts>Encryption keys, certificates, security policies</security_artifacts>
    </domain_artifacts>
  </primary_indicators>
  
  <secondary_indicators>
    <development_patterns>Transaction processing, risk management, compliance reporting</development_patterns>
    <security_patterns>Multi-factor authentication, encryption, audit logging</security_patterns>
    <integration_patterns>Banking APIs, payment processors, regulatory reporting</integration_patterns>
  </secondary_indicators>
  
  <confidence_modifiers>
    <boost_factors>Compliance documentation, financial APIs, security frameworks</boost_factors>
    <reduction_factors>Non-financial business logic, consumer applications, basic web features</reduction_factors>
  </confidence_modifiers>
</financial_technology_domain>
```

### DevOps & Platform Engineering
```xml
<devops_platform_domain>
  <primary_indicators>
    <technology_stack>
      <infrastructure>Docker, Kubernetes, Terraform, Ansible, CloudFormation</infrastructure>
      <cicd>Jenkins, GitLab CI, GitHub Actions, CircleCI, Azure DevOps</cicd>
      <monitoring>Prometheus, Grafana, ELK Stack, Datadog, New Relic</monitoring>
      <cloud>AWS, Azure, GCP, cloud-native services</cloud>
    </technology_stack>
    
    <project_structure>
      <infrastructure_dirs>infrastructure/, terraform/, k8s/, helm/</infrastructure_dirs>
      <cicd_dirs>.github/, .gitlab-ci.yml, Jenkinsfile, pipelines/</cicd_dirs>
      <monitoring_dirs>monitoring/, observability/, alerts/, dashboards/</monitoring_dirs>
    </project_structure>
    
    <domain_artifacts>
      <infrastructure_code>Terraform files, CloudFormation templates, Kubernetes manifests</infrastructure_code>
      <deployment_configs>CI/CD pipelines, deployment scripts, environment configs</deployment_configs>
      <monitoring_configs>Prometheus configs, Grafana dashboards, alerting rules</monitoring_configs>
    </domain_artifacts>
  </primary_indicators>
  
  <secondary_indicators>
    <development_patterns>Infrastructure as Code, GitOps, automated deployments</development_patterns>
    <operational_patterns>Monitoring, alerting, incident response, capacity planning</operational_patterns>
    <security_patterns>Secret management, security scanning, compliance automation</security_patterns>
  </secondary_indicators>
  
  <confidence_modifiers>
    <boost_factors>Multiple infrastructure tools, CI/CD pipelines, monitoring systems</boost_factors>
    <reduction_factors>Application-only code, business logic, user interface components</reduction_factors>
  </confidence_modifiers>
</devops_platform_domain>
```

### Data Engineering
```xml
<data_engineering_domain>
  <primary_indicators>
    <technology_stack>
      <processing>Apache Spark, Hadoop, Kafka, Airflow, Flink</processing>
      <storage>HDFS, S3, BigQuery, Snowflake, Redshift</storage>
      <orchestration>Airflow, Prefect, Dagster, Kubeflow</orchestration>
      <streaming>Kafka, Kinesis, Pulsar, Apache Beam</streaming>
    </technology_stack>
    
    <project_structure>
      <pipeline_dirs>pipelines/, dags/, workflows/, etl/</pipeline_dirs>
      <data_dirs>raw/, processed/, staging/, warehouse/</data_dirs>
      <config_dirs>configs/, schemas/, transformations/</config_dirs>
    </project_structure>
    
    <domain_artifacts>
      <pipeline_code>ETL scripts, data transformation logic, orchestration DAGs</pipeline_code>
      <data_schemas>Schema definitions, data contracts, validation rules</data_schemas>
      <infrastructure>Data warehouse configs, streaming configurations</infrastructure>
    </domain_artifacts>
  </primary_indicators>
  
  <secondary_indicators>
    <development_patterns>ETL/ELT processes, data validation, quality monitoring</development_patterns>
    <operational_patterns>Pipeline orchestration, data lineage, monitoring</operational_patterns>
    <scaling_patterns>Distributed processing, partitioning, optimization</scaling_patterns>
  </secondary_indicators>
  
  <confidence_modifiers>
    <boost_factors>Multiple data processing tools, orchestration systems, data infrastructure</boost_factors>
    <reduction_factors>Analysis-only code, visualization focus, single-machine processing</reduction_factors>
  </confidence_modifiers>
</data_engineering_domain>
```

### Enterprise Tools
```xml
<enterprise_tools_domain>
  <primary_indicators>
    <technology_stack>
      <enterprise_frameworks>Spring Boot, .NET, SAP, Oracle, IBM platforms</enterprise_frameworks>
      <integration>ESB, API gateways, message queues, workflow engines</integration>
      <databases>Oracle, SQL Server, DB2, enterprise data warehouses</databases>
      <security>LDAP, Active Directory, SAML, enterprise SSO</security>
    </technology_stack>
    
    <project_structure>
      <enterprise_dirs>services/, modules/, interfaces/, integrations/</enterprise_dirs>
      <config_dirs>configurations/, profiles/, environments/</config_dirs>
      <documentation_dirs>specifications/, requirements/, architecture/</documentation_dirs>
    </project_structure>
    
    <domain_artifacts>
      <enterprise_configs>Application server configs, enterprise service configs</enterprise_configs>
      <integration_artifacts>WSDL files, API specifications, message schemas</integration_artifacts>
      <documentation>Architecture documents, requirements specifications</documentation>
    </domain_artifacts>
  </primary_indicators>
  
  <secondary_indicators>
    <development_patterns>Service-oriented architecture, enterprise integration patterns</development_patterns>
    <workflow_patterns>Business process management, workflow automation</workflow_patterns>
    <compliance_patterns>Enterprise governance, audit trails, compliance reporting</compliance_patterns>
  </secondary_indicators>
  
  <confidence_modifiers>
    <boost_factors>Enterprise frameworks, integration patterns, formal documentation</boost_factors>
    <reduction_factors>Consumer applications, simple architectures, lightweight frameworks</reduction_factors>
  </confidence_modifiers>
</enterprise_tools_domain>
```

### Web Development
```xml
<web_development_domain>
  <primary_indicators>
    <technology_stack>
      <frontend>React, Vue.js, Angular, HTML/CSS/JavaScript</frontend>
      <backend>Node.js, Python, Ruby, PHP, Java</backend>
      <frameworks>Express, Django, Rails, Spring Boot, FastAPI</frameworks>
      <databases>PostgreSQL, MySQL, MongoDB, Redis</databases>
    </technology_stack>
    
    <project_structure>
      <web_dirs>public/, src/, assets/, components/, pages/</web_dirs>
      <api_dirs>api/, routes/, controllers/, services/</api_dirs>
      <config_dirs>config/, environments/, webpack/, vite/</config_dirs>
    </project_structure>
    
    <domain_artifacts>
      <web_configs>package.json, webpack.config.js, tsconfig.json</web_configs>
      <deployment_configs>Docker files, nginx configs, deployment scripts</deployment_configs>
      <api_artifacts>OpenAPI specs, API documentation, route definitions</api_artifacts>
    </domain_artifacts>
  </primary_indicators>
  
  <secondary_indicators>
    <development_patterns>MVC architecture, RESTful APIs, responsive design</development_patterns>
    <frontend_patterns>Component-based architecture, state management, routing</frontend_patterns>
    <deployment_patterns>Web server deployment, CDN usage, load balancing</deployment_patterns>
  </secondary_indicators>
  
  <confidence_modifiers>
    <boost_factors>Frontend and backend components, web-specific tools, deployment patterns</boost_factors>
    <reduction_factors>Desktop applications, mobile-only code, batch processing</reduction_factors>
  </confidence_modifiers>
</web_development_domain>
```

### Machine Learning
```xml
<machine_learning_domain>
  <primary_indicators>
    <technology_stack>
      <ml_frameworks>TensorFlow, PyTorch, scikit-learn, XGBoost, LightGBM</ml_frameworks>
      <model_serving>MLflow, Kubeflow, TensorFlow Serving, Seldon</model_serving>
      <data_processing>pandas, numpy, Spark, Dask</data_processing>
      <deployment>Docker, Kubernetes, cloud ML services</deployment>
    </technology_stack>
    
    <project_structure>
      <ml_dirs>models/, training/, inference/, experiments/</ml_dirs>
      <data_dirs>data/, features/, datasets/, preprocessed/</data_dirs>
      <pipeline_dirs>pipelines/, workflows/, orchestration/</pipeline_dirs>
    </project_structure>
    
    <domain_artifacts>
      <model_artifacts>Trained models, model configs, hyperparameter files</model_artifacts>
      <experiment_tracking>MLflow experiments, Weights & Biases configs</experiment_tracking>
      <pipeline_code>Training pipelines, inference pipelines, feature pipelines</pipeline_code>
    </domain_artifacts>
  </primary_indicators>
  
  <secondary_indicators>
    <development_patterns>Experiment tracking, model versioning, A/B testing</development_patterns>
    <operational_patterns>Model monitoring, retraining, performance tracking</operational_patterns>
    <research_patterns>Jupyter notebooks, research documentation, paper implementations</research_patterns>
  </secondary_indicators>
  
  <confidence_modifiers>
    <boost_factors>ML frameworks, model artifacts, experiment tracking, production ML</boost_factors>
    <reduction_factors>Simple analysis, basic statistics, non-ML data processing</reduction_factors>
  </confidence_modifiers>
</machine_learning_domain>
```

## Classification Algorithm

```xml
<classification_algorithm>
  <step_1_analysis>
    <parallel_analysis>
      <technology_stack_analysis>Scan for languages, frameworks, libraries, tools</technology_stack_analysis>
      <project_structure_analysis>Analyze directory patterns, file organization</project_structure_analysis>
      <domain_artifacts_analysis>Identify domain-specific files and configurations</domain_artifacts_analysis>
      <development_patterns_analysis>Detect workflow and methodology indicators</development_patterns_analysis>
      <business_context_analysis>Identify industry and compliance indicators</business_context_analysis>
    </parallel_analysis>
  </step_1_analysis>
  
  <step_2_scoring>
    <domain_scoring>
      <score_calculation>
        For each domain:
        - Technology stack match: 0-100 points × 35% weight
        - Project structure match: 0-100 points × 25% weight
        - Domain artifacts match: 0-100 points × 20% weight
        - Development patterns match: 0-100 points × 15% weight
        - Business context match: 0-100 points × 5% weight
        - Total score: Weighted sum of all dimensions
      </score_calculation>
      
      <confidence_calculation>
        - High confidence: 85%+ with strong indicators across multiple dimensions
        - Medium confidence: 70-84% with clear indicators but some ambiguity
        - Low confidence: 50-69% with weak indicators, manual review recommended
        - Unclear: Below 50% insufficient indicators for classification
      </confidence_calculation>
    </domain_scoring>
  </step_2_scoring>
  
  <step_3_validation>
    <cross_validation>
      <consistency_check>Verify classification consistency across analysis dimensions</consistency_check>
      <conflict_resolution>Resolve conflicts between competing domain indicators</conflict_resolution>
      <edge_case_handling>Handle multi-domain projects and hybrid architectures</edge_case_handling>
    </cross_validation>
  </step_3_validation>
  
  <step_4_recommendation>
    <primary_domain>Domain with highest confidence score above threshold</primary_domain>
    <secondary_domains>Additional domains with significant (>60%) confidence</secondary_domains>
    <customization_recommendations>Specific customizations based on domain characteristics</customization_recommendations>
    <uncertainty_guidance>Guidance for unclear classifications or multi-domain projects</uncertainty_guidance>
  </step_4_recommendation>
</classification_algorithm>
```

## Multi-Domain Classification

```xml
<multi_domain_classification>
  <hybrid_project_handling>
    <primary_secondary_model>
      <primary_domain>Domain with highest confidence score (>80%)</primary_domain>
      <secondary_domains>Additional domains with moderate confidence (60-79%)</secondary_domains>
      <integration_strategy>Combine templates and modules from multiple domains</integration_strategy>
    </primary_secondary_model>
    
    <common_hybrid_patterns>
      <web_mobile>Web development with mobile app components</web_mobile>
      <data_ml>Data engineering with machine learning components</data_ml>
      <fintech_enterprise>Financial technology with enterprise integration</fintech_enterprise>
      <devops_web>Web development with DevOps/platform engineering</devops_web>
      <analytics_engineering>Data analytics with data engineering pipelines</analytics_engineering>
    </common_hybrid_patterns>
  </hybrid_project_handling>
  
  <template_composition>
    <primary_template>Full template from primary domain</primary_template>
    <secondary_modules>Selected modules from secondary domains</secondary_modules>
    <integration_modules>Specialized modules for cross-domain integration</integration_modules>
    <conflict_resolution>Resolution strategies for conflicting configurations</conflict_resolution>
  </template_composition>
</multi_domain_classification>
```

## Usage Interface

```xml
<usage_interface>
  <classification_api>
    <function name="classify_domain">
      <parameters>
        <project_path>string - Path to project root directory</project_path>
        <analysis_depth>enum - shallow|normal|deep analysis level</analysis_depth>
        <confidence_threshold>float - Minimum confidence for classification</confidence_threshold>
        <multi_domain>boolean - Allow multi-domain classification</multi_domain>
      </parameters>
      <returns>
        <primary_domain>Domain classification with confidence score</primary_domain>
        <secondary_domains>Additional domains with confidence scores</secondary_domains>
        <analysis_details>Detailed analysis breakdown by dimension</analysis_details>
        <customization_recommendations>Specific customization suggestions</customization_recommendations>
      </returns>
    </function>
    
    <function name="validate_classification">
      <parameters>
        <classification_result>Domain classification to validate</classification_result>
        <manual_indicators>Optional manual domain indicators</manual_indicators>
      </parameters>
      <returns>
        <validation_result>Validation success/failure with reasons</validation_result>
        <confidence_adjustment>Adjusted confidence based on validation</confidence_adjustment>
        <recommendations>Recommendations for classification improvement</recommendations>
      </returns>
    </function>
  </classification_api>
  
  <interactive_classification>
    <guided_analysis>Step-by-step analysis with user feedback</guided_analysis>
    <manual_override>User can override or adjust classification results</manual_override>
    <uncertainty_resolution>Interactive resolution of unclear classifications</uncertainty_resolution>
    <feedback_integration>Learning from user feedback for future classifications</feedback_integration>
  </interactive_classification>
</usage_interface>
```

## Performance Optimization

```xml
<performance_optimization>
  <parallel_analysis>
    <dimension_parallelization>Analyze all dimensions simultaneously</dimension_parallelization>
    <file_system_optimization>Efficient file system scanning with parallel operations</file_system_optimization>
    <caching_strategy>Cache analysis results for repeated classifications</caching_strategy>
  </parallel_analysis>
  
  <efficiency_targets>
    <classification_time>Complete classification in under 30 seconds</classification_time>
    <accuracy_target>95%+ accuracy for clear domain indicators</accuracy_target>
    <confidence_calibration>Confidence scores accurately reflect classification certainty</confidence_calibration>
  </efficiency_targets>
  
  <optimization_techniques>
    <smart_sampling>Intelligent sampling of large codebases</smart_sampling>
    <pattern_recognition>Pre-trained patterns for common domain indicators</pattern_recognition>
    <incremental_analysis>Incremental analysis for project updates</incremental_analysis>
  </optimization_techniques>
</performance_optimization>
```

## Integration Points

```xml
<integration_points>
  <command_integration>
    <init_command>Domain classification during project initialization</init_command>
    <adapt_command>Domain-specific adaptation based on classification</adapt_command>
    <validate_command>Validation of classification accuracy</validate_command>
  </command_integration>
  
  <module_dependencies>
    <depends_on>
      patterns/codebase-analysis.md for project structure analysis
      patterns/technology-detection.md for technology stack identification
      ../../domain/templates/README.md for domain template management
      ../../system/../../system/quality/domain-validation.md for classification validation
    </depends_on>
    <provides_to>
      ../../domain/adaptation/domain-adaptation.md for adaptation orchestration
      ../../domain/adaptation/template-orchestration.md for template selection
      commands/init.md for initialization domain detection
      commands/adapt.md for adaptation domain requirements
    </provides_to>
  </integration_points>
</integration_points>
```

## Quality Assurance

```xml
<quality_assurance>
  <classification_validation>
    <accuracy_testing>Validate classification accuracy against known projects</accuracy_testing>
    <confidence_calibration>Ensure confidence scores accurately reflect certainty</confidence_calibration>
    <edge_case_testing>Test classification of edge cases and hybrid projects</edge_case_testing>
  </classification_validation>
  
  <continuous_improvement>
    <feedback_learning>Learn from user feedback and corrections</feedback_learning>
    <pattern_updates>Update classification patterns based on new domain trends</pattern_updates>
    <accuracy_monitoring>Monitor classification accuracy over time</accuracy_monitoring>
  </continuous_improvement>
  
  <quality_metrics>
    <accuracy_rate>Percentage of correct classifications</accuracy_rate>
    <confidence_calibration>Correlation between confidence and accuracy</confidence_calibration>
    <processing_time>Time to complete classification</processing_time>
    <user_satisfaction>User satisfaction with classification results</user_satisfaction>
  </quality_metrics>
</quality_assurance>
```

## Error Handling

```xml
<error_handling>
  <classification_errors>
    <insufficient_data>Handle projects with insufficient domain indicators</insufficient_data>
    <conflicting_indicators>Resolve conflicts between competing domain signals</conflicting_indicators>
    <unsupported_domains>Handle projects from unsupported or emerging domains</unsupported_domains>
  </classification_errors>
  
  <recovery_strategies>
    <manual_classification>Fall back to manual domain selection</manual_classification>
    <generic_templates>Use generic templates for unclear classifications</generic_templates>
    <iterative_refinement>Refine classification through iterative user feedback</iterative_refinement>
  </recovery_strategies>
  
  <error_reporting>
    <detailed_diagnostics>Provide detailed error information for troubleshooting</detailed_diagnostics>
    <user_guidance>Guide users through error resolution</user_guidance>
    <feedback_collection>Collect feedback on classification errors for improvement</feedback_collection>
  </error_reporting>
</error_handling>
```

---

**Reference**: This module provides comprehensive domain classification capabilities for intelligent framework customization, supporting automated domain detection with high accuracy and confidence scoring.