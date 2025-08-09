# Consultation Flow Control System
# Interactive consultation orchestration and session management
# Purpose: Enable smooth, user-controlled 20-30 minute discovery experience

## Flow Control Overview

The consultation flow control system manages the progression through the 4-stage discovery process, providing users with complete control over pacing, depth, and navigation while ensuring comprehensive information gathering.

## Stage Progression Logic

### Linear Default Flow
```
Stage 1: Project Discovery (5-7 min)
    ↓
Stage 2: Technical Deep Dive (7-10 min)  
    ↓
Stage 3: Domain Extraction (7-10 min)
    ↓
Stage 4: Preference Learning (3-5 min)
    ↓
Synthesis & Generation Preparation
```

### Adaptive Flow Control

#### Skip Logic Intelligence
- **Detected Information**: Skip questions when repository analysis already provides answers
- **Redundant Context**: Skip areas covered in previous stages or obvious from responses
- **Time Constraints**: Prioritize essential questions when approaching time limits
- **User Expertise**: Skip basic explanations for clearly expert users

#### Depth Calibration
- **Beginner Mode**: More explanation, simpler terms, learning-focused
- **Standard Mode**: Balanced depth with context and examples
- **Expert Mode**: Technical precision, assume familiarity, efficiency-focused
- **Quick Mode**: Essential questions only, minimal exploration

### User Control Commands

#### Navigation Control
- **`skip`** - Move to next question in current stage
- **`skip stage`** - Move to next stage entirely
- **`back`** - Return to previous question for revision
- **`back stage`** - Return to previous stage for more detail
- **`review`** - Review current understanding and confirm accuracy

#### Pace Control
- **`quick mode`** - Switch to essential questions only (reduces time by 40%)
- **`deep mode`** - Comprehensive exploration with examples (increases time by 30%)
- **`standard mode`** - Default balanced approach
- **`pause`** - Save current progress and pause consultation
- **`resume`** - Continue from last checkpoint with context recap

#### Understanding Control
- **`clarify`** - Ask for clarification or more detail on current topic
- **`example`** - Provide concrete example of concept being discussed
- **`summary`** - Summarize current understanding for validation
- **`confident`** - Confirm understanding is correct, proceed confidently

## Time Management System

### Target Duration Management
- **Total Target**: 20-30 minutes
- **Stage Allocation**: 
  - Stage 1: 5-7 minutes (25-30%)
  - Stage 2: 7-10 minutes (35-40%)
  - Stage 3: 7-10 minutes (30-35%)
  - Stage 4: 3-5 minutes (10-15%)

### Overtime Handling
- **Soft Reminder (25 minutes)**: "We're at about 25 minutes. Would you like to continue in detail or switch to quick mode for the remaining stages?"
- **Gentle Guidance (30 minutes)**: "We're approaching 30 minutes. I can finish up with essential questions, or we can pause and resume later. Your preference?"
- **Hard Limit (35 minutes)**: "To respect your time, let me quickly capture the essentials for the remaining areas and move to generation."

### Time Estimation
- **Real-time Progress**: "We're about 40% through the discovery process"
- **Remaining Time**: "Approximately 12-15 minutes remaining"
- **Stage Completion**: "Stage 1 complete - 3 stages remaining, about 18-20 minutes"

## Session Management System

### Checkpoint Creation
```yaml
automatic_checkpoints:
  - stage_completion: "After each stage is fully completed"
  - ten_minute_intervals: "Every 10 minutes of consultation time"
  - significant_understanding: "When major insights are captured"
  - user_pause_request: "When user explicitly requests pause"

manual_checkpoints:
  - user_initiated: "User says 'checkpoint' or 'save progress'"
  - revision_point: "Before making significant changes to understanding"
  - uncertainty_point: "When confidence in understanding is low"
```

### State Persistence Schema
```yaml
session_state:
  consultation_id: "[unique_identifier]"
  start_time: "[timestamp]"
  last_update: "[timestamp]"
  total_elapsed: "[minutes]"
  
  current_position:
    stage: "[1-4]"
    question_flow: "[flow_name]"
    question_index: "[number]"
  
  completed_stages:
    stage_1:
      status: "complete|incomplete|skipped"
      information_captured: "[structured_data]"
      confidence_level: "[high|medium|low]"
    # ... for each stage
  
  user_preferences:
    pace_mode: "[quick|standard|deep]"
    expertise_level: "[beginner|intermediate|expert]"
    communication_style: "[formal|conversational|technical]"
  
  accumulated_understanding:
    project_foundation: "[structured_summary]"
    technical_architecture: "[structured_summary]"  
    domain_knowledge: "[structured_summary]"
    team_preferences: "[structured_summary]"
```

