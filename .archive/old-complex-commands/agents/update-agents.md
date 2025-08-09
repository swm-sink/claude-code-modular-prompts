---
name: update-agents
description: Refresh agent knowledge from evolving project context and patterns
usage: "update-agents [agent-name|all] [--source=context|consultation|git-history] [--incremental|--full-refresh]"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Grep, Glob, LS, TodoWrite]
category: agents
argument-hint: "[agent-name|all] [--update-options]"
version: "1.0"
---

# Update Agents: Keep Specialized Agents Current with Project Evolution

## Purpose: Dynamic Agent Knowledge Management

The `/update-agents` command keeps your specialized agents synchronized with your evolving project, ensuring they maintain current understanding of your architecture, patterns, conventions, and domain knowledge as your codebase grows and changes.

**Agent Update Philosophy**: Continuous learning from project evolution, incremental knowledge enhancement, performance-preserving updates, validation of improved effectiveness, transparent change tracking.

## 🎯 Intelligent Update System

### Project Evolution Detection
- **Change Analysis**: Automatically detect significant project changes since last update
- **Pattern Recognition**: Identify new patterns, conventions, and architectural developments
- **Context Currency**: Ensure agent knowledge reflects current project state
- **Performance Impact**: Measure how project changes affect agent effectiveness

### Smart Update Strategies
- **Incremental Updates**: Add new knowledge without disrupting existing capabilities
- **Full Refresh**: Complete agent knowledge rebuilding for major project changes
- **Selective Updates**: Update specific knowledge areas based on detected changes
- **Rollback Safety**: Maintain previous agent versions for safe rollback if needed

## 🔄 Update Sources and Triggers

### Context Layer Updates
```bash
/update-agents all --source=context --layers=architecture,domain,workflow
```

**Context Sources**:
- **Architecture Context**: Updated system design patterns and framework changes
- **Domain Context**: New business rules, terminology, and domain model evolution
- **Workflow Context**: Changed development processes, testing strategies, deployment patterns
- **Technical Context**: New dependencies, API changes, performance requirements

### Consultation Integration
```bash
/update-agents all --source=consultation --phase=recent
```

**Consultation-Based Updates**:
- **New Consultation Results**: Integrate insights from recent `/begin-consultation` sessions
- **User Feedback Integration**: Incorporate user corrections and preference changes
- **Interactive Refinements**: Apply user-approved modifications to agent knowledge
- **Requirement Evolution**: Update agents based on changed project requirements

### Git History Analysis
```bash
/update-agents all --source=git-history --since=last-update
```

**Code Evolution Tracking**:
- **Pattern Changes**: Detect new coding patterns and architectural shifts
- **Convention Evolution**: Track changes in naming conventions and code organization
- **Framework Updates**: Identify framework version changes and new feature usage
- **Team Practice Changes**: Recognize evolving development and review practices

## 🤖 Agent-Specific Update Procedures

### Core Coordination Agent Updates

**🏗️ Architecture Agent Updates**
```bash
/update-agents architecture --source=context --focus=system-design
```

**Update Focus Areas**:
1. **Framework Evolution** (2-3 minutes)
   - Analyze new framework versions and feature adoption
   - Update architectural patterns and best practices
   - Refresh performance and scalability knowledge
   - Integrate new integration patterns and APIs

2. **System Growth Patterns** (2-3 minutes)
   - Learn from system scaling and evolution patterns
   - Update understanding of bottlenecks and optimization strategies
   - Refresh knowledge of deployment and infrastructure changes
   - Integrate new monitoring and observability patterns

**Update Success Criteria**:
- Architecture recommendations reflect current project state (>98%)
- New framework features and patterns integrated (100%)
- Performance guidance updated with current requirements (>95%)
- Integration patterns match current system architecture (>98%)

**⚙️ Code Generation Agent Updates**
```bash
/update-agents code-generation --source=git-history --pattern-analysis=deep
```

**Update Focus Areas**:
1. **Code Pattern Evolution** (3-4 minutes)
   - Analyze recent code changes for new patterns and conventions
   - Update component templates and generation patterns
   - Refresh understanding of project-specific abstractions
   - Integrate new utility functions and helper patterns

2. **Style and Convention Changes** (2-3 minutes)
   - Update coding style preferences and formatting rules
   - Refresh naming conventions and organizational patterns
   - Integrate new linting rules and quality standards
   - Update error handling and logging patterns

**Update Success Criteria**:
- Generated code matches current project conventions (>98%)
- New patterns and abstractions properly integrated (100%)
- Code quality maintains or improves project standards (>95%)
- Integration with existing codebase remains seamless (>98%)

**🧪 Testing Agent Updates**
```bash
/update-agents testing --source=consultation --focus=strategy-evolution
```

**Update Focus Areas**:
1. **Testing Strategy Evolution** (3-4 minutes)
   - Update testing frameworks and tool preferences
   - Refresh understanding of coverage requirements and quality gates
   - Integrate new testing patterns and best practices
   - Update performance and reliability testing approaches

