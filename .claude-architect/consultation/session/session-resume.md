# Session Resume Logic
# Intelligent resume functionality for deep discovery consultation
# Purpose: Seamless continuation from saved session state
# Version: 1.0 - Production Session Resume System

---
name: consultation-session-resume
description: Intelligent resume functionality with context reconstruction and warm-up
usage: "/consultation-session-resume [session-id] [options]"
allowed-tools: [Read, Write, Edit, LS]
category: consultation
---

# Session Resume System

## Core Resume Process

### Command: `/resume-consultation`
**Purpose**: Intelligently resume consultation from saved session state

**Usage Patterns**:
```
/resume-consultation [session-id]
/resume-consultation [session-name-pattern]
/resume-consultation --interactive
/resume-consultation --quick-start

Examples:
/resume-consultation 550e8400-e29b-41d4-a716-446655440000
/resume-consultation "React E-commerce"
/resume-consultation --interactive  # Choose from available sessions
/resume-consultation --quick-start   # Skip warm-up, go directly to next question
```

## Context Reconstruction Process

### Phase 1: Session Loading and Validation

**Step 1: Session Discovery and Loading**
```yaml
session_loading:
  discovery_methods:
    by_id: "Direct UUID lookup"
    by_name: "Pattern matching on session names"
    interactive: "Present available sessions for selection"
    recent: "Default to most recent session"
    
  validation_checks:
    file_integrity: "Verify JSON structure and completeness"
    schema_version: "Check compatibility with current schema"
    timestamp_validity: "Ensure session not corrupted by age"
    required_fields: "Verify all critical fields present"
    
  error_handling:
    file_not_found: "Offer session discovery or list available"
    corrupted_data: "Attempt backup recovery or graceful degradation"
    version_mismatch: "Apply migration or offer compatibility mode"
    permission_denied: "Guide user through access resolution"
```

**Step 2: State Integrity Verification**
```yaml
integrity_verification:
  consistency_checks:
    stage_progression: "Verify logical stage sequence"
    time_coherence: "Check time tracking makes sense"
    context_alignment: "Ensure accumulated context is coherent"
    progress_validity: "Validate progress percentages and counts"
    
  data_quality_assessment:
    confidence_scores: "Verify confidence scores are reasonable"
    completeness_metrics: "Check information completeness indicators"
    response_consistency: "Validate response patterns and quality"
    gap_analysis: "Identify and validate information gaps"
    
  recovery_actions:
    minor_inconsistencies: "Log warnings but continue"
    major_inconsistencies: "Offer correction options"
    critical_corruption: "Fallback to backup or manual recovery"
```

### Phase 2: Context Reconstruction

**Step 3: Project Understanding Reconstruction**
```yaml
context_reconstruction:
  foundation_rebuild:
    project_identity:
      - "Rebuild project type and domain understanding"
      - "Restore team size and structure context"
      - "Reconstruct development stage and goals"
      - "Restore expertise level calibration"
      
    technical_architecture:
      - "Rebuild technology stack understanding"
      - "Restore framework and architecture patterns"
      - "Reconstruct development workflow context"
      - "Restore performance and deployment understanding"
      
    domain_expertise:
      - "Rebuild business entity and terminology knowledge"
      - "Restore workflow and user journey understanding"
      - "Reconstruct business rule and compliance context"
      - "Restore integration and data relationship knowledge"
      
    preferences_style:
      - "Rebuild coding standards and style preferences"
      - "Restore communication and documentation preferences"
      - "Reconstruct tool and workflow preferences"
      - "Restore team convention understanding"
```

**Step 4: Consultation State Restoration**
```yaml
state_restoration:
  position_setting:
    current_location:
      - "Set current stage and substage"
      - "Position at exact question index"
      - "Restore question flow context"
      - "Prepare next question sequence"
      
    progress_restoration:
      - "Restore completion percentages"
      - "Rebuild time tracking state"
      - "Restore quality metrics"
      - "Reconstruct user interaction patterns"
      
  adaptation_recalibration:
    expertise_level: "Restore detected expertise calibration"
    communication_style: "Rebuild communication adaptation"
    pace_preferences: "Restore pace and depth settings"
    skip_logic: "Rebuild intelligent skip patterns"
```

