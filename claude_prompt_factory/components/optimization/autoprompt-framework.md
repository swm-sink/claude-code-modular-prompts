<prompt_component>
  <step name="AutoPrompt Gradient-Based Optimization">
    <description>
Advanced AutoPrompt framework for automatic prompt discovery using gradient-based optimization methods. Eliminates manual prompt engineering by finding optimal discrete prompts through gradient-guided token sequence optimization for maximum task performance.
    </description>
  </step>

  <autoprompt_framework>
    <gradient_optimization>
      <!-- AutoPrompt gradient-based optimization process -->
      <discrete_prompt_optimization>

```xml
<command>autoprompt-optimization</command>
<params>
  <!-- Core AutoPrompt Configuration -->
  <model>gpt-4</model>
  <task_type>classification</task_type>
  <target_metric>accuracy</target_metric>
  <optimization_steps>1000</optimization_steps>
  
  <!-- Prompt Structure -->
  <prompt_length>10</prompt_length>
  <template_structure>[TRIGGER] [X] [MASK]</template_structure>
  <trigger_length>5</trigger_length>
  <mask_position>end</mask_position>
  
  <!-- Optimization Settings -->
  <search_algorithm>gradient_descent</search_algorithm>
  <gradient_accumulation>true</gradient_accumulation>
  <learning_rate>0.3</learning_rate>
  <beam_size>10</beam_size>
  
  <!-- Token Selection -->
  <vocabulary_subset>top_50k</vocabulary_subset>
  <token_filtering>
    <exclude_special>true</exclude_special>
    <exclude_rare>true</exclude_rare>
    <min_frequency>100</min_frequency>
  </token_filtering>
  
  <!-- Search Strategy -->
  <initialization>random</initialization>
  <search_method>
    <type>hotflip</type>
    <candidate_pool_size>100</candidate_pool_size>
    <flip_probability>0.1</flip_probability>
  </search_method>
  
  <!-- Evaluation -->
  <validation_split>0.2</validation_split>
  <early_stopping>
    <patience>50</patience>
    <min_delta>0.001</min_delta>
  </early_stopping>
  
  <!-- Output Configuration -->
  <save_intermediate>true</save_intermediate>
  <log_frequency>10</log_frequency>
        <output_best_k>5</output_best_k>
      </gradient_configuration>
    </gradient_optimization>
    
    <technical_implementation>
      <gradient_search>
        <embedding_gradients>Compute gradients with respect to token embeddings</embedding_gradients>
- **Discrete Optimization**: Map continuous gradients to discrete token selections
- **HotFlip Algorithm**: Efficiently find optimal token substitutions
- **Beam Search**: Maintain multiple candidate prompt hypotheses

### Search Algorithms
- **Random Search**: Baseline comparison method
- **Gradient Descent**: Continuous embedding space optimization
- **Genetic Algorithm**: Evolutionary prompt optimization
- **Simulated Annealing**: Escape local optima in prompt space

### Token Selection Strategies
- **Gradient-Based**: Select tokens with highest gradient magnitudes
- **Semantic Similarity**: Choose tokens semantically similar to optimal embeddings
- **Frequency Filtering**: Prioritize common, meaningful tokens
- **POS Constraints**: Enforce grammatical structure constraints

## Advanced Features

### Multi-Task Optimization
```xml
<multi_task>
  <enabled>true</enabled>
  <tasks>
    <task>sentiment_analysis</task>
    <task>topic_classification</task>
    <task>intent_detection</task>
  </tasks>
  <weight_strategy>uniform</weight_strategy>
  <joint_optimization>true</joint_optimization>
</multi_task>
```

### Adversarial Robustness
```xml
<adversarial_training>
  <enabled>true</enabled>
  <attack_methods>
    <method>synonym_substitution</method>
    <method>character_level_noise</method>
    <method>paraphrase_attacks</method>
  </attack_methods>
  <robustness_weight>0.1</robustness_weight>
</adversarial_training>
```

### Transfer Learning
```xml
<transfer_learning>
  <source_domain>movie_reviews</source_domain>
  <target_domain>product_reviews</target_domain>
  <adaptation_strategy>fine_tuning</adaptation_strategy>
  <domain_regularization>0.01</domain_regularization>
