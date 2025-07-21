---
description: Intelligent session creation with auto-configuration, context detection, and workspace optimization
argument-hint: "[session_type] [configuration]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /session create - Intelligent Session Creation

Advanced session creation system with auto-configuration, intelligent context detection, and optimized workspace setup.

## Usage
```bash
/session create development                   # Create development session
/session create --auto-config                # Auto-configure from project
/session create --template react             # Create from template
/session create --collaborative              # Multi-user collaborative session
```

## Purpose
**WORKING** command that creates a new Claude Code development session with comprehensive metadata tracking, context preservation, and productivity analytics.

## Command
`/session-create`

## Functional Implementation

### XML Command Structure
```xml
<command>
  <name>session-create</name>
  <context>
    <title>Session title/description</title>
    <project>Project identifier</project>
    <tags>Comma-separated tags</tags>
    <template>Optional session template</template>
  </context>
  <components>
    <import>context/persistent-memory</import>
    <import>constitutional/safety-framework</import>
    <import>analytics/session-tracking</import>
  </components>
  <execution>
    <mode>session_initialization</mode>
    <auto_save>enabled</auto_save>
    <context_tracking>comprehensive</context_tracking>
  </execution>
</command>
```

## ACTUAL EXECUTION LOGIC

### Session Creation Process
```
CLAUDE SESSION CREATION SEQUENCE:
1. Generate unique session ID with timestamp and topic
2. Create session directory structure in .claude/sessions/
3. Initialize session metadata with user-provided information
4. Set up conversation tracking and context preservation
5. Create initial checkpoint with starting state
6. Begin command and interaction logging
7. Activate productivity analytics tracking
```

## WORKING EXAMPLES

### Example 1: Basic Session Creation
**Input:**
```
/session-create "Database Performance Optimization" --project ecommerce --tags database,performance,postgresql
```

**ACTUAL CLAUDE EXECUTION:**
```xml
<session_creation_execution>
  <initialization>
    <session_id>claude-session-20250119-db-performance-optimization</session_id>
    <created_at>2025-01-19T14:30:15Z</created_at>
    <title>Database Performance Optimization</title>
    <project>ecommerce</project>
    <tags>["database", "performance", "postgresql"]</tags>
    <status>active</status>
  </initialization>
  
  <directory_structure_created>
    <session_dir>.claude/sessions/active/claude-session-20250119-db-performance-optimization/</session_dir>
    <metadata_file>session-metadata.json</metadata_file>
    <conversation_log>conversation-history.md</conversation_log>
    <command_log>commands-executed.json</command_log>
    <context_snapshots>context-snapshots/</context_snapshots>
    <checkpoints>checkpoints/</checkpoints>
  </directory_structure_created>
  
  <session_metadata>
    {
      "session_id": "claude-session-20250119-db-performance-optimization",
      "created_at": "2025-01-19T14:30:15Z",
      "updated_at": "2025-01-19T14:30:15Z",
      "title": "Database Performance Optimization",
      "description": "Optimizing database queries and improving overall database performance for ecommerce platform",
      "project": "ecommerce",
      "tags": ["database", "performance", "postgresql"],
      "status": "active",
      "branch": "feature/db-optimization",
      "participants": ["user", "claude"],
      "total_messages": 1,
      "commands_executed": 1,
      "files_modified": 0,
      "context_usage": "15%",
      "productivity_metrics": {
        "session_start": "2025-01-19T14:30:15Z",
        "expected_duration": "2-4 hours",
        "complexity_level": "medium",
        "success_criteria": ["improve query performance", "optimize schema", "reduce response times"]
      },
      "checkpoints": [],
      "git_integration": {
        "branch_created": "feature/db-optimization",
        "initial_commit": "feat: start database optimization session"
      }
    }
  </session_metadata>
  
  <conversation_history_initialized>
    # Session: Database Performance Optimization
    **Session ID**: claude-session-20250119-db-performance-optimization
    **Created**: 2025-01-19T14:30:15Z
    **Project**: ecommerce
    **Tags**: database, performance, postgresql
    
    ## Session Goals
    - Analyze current database performance bottlenecks
    - Optimize slow-running queries
    - Improve database schema design
    - Implement performance monitoring
    
    ## Conversation Log
    
    ### 🚀 Session Started (14:30:15)
    **User**: /session-create "Database Performance Optimization" --project ecommerce --tags database,performance,postgresql
    
    **Claude**: ✅ Session created successfully!
    
    **Session Details:**
    - **ID**: claude-session-20250119-db-performance-optimization
    - **Project**: ecommerce
    - **Focus**: Database performance optimization
    - **Git Branch**: feature/db-optimization (created)
    - **Context Tracking**: Active
    - **Auto-save**: Enabled
    
    **Ready for development work!** 
    All commands, conversations, and context changes will be automatically tracked.
    Use `/session-checkpoint "description"` to create milestones.
  </conversation_history_initialized>
  
  <tracking_systems_activated>
    <context_tracking>
      <status>active</status>
      <tracking_mode>comprehensive</tracking_mode>
      <snapshot_frequency>every_command</snapshot_frequency>
    </context_tracking>
    
    <command_logging>
      <status>active</status>
      <log_level>detailed</log_level>
      <include_results>true</include_results>
    </command_logging>
    
    <productivity_analytics>
      <status>active</status>
      <metrics_tracked>["commands_per_hour", "context_efficiency", "goal_progress", "decision_quality"]</metrics_tracked>
      <auto_reporting>enabled</auto_reporting>
    </productivity_analytics>
  </tracking_systems_activated>
  
  <git_integration>
    <branch_creation>
      <command>git checkout -b feature/db-optimization</command>
      <status>success</status>
      <initial_commit>feat: start database optimization session</initial_commit>
    </branch_creation>
    
    <session_linking>
      <git_branch>feature/db-optimization</git_branch>
      <session_id>claude-session-20250119-db-performance-optimization</session_id>
      <auto_commit>true</auto_commit>
    </session_linking>
  </git_integration>
</session_creation_execution>
```

