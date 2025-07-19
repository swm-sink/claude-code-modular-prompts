# AI/ML Engineering & Research R&D Domain Template

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-11   | stable |

## Domain Overview

AI/ML Engineering & Research R&D domain template provides specialized framework configuration for machine learning systems, AI research implementation, and production ML infrastructure. This template optimizes the Claude Code Framework for MLOps workflows, model development, and AI research to production pipelines.

## Domain Configuration

```xml
<ai_ml_engineering_research_domain>
  <purpose>Advanced AI/ML engineering and research for production-ready ML systems</purpose>
  
  <core_capabilities>
    <ml_system_engineering>Model development, training, deployment, monitoring, and scaling</ml_system_engineering>
    <research_implementation>Research paper implementation, experimental validation, reproducible research</research_implementation>
    <mlops_engineering>CI/CD for ML, model versioning, experiment tracking, automated retraining</mlops_engineering>
    <ai_infrastructure>GPU clusters, distributed training, model serving, edge deployment</ai_infrastructure>
    <responsible_ai>Fairness, explainability, privacy, safety, ethical AI development</responsible_ai>
  </core_capabilities>
  
  <ml_technologies>
    <frameworks>TensorFlow, PyTorch, JAX, Hugging Face, scikit-learn, XGBoost</frameworks>
    <infrastructure>Kubernetes, Docker, Ray, Horovod, CUDA, distributed training</infrastructure>
    <platforms>AWS SageMaker, Azure ML, Google AI Platform, Databricks, MLflow</platforms>
    <deployment>TensorFlow Serving, TorchServe, ONNX Runtime, Triton, KServe</deployment>
  </ml_technologies>
  
  <rd_characteristics>
    <research_focus>Cutting-edge AI research, novel architectures, experimental validation</research_focus>
    <production_engineering>Scalable ML systems, low-latency inference, high availability</production_engineering>
    <experimental_rigor>Reproducible research, statistical validation, hypothesis testing</experimental_rigor>
    <ethical_ai>Responsible AI development, bias detection, fairness metrics</ethical_ai>
  </rd_characteristics>
</ai_ml_engineering_research_domain>
```

## Template Variables

```xml
<template_variables>
  <ml_architecture>
    <deployment_target>{{DEPLOYMENT_TARGET:cloud|edge|hybrid|on_device}}</deployment_target>
    <model_complexity>{{MODEL_COMPLEXITY:traditional_ml|deep_learning|large_language_models|multimodal}}</model_complexity>
    <inference_requirements>{{INFERENCE_REQUIREMENTS:batch|real_time|streaming|interactive}}</inference_requirements>
    <scaling_needs>{{SCALING_NEEDS:single_gpu|multi_gpu|distributed|auto_scaling}}</scaling_needs>
  </ml_architecture>
  
  <research_configuration>
    <research_type>{{RESEARCH_TYPE:applied_research|fundamental_research|product_research|experimental}}</research_type>
    <validation_approach>{{VALIDATION_APPROACH:statistical|experimental|benchmark|peer_review}}</validation_approach>
    <reproducibility_level>{{REPRODUCIBILITY_LEVEL:basic|standard|research_grade|publication_ready}}</reproducibility_level>
    <collaboration_model>{{COLLABORATION_MODEL:individual|team|open_source|academia_industry}}</collaboration_model>
  </research_configuration>
  
  <mlops_setup>
    <experiment_tracking>{{EXPERIMENT_TRACKING:mlflow|wandb|tensorboard|neptune}}</experiment_tracking>
    <model_registry>{{MODEL_REGISTRY:mlflow|sagemaker|azure_ml|custom}}</model_registry>
    <deployment_platform>{{DEPLOYMENT_PLATFORM:kubernetes|sagemaker|azure_ml|gcp_ai_platform}}</deployment_platform>
    <monitoring_solution>{{MONITORING_SOLUTION:evidently|whylogs|fiddler|custom}}</monitoring_solution>
  </mlops_setup>
</template_variables>
```

