# Prompt Pattern Library

## Overview

A comprehensive library of proven prompt engineering patterns for Claude Code framework. This module provides systematic approaches to prompt construction, pattern recognition, and effectiveness optimization.

## Framework Integration

<delegation_reference>
  This module implements prompt pattern orchestration for all Claude Code commands
</delegation_reference>

## Core Pattern Categories

### 1. Reasoning Patterns
- **Chain-of-Thought (CoT)** - Step-by-step reasoning with explicit logic steps
- **Self-Consistency** - Multiple reasoning paths with majority voting
- **Tree-of-Thought (ToT)** - Parallel exploration with backtracking capability
- **Zero-Shot-CoT** - Implicit reasoning activation with "Let's think step-by-step"

### 2. Learning Patterns
- **Few-Shot** - Example-based learning with 3-5 demonstrations
- **Zero-Shot** - Task-only instruction without examples
- **One-Shot** - Single example guidance for pattern recognition
- **Meta-Learning** - Learning to learn with structural focus

### 3. Structural Patterns
- **XML-Structured** - Hierarchical organization with semantic tags
- **Template-Based** - Reusable formats with variable placeholders
- **Role-Based** - Persona assignment for domain expertise
- **Context-Aware** - Situational adaptation with environmental factors

### 4. Optimization Patterns
- **Token-Efficient** - Minimal token usage with maximum information density
- **Parallel-Processing** - Concurrent execution for multiple tasks
- **Progressive-Refinement** - Iterative improvement with feedback loops
- **Error-Recovery** - Graceful failure handling with fallback strategies

## Pattern Library Structure

<pattern_library>
  <categories>
    <category name="reasoning">Chain-of-Thought, Self-Consistency, Tree-of-Thought</category>
    <category name="learning">Few-Shot, Zero-Shot, One-Shot, Meta-Learning</category>
    <category name="structural">XML-Structured, Template-Based, Role-Based</category>
    <category name="optimization">Token-Efficient, Parallel-Processing, Progressive-Refinement</category>
  </categories>
  
  <effectiveness_metrics>
    <metric name="accuracy">Pattern success rate on target tasks</metric>
    <metric name="efficiency">Token usage vs. outcome quality</metric>
    <metric name="consistency">Reproducibility across contexts</metric>
    <metric name="robustness">Performance under edge cases</metric>
  </effectiveness_metrics>
  
  <pattern_matching>
    <system>Automatic pattern detection from user input</system>
    <recommendation>Context-aware pattern suggestions</recommendation>
    <validation>Pattern effectiveness verification</validation>
  </pattern_matching>
</pattern_library>

## Pattern Template Structure

Each pattern follows a standardized template:

```xml
<pattern_template>
  <pattern_id>unique_identifier</pattern_id>
  <pattern_name>Human-readable name</pattern_name>
  <pattern_category>Primary classification</pattern_category>
  <pattern_type>Reasoning|Learning|Structural|Optimization</pattern_type>
  <effectiveness_score>0.0-1.0</effectiveness_score>
  <use_cases>
    <use_case>Specific application scenario</use_case>
  </use_cases>
  <implementation>
    <template>Pattern template with placeholders</template>
    <variables>Required and optional variables</variables>
    <constraints>Pattern-specific requirements</constraints>
  </implementation>
  <examples>
    <example>
      <context>Usage scenario</context>
      <input>Pattern application</input>
      <output>Expected result</output>
    </example>
  </examples>
  <anti_patterns>
    <anti_pattern>Common misuses to avoid</anti_pattern>
  </anti_patterns>
  <metrics>
    <metric name="accuracy">Pattern-specific accuracy</metric>
    <metric name="efficiency">Token efficiency rating</metric>
    <metric name="consistency">Reproducibility score</metric>
  </metrics>
</pattern_template>
```

## Pattern Recommendation System

<recommendation_engine>
  <input_analysis>
    <task_complexity>Simple|Medium|Complex</task_complexity>
    <domain_context>Technical|Creative|Analytical</domain_context>
    <output_requirements>Format|Structure|Quality</output_requirements>
    <constraints>Token|Time|Accuracy</constraints>
  </input_analysis>
  
  <pattern_selection>
    <primary_pattern>Best matching pattern</primary_pattern>
    <secondary_patterns>Alternative approaches</secondary_patterns>
    <combination_patterns>Multi-pattern orchestration</combination_patterns>
  </pattern_selection>
  
  <effectiveness_prediction>
    <accuracy_estimate>Expected success rate</accuracy_estimate>
    <efficiency_estimate>Token usage projection</efficiency_estimate>
    <risk_assessment>Potential failure modes</risk_assessment>
  </effectiveness_prediction>
</recommendation_engine>

## Pattern Validation Rules