**Session Creation Result:**
```
✅ SESSION CREATED SUCCESSFULLY!

📋 **Session Details:**
- **ID**: claude-session-20250119-db-performance-optimization
- **Title**: Database Performance Optimization
- **Project**: ecommerce
- **Tags**: database, performance, postgresql
- **Git Branch**: feature/db-optimization ✅ created
- **Storage**: .claude/sessions/active/claude-session-20250119-db-performance-optimization/

🔧 **Tracking Active:**
- ✅ Conversation history logging
- ✅ Command execution tracking  
- ✅ Context window monitoring
- ✅ Productivity analytics
- ✅ Git integration

🎯 **Ready for Development!**
All your work will be automatically tracked and preserved.
Use `/session-checkpoint "milestone description"` to create save points.
Use `/session-save` to save current progress.

**Next Steps:**
1. Begin with `/reason-react "analyze current database performance"`
2. Use `/query` to examine database code
3. Apply `/optimize-prompt` for query improvements
4. Create checkpoints at major milestones
```

### Example 2: Advanced Session with Template
**Input:**
```
/session-create "User Authentication Overhaul" --project saas-platform --tags auth,security,oauth --template security-audit --complexity high
```

**ACTUAL CLAUDE EXECUTION:**
```xml
<advanced_session_creation>
  <template_application>
    <template>security-audit</template>
    <auto_applied_components>
      <component>security/owasp-compliance</component>
      <component>security/threat-modeling</component>
      <component>constitutional/safety-framework</component>
    </auto_applied_components>
    
    <security_checklist_initialized>
      <checklist>
        - [ ] Threat model analysis
        - [ ] OWASP security review
        - [ ] Authentication flow audit
        - [ ] Authorization mechanism review
        - [ ] Session management security
        - [ ] Input validation assessment
        - [ ] Cryptographic implementation review
      </checklist>
    </security_checklist_initialized>
  </template_application>
  
  <enhanced_metadata>
    {
      "session_id": "claude-session-20250119-auth-overhaul",
      "template_used": "security-audit",
      "complexity_level": "high",
      "estimated_duration": "1-2 weeks",
      "security_requirements": ["OWASP compliance", "OAuth 2.0", "JWT security", "Multi-factor auth"],
      "success_criteria": [
        "Pass security audit",
        "Implement OAuth 2.0",
        "Add MFA support",
        "Zero security vulnerabilities"
      ],
      "pre_loaded_components": [
        "security/owasp-compliance",
        "security/threat-modeling",
        "constitutional/safety-framework",
        "reasoning/react-reasoning"
      ]
    }
  </enhanced_metadata>
  
  <security_focused_setup>
    <security_tracking>
      <vulnerability_monitoring>enabled</vulnerability_monitoring>
      <compliance_checking>automatic</compliance_checking>
      <threat_assessment>continuous</threat_assessment>
    </security_tracking>
    
    <documentation_requirements>
      <security_decisions>mandatory</security_decisions>
      <threat_mitigation>documented</threat_mitigation>
      <audit_trail>comprehensive</audit_trail>
    </documentation_requirements>
  </security_focused_setup>
</advanced_session_creation>
```

## FUNCTIONAL FEATURES

### Session Templates
```
AVAILABLE TEMPLATES:
- security-audit: Pre-configured for security-focused development
- performance-optimization: Set up for performance improvement work
- feature-development: Standard feature development workflow
- bug-investigation: Debugging and issue resolution setup
- architecture-design: High-level design and planning setup
- code-review: Code quality and review workflow
- research-spike: Exploratory research and prototyping
```

### Git Integration
```
AUTOMATIC GIT WORKFLOW:
1. Create feature branch: feature/[session-topic]
2. Initial commit: "feat: start [session-title] session"
3. Auto-commit session metadata and checkpoints
4. Link commits to session for traceability
5. Optional: Create draft PR for collaboration
```

### Context Management
```
CONTEXT PRESERVATION:
- Full conversation history with timestamps
- Command execution logs with results
- Context window snapshots at key points
- File modification tracking
- Decision rationale documentation
- Error and solution tracking
```

## Session Analytics Integration

### Productivity Metrics
```
AUTOMATICALLY TRACKED:
- Commands executed per hour
- Context window efficiency
- Goal completion rate
- Decision quality assessment
- Collaboration effectiveness
- Knowledge retention between sessions
```

### Pattern Recognition
```
LEARNING PATTERNS:
- Successful workflow sequences
- Common problem-solution pairs
- Effective command combinations
- Optimal session duration patterns
- Context management strategies
```

## Security and Privacy

### Data Protection
```
PRIVACY SAFEGUARDS:
- Encrypt sensitive session data
- User control over data retention
- Option to exclude sensitive files/conversations
- Anonymization for session sharing
- Secure deletion capabilities
```

### Constitutional AI Integration
```
ETHICAL CONSIDERATIONS:
- Respect user privacy preferences
- Transparent data collection practices
- User consent for all tracking
- Right to modify or delete session data
- Clear explanation of data usage
```

This `/session-create` command provides comprehensive session management that enhances productivity while respecting user privacy and security requirements. 