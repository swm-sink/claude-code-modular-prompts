---
name: /session-manage
description: Session management for pause/resume capability during onboarding and long operations
usage: "/session-manage [--save|--restore|--list|--clear]"
allowed-tools: [Read, Write, LS, Glob]
---

# 🔄 Session Management System

Save and restore your progress during long operations like onboarding, allowing you to pause and resume exactly where you left off. Perfect for the 30+ minute consultation process.

## Why Session Management?

### Real-World Interruptions
- Meeting starts mid-onboarding
- Need to switch to urgent bug fix
- Machine needs to restart
- Want to continue tomorrow

### Long Operations
- 30+ minute consultations
- Large codebase analysis
- Complex refactoring
- Multi-step workflows

### Team Coordination
- Share session with teammate
- Review progress together
- Hand off work smoothly
- Maintain context across shifts

## How It Works

### Automatic Session Saving
```javascript
// Sessions auto-save every 30 seconds during:
- Onboarding processes
- Multi-step workflows
- Long-running analyses
- Complex operations

// Session includes:
- Current step/phase
- Gathered information
- User responses
- Detected patterns
- Partial results
- Next actions queued
```

### Session Structure
```yaml
.claude/sessions/
├── current.session.json      # Active session
├── autosave.session.json     # Auto-backup
└── archive/                   # Completed sessions
    ├── 2024-01-15-onboarding.session.json
    ├── 2024-01-14-refactor.session.json
    └── 2024-01-13-migration.session.json
```

## Session Commands

### Save Current Session
```bash
/session-manage --save [name]

💾 Saving Session...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Session ID   : onboard-2024-01-15-14:30
Progress     : Step 7 of 12 (58%)
Time Elapsed : 18 minutes
Data Gathered: 
  ✓ Framework detection complete
  ✓ Pattern analysis complete
  ⚡ Team conventions (in progress)
  ○ Command generation (pending)

Session saved to: .claude/sessions/current.session.json
Resume with: /session-manage --restore
```

### Restore Session
```bash
/session-manage --restore [id]

🔄 Restoring Session...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Session ID   : onboard-2024-01-15-14:30
Created      : 2 hours ago
Progress     : Step 7 of 12 (58%)
Time Elapsed : 18 minutes

📊 Session Context:
  Project: Next.js + TypeScript
  Patterns: Atomic design detected
  Team Size: 5-10 developers
  
🔄 Resuming from: Analyzing team conventions...

Continue where you left off? [Y/n]: Y

✨ Session restored! Continuing analysis...
```

### List Available Sessions
```bash
/session-manage --list

📋 Available Sessions:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] onboard-2024-01-15-14:30 (current)
    Progress: 58% | Status: Paused
    Last modified: 2 hours ago
    
[2] refactor-2024-01-14-09:15
    Progress: 100% | Status: Complete
    Completed: Yesterday
    
[3] setup-team-2024-01-13-16:45
    Progress: 45% | Status: Abandoned
    Last modified: 2 days ago

Use: /session-manage --restore [number]
```

### Clear Sessions
```bash
/session-manage --clear [all|completed|abandoned]

🗑️ Clear Sessions:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Found:
  2 completed sessions
  1 abandoned session
  1 current session

Clear completed sessions? [Y/n]: Y
✓ Cleared 2 completed sessions
✓ Archived to .claude/sessions/archive/
```

## Session Data Structure

### What Gets Saved
```json
{
  "sessionId": "onboard-2024-01-15-14:30",
  "type": "onboarding",
  "created": "2024-01-15T14:30:00Z",
  "lastModified": "2024-01-15T14:48:00Z",
  "progress": {
    "currentStep": 7,
    "totalSteps": 12,
    "percentage": 58,
    "phase": "team-analysis"
  },
  "context": {
    "project": {
      "framework": "Next.js",
      "language": "TypeScript",
      "testing": "Jest",
      "patterns": ["atomic-design", "REST-api"]
    },
    "decisions": {
      "strictMode": true,
      "tdd": false,
      "teamSize": "medium"
    },
    "detected": {
      "components": 47,
      "apis": 23,
      "tests": 89,
      "coverage": 73
    }
  },
  "pendingActions": [
    "analyzeTeamConventions",
    "generateCommands",
    "createContext"
  ],
  "completedActions": [
    "detectFramework",
    "analyzePatterns",
    "extractConventions"
  ]
}
```

## Advanced Session Features

### Session Branching
```bash
# Try different paths from same point
/session-manage --branch experiment

📋 Branched Session: experiment-2024-01-15-15:00
You can now try different options without losing progress
Return to original with: /session-manage --restore main
```

### Session Sharing
```bash
# Export session for team member
/session-manage --export

📤 Exported: onboard-2024-01-15.claude-session
Share this file with your team
Import with: /session-manage --import [file]
```

### Session Merging
```bash
# Combine multiple partial sessions
/session-manage --merge [session1] [session2]

🔀 Merging Sessions:
  Session 1: 40% complete (framework detection)
  Session 2: 30% complete (pattern analysis)
  
Combined: 70% complete
Conflicts: 0
```

## Smart Session Management

### Auto-Recovery
```javascript
// If Claude crashes or connection lost:
detectIncompleteSession() {
  const lastSession = getLastSession()
  if (lastSession.isIncomplete) {
    prompt("Found incomplete session from 5 minutes ago. Resume?")
  }
}
```

### Intelligent Resumption
```javascript
// Revalidate context on resume
resumeSession(session) {
  // Check if files changed
  const changes = detectChanges(session.timestamp)
  
  if (changes.significant) {
    prompt("Project changed since session. Reanalyze?")
  } else {
    continueFromLastStep()
  }
}
```

### Session Optimization
```javascript
// Only save what matters
optimizeSession(data) {
  // Don't save:
  - Temporary calculations
  - Cached file contents
  - Redundant detections
  
  // Do save:
  - User decisions
  - Key discoveries
  - Progress markers
  - Context snapshots
}
```

## Use Cases

### Long Consultation Process
```
Start: Monday morning
  Complete 40% of consultation
  Save session for meeting
  
Resume: Monday afternoon  
  Continue from 40%
  Complete to 70%
  EOD save
  
Finish: Tuesday morning
  Resume from 70%
  Complete consultation
```

### Team Handoff
```
Developer A:
  Starts onboarding
  Completes technical analysis
  Exports session
  
Developer B:
  Imports session
  Reviews technical findings
  Continues with team setup
  Completes process
```

### Experimentation
```
Main session:
  Reach decision point
  Branch session
  
Experiment branch:
  Try option A
  See results
  Don't like it
  
Return to main:
  Try option B
  Better results
  Continue
```

## Session Best Practices

### Regular Saves
- Auto-save every 30 seconds
- Manual save at key decisions
- Save before breaking
- Save after milestones

### Clear Naming
```bash
/session-manage --save "onboard-production-stripe"
/session-manage --save "refactor-auth-system"
/session-manage --save "team-setup-frontend"
```

### Session Hygiene
- Clear completed sessions weekly
- Archive important sessions
- Document session outcomes
- Share successful sessions

## The Result

Never lose progress. Always maintain context. Work at your own pace.

**Your work is always safe, recoverable, and shareable.**