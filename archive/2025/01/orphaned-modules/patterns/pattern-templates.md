# Pattern Templates Library

## Overview

Reusable XML-structured templates for all prompt engineering patterns. These templates provide consistent, validated structures that can be dynamically populated based on task requirements.

## Template Structure Standard

All pattern templates follow this standardized XML structure:

```xml
<pattern_template>
  <metadata>
    <pattern_id>unique_identifier</pattern_id>
    <pattern_name>Human-readable name</pattern_name>
    <category>reasoning|learning|structural|optimization</category>
    <effectiveness_score>0.0-1.0</effectiveness_score>
    <version>semantic_version</version>
    <last_updated>ISO_date</last_updated>
  </metadata>
  
  <description>
    <purpose>Primary use case and objective</purpose>
    <strengths>Key advantages and effective scenarios</strengths>
    <limitations>Known constraints and anti-patterns</limitations>
  </description>
  
  <template_structure>
    <variables>
      <variable name="variable_name" type="string|array|object" required="true|false">
        Description and constraints
      </variable>
    </variables>
    
    <template>
      Template content with ${variable_name} placeholders
    </template>
  </template_structure>
  
  <validation_rules>
    <rule type="structural|semantic|effectiveness">Validation criteria</rule>
  </validation_rules>
  
  <usage_metrics>
    <metric name="token_efficiency">Average tokens used vs. output quality</metric>
    <metric name="success_rate">Percentage of successful applications</metric>
    <metric name="consistency">Reproducibility across similar tasks</metric>
  </usage_metrics>
</pattern_template>
```

## Reasoning Pattern Templates

### Chain-of-Thought Template

```xml
<pattern_template>
  <metadata>
    <pattern_id>cot-template-001</pattern_id>
    <pattern_name>Chain-of-Thought Reasoning Template</pattern_name>
    <category>reasoning</category>
    <effectiveness_score>0.85</effectiveness_score>
    <version>1.0.0</version>
    <last_updated>2024-07-06</last_updated>
  </metadata>
  
  <description>
    <purpose>Enable step-by-step logical reasoning for complex problems</purpose>
    <strengths>High accuracy on logical tasks, transparent reasoning process</strengths>
    <limitations>Verbose output, not suitable for simple tasks</limitations>
  </description>
  
  <template_structure>
    <variables>
      <variable name="task_description" type="string" required="true">
        The main problem or question to be solved
      </variable>
      <variable name="reasoning_steps" type="array" required="false">
        Predefined reasoning steps if known
      </variable>
      <variable name="verification_method" type="string" required="false">
        How to verify the final answer
      </variable>
    </variables>
    
    <template>
      <task>
        ${task_description}
      </task>
      
      <reasoning_approach>
        Let's work through this step-by-step:
        
        ${reasoning_steps ? reasoning_steps.map((step, i) => `${i+1}. ${step}`).join('\n') : 
        `1. Identify the key components of the problem
        2. Analyze relationships between components  
        3. Apply relevant principles or methods
        4. Work through the solution systematically
        5. Verify the result`}
      </reasoning_approach>
      
      <instructions>
        Please show your reasoning for each step and explain how you arrive at each conclusion.
        ${verification_method ? `Use this method to verify: ${verification_method}` : 
        'Double-check your work by reviewing each step.'}
      </instructions>
    </template>
  </template_structure>
  
  <validation_rules>
    <rule type="structural">Must include explicit step-by-step breakdown</rule>
    <rule type="semantic">Steps must be logically connected</rule>
    <rule type="effectiveness">Should achieve >80% accuracy on logical reasoning tasks</rule>
  </validation_rules>
  
  <usage_metrics>
    <metric name="token_efficiency">0.75 (moderate efficiency due to verbose reasoning)</metric>
    <metric name="success_rate">0.85 (high success on complex reasoning tasks)</metric>
    <metric name="consistency">0.82 (consistent step-by-step approach)</metric>
  </usage_metrics>
</pattern_template>
```

### Tree-of-Thought Template