## Command Customizations

```xml
<command_customizations>
  <task_command>
    <ml_engineering_thinking>
      <data_centric_approach>Focus on data quality, bias detection, and representation</data_centric_approach>
      <reproducibility_first>Ensure reproducible experiments and deterministic training</reproducibility_first>
      <scalability_design>Design for distributed training and high-throughput inference</scalability_design>
      <responsible_ai>Consider fairness, explainability, and ethical implications</responsible_ai>
      <production_readiness>Build for production deployment, monitoring, and maintenance</production_readiness>
    </ml_engineering_thinking>
    
    <quality_gates>
      <model_performance>Meet accuracy, precision, recall, and F1 score targets</model_performance>
      <reproducibility_validation>Consistent results across runs and environments</reproducibility_validation>
      <bias_fairness_testing>Bias detection and fairness metrics validation</bias_fairness_testing>
      <performance_benchmarks>Inference latency and throughput requirements</performance_benchmarks>
      <monitoring_implementation>Model drift detection and performance monitoring</monitoring_implementation>
    </quality_gates>
  </task_command>
  
  <feature_command>
    <ml_feature_planning>
      <research_hypothesis>Define clear research questions and success metrics</research_hypothesis>
      <data_requirements>Identify data sources, quality requirements, and labeling needs</data_requirements>
      <model_architecture>Design appropriate model architecture for the problem</model_architecture>
      <evaluation_strategy>Define comprehensive evaluation metrics and validation approach</evaluation_strategy>
      <deployment_strategy>Plan for model deployment, serving, and monitoring</deployment_strategy>
    </ml_feature_planning>
    
    <development_workflow>
      <experiment_design>Design statistically sound experiments</experiment_design>
      <iterative_development>Rapid prototyping and iterative model improvement</iterative_development>
      <automated_evaluation>Automated model evaluation and comparison</automated_evaluation>
      <reproducibility_engineering>Version control for code, data, and models</reproducibility_engineering>
    </development_workflow>
  </feature_command>
  
  <validate_command>
    <ml_validation>
      <statistical_validation>Statistical significance testing and confidence intervals</statistical_validation>
      <cross_validation>K-fold cross-validation and holdout testing</cross_validation>
      <bias_fairness_assessment>Comprehensive bias and fairness evaluation</bias_fairness_assessment>
      <performance_testing>Inference performance and scalability testing</performance_testing>
      <production_readiness>Production deployment readiness assessment</production_readiness>
    </ml_validation>
  </validate_command>
</command_customizations>
```

## Quality Gates

```xml
<quality_gates>
  <model_performance_standards>
    <accuracy_metrics>Meet target accuracy, precision, recall, and F1 scores</accuracy_metrics>
    <statistical_significance>Results must be statistically significant (p < 0.05)</statistical_significance>
    <cross_validation>Consistent performance across cross-validation folds</cross_validation>
    <benchmark_comparison>Performance comparison against established baselines</benchmark_comparison>
    <generalization_testing>Model performance on unseen test data</generalization_testing>
  </model_performance_standards>
  
  <production_readiness_standards>
    <inference_latency>Meet latency requirements (< 100ms for real-time applications)</inference_latency>
    <throughput>Handle expected inference load with headroom</throughput>
    <resource_utilization>Efficient CPU/GPU utilization and memory usage</resource_utilization>
    <scalability>Auto-scaling based on demand and load</scalability>
    <monitoring_coverage>Comprehensive monitoring and alerting</monitoring_coverage>
  </production_readiness_standards>
  
  <responsible_ai_standards>
    <bias_detection>Systematic bias detection across protected attributes</bias_detection>
    <fairness_metrics>Fairness metrics validation (demographic parity, equalized odds)</fairness_metrics>
    <explainability>Model interpretability and explanation capabilities</explainability>
    <privacy_protection>Data privacy and model privacy protection</privacy_protection>
    <safety_validation>Safety testing and failure mode analysis</safety_validation>
  </responsible_ai_standards>
</quality_gates>
```

