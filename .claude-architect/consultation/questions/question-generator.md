---
name: generate-next-question
description: Dynamic question generation based on context and consultation flow
usage: "generate-next-question <stage> [context]"
allowed-tools: [Read, Grep, Write]
category: consultation
---

# Dynamic Question Generator - Context-Aware Question Selection

This command implements intelligent question generation for the deep discovery consultation, selecting optimal questions based on accumulated context, time constraints, and user engagement patterns.

## Core Intelligence Features

### Context-Aware Selection
- **Previous Responses**: Questions adapt based on what user has already shared
- **Information Gaps**: Prioritize questions that fill knowledge gaps
- **Smart Inference**: Skip questions when answers can be inferred from context
- **Domain Detection**: Select domain-specific questions when patterns emerge

### Adaptive Questioning Logic
- **Expertise Calibration**: Adjust question complexity to user knowledge level
- **Time Management**: Prioritize essential questions when time is limited
- **Engagement Response**: Modify depth based on user engagement level
- **Skip Intelligence**: Automatically skip redundant or inapplicable questions

## Question Generation Algorithm

### 1. Context Analysis Phase
```yaml
analyze_current_context:
  accumulated_information:
    - Review all previous responses
    - Identify information gaps
    - Check for contradictions
    - Map current understanding
  
  situational_factors:
    - Time remaining in stage/total
    - User engagement level
    - Response quality patterns
    - Technical complexity indicators
  
  inference_opportunities:
    - Repository analysis insights
    - Pattern recognition from responses
    - Domain-specific indicators
    - Team structure implications
```

### 2. Question Prioritization
```yaml
priority_calculation:
  essential_information: 40%    # Must-have for context generation
  time_efficiency: 25%         # Questions that maximize value per minute
  user_engagement: 20%         # Match user interest and energy level
  context_building: 15%        # Questions that enable better follow-ups

scoring_factors:
  information_value:
    high: "Directly impacts context generation quality"
    medium: "Improves context but not critical"
    low: "Nice to know but can be skipped"
  
  time_cost:
    quick: "Simple yes/no or short answer (30 seconds)"
    standard: "Moderate explanation needed (1-2 minutes)"
    deep: "Requires detailed discussion (3+ minutes)"
  
  engagement_match:
    technical: "For users showing technical depth"
    business: "For users focused on outcomes"
    learning: "For users in exploration mode"
```

### 3. Dynamic Question Selection
```yaml
selection_process:
  1_filter_applicable:
    - Check stage requirements
    - Verify prerequisites met
    - Apply skip conditions
    - Remove redundant questions
  
  2_apply_context:
    - Match detected patterns
    - Align with user expertise
    - Consider time constraints
    - Factor in engagement level
  
  3_select_optimal:
    - Calculate priority scores
    - Select highest value question
    - Prepare follow-up options
    - Set context for next question
```

## Implementation Examples

### Project Type Detection
```markdown
# Context: Repository shows React app with Node.js backend
# Instead of: "What type of project are you building?"
# Generated: "I can see this is a React web application with a Node.js backend - is that right?"

context_aware_adjustment:
  detected_pattern: "React + Node.js"
  question_modification: "Confirmation instead of open exploration"
  time_saved: "2-3 minutes"
  engagement_maintained: "Shows intelligent analysis"
```

### Expertise-Based Adaptation
```markdown
# Context: User mentions Docker, Kubernetes, microservices
# Standard question: "How do you handle deployment?"
# Expert version: "What's your container orchestration strategy - raw Kubernetes, managed services, or something else?"

expertise_indicators:
  - "Complex technology mentions"
  - "Architecture pattern familiarity"
  - "Advanced tooling references"
  
adaptation_strategy:
  - "Increase technical depth"
  - "Assume concept familiarity"  
  - "Focus on optimization details"
```

### Time-Constraint Management
```markdown
# Context: 8 minutes remaining, Stage 2 not started
# Normal flow: Full architecture exploration
# Time-adapted: "Quick architecture question - monolith or microservices? And what's your main stack?"

time_pressure_adaptations:
  behind_schedule:
    - "Combine related questions"
    - "Skip nice-to-have categories"
    - "Use closed vs. open questions"
    - "Offer quick mode transition"
```

## Smart Follow-up Generation

### Response-Based Follow-ups
```yaml
follow_up_patterns:
  mentions_performance:
    triggers: ["slow", "performance", "speed", "optimization"]
    follow_ups:
      - "What kind of performance issues are you seeing?"
      - "Response times, throughput, or resource usage?"
      - "Any specific performance targets or constraints?"
  
  mentions_team_challenges:
    triggers: ["team", "coordination", "consistency", "reviews"]
    follow_ups:
      - "How large is your development team?"
      - "What's the biggest coordination challenge?"
      - "How do you maintain code consistency?"
  
  mentions_scaling:
    triggers: ["scale", "growth", "users", "traffic"]
    follow_ups:
      - "What's your current scale vs. expected growth?"
      - "Where do you expect bottlenecks to emerge?"
      - "Any scaling challenges you've already faced?"
```

