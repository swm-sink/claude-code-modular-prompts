---
name: /session-manage
description: Comprehensive session control and management for consultation processes with advanced state persistence
usage: "/session-manage [pause|resume|status|export|restart|cleanup] [session-id]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite]
category: consultation
version: "1.0"
---

# Session Management: Professional Consultation Control & State Persistence

## Purpose
This command provides comprehensive session control for consultation processes, enabling users to pause consultations at optimal points, resume seamlessly across multiple Claude interactions, monitor progress, and manage consultation state with enterprise-grade reliability.

## 🎯 Core Session Management Features

**Advanced Session Control:**
- **Intelligent Pause**: Save consultation state at optimal breakpoints
- **Seamless Resume**: Continue from exact pause point with full context restoration
- **Progress Monitoring**: Real-time consultation progress tracking and analytics
- **State Export**: Extract consultation data for sharing or backup
- **Session Cleanup**: Manage and archive completed or abandoned sessions

**Professional State Persistence:**
- **Atomic Operations**: <100ms state save/load with data integrity protection
- **Version Compatibility**: Handle different consultation framework versions
- **Error Recovery**: Robust handling of corrupted or incomplete state data
- **Backup Management**: Automatic backup creation and recovery capability

## 📋 Session Management Operations

### 🛑 Pause Consultation
**Intelligent Pause Point Detection:**
```bash
/session-manage pause
```
- **Auto-Detection**: Identifies optimal pause points in consultation flow
- **Context Preservation**: Saves complete conversation context and user responses
- **Agent State Capture**: Preserves specialized agent analysis and coordination state
- **Progress Snapshot**: Captures detailed progress metrics and quality scores

**Pause Intelligence Features:**
- **Phase Boundary Pause**: Clean breaks between consultation phases
- **User Interaction Pause**: Safe pause after complete user response cycles
- **Agent Handoff Pause**: Strategic pauses during agent coordination transitions
- **Content Generation Pause**: Optimal breaks before major content generation

### ▶️ Resume Consultation
**Seamless Continuation:**
```bash
/session-manage resume
```
- **Context Restoration**: Complete conversation history and user preference recovery
- **Agent State Recovery**: Full restoration of specialized agent activities and outputs
- **Progress Continuity**: Exact point continuation with no information loss
- **User Control Restoration**: Preference settings and customization recovery

**Resume Options:**
```bash
# Resume from exact pause point
/session-manage resume exact

# Resume from phase beginning with progress intact
/session-manage resume phase

# Custom resume from specific checkpoint
/session-manage resume checkpoint [checkpoint-id]

# Fresh session with preserved project context
/session-manage resume fresh
```

### 📊 Session Status & Progress
**Comprehensive Progress Monitoring:**
```bash
/session-manage status
```

**Status Information Provided:**
- **Current Phase**: Active consultation phase with completion percentage
- **Time Analytics**: Time spent per phase and estimated completion time
- **Quality Metrics**: Agent-validated quality scores for completed phases
- **User Engagement**: Response completeness and interaction quality tracking
- **Agent Coordination**: Specialized agent status and analysis progress
- **Session Health**: Data integrity and state validation status

**Progress Visualization:**
```
📊 Consultation Progress Status

Session ID: consultation_2025_08_07_14_30_15
Started: 2025-08-07 14:30:15 | Duration: 18m 45s

Phase Progress:
✅ Project Discovery (Stage 1)    [████████████████████] 100% (5m 20s)
✅ Technical Analysis (Stage 2)   [████████████████████] 100% (8m 15s) 
🔄 Domain Intelligence (Stage 3)  [████████████▓▓▓▓▓▓▓▓] 60%  (5m 10s)
⏳ Context Generation (Stage 4)   [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 0%

Agent Analysis Status:
✅ Framework Detection Agent      - Complete (React/TypeScript identified)
✅ Architecture Analysis Agent    - Complete (Next.js patterns mapped)
🔄 Business Domain Agent          - In Progress (E-commerce patterns detected)
⏳ User Journey Agent             - Pending
⏳ Context Generation Agent       - Pending

Quality Scores:
• Technical Understanding: 92% (High confidence)
• Business Context:       67% (Moderate confidence)
• Overall Readiness:      78% (Good foundation)

Estimated Completion: 8-12 minutes remaining
```