2. **TDD Enforcement Enhancement** (2-3 minutes)
   - Refine TDD workflow based on team feedback and results
   - Update code deletion penalty criteria and exceptions
   - Refresh understanding of test maintenance and refactoring
   - Integrate new test automation and CI/CD integration patterns

**Update Success Criteria**:
- TDD enforcement aligned with current team practices (100%)
- Testing strategy matches current project requirements (>98%)
- Quality gates reflect current standards and expectations (>95%)
- Test generation follows current frameworks and patterns (>98%)

**🔍 Debugging Agent Updates**
```bash
/update-agents debugging --source=git-history --error-pattern-analysis=comprehensive
```

**Update Focus Areas**:
1. **Error Pattern Learning** (3-4 minutes)
   - Analyze recent error reports and resolution patterns
   - Update knowledge of common failure modes and root causes
   - Refresh debugging strategies for new components and integrations
   - Integrate new monitoring and logging patterns

2. **Diagnostic Tool Integration** (2-3 minutes)
   - Update knowledge of debugging tools and techniques
   - Refresh understanding of performance profiling and analysis
   - Integrate new observability and monitoring capabilities
   - Update incident response and escalation procedures

**Update Success Criteria**:
- Error diagnosis accuracy improves with historical learning (>95%)
- Debugging strategies updated for current system architecture (>98%)
- Resolution recommendations reflect current tools and practices (>95%)
- Performance issue detection enhanced with new patterns (>90%)

### Specialized Function Agent Updates

**📝 Documentation Agent Updates**
```bash
/update-agents documentation --source=context --standards-refresh=comprehensive
```

**Update Focus Areas**:
1. **Documentation Standards Evolution** (2-3 minutes)
   - Update style guides and formatting preferences
   - Refresh audience understanding and communication needs
   - Integrate new documentation tools and automation
   - Update API documentation and specification standards

2. **Content Strategy Enhancement** (2-3 minutes)
   - Learn from user feedback on documentation effectiveness
   - Update understanding of information architecture needs
   - Refresh knowledge of onboarding and maintenance documentation
   - Integrate new knowledge management and search patterns

**🏢 Domain Expert Agent Updates**
```bash
/update-agents domain --source=consultation --business-knowledge=deep-refresh
```

**Update Focus Areas**:
1. **Business Logic Evolution** (3-4 minutes)
   - Update understanding of business rules and process changes
   - Refresh domain terminology and concept definitions
   - Integrate new business requirements and constraints
   - Update data model understanding and relationships

2. **Industry Context Refresh** (2-3 minutes)
   - Update knowledge of industry trends and regulatory changes
   - Refresh understanding of competitive landscape and best practices
   - Integrate new compliance and governance requirements
   - Update user journey and experience patterns

## 📊 Update Process Management

### Incremental Update Process
```bash
/update-agents architecture --incremental --since=last-week
```

**Incremental Update Flow**:
1. **Change Detection** (30 seconds)
   - Scan project for changes since last update
   - Identify areas of significant evolution
   - Prioritize updates based on change impact
   - Estimate update time and complexity

2. **Knowledge Integration** (2-4 minutes per agent)
   - Add new knowledge without disrupting existing capabilities
   - Validate new knowledge against existing patterns
   - Resolve conflicts between old and new understanding
   - Test integration effectiveness

3. **Performance Validation** (1-2 minutes)
   - Verify agent performance maintains or improves
   - Test agent responses with updated knowledge
   - Validate specialization boundaries remain intact
   - Confirm integration with other agents remains effective

### Full Refresh Process
```bash
/update-agents all --full-refresh --backup-current-state
```

**Full Refresh Flow**:
1. **Current State Backup** (1 minute)
   - Save current agent configurations and knowledge
   - Create rollback checkpoints for safe recovery
   - Document current performance baselines
   - Preserve successful patterns and capabilities

2. **Comprehensive Analysis** (3-5 minutes)
   - Perform deep analysis of current project state
   - Extract all current patterns, conventions, and knowledge
   - Identify areas where agents may have become outdated
   - Plan comprehensive knowledge refresh strategy

3. **Agent Rebuilding** (4-8 minutes per agent)
   - Rebuild agent knowledge from current project state
   - Integrate all accumulated learnings and feedback
   - Validate agent effectiveness with comprehensive testing
   - Ensure agent specialization and coordination remain optimal

4. **Performance Comparison** (2-3 minutes)
   - Compare refreshed agents against previous performance
   - Validate improvements in accuracy and relevance
   - Confirm no regression in agent capabilities
   - Document performance improvements and changes

## 🔍 Update Validation and Quality Assurance

### Pre-Update Assessment
```bash
/update-agents all --assess-update-needs --report-recommendations
```

**Assessment Process**:
- **Change Impact Analysis**: Measure how project changes affect current agent knowledge
- **Performance Gap Detection**: Identify areas where agents may be underperforming
- **Knowledge Currency Evaluation**: Assess how outdated agent knowledge has become
- **Update Priority Matrix**: Rank agents by update urgency and potential impact

