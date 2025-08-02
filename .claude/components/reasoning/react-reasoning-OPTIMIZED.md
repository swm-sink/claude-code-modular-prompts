# ReAct Reasoning Framework

**Purpose**: Combines systematic reasoning with action planning through iterative cycles of thought, action, observation, and evaluation for complex problem-solving.

**Usage**: 
- Execute iterative reasoning cycles with structured thought-action-observation patterns
- Analyze current situation and plan specific, measurable next steps
- Observe and evaluate action results to determine next iteration
- Adapt reasoning strategy based on feedback and progress assessment
- Handle complex multi-step problems through systematic decomposition

**Compatibility**: 
- **Works with**: tree-of-thoughts-framework, pattern-extraction, cognitive-architecture
- **Requires**: Complex problems requiring iterative reasoning and action
- **Conflicts**: simple-reasoning (adds unnecessary overhead for simple tasks)

**Implementation**:
```python
# Execute ReAct reasoning cycle
def react_reasoning_cycle(problem, context):
    max_iterations = 10
    current_state = context
    
    for iteration in range(max_iterations):
        # THOUGHT: Analyze current situation
        thought = analyze_situation(problem, current_state)
        
        # ACTION: Take specific, measurable action
        action = plan_next_action(thought, current_state)
        action_result = execute_action(action)
        
        # OBSERVATION: Observe and analyze results
        observation = observe_results(action_result, current_state)
        
        # EVALUATION: Assess progress and determine continuation
        evaluation = evaluate_progress(observation, problem)
        
        # Update state for next iteration
        current_state = update_state(current_state, action_result, observation)
        
        # Check if problem is solved
        if evaluation.problem_solved:
            return ReActResult(
                solution=evaluation.solution,
                iterations=iteration + 1,
                reasoning_trace=evaluation.trace
            )
    
    return ReActResult(partial_solution=current_state, iterations=max_iterations)

# Helper functions for structured reasoning
def analyze_situation(problem, state):
    return {
        "known_facts": extract_known_information(state),
        "unknowns": identify_missing_information(problem, state),
        "constraints": identify_constraints(problem, state),
        "next_step_options": generate_action_options(state)
    }
```

**Category**: reasoning | **Complexity**: high | **Time**: 1 day