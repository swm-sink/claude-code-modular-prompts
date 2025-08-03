<prompt_component>
  <step name="TextGrad Natural Language Optimization">
    <description>
Advanced TextGrad framework for automatic prompt refinement using textual gradients and natural language differentiation. Treats natural language feedback as gradients to iteratively optimize prompt performance through continuous improvement cycles.
    </description>
  </step>

  <textgrad_framework>
    <natural_language_gradients>
      <!-- TextGrad optimization through natural language feedback -->
      <textual_differentiation>

```xml
<command>prompt-textgrad</command>
<params>
  <!-- Core Optimization Settings -->
  <prompt>initial_prompt.md</prompt>
  <objective>accuracy</objective>
  <iterations>15</iterations>
  <learning_rate>0.1</learning_rate>
  
  <!-- TextGrad Configuration -->
  <gradient_method>natural_language_feedback</gradient_method>
  <evaluator>claude-4-opus</evaluator>
  <optimizer>textual_gradient_descent</optimizer>
  
  <!-- Feedback Generation -->
  <feedback>
    <critique_depth>comprehensive</critique_depth>
    <error_analysis>detailed</error_analysis>
    <improvement_suggestions>specific</improvement_suggestions>
    <context_awareness>high</context_awareness>
  </feedback>
  
  <!-- Optimization Strategy -->
  <strategy>
    <exploration_factor>0.2</exploration_factor>
    <convergence_threshold>0.95</convergence_threshold>
    <diversity_maintenance>true</diversity_maintenance>
    <momentum>0.9</momentum>
  </strategy>
  
  <!-- Validation -->
  <validation>
    <test_cases>evaluation_set.json</test_cases>
    <metrics>["accuracy", "coherence", "relevance", "completeness"]</metrics>
    <cross_validation>5_fold</cross_validation>
  </validation>
</params>
```

## Implementation

### TextGrad Methodology

#### 1. Textual Gradient Computation
```markdown
**Natural Language Differentiation:**
- Evaluate current prompt performance on test cases
- Generate detailed critique highlighting specific failures
- Identify precise areas needing improvement
- Quantify improvement direction and magnitude
- Create actionable feedback as "textual gradients"
```

#### 2. Gradient-Based Updates
```markdown
**Prompt Refinement Process:**
- Apply textual gradients to modify prompt components
- Adjust instruction clarity and specificity
- Refine example selection and formatting
- Optimize context and constraint specification
- Validate improvements through testing
```

#### 3. Iterative Optimization Loop
```markdown
**Continuous Improvement Cycle:**
- Execute current prompt on evaluation dataset
- Measure performance across multiple metrics
- Generate comprehensive improvement feedback
- Apply targeted modifications based on gradients
- Validate changes and continue optimization
```

### Optimization Framework

#### Phase 1: Initial Assessment
```yaml
assessment:
  - baseline_evaluation: current_prompt_performance
  - error_pattern_analysis: systematic_failure_identification
  - improvement_potential: optimization_opportunity_assessment
  - gradient_initialization: feedback_generation_setup
```

#### Phase 2: Gradient Generation
```yaml
gradient_computation:
  - performance_analysis: detailed_error_examination
  - failure_mode_identification: specific_problem_areas
  - improvement_direction: targeted_enhancement_suggestions
  - textual_gradient_formulation: actionable_feedback_creation
```

#### Phase 3: Prompt Update
```yaml
prompt_modification:
  - gradient_application: targeted_prompt_adjustments
  - component_refinement: instruction_and_example_improvement
  - validation_testing: performance_verification
  - iteration_continuation: optimization_loop_advancement
```

### Textual Gradient Types

#### Clarity Gradients
```markdown
**Instruction Clarity Enhancement:**
- Identify ambiguous or unclear instructions
- Suggest specific wording improvements
- Enhance precision and eliminates confusion
- Provide concrete examples for clarification
```

#### Relevance Gradients
```markdown
**Content Relevance Optimization:**
- Assess relevance of examples and context
- Remove extraneous or misleading information
- Focus content on core objectives
- Align all components with target outcomes
```

#### Completeness Gradients
```markdown
**Information Completeness Improvement:**
- Identify missing critical information
- Add necessary context and constraints
- Include relevant background details
- Ensure comprehensive coverage of requirements
```

#### Structure Gradients
```markdown
**Organizational Structure Enhancement:**
- Optimize information flow and organization
- Improve logical sequence and presentation
- Enhance readability and comprehension
- Refine formatting and visual structure
```

## Advanced Features

### Multi-Dimensional Optimization
```yaml
dimensions:
  accuracy: performance_on_target_metrics
  clarity: instruction_comprehensibility
  completeness: information_coverage
  efficiency: token_economy_optimization
  robustness: performance_across_contexts
```

### Adaptive Learning Rates
```yaml
learning_rate_adaptation:
  high_error: increase_modification_magnitude
  convergence: reduce_modification_intensity
  oscillation: stabilize_optimization_trajectory
  plateau: explore_alternative_directions
```

### Momentum-Based Updates
```yaml
momentum_system:
  gradient_history: previous_improvement_directions
  velocity_accumulation: consistent_improvement_amplification
  oscillation_dampening: stability_enhancement
  convergence_acceleration: faster_optimization
```