### Post-Update Validation
```bash
/update-agents architecture --validate-update --test-scenarios=comprehensive
```

**Validation Process**:
- **Response Quality Testing**: Verify updated agents provide improved responses
- **Performance Benchmarking**: Compare performance before and after updates
- **Integration Testing**: Ensure updated agents coordinate effectively with others
- **Regression Detection**: Confirm no loss of previous capabilities

### Rollback Procedures
```bash
/update-agents architecture --rollback --to-checkpoint=pre-update-20240805
```

**Rollback Safety**:
- **Automatic Checkpointing**: Every update creates automatic rollback points
- **Performance-Based Rollback**: Automatically rollback if performance degrades
- **User-Initiated Rollback**: Manual rollback when updates don't meet expectations
- **Selective Rollback**: Roll back specific knowledge areas while preserving improvements

## ⚡ Smart Update Scheduling and Automation

### Automated Update Detection
```bash
/update-agents --schedule=weekly --auto-detect-changes --threshold=significant
```

**Automation Features**:
- **Change Detection Monitoring**: Continuously monitor for significant project changes
- **Performance Degradation Alerts**: Automatically trigger updates when agent performance drops
- **Scheduled Maintenance**: Regular update cycles to maintain knowledge currency
- **Event-Triggered Updates**: Updates triggered by major project milestones or releases

### Update Recommendations
```bash
/update-agents --recommend --analysis=comprehensive
```

**Recommendation System**:
- **Priority-Based Suggestions**: Recommend updates based on impact and urgency
- **Performance-Driven Updates**: Suggest updates for agents showing performance decline
- **Context Change Alerts**: Notify when significant context changes require updates
- **Seasonal Maintenance**: Recommend comprehensive updates at regular intervals

## 📈 Update Impact Analysis and Reporting

### Update Effectiveness Reports
```bash
/update-agents all --report=effectiveness --period=post-update
```

**Report Components**:
1. **Performance Improvements**: Quantified improvements in agent accuracy and speed
2. **Knowledge Currency**: How current agent knowledge now is compared to project state
3. **User Satisfaction Changes**: Impact of updates on user experience and satisfaction
4. **Integration Effectiveness**: How well updated agents work together
5. **Recommendation Quality**: Improvement in the usefulness of agent recommendations

### Trend Analysis
```bash
/update-agents --trend-analysis --period=6-months --focus=knowledge-decay
```

**Analysis Features**:
- **Knowledge Decay Patterns**: Track how agent knowledge becomes outdated over time
- **Update Frequency Optimization**: Identify optimal update schedules for different agents
- **Performance Evolution**: Track agent performance evolution through updates
- **Project Growth Impact**: Understand how project growth affects agent update needs

## ⚡ Usage Examples

### Regular Maintenance Updates
```bash
# Weekly incremental updates
/update-agents all --incremental --source=git-history --since=last-week

# Monthly comprehensive updates
/update-agents all --source=context,consultation --comprehensive
```

### Targeted Agent Updates
```bash
# Update specific agents based on recent changes
/update-agents architecture testing --source=consultation --recent-changes

# Update agents after major framework upgrade
/update-agents code-generation architecture --source=context --framework-upgrade
```

### Performance-Driven Updates
```bash
# Update underperforming agents
/update-agents --performance-threshold=90% --source=all

# Refresh agents based on user feedback
/update-agents documentation domain --source=consultation --user-feedback
```

### Automated Update Management
```bash
# Set up automated update monitoring
/update-agents --monitor --auto-update=incremental --notify=significant-changes

# Schedule regular maintenance updates
/update-agents --schedule="weekly-incremental,monthly-comprehensive"
```

## 🔗 Integration with Agent Management

### Seamless Workflow Integration
- **Performance Monitoring Integration**: Updates triggered by performance degradation from `/test-agents`
- **Activation Preparation**: Updated agents ready for immediate activation
- **Coordination Optimization**: Updates improve multi-agent collaboration effectiveness
- **Context Synchronization**: Updates automatically sync with evolving project context

### Quality Assurance Integration
- **Pre-Update Testing**: Validate agent state before applying updates
- **Post-Update Validation**: Comprehensive testing after updates
- **Performance Comparison**: Before/after analysis of agent capabilities
- **Rollback Triggers**: Automatic rollback if updates cause performance regression

## 🚀 Success Criteria

**Knowledge Currency**: Agents maintain current understanding of project evolution (>95% accuracy)
**Performance Enhancement**: Updates improve or maintain agent effectiveness (no degradation)
**Update Efficiency**: Updates complete quickly without disrupting agent availability (<5 minutes downtime)
**Quality Assurance**: All updates validated before deployment with rollback safety

**🎯 Final Result**: Your specialized agents remain current and effective as your project evolves, continuously learning from project changes and maintaining peak performance in providing project-specific expertise.