<prompt_component>
  <step name="OPRO Optimization Framework">
    <description>
Google DeepMind's OPRO (Optimization by Prompting) framework that uses Large Language Models as optimizers for automatic prompt engineering. Leverages natural language to describe optimization problems and iteratively improve prompt performance through meta-optimization.
    </description>
  </step>

  <opro_framework>
    <optimization_pipeline>
      <!-- OPRO meta-optimization process -->
      <prompt_optimization>

```xml
<command>prompt-opro</command>
<params>
  <!-- Core OPRO Configuration -->
  <optimizer_llm>gpt-4-turbo</optimizer_llm>
  <scorer_llm>gpt-4</scorer_llm>
  <optimization_objective>accuracy</optimization_objective>
  <max_iterations>50</max_iterations>
  
  <!-- Meta-Prompt Structure -->
  <meta_prompt>
    <instruction_template>Generate a new instruction that achieves higher accuracy</instruction_template>
    <solution_score_pairs>20</solution_score_pairs>
    <problem_description>detailed_task_specification</problem_description>
    <output_format>structured_prompt_generation</output_format>
  </meta_prompt>
  
  <!-- Training Configuration -->
  <training_set>
    <dataset>training_examples.json</dataset>
    <subset_size>100</subset_size>
    <sampling>random</sampling>
    <validation_split>0.2</validation_split>
  </training_set>
  
  <!-- Optimization Strategy -->
  <strategy>
    <temperature>1.0</temperature>
    <num_generated_instructions>8</num_generated_instructions>
    <selection_method>top_k</selection_method>
    <convergence_threshold>0.95</convergence_threshold>
  </strategy>
  
  <!-- Advanced Settings -->
  <optimization>
    <step_size>adaptive</step_size>
    <momentum>0.9</momentum>
    <exploration_factor>0.2</exploration_factor>
    <early_stopping>patience_5</early_stopping>
  </optimization>
</params>
```

## Implementation

### OPRO Framework Architecture

#### 1. Meta-Prompt Construction
```yaml
meta_prompt_components:
  optimization_task_description:
    - problem_definition: "Find instructions that maximize task accuracy"
    - objective_function: "accuracy on validation dataset"
    - constraints: "instruction_length_limit, clarity_requirements"
    - success_criteria: "performance_improvement_threshold"
  
  solution_score_history:
    - format: "(instruction, score) pairs"
    - ordering: "ascending by score"
    - count: "top_20_historical_solutions"
    - purpose: "pattern_learning_and_guidance"
  
  task_examples:
    - count: 3
    - selection: "representative_diverse_cases"
    - format: "input_output_pairs"
    - purpose: "task_context_and_understanding"
  
  meta_instructions:
    - generation_guidance: "create_better_instructions"
    - format_specification: "clear_precise_actionable"
    - diversity_requirement: "explore_different_approaches"
    - improvement_focus: "build_on_successful_patterns"
```

#### 2. Optimization Loop
```yaml
opro_optimization_process:
  initialization:
    - baseline_instruction: "simple_starting_prompt"
    - evaluation_dataset: "held_out_validation_set"
    - performance_tracking: "score_history_initialization"
    - meta_prompt_setup: "template_and_context_preparation"
  
  iteration_cycle:
    - instruction_generation:
        - meta_prompt_construction: "include_history_and_context"
        - llm_prompting: "generate_candidate_instructions"
        - candidate_filtering: "basic_quality_checks"
        - diversity_enforcement: "avoid_repetition_and_stagnation"
    
    - instruction_evaluation:
        - scorer_llm_execution: "run_on_validation_set"
        - metric_computation: "accuracy_f1_custom_metrics"
        - performance_ranking: "order_by_effectiveness"
        - statistical_significance: "confidence_interval_testing"
    
    - history_update:
        - solution_recording: "add_new_instruction_score_pairs"
        - meta_prompt_refresh: "update_with_best_performers"
        - pattern_analysis: "identify_successful_characteristics"
        - convergence_check: "evaluate_improvement_plateau"
```

