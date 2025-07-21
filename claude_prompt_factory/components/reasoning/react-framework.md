# ReAct: Reasoning and Acting

Implementation of the ReAct framework for interleaving reasoning traces with task-specific actions in language models for enhanced problem-solving capabilities.

## Command

`/reasoning-react`

## Purpose

Implement the ReAct (Reasoning and Acting) framework that combines verbal reasoning traces with task-specific actions, enabling language models to dynamically plan, act, and adapt based on observations in complex problem-solving scenarios.

## Parameters

```xml
<command>reasoning-react</command>
<params>
  <!-- Core ReAct Configuration -->
  <model>claude-3-opus</model>
  <max_iterations>10</max_iterations>
  <reasoning_depth>detailed</reasoning_depth>
  <action_space>flexible</action_space>
  
  <!-- Task Specification -->
  <task>
    <type>question_answering</type>
    <domain>general_knowledge</domain>
    <tools>["search", "lookup", "calculate", "verify"]</tools>
    <environment>wikipedia_knowledge_base</environment>
  </task>
  
  <!-- Reasoning Configuration -->
  <reasoning>
    <trace_verbosity>high</trace_verbosity>
    <self_reflection>enabled</self_reflection>
    <error_correction>adaptive</error_correction>
    <plan_tracking>dynamic</plan_tracking>
  </reasoning>
  
  <!-- Action Configuration -->
  <actions>
    <validation>strict</validation>
    <execution_mode>sequential</execution_mode>
    <fallback_strategy>graceful_degradation</fallback_strategy>
    <observation_processing>comprehensive</observation_processing>
  </actions>
  
  <!-- Integration Settings -->
  <integration>
    <tool_interface>unified_api</tool_interface>
    <state_management>persistent</state_management>
    <context_preservation>full_history</context_preservation>
    <parallelization>false</parallelization>
  </integration>
</params>
```

## Implementation

### ReAct Framework Architecture

#### 1. Reasoning-Action Interleaving
```yaml
react_cycle:
  thought_phase:
    - current_situation_analysis: "assess_problem_state"
    - goal_decomposition: "break_down_objectives"
    - strategy_formation: "plan_next_actions"
    - expectation_setting: "predict_outcomes"
  
  action_phase:
    - action_selection: "choose_appropriate_tool"
    - parameter_specification: "define_action_inputs"
    - execution_monitoring: "track_action_progress"
    - result_capture: "gather_observations"
  
  observation_phase:
    - result_interpretation: "analyze_action_outcomes"
    - success_evaluation: "assess_goal_progress"
    - error_detection: "identify_unexpected_results"
    - state_update: "revise_understanding"
  
  adaptation_phase:
    - strategy_adjustment: "modify_approach_if_needed"
    - plan_revision: "update_action_sequence"
    - learning_integration: "incorporate_new_knowledge"
    - continuation_decision: "determine_next_steps"
```

#### 2. Reasoning Trace Generation
```markdown
**Thought Process Documentation:**
- Explicit verbalization of reasoning steps
- Clear articulation of goals and subgoals
- Justification for action choices
- Hypothesis formation and testing
- Error analysis and correction strategies
- Progress assessment and plan adjustment
```

#### 3. Action Execution Framework
```yaml
action_execution:
  tool_integration:
    search:
      description: "Query external knowledge sources"
      parameters: ["query_string", "source_type", "result_count"]
      output_format: "structured_search_results"
    
    lookup:
      description: "Find specific information within documents"
      parameters: ["document_id", "search_term", "context_window"]
      output_format: "relevant_text_snippets"
    
    calculate:
      description: "Perform mathematical computations"
      parameters: ["expression", "precision", "units"]
      output_format: "numerical_result_with_explanation"
    
    verify:
      description: "Cross-check information accuracy"
      parameters: ["claim", "evidence_sources", "confidence_threshold"]
      output_format: "verification_result_with_confidence"
  
  execution_management:
    - parameter_validation: "ensure_valid_action_inputs"
    - error_handling: "manage_execution_failures"
    - timeout_management: "prevent_infinite_loops"
    - resource_monitoring: "track_computational_costs"
```

### Advanced ReAct Capabilities

