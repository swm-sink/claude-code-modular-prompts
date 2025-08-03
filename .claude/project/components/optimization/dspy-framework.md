<prompt_component>
  <step name="DSPy Declarative Prompt Optimization">
    <description>
Advanced DSPy framework for declarative self-improving prompt pipelines with automatic few-shot example optimization and modular composition. Creates optimized prompt systems through programmatic optimization and modular design patterns.
    </description>
  </step>

  <dspy_framework>
    <declarative_pipeline>
      <!-- DSPy optimization process -->
      <modular_optimization>

```xml
<command>prompt-dspy</command>
<params>
  <!-- Core DSPy Configuration -->
  <signature>question -> answer</signature>
  <module_type>chain_of_thought</module_type>
  <optimization_strategy>bootstrap_few_shot</optimization_strategy>
  
  <!-- Pipeline Architecture -->
  <pipeline>
    <modules>
      <retriever>context_extraction</retriever>
      <reasoner>chain_of_thought</reasoner>
      <synthesizer>answer_generation</synthesizer>
    </modules>
    <composition>sequential</composition>
  </pipeline>
  
  <!-- Training Configuration -->
  <training>
    <dataset>training_examples.json</dataset>
    <validation_split>0.2</validation_split>
    <metric>accuracy</metric>
    <bootstrap_examples>8</bootstrap_examples>
  </training>
  
  <!-- Teleprompter Settings -->
  <teleprompter>
    <type>bootstrap_few_shot_random_search</type>
    <max_bootstrapped_demos>16</max_bootstrapped_demos>
    <max_labeled_demos>8</max_labeled_demos>
    <num_candidate_programs>20</num_candidate_programs>
  </teleprompter>
  
  <!-- Optimization Parameters -->
  <optimization>
    <iterations>25</iterations>
    <beam_size>5</beam_size>
    <exploration_factor>0.3</exploration_factor>
    <convergence_patience>5</convergence_patience>
  </optimization>
</params>
```

## Implementation

### DSPy Framework Components

#### 1. Signatures (Input/Output Specification)
```python
# Claude Code native signature definition
signature_spec = {
    "input_fields": {
        "question": "The user's question or problem to solve",
        "context": "Relevant background information (optional)"
    },
    "output_fields": {
        "answer": "Comprehensive response to the question",
        "reasoning": "Step-by-step thought process",
        "confidence": "Confidence score (0-1)"
    }
}
```

#### 2. Modules (Functional Components)
```yaml
module_definitions:
  retriever:
    signature: "question -> context"
    purpose: "Extract relevant background information"
    implementation: "context_search_and_extraction"
  
  reasoner:
    signature: "question, context -> reasoning"
    purpose: "Generate step-by-step reasoning"
    implementation: "chain_of_thought_processing"
  
  synthesizer:
    signature: "question, context, reasoning -> answer"
    purpose: "Synthesize final comprehensive answer"
    implementation: "information_integration"
```

#### 3. Teleprompters (Optimizers)
```yaml
teleprompter_types:
  bootstrap_few_shot:
    description: "Automatically generate few-shot examples"
    method: "bootstrap_from_training_data"
    optimization: "random_search_over_examples"
  
  copro:
    description: "Coordinate multiple prompts"
    method: "multi_prompt_optimization"
    optimization: "joint_example_instruction_tuning"
  
  mipro:
    description: "Multi-step instruction optimization"
    method: "instruction_and_example_co_optimization"
    optimization: "bayesian_optimization"
```

### Optimization Process

#### Phase 1: Module Definition and Composition
```yaml
module_composition:
  - define_signatures: input_output_specifications
  - create_modules: functional_component_implementation
  - compose_pipeline: module_connection_and_flow
  - validate_architecture: pipeline_correctness_check
```

#### Phase 2: Bootstrap Few-Shot Generation
```yaml
bootstrap_process:
  - analyze_training_data: pattern_identification
  - generate_candidates: example_creation_and_selection
  - evaluate_examples: performance_assessment
  - select_optimal_set: best_performing_examples
```