#### 3. Natural Language Optimization
```markdown
**LLM as Optimizer Methodology:**
- The LLM analyzes the optimization trajectory (previous solutions and scores)
- It identifies patterns in successful instructions vs. failed attempts
- It generates new candidate instructions that build on successful patterns
- It uses natural language understanding to reason about what makes instructions effective
- It applies this reasoning to propose improved instructions
```

### Advanced OPRO Features

#### Multi-Objective Optimization
```yaml
multi_objective_setup:
  primary_objective:
    name: "accuracy"
    weight: 0.7
    target: "maximize"
    measurement: "validation_set_performance"
  
  secondary_objectives:
    efficiency:
      weight: 0.2
      target: "minimize"
      measurement: "token_count_per_response"
    
    clarity:
      weight: 0.1
      target: "maximize"
      measurement: "human_readability_score"
  
  aggregation_method: "weighted_sum"
  pareto_frontier: "track_trade_offs"
```

#### Adaptive Optimization Strategies
```yaml
adaptive_mechanisms:
  learning_rate_adaptation:
    - high_improvement: "maintain_current_strategy"
    - plateau_detection: "increase_exploration"
    - oscillation_pattern: "reduce_step_size"
    - convergence_approach: "fine_tune_adjustments"
  
  exploration_exploitation_balance:
    - early_phase: "high_exploration_diverse_candidates"
    - middle_phase: "balanced_exploration_exploitation"
    - late_phase: "focused_exploitation_refinement"
    - adaptive_switching: "performance_based_transitions"
  
  meta_prompt_evolution:
    - instruction_refinement: "improve_generation_guidance"
    - example_curation: "select_most_informative_cases"
    - context_optimization: "enhance_task_understanding"
    - format_adaptation: "adjust_for_llm_preferences"
```

## Use Cases

### 1. Question Answering Optimization
```xml
<scenario>
  <task>Multi-hop question answering</task>
  <objective>Improve reasoning accuracy</objective>
  <baseline_instruction>"Answer the question based on the given context"</baseline_instruction>
  <optimized_result>"Carefully analyze the context, identify key facts, trace logical connections between information, and provide a step-by-step reasoning path to the answer"</optimized_result>
  <improvement>+15% accuracy gain</improvement>
</scenario>
```

### 2. Code Generation Enhancement
```xml
<scenario>
  <task>Python function generation</task>
  <objective>Increase code correctness and efficiency</objective>
  <baseline_instruction>"Write a Python function"</baseline_instruction>
  <optimized_result>"Generate a well-documented Python function with clear variable names, efficient algorithms, proper error handling, and comprehensive docstring including examples"</optimized_result>
  <improvement>+22% functional correctness</improvement>
</scenario>
```

### 3. Creative Writing Optimization
```xml
<scenario>
  <task>Story generation</task>
  <objective>Enhance narrative quality and engagement</objective>
  <baseline_instruction>"Write a short story"</baseline_instruction>
  <optimized_result>"Craft an engaging short story with vivid character development, compelling plot progression, rich sensory details, and emotional resonance that draws readers into the narrative"</optimized_result>
  <improvement>+28% human preference scores</improvement>
</scenario>
```

## Advanced Optimization Techniques

### Random Search with LLM Guidance
```markdown
**Enhanced Random Search:**
- Traditional random search generates instructions randomly
- OPRO guides this randomness using LLM understanding
- The LLM suggests "smart" variations rather than purely random ones
- This combines systematic exploration with intelligent guidance
```

### Evolutionary Optimization
```yaml
evolutionary_approach:
  population_management:
    - population_size: 20
    - selection_pressure: "tournament_selection"
    - mutation_rate: "adaptive_based_on_diversity"
    - crossover_method: "semantic_instruction_blending"
  
  genetic_operators:
    - mutation: "llm_guided_instruction_variation"
    - crossover: "combine_successful_instruction_elements"
    - selection: "performance_based_fitness_evaluation"
    - elitism: "preserve_top_performing_instructions"
```

