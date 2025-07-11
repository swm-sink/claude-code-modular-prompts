# Data Analytics Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

Data Analytics domain template provides specialized framework configuration for data science, statistical analysis, and business intelligence projects. This template optimizes the Claude Code Framework for data-driven workflows, exploratory analysis, and insight generation.

## Domain Configuration

```xml
<data_analytics_domain>
  <purpose>Specialized framework configuration for data analytics and data science projects</purpose>
  
  <analysis_types>
    <exploratory_analysis>Exploratory data analysis and hypothesis generation</exploratory_analysis>
    <statistical_analysis>Statistical modeling and hypothesis testing</statistical_analysis>
    <predictive_modeling>Machine learning and predictive analytics</predictive_modeling>
    <business_intelligence>Business reporting and dashboard creation</business_intelligence>
  </analysis_types>
  
  <development_characteristics>
    <experiment_driven>Hypothesis-driven analysis and experimentation</experiment_driven>
    <iterative_process>Iterative analysis and model refinement</iterative_process>
    <visualization_heavy>Data visualization and storytelling</visualization_heavy>
    <statistical_rigor>Statistical validation and significance testing</statistical_rigor>
    <reproducible_research>Reproducible and documented analysis</reproducible_research>
  </development_characteristics>
</data_analytics_domain>
```

## Template Variables

```xml
<template_variables>
  <analysis_configuration>
    <primary_language>{{PRIMARY_LANGUAGE:python|r|sql|scala}}</primary_language>
    <analysis_type>{{ANALYSIS_TYPE:exploratory|statistical|predictive|business_intelligence}}</analysis_type>
    <data_sources>{{DATA_SOURCES:database|files|apis|streaming}}</data_sources>
    <visualization_tools>{{VISUALIZATION_TOOLS:matplotlib|plotly|ggplot2|tableau|power_bi}}</visualization_tools>
  </analysis_configuration>
  
  <project_configuration>
    <project_name>{{PROJECT_NAME:string}}</project_name>
    <domain_area>{{DOMAIN_AREA:finance|healthcare|marketing|operations|research}}</domain_area>
    <analysis_scope>{{ANALYSIS_SCOPE:adhoc|recurring|realtime|batch}}</analysis_scope>
    <stakeholder_level>{{STAKEHOLDER_LEVEL:technical|business|executive}}</stakeholder_level>
  </project_configuration>
  
  <technical_settings>
    <data_processing>{{DATA_PROCESSING:pandas|spark|dask|polars}}</data_processing>
    <statistical_framework>{{STATISTICAL_FRAMEWORK:scipy|statsmodels|scikit_learn|tidyverse}}</statistical_framework>
    <notebook_environment>{{NOTEBOOK_ENVIRONMENT:jupyter|rstudio|databricks|colab}}</notebook_environment>
    <deployment_target>{{DEPLOYMENT_TARGET:local|cloud|production|dashboard}}</deployment_target>
  </technical_settings>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <analytics_specific_thinking>
      <data_quality_assessment>Validate data quality and completeness</data_quality_assessment>
      <statistical_appropriateness>Ensure statistical methods are appropriate for data</statistical_appropriateness>
      <bias_consideration>Consider potential biases in data and analysis</bias_consideration>
      <reproducibility_check>Ensure analysis is reproducible and documented</reproducibility_check>
    </analytics_specific_thinking>
    
    <quality_gates>
      <data_validation>Comprehensive data quality validation</data_validation>
      <statistical_testing>Statistical significance and power analysis</statistical_testing>
      <visualization_review>Visualization clarity and accuracy validation</visualization_review>
      <reproducibility_test>Reproducibility verification and documentation</reproducibility_test>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <analytics_feature_planning>
      <hypothesis_definition>Define clear hypotheses and success metrics</hypothesis_definition>
      <experimental_design>Design robust experimental framework</experimental_design>
      <data_requirements>Identify and validate required data sources</data_requirements>
      <stakeholder_alignment>Ensure alignment with business objectives</stakeholder_alignment>
    </analytics_feature_planning>
    
    <analysis_workflow>
      <data_collection>Systematic data collection and validation</data_collection>
      <exploratory_analysis>Comprehensive exploratory data analysis</exploratory_analysis>
      <statistical_modeling>Rigorous statistical modeling and testing</statistical_modeling>
      <insight_generation>Clear insight generation and validation</insight_generation>
    </analysis_workflow>
  </feature_command>
  
  <validate_command>
    <analytics_validation>
      <statistical_validation>Validate statistical assumptions and methods</statistical_validation>
      <data_quality_validation>Comprehensive data quality assessment</data_quality_validation>
      <reproducibility_validation>Verify analysis reproducibility</reproducibility_validation>
      <business_validation>Validate insights against business context</business_validation>
    </analytics_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates Configuration

```xml
<quality_gates_configuration>
  <data_quality>
    <completeness_validation>
      <rule>Data completeness meets minimum requirements for analysis</rule>
      <validation>Automated data completeness assessment</validation>
      <threshold>95% completeness for critical variables</threshold>
    </completeness_validation>
    
    <accuracy_validation>
      <rule>Data accuracy verified through multiple validation methods</rule>
      <validation>Cross-validation with authoritative sources</validation>
      <threshold>99% accuracy for key business metrics</threshold>
    </accuracy_validation>
    
    <consistency_validation>
      <rule>Data consistency maintained across all sources</rule>
      <validation>Automated consistency checks and reconciliation</validation>
      <threshold>Zero critical consistency violations</threshold>
    </consistency_validation>
  </data_quality>
  
  <statistical_quality>
    <statistical_significance>
      <rule>Statistical tests achieve appropriate significance levels</rule>
      <validation>Automated statistical significance testing</validation>
      <threshold>p-value < 0.05 for hypothesis testing</threshold>
    </statistical_significance>
    
    <effect_size_validation>
      <rule>Effect sizes are practically meaningful</rule>
      <validation>Effect size calculation and interpretation</validation>
      <threshold>Cohen's d > 0.5 for meaningful differences</threshold>
    </effect_size_validation>
    
    <power_analysis>
      <rule>Statistical power adequate for detecting meaningful effects</rule>
      <validation>Power analysis for all statistical tests</validation>
      <threshold>Statistical power > 0.8</threshold>
    </power_analysis>
  </statistical_quality>
  
  <reproducibility_quality>
    <code_reproducibility>
      <rule>All analysis code is fully reproducible</rule>
      <validation>Automated reproducibility testing</validation>
      <threshold>100% reproducible results</threshold>
    </code_reproducibility>
    
    <documentation_completeness>
      <rule>Analysis methodology fully documented</rule>
      <validation>Documentation completeness assessment</validation>
      <threshold>100% methodology documentation</threshold>
    </documentation_completeness>
    
    <version_control>
      <rule>All analysis artifacts under version control</rule>
      <validation>Version control compliance validation</validation>
      <threshold>100% version control coverage</threshold>
    </version_control>
  </reproducibility_quality>
