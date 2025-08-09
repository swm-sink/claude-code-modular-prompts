# Session Persistence System
# Claude Code command for robust session state management
# Purpose: Save, load, and manage consultation session state
# Version: 1.0 - Production Session Management

---
name: consultation-session-persist
description: Save and load consultation session state for pause/resume capability
usage: "/consultation-session-persist [action] [session-id]"
allowed-tools: [Read, Write, Edit, LS, Bash]
category: consultation
---

# Session Persistence Commands

## Save Current Session State

### Command: `/save-consultation-session`
**Purpose**: Save current consultation state to persistent storage

**Usage Pattern**:
```
/save-consultation-session [optional-session-name]

Examples:
/save-consultation-session
/save-consultation-session "React E-commerce Deep Dive"
/save-consultation-session "Team Onboarding - Frontend Focus"
```

**Implementation Logic**:
1. **Generate Session ID**: Create UUID if new session
2. **Capture Current State**: Extract all consultation progress and context
3. **Validate State Completeness**: Ensure critical information is preserved
4. **Write to Persistent Storage**: Save to `.claude/consultation-state.json`
5. **Create Backup**: Maintain rollback capability
6. **Confirm Success**: Provide session ID and save confirmation

**State Capture Process**:
- **Current Position**: Stage, substage, question index, question ID
- **Progress Tracking**: Completion percentages, time spent, questions answered
- **Accumulated Context**: All responses and extracted information
- **Quality Metrics**: Confidence scores, gaps identified, validation status
- **User Preferences**: Pace, skip settings, communication style
- **Time Information**: Elapsed time, targets, actuals per stage

**File Structure**:
```json
{
  "session_metadata": {
    "session_id": "uuid",
    "session_name": "user-provided name",
    "created": "timestamp",
    "last_updated": "timestamp"
  },
  "progress_state": { ... },
  "accumulated_context": { ... },
  "time_tracking": { ... },
  "quality_metrics": { ... },
  "user_interaction": { ... }
}
```

## Load Existing Session State

### Command: `/load-consultation-session`
**Purpose**: Resume consultation from previously saved state

**Usage Pattern**:
```
/load-consultation-session [session-id]
/load-consultation-session [session-name-pattern]

Examples:
/load-consultation-session 550e8400-e29b-41d4-a716-446655440000
/load-consultation-session "React E-commerce"
/load-consultation-session  # Show available sessions for selection
```

**Implementation Logic**:
1. **Session Discovery**: Find available saved sessions
2. **Session Selection**: Handle ID, name pattern, or interactive selection
3. **State Validation**: Verify session data integrity
4. **Context Restoration**: Rebuild consultation understanding
5. **Position Setting**: Set current stage and question position
6. **Warm-up Summary**: Present progress summary to user
7. **Resume Confirmation**: Confirm ready to continue

**Restoration Process**:
- **Validate File Integrity**: Check JSON structure and required fields
- **Reconstruct Context**: Rebuild accumulated project understanding
- **Set Current Position**: Resume from exact checkpoint
- **Load User Preferences**: Restore pace, skip settings, style preferences
- **Calculate Remaining Time**: Update time estimates based on progress
- **Prepare Next Steps**: Ready next questions and follow-ups

## Session Management Commands

### Command: `/list-consultation-sessions`
**Purpose**: Show all available saved sessions

**Output Format**:
```
Available Consultation Sessions:
1. React E-commerce Deep Dive (Stage 2/4, 45% complete, 15 min elapsed)
   ID: 550e8400-e29b-41d4-a716-446655440000
   Last Updated: 2025-08-07 14:45:30
   
2. Vue Dashboard Project (Stage 1/4, 80% complete, 6 min elapsed)
   ID: 7a9f2b1c-3d4e-5f6g-7h8i-9j0k1l2m3n4o
   Last Updated: 2025-08-07 12:30:15

3. Python Data Pipeline (Stage 3/4, 60% complete, 22 min elapsed)
   ID: 1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p
   Last Updated: 2025-08-06 16:20:45
```

### Command: `/delete-consultation-session`
**Purpose**: Remove saved session (with confirmation)

**Usage Pattern**:
```
/delete-consultation-session [session-id]
/delete-consultation-session [session-name-pattern]

Examples:
/delete-consultation-session 550e8400-e29b-41d4-a716-446655440000
/delete-consultation-session "React E-commerce"
```

**Safety Features**:
- **Confirmation Required**: User must confirm deletion
- **Backup Creation**: Create backup before deletion
- **Soft Delete Option**: Mark as deleted but keep file
- **Recovery Window**: Allow undelete within 24 hours

## Auto-Save and Checkpointing

### Automatic Save Triggers
**When session state is automatically saved**:

1. **Stage Transitions**: After completing each consultation stage
2. **Time Intervals**: Every 5 minutes during active consultation
3. **Significant Progress**: After answering 5 questions
4. **User Control Actions**: When user uses pause, skip, or back commands
5. **Quality Checkpoints**: When confidence scores update significantly
6. **Error Recovery**: Before potentially problematic operations

