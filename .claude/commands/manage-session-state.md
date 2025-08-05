---
name: /manage-session-state
description: Manage consultation session state persistence with save/load and pause/resume functionality
usage: "/manage-session-state [save|load|pause|resume|status] [session-id]"
allowed-tools: [Read, Write, Edit, LS, Glob, Grep, TodoWrite]
category: session-management
version: "1.0"
---

# Session State Management: Professional Consultation Persistence

## Purpose
This command provides enterprise-grade consultation session state persistence, enabling users to save consultation progress, pause sessions at optimal points, and resume consultations seamlessly across multiple interactions. Built for reliability, performance, and user experience.

## 🎯 How Session State Management Works
The system provides comprehensive consultation persistence through:
1. **Automatic State Persistence** - Continuous background saving during consultation
2. **Smart Pause Points** - Intelligent identification of optimal stopping points
3. **Reliable Recovery** - Robust error handling and data integrity protection
4. **Performance Optimization** - <100ms state operations with data validation
5. **User Control** - Complete visibility and control over session state

## 💾 Consultation State File Structure

The consultation state is maintained in `.claude/consultation-state.json` with the following structure:

### Consultation Metadata
- **session_id**: Unique identifier for consultation session
- **created_at**: Timestamp when consultation was initiated
- **last_updated**: Timestamp of most recent state update
- **version**: State file format version for compatibility

### Phase Management
- **current_phase**: Active consultation phase (technical-analysis|domain-intelligence|context-generation)
- **completed_phases**: Array of successfully completed phases with timestamps
- **phase_progress**: Detailed completion percentage for current phase activities
- **phase_quality_score**: Agent-validated quality assessment for each completed phase

### User Interaction State
- **user_responses**: Structured responses from each phase with validation status
- **pending_approvals**: Content awaiting user review and approval
- **modification_requests**: User-requested changes to agent-generated content
- **session_preferences**: User settings for consultation style and depth

### Agent Coordination State
- **active_agents**: Currently engaged agents with their specialization status
- **agent_execution**: Agent integration system execution status and results tracking
- **agent_outputs**: Generated content from each specialized agent with quality metrics
- **agent_handoffs**: Completed inter-agent information transfers with validation
- **agent_conflicts**: Any conflicts detected between agent recommendations

## 🔄 Core Functionality & Advanced Features

### 💾 Save Consultation State (Automatic & Manual)
**Automatic Persistence:**
- **Background Saving**: Continuous state persistence every 30 seconds during active consultation
- **Milestone Checkpoints**: Automatic saves at phase transitions and major decision points
- **User Response Capture**: Immediate persistence after each user interaction
- **Agent Output Preservation**: Real-time saving of specialized agent analysis and recommendations
- **Agent Execution Tracking**: Complete tracking of agent invocations, execution status, and results through integration with `/integrate-agents`

**Manual Save Operations:**
- **On-Demand Saving**: Explicit save triggers with `/manage-session-state save`
- **Custom Checkpoints**: User-created save points with descriptive labels
- **Backup Creation**: Automatic backup of previous state before new saves
- **Validation Checks**: Pre-save validation to ensure data integrity and completeness

### 📂 Load Consultation State (Intelligent Recovery)
**Smart Loading Process:**
- **Version Compatibility**: Automatic handling of different state file versions
- **Data Validation**: Comprehensive validation of loaded state structure and content
- **Corruption Detection**: Advanced detection and repair of corrupted state data
- **Partial Recovery**: Ability to recover partial state when full restoration isn't possible

**Recovery Options:**
- **Full Restoration**: Complete consultation state recovery with all progress preserved
- **Selective Loading**: Choose specific aspects of state to restore (phases, responses, outputs)
- **Backup Fallback**: Automatic fallback to most recent valid backup if primary state is corrupted
- **Manual Override**: User control over recovery process with detailed status reporting

### 📊 Advanced Phase Progress Tracking
**Real-Time Progress Monitoring:**
- **Granular Progress**: Track completion percentage within each consultation phase (0-100%)
- **Quality Scoring**: Multi-agent validated quality assessment for each completed phase
- **Time Tracking**: Duration spent in each phase with efficiency metrics
- **Milestone Recording**: Detailed timestamps for all major consultation milestones