</quality_gates_configuration>
```

## Module Selection

```xml
<module_selection>
  <core_modules>
    <data_analytics>
      <data_processing>Efficient data processing and manipulation</data_processing>
      <statistical_analysis>Comprehensive statistical analysis toolkit</statistical_analysis>
      <visualization_framework>Advanced data visualization capabilities</visualization_framework>
      <experiment_design>Robust experimental design and analysis</experiment_design>
    </data_analytics>
    
    <domain_specific>
      <exploratory_analysis condition="{{ANALYSIS_TYPE:exploratory}}">
        <eda_patterns>Exploratory data analysis patterns and techniques</eda_patterns>
        <hypothesis_generation>Systematic hypothesis generation methods</hypothesis_generation>
        <data_profiling>Comprehensive data profiling and characterization</data_profiling>
      </exploratory_analysis>
      
      <statistical_modeling condition="{{ANALYSIS_TYPE:statistical}}">
        <statistical_methods>Advanced statistical modeling techniques</statistical_methods>
        <model_validation>Statistical model validation and diagnostics</model_validation>
        <significance_testing>Comprehensive significance testing framework</significance_testing>
      </statistical_modeling>
      
      <predictive_analytics condition="{{ANALYSIS_TYPE:predictive}}">
        <ml_modeling>Machine learning model development</ml_modeling>
        <model_evaluation>Model performance evaluation and comparison</model_evaluation>
        <feature_engineering>Advanced feature engineering techniques</feature_engineering>
      </predictive_analytics>
    </domain_specific>
  </core_modules>
  
  <quality_modules>
    <data_validation>
      <quality_assessment>Comprehensive data quality assessment</quality_assessment>
      <anomaly_detection>Automated anomaly detection and handling</anomaly_detection>
      <data_profiling>Detailed data profiling and characterization</data_profiling>
      <validation_reporting>Data validation reporting and documentation</validation_reporting>
    </data_validation>
    
    <statistical_validation>
      <assumption_testing>Statistical assumption validation</assumption_testing>
      <power_analysis>Statistical power analysis and sample size calculation</power_analysis>
      <effect_size_analysis>Effect size calculation and interpretation</effect_size_analysis>
      <multiple_comparisons>Multiple comparison correction methods</multiple_comparisons>
    </statistical_validation>
  </quality_modules>
  
  <development_modules>
    <notebook_development>
      <notebook_standards>Notebook development standards and best practices</notebook_standards>
      <code_organization>Code organization and modularization</code_organization>
      <documentation_standards>Analysis documentation standards</documentation_standards>
      <reproducibility_framework>Reproducibility and version control</reproducibility_framework>
    </notebook_development>
    
    <visualization_development>
      <chart_library>Comprehensive chart and visualization library</chart_library>
      <interactive_visualizations>Interactive visualization development</interactive_visualizations>
      <dashboard_creation>Dashboard and reporting development</dashboard_creation>
      <storytelling_framework>Data storytelling and presentation</storytelling_framework>
    </visualization_development>
  </development_modules>