## ML Engineering Patterns

```xml
<ml_engineering_patterns>
  <model_development_lifecycle>
    <data_preparation>Data collection, cleaning, labeling, and feature engineering</data_preparation>
    <model_training>Training pipeline, hyperparameter tuning, experiment tracking</model_training>
    <model_evaluation>Validation metrics, testing, bias assessment</model_evaluation>
    <model_deployment>Serving infrastructure, A/B testing, canary deployment</model_deployment>
    <model_monitoring>Performance monitoring, drift detection, retraining triggers</model_monitoring>
  </model_development_lifecycle>
  
  <distributed_training_patterns>
    <data_parallelism>Distribute training data across multiple GPUs/nodes</data_parallelism>
    <model_parallelism>Distribute model parameters across multiple devices</model_parallelism>
    <pipeline_parallelism>Pipeline stages across multiple devices</pipeline_parallelism>
    <gradient_accumulation>Accumulate gradients for large effective batch sizes</gradient_accumulation>
    <mixed_precision>Mixed precision training for efficiency</mixed_precision>
  </distributed_training_patterns>
  
  <model_serving_patterns>
    <batch_inference>Batch processing for high-throughput scenarios</batch_inference>
    <real_time_inference>Low-latency serving for interactive applications</real_time_inference>
    <streaming_inference>Continuous inference on streaming data</streaming_inference>
    <edge_deployment>On-device inference for mobile and IoT</edge_deployment>
    <model_ensembling>Ensemble methods for improved performance</model_ensembling>
  </model_serving_patterns>
</ml_engineering_patterns>
```

## Technology Stack

```xml
<technology_stack>
  <ml_frameworks>
    <deep_learning>TensorFlow, PyTorch, JAX, Flax, Keras</deep_learning>
    <traditional_ml>scikit-learn, XGBoost, LightGBM, CatBoost</traditional_ml>
    <specialized>Hugging Face Transformers, OpenAI GPT, Stable Diffusion</specialized>
    <reinforcement_learning>Ray RLlib, Stable Baselines3, OpenAI Gym</reinforcement_learning>
  </ml_frameworks>
  
  <mlops_platforms>
    <experiment_tracking>MLflow, Weights & Biases, Neptune, TensorBoard</experiment_tracking>
    <model_registry>MLflow Model Registry, AWS SageMaker, Azure ML</model_registry>
    <pipeline_orchestration>Kubeflow, Apache Airflow, MLflow Pipelines</pipeline_orchestration>
    <feature_stores>Feast, Tecton, AWS Feature Store, Databricks Feature Store</feature_stores>
  </mlops_platforms>
  
  <infrastructure>
    <compute_platforms>AWS SageMaker, Azure ML, Google AI Platform, Databricks</compute_platforms>
    <container_orchestration>Kubernetes, Docker, KServe, Seldon Core</container_orchestration>
    <distributed_training>Ray, Horovod, DeepSpeed, FairScale</distributed_training>
    <model_serving>TensorFlow Serving, TorchServe, ONNX Runtime, Triton</model_serving>
  </infrastructure>
  
  <data_management>
    <data_versioning>DVC, Pachyderm, Delta Lake, Git LFS</data_versioning>
    <data_labeling>Label Studio, Labelbox, Snorkel, Amazon SageMaker Ground Truth</data_labeling>
    <data_processing>Apache Spark, Dask, Ray, Pandas, Polars</data_processing>
    <data_storage>S3, Azure Blob, Google Cloud Storage, HDFS</data_storage>
  </data_management>
</technology_stack>
```

## Best Practices

