<prompt_component>
  <step name="Native Prompt Optimization">
    <description>
Advanced prompt optimization using Claude's iterative improvement and self-evaluation capabilities. Provides native optimization through iterative refinement, prompt analysis, performance evaluation, and adaptive enhancement without external optimization tools.
    </description>
  </step>

  <prompt_optimization>
    <native_optimization>
      <!-- Native prompt optimization using Claude's capabilities -->
      <optimization_cycle>
  <analyze>Examine current prompt structure and performance</analyze>
  <identify>Find specific areas for improvement</identify>
  <modify>Generate improved version with targeted changes</modify>
  <evaluate>Assess improvement in quality, clarity, and effectiveness</evaluate>
  <iterate>Repeat cycle until optimal performance achieved</iterate>
</optimization_cycle>
```

### Claude's Optimization Approach
Claude leverages its natural language understanding to optimize prompts through:

1. **Structural Analysis**: Examine prompt organization and flow
2. **Clarity Assessment**: Identify ambiguous or unclear instructions
3. **Completeness Check**: Ensure all necessary information is included
4. **Efficiency Review**: Remove redundancy and improve conciseness
5. **Performance Prediction**: Anticipate how changes will affect outcomes

## Optimization Strategies

### Clarity Enhancement
```xml
<clarity_optimization>
  <original_prompt>
    "Make the code better and fix any issues you find"
  </original_prompt>
  
  <analysis>
    <issues>
      <vague>"better" is subjective and unclear</vague>
      <ambiguous>"issues" could mean many things</ambiguous>
      <incomplete>No specific goals or constraints</incomplete>
    </issues>
  </analysis>
  
  <optimized_prompt>
    "Analyze the provided code and improve it by:
    1. Fixing any syntax errors or bugs
    2. Optimizing performance bottlenecks
    3. Improving readability and maintainability
    4. Adding error handling where needed
    
    Provide specific explanations for each change made."
  </optimized_prompt>
  
  <improvement_metrics>
    <specificity>Increased from 2/10 to 9/10</specificity>
    <actionability>Increased from 3/10 to 9/10</actionability>
    <clarity>Increased from 4/10 to 9/10</clarity>
  </improvement_metrics>
</clarity_optimization>
```

### Structure Optimization
```xml
<structure_optimization>
  <pattern>Logical flow improvement</pattern>
  
  <before>
    "Fix the authentication system. Make sure it's secure. Also handle errors properly. 
    The database connections need optimization too. Don't forget about logging."
  </before>
  
  <optimized_structure>
    "Optimize the authentication system with the following priorities:
    
    1. **Security Improvements:**
       - Implement proper password hashing
       - Add rate limiting for login attempts
       - Validate input sanitization
    
    2. **Database Optimization:**
       - Review connection pooling
       - Optimize authentication queries
       - Add proper indexing
    
    3. **Error Handling & Logging:**
       - Add comprehensive error catching
       - Implement security event logging
       - Create user-friendly error messages
    
    For each improvement, provide before/after code examples."
  </optimized_structure>
  
  <improvements>
    <organization>Clear priority-based structure</organization>
    <specificity>Detailed sub-requirements</specificity>
    <output_format>Explicit format requirements</output_format>
  </improvements>
</structure_optimization>
```

### Context Optimization
```xml
<context_optimization>
  <principle>Provide optimal context without overwhelming</principle>
  
  <analysis>
    <too_little_context>
      "Debug this function"
      <problem>No information about expected behavior, inputs, or errors</problem>
    </too_little_context>
    
    <too_much_context>
      "Debug this function [followed by 500 lines of unrelated code]"
      <problem>Overwhelming information, hard to focus</problem>
    </too_much_context>
    
    <optimal_context>
      "Debug this authentication function that should validate user credentials:
      
      **Expected Behavior:**
      - Accept username/password
      - Return success/failure status
      - Log authentication attempts
      
      **Current Issue:**
      - Function returns success for invalid passwords
      
      **Relevant Code:**
      [Only the problematic function and related helpers]"
      
      <benefits>
        <focused>Relevant information only</focused>
        <clear_goal>Specific problem statement</clear_goal>
        <context>Sufficient background for understanding</context>
      </benefits>
    </optimal_context>
  </analysis>
</context_optimization>
```

## Advanced Optimization Techniques

### Multi-Dimensional Optimization
```xml
<multi_dimensional>
  <dimensions>
    <accuracy>How precisely does the prompt achieve its goal?</accuracy>
    <efficiency>How concisely is the request communicated?</efficiency>
    <clarity>How easily understood is the prompt?</clarity>
    <completeness>Are all necessary details included?</completeness>
    <robustness>How well does it handle edge cases?</robustness>
  </dimensions>
  
  <optimization_example>
    <original_score>
      <accuracy>6/10</accuracy>
      <efficiency>4/10</efficiency>
      <clarity>5/10</clarity>
      <completeness>3/10</completeness>
      <robustness>2/10</robustness>
    </original_score>
    
    <after_optimization>
      <accuracy>9/10</accuracy>
      <efficiency>8/10</efficiency>
      <clarity>9/10</clarity>
      <completeness>8/10</completeness>
      <robustness>7/10</robustness>
    </after_optimization>
  </optimization_example>
