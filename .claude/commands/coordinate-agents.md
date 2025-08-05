---
name: /coordinate-agents
description: Orchestrate specialized agents for 3-phase consultation workflow
usage: "/coordinate-agents [phase-1|phase-2|phase-3] [project-path]"
allowed-tools: [Read, Write, Edit, LS, Glob, Grep, TodoWrite]
category: coordination
version: "1.0"
---

# Agent Coordination System: Orchestrate Specialized AI Agents

## Purpose
This command orchestrates specialized agents through the 3-phase consultation workflow, managing handoffs and maintaining session state for the Claude Context Architect system. Each agent operates within strict specialization boundaries to provide expert-level analysis and recommendations.

## 🎯 How Agent Coordination Works
The system coordinates multiple specialized AI agents, each with unique expertise:
1. **Sequential Phase Execution** - Agents activate during their specialized phase
2. **Intelligent Handoffs** - Information flows between agents with validation
3. **Session Persistence** - State maintained across consultation sessions  
4. **User Control** - Approval required at each major decision point
5. **Quality Assurance** - Each agent validates outputs within their domain

## 🤖 Specialized Agent System

### Phase 1: Technical Analysis (Context Engineer + Research Validator)
**Context Engineer** analyzes project architecture and creates hierarchical context structures.
**Research Validator** validates technical patterns with evidence-based research.

**Key Questions Generated:**
- What framework does your project use? (React/Vue/Angular, Django/Flask/Rails, etc.)
- How is your project structured? (monorepo/microservices, frontend/backend separation)
- What testing strategies do you follow? (unit/integration/e2e coverage)
- What are your performance requirements and constraints?

### Phase 2: Domain Intelligence (Command Builder + Research Validator)  
**Command Builder** creates project-specific commands based on domain patterns.
**Research Validator** ensures domain terminology follows industry standards.

**Key Questions Generated:**
- What business domain does your project serve? (e-commerce, fintech, healthcare, etc.)
- What are your key business entities and relationships?
- How do users typically interact with your application?
- What external services and APIs do you integrate with?

### Phase 3: Context Generation (Context Engineer + All Agents)
**Context Engineer** generates multi-file hierarchical context system.
**All Agents** contribute their specialized knowledge to final context.

**Generated Artifacts:**
- Enhanced CLAUDE.md with project-specific context
- Context files in `.claude/context/` directory  
- Navigation patterns and cross-references
- Session state for future consultation updates

## ⚡ Agent Integration System

### Automated Agent Execution
The coordination system integrates with `/integrate-agents` for automated agent execution:
```bash
# Execute agents by phase
/integrate-agents phase-1 /path/to/project
/integrate-agents phase-2 /path/to/project  
/integrate-agents phase-3 /path/to/project

# Execute individual agents
/integrate-agents context-engineer /path/to/project
```

### Integration Architecture
- **Agent Definitions**: Specialized agents defined in `.claude/agents/`
- **Execution Scripts**: `scripts/integrate-agents.sh` and `scripts/invoke-agent.sh`
- **Session Integration**: All agent executions tracked in consultation state
- **Quality Assurance**: Agent boundaries enforced through integration system

## 🔄 Agent Handoff Protocols & Quality Assurance

### Strict Agent Specialization Boundaries
Each agent operates within clearly defined boundaries to ensure expert-level performance:

**🏗️ Context Engineer** - *Architecture & Navigation Specialist*
- ✅ **ONLY Handles**: Hierarchical context structures, navigation patterns, CLAUDE.md hub management
- ✅ **Core Expertise**: 11-layer Context Window Architecture, file hop patterns, token optimization
- ❌ **Never Handles**: Research validation, command creation, quality assurance
- 🎯 **Output**: Structured context files, navigation systems, memory architectures

**⚙️ Command Builder** - *Claude Code Command Specialist*  
- ✅ **ONLY Handles**: Claude Code slash command creation, YAML optimization, scaffolding patterns
- ✅ **Core Expertise**: Evidence-based command patterns, framework integration, anti-pattern prevention
- ❌ **Never Handles**: Web research, context structure design, general framework architecture
- 🎯 **Output**: Project-specific commands, YAML frontmatter, validation workflows

**🔍 Research Validator** - *Evidence & Source Specialist*
- ✅ **ONLY Handles**: Web research, evidence validation, source credibility assessment (3+ sources)
- ✅ **Core Expertise**: CRAAP test methodology, zero-hallucination enforcement, systematic research
- ❌ **Never Handles**: Pattern implementation, command creation, context structure design
- 🎯 **Output**: Validated evidence, credible sources, research documentation

### Advanced Coordination Workflow
1. **🚀 Phase Initialization**: Activate specialized agents with clear success criteria
2. **🤖 Agent Analysis**: Each agent performs deep analysis within their expertise domain
3. **💬 Question Synthesis**: Agents collaborate to generate comprehensive user prompts
4. **👤 User Interaction**: Collect detailed project information with follow-up clarifications
5. **⚡ Parallel Processing**: Agents process responses simultaneously within specialization boundaries
6. **🔗 Intelligent Handoff**: Validated information transferred with quality checks
7. **💾 Session Persistence**: State saved with agent contribution tracking
8. **✅ Quality Validation**: Multi-agent review before proceeding to next phase

## 📊 Session State Management & Progress Tracking

### Robust Consultation State Architecture
Session state maintained in `.claude/consultation-state.json` with comprehensive tracking:

**📍 Phase Management**
- **current_phase**: Active consultation phase (technical-analysis|domain-intelligence|context-generation)
- **completed_phases**: Array of successfully completed phases with timestamps
- **phase_progress**: Detailed completion percentage for current phase activities
- **phase_quality_score**: Agent-validated quality assessment for each completed phase