</module_selection>
```

## Framework Integration

```xml
<framework_integration>
  <optimal_frameworks>
    <primary_framework>SPARK - Innovation and knowledge creation for research</primary_framework>
    <secondary_framework>CLEAR - Clarity and precision for methodology</secondary_framework>
    <specialized_framework>LEAP - Learning and exploration for discovery</specialized_framework>
  </optimal_frameworks>
  
  <framework_customization>
    <spark_analytics_optimization>
      <situation>Current data landscape and business context</situation>
      <problem>Specific analytical questions and hypotheses</problem>
      <action>Systematic analysis approach with statistical rigor</action>
      <result>Actionable insights and validated findings</result>
      <knowledge>Transferable analytical methods and domain insights</knowledge>
    </spark_analytics_optimization>
    
    <clear_analytics_optimization>
      <context>Data sources, business context, and analytical constraints</context>
      <logic>Statistical methodology and analytical reasoning</logic>
      <expectation>Clear success criteria and validation standards</expectation>
      <action>Systematic analytical procedures and methods</action>
      <result>Validated insights with statistical confidence</result>
    </clear_analytics_optimization>
  </framework_customization>
</framework_integration>
```

## Development Workflows

```xml
<development_workflows>
  <analytics_development_cycle>
    <problem_definition>
      <step>Define business problem and analytical objectives</step>
      <step>Establish success metrics and validation criteria</step>
      <step>Identify stakeholders and communication requirements</step>
      <step>Define project scope and timeline</step>
    </problem_definition>
    
    <data_acquisition>
      <step>Identify and access required data sources</step>
      <step>Perform initial data quality assessment</step>
      <step>Establish data governance and privacy compliance</step>
      <step>Create data processing and cleaning pipelines</step>
    </data_acquisition>
    
    <exploratory_analysis>
      <step>Comprehensive exploratory data analysis</step>
      <step>Statistical profiling and characterization</step>
      <step>Hypothesis generation and refinement</step>
      <step>Initial visualization and pattern identification</step>
    </exploratory_analysis>
    
    <analysis_execution>
      <step>Statistical modeling and hypothesis testing</step>
      <step>Model validation and diagnostics</step>
      <step>Sensitivity analysis and robustness testing</step>
      <step>Results interpretation and insight generation</step>
    </analysis_execution>
    
    <validation_and_deployment>
      <step>Independent validation of results</step>
      <step>Peer review and stakeholder validation</step>
      <step>Documentation and reproducibility verification</step>
      <step>Deployment and monitoring setup</step>
    </validation_and_deployment>
  </analytics_development_cycle>
  
  <specialized_workflows>
    <experimental_design_workflow>
      <hypothesis_formulation>Formulate clear, testable hypotheses</hypothesis_formulation>
      <experimental_design>Design robust experimental framework</experimental_design>
      <power_analysis>Perform statistical power analysis</power_analysis>
      <data_collection>Systematic data collection execution</data_collection>
      <statistical_analysis>Rigorous statistical analysis</statistical_analysis>
    </experimental_design_workflow>
    
    <predictive_modeling_workflow>
      <feature_engineering>Advanced feature engineering and selection</feature_engineering>
      <model_development>Model development and hyperparameter tuning</model_development>
      <model_validation>Cross-validation and performance assessment</model_validation>
      <model_interpretation>Model interpretation and explainability</model_interpretation>
      <deployment_preparation>Model deployment and monitoring preparation</deployment_preparation>
    </predictive_modeling_workflow>
  </specialized_workflows>