#### Dynamic Plan Management
```yaml
planning_system:
  plan_representation:
    - hierarchical_goals: "main_objective_with_subgoals"
    - action_sequences: "ordered_steps_with_dependencies"
    - contingency_plans: "alternative_paths_for_failures"
    - success_criteria: "measurable_completion_conditions"
  
  plan_adaptation:
    - real_time_updates: "modify_plans_based_on_observations"
    - goal_prioritization: "adjust_focus_based_on_progress"
    - resource_reallocation: "optimize_effort_distribution"
    - strategy_switching: "change_approach_when_stuck"
  
  plan_tracking:
    - progress_monitoring: "track_completion_of_subgoals"
    - deviation_detection: "identify_off_track_situations"
    - bottleneck_identification: "find_blocking_issues"
    - efficiency_optimization: "improve_execution_speed"
```

#### Self-Reflection and Meta-Cognition
```yaml
meta_cognitive_abilities:
  self_monitoring:
    - reasoning_quality_assessment: "evaluate_thought_process_clarity"
    - action_effectiveness_review: "analyze_tool_usage_success"
    - bias_detection: "identify_reasoning_biases"
    - confidence_calibration: "assess_certainty_accuracy"
  
  self_correction:
    - error_identification: "detect_reasoning_mistakes"
    - assumption_questioning: "challenge_initial_beliefs"
    - alternative_generation: "explore_different_approaches"
    - strategy_refinement: "improve_problem_solving_methods"
  
  knowledge_management:
    - fact_verification: "validate_information_accuracy"
    - source_credibility: "assess_information_reliability"
    - knowledge_gaps: "identify_missing_information"
    - learning_integration: "incorporate_new_insights"
```

## Use Cases

### 1. Multi-Hop Question Answering
```xml
<scenario>
  <question>Who was the director of the movie that won the Academy Award for Best Picture in 1994?</question>
  <react_trace>
    <thought>I need to find which movie won Best Picture in 1994, then find its director</thought>
    <action>Search[Academy Award Best Picture 1994]</action>
    <observation>Forrest Gump won the Academy Award for Best Picture in 1994</observation>
    <thought>Now I need to find who directed Forrest Gump</thought>
    <action>Search[Forrest Gump director]</action>
    <observation>Forrest Gump was directed by Robert Zemeckis</observation>
    <thought>I have the complete answer now</thought>
    <action>Finish[Robert Zemeckis]</action>
  </react_trace>
</scenario>
```

### 2. Complex Problem Solving
```xml
<scenario>
  <problem>Calculate the compound interest earned on $10,000 invested at 5% annual rate for 8 years, compounded quarterly</problem>
  <react_trace>
    <thought>I need to use the compound interest formula: A = P(1 + r/n)^(nt)</thought>
    <action>Calculate[10000 * (1 + 0.05/4)^(4*8)]</action>
    <observation>Final amount = $14,888.64</observation>
    <thought>Now I need to subtract the principal to get the interest earned</thought>
    <action>Calculate[14888.64 - 10000]</action>
    <observation>Interest earned = $4,888.64</observation>
    <thought>Let me verify this calculation is correct</thought>
    <action>Verify[compound interest calculation with given parameters]</action>
    <observation>Calculation verified as correct</observation>
  </react_trace>
</scenario>
```

### 3. Research and Fact-Checking
```xml
<scenario>
  <claim>The Great Wall of China is visible from space with the naked eye</claim>
  <react_trace>
    <thought>This is a common claim that I should verify with reliable sources</thought>
    <action>Search[Great Wall China visible from space NASA astronauts]</action>
    <observation>NASA states that the Great Wall is not visible from space with naked eye</observation>
    <thought>Let me get more specific information from astronauts</thought>
    <action>Lookup[astronaut testimonies Great Wall visibility]</action>
    <observation>Multiple astronauts confirm the wall is not visible without aid</observation>
    <thought>I should verify what is actually visible from space</thought>
    <action>Search[what human-made structures visible from space naked eye]</action>
    <observation>Very few structures are visible; mainly city lights at night and large reservoirs</observation>
    <thought>The claim appears to be false based on authoritative sources</thought>
  </react_trace>
</scenario>
```

## Advanced Features

### Error Recovery and Adaptation
```yaml
error_handling:
  error_types:
    - action_failure: "tool_execution_errors"
    - reasoning_error: "logical_inconsistencies"
    - information_gap: "missing_required_data"
    - goal_confusion: "unclear_objectives"
  
  recovery_strategies:
    - retry_with_modification: "adjust_parameters_and_retry"
    - alternative_approach: "use_different_tools_or_methods"
    - goal_decomposition: "break_problem_into_smaller_parts"
    - human_assistance: "request_clarification_or_help"
  
  adaptation_mechanisms:
    - strategy_learning: "remember_successful_approaches"
    - failure_analysis: "understand_why_actions_failed"
    - pattern_recognition: "identify_recurring_challenges"
    - method_optimization: "improve_efficiency_over_time"
```