### 💾 Export Session Data
**Comprehensive Data Export:**
```bash
/session-manage export [format] [destination]
```

**Export Formats:**
- **JSON**: Complete machine-readable session state
- **Markdown**: Human-readable consultation summary
- **Context**: Generated context files for team sharing
- **Report**: Executive summary with key findings and recommendations

**Export Examples:**
```bash
# Export complete session as JSON
/session-manage export json backup/

# Export human-readable summary
/session-manage export markdown docs/consultation-summary.md

# Export generated context files
/session-manage export context .claude/context/

# Export executive summary report
/session-manage export report docs/claude-setup-report.md
```

### 🔄 Restart & Reset Operations
**Session Reset Options:**
```bash
# Restart consultation with fresh state
/session-manage restart

# Restart specific phase with previous progress
/session-manage restart phase [phase-number]

# Reset to specific checkpoint
/session-manage restart checkpoint [checkpoint-id]

# Complete reset with project context preservation
/session-manage restart fresh
```

### 🧹 Session Cleanup & Maintenance
**State Management Cleanup:**
```bash
# Clean up completed sessions
/session-manage cleanup completed

# Archive old sessions
/session-manage cleanup archive

# Remove corrupted or incomplete sessions
/session-manage cleanup corrupted

# Full cleanup with confirmation
/session-manage cleanup all
```

## 🔧 Advanced Session Features

### Multi-Session Support
**Professional Session Management:**
- **Session Scheduling**: Plan consultations across multiple time slots
- **Cross-Device Continuity**: Resume consultations across different environments
- **Collaborative Sessions**: Enable team consultations with shared state
- **Long-Term Persistence**: Support consultations spanning multiple days

### Session Analytics & Optimization
**Consultation Intelligence:**
- **Pattern Recognition**: Track consultation patterns and optimization opportunities
- **Efficiency Metrics**: Analyze consultation speed vs quality balance
- **User Engagement**: Monitor user satisfaction and interaction quality
- **Success Prediction**: Forecast consultation success based on progress patterns

### Error Handling & Recovery
**Robust State Management:**
- **Corruption Detection**: Advanced detection and repair of state corruption
- **Backup Recovery**: Automatic fallback to most recent valid state
- **Partial Recovery**: Selective recovery when full restoration isn't possible
- **Manual Override**: User control over recovery process with detailed diagnostics

## 📊 Session State File Structure

### Consultation State Schema (`.claude/consultation-state.json`)

```json
{
  "session_metadata": {
    "session_id": "consultation_2025_08_07_14_30_15",
    "created_at": "2025-08-07T14:30:15Z",
    "last_updated": "2025-08-07T14:48:30Z",
    "version": "1.0",
    "consultation_type": "full_consultation"
  },
  "phase_management": {
    "current_phase": "domain-intelligence",
    "completed_phases": [
      {
        "phase": "project-discovery",
        "completed_at": "2025-08-07T14:35:35Z",
        "duration_seconds": 320,
        "quality_score": 95
      },
      {
        "phase": "technical-analysis", 
        "completed_at": "2025-08-07T14:43:50Z",
        "duration_seconds": 495,
        "quality_score": 92
      }
    ],
    "phase_progress": {
      "current_phase_completion": 60,
      "estimated_remaining_minutes": 10,
      "quality_trend": "increasing"
    }
  },
  "user_interaction_state": {
    "user_responses": {
      "project_type": "E-commerce platform",
      "technical_stack": "React, TypeScript, Next.js, PostgreSQL",
      "team_size": "5-8 developers",
      "development_stage": "MVP to growth transition"
    },
    "session_preferences": {
      "consultation_pace": "standard",
      "detail_level": "comprehensive",
      "communication_style": "technical"
    },
    "pending_approvals": [],
    "modification_requests": []
  },
  "agent_coordination_state": {
    "active_agents": [
      {
        "agent_name": "business_domain_agent",
        "status": "active",
        "progress": 60,
        "current_analysis": "E-commerce workflow mapping"
      }
    ],
    "completed_agent_outputs": [
      {
        "agent_name": "framework_detection_agent",
        "analysis_results": {
          "primary_framework": "React 18 with TypeScript",
          "architecture_pattern": "Next.js with API routes",
          "confidence_score": 95
        }
      }
    ],
    "agent_handoffs": [
      {
        "from_agent": "technical_architecture_agent",
        "to_agent": "business_domain_agent", 
        "handoff_time": "2025-08-07T14:43:50Z",
        "context_transferred": "Technical stack analysis complete"
      }
    ]
  }
}
```