```xml
<best_practices>
  <research_engineering>
    <reproducible_research>Version control for code, data, models, and environments</reproducible_research>
    <experiment_design>Statistical rigor in experimental design and validation</experiment_design>
    <documentation>Comprehensive documentation of methods, results, and insights</documentation>
    <peer_review>Code reviews and research validation by peers</peer_review>
    <open_science>Open source code and reproducible research practices</open_science>
  </research_engineering>
  
  <production_ml>
    <model_versioning>Systematic model versioning and lineage tracking</model_versioning>
    <automated_testing>Unit tests, integration tests, and model validation tests</automated_testing>
    <continuous_integration>CI/CD pipelines for ML model development</continuous_integration>
    <monitoring_observability>Comprehensive monitoring of model performance and data drift</monitoring_observability>
    <gradual_rollout>Canary deployments and A/B testing for model releases</gradual_rollout>
  </production_ml>
  
  <responsible_ai>
    <bias_mitigation>Systematic bias detection and mitigation strategies</bias_mitigation>
    <fairness_assessment>Regular fairness audits and metric evaluation</fairness_assessment>
    <explainable_ai>Model interpretability and explanation capabilities</explainable_ai>
    <privacy_preservation>Differential privacy and federated learning</privacy_preservation>
    <safety_first>Safety testing and failure mode analysis</safety_first>
  </responsible_ai>
</best_practices>
```

## Research & Innovation Focus

```xml
<research_innovation>
  <emerging_technologies>
    <foundation_models>Large language models, multimodal models, emergent capabilities</foundation_models>
    <edge_ai>On-device AI, model compression, quantization, pruning</edge_ai>
    <federated_learning>Distributed learning, privacy-preserving ML</federated_learning>
    <quantum_ml>Quantum machine learning algorithms and applications</quantum_ml>
  </emerging_technologies>
  
  <ai_research_frontiers>
    <multimodal_ai>Vision-language models, audio-visual understanding</multimodal_ai>
    <continual_learning>Lifelong learning, catastrophic forgetting mitigation</continual_learning>
    <few_shot_learning>Meta-learning, prompt engineering, in-context learning</few_shot_learning>
    <neuromorphic_computing>Spiking neural networks, brain-inspired computing</neuromorphic_computing>
  </ai_research_frontiers>
  
  <ml_systems_innovation>
    <automated_ml>AutoML, neural architecture search, hyperparameter optimization</automated_ml>
    <efficient_training>Gradient compression, mixed precision, model parallelism</efficient_training>
    <model_optimization>Quantization, pruning, knowledge distillation</model_optimization>
    <inference_acceleration>Hardware acceleration, specialized chips, edge deployment</inference_acceleration>
  </ml_systems_innovation>
</research_innovation>
```

## Usage Instructions

```xml
<usage_instructions>
  <initialization>
    <setup_command>Use `/init` command with ai-ml-engineering-research template</setup_command>
    <environment_setup>Configure ML development environment and infrastructure</environment_setup>
    <data_preparation>Prepare datasets, establish data pipelines, and quality checks</data_preparation>
    <experiment_tracking>Set up experiment tracking and model registry</experiment_tracking>
  </initialization>
  
  <research_workflow>
    <problem_definition>Define research questions and success metrics</problem_definition>
    <literature_review>Review existing research and establish baselines</literature_review>
    <experiment_design>Design statistically sound experiments</experiment_design>
    <implementation_validation>Implement, validate, and iterate on solutions</implementation_validation>
  </research_workflow>
  
  <production_deployment>
    <model_optimization>Optimize models for production deployment</model_optimization>
    <infrastructure_setup>Set up serving infrastructure and monitoring</infrastructure_setup>
    <deployment_validation>Validate deployment through A/B testing</deployment_validation>
    <continuous_monitoring>Monitor model performance and data drift</continuous_monitoring>
  </production_deployment>
</usage_instructions>
```

**Usage**: Apply this template for AI/ML engineering and research projects focused on building production-ready ML systems, conducting reproducible research, and implementing cutting-edge AI technologies. Optimized for ML engineers and researchers working on scalable AI systems and responsible AI development.