```xml
<pattern_template>
  <metadata>
    <pattern_id>tot-template-001</pattern_id>
    <pattern_name>Tree-of-Thought Exploration Template</pattern_name>
    <category>reasoning</category>
    <effectiveness_score>0.78</effectiveness_score>
    <version>1.0.0</version>
    <last_updated>2024-07-06</last_updated>
  </metadata>
  
  <description>
    <purpose>Explore multiple reasoning paths in parallel with evaluation</purpose>
    <strengths>Discovers creative solutions, handles complex decision-making</strengths>
    <limitations>High token usage, can be overwhelming for simple problems</limitations>
  </description>
  
  <template_structure>
    <variables>
      <variable name="problem_statement" type="string" required="true">
        The core problem or challenge to address
      </variable>
      <variable name="evaluation_criteria" type="array" required="false">
        Criteria for comparing different approaches
      </variable>
      <variable name="max_approaches" type="number" required="false">
        Maximum number of approaches to explore (default: 3)
      </variable>
    </variables>
    
    <template>
      <problem>
        ${problem_statement}
      </problem>
      
      <exploration_framework>
        Let's explore multiple approaches to this problem:
        
        <approach_a>
          <reasoning>First approach and its logic</reasoning>
          <implementation>How this approach would work</implementation>
          <pros>Advantages of this method</pros>
          <cons>Limitations and risks</cons>
          <feasibility_score>1-10 rating</feasibility_score>
        </approach_a>
        
        <approach_b>
          <reasoning>Second approach and its logic</reasoning>
          <implementation>How this approach would work</implementation>
          <pros>Advantages of this method</pros>
          <cons>Limitations and risks</cons>
          <feasibility_score>1-10 rating</feasibility_score>
        </approach_b>
        
        <approach_c>
          <reasoning>Third approach and its logic</reasoning>
          <implementation>How this approach would work</implementation>
          <pros>Advantages of this method</pros>
          <cons>Limitations and risks</cons>
          <feasibility_score>1-10 rating</feasibility_score>
        </approach_c>
      </exploration_framework>
      
      <evaluation>
        Compare approaches using these criteria:
        ${evaluation_criteria ? evaluation_criteria.join(', ') : 
        'effectiveness, feasibility, resource requirements, risk level'}
        
        Select the best approach or recommend a hybrid solution.
        Provide clear justification for your recommendation.
      </evaluation>
    </template>
  </template_structure>
  
  <validation_rules>
    <rule type="structural">Must explore at least 2 distinct approaches</rule>
    <rule type="semantic">Each approach must be meaningfully different</rule>
    <rule type="effectiveness">Should provide valuable alternatives for complex problems</rule>
  </validation_rules>
  
  <usage_metrics>
    <metric name="token_efficiency">0.65 (lower efficiency due to parallel exploration)</metric>
    <metric name="success_rate">0.78 (good for creative problem-solving)</metric>
    <metric name="consistency">0.71 (varies based on problem complexity)</metric>
  </usage_metrics>
</pattern_template>
```

## Learning Pattern Templates

### Few-Shot Learning Template

```xml
<pattern_template>
  <metadata>
    <pattern_id>few-shot-template-001</pattern_id>
    <pattern_name>Few-Shot Learning Template</pattern_name>
    <category>learning</category>
    <effectiveness_score>0.89</effectiveness_score>
    <version>1.0.0</version>
    <last_updated>2024-07-06</last_updated>
  </metadata>
  
  <description>
    <purpose>Establish patterns through high-quality examples</purpose>
    <strengths>Excellent for format specification, style transfer</strengths>
    <limitations>Requires good examples, may not work for novel tasks</limitations>
  </description>
  
  <template_structure>
    <variables>
      <variable name="task_description" type="string" required="true">
        Clear explanation of the desired task
      </variable>
      <variable name="examples" type="array" required="true">
        Array of input-output example pairs
      </variable>
      <variable name="new_input" type="string" required="true">
        The actual input to process
      </variable>
      <variable name="format_requirements" type="string" required="false">
        Specific format constraints
      </variable>
    </variables>
    
    <template>
      <task_definition>
        ${task_description}
        ${format_requirements ? `\n\nFormat requirements: ${format_requirements}` : ''}
      </task_definition>
      
      <examples>
        Here are examples of the desired pattern:
        
        ${examples.map((example, i) => `
        Example ${i + 1}:
        Input: ${example.input}
        Output: ${example.output}
        `).join('\n')}
      </examples>
      
      <application>
        Now apply the same pattern to this new input:
        
        Input: ${new_input}
        Output:
      </application>
    </template>
  </template_structure>
  
  <validation_rules>
    <rule type="structural">Must include 3-5 diverse examples</rule>
    <rule type="semantic">Examples must clearly demonstrate the pattern</rule>
    <rule type="effectiveness">Should achieve >85% accuracy on pattern recognition tasks</rule>
  </validation_rules>
  
  <usage_metrics>
    <metric name="token_efficiency">0.80 (good efficiency with focused examples)</metric>
    <metric name="success_rate">0.89 (high success for pattern-based tasks)</metric>
    <metric name="consistency">0.87 (very consistent with good examples)</metric>
  </usage_metrics>
</pattern_template>
```

