# Create Step-by-Step Plan

**Purpose**: Formulate detailed, logical implementation plans with clear actions, expected outcomes, and risk considerations before making changes.

**Usage**: 
- Break down complex tasks into clear, sequential steps
- Define specific actions and expected outcomes for each step
- Account for potential risks, edge cases, and dependencies
- Create comprehensive plans that other developers can execute
- Present plans in structured, numbered format for clarity

**Compatibility**: 
- **Works with**: task-planning, project-planning, workflow-coordinator, task-execution
- **Requires**: Complex tasks or projects requiring systematic planning
- **Conflicts**: None (universal planning utility)

**Implementation**:
```python
# Step-by-step plan creation
def create_implementation_plan(task_description, requirements, constraints=None):
    plan = StepByStepPlan(task_description)
    
    # 1. Analyze task complexity and scope
    analysis = analyze_task_complexity(task_description, requirements)
    
    # 2. Break down into logical phases
    phases = decompose_into_phases(analysis)
    
    # 3. Create detailed steps for each phase
    for phase in phases:
        steps = create_phase_steps(phase, requirements)
        
        for step in steps:
            # Define action and expected outcome
            action = define_specific_action(step)
            outcome = define_expected_outcome(step)
            risks = identify_potential_risks(step)
            dependencies = identify_dependencies(step)
            
            plan.add_step(
                action=action,
                outcome=outcome,
                risks=risks,
                dependencies=dependencies,
                estimated_time=estimate_completion_time(step)
            )
    
    # 4. Validate plan completeness
    plan.validate_completeness(requirements)
    
    return plan

# Plan presentation formatting
def format_plan_for_presentation(plan):
    formatted_plan = f"""
# Implementation Plan: {plan.title}

## Overview
- **Total Steps**: {len(plan.steps)}
- **Estimated Duration**: {plan.total_estimated_time}
- **Complexity Level**: {plan.complexity_level}

## Detailed Steps

"""
    
    for i, step in enumerate(plan.steps, 1):
        formatted_plan += f"""
### Step {i}: {step.action}

**Action**: {step.action}
**Expected Outcome**: {step.outcome}
**Estimated Time**: {step.estimated_time}

**Dependencies**: {', '.join(step.dependencies) if step.dependencies else 'None'}
**Potential Risks**: {', '.join(step.risks) if step.risks else 'None'}

**Validation Criteria**:
- {step.validation_criteria}

---
"""
    
    formatted_plan += f"""
## Risk Mitigation
{plan.risk_mitigation_strategies}

## Success Criteria
{plan.success_criteria}
"""
    
    return formatted_plan

# Plan validation and refinement
def validate_plan_quality(plan):
    quality_metrics = {
        'clarity': assess_step_clarity(plan.steps),
        'completeness': assess_plan_completeness(plan),
        'feasibility': assess_implementation_feasibility(plan),
        'risk_coverage': assess_risk_coverage(plan)
    }
    
    overall_quality = sum(quality_metrics.values()) / len(quality_metrics)
    
    if overall_quality < 0.8:
        suggestions = generate_improvement_suggestions(quality_metrics)
        return PlanValidation(passed=False, suggestions=suggestions)
    
    return PlanValidation(passed=True, quality_score=overall_quality)
```

**Category**: planning | **Complexity**: simple | **Time**: 1 hour