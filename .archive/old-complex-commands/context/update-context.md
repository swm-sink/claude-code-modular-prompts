---
name: update-context
description: Update and modify specific context sections with intelligent change management and validation
usage: "update-context [file|section|layer|batch] [--validate|--preview|--rollback]"
allowed-tools: [Read, Write, Edit, MultiEdit, LS, Glob, Grep, TodoWrite]
category: context
version: "1.0"
---

# Update Context: Intelligent Context Modification System

## Purpose: Precise Context Updates with Change Management

The `/update-context` command provides intelligent modification of your project's context system with comprehensive change management, validation, and rollback capabilities. It ensures context updates maintain consistency, accuracy, and effectiveness while preserving the integrity of your hierarchical context architecture.

**Update Philosophy**: Surgical over wholesale, validated over assumed, reversible over permanent, integrated over isolated.

## 🔧 Context Update Modes

### File-Level Updates
**Usage**: `/update-context file [path]`

Update entire context files with intelligent change detection and validation:

```
File Update Process:
├── Current State Analysis
│   ├── Read existing file content
│   ├── Analyze current cross-references
│   ├── Identify dependent context files
│   └── Check integration points
│
├── Change Preparation
│   ├── Backup current version
│   ├── Prepare change manifest
│   ├── Validate proposed changes
│   └── Check impact on related files
│
├── Update Execution
│   ├── Apply changes with MultiEdit
│   ├── Update cross-references
│   ├── Validate file integrity
│   └── Test context effectiveness
│
└── Change Finalization
    ├── Update change log
    ├── Refresh dependent contexts
    ├── Run validation tests
    └── Confirm successful update
```

**Examples**:
```bash
# Update business rules context
/update-context file .claude/context/domain/business-rules.md

# Update technical architecture
/update-context file .claude/context/technical/architecture.md

# Update foundation context
/update-context file CLAUDE.md
```

### Section-Level Updates
**Usage**: `/update-context section [file] [section-name]`

Precise updates to specific sections within context files:

```
Section Update Capabilities:
├── Domain Context Sections
│   ├── Business Logic Updates
│   ├── User Workflow Modifications
│   ├── Terminology Additions
│   └── Data Model Changes
│
├── Technical Context Sections  
│   ├── Architecture Modifications
│   ├── Framework Updates
│   ├── Deployment Changes
│   └── Testing Strategy Updates
│
├── Workflow Context Sections
│   ├── Process Improvements
│   ├── Tool Updates
│   ├── Guideline Changes
│   └── Standard Modifications
│
└── Agent Context Sections
    ├── Capability Updates
    ├── Specialization Changes
    ├── Knowledge Base Updates
    └── Integration Modifications
```

**Examples**:
```bash
# Update authentication section in business rules
/update-context section domain/business-rules.md "Authentication & Authorization"

# Update deployment section in technical architecture
/update-context section technical/architecture.md "Deployment Strategy"

# Update code review section in development workflow
/update-context section workflows/development.md "Code Review Process"
```

### Layer-Level Updates
**Usage**: `/update-context layer [foundation|domain|technical|workflow|agents]`

Coordinate updates across an entire context layer:

```
Layer Update Coordination:
├── Foundation Layer Update
│   ├── Core project identity updates
│   ├── Anti-pattern additions
│   ├── Navigation guide updates
│   └── Cross-layer reference updates
│
├── Domain Layer Update
│   ├── Business rules evolution
│   ├── User workflow changes
│   ├── Terminology expansions
│   └── Data model modifications
│
├── Technical Layer Update
│   ├── Architecture evolution
│   ├── Framework upgrades
│   ├── Infrastructure changes
│   └── Tool stack modifications
│
├── Workflow Layer Update
│   ├── Process improvements
│   ├── Quality standard changes
│   ├── Team structure updates
│   └── Communication updates
│
└── Agent Layer Update
    ├── Agent capability expansion
    ├── Specialization refinement
    ├── Knowledge base updates
    └── Integration improvements
```

### Batch Update Mode
**Usage**: `/update-context batch [--from-file|--from-consultation|--from-changes]`

Coordinate multiple context updates with dependency management:

```
Batch Update Sources:
├── From File Updates
│   ├── Read update specifications from file
│   ├── Validate all proposed changes
│   ├── Execute in dependency order
│   └── Validate complete system
│
├── From Consultation Results
│   ├── Apply new consultation insights
│   ├── Update context with new patterns
│   ├── Refresh outdated information
│   └── Integrate new domain knowledge
│
├── From Project Changes
│   ├── Scan project for changes since last update
│   ├── Identify context needing updates
│   ├── Propose specific modifications
│   └── Execute approved updates
│
└── From Pattern Updates
    ├── Apply new anti-pattern discoveries
    ├── Update best practice guidance
    ├── Refine context effectiveness
    └── Improve cross-references
```