## Warm-Up and Re-engagement

### Phase 3: Session Warm-Up Process

**Step 5: Progress Summary Presentation**
```yaml
progress_summary:
  summary_components:
    session_overview:
      template: |
        Welcome back! Let's continue your deep discovery consultation.
        
        📊 **Session Progress**:
        • Started: {session_start_date}
        • Progress: {overall_completion}% complete
        • Time invested: {elapsed_time} minutes
        • Quality score: {quality_score}% ({quality_rating})
        
        🎯 **What we've discovered about your project**:
        {key_discoveries_summary}
        
    stage_progress_detail:
      template: |
        📈 **Stage-by-Stage Progress**:
        
        ✅ Stage 1: Project Discovery ({stage_1_completion}%)
           Key insights: {stage_1_key_insights}
           
        {current_stage_status} Stage {current_stage_number}: {current_stage_name} ({current_stage_completion}%)
           Progress: {current_stage_progress_detail}
           Next: {next_questions_preview}
           
        {remaining_stages_preview}
        
    confidence_and_gaps:
      template: |
        🔍 **Understanding Quality**:
        • Overall confidence: {overall_confidence}%
        • Strongest areas: {high_confidence_areas}
        • Areas to strengthen: {improvement_opportunities}
        
        ⏱️ **Time Estimate**: About {estimated_remaining} minutes remaining
```

**Step 6: Context Validation with User**
```yaml
context_validation:
  validation_questions:
    accuracy_check: |
      "Does this summary accurately capture where we left off and what 
      we've learned about your project so far?"
      
    change_detection: |
      "Have there been any significant changes to your project since our 
      last session that I should know about?"
      
    goal_alignment: |
      "Are we still on the right track for what you want to achieve with 
      this Claude setup?"
      
    preference_confirmation: |
      "Any changes to your preferences for pace, depth, or communication 
      style since we last talked?"
      
  validation_responses:
    full_agreement: "Perfect! Let's continue exactly where we left off."
    minor_updates: "Let me capture those updates and then we'll continue."
    significant_changes: "Let me adjust our understanding and then proceed."
    major_revision: "Let's take a moment to revise our approach."
```

### Phase 4: Seamless Continuation

**Step 7: Position Confirmation and Next Steps**
```yaml
continuation_setup:
  position_confirmation:
    current_focus: |
      "We were in the middle of {current_stage_name}, specifically 
      exploring {current_substage}. Our next question focuses on 
      {next_question_topic}."
      
    context_bridge: |
      "Based on what you've told me about {relevant_context}, I'd like 
      to understand {next_question_focus} to complete our understanding 
      of {current_area}."
      
  transition_options:
    direct_continuation: |
      "Ready to continue with the next question?"
      
    brief_review: |
      "Would you like a quick review of this stage's focus before continuing?"
      
    modify_approach: |
      "Any adjustments to our approach before we continue?"
      
    skip_ahead: |
      "Feel confident about this area and want to skip ahead?"
```

## Resume Intelligence Features

### Adaptive Resume Strategies

**Time-Based Adaptations**
```yaml
time_adaptive_resume:
  recent_session:  # Within 2 hours
    approach: "quick_reconnect"
    warm_up: "minimal"
    context_check: "brief"
    assumption: "high_context_retention"
    
  same_day_session:  # Within 24 hours
    approach: "standard_warm_up"
    warm_up: "comprehensive_summary"
    context_check: "moderate"
    assumption: "good_context_retention"
    
  next_day_session:  # 1-3 days
    approach: "full_context_rebuild"
    warm_up: "detailed_summary"
    context_check: "thorough"
    assumption: "moderate_context_retention"
    
  long_gap_session:  # 4+ days
    approach: "comprehensive_reengagement"
    warm_up: "complete_project_review"
    context_check: "validation_required"
    assumption: "limited_context_retention"
```