</development_workflows>
```

## Performance Optimization

```xml
<performance_optimization>
  <data_processing_optimization>
    <efficient_data_structures>
      <vectorization>Leverage vectorized operations for performance</vectorization>
      <memory_optimization>Optimize memory usage for large datasets</memory_optimization>
      <parallel_processing>Utilize parallel processing for computations</parallel_processing>
      <lazy_evaluation>Implement lazy evaluation strategies</lazy_evaluation>
    </efficient_data_structures>
    
    <algorithm_optimization>
      <computational_complexity>Optimize algorithms for computational efficiency</computational_complexity>
      <approximation_methods>Use approximation methods for large-scale analysis</approximation_methods>
      <caching_strategies>Implement intelligent caching for repeated operations</caching_strategies>
      <incremental_processing>Enable incremental processing for large datasets</incremental_processing>
    </algorithm_optimization>
  </data_processing_optimization>
  
  <statistical_optimization>
    <sampling_strategies>
      <statistical_sampling>Implement statistically sound sampling methods</statistical_sampling>
      <stratified_sampling>Use stratified sampling for representative samples</stratified_sampling>
      <bootstrap_methods>Leverage bootstrap methods for inference</bootstrap_methods>
      <monte_carlo_methods>Implement Monte Carlo methods for complex problems</monte_carlo_methods>
    </sampling_strategies>
    
    <computational_statistics>
      <numerical_optimization>Optimize numerical computations for accuracy</numerical_optimization>
      <iterative_algorithms>Implement efficient iterative algorithms</iterative_algorithms>
      <sparse_methods>Utilize sparse methods for high-dimensional data</sparse_methods>
      <distributed_computing>Leverage distributed computing for scalability</distributed_computing>
    </computational_statistics>
  </statistical_optimization>
</performance_optimization>
```

## Testing Strategy

```xml
<testing_strategy>
  <analytics_testing_pyramid>
    <unit_tests>
      <statistical_functions>Test statistical functions and calculations</statistical_functions>
      <data_processing>Test data processing and transformation functions</data_processing>
      <utility_functions>Test utility and helper functions</utility_functions>
      <coverage_target>90% code coverage for analytical functions</coverage_target>
    </unit_tests>
    
    <integration_tests>
      <data_pipeline_tests>Test end-to-end data processing pipelines</data_pipeline_tests>
      <model_integration_tests>Test model integration and prediction pipelines</model_integration_tests>
      <visualization_tests>Test visualization generation and accuracy</visualization_tests>
      <coverage_target>80% coverage for integration workflows</coverage_target>
    </integration_tests>
    
    <statistical_tests>
      <assumption_validation>Test statistical assumptions and prerequisites</assumption_validation>
      <reproducibility_tests>Test analysis reproducibility and consistency</reproducibility_tests>
      <sensitivity_analysis>Test sensitivity to parameter changes</sensitivity_analysis>
      <coverage_target>100% coverage for statistical validations</coverage_target>
    </statistical_tests>
    
    <data_quality_tests>
      <data_validation_tests>Test data quality and validation rules</data_validation_tests>
      <anomaly_detection_tests>Test anomaly detection and handling</anomaly_detection_tests>
      <schema_validation_tests>Test data schema and structure validation</schema_validation_tests>
      <coverage_target>100% coverage for data quality checks</coverage_target>
    </data_quality_tests>
  </analytics_testing_pyramid>
  
  <validation_testing_strategy>
    <cross_validation>
      <k_fold_validation>Implement k-fold cross-validation for models</k_fold_validation>
      <time_series_validation>Use time series validation for temporal data</time_series_validation>
      <stratified_validation>Implement stratified validation for imbalanced data</stratified_validation>
    </cross_validation>
    
    <statistical_validation>
      <hypothesis_testing>Validate statistical hypotheses and assumptions</hypothesis_testing>
      <power_analysis>Validate statistical power and sample size</power_analysis>
      <effect_size_validation>Validate effect sizes and practical significance</effect_size_validation>
    </statistical_validation>
  </validation_testing_strategy>