## 🔍 Intelligent Change Management

### Change Impact Analysis
Analyze the full impact of proposed context changes:

```
Impact Analysis Report:
├── Direct Impact
│   ├── Files directly modified
│   ├── Sections being changed
│   ├── Content being added/removed
│   └── References being updated
│
├── Indirect Impact
│   ├── Files with cross-references to changed content
│   ├── Context layers affected by changes
│   ├── Agent specializations impacted
│   └── Navigation patterns affected
│
├── Risk Assessment
│   ├── Breaking changes to context hierarchy
│   ├── Potential cross-reference conflicts
│   ├── Context effectiveness impact
│   └── User experience implications
│
└── Mitigation Strategies
    ├── Rollback procedures
    ├── Alternative update approaches
    ├── Validation requirements
    └── Testing recommendations
```

### Preview Mode
**Usage**: `/update-context [mode] --preview`

Preview changes before applying them:

```
Change Preview:
┌─────────────────────────────────────────────────────────┐
│ Context Update Preview                                   │
├─────────────────────────────────────────────────────────┤
│ File: .claude/context/domain/business-rules.md         │
│ Section: Authentication & Authorization                 │
│                                                         │
│ Changes:                                                │
│ + Added: Multi-factor authentication requirements       │
│ + Added: Role-based access control patterns            │
│ ~ Modified: Session management guidelines               │
│ - Removed: Outdated password policy references         │
│                                                         │
│ Cross-Reference Impact:                                 │
│ ├── technical/security.md (1 reference to update)      │
│ ├── workflows/onboarding.md (2 references to update)   │
│ └── agents/security-expert.md (3 references to update) │
│                                                         │
│ Actions: [Apply Changes] [Modify Changes] [Cancel]     │
└─────────────────────────────────────────────────────────┘
```

### Validation Mode
**Usage**: `/update-context [mode] --validate`

Comprehensive validation of changes before and after application:

```
Update Validation Checklist:
├── Pre-Update Validation
│   ├── ✓ Context hierarchy integrity
│   ├── ✓ Cross-reference consistency
│   ├── ✓ No circular references
│   ├── ✓ Content format compliance
│   └── ✓ Change impact acceptable
│
├── Change Application
│   ├── ✓ Files updated successfully
│   ├── ✓ Cross-references updated
│   ├── ✓ No syntax errors
│   ├── ✓ Backup created
│   └── ✓ Change log updated
│
└── Post-Update Validation
    ├── ✓ Context effectiveness maintained
    ├── ✓ Navigation still functional
    ├── ✓ Agent integration working
    ├── ✓ No broken references
    └── ✓ User acceptance confirmed
```

## 🔄 Change Management Features

### Version Control Integration
Automatic integration with project version control:

```
Git Integration:
├── Automatic Backups
│   ├── Create backup branch before updates
│   ├── Commit current state
│   ├── Tag with update timestamp
│   └── Push backup to remote
│
├── Change Tracking
│   ├── Detailed commit messages
│   ├── Change impact documentation
│   ├── Before/after context diffs
│   └── Update reason tracking
│
├── Rollback Support
│   ├── Quick rollback to previous version
│   ├── Selective rollback of specific changes
│   ├── Merge conflict resolution
│   └── Change history browsing
│
└── Collaboration Support
    ├── Multi-user update coordination
    ├── Change approval workflows
    ├── Update notification system
    └── Conflict resolution procedures
```

### Change History Tracking
Comprehensive tracking of all context modifications:

```
Change History Log:
├── Update Metadata
│   ├── Timestamp and duration
│   ├── User identification
│   ├── Update type and scope
│   └── Success/failure status
│
├── Change Description
│   ├── What was changed
│   ├── Why it was changed
│   ├── How it was changed
│   └── Expected impact
│
├── Validation Results
│   ├── Pre-update validation status
│   ├── Post-update validation status
│   ├── Context effectiveness impact
│   └── User satisfaction rating
│
└── Rollback Information
    ├── Rollback procedure
    ├── Dependencies for rollback
    ├── Rollback impact assessment
    └── Alternative restoration methods
```

### Rollback Capabilities
**Usage**: `/update-context --rollback [update-id|latest|date]`

Sophisticated rollback system for undoing context changes:

```
Rollback Options:
├── Latest Change Rollback
│   ├── Undo most recent context update
│   ├── Restore from automatic backup
│   ├── Validate rollback success
│   └── Update change history
│
├── Specific Update Rollback
│   ├── Rollback identified by update ID
│   ├── Handle dependent changes
│   ├── Resolve rollback conflicts
│   └── Maintain context integrity
│
├── Point-in-Time Rollback
│   ├── Rollback to specific date/time
│   ├── Multiple update coordination
│   ├── Dependency chain handling
│   └── Comprehensive validation
│
└── Selective Rollback
    ├── Rollback specific files only
    ├── Rollback specific sections only
    ├── Preserve approved changes
    └── Custom rollback scenarios
```

## 🚀 Advanced Update Features

### Smart Content Merging
Intelligent merging of context updates with conflict resolution:

```
Merge Capabilities:
├── Automatic Merging
│   ├── Non-conflicting changes auto-merged
│   ├── Cross-reference updates coordinated
│   ├── Format consistency maintained
│   └── Validation requirements met
│
├── Conflict Detection
│   ├── Content overlap identification
│   ├── Cross-reference conflicts
│   ├── Semantic conflict detection
│   └── Priority conflict resolution
│
├── Manual Resolution
│   ├── Interactive conflict resolution
│   ├── Side-by-side comparison
│   ├── Expert guidance for decisions
│   └── Resolution validation
│
└── Merge Validation
    ├── Post-merge integrity checking
    ├── Context effectiveness testing
    ├── User acceptance confirmation
    └── Success criteria validation
```

### Context Consistency Maintenance
Ensure updates maintain consistency across context hierarchy:

```
Consistency Checks:
├── Cross-Reference Validation
│   ├── All references still valid
│   ├── Bidirectional link consistency
│   ├── Navigation path integrity
│   └── Dead link detection
│
├── Content Consistency
│   ├── Terminology consistency across files
│   ├── Information duplication detection
│   ├── Contradictory information identification
│   └── Completeness gap detection
│
├── Hierarchy Integrity
│   ├── Layer relationship preservation
│   ├── Inheritance chain validation
│   ├── Context loading order maintained
│   └── Dependency chain integrity
│
└── Format Compliance
    ├── Markdown syntax validation
    ├── Cross-reference format consistency
    ├── Header hierarchy compliance
    └── Metadata format validation
```

## 📊 Update Analytics & Insights

### Update Pattern Analysis
Track context update patterns for optimization insights:

```
Pattern Analytics:
├── Update Frequency
│   ├── Which context areas change most often
│   ├── Update timing patterns
│   ├── Seasonal update trends
│   └── User update behavior patterns
│
├── Change Impact Analysis
│   ├── Average impact scope of updates
│   ├── Most common update types
│   ├── Update success rates
│   └── Rollback frequency analysis
│
├── Content Evolution
│   ├── Context growth over time
│   ├── Information freshness tracking
│   ├── Content quality improvements
│   └── User satisfaction trends
│
└── Optimization Insights
    ├── Update efficiency improvements
    ├── Context architecture optimizations
    ├── Workflow optimization opportunities
    └── Tool integration enhancements
```

### Performance Impact Tracking
Monitor how updates affect context system performance:

```
Performance Metrics:
├── Update Performance
│   ├── Update execution time
│   ├── Validation performance
│   ├── Rollback performance
│   └── User experience impact
│
├── Context Effectiveness
│   ├── Response quality after updates
│   ├── Context utilization changes
│   ├── User satisfaction changes
│   └── Productivity impact measurement
│
├── System Health
│   ├── Context loading performance
│   ├── Navigation responsiveness
│   ├── Search effectiveness
│   └── Integration stability
│
└── Resource Usage
    ├── Token usage optimization
    ├── Storage efficiency
    ├── Memory usage patterns
    └── Processing overhead
```

## 🎯 Integration with Context System

### Context Generation Integration
Updates work seamlessly with context generation:
- New consultation results can trigger targeted updates
- Context generation patterns inform update recommendations
- Update history influences future context generation strategies

### Navigation System Integration  
Updates automatically refresh navigation systems:
- Updated cross-references immediately available in navigation
- Changed content reflected in search results
- Navigation analytics updated with new content

### Testing Framework Integration
Updates trigger appropriate context validation:
- Automated testing of updated context effectiveness
- Regression testing to ensure no functionality loss
- Performance testing to validate update impact

### Status Monitoring Integration
Updates contribute to context health monitoring:
- Update frequency and success rates tracked
- Context freshness metrics updated
- Overall system health scores adjusted

---

**Remember**: Context updates should be surgical and validated. The goal is to keep your context system current and accurate while maintaining the integrity and effectiveness that makes Claude truly understand your project.