### Depth Calibration
```yaml
response_depth_analysis:
  detailed_technical_response:
    indicators: ["Length > 100 words", "Specific tools mentioned", "Architecture details"]
    follow_up_strategy: "Technical depth", "Advanced patterns", "Optimization focus"
  
  brief_business_response:
    indicators: ["Short answer", "Business terms", "Outcome focus"]
    follow_up_strategy: "Business impact", "Value delivery", "User benefit"
  
  learning_oriented_response:
    indicators: ["Questions in response", "Uncertainty", "Best practices requests"]
    follow_up_strategy: "Educational approach", "Best practices", "Learning resources"
```

## Context Validation System

### Understanding Confirmation
```yaml
validation_checkpoints:
  stage_transitions:
    process: "Summarize current understanding and confirm accuracy"
    example: "Let me confirm what I understand: You're building a React/Node.js SaaS platform for small businesses, with a 3-person team currently in MVP stage. Is that accurate?"
  
  information_conflicts:
    trigger: "When responses seem contradictory"
    process: "Clarify discrepancy without accusation"
    example: "Earlier you mentioned being solo, but just mentioned team coordination - could you help me understand your team structure?"
  
  confidence_drops:
    trigger: "When responses become vague or uncertain"
    process: "Pause and ensure clear communication"
    example: "I want to make sure I understand correctly - could you give me a specific example of..."
```

### Gap Identification
```yaml
information_gap_detection:
  essential_missing:
    project_type: "Must identify before technical questions"
    team_size: "Critical for workflow and coordination questions"
    development_stage: "Affects priority and complexity questions"
  
  nice_to_have_missing:
    specific_technologies: "Can be inferred or discovered later"
    exact_performance_metrics: "Not critical for initial context"
    detailed_business_rules: "Can be explored in domain stage"
```

## Quality Assurance Features

### Question Quality Metrics
```yaml
quality_indicators:
  engagement_maintenance:
    - "User provides detailed responses"
    - "Follow-up questions from user"
    - "Enthusiasm or interest in answers"
  
  information_extraction:
    - "Responses contain actionable information"
    - "Gaps in understanding are being filled"
    - "Context picture becoming clearer"
  
  time_efficiency:
    - "Questions appropriate to time remaining"
    - "No redundant information requests"
    - "Value extracted per minute spent"
```

### Failure Recovery
```yaml
recovery_strategies:
  user_confusion:
    symptoms: "Asks for clarification, uncertain responses"
    response: "Pause, provide context, simplify question, give examples"
  
  information_overload:
    symptoms: "Requests to slow down, overwhelmed responses"
    response: "Switch to quick mode, focus essentials, offer pause"
  
  time_pressure:
    symptoms: "Mentions time constraints, rushed responses"
    response: "Quick mode, essential questions only, pause option"
  
  engagement_drop:
    symptoms: "Very brief responses, seems distracted"
    response: "Check for break need, quick mode, maintain energy"
```

## Usage Examples

### Basic Question Generation
```bash
# Generate next question for Stage 1 with current context
generate-next-question 1 --context="project_type=web_app,team_size=unknown,responses=2"

# Output: "How many people are actively working on this? Solo, small team, or larger group?"
```

### Expert User Adaptation
```bash
# Generate question for technical expert in Stage 2
generate-next-question 2 --context="expertise=expert,mentions=microservices+docker"

# Output: "What's your service communication pattern - HTTP APIs, message queues, or event streaming?"
```

### Time-Constrained Generation  
```bash
# Generate question with time pressure
generate-next-question 3 --context="time_remaining=3min,mode=quick"

# Output: "Quick domain question - what are the 2-3 core business entities your system manages?"
```

## Integration with Consultation Flow

### Stage Transitions
- **Validates completion** of essential information before stage transition
- **Identifies gaps** that need filling before moving forward
- **Prepares context** for next stage based on accumulated understanding
- **Manages time** to ensure all stages get appropriate coverage

### Context Building
- **Accumulates understanding** across all questions and responses
- **Identifies patterns** that inform future question selection
- **Builds expertise profile** of user for appropriate depth calibration
- **Maintains engagement** through intelligent question variation

### Quality Control
- **Monitors understanding quality** through response analysis
- **Detects confusion** or information gaps requiring clarification
- **Adjusts questioning strategy** based on user feedback and engagement
- **Ensures comprehensive coverage** of essential information areas

This dynamic question generator ensures every minute of the consultation extracts maximum value through intelligent, context-aware questioning that adapts to the user's project, expertise level, and time constraints.