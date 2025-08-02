# OPRO Optimization Framework

**Purpose**: Google DeepMind's OPRO (Optimization by Prompting) framework using LLMs as optimizers for automatic prompt engineering through natural language meta-optimization.

**Usage**: 
- Leverages LLMs to iteratively optimize prompts through meta-prompting
- Generates solution-score pairs to guide prompt improvement
- Supports multiple optimization objectives (accuracy, efficiency, creativity)
- Implements exploration strategies (random search, guided generation, evolutionary)
- Provides comprehensive performance metrics and convergence criteria

**Compatibility**: 
- **Works with**: prompt-optimization, dspy-framework, textgrad-framework, autoprompt-framework
- **Requires**: optimizer_llm, scorer_llm, optimization_objective, training_set
- **Conflicts**: None (enhances other optimization approaches)

**Implementation**:
```xml
<command>prompt-opro</command>
<params>
  <optimizer_llm>gpt-4-turbo</optimizer_llm>
  <optimization_objective>accuracy</optimization_objective>
  <max_iterations>50</max_iterations>
  <meta_prompt>Generate improved instruction for higher accuracy</meta_prompt>
</params>
```

**Category**: optimization | **Complexity**: complex | **Time**: 1-2 days