## 🔗 Integration with Consultation Commands

### Automatic Integration
**Seamless Workflow Integration:**
- **Auto-Save**: Background state persistence during all consultations
- **Progress Tracking**: Real-time progress updates across consultation phases
- **Error Recovery**: Automatic state recovery on consultation interruption
- **Context Continuity**: Maintain conversation context across session boundaries

### Manual Control Points
**User-Directed Session Management:**
- **Strategic Pauses**: User-initiated pauses at optimal consultation points
- **Custom Checkpoints**: User-created save points with descriptive labels
- **Selective Resume**: Choose specific aspects of session to restore
- **Progress Review**: On-demand status checks and progress visualization

## 💡 Usage Examples & Workflows

### Typical Multi-Session Consultation:
```bash
# Day 1: Start consultation (20 minutes available)
/begin-consultation

# [After 18 minutes, need to stop]
/session-manage pause
> ✅ Session paused at optimal point (end of technical analysis)
> Session ID: consultation_2025_08_07_14_30_15
> Resume with: /session-manage resume

# Day 2: Resume consultation (15 minutes available) 
/session-manage resume
> ✅ Resuming from domain intelligence phase
> Previous context restored: Technical analysis complete
> Continuing with business domain exploration...

# [Complete domain phase]
/session-manage status
> 📊 Progress: 85% complete, estimated 5 minutes remaining

# Complete consultation
/session-manage export report docs/claude-setup-summary.md
```

### Team Collaboration Workflow:
```bash
# Lead developer starts consultation
/begin-consultation
/session-manage pause

# Export for team review
/session-manage export markdown consultation-progress.md

# Team lead resumes with adjustments
/session-manage resume
# [Complete consultation with team input]

# Share final context with team
/session-manage export context .claude/context/
```

## 🎯 Success Criteria

### Performance Standards
- **State Operations**: <100ms save/load operations
- **Data Integrity**: 100% reliable state persistence with corruption detection
- **Recovery Success**: 99%+ successful recovery from corrupted or incomplete state
- **Cross-Session Continuity**: Seamless resume with no information loss

### User Experience Standards
- **Progress Visibility**: Clear, real-time progress indicators and completion forecasting
- **Control Flexibility**: User control over all session management operations
- **Error Handling**: Graceful error recovery with clear user guidance
- **Data Export**: Complete consultation data available in multiple formats

## 🚀 Advanced Features

### Session Intelligence
**Smart Session Management:**
- **Optimal Pause Detection**: AI-identified best stopping points in consultation flow
- **Completion Forecasting**: Accurate time estimation based on progress and user interaction patterns
- **Quality Trend Analysis**: Real-time assessment of consultation effectiveness
- **User Engagement Monitoring**: Track and optimize user satisfaction throughout process

### Enterprise Integration
**Professional Deployment Features:**
- **Team Session Sharing**: Enable collaborative consultation processes
- **Audit Trail**: Complete session activity logging for compliance
- **Backup Automation**: Scheduled state backups with retention policies
- **Performance Monitoring**: Session performance analytics and optimization insights

**Result**: Professional-grade session management that enables flexible, reliable consultation experiences with complete user control and enterprise-ready state persistence.

## Next Steps After Session Management

1. **Resume active consultations**: Use `/session-manage resume` to continue
2. **Monitor consultation progress**: Use `/session-manage status` for real-time updates
3. **Export consultation results**: Use `/session-manage export` to share findings
4. **Integrate with team workflow**: Share exported context and consultation summaries

**Time Investment**: Session management operates in the background with <100ms operations, enabling flexible consultation scheduling without time penalties.