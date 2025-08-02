# TextGrad Natural Language Optimization

**Purpose**: Advanced TextGrad framework for automatic prompt refinement using textual gradients and natural language differentiation to iteratively optimize prompt performance.

**Usage**: 
- Treats natural language feedback as gradients for continuous improvement
- Implements textual gradient descent with comprehensive error analysis
- Generates specific improvement suggestions through AI critique
- Supports multi-model evaluation for robust optimization
- Maintains diversity while converging to optimal prompts

**Compatibility**: 
- **Works with**: prompt-optimization, opro-framework, dspy-framework, meta-improve
- **Requires**: initial_prompt, objective, evaluator_model, learning_rate
- **Conflicts**: None (complementary to other optimization methods)

**Implementation**:
```xml
<command>prompt-textgrad</command>
<params>
  <gradient_method>natural_language_feedback</gradient_method>
  <evaluator>claude-4-opus</evaluator>
  <optimizer>textual_gradient_descent</optimizer>
  <learning_rate>0.1</learning_rate>
  <iterations>15</iterations>
</params>
```

**Category**: optimization | **Complexity**: complex | **Time**: 1-2 days