### Checkpoint Management
**Rollback and Recovery System**:

```yaml
checkpoint_strategy:
  frequency: "every_5_questions"
  retention: "last_5_checkpoints"
  triggers:
    - "stage_completion"
    - "user_pause_request" 
    - "quality_validation_point"
    - "error_before_critical_operation"
    
  recovery_options:
    - "rollback_to_last_checkpoint"
    - "rollback_to_stage_beginning"
    - "rollback_to_specific_question"
    - "complete_session_restart"
```

## Error Handling and Recovery

### Session Corruption Recovery
**When session files are corrupted or incomplete**:

1. **Automatic Validation**: Check file integrity on load
2. **Partial Recovery**: Attempt to salvage valid portions
3. **Backup Restoration**: Use most recent valid backup
4. **Graceful Degradation**: Continue with reduced context if needed
5. **User Notification**: Clear explanation of what was recovered/lost

### Common Error Scenarios
**Handling typical session management issues**:

```yaml
error_scenarios:
  file_not_found:
    action: "Offer session discovery or new session start"
    message: "Session not found. Would you like to see available sessions?"
    
  corrupted_json:
    action: "Attempt backup restoration"
    message: "Session file corrupted. Attempting recovery from backup..."
    
  invalid_session_id:
    action: "Suggest similar sessions or show session list"
    message: "Invalid session ID. Here are available sessions:"
    
  permission_denied:
    action: "Check file permissions and suggest alternatives"
    message: "Cannot access session file. Check file permissions."
    
  disk_full:
    action: "Cleanup old sessions and retry"
    message: "Storage full. Cleaning up old sessions and retrying..."
```

## Session Migration and Versioning

### Version Compatibility
**Handling different session schema versions**:

```yaml
version_handling:
  current_version: "1.0"
  supported_versions: ["1.0"]
  migration_paths:
    "0.9_to_1.0":
      - "Add quality_metrics section"
      - "Convert time_tracking format"
      - "Update user_interaction structure"
      
  migration_strategy:
    automatic: true
    backup_before_migration: true
    validation_after_migration: true
```

### Session Export/Import
**Sharing sessions between environments**:

```yaml
export_format:
  standard: "JSON with full state"
  compact: "JSON with essential information only"
  portable: "Platform-independent format"
  
import_validation:
  - "Check schema version compatibility"
  - "Validate required fields"
  - "Verify context consistency"
  - "Test session resumability"
```

## Performance Optimization

### Efficient State Management
**Optimizing for large consultation sessions**:

1. **Incremental Saves**: Only save changed portions of state
2. **Compression**: Compress accumulated context for storage
3. **Lazy Loading**: Load session parts as needed
4. **Memory Management**: Clear unused context when not needed
5. **Background Saves**: Non-blocking save operations

### Storage Strategy
**Managing session file growth and cleanup**:

```yaml
storage_management:
  max_session_age: "30_days"
  max_sessions_per_project: 10
  cleanup_triggers:
    - "startup_check"
    - "storage_threshold_reached"
    - "user_initiated_cleanup"
    
  retention_policy:
    active_sessions: "keep_indefinitely"
    completed_sessions: "keep_7_days"
    abandoned_sessions: "keep_3_days"
```

## Integration with Consultation Framework

### Seamless Integration Points
**How session persistence integrates with consultation flow**:

1. **Question Framework Integration**: Save question IDs and context
2. **Stage Management**: Coordinate with stage completion logic
3. **User Control Integration**: Work with pause, skip, back commands
4. **Quality Validation**: Save confidence scores and validation status
5. **Time Management**: Integrate with consultation timing system

### Context Handoff
**Preparing saved context for consultation resume**:

```yaml
context_preparation:
  resume_summary:
    - "Progress overview"
    - "Key findings so far"
    - "Current understanding confidence"
    - "Next steps preview"
    
  warm_up_questions:
    - "Does this summary capture where we left off?"
    - "Any changes to add since our last session?"
    - "Ready to continue where we stopped?"
    
  context_validation:
    - "Verify project understanding still accurate"
    - "Check if any major changes occurred"
    - "Confirm consultation goals remain same"
```

## Security and Privacy

### Data Protection
**Protecting sensitive consultation information**:

1. **Local Storage Only**: Session files never transmitted
2. **File Permissions**: Restrict access to user only
3. **Encryption Option**: Encrypt sensitive context data
4. **Cleanup on Completion**: Automatic cleanup of temporary files
5. **No Cloud Sync**: Prevent accidental cloud synchronization

### Privacy Controls
**User control over session data**:

```yaml
privacy_features:
  data_retention_control: true
  selective_save: "Users can exclude sensitive information"
  anonymous_mode: "Save structure without specific details"
  complete_cleanup: "Remove all traces when requested"
  
  sensitive_data_handling:
    - "Business-specific terminology"
    - "Integration details"
    - "Performance requirements"
    - "Team structure information"
```

This session persistence system provides robust, reliable state management for the deep discovery consultation, enabling users to pause and resume their 30-60 minute session across multiple interactions while maintaining complete context and progress.