## Use Cases

### 1. Code Generation Prompt Optimization
```xml
<scenario>
  <task>Optimize code generation prompts</task>
  <objective>accuracy</objective>
  <focus_areas>
    <syntax_correctness>90%</syntax_correctness>
    <functionality>95%</functionality>
    <readability>85%</readability>
    <efficiency>80%</efficiency>
  </focus_areas>
</scenario>
```

### 2. Technical Documentation Enhancement
```xml
<scenario>
  <task>Improve documentation generation</task>
  <metrics>
    <clarity>high</clarity>
    <completeness>comprehensive</completeness>
    <accuracy>precise</accuracy>
    <usability>user_friendly</usability>
  </metrics>
</scenario>
```

### 3. Complex Reasoning Task Optimization
```xml
<scenario>
  <task>Multi-step reasoning improvement</task>
  <optimization>
    <logical_flow>enhanced</logical_flow>
    <step_clarity>detailed</step_clarity>
    <conclusion_validity>verified</conclusion_validity>
    <error_handling>robust</error_handling>
  </optimization>
</scenario>
```

## Gradient Generation Examples

### Performance Critique Example
```markdown
**Current Prompt Analysis:**
"The prompt successfully handles 70% of test cases but fails on edge cases involving complex nested structures. Specific improvements needed:

1. **Clarity Issue**: Instruction lacks specificity about handling nested objects
2. **Completeness Gap**: Missing examples of complex data structures
3. **Context Deficiency**: No guidance for error handling scenarios

**Textual Gradient (Improvement Direction):**
- Add explicit instructions for nested structure processing
- Include 2-3 examples of complex data scenarios
- Provide error handling guidelines and fallback strategies"
```

### Iterative Improvement Tracking
```json
{
  "optimization_history": [
    {
      "iteration": 1,
      "performance": 0.70,
      "primary_issues": ["clarity", "completeness"],
      "gradient_applied": "added_nested_structure_examples",
      "improvement": 0.15
    },
    {
      "iteration": 2,
      "performance": 0.85,
      "primary_issues": ["edge_case_handling"],
      "gradient_applied": "enhanced_error_handling_instructions",
      "improvement": 0.08
    }
  ]
}
```

## Output Format

```json
{
  "textgrad_optimization": {
    "session_id": "textgrad_2024_001",
    "initial_prompt": {
      "content": "original_prompt_text",
      "baseline_performance": 0.65,
      "identified_weaknesses": ["ambiguity", "incomplete_examples"]
    },
    "optimization_trajectory": [
      {
        "iteration": 1,
        "textual_gradient": {
          "critique": "detailed_performance_analysis",
          "improvement_suggestions": ["specific_enhancement_1", "specific_enhancement_2"],
          "priority_areas": ["instruction_clarity", "example_quality"]
        },
        "prompt_update": {
          "modifications": ["added_clarification", "improved_examples"],
          "updated_content": "modified_prompt_text",
          "performance_improvement": 0.12
        }
      }
    ],
    "final_optimized_prompt": {
      "content": "final_optimized_prompt_text",
      "performance_metrics": {
        "accuracy": 0.94,
        "clarity": 0.91,
        "completeness": 0.93,
        "robustness": 0.89
      },
      "optimization_summary": {
        "total_iterations": 8,
        "total_improvement": 0.29,
        "convergence_achieved": true,
        "key_optimizations": ["instruction_clarity", "example_enhancement", "structure_improvement"]
      }
    }
  }
}
```

## Research Foundation

Based on Stanford's TextGrad research and related work:
- **Automatic Differentiation via Text**: Natural language as optimization gradients
- **Iterative Prompt Refinement**: Systematic improvement through feedback loops
- **Multi-Metric Optimization**: Balancing multiple performance dimensions
- **Convergence Theory**: Mathematical foundations for text-based optimization

## Integration Points

- Combines with `/agent-swarm` for distributed prompt optimization
- Works with `/quality review` for validation and assessment
- Integrates with `/prompt-dspy` for declarative optimization comparison
- Supports `/meta-improve` for framework enhancement

## Advanced Configurations

### Custom Gradient Functions
```yaml
gradient_customization:
  error_weight_function: custom_error_prioritization
  improvement_direction_bias: domain_specific_preferences
  convergence_criteria: task_specific_thresholds
  gradient_smoothing: noise_reduction_techniques
```

### Multi-Model Evaluation
```yaml
multi_model_validation:
  evaluator_ensemble: [claude-4, gpt-4, custom-model]
  consensus_weighting: performance_based_voting
  disagreement_resolution: expert_arbitration
  cross_model_generalization: robustness_validation
```

---

      </iterative_refinement>
    </natural_language_gradients>
  </textgrad_framework>

  <o>
TextGrad natural language optimization completed with iterative refinement:

**Optimization Method:** TextGrad natural language differentiation
**Gradient Cycles:** [count] textual gradient optimization cycles completed
**Performance Gain:** [percentage]% prompt effectiveness improvement
**Refinement Quality:** [0-100] iterative improvement success rating
**Natural Language Feedback:** [count] feedback iterations processed
**Optimization Success:** TextGrad framework successfully applied for prompt enhancement
  </o>
</prompt_component> 