**Progress-Based Adaptations**
```yaml
progress_adaptive_resume:
  early_stage_resume:  # <25% complete
    focus: "foundation_reinforcement"
    approach: "ensure_solid_understanding"
    validation: "confirm_project_basics"
    
  mid_stage_resume:  # 25-75% complete
    focus: "momentum_maintenance" 
    approach: "bridge_to_next_questions"
    validation: "spot_check_understanding"
    
  late_stage_resume:  # >75% complete
    focus: "completion_acceleration"
    approach: "efficient_final_push"
    validation: "confirm_readiness_for_completion"
```

### Quality-Based Resume Logic

**Confidence Score Adaptations**
```yaml
confidence_based_resume:
  high_confidence_session:  # >80% confidence
    warm_up: "brief_progress_review"
    validation: "minimal_spot_checking"
    approach: "trust_accumulated_context"
    acceleration: "enable_quick_mode_options"
    
  medium_confidence_session:  # 60-80% confidence
    warm_up: "standard_progress_review"
    validation: "moderate_context_checking"
    approach: "balanced_verification"
    acceleration: "standard_pacing"
    
  low_confidence_session:  # <60% confidence
    warm_up: "comprehensive_review"
    validation: "thorough_context_verification"
    approach: "rebuild_confidence_first"
    acceleration: "careful_pacing_with_validation"
```

## Resume Error Handling

### Common Resume Scenarios

**Scenario 1: Incomplete Session Data**
```yaml
incomplete_data_handling:
  missing_critical_fields:
    detection: "Check for required fields in session state"
    response: "Graceful degradation with user notification"
    recovery: "Offer to continue with reduced context"
    
  partial_stage_completion:
    detection: "Stage marked in-progress but no current question"
    response: "Determine appropriate restart point within stage"
    recovery: "Brief review and position confirmation"
    
  orphaned_progress:
    detection: "Progress indicators inconsistent with actual data"
    response: "Recalculate based on available information"
    recovery: "Present corrected progress and continue"
```

**Scenario 2: Context Inconsistencies**
```yaml
context_inconsistency_handling:
  contradictory_information:
    detection: "Scan for logical inconsistencies in accumulated context"
    response: "Flag inconsistencies for user verification"
    recovery: "Allow user to clarify and correct"
    
  outdated_information:
    detection: "Information that seems out of date based on new responses"
    response: "Query user about potential changes"
    recovery: "Update context with current information"
    
  incomplete_understanding:
    detection: "Major gaps in critical areas"
    response: "Acknowledge gaps and prioritize filling them"
    recovery: "Strategic questions to address gaps efficiently"
```

**Scenario 3: User Context Loss**
```yaml
user_context_loss_handling:
  user_forgot_session:
    detection: "User responses indicate lost context"
    response: "Provide gentle reminder and session summary"
    recovery: "Rebuild user understanding before continuing"
    
  project_changes:
    detection: "User indicates significant project changes"
    response: "Acknowledge changes and assess impact"
    recovery: "Update session state with new information"
    
  different_user:
    detection: "Response patterns suggest different user"
    response: "Confirm user identity and context"
    recovery: "Adjust communication style if needed"
```

## Integration with Consultation Flow

### Seamless Integration Points

**Question Framework Integration**
```yaml
question_framework_integration:
  question_sequencing:
    resume_point: "Continue from exact question in sequence"
    skip_logic: "Apply intelligent skips based on new context"
    follow_up_chains: "Resume follow-up sequences appropriately"
    
  adaptive_questioning:
    expertise_recalibration: "Adjust questions based on resume context"
    depth_adjustment: "Modify depth based on time and engagement"
    context_awareness: "Use accumulated context in question framing"
```

**Progress Tracking Integration**  
```yaml
progress_tracking_integration:
  time_recalculation:
    elapsed_adjustment: "Account for gap between sessions"
    pace_recalibration: "Adjust pace based on resume context"
    estimate_updates: "Recalculate remaining time estimates"
    
  quality_continuity:
    confidence_restoration: "Restore confidence tracking"
    gap_assessment: "Re-evaluate information gaps"
    quality_monitoring: "Continue quality score tracking"
```

This intelligent session resume system ensures that users can pause and continue their deep discovery consultation seamlessly, with full context reconstruction, appropriate warm-up, and smart adaptations based on the gap between sessions.