**Progress Analytics:**
- **Completion Forecasting**: Estimated time to consultation completion based on current progress
- **Efficiency Metrics**: Analysis of consultation speed and quality balance
- **Bottleneck Detection**: Identification of phases requiring additional user attention
- **Success Indicators**: Real-time feedback on consultation effectiveness and progress quality

## ⏸️ Advanced Pause/Resume Functionality

### 🛑 Intelligent Pause System
**Smart Pause Point Detection:**
- **Phase Transition Boundaries**: Automatic identification of clean breakpoints between consultation phases
- **User Interaction Completion**: Pause after complete user response cycles to avoid data loss
- **Agent Processing Windows**: Optimal pauses during agent handoffs to minimize workflow disruption
- **Content Generation Gates**: Strategic pauses before major content generation for user approval workflow

**Pause Operations:**
- **Instant Pause**: Immediate consultation suspension with full state preservation
- **Scheduled Pause**: Set future pause points based on consultation progress milestones
- **Context Preservation**: Complete capture of conversation context, user preferences, and agent state
- **Continuation Planning**: Automatic generation of resume instructions and next action items

### ▶️ Seamless Resume Capability
**Resume Intelligence:**
- **Context Restoration**: Complete restoration of consultation context, conversation history, and user preferences
- **Progress Continuity**: Seamless continuation from exact pause point with no information loss
- **Agent State Recovery**: Full restoration of specialized agent activities, outputs, and coordination state
- **User Preference Recall**: Automatic restoration of user settings, approval preferences, and customization choices

**Resume Options:**
- **Exact Point Resume**: Continue from precise pause location with full context preservation
- **Phase Resume**: Resume from beginning of current phase with all previous progress intact
- **Custom Resume**: User-directed resume from any valid checkpoint with selective state restoration
- **Fresh Start Resume**: Begin new session while preserving project context and user responses

### 🎯 Session Continuity Features
**Multi-Session Support:**
- **Session Scheduling**: Plan consultation across multiple time slots with automatic state persistence
- **Cross-Device Continuity**: Resume consultations across different devices with cloud state sync
- **Collaborative Sessions**: Enable team consultations with shared state and collaborative decision making
- **Long-Term Persistence**: Support for consultations spanning days or weeks with state integrity

**Advanced Session Management:**
- **Session Analytics**: Track consultation patterns, completion rates, and user engagement metrics
- **Optimization Recommendations**: Suggest optimal consultation scheduling based on user patterns and progress
- **Session Health Monitoring**: Continuous validation of session integrity and automatic corruption prevention
- **Performance Insights**: Real-time feedback on consultation efficiency and quality progression

## 🔗 Integration with Consultation Workflow

This session state management integrates with the consultation process:
- **Begin Consultation Integration**: Automatically create state file when `/begin-consultation` starts
- **Agent Coordination**: Work with `/coordinate-agents` to track agent activities and outputs
- **Progress Monitoring**: Provide real-time progress updates during consultation phases
- **Session Continuity**: Enable pause/resume across consultation sessions

## 🛡️ Error Handling and Validation

### State File Validation
- Verify JSON structure and required fields
- Validate state version compatibility
- Check for corrupted state data
- Handle permission errors for file access

### Backup and Recovery
- Create backup copies before state updates
- Restore from backup if state becomes corrupted
- Handle missing state files gracefully
- Provide rollback capability for state corruption

### Error Recovery
- Handle file permission errors with clear user guidance
- Manage JSON parsing errors with recovery options
- Provide corruption detection and repair capabilities
- Enable manual state reset if automated recovery fails

## 📊 Usage Examples

```
# Save current consultation state
/manage-session-state save

# Load existing consultation state
/manage-session-state load

# Pause consultation at current point
/manage-session-state pause

# Resume paused consultation
/manage-session-state resume

# Check current session status
/manage-session-state status
```

## 🎯 Success Criteria

- **State Persistence**: 100% reliable save/load operations
- **Performance**: State operations complete in <100ms
- **Data Integrity**: No data loss during pause/resume cycles
- **Error Recovery**: Graceful handling of corrupted or missing state files
- **Integration**: Seamless workflow with consultation and agent coordination commands