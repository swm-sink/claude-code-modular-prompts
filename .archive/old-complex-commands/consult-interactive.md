---
name: consult-interactive
description: Begin interactive 20-30 minute consultation with 4-stage discovery flow
usage: "consult-interactive [mode] [stage]"
allowed-tools: [Read, Write, MultiEdit, Bash, Grep, LS, Glob]
category: consultation
version: "2.0"
---

# Interactive Consultation Command

## Purpose
Conduct a comprehensive 20-30 minute interactive consultation to extract deep project understanding, replacing generic assumptions with tailored discovery through intelligent conversation.

**Consultation Philosophy**: Conversation, not interrogation. Users WANT to spend time because they see immediate value in the understanding being built.

## Command Usage

### Start Complete Consultation
```bash
/consult-interactive
# Begins full 4-stage consultation process (20-30 minutes)
```

### Start in Specific Mode
```bash
/consult-interactive quick
# Essential questions only (12-15 minutes)

/consult-interactive deep  
# Comprehensive exploration (30-35 minutes)

/consult-interactive resume
# Continue from last checkpoint
```

### Start at Specific Stage
```bash
/consult-interactive --stage 2
# Start at Technical Deep Dive (if Stage 1 complete)

/consult-interactive --stage 3 --mode quick
# Start at Domain Extraction in quick mode
```

## Consultation Stages

### Stage 1: Project Discovery (5-7 minutes)
- Project type, domain, and team size
- Current challenges and goals  
- Claude integration motivation
- Foundation for technical discussion

### Stage 2: Technical Deep Dive (7-10 minutes)
- Architecture patterns and tech stack
- Development workflow and testing approach
- Performance requirements and constraints
- Technical foundation for context generation

### Stage 3: Domain Extraction (7-10 minutes)
- Business entities and terminology
- Key workflows and user journeys
- Data relationships and integrations
- Domain knowledge for specialized responses

### Stage 4: Preference Learning (3-5 minutes)
- Coding standards and style preferences
- Documentation and communication style
- Tool preferences and workflow habits
- Team conventions for response customization

## User Control Features

### Navigation Commands (Available Throughout)
- `skip` - Move to next question
- `skip stage` - Move to next stage
- `back` - Return to previous question
- `back stage` - Return to previous stage
- `review` - Review current understanding

### Pace Control Commands
- `quick mode` - Essential questions only
- `deep mode` - Comprehensive exploration
- `standard mode` - Balanced approach
- `pause` - Save progress and pause consultation
- `resume` - Continue from checkpoint

### Understanding Commands
- `clarify` - Ask for more detail on current topic
- `example` - Get concrete example of concept
- `summary` - Review current understanding
- `confident` - Confirm understanding and proceed

## Implementation

This command orchestrates the complete consultation flow by:

1. **Loading consultation architecture** from `.claude-architect/consultation/`
2. **Managing session state** and progress tracking
3. **Executing stage-specific question flows** with adaptive intelligence
4. **Providing user control** throughout the process
5. **Building comprehensive project understanding** for context generation

## Execution Flow

```bash
# The command follows this execution pattern:

1. Initialize consultation session
   - Load consultation architecture files
   - Check for existing session state
   - Set up progress tracking

2. Execute Stage 1: Project Discovery
   - Load stage-1-project-discovery.yaml
   - Apply adaptive questioning based on repository analysis
   - Validate understanding before proceeding

3. Execute Stage 2: Technical Deep Dive  
   - Load stage-2-technical-deep-dive.yaml
   - Adapt questions based on Stage 1 findings
   - Framework-specific deep dives based on detected stack

4. Execute Stage 3: Domain Extraction
   - Load stage-3-domain-extraction.yaml
   - Domain-specific questioning based on project type
   - Business terminology and workflow capture

5. Execute Stage 4: Preference Learning
   - Load stage-4-preference-learning.yaml
   - Team-size and project-stage adapted preferences
   - Final style and convention capture

6. Synthesize Complete Understanding
   - Comprehensive project profile summary
   - Validation of all captured information
   - Preparation for context generation phase
```

## Integration Points

### From Research Phase
- Uses repository analysis results to skip redundant questions
- Leverages detected patterns to customize question depth
- References validated evidence to inform adaptive questioning

### To Context Generation
- Provides complete project profile for context architecture
- Supplies technical requirements for context file structure  
- Delivers domain knowledge for specialized context content
- Defines preferences for context generation style

### Session Management
- Saves progress to `.claude-architect/consultation/sessions/`
- Enables pause/resume across multiple Claude conversations
- Maintains state for revision and backtracking
- Tracks time and completion metrics

## Quality Assurance

### Information Validation
- Understanding checks at each stage transition
- Confidence monitoring and clarification loops
- Comprehensive synthesis validation
- Gap identification and filling

### User Experience
- Progress indicators and time estimation
- Smooth stage transitions with context bridging
- Natural conversation flow, not interrogation
- Immediate value demonstration throughout

### Adaptive Intelligence
- Framework-specific question adaptation
- Team size and project stage customization
- Expertise level calibration
- Time-aware questioning prioritization

## Success Metrics

### Time Efficiency
- Target: 20-30 minutes total consultation time
- Stage balance: No stage exceeds 35% of total time  
- User control: >80% find flow control helpful

### Information Quality
- Completeness: >90% required information captured
- Accuracy: >95% information validated as correct
- Relevance: >85% information used in generation

### User Experience  
- Engagement: >4.0/5.0 conversation quality rating
- Value: >4.5/5.0 time investment rating
- Control: >4.0/5.0 user control satisfaction

## File Dependencies

```bash
# Core consultation architecture
.claude-architect/consultation/consultation-flow.yaml
.claude-architect/consultation/stage-1-project-discovery.yaml
.claude-architect/consultation/stage-2-technical-deep-dive.yaml
.claude-architect/consultation/stage-3-domain-extraction.yaml
.claude-architect/consultation/stage-4-preference-learning.yaml
.claude-architect/consultation/flow-control.md

# Templates and scripts
.claude-architect/consultation/templates/consultation-script.md

# Session management (created during execution)
.claude-architect/consultation/sessions/[session-id]/
```

## Example Usage

```bash
# Start comprehensive consultation
> /consult-interactive

🎯 Welcome to Claude Context Architect Deep Discovery!

I'm excited to help transform Claude into YOUR project expert through 
comprehensive understanding of your specific project. This 20-30 minute 
conversation will explore your project, technical architecture, business 
domain, and team preferences.

You're in complete control:
- Say "skip" to move past questions
- Say "pause" to save and resume later  
- Say "quick mode" for essentials only

Ready to discover your project together? 🚀

[Consultation proceeds through 4 stages with intelligent adaptation]
```

This command transforms the consultation architecture into an executable Claude Code command that provides comprehensive project discovery through intelligent, adaptive conversation.