### Bayesian Optimization with Natural Language
```yaml
bayesian_optimization:
  surrogate_model:
    - type: "llm_based_performance_predictor"
    - input: "instruction_text_embeddings"
    - output: "predicted_performance_distribution"
    - uncertainty_quantification: "confidence_intervals"
  
  acquisition_function:
    - exploration_component: "uncertainty_sampling"
    - exploitation_component: "expected_improvement"
    - balancing: "adaptive_exploration_exploitation"
    - diversity_bonus: "encourage_novel_instructions"
```

## Output Format

```json
{
  "opro_optimization_session": {
    "session_id": "opro_2024_001",
    "configuration": {
      "optimizer_llm": "gpt-4-turbo",
      "scorer_llm": "gpt-4",
      "objective": "accuracy",
      "max_iterations": 50
    },
    "optimization_trajectory": [
      {
        "iteration": 1,
        "generated_instructions": [
          {
            "instruction": "Answer the question by first identifying key information",
            "score": 0.72,
            "rank": 1
          }
        ],
        "best_score": 0.72,
        "meta_prompt_version": "v1.0"
      }
    ],
    "final_results": {
      "best_instruction": {
        "text": "Analyze the context systematically, extract relevant facts, apply logical reasoning to connect information, and provide a comprehensive answer with supporting evidence",
        "final_score": 0.89,
        "improvement_over_baseline": 0.24,
        "iteration_discovered": 23
      },
      "optimization_summary": {
        "total_iterations": 31,
        "convergence_achieved": true,
        "total_instructions_evaluated": 248,
        "success_rate": "high",
        "computation_cost": "moderate"
      },
      "performance_analysis": {
        "score_progression": [0.65, 0.72, 0.78, 0.85, 0.89],
        "improvement_rate": "consistent",
        "plateau_detection": "none",
        "statistical_significance": "p&lt;0.001"
      }
    }
  }
}
```

## Research Foundation

Based on Google DeepMind's OPRO research:
- **Natural Language Optimization**: Using LLMs to optimize in natural language space
- **Meta-Prompt Design**: Effective patterns for guiding LLM optimizers
- **Optimization Trajectories**: Learning from previous solutions to generate better ones
- **Multi-Task Generalization**: Applying optimization across diverse problem domains

## Integration Points

- Combines with `/prompt-textgrad` for hybrid text-based optimization
- Works with `/prompt-dspy` for declarative prompt optimization
- Integrates with `/quality review` for multi-metric evaluation
- Supports `/agent-swarm` for distributed prompt optimization

## Advanced Configuration

### Custom Optimization Objectives
```yaml
custom_objectives:
  domain_specific_metrics:
    - medical_accuracy: "clinical_fact_verification"
    - legal_precision: "regulatory_compliance_checking"
    - educational_effectiveness: "learning_outcome_measurement"
    - creative_quality: "artistic_merit_assessment"
  
  composite_scoring:
    - weighted_combination: "multiple_metric_aggregation"
    - constraint_satisfaction: "hard_requirement_enforcement"
    - user_preference_modeling: "personalized_optimization"
    - contextual_adaptation: "situation_specific_tuning"
```

### Optimization Strategy Selection
```yaml
strategy_configuration:
  exploration_strategies:
    - random_search: "broad_instruction_space_exploration"
    - guided_generation: "llm_informed_candidate_creation"
    - evolutionary_methods: "genetic_algorithm_adaptation"
    - bayesian_optimization: "surrogate_model_guided_search"
  
  convergence_criteria:
    - performance_threshold: "target_score_achievement"
    - improvement_rate: "diminishing_returns_detection"
    - iteration_limit: "computational_budget_constraint"
        - stability_check: "consistent_performance_maintenance"
      </optimization_validation>
    </optimization_pipeline>
  </opro_framework>

  <o>
OPRO optimization framework completed with meta-prompt optimization:

**Optimization Method:** OPRO meta-optimization using LLM as optimizer
**Performance Improvement:** [percentage]% prompt effectiveness gain achieved
**Iterations Completed:** [count] optimization iterations executed
**Success Metrics:** [score] optimization success rate
**Prompt Quality:** [0-100] optimized prompt performance rating
**Meta-Learning:** OPRO framework successfully applied for automated improvement
  </o>
</prompt_component> 