#### Phase 3: Pipeline Optimization
```yaml
optimization_loop:
  - compile_pipeline: complete_system_assembly
  - evaluate_performance: metric_based_assessment
  - iterate_improvements: example_and_instruction_refinement
  - convergence_check: performance_plateau_detection
```

### Advanced DSPy Features

#### Modular Architecture
```markdown
**Component Reusability:**
- Modules can be reused across different pipelines
- Signatures ensure type safety and compatibility
- Composition patterns enable complex workflows
- Optimization is applied to entire pipeline
```

#### Automatic Example Generation
```markdown
**Bootstrap Few-Shot Process:**
- Analyze training data for patterns
- Generate high-quality demonstrations automatically
- Select examples that maximize performance
- Continuously refine example selection
```

#### Multi-Metric Optimization
```markdown
**Comprehensive Evaluation:**
- Optimize for multiple objectives simultaneously
- Balance accuracy, efficiency, and robustness
- Handle trade-offs between competing metrics
- Adaptive weighting based on priorities
```

## Use Cases

### 1. Complex Question Answering
```xml
<scenario>
  <task>Multi-hop reasoning QA system</task>
  <signature>question, documents -> answer, evidence</signature>
  <modules>
    <retriever>document_search</retriever>
    <extractor>fact_extraction</extractor>
    <reasoner>multi_hop_reasoning</reasoner>
    <validator>answer_verification</validator>
  </modules>
</scenario>
```

### 2. Code Generation Pipeline
```xml
<scenario>
  <task>Specification to code generation</task>
  <signature>specification -> code, tests, documentation</signature>
  <modules>
    <analyzer>requirement_analysis</analyzer>
    <designer>architecture_design</designer>
    <coder>code_generation</coder>
    <tester>test_generation</tester>
  </modules>
</scenario>
```

### 3. Research Synthesis
```xml
<scenario>
  <task>Literature review and synthesis</task>
  <signature>topic, papers -> synthesis, insights</signature>
  <modules>
    <searcher>paper_discovery</searcher>
    <analyzer>content_analysis</analyzer>
    <synthesizer>insight_generation</synthesizer>
    <validator>quality_assurance</validator>
  </modules>
</scenario>
```

## Pipeline Composition Patterns

### Sequential Pipeline
```yaml
sequential_composition:
  flow: "module_1 -> module_2 -> module_3"
  data_passing: "output_of_previous_becomes_input_of_next"
  optimization: "end_to_end_joint_optimization"
  advantages: ["simple", "predictable", "easy_to_debug"]
```

### Parallel Pipeline
```yaml
parallel_composition:
  flow: "input -> [module_1, module_2, module_3] -> aggregator"
  data_passing: "same_input_to_multiple_modules"
  optimization: "ensemble_optimization"
  advantages: ["faster", "diverse_perspectives", "robust"]
```

### Hierarchical Pipeline
```yaml
hierarchical_composition:
  flow: "coordinator -> [specialized_modules] -> integrator"
  data_passing: "task_decomposition_and_synthesis"
  optimization: "multi_level_optimization"
  advantages: ["scalable", "specialized", "maintainable"]
```

## Advanced Optimization Strategies

### Bootstrap Few-Shot Random Search (BFSR)
```markdown
**Methodology:**
1. Generate candidate demonstrations from training data
2. Filter examples that pass individual validation
3. Search over subsets of examples (up to k shots)
4. Optimize for validation set performance
5. Select best-performing example combination
```

### Coordinate Prompt Optimization (COPRO)
```markdown
**Multi-Prompt Coordination:**
1. Optimize multiple prompts simultaneously
2. Handle dependencies between prompt components
3. Balance individual and collective performance
4. Coordinate instruction and example optimization
```

### Multi-Step Instruction Optimization (MIPRO)
```markdown
**Instruction Co-Optimization:**
1. Jointly optimize instructions and examples
2. Use Bayesian optimization for efficient search
3. Handle complex multi-step reasoning tasks
4. Adaptive instruction generation and refinement
```