## Structural Pattern Templates

### XML-Structured Template

```xml
<pattern_template>
  <metadata>
    <pattern_id>xml-template-001</pattern_id>
    <pattern_name>XML-Structured Organization Template</pattern_name>
    <category>structural</category>
    <effectiveness_score>0.92</effectiveness_score>
    <version>1.0.0</version>
    <last_updated>2024-07-06</last_updated>
  </metadata>
  
  <description>
    <purpose>Create hierarchical, well-organized prompt structure</purpose>
    <strengths>Prevents information mixing, highly parseable</strengths>
    <limitations>Verbose for simple tasks, requires XML knowledge</limitations>
  </description>
  
  <template_structure>
    <variables>
      <variable name="context_info" type="string" required="false">
        Background information and situational context
      </variable>
      <variable name="task_specification" type="string" required="true">
        Detailed task description
      </variable>
      <variable name="constraints" type="array" required="false">
        Limitations and requirements
      </variable>
      <variable name="examples" type="array" required="false">
        Supporting examples
      </variable>
      <variable name="output_format" type="string" required="false">
        Specific output format requirements
      </variable>
    </variables>
    
    <template>
      ${context_info ? `<context>${context_info}</context>\n\n` : ''}
      
      <task>
        ${task_specification}
      </task>
      
      ${constraints && constraints.length > 0 ? `
      <constraints>
        ${constraints.map(constraint => `<constraint>${constraint}</constraint>`).join('\n')}
      </constraints>
      ` : ''}
      
      ${examples && examples.length > 0 ? `
      <examples>
        ${examples.map((example, i) => `
        <example id="${i + 1}">
          <input>${example.input}</input>
          <output>${example.output}</output>
        </example>
        `).join('')}
      </examples>
      ` : ''}
      
      ${output_format ? `
      <output_format>
        ${output_format}
      </output_format>
      ` : ''}
    </template>
  </template_structure>
  
  <validation_rules>
    <rule type="structural">Must use properly nested XML tags</rule>
    <rule type="semantic">Tag names must be semantically meaningful</rule>
    <rule type="effectiveness">Should improve parsing accuracy by >15%</rule>
  </validation_rules>
  
  <usage_metrics>
    <metric name="token_efficiency">0.85 (good efficiency with clear structure)</metric>
    <metric name="success_rate">0.92 (excellent for complex prompts)</metric>
    <metric name="consistency">0.90 (highly consistent structure)</metric>
  </usage_metrics>
</pattern_template>
```

## Template Usage System

### Template Selection Algorithm

```xml
<template_selection>
  <input_analysis>
    <task_complexity>Analyze problem complexity level</task_complexity>
    <domain_context>Identify subject matter domain</domain_context>
    <output_requirements>Determine format and structure needs</output_requirements>
    <performance_constraints>Consider token and time limitations</performance_constraints>
  </input_analysis>
  
  <pattern_matching>
    <reasoning_indicators>Keywords suggesting need for logical reasoning</reasoning_indicators>
    <learning_indicators>Presence of examples or pattern recognition needs</learning_indicators>
    <structural_indicators>Complex requirements needing organization</structural_indicators>
    <optimization_indicators>Performance or efficiency constraints</optimization_indicators>
  </pattern_matching>
  
  <template_ranking>
    <effectiveness_score>Pattern's historical success rate for similar tasks</effectiveness_score>
    <efficiency_score>Token usage vs. output quality ratio</efficiency_score>
    <complexity_match>How well pattern complexity matches task needs</complexity_match>
    <context_fit>Alignment with domain and situational requirements</context_fit>
  </template_ranking>
</template_selection>
```

### Template Customization Engine

```xml
<customization_engine>
  <variable_population>
    <automatic_extraction>Extract values from user input</automatic_extraction>
    <intelligent_defaults>Apply context-appropriate defaults</intelligent_defaults>
    <validation_checks>Ensure all required variables are populated</validation_checks>
  </variable_population>
  
  <dynamic_adaptation>
    <length_optimization>Adjust template verbosity based on constraints</length_optimization>
    <style_matching>Adapt tone and style to context</style_matching>
    <domain_specialization>Include domain-specific terminology and concepts</domain_specialization>
  </dynamic_adaptation>
  
  <quality_assurance>
    <structural_validation>Verify template structure integrity</structural_validation>
    <semantic_validation>Check logical consistency of populated content</semantic_validation>
    <effectiveness_prediction>Estimate likely success based on similar cases</effectiveness_prediction>
  </quality_assurance>
</customization_engine>
```

---

*These templates provide the foundation for consistent, effective prompt construction across all Claude Code framework operations.*