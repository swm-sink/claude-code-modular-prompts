# Context-Prime-Mega Design Specification

**Date**: 2025-07-19  
**Task**: Design context-prime-mega with multi-agent sequential analysis  
**Status**: ✅ COMPLETE  

## 🎯 Core Requirements

### Primary Function
Context-prime-mega performs comprehensive codebase analysis using multiple sequential agents, with each agent documenting detailed findings for compilation into a master analysis report.

### Key Features
1. **Codebase Size Assessment** - Auto-detect or ask user about codebase complexity
2. **Agent Allocation** - Determine optimal number of analysis agents
3. **Sequential Analysis** - Agents work sequentially, building on previous findings
4. **Findings Documentation** - Each agent writes detailed analysis documents
5. **Critical Analysis** - Final compilation includes issues and recommendations

## 📊 Codebase Size Detection Logic

### Auto-Detection Metrics
```xml
<codebase_assessment>
  <size_categories>
    <small>
      <criteria>< 50 files, < 10k LOC, < 5 directories</criteria>
      <agents>2 agents (Structure + Issues)</agents>
      <timeframe>15 minutes total</timeframe>
    </small>
    <medium>
      <criteria>50-500 files, 10k-100k LOC, 5-20 directories</criteria>
      <agents>4 agents (Structure, Dependencies, Patterns, Issues)</agents>
      <timeframe>45 minutes total</timeframe>
    </medium>
    <large>
      <criteria>500-2000 files, 100k-500k LOC, 20-50 directories</criteria>
      <agents>6 agents (Architecture, Dependencies, Security, Performance, Patterns, Issues)</agents>
      <timeframe>90 minutes total</timeframe>
    </large>
    <enterprise>
      <criteria>> 2000 files, > 500k LOC, > 50 directories</criteria>
      <agents>8 agents (Architecture, Services, Data, Security, Performance, Quality, Patterns, Issues)</agents>
      <timeframe>2+ hours with checkpoints</timeframe>
    </enterprise>
  </size_categories>
  
  <user_override>
    <prompt>"Detected [SIZE] codebase. Use [X] agents? (y/n/custom)"</prompt>
    <custom_options>Allow user to specify number of agents (1-12)</custom_options>
  </user_override>
</codebase_assessment>
```

## 🤖 Agent Specialization Matrix

### Agent Types by Codebase Size

#### Small Codebase (2 agents)
1. **Structure Agent**: Project architecture and organization
2. **Issues Agent**: Problems, technical debt, recommendations

#### Medium Codebase (4 agents)  
1. **Structure Agent**: Architecture and directory organization
2. **Dependencies Agent**: External/internal dependencies and integrations
3. **Patterns Agent**: Coding patterns, conventions, best practices
4. **Issues Agent**: Technical debt, security, performance issues

#### Large Codebase (6 agents)
1. **Architecture Agent**: High-level system design and structure
2. **Dependencies Agent**: Package management and integration analysis
3. **Security Agent**: Security vulnerabilities and compliance
4. **Performance Agent**: Performance bottlenecks and optimization
5. **Patterns Agent**: Design patterns and code quality
6. **Issues Agent**: Critical issues and improvement roadmap

#### Enterprise Codebase (8 agents)
1. **Architecture Agent**: System architecture and service design
2. **Services Agent**: Microservices, APIs, and inter-service communication
3. **Data Agent**: Data flow, storage, and data architecture
4. **Security Agent**: Security posture and vulnerability assessment
5. **Performance Agent**: Performance analysis and scalability
6. **Quality Agent**: Code quality, testing, and maintainability
7. **Patterns Agent**: Design patterns and engineering practices
8. **Issues Agent**: Critical issues, technical debt, strategic recommendations

## 🔄 Sequential Execution Workflow

### Phase 1: Assessment and Planning
```xml
<assessment_phase>
  <steps>
    <step order="1">Scan project directory structure and count files/LOC</step>
    <step order="2">Determine codebase size category and agent allocation</step>
    <step order="3">Present recommendation to user and get confirmation</step>
    <step order="4">Initialize agent coordination tracker and findings structure</step>
    <step order="5">Create analysis workspace in agent_comms/context-analysis/</step>
  </steps>
</assessment_phase>
```