<validation_system>
  <structural_validation>
    <rule>Pattern must follow standard template</rule>
    <rule>All required fields must be present</rule>
    <rule>Examples must be complete and accurate</rule>
  </structural_validation>
  
  <effectiveness_validation>
    <rule>Pattern must achieve >70% accuracy on test cases</rule>
    <rule>Token efficiency must be within acceptable range</rule>
    <rule>Consistency must be >80% across contexts</rule>
  </effectiveness_validation>
  
  <anti_pattern_validation>
    <rule>Pattern must not contain known anti-patterns</rule>
    <rule>Pattern must not conflict with existing patterns</rule>
    <rule>Pattern must handle edge cases gracefully</rule>
  </anti_pattern_validation>
</validation_system>

## Pattern Evolution System

<evolution_tracking>
  <versioning>
    <version_format>Major.Minor.Patch (semantic versioning)</version_format>
    <change_tracking>All modifications logged with rationale</change_tracking>
    <backward_compatibility>Ensure existing implementations continue working</backward_compatibility>
  </versioning>
  
  <performance_monitoring>
    <continuous_assessment>Real-time effectiveness tracking</continuous_assessment>
    <a_b_testing>Pattern variant comparison</a_b_testing>
    <user_feedback>Community-driven improvements</user_feedback>
  </performance_monitoring>
  
  <pattern_lifecycle>
    <development>Pattern creation and initial testing</development>
    <validation>Comprehensive testing and verification</validation>
    <deployment>Production release with monitoring</deployment>
    <maintenance>Ongoing optimization and updates</maintenance>
    <deprecation>Graceful retirement of obsolete patterns</deprecation>
  </pattern_lifecycle>
</evolution_tracking>

## Integration Points

### Command Integration
- **Auto** - Intelligent pattern selection
- **Task** - Task-specific pattern application
- **Query** - Research-oriented patterns
- **Swarm** - Multi-agent pattern coordination

### Module Integration
- **Quality** - Pattern effectiveness validation
- **Security** - Pattern safety verification
- **Performance** - Pattern efficiency optimization
- **Development** - Pattern application in workflows

## Usage Guidelines

### Getting Started
1. Identify task requirements and constraints
2. Use pattern recommendation system
3. Apply selected pattern with proper templates
4. Validate effectiveness and adjust as needed

### Best Practices
- Always validate patterns before production use
- Monitor effectiveness metrics continuously
- Combine patterns strategically for complex tasks
- Document pattern customizations for reproducibility

### Common Pitfalls
- Over-engineering simple tasks with complex patterns
- Ignoring context-specific requirements
- Failing to validate pattern effectiveness
- Mixing incompatible pattern types

## Future Extensions

### Planned Features
- Machine learning-based pattern optimization
- Community pattern contribution system
- Cross-model pattern compatibility
- Advanced pattern combination algorithms

### Research Areas
- Pattern emergence detection
- Automated pattern synthesis
- Cross-domain pattern transfer
- Pattern effectiveness prediction

## Detailed Pattern Documentation

### Chain-of-Thought (CoT) Pattern

<pattern_definition>
  <pattern_id>cot-001</pattern_id>
  <pattern_name>Chain-of-Thought Reasoning</pattern_name>
  <pattern_category>reasoning</pattern_category>
  <effectiveness_score>0.85</effectiveness_score>
  
  <description>
    Enables step-by-step logical reasoning by explicitly requesting intermediate steps.
    Particularly effective for mathematical problems, logical puzzles, and complex analysis.
  </description>
  
  <template>
    <instructions>
      [Task description]
      
      Let's work through this step-by-step:
      1. [Step 1 description]
      2. [Step 2 description]
      3. [Continue as needed]
      
      Please show your reasoning for each step.
    </instructions>
  </template>
  
  <best_practices>
    - Use explicit step indicators (1, 2, 3 or First, Next, Finally)
    - Request reasoning justification for each step
    - Include verification step at the end
    - Works best with logical or mathematical problems
  </best_practices>
  
  <anti_patterns>
    - Don't use for simple tasks that don't require reasoning
    - Avoid when speed is more important than accuracy
    - Don't chain too many steps (limit to 5-7 for clarity)
  </anti_patterns>
</pattern_definition>

### Tree-of-Thought (ToT) Pattern

<pattern_definition>
  <pattern_id>tot-001</pattern_id>
  <pattern_name>Tree-of-Thought Exploration</pattern_name>
  <pattern_category>reasoning</pattern_category>
  <effectiveness_score>0.78</effectiveness_score>
  
  <description>
    Enables parallel exploration of multiple reasoning paths with ability to backtrack.
    Excellent for creative problem-solving and scenarios with multiple valid approaches.
  </description>
  
  <template>
    <instructions>
      [Problem statement]
      
      Let's explore multiple approaches:
      
      Approach A: [First approach]
      - Reasoning: [Logic for this path]
      - Pros: [Advantages]
      - Cons: [Limitations]
      
      Approach B: [Second approach]
      - Reasoning: [Logic for this path]
      - Pros: [Advantages]
      - Cons: [Limitations]
      
      Approach C: [Third approach]
      - Reasoning: [Logic for this path]
      - Pros: [Advantages]
      - Cons: [Limitations]
      
      Now let's evaluate and select the best path or combine approaches.
    </instructions>
  </template>
  
  <best_practices>
    - Generate 3-5 distinct approaches
    - Evaluate each path independently
    - Allow for hybrid solutions
    - Include explicit comparison criteria
  </best_practices>
