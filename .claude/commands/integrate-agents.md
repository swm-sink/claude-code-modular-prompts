---
name: /integrate-agents
description: Execute and coordinate specialized agents during consultation phases
usage: "/integrate-agents [phase] [agent-name] [project-path]"
allowed-tools: [Read, Write, Edit, LS, Glob, Grep, Bash, TodoWrite]
category: integration
version: "1.0"
---

# Agent Integration System: Execute Specialized AI Agents

## Purpose
This command provides the execution layer for specialized agents, bridging the coordination logic with actual agent implementations. It manages agent invocation, output processing, and integration with the consultation workflow.

## 🎯 How Agent Integration Works
The system executes specialized agents through a structured invocation mechanism:
1. **Agent Loading** - Dynamically loads agent definitions from `.claude/agents/` 
2. **Context Preparation** - Prepares project-specific context for agent analysis
3. **Agent Execution** - Invokes agents with specialized prompts and constraints
4. **Output Processing** - Processes agent outputs and integrates with session state
5. **Handoff Management** - Coordinates information flow between agents

## 🤖 Supported Agent Types

### Context Engineer (`context-engineer`)
**Purpose**: Analyzes project architecture and creates hierarchical context structures
**Input**: Project structure, framework detection, existing documentation
**Output**: Context hierarchy, navigation patterns, CLAUDE.md enhancements

### Command Builder (`command-builder`) 
**Purpose**: Creates project-specific Claude Code commands based on patterns
**Input**: Domain analysis, workflow patterns, user requirements
**Output**: Custom slash commands, YAML configurations, scaffolding templates

### Research Validator (`research-validator`)
**Purpose**: Validates patterns and decisions with evidence-based research
**Input**: Technical claims, pattern choices, architecture decisions  
**Output**: Evidence reports, source validation, credibility assessments

## ⚡ Advanced Agent Invocation Patterns

### Sequential Phase Execution with Validation
```bash
# Execute agents in sequence with quality gates
./scripts/integrate-agents.sh phase-1 /path/to/project
# → Runs Context Engineer + Research Validator with handoff validation
# → Quality gate: Technical architecture must be validated before Phase 2

./scripts/integrate-agents.sh phase-2 /path/to/project  
# → Runs Command Builder + Research Validator with domain validation
# → Quality gate: Domain patterns must be evidence-based before Phase 3

./scripts/integrate-agents.sh phase-3 /path/to/project
# → Runs all agents for final context generation and validation
# → Quality gate: All outputs must pass cross-agent consistency checks
```

### Parallel Agent Execution (Advanced)
```bash
# Execute agents in parallel for faster analysis
./scripts/integrate-agents.sh parallel-phase-1 /path/to/project
# → Context Engineer and Research Validator run simultaneously
# → Results merged with conflict detection and resolution

# Execute all agents with dependency management
./scripts/integrate-agents.sh orchestrate-all /path/to/project
# → Intelligent scheduling based on agent dependencies
# → Automatic conflict resolution and quality assurance
```

### Individual Agent Invocation with Context Chaining
```bash
# Invoke agents with context inheritance
./scripts/invoke-agent.sh context-engineer /path/to/project --inherit-session
./scripts/invoke-agent.sh command-builder /path/to/project --use-context technical-architecture
./scripts/invoke-agent.sh research-validator /path/to/project --validate-claims all
```

### Testing and Validation Modes
```bash
# Test agent integration without affecting session state
./scripts/integrate-agents.sh test-mode /path/to/project
# → Dry-run execution with validation reporting

# Validate agent definitions and constraints
./scripts/integrate-agents.sh validate-agents
# → Check agent boundary compliance and definition consistency
```

## 📊 Integration with Consultation System

### Session State Integration
All agent executions are tracked in `.claude/consultation-state.json`:
- Agent invocation timestamps and parameters
- Agent output summaries and key findings
- Cross-agent information dependencies
- Quality scores and validation results

### Coordination Integration  
Seamlessly integrates with `/coordinate-agents` command:
- Agents activated based on consultation phase
- Information flows managed through session state
- Quality gates enforced before phase transitions

## 🔧 Implementation Architecture

### Agent Definition Format
Agents are defined in `.claude/agents/[agent-name].md` with:
- Specialized analysis prompts and constraints  
- Input/output specifications
- Quality validation criteria 
- Integration protocols

### Execution Environment
- Project context automatically loaded and prepared
- Agent constraints and boundaries enforced
- Output validation and formatting applied
- Session state updated with execution results

## 🚨 Quality Assurance

### Agent Boundary Enforcement
- Strict specialization boundaries prevent scope creep
- Input validation ensures agents receive appropriate data
- Output validation confirms expected deliverable format
- Cross-agent consistency checks prevent conflicting advice

### Error Handling
- Agent execution failures handled gracefully
- Partial results preserved for manual review
- Session state maintained even during errors
- Recovery mechanisms for interrupted consultations

## Usage Examples

### Full Phase Execution
```bash
# Execute all agents for technical analysis phase
/integrate-agents phase-1 all /path/to/project
```

### Targeted Agent Analysis  
```bash
# Execute specific agent for focused analysis
/integrate-agents context-engineer /path/to/project
```

### Integration Testing
```bash
# Test agent integration system
/integrate-agents test-mode validation
```