### Resume Capability
```yaml
resume_process:
  context_restoration:
    - "Load complete session state"
    - "Reconstruct conversation history"
    - "Restore current understanding"
    - "Identify next logical step"
  
  user_reorientation:
    - "Welcome back message with time elapsed"
    - "Summary of information captured so far"  
    - "Confidence check on current understanding"
    - "Options for how to proceed"
  
  continuation_options:
    - "Continue from exact pause point"
    - "Review and revise previous stages"
    - "Skip to specific stage or topic"
    - "Switch to different pace mode"
```

## Quality Control System

### Understanding Validation
```yaml
validation_checkpoints:
  stage_transitions:
    trigger: "Before moving to next stage"
    process: "Summarize understanding, confirm accuracy, identify gaps"
    
  confidence_monitoring:
    high_confidence: "Proceed smoothly with standard follow-ups"
    medium_confidence: "Add clarifying questions, confirm understanding"
    low_confidence: "Stop, ask for clarification, validate before proceeding"
    
  information_completeness:
    essential_captured: "All must-have information for stage obtained"  
    nice_to_have_gaps: "Identify and optionally pursue additional context"
    critical_missing: "Stop and gather essential missing information"
```

### Adaptive Questioning
```yaml
dynamic_adjustments:
  based_on_responses:
    detailed_answers: "Reduce follow-up questions, increase depth"
    brief_answers: "Add clarifying questions, provide examples"
    expert_indicators: "Increase technical depth, reduce explanations"
    beginner_indicators: "Add context, define terms, provide examples"
    
  based_on_time:
    ahead_of_schedule: "Add depth, explore interesting tangents"
    on_schedule: "Maintain standard pace and depth"
    behind_schedule: "Focus on essentials, reduce optional exploration"
    
  based_on_engagement:
    high_engagement: "Continue current approach, explore depth"
    medium_engagement: "Add examples, make more interactive"
    low_engagement: "Switch to quicker pace, check if pause needed"
```

## Error Handling and Recovery

### Common Flow Issues
```yaml
user_confusion:
  symptoms: "Unclear responses, requests for clarification"
  response: "Pause, provide context, offer examples, simplify question"
  
unclear_answers:
  symptoms: "Ambiguous responses, multiple interpretations"
  response: "Ask for clarification, provide specific examples, confirm understanding"
  
information_overload:
  symptoms: "User overwhelm, requests to slow down"
  response: "Switch to quick mode, focus on essentials, offer to pause"
  
time_pressure:
  symptoms: "User mentions time constraints"
  response: "Offer quick mode, prioritize essentials, provide pause option"
```

### Recovery Strategies
- **Clarification Loop**: Stop progression, clarify current topic, validate understanding
- **Mode Switch**: Change from current mode (quick/standard/deep) to better fit user needs
- **Backtrack**: Return to previous stage or question for better foundation
- **Pause and Resume**: Save progress, allow user to return when ready
- **Skip Forward**: Move past difficult areas, return if time allows

## Integration with Other Systems

### Context Accumulation
As information is gathered, the flow control system continuously builds the project understanding that will be passed to the context generation engine.

### Agent Factory Preparation  
User responses and engagement patterns inform agent specialization requirements.

### Command Generation Readiness
Workflow patterns and preferences guide command type and structure recommendations.

## Success Metrics and Monitoring

### Flow Effectiveness
- **Completion Rate**: Percentage of consultations completed successfully
- **Time Efficiency**: Average time per stage and total consultation
- **User Satisfaction**: Ratings for flow control and user experience
- **Information Quality**: Completeness and accuracy of captured information

### User Control Usage
- **Navigation Commands**: Frequency of skip, back, review usage
- **Pace Adjustments**: How often users change modes
- **Pause/Resume**: Success rate of session management
- **Understanding Checks**: Effectiveness of validation checkpoints

This flow control system ensures that every consultation is user-controlled, time-efficient, and comprehensive while maintaining high engagement and producing high-quality input for the context generation phase.