### Multi-Domain Knowledge Integration
```yaml
knowledge_domains:
  factual_knowledge:
    - historical_facts: "dates_events_people"
    - scientific_data: "formulas_constants_theories"
    - geographical_info: "locations_features_demographics"
    - cultural_information: "traditions_languages_customs"
  
  procedural_knowledge:
    - mathematical_operations: "calculation_methods"
    - logical_reasoning: "inference_patterns"
    - research_methods: "information_gathering_techniques"
    - problem_solving: "systematic_approaches"
  
  domain_integration:
    - cross_reference: "connect_information_across_domains"
    - consistency_check: "verify_information_alignment"
    - synthesis: "combine_insights_from_multiple_areas"
    - application: "apply_knowledge_to_specific_problems"
```

## Output Format

```json
{
  "react_session": {
    "session_id": "react_2024_001",
    "task_description": "Multi-hop question answering task",
    "configuration": {
      "model": "claude-3-opus",
      "max_iterations": 10,
      "tools_enabled": ["search", "lookup", "calculate", "verify"]
    },
    "execution_trace": [
      {
        "step": 1,
        "type": "thought",
        "content": "I need to break this problem down into smaller parts",
        "reasoning_quality": "clear_and_logical",
        "confidence": 0.9
      },
      {
        "step": 2,
        "type": "action",
        "tool": "search",
        "parameters": {"query": "example search query"},
        "execution_time": 1.2,
        "success": true
      },
      {
        "step": 3,
        "type": "observation",
        "content": "Search returned relevant information about...",
        "relevance_score": 0.85,
        "confidence": 0.8
      }
    ],
    "final_result": {
      "answer": "Comprehensive answer based on reasoning and actions",
      "confidence": 0.92,
      "evidence_sources": ["source1", "source2", "source3"],
      "reasoning_path": "summary_of_logical_steps",
      "actions_taken": 6,
      "total_execution_time": 15.7
    },
    "performance_metrics": {
      "task_completion": true,
      "reasoning_quality": "high",
      "action_efficiency": "good",
      "information_accuracy": "verified",
      "adaptability_demonstrated": true
    }
  }
}
```

## Research Foundation

Based on foundational ReAct research:
- **Reasoning-Acting Synergy**: Combining verbal reasoning with concrete actions
- **Interactive Problem Solving**: Dynamic adaptation based on environmental feedback
- **Tool Integration**: Seamless interface with external knowledge sources
- **Transparent Decision Making**: Interpretable reasoning traces for human understanding

## Integration Points

- Works with `/agent-swarm` for multi-agent ReAct coordination
- Combines with `/prompt-optimization` for ReAct prompt improvement
- Integrates with `/quality-review` for reasoning trace evaluation
- Supports `/research-advanced` for complex research tasks

## Advanced Configuration

### Custom Tool Development
```yaml
custom_tools:
  domain_specific:
    - medical_diagnosis: "clinical_decision_support"
    - legal_research: "case_law_analysis"
    - financial_analysis: "market_data_processing"
    - scientific_computation: "specialized_calculations"
  
  tool_chaining:
    - sequential_execution: "output_of_one_feeds_next"
    - parallel_processing: "simultaneous_tool_usage"
    - conditional_logic: "tool_selection_based_on_results"
    - feedback_loops: "iterative_refinement_cycles"
```

### Reasoning Enhancement
```yaml
reasoning_augmentation:
  cognitive_strategies:
    - analogical_reasoning: "solve_by_analogy"
    - causal_analysis: "understand_cause_effect_relationships"
    - counterfactual_thinking: "consider_alternative_scenarios"
    - metacognitive_reflection: "think_about_thinking"
  
  reasoning_validation:
    - logical_consistency: "check_for_contradictions"
    - evidence_sufficiency: "assess_support_quality"
    - bias_mitigation: "reduce_systematic_errors"
    - confidence_calibration: "accurate_uncertainty_estimation"
```

---

*This command implements the ReAct framework for synergizing reasoning and acting in language models, enabling sophisticated problem-solving through interleaved thought and action cycles.* 