</pattern_definition>

### XML-Structured Pattern

<pattern_definition>
  <pattern_id>xml-001</pattern_id>
  <pattern_name>XML-Structured Organization</pattern_name>
  <pattern_category>structural</pattern_category>
  <effectiveness_score>0.92</effectiveness_score>
  
  <description>
    Uses XML-like tags to create clear hierarchical structure and prevent information mixing.
    Highly effective for complex prompts with multiple components.
  </description>
  
  <template>
    <instructions>
      <context>
        [Background information and situational context]
      </context>
      
      <task>
        [Specific task description and requirements]
      </task>
      
      <constraints>
        [Limitations, requirements, and boundaries]
      </constraints>
      
      <examples>
        <example>
          <input>[Example input]</input>
          <output>[Expected output]</output>
        </example>
      </examples>
      
      <output_format>
        [Specific format requirements for the response]
      </output_format>
    </instructions>
  </template>
  
  <best_practices>
    - Use semantic tag names that clearly indicate content purpose
    - Maintain consistent tag naming throughout the prompt
    - Nest tags logically for hierarchical organization
    - Reference tag names when explaining instructions
  </best_practices>
</pattern_definition>

### Few-Shot Learning Pattern

<pattern_definition>
  <pattern_id>few-shot-001</pattern_id>
  <pattern_name>Few-Shot Example Learning</pattern_name>
  <pattern_category>learning</pattern_category>
  <effectiveness_score>0.89</effectiveness_score>
  
  <description>
    Provides 3-5 high-quality examples to establish patterns and expectations.
    Extremely effective for tasks requiring specific format or style.
  </description>
  
  <template>
    <instructions>
      [Task description]
      
      Here are some examples:
      
      Example 1:
      Input: [Input 1]
      Output: [Output 1]
      
      Example 2:
      Input: [Input 2]
      Output: [Output 2]
      
      Example 3:
      Input: [Input 3]
      Output: [Output 3]
      
      Now apply the same pattern to:
      Input: [New input]
      Output:
    </instructions>
  </template>
  
  <best_practices>
    - Use 3-5 diverse, high-quality examples
    - Ensure examples cover edge cases
    - Maintain consistent format across examples
    - Choose examples that clearly demonstrate the pattern
  </best_practices>
</pattern_definition>

### Role-Based Pattern

<pattern_definition>
  <pattern_id>role-001</pattern_id>
  <pattern_name>Role-Based Expertise</pattern_name>
  <pattern_category>structural</pattern_category>
  <effectiveness_score>0.72</effectiveness_score>
  
  <description>
    Assigns specific persona or expertise domain to guide response style and depth.
    Effectiveness varies by task complexity and domain specificity.
  </description>
  
  <template>
    <instructions>
      You are a [specific role/expert] with [relevant experience/credentials].
      
      [Task description tailored to the role]
      
      Please respond as this expert would, considering:
      - [Domain-specific knowledge]
      - [Professional standards]
      - [Typical concerns/priorities]
    </instructions>
  </template>
  
  <best_practices>
    - Use specific, well-defined roles rather than generic ones
    - Include relevant context about the role's expertise
    - Align task complexity with role's expected knowledge
    - Consider that effectiveness may be limited for factual tasks
  </best_practices>
  
  <anti_patterns>
    - Avoid overly broad or generic roles
    - Don't rely solely on role for complex reasoning tasks
    - Avoid roles that might introduce bias
  </anti_patterns>
</pattern_definition>

### Self-Consistency Pattern

<pattern_definition>
  <pattern_id>consistency-001</pattern_id>
  <pattern_name>Self-Consistency Validation</pattern_name>
  <pattern_category>reasoning</pattern_category>
  <effectiveness_score>0.81</effectiveness_score>
  
  <description>
    Generates multiple reasoning paths and uses majority voting or consistency checking.
    Excellent for increasing confidence in complex reasoning tasks.
  </description>
  
  <template>
    <instructions>
      [Problem statement]
      
      Let's solve this problem using multiple approaches to verify consistency:
      
      Solution Path 1:
      [First reasoning approach]
      Result: [Answer 1]
      
      Solution Path 2:
      [Second reasoning approach]
      Result: [Answer 2]
      
      Solution Path 3:
      [Third reasoning approach]
      Result: [Answer 3]
      
      Consistency Check:
      - Compare all results
      - Identify any discrepancies
      - Determine the most reliable answer
      - Explain why this answer is most trustworthy
    </instructions>
  </template>
  
  <best_practices>
    - Use 3-5 different reasoning approaches
    - Look for convergence in results
    - Explicitly address any discrepancies
    - Weight results based on reasoning quality
  </best_practices>
</pattern_definition>

---

*This module provides the foundation for systematic prompt engineering within the Claude Code framework, enabling consistent, effective, and optimized AI interactions.*