</multi_dimensional>
```

### Adaptive Optimization
```xml
<adaptive_optimization>
  <strategy>Optimize based on task type and complexity</strategy>
  
  <task_types>
    <creative_tasks>
      <optimization_focus>Inspiration, freedom, exploration</optimization_focus>
      <prompt_style>Open-ended, encouraging, multi-path</prompt_style>
    </creative_tasks>
    
    <analytical_tasks>
      <optimization_focus>Precision, methodology, completeness</optimization_focus>
      <prompt_style>Structured, detailed, step-by-step</prompt_style>
    </analytical_tasks>
    
    <implementation_tasks>
      <optimization_focus>Clarity, specificity, actionability</optimization_focus>
      <prompt_style>Concrete, detailed, with examples</prompt_style>
    </implementation_tasks>
  </task_types>
</adaptive_optimization>
```

### Iterative Refinement
```xml
<iterative_refinement>
  <iteration_1>
    <prompt>"Improve this code"</prompt>
    <assessment>Too vague, lacks direction</assessment>
    <refinement>Add specific improvement areas</refinement>
  </iteration_1>
  
  <iteration_2>
    <prompt>"Improve this code for better performance and readability"</prompt>
    <assessment>Better but still lacks specificity</assessment>
    <refinement>Define what "better" means with metrics</refinement>
  </iteration_2>
  
  <iteration_3>
    <prompt>"Optimize this code to:
    1. Reduce execution time by identifying O(n²) operations
    2. Improve readability by adding clear variable names and comments
    3. Add error handling for edge cases
    
    Measure improvements with before/after benchmarks."</prompt>
    <assessment>Specific, actionable, measurable</assessment>
    <status>Optimization complete</status>
  </iteration_3>
</iterative_refinement>
```

## Performance Metrics

### Quality Measurements
```xml
<quality_metrics>
  <specificity>
    <measure>Percentage of concrete, actionable instructions</measure>
    <target>85%+ specific instructions</target>
  </specificity>
  
  <clarity>
    <measure>Readability and unambiguous language</measure>
    <target>95%+ clear communication</target>
  </clarity>
  
  <completeness>
    <measure>All necessary information provided</measure>
    <target>90%+ complete requirements</target>
  </completeness>
  
  <efficiency>
    <measure>Optimal information density</measure>
    <target>80%+ relevant content</target>
  </efficiency>
</quality_metrics>
```

### Effectiveness Testing
```xml
<effectiveness_testing>
  <before_optimization>
    <success_rate>60%</success_rate>
    <quality_score>6.5/10</quality_score>
    <completion_time>High variance</completion_time>
  </before_optimization>
  
  <after_optimization>
    <success_rate>90%</success_rate>
    <quality_score>8.7/10</quality_score>
    <completion_time>Consistent, predictable</completion_time>
  </after_optimization>
  
  <improvement>
    <success_rate>+50% improvement</success_rate>
    <quality>+34% improvement</quality>
    <consistency>Significantly improved</consistency>
  </improvement>
</effectiveness_testing>
```

## Integration Patterns

### With ReAct Reasoning
```xml
<react_optimization>
  <thought>This prompt could be clearer and more specific</thought>
  <action>Analyze current prompt structure and identify improvement areas</action>
  <observation>Found 3 areas of ambiguity and 2 missing requirements</observation>
  <thought>I'll address the most critical issues first</thought>
  <action>Rewrite prompt with specific instructions and clear objectives</action>
  <observation>New prompt is 40% more specific and includes all requirements</observation>
</react_optimization>
```

### With Tree of Thoughts
```xml
<tot_optimization>
  <branch_1>Optimize for clarity and specificity</branch_1>
  <branch_2>Optimize for efficiency and conciseness</branch_2>
  <branch_3>Optimize for completeness and robustness</branch_3>
  <synthesis>Combine best elements: clear, efficient, and complete</synthesis>
</tot_optimization>
```

## Usage Instructions

### Activation
```xml
<activate_optimization>
  <mode>prompt_optimization</mode>
  <focus>clarity|efficiency|completeness|all</focus>
  <iterations>auto|1|3|5</iterations>
</activate_optimization>
```

### Customization
```xml
<optimization_settings>
  <style>conservative|balanced|aggressive</style>
  <priority>clarity|efficiency|accuracy</priority>
  <constraints>token_limit|complexity_limit|time_limit</constraints>
</optimization_settings>
```

      </optimization_settings>
    </native_optimization>
  </prompt_optimization>

  <o>
Native prompt optimization completed with iterative improvement:

**Optimization Cycles:** [count] iterative improvement cycles completed
**Performance Gain:** [percentage]% prompt effectiveness improvement achieved
**Quality Enhancement:** [0-100] prompt quality optimization rating
**Iterative Refinement:** [count] refinement iterations executed
**Communication Effectiveness:** [percentage]% communication clarity improvement
**Native Integration:** Advanced prompt optimization using Claude's natural capabilities
  </o>
</prompt_component> 