</transfer_learning>
```

## Output Format

### Optimized Prompts
```json
{
  "best_prompts": [
    {
      "rank": 1,
      "prompt": "Please classify carefully [X] as",
      "score": 0.924,
      "tokens": ["Please", "classify", "carefully", "[X]", "as"],
      "metrics": {
        "accuracy": 0.924,
        "f1_score": 0.918,
        "precision": 0.922,
        "recall": 0.915
      }
    }
  ],
  "optimization_history": {
    "iterations": 847,
    "best_score_trajectory": [0.654, 0.721, 0.798, 0.924],
    "convergence_step": 847,
    "total_time": "2h 15m"
  },
  "token_analysis": {
    "most_effective_tokens": ["carefully", "classify", "analyze"],
    "position_importance": [0.8, 0.6, 0.9, 0.4, 0.7],
    "semantic_clusters": ["evaluation", "analysis", "classification"]
  }
}
```

## Integration Examples

### With Classification Tasks
```xml
<integration>
  <task>sentiment_classification</task>
  <baseline_prompt>What is the sentiment of: [X]</baseline_prompt>
  <optimization_target>f1_macro</optimization_target>
  <constraint>max_length_20_tokens</constraint>
</integration>
```

### With Question Answering
```xml
<integration>
  <task>reading_comprehension</task>
  <template>Context: [CONTEXT] Question: [QUESTION] Answer: [MASK]</template>
  <optimize_components>["CONTEXT", "QUESTION"]</optimize_components>
  <answer_constraints>extractive</answer_constraints>
</integration>
```

## Evaluation Metrics

### Performance Metrics
- **Task Performance**: Primary task accuracy/F1 score
- **Prompt Quality**: Semantic coherence and fluency
- **Generalization**: Performance on held-out domains
- **Efficiency**: Optimization time and convergence speed

### Robustness Testing
- **Input Variation**: Performance across input variations
- **Domain Transfer**: Cross-domain prompt effectiveness
- **Adversarial Stability**: Resistance to prompt attacks
- **Length Sensitivity**: Performance across input lengths

## Research Integration

Based on cutting-edge research in automatic prompt optimization:
- **Gradient-Based Methods**: AutoPrompt and derivative techniques
- **Discrete Optimization**: HotFlip and token-level search
- **Meta-Learning**: Learning to optimize prompts across tasks
- **Neural Architecture Search**: Applying NAS principles to prompts

## Use Cases

### Content Moderation
- Automatically discover optimal prompts for toxicity detection
- Optimize classification triggers for different content types
- Adapt prompts for emerging harmful content patterns

### Scientific Literature Analysis
- Generate domain-specific prompts for paper classification
- Optimize extraction prompts for citation networks
- Discover effective prompts for hypothesis generation

### Legal Document Processing
- Automatically generate prompts for legal case classification
- Optimize contract analysis and clause extraction prompts
- Discover effective prompts for legal precedent matching

### Medical Text Analysis
- Generate specialized prompts for symptom classification
- Optimize diagnostic reasoning prompt templates
- Discover effective prompts for treatment recommendation

      </gradient_validation>
    </gradient_optimization>
  </autoprompt_framework>

  <o>
AutoPrompt gradient-based optimization completed with discrete prompt discovery:

**Optimization Method:** Gradient-based discrete prompt optimization
**Performance Improvement:** [percentage]% task performance gain achieved
**Token Sequences:** [count] optimal token sequences discovered
**Gradient Steps:** [count] optimization iterations executed
**Discovery Success:** [0-100] prompt discovery effectiveness rating
**Automation Level:** Full automation of manual prompt engineering achieved
      </technical_implementation>
    </autoprompt_framework>

  <o>
AutoPrompt gradient-based optimization completed with discrete prompt optimization:

**Optimization Method:** AutoPrompt gradient-based discrete optimization
**Prompt Performance:** [percentage]% improvement in task performance achieved
**Token Efficiency:** [count] optimal tokens identified through gradient search
**Optimization Quality:** [0-100] AutoPrompt optimization effectiveness rating
**Discrete Excellence:** Advanced gradient-based prompt optimization with HotFlip algorithm
  </o>
</prompt_component> 