# Consultation Directory - Interactive Consultation Flow

## Purpose: 20-30 Minute Intelligent Project Discovery

This directory houses the interactive consultation framework that conducts smart, valuable questioning sessions to extract deep project understanding, replacing zero-question assumptions with guided discovery.

## How This Differs from Speed-Focused Approach

**❌ Speed Approach**: Made assumptions about project needs without asking questions
**✅ Depth Approach**: Interactive discovery through intelligent, context-aware questioning

### Speed vs Depth Philosophy
- **Speed**: "We'll guess what you need" → Often completely wrong
- **Depth**: "Let's discover what you actually need" → Provides tailored solutions

## Phase 3 Integration: Interactive Consultation Framework

This directory implements **Phase 3** of the 8-phase deep discovery consultation:

### Duration: 5 days
### Objectives:
- Build 20-30 minute guided consultation experience
- Create intelligent questioning system
- Implement session management

## Key Components to be Developed

### 1. Multi-Stage Consultation Flow
**Files to be created:**
- `consultation-stages.yaml` - 4-stage consultation structure
- `flow-architecture.md` - Stage transition logic and timing
- `stage-templates/` - Individual stage implementations
- `time-management.yaml` - Time allocation and tracking system

**Stage Structure:**
- **Stage 1: Project Discovery** (5-7 minutes) - Understanding project type, scale, domain
- **Stage 2: Technical Deep Dive** (7-10 minutes) - Architecture, frameworks, patterns
- **Stage 3: Domain Extraction** (7-10 minutes) - Business rules, terminology, workflows  
- **Stage 4: Preference Learning** (3-5 minutes) - Team conventions, style preferences

### 2. Intelligent Questioning System
**Files to be created:**
- `question-generation-engine.md` - Dynamic question creation methodology
- `smart-defaults.yaml` - Detected information and default assumptions
- `skip-logic.yaml` - Question skip rules based on detected patterns
- `depth-adjustment.md` - Confidence-based question depth calibration

**Capabilities:**
- **Dynamic Questions**: Generated based on detected project characteristics
- **Smart Defaults**: Pre-populate answers from analysis where possible
- **Skip Logic**: Avoid asking about information already detected
- **Depth Calibration**: Adjust question complexity based on user expertise

### 3. Session Management System
**Files to be created:**
- `session-state.yaml` - State persistence schema
- `pause-resume.md` - Session interruption and continuation logic
- `progress-tracking.yaml` - Progress measurement and estimation
- `checkpoint-system.md` - Save points and rollback capability

**Capabilities:**
- **Pause/Resume**: Handle consultation interruptions gracefully
- **Progress Tracking**: Real-time progress with time estimates
- **State Persistence**: Maintain state across session boundaries
- **Rollback Support**: Allow revision of previous answers

### 4. Consultation Commands
**Commands to be developed:**
- `/consult-technical` - Technical architecture consultation stage
- `/consult-domain` - Domain knowledge extraction stage
- `/consult-workflow` - Workflow and preference discovery stage
- `/session-manage` - Session state management and control

## Integration Points with Other Directories

### ← research/
Research findings inform question generation:
- Patterns discovered suggest relevant questions
- Evidence confidence affects question importance
- Common pitfalls guide critical question areas

### → context-engine/
Consultation answers inform context generation:
- Technical answers guide architecture context
- Domain answers inform business context
- Preference answers shape generation style

### → agent-factory/
Consultation results inform agent specialization:
- Domain expertise suggests agent types needed
- Complexity level affects agent sophistication
- Team size influences coordination requirements

### → orchestration/
Consultation integrates with overall flow:
- Session state management coordinates with main flow
- Progress tracking feeds into overall progress
- Time management integrates with total consultation time

## Consultation Methodology: Interactive Discovery vs Assumptions

### Traditional Approach (Assumption-Based):
1. Assume project is like others
2. Apply generic templates
3. Hope they fit

### Deep Discovery Approach (Interactive):
1. **Guided Discovery**: Systematic exploration of project characteristics
2. **Context-Aware Questions**: Questions adapt based on previous answers
3. **Smart Defaults**: Leverage detected information to reduce user burden
4. **Depth Calibration**: Match question complexity to user expertise
5. **Validation Loops**: Confirm understanding before proceeding

## Question Generation Strategy

### 1. **Project Discovery Stage** (5-7 minutes)
**Sample Question Categories:**
- Project type and scale detection
- Primary domain and industry
- Team size and structure
- Current pain points and goals
- Timeline and constraint identification

### 2. **Technical Deep Dive** (7-10 minutes)
**Sample Question Categories:**
- Framework and technology stack
- Architecture patterns and preferences
- Testing strategies and coverage
- Deployment and CI/CD approaches
- Performance and scalability requirements

### 3. **Domain Extraction** (7-10 minutes)
**Sample Question Categories:**
- Business rules and logic patterns
- Domain terminology and concepts
- User journey and workflow mapping
- Data models and relationships
- Integration and API patterns

### 4. **Preference Learning** (3-5 minutes)
**Sample Question Categories:**
- Code style and convention preferences
- Documentation style and depth
- Error handling and logging approaches
- Team collaboration patterns
- Tool and IDE preferences

## Smart Question Features

### 1. **Context Awareness**
Questions adapt based on:
- Detected project characteristics from analysis
- Previous answers in current consultation
- Patterns identified in research phase
- User expertise level indicators

### 2. **Skip Logic Intelligence**
Automatically skip questions when:
- Information already detected through analysis
- Previous answers make questions irrelevant
- High confidence defaults can be assumed
- Time constraints require prioritization

### 3. **Depth Calibration**
Question complexity adjusts based on:
- User experience level indicators
- Project complexity assessment
- Time availability and constraints
- Confidence in current understanding

### 4. **Validation and Confirmation**
Built-in validation through:
- Answer consistency checking
- Critical assumption confirmation
- Understanding verification questions
- Confidence level tracking

## Session Management Features

### 1. **Pause/Resume Capability**
- **Flexible Timing**: Users can pause at any stage
- **State Preservation**: Complete session state maintained
- **Smart Resumption**: Resume with context recap
- **Progress Protection**: No loss of consultation progress

### 2. **Progress Tracking**
- **Real-Time Progress**: Visual progress indicators
- **Time Estimation**: Remaining time estimation
- **Stage Completion**: Clear stage completion feedback
- **Overall Progress**: Position in complete consultation

### 3. **Checkpoint System**
- **Save Points**: Automatic checkpoints at stage boundaries
- **Manual Saves**: User-initiated save points
- **Rollback Capability**: Return to previous checkpoints
- **Revision Support**: Modify previous answers

## Success Criteria for Consultation Phase

### User Experience Metrics:
- **20-30 minute completion time** for full consultation
- **< 5 questions per stage** for focused efficiency
- **90%+ relevance rating** for generated questions
- **Smooth session management** with pause/resume capability

### Quality Outcomes:
- Deep understanding of project technical architecture
- Clear domain knowledge extraction and terminology
- Comprehensive preference and convention discovery
- High-confidence foundation for subsequent phases

### Integration Success:
- Seamless flow from research-informed questions
- Clear handoff to context generation with complete information
- Session state integration with overall orchestration
- Progress tracking alignment with main consultation flow

---

**This consultation directory transforms Claude Context Architect from assumption-based configuration to interactive discovery, ensuring every generated solution is tailored to your actual project needs and preferences.**