**👤 User Interaction State**
- **user_responses**: Structured responses from each phase with validation status
- **pending_approvals**: Content awaiting user review and approval
- **modification_requests**: User-requested changes to agent-generated content
- **session_preferences**: User settings for consultation style and depth

**🤖 Agent Coordination State**
- **active_agents**: Currently engaged agents with their specialization status
- **agent_outputs**: Generated content from each specialized agent with quality metrics
- **agent_handoffs**: Completed inter-agent information transfers with validation
- **agent_conflicts**: Any conflicts detected between agent recommendations

**🎯 Execution Control**
- **next_actions**: Prioritized list of remaining tasks for current phase
- **session_duration**: Total time spent in consultation with phase breakdowns
- **pause_points**: Available stopping points for session resume capability
- **rollback_checkpoints**: Saved states for recovery from errors or user changes

### Advanced Progress Tracking
- **📊 Phase Progress**: Real-time completion within current phase (0-100%)
- **🎯 Overall Progress**: Total consultation completion across all phases
- **⚡ Agent Efficiency**: Performance metrics for each specialized agent
- **✅ Quality Gates**: Validation checkpoints passed before phase transitions
- **👥 User Satisfaction**: Approval ratings for agent-generated content

## 💬 Interactive User Prompts System & User Experience

### Intelligent Question Generation Process
1. **🔍 Agent Analysis**: Specialized agents analyze current project state within their expertise
2. **🧠 Question Synthesis**: Generate phase-appropriate questions using agent specialization knowledge
3. **💬 Adaptive Interaction**: Present questions with contextual multiple choice and guided free-form options  
4. **✅ Response Validation**: Multi-agent validation of user responses for completeness and technical accuracy
5. **🔄 Dynamic Follow-up**: Generate intelligent follow-up questions based on user responses and agent insights
6. **📊 Progress Feedback**: Real-time feedback on consultation progress and next steps

### Enhanced User Approval Workflow
**📋 Content Review Process**
- **Preview Generation**: Show comprehensive preview of all agent-generated content
- **Side-by-Side Comparison**: Display before/after context improvements with clear benefits
- **Interactive Modification**: Allow in-place editing of generated content with agent validation
- **Change Impact Analysis**: Show how modifications affect other parts of the consultation

**🎛️ User Control Features**
- **Granular Approval**: Approve individual sections rather than all-or-nothing approach
- **Confidence Scoring**: Rate confidence in generated content to guide future improvements
- **Alternative Options**: View multiple approaches when agents generate different recommendations
- **Rollback Safety**: Multiple checkpoint levels for safe rollback to previous states

**⚡ Advanced Session Management**
- **Smart Pause Points**: Identify optimal stopping points based on consultation progress
- **Resume Intelligence**: Context-aware resume that recalls where user left off
- **Session Scheduling**: Plan multi-session consultations with progress persistence
- **Collaboration Features**: Share consultation state with team members

## 🔗 Integration Points & System Architecture

### Begin Consultation Integration
This coordination system is the **orchestration engine** invoked by `/begin-consultation` to:
- **🚀 Initialize Workflow**: Activate the 3-phase consultation with agent coordination
- **🔄 Manage Transitions**: Seamlessly transition between phases with state preservation
- **🤖 Agent Activation**: Coordinate specialized agent activities within appropriate phases
- **💾 Session Continuity**: Maintain comprehensive session state across consultation sessions
- **📊 Progress Monitoring**: Track and report consultation progress to user in real-time

### Advanced Agent Communication Protocols
**🎯 Intelligent Delegation System**
- **Task Routing**: Coordinator analyzes tasks and routes to appropriate specialized agents
- **Conflict Resolution**: Detect and resolve conflicts between agent recommendations
- **Load Balancing**: Distribute work optimally across available agents based on specialization

**📡 Secure Information Flow**
- **Boundary Enforcement**: Agents receive only information within their specialization scope
- **Data Validation**: All inter-agent communication validated for accuracy and completeness
- **Privacy Protection**: Sensitive project information handled according to agent clearance levels

**⚡ Real-Time Coordination**
- **Output Synthesis**: Coordinator intelligently combines agent outputs into coherent recommendations
- **Quality Assurance**: Multi-layer validation ensures agents maintain specialization boundaries
- **Performance Monitoring**: Track and optimize agent coordination efficiency

### System Integration Points
**🔌 Claude Code Native Integration**
- **Command Compatibility**: Full integration with Claude Code slash command system
- **Tool Permissions**: Proper allowed-tools declarations for each agent specialization
- **Session Management**: Native integration with Claude Code conversation state

**🌐 Extensibility Architecture**  
- **Plugin System**: Support for additional specialized agents as needed
- **API Integration**: Ready for integration with external project analysis tools
- **Custom Workflows**: Configurable consultation flows for different project types

## 🎯 Coordination Outcomes & Success Metrics

### Phase Completion Criteria
**📊 Phase 1 Completion**: Technical architecture context and framework-specific patterns documented with evidence validation
**🏢 Phase 2 Completion**: Domain knowledge and business logic context established with industry standard terminology  
**🎯 Phase 3 Completion**: Complete multi-file context system generated with user approval and quality validation

### Measurable Success Indicators
- **Context Quality Score**: Multi-agent validated quality assessment (target: >90%)
- **User Satisfaction Rating**: Approval rating for generated content (target: >4.5/5)
- **Agent Specialization Compliance**: Percentage of tasks handled within proper boundaries (target: 100%)
- **Session Efficiency**: Time to complete consultation compared to baseline (target: <35 minutes)
- **Context Effectiveness**: Measured improvement in Claude's project-specific responses

**🚀 Final Result**: Claude becomes a specialized expert for YOUR specific project through coordinated multi-agent intelligence, with measurable quality improvements and user satisfaction guarantees.