</testing_strategy>
```

## Deployment Configuration

```xml
<deployment_configuration>
  <analysis_deployment>
    <notebook_deployment>
      <jupyter_deployment>Deploy interactive Jupyter notebooks</jupyter_deployment>
      <notebook_scheduling>Schedule automated notebook execution</notebook_scheduling>
      <notebook_monitoring>Monitor notebook execution and performance</notebook_monitoring>
      <version_control>Version control for notebook deployments</version_control>
    </notebook_deployment>
    
    <dashboard_deployment>
      <interactive_dashboards>Deploy interactive analytical dashboards</interactive_dashboards>
      <automated_reporting>Set up automated report generation</automated_reporting>
      <real_time_updates>Enable real-time data updates</real_time_updates>
      <user_access_control>Implement user access control and permissions</user_access_control>
    </dashboard_deployment>
  </analysis_deployment>
  
  <model_deployment>
    <batch_scoring>
      <batch_processing>Deploy batch scoring pipelines</batch_processing>
      <scheduled_execution>Schedule regular batch processing</scheduled_execution>
      <result_storage>Store and manage batch scoring results</result_storage>
      <monitoring_alerts>Set up monitoring and alerting</monitoring_alerts>
    </batch_scoring>
    
    <real_time_scoring>
      <api_deployment>Deploy real-time scoring APIs</api_deployment>
      <performance_optimization>Optimize for low-latency scoring</performance_optimization>
      <scalability_planning>Plan for horizontal scalability</scalability_planning>
      <monitoring_dashboard>Implement real-time monitoring</monitoring_dashboard>
    </real_time_scoring>
  </model_deployment>
</deployment_configuration>
```

## Documentation Templates

```xml
<documentation_templates>
  <analytics_documentation>
    <methodology_documentation>
      <analytical_approach>Document analytical methodology and rationale</analytical_approach>
      <statistical_methods>Document statistical methods and assumptions</statistical_methods>
      <data_sources>Document data sources and quality assessment</data_sources>
      <validation_procedures>Document validation and verification procedures</validation_procedures>
    </methodology_documentation>
    
    <results_documentation>
      <findings_summary>Summarize key findings and insights</findings_summary>
      <statistical_results>Document statistical results and significance</statistical_results>
      <visualization_catalog>Catalog all visualizations and interpretations</visualization_catalog>
      <recommendations>Document actionable recommendations</recommendations>
    </results_documentation>
    
    <technical_documentation>
      <code_documentation>Document code structure and functions</code_documentation>
      <data_pipeline_docs>Document data processing pipelines</data_pipeline_docs>
      <model_documentation>Document model development and evaluation</model_documentation>
      <deployment_documentation>Document deployment and monitoring procedures</deployment_documentation>
    </technical_documentation>
  </analytics_documentation>
  
  <stakeholder_documentation>
    <executive_summary>
      <business_impact>Summarize business impact and value</business_impact>
      <key_insights>Highlight key insights and findings</key_insights>
      <recommendations>Present actionable recommendations</recommendations>
      <next_steps>Outline next steps and follow-up actions</next_steps>
    </executive_summary>
    
    <technical_stakeholder_docs>
      <implementation_guide>Guide for implementing recommendations</implementation_guide>
      <technical_specifications>Technical specifications and requirements</technical_specifications>
      <integration_procedures>Integration procedures and considerations</integration_procedures>
      <monitoring_guidelines>Monitoring and maintenance guidelines</monitoring_guidelines>
    </technical_stakeholder_docs>
  </stakeholder_documentation>
</documentation_templates>
```

## Success Metrics

```xml
<success_metrics>
  <analytical_quality_metrics>
    <statistical_rigor>Statistical significance and power achievement</statistical_rigor>
    <reproducibility_score>Analysis reproducibility and consistency</reproducibility_score>
    <data_quality_score>Data quality and completeness metrics</data_quality_score>
    <methodology_compliance>Adherence to analytical best practices</methodology_compliance>
  </analytical_quality_metrics>
  
  <business_impact_metrics>
    <insight_actionability>Percentage of insights leading to actions</insight_actionability>
    <business_value_generated>Quantified business value from insights</business_value_generated>
    <stakeholder_satisfaction>Stakeholder satisfaction with analysis</stakeholder_satisfaction>
    <decision_support_effectiveness>Effectiveness in supporting decisions</decision_support_effectiveness>
  </business_impact_metrics>
  
  <technical_performance_metrics>
    <processing_efficiency>Data processing speed and efficiency</processing_efficiency>
    <model_performance>Model accuracy and performance metrics</model_performance>
    <deployment_success>Successful deployment and adoption rates</deployment_success>
    <system_reliability>System uptime and reliability metrics</system_reliability>
  </technical_performance_metrics>
</success_metrics>
```

---

**Reference**: This template provides comprehensive data analytics domain configuration, enabling specialized framework adaptation for data science, statistical analysis, and business intelligence projects with optimized workflows, quality gates, and validation procedures.