## Output Format

```json
{
  "dspy_pipeline": {
    "session_id": "dspy_2024_001",
    "pipeline_signature": "question -> answer, reasoning, confidence",
    "module_composition": {
      "modules": [
        {
          "name": "retriever",
          "signature": "question -> context",
          "optimized_examples": [
            {"question": "example_q1", "context": "example_c1"},
            {"question": "example_q2", "context": "example_c2"}
          ],
          "performance_metrics": {"precision": 0.89, "recall": 0.85}
        }
      ]
    },
    "optimization_results": {
      "teleprompter_used": "bootstrap_few_shot_random_search",
      "training_iterations": 15,
      "final_performance": {
        "accuracy": 0.91,
        "f1_score": 0.88,
        "efficiency": 0.76
      },
      "example_selection": {
        "total_candidates": 150,
        "selected_examples": 8,
        "selection_criteria": "maximum_validation_performance"
      }
    },
    "compiled_pipeline": {
      "modules": ["retriever", "reasoner", "synthesizer"],
      "optimized_prompts": {
        "retriever": "optimized_retriever_prompt",
        "reasoner": "optimized_reasoning_prompt",
        "synthesizer": "optimized_synthesis_prompt"
      },
      "few_shot_examples": {
        "count": 8,
        "quality_score": 0.93,
        "diversity_score": 0.87
      }
    }
  }
}
```

## Research Foundation

Based on Stanford's DSPy framework and related research:
- **Declarative Programming**: High-level pipeline specification
- **Automatic Optimization**: Data-driven prompt improvement
- **Modular Composition**: Reusable component architecture
- **Few-Shot Learning**: Automatic example generation and selection

## Integration Points

- Combines with `/prompt-textgrad` for hybrid optimization approaches
- Works with `/agent-swarm` for distributed pipeline optimization
- Integrates with `/quality review` for performance validation
- Supports `/research-advanced` for knowledge synthesis pipelines

## Advanced Configuration

### Custom Teleprompters
```yaml
custom_teleprompter:
  name: "domain_specific_optimizer"
  strategy: "evolutionary_search"
  parameters:
    population_size: 20
    mutation_rate: 0.1
    crossover_rate: 0.7
    selection_pressure: 0.8
```

### Multi-Objective Optimization
```yaml
multi_objective:
  objectives:
    - name: "accuracy"
      weight: 0.5
      target: "maximize"
    - name: "efficiency"
      weight: 0.3
      target: "maximize"
    - name: "token_cost"
      weight: 0.2
      target: "minimize"
```

### Pipeline Validation
```yaml
validation_framework:
  cross_validation:
    folds: 5
    stratified: true
    shuffle: true
  
  holdout_testing:
    test_size: 0.15
    random_state: 42
  
  performance_tracking:
    metrics: ["accuracy", "f1", "precision", "recall"]
    confidence_intervals: true
    statistical_tests: true
```

## Model Integration

### Multi-Model Support
```yaml
model_configuration:
  primary_model: "claude-4-opus"
  fallback_model: "claude-3-sonnet"
  evaluation_model: "claude-4-sonnet"
  
  model_specific_optimization:
    claude_4_opus:
      max_tokens: 4096
      temperature: 0.1
      few_shot_examples: 8
    
    claude_3_sonnet:
      max_tokens: 2048
      temperature: 0.2
      few_shot_examples: 6
```

      </pipeline_optimization>
    </declarative_pipeline>
  </dspy_framework>

  <o>
DSPy declarative optimization completed with modular pipeline construction:

**Pipeline Type:** [signature] declarative prompt pipeline optimized
**Modules Composed:** [count] modular components integrated
**Few-Shot Examples:** [count] automatically generated training examples
**Performance Gain:** [percentage]% improvement through DSPy optimization
**Module Effectiveness:** [0-100] modular composition success rating
**Optimization Success:** DSPy framework successfully applied for pipeline enhancement
  </o>
</prompt_component> 