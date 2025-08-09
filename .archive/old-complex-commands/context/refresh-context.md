---
name: refresh-context
description: Refresh and synchronize context with current project state, detecting changes and updating outdated information
usage: "refresh-context [scan|sync|auto|schedule] [--force|--incremental|--validate]"
allowed-tools: [Read, Write, Edit, MultiEdit, LS, Glob, Grep, Bash, TodoWrite]
category: context
version: "1.0"
---

# Refresh Context: Intelligent Context Synchronization System

## Purpose: Keep Context Current with Project Evolution

The `/refresh-context` command automatically detects changes in your project and updates context accordingly, ensuring Claude's understanding stays current as your project evolves. Through intelligent change detection, impact analysis, and selective updates, it maintains context accuracy without manual oversight.

**Refresh Philosophy**: Proactive over reactive, intelligent over blanket, validated over assumed, efficient over exhaustive.

## 🔄 Context Refresh Modes

### Scan Mode
**Usage**: `/refresh-context scan [--deep|--quick|--targeted]`

Comprehensive analysis of project state vs context currency:

```
Project State Analysis:
├── Code Structure Changes
│   ├── New/deleted files and directories
│   ├── File moves and renames
│   ├── Package.json/requirements.txt changes
│   └── Build configuration updates
│
├── Framework & Dependency Changes
│   ├── Framework version updates
│   ├── New package additions
│   ├── Deprecated package removals
│   └── Configuration file modifications
│
├── Team & Process Changes
│   ├── Team member additions/departures
│   ├── Role and responsibility changes
│   ├── Workflow process modifications
│   └── Tool stack updates
│
├── Business Logic Changes
│   ├── New feature implementations
│   ├── API endpoint modifications
│   ├── Data model changes
│   └── Business rule updates
│
└── Documentation Changes
    ├── README updates
    ├── API documentation changes
    ├── Architecture decision records
    └── Process documentation updates
```

**Output**: Change detection report with recommendations for context updates

### Sync Mode
**Usage**: `/refresh-context sync [--preview|--execute|--batch]`

Synchronize context with detected project changes:

```
Synchronization Process:
├── Change Prioritization
│   ├── Critical changes (breaking changes, new features)
│   ├── Important changes (dependency updates, process changes)
│   ├── Minor changes (documentation updates, small tweaks)
│   └── Optional changes (formatting, minor refactoring)
│
├── Context Impact Analysis
│   ├── Foundation context updates needed
│   ├── Domain context modifications required
│   ├── Technical context synchronization
│   ├── Workflow context adjustments
│   └── Agent specialization updates
│
├── Update Execution Plan
│   ├── Dependency-ordered update sequence
│   ├── Cross-reference update coordination
│   ├── Validation checkpoint definitions
│   └── Rollback preparation procedures
│
└── Execution & Validation
    ├── Execute updates in planned sequence
    ├── Validate each update before proceeding
    ├── Test context effectiveness after changes
    └── Confirm successful synchronization
```

### Auto Mode
**Usage**: `/refresh-context auto [--enable|--disable|--configure]`

Automated context refresh based on project activity:

```
Auto-Refresh Triggers:
├── Git Event Triggers
│   ├── After significant commits (configurable threshold)
│   ├── Before/after branch merges
│   ├── After dependency updates
│   └── Before releases/deployments
│
├── File System Triggers
│   ├── Configuration file changes
│   ├── Package/dependency file modifications
│   ├── Documentation updates
│   └── Schema/model file changes
│
├── Time-Based Triggers
│   ├── Daily light refresh (incremental)
│   ├── Weekly comprehensive refresh
│   ├── Monthly deep analysis
│   └── Custom schedule configuration
│
└── User Activity Triggers
    ├── After consultation updates
    ├── Before major context operations
    ├── After manual context modifications
    └── On user request
```

### Schedule Mode
**Usage**: `/refresh-context schedule [--daily|--weekly|--monthly|--custom]`

Scheduled context maintenance with customizable intervals:

```
Refresh Schedules:
├── Daily Refresh (Incremental)
│   ├── Check for recent file changes
│   ├── Update file references
│   ├── Refresh cross-references
│   └── Quick validation check
│
├── Weekly Refresh (Moderate)
│   ├── Dependency change analysis
│   ├── Workflow process updates
│   ├── Team change integration
│   └── Context effectiveness review
│
├── Monthly Refresh (Comprehensive)
│   ├── Deep project analysis
│   ├── Architecture evolution review
│   ├── Business logic updates
│   └── Complete context validation
│
└── Custom Schedule
    ├── User-defined intervals
    ├── Event-based triggers
    ├── Workload-based scheduling
    └── Team workflow integration
```

## 🔍 Intelligent Change Detection

### Code Structure Analysis
Detect structural changes that affect context accuracy:

```
Structure Change Detection:
├── Directory Structure Changes
│   ├── New directories requiring context
│   ├── Deleted directories with context references
│   ├── Moved directories affecting navigation
│   └── Renamed directories breaking links
│
├── File Organization Changes
│   ├── New important files (configs, schemas, docs)
│   ├── Deleted files referenced in context
│   ├── File moves affecting context paths
│   └── File renames breaking references
│
├── Package & Dependencies
│   ├── New frameworks requiring context updates
│   ├── Removed dependencies needing cleanup
│   ├── Version updates affecting best practices
│   └── Configuration changes impacting workflow
│
└── Build & Configuration
    ├── Build system changes
    ├── Environment configuration updates
    ├── CI/CD pipeline modifications
    └── Deployment configuration changes
```

### Content Currency Analysis
Evaluate how current context information remains:

```
Currency Assessment:
├── Technical Information Currency
│   ├── Framework version alignment
│   ├── API documentation accuracy
│   ├── Architecture diagram currency
│   └── Deployment instruction validity
│
├── Business Logic Currency
│   ├── Business rule accuracy
│   ├── User workflow relevance
│   ├── Data model consistency
│   └── Feature description accuracy
│
├── Process Information Currency
│   ├── Development workflow accuracy
│   ├── Quality standard relevance
│   ├── Team role descriptions
│   └── Communication process validity
│
└── Reference Link Currency
    ├── Internal link validity
    ├── External link accessibility
    ├── Cross-reference accuracy
    └── Navigation path effectiveness
```

### Impact-Driven Refresh Strategy
Prioritize refresh activities based on impact to context effectiveness:

```
Impact Priority Matrix:
├── Critical Impact (Immediate Refresh Required)
│   ├── Breaking changes affecting core context
│   ├── New major features requiring context
│   ├── Framework changes affecting patterns
│   └── Workflow changes affecting team processes
│
├── High Impact (Refresh Within 24 Hours)
│   ├── Dependency updates affecting recommendations
│   ├── Team changes affecting responsibilities
│   ├── API changes affecting integration patterns
│   └── Security updates affecting guidelines
│
├── Medium Impact (Refresh Within Week)
│   ├── Documentation updates
│   ├── Minor configuration changes
│   ├── Performance optimizations
│   └── Code style guideline updates
│
└── Low Impact (Refresh During Scheduled Maintenance)
    ├── Formatting changes
    ├── Comment updates
    ├── Minor refactoring
    └── Non-functional improvements
```

## 🔧 Synchronization Intelligence

### Smart Update Strategies
Intelligent approaches to keeping context current:

```
Update Strategy Selection:
├── Incremental Updates
│   ├── Update only changed sections
│   ├── Preserve existing cross-references
│   ├── Minimal disruption to context
│   └── Fast execution for small changes
│
├── Targeted Updates
│   ├── Focus on specific context layers
│   ├── Update related context files together
│   ├── Coordinate cross-layer references
│   └── Validate layer consistency
│
├── Comprehensive Refresh
│   ├── Full context rebuild from current state
│   ├── Update all cross-references
│   ├── Validate complete context hierarchy
│   └── Ensure maximum accuracy
│
└── Hybrid Approach
    ├── Critical changes get immediate targeted updates
    ├── Moderate changes batched for efficiency
    ├── Minor changes included in scheduled refresh
    └── User approval for significant changes
```

### Conflict Resolution
Handle conflicts between current project state and existing context:

```
Conflict Resolution Strategies:
├── Automatic Resolution
│   ├── Clear conflicts with obvious solutions
│   ├── Non-breaking additive changes
│   ├── Format standardization
│   └── Reference link updates
│
├── User-Guided Resolution
│   ├── Semantic conflicts requiring judgment
│   ├── Process changes affecting workflow
│   ├── Architecture decisions requiring approval
│   └── Business logic modifications
│
├── Context Merge Options
│   ├── Preserve current context (ignore changes)
│   ├── Accept project changes (update context)
│   ├── Merge both (combined approach)
│   └── Custom resolution (user-defined)
│
└── Conflict Documentation
    ├── Track resolution decisions
    ├── Document reasoning for choices
    ├── Create precedents for similar conflicts
    └── Enable conflict pattern recognition
```

### Validation Integration
Ensure refresh operations maintain context quality:

```
Refresh Validation Framework:
├── Pre-Refresh Validation
│   ├── Current context state assessment
│   ├── Change impact analysis
│   ├── Refresh strategy validation
│   └── Risk assessment and mitigation
│
├── During-Refresh Monitoring
│   ├── Update progress tracking
│   ├── Error detection and handling
│   ├── Conflict resolution monitoring
│   └── Performance impact assessment
│
├── Post-Refresh Validation
│   ├── Context effectiveness testing
│   ├── Cross-reference integrity check
│   ├── Navigation functionality validation
│   └── User acceptance confirmation
│
└── Continuous Monitoring
    ├── Context currency tracking
    ├── Refresh effectiveness measurement
    ├── User satisfaction monitoring
    └── System performance impact
```