### Phase 2: Sequential Agent Analysis
```xml
<agent_execution_phase>
  <execution_pattern>
    <agent_workflow>
      <step order="1">Load previous agent findings (if any)</step>
      <step order="2">Perform specialized analysis in assigned domain</step>
      <step order="3">Document findings in agent-specific report</step>
      <step order="4">Identify integration points with other agent domains</step>
      <step order="5">Pass analysis state to next agent</step>
    </agent_workflow>
    
    <findings_structure>
      <agent_report>
        <header>Agent ID, specialization, analysis timestamp</header>
        <executive_summary>Key findings and critical issues</executive_summary>
        <detailed_analysis>Comprehensive analysis with evidence</detailed_analysis>
        <issues_identified>Problems categorized by severity</issues_identified>
        <recommendations>Specific actionable improvements</recommendations>
        <integration_notes>Notes for subsequent agents</integration_notes>
      </agent_report>
    </findings_structure>
  </execution_pattern>
</agent_execution_phase>
```

### Phase 3: Compilation and Master Report
```xml
<compilation_phase>
  <master_report_generation>
    <step order="1">Aggregate all agent findings into unified structure</step>
    <step order="2">Perform cross-agent analysis for conflicting/reinforcing findings</step>
    <step order="3">Prioritize issues by severity and impact</step>
    <step order="4">Generate executive summary with critical issues</step>
    <step order="5">Create actionable improvement roadmap</step>
    <step order="6">Compile final comprehensive analysis document</step>
  </master_report_generation>
</compilation_phase>
```

## 📋 Document Generation Structure

### Agent-Specific Reports
```
agent_comms/context-analysis-[timestamp]/
├── 00-assessment-report.md           # Initial size assessment
├── 01-agent-[specialization].md      # Individual agent findings
├── 02-agent-[specialization].md      # Next agent findings
├── ...
├── XX-master-analysis-report.md      # Final compilation
└── coordination-tracker.json         # Agent progress tracking
```

### Master Analysis Report Template
```xml
<master_report_structure>
  <executive_summary>
    <codebase_overview>Size, complexity, technology stack</codebase_overview>
    <critical_issues>Top 5 most serious problems requiring immediate attention</critical_issues>
    <overall_health>Health score and key metrics</overall_health>
    <strategic_recommendations>High-level improvement strategy</strategic_recommendations>
  </executive_summary>
  
  <detailed_findings>
    <architecture_analysis>System design, patterns, structure quality</architecture_analysis>
    <technical_debt>Code quality issues, maintenance burden</technical_debt>
    <security_assessment>Vulnerabilities, compliance, risk factors</security_assessment>
    <performance_analysis>Bottlenecks, scalability, optimization opportunities</performance_analysis>
    <dependency_analysis>External dependencies, integration risks</dependency_analysis>
  </detailed_findings>
  
  <improvement_roadmap>
    <immediate_actions>Issues requiring urgent attention (next 30 days)</immediate_actions>
    <short_term_goals>Improvements for next 3 months</short_term_goals>
    <long_term_strategy>Strategic improvements for next 6-12 months</long_term_strategy>
    <resource_requirements>Team, time, and technology needs</resource_requirements>
  </improvement_roadmap>
  
  <appendices>
    <agent_reports>Links to individual agent detailed reports</agent_reports>
    <metrics_summary>Quantitative analysis results</metrics_summary>
    <tool_recommendations>Suggested tools and frameworks</tool_recommendations>
  </appendices>
</master_report_structure>
```

## 🛡️ Safety and Quality Controls

### Agent Coordination Safety
- Maximum 2-hour total execution time with checkpoints
- User can interrupt and resume analysis at any agent boundary
- Progress tracking with estimated completion times
- Automatic backup of findings after each agent

### Quality Assurance
- Each agent must validate findings before proceeding
- Cross-agent consistency checking in compilation phase
- Critical issue validation with evidence requirements
- Final report review with user approval before finalization

## 🎯 Success Metrics

### Analysis Quality
- **Comprehensiveness**: All major codebase aspects covered
- **Actionability**: Specific, implementable recommendations
- **Prioritization**: Issues ranked by impact and effort
- **Evidence**: All findings backed by concrete examples

### User Experience
- **Clarity**: Easy to understand analysis and recommendations
- **Usefulness**: Actionable insights for immediate use
- **Completeness**: No major gaps in analysis coverage
- **Time Efficiency**: Analysis completed within estimated timeframes

This design provides a robust foundation for context-prime-mega that scales from small to enterprise codebases while ensuring comprehensive analysis through specialized sequential agents.