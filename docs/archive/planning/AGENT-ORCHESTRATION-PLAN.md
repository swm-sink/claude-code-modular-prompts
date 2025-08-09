# Sequential Agent Orchestration Plan for Phase 2

## Orchestration Architecture

### Core Design Principles
1. **Stateless Execution**: Each agent reads full context from files, never assumes memory
2. **Adaptive Feedback**: Agents can be respawned with corrections based on validation
3. **Context Packages**: Each agent receives specific, focused context
4. **Quality Gates**: Validation agents check work before progression
5. **Atomic Operations**: Each agent completes one specific task atomically

## Agent Types & Specializations

### 1. Analysis Agent
**Purpose**: Analyze current state and identify all occurrences needing change
**Input Context**:
- Target file path
- Search patterns to identify
- Risk assessment criteria
**Output**: 
- List of all locations needing changes
- Risk analysis report
- Recommended change strategy

### 2. Transformation Agent  
**Purpose**: Execute specific transformations on identified locations
**Input Context**:
- Analysis report from Analysis Agent
- Specific transformation rules
- Validation criteria
**Output**:
- Completed transformations
- Change log
- Validation report

### 3. Validation Agent
**Purpose**: Verify changes meet requirements and maintain consistency
**Input Context**:
- Original requirements
- Changes made
- Success criteria
**Output**:
- Validation status (pass/fail)
- Issues identified
- Correction recommendations

### 4. Correction Agent
**Purpose**: Fix issues identified by Validation Agent
**Input Context**:
- Validation report
- Original requirements
- Correction strategies
**Output**:
- Applied corrections
- Updated validation status

## Execution Flow for Tasks 13-18

### Task 13: Replace 'template library' with 'deep discovery engine'

#### Stage 1: Analysis
```yaml
agent: Analysis_Agent_13
mission: Find all occurrences of 'template library' in CLAUDE.md
context:
  file: CLAUDE.md
  patterns: 
    - "template library"
    - "Template Library"
    - "TEMPLATE LIBRARY"
  exclude_sections:
    - "GENERATIVE VISION" # Already updated
validation:
  - Must find at least 5 occurrences
  - Must not include new GENERATIVE VISION section
```

#### Stage 2: Transformation
```yaml
agent: Transformation_Agent_13
mission: Replace identified occurrences with appropriate variations
context:
  replacements:
    "template library" -> "deep discovery engine"
    "Template Library" -> "Deep Discovery Engine"
    "TEMPLATE LIBRARY" -> "DEEP DISCOVERY ENGINE"
  preserve:
    - Original meaning/context
    - Sentence structure
validation:
  - All identified occurrences replaced
  - No unintended changes
```

#### Stage 3: Validation
```yaml
agent: Validation_Agent_13
mission: Verify all replacements are correct and complete
checks:
  - No remaining "template library" references (except in GENERATIVE VISION)
  - Replacements maintain grammatical correctness
  - Context still makes sense
```

### Inter-Agent Communication Protocol

#### Context Handoff Structure
```yaml
handoff:
  from_agent: Analysis_Agent_13
  to_agent: Transformation_Agent_13
  timestamp: ISO-8601
  data:
    locations: [line_numbers]
    patterns_found: [exact_matches]
    risk_assessment: low|medium|high
    recommendations: [specific_suggestions]
  validation:
    checksum: SHA256
    status: ready|blocked|failed
```

#### Feedback Loop Structure
```yaml
feedback:
  from_agent: Validation_Agent_13
  to_orchestrator: true
  issues_found:
    - description: "Missed occurrence at line X"
      severity: high
      action_required: respawn_transformation
  recommendations:
    respawn_with:
      agent: Transformation_Agent_13
      additional_context: [specific_corrections_needed]
```

## Orchestrator Responsibilities

### 1. Context Preparation
- Read current task from claude.todos.yaml
- Prepare agent-specific context packages
- Include relevant sections of CLAUDE.md
- Add validation criteria

### 2. Agent Spawning
- Create focused prompts for each agent
- Include only necessary context (avoid token waste)
- Set clear success criteria
- Define output format

### 3. Result Validation
- Check agent outputs against criteria
- Identify need for respawning
- Track progress in TodoWrite
- Update claude.todos.yaml

### 4. Adaptive Correction
- Analyze validation failures
- Prepare correction context
- Respawn agents with enhanced instructions
- Iterate until success

## Quality Gates

### Gate 1: Pre-Transformation
- Verify backup exists
- Confirm analysis completeness
- Check risk assessment

### Gate 2: Post-Transformation  
- Validate all changes applied
- Check for unintended modifications
- Ensure consistency maintained

### Gate 3: Final Validation
- End-to-end verification
- Cross-reference with requirements
- Confirm ready for commit

## Success Metrics

1. **Accuracy**: 100% of identified patterns transformed correctly
2. **Completeness**: No patterns missed (validated by grep)
3. **Consistency**: All changes maintain document coherence
4. **Atomicity**: Each task results in one clean commit
5. **Efficiency**: Minimal respawns needed (<2 per task)

## Execution Commands

### Start Orchestration
```bash
# Orchestrator initializes
./orchestrate.sh --phase 2 --tasks 13-18 --mode sequential

# For each task:
# 1. Spawn Analysis Agent
# 2. Validate analysis
# 3. Spawn Transformation Agent
# 4. Validate transformation
# 5. If issues, spawn Correction Agent
# 6. Final validation
# 7. Commit changes
```

## Agent Context Templates

### Analysis Agent Context
```
You are Analysis_Agent_[TASK_NUM]. Your ONLY job is to analyze CLAUDE.md and find all occurrences of [PATTERN].

REQUIREMENTS:
1. Use Grep to find all occurrences
2. Report line numbers and exact text
3. Assess risk level of each change
4. Output structured report

DO NOT:
- Make any changes
- Analyze other files
- Provide opinions

OUTPUT FORMAT:
```yaml
occurrences:
  - line: [number]
    text: "[exact text]"
    risk: [low|medium|high]
total_found: [number]
```
```

### Transformation Agent Context  
```
You are Transformation_Agent_[TASK_NUM]. Your ONLY job is to apply transformations based on the analysis report.

INPUT: [Analysis report]

REQUIREMENTS:
1. Apply ONLY the specified transformations
2. Preserve surrounding context
3. Maintain formatting
4. Log all changes

OUTPUT FORMAT:
```yaml
changes_made:
  - line: [number]
    before: "[text]"
    after: "[text]"
total_changed: [number]
```
```

This orchestration plan ensures autonomous execution with clear boundaries, validation checkpoints, and adaptive correction mechanisms.