## 📊 Refresh Analytics & Insights

### Change Pattern Analysis
Track patterns in project evolution and context refresh needs:

```
Pattern Analytics:
├── Change Frequency Patterns
│   ├── Most frequently changing project areas
│   ├── Seasonal patterns in project evolution
│   ├── Team activity patterns affecting context
│   └── Feature development cycle patterns
│
├── Context Impact Patterns
│   ├── Which changes most affect context accuracy
│   ├── Context areas requiring frequent updates
│   ├── Cross-layer impact patterns
│   └── User behavior patterns with context
│
├── Refresh Effectiveness
│   ├── Refresh strategy success rates
│   ├── Time between refresh and context usage
│   ├── User satisfaction with refreshed context
│   └── Context accuracy improvement metrics
│
└── Optimization Opportunities
    ├── Refresh timing optimization
    ├── Update strategy refinement
    ├── Automation opportunity identification
    └── Resource efficiency improvements
```

### Context Health Tracking
Monitor context freshness and accuracy over time:

```
Health Metrics:
├── Freshness Indicators
│   ├── Time since last refresh
│   ├── Number of unprocessed changes
│   ├── Context accuracy degradation rate
│   └── User-reported accuracy issues
│
├── Currency Measurements
│   ├── Information age in context files
│   ├── Reference link validity rates
│   ├── Technical information accuracy
│   └── Process information relevance
│
├── Synchronization Quality
│   ├── Successful refresh rate
│   ├── Conflict resolution success
│   ├── Post-refresh effectiveness
│   └── User satisfaction with updates
│
└── Performance Impact
    ├── Refresh operation efficiency
    ├── Context loading performance
    ├── User productivity impact
    └── System resource utilization
```

## 🚀 Advanced Refresh Features

### Machine Learning Integration
Intelligent prediction of refresh needs:

```
ML-Enhanced Features:
├── Change Impact Prediction
│   ├── Predict which project changes will affect context
│   ├── Estimate refresh priority and urgency
│   ├── Recommend optimal refresh strategies
│   └── Identify potential conflicts before they occur
│
├── Pattern Recognition
│   ├── Learn from historical change patterns
│   ├── Predict future refresh needs
│   ├── Optimize refresh timing
│   └── Improve change detection accuracy
│
├── User Behavior Analysis
│   ├── Learn from user refresh preferences
│   ├── Predict when users need fresh context
│   ├── Optimize refresh schedules for user productivity
│   └── Personalize refresh recommendations
│
└── Context Quality Optimization
    ├── Learn which refresh strategies work best
    ├── Predict context effectiveness after refresh
    ├── Optimize resource allocation for refresh
    └── Improve overall context system performance
```

### Integration with Development Tools
Seamless integration with development workflow tools:

```
Tool Integrations:
├── Version Control Integration
│   ├── Git hook triggers for automatic refresh
│   ├── Branch-based refresh strategies
│   ├── Commit analysis for change detection
│   └── Merge conflict resolution assistance
│
├── CI/CD Pipeline Integration
│   ├── Build-triggered context refresh
│   ├── Deployment-time context validation
│   ├── Test result integration for context accuracy
│   └── Release preparation context updates
│
├── Project Management Integration
│   ├── Issue tracker integration for feature context
│   ├── Sprint planning integration for refresh scheduling
│   ├── Team change notifications for context updates
│   └── Workflow tool integration for process updates
│
└── Documentation Tool Integration
    ├── Wiki integration for business context updates
    ├── API documentation sync for technical context
    ├── Architecture tool integration for diagram updates
    └── Knowledge base integration for process context
```

## 🎯 Integration with Context System

### Context Generation Integration
Refresh operations enhance context generation:
- Fresh project analysis improves future context generation
- Refresh patterns inform context architecture decisions
- Change detection improves consultation accuracy

### Update Management Integration
Coordinated refresh and update operations:
- Refresh identifies what needs updating
- Update operations can trigger targeted refresh
- Change tracking shared between systems

### Testing Framework Integration
Refresh operations validate context effectiveness:
- Post-refresh testing ensures context quality
- Refresh impact measured through testing metrics
- Testing results guide future refresh strategies

### Status Monitoring Integration
Refresh contributes to overall context health:
- Refresh frequency and success tracked in status
- Context freshness metrics updated by refresh
- Overall system health influenced by refresh quality

---

**Remember**: Context refresh should be proactive and intelligent. The goal is to keep Claude's understanding of your project current without overwhelming users with constant updates or degrading context quality through excessive automation.