# 🎨 The Elegant Architecture
*Simple but Sophisticated - Claude Code Native*

## Core Philosophy
**Prompts over Scripts** - Claude interprets markdown, we don't need execution layers

## The Only 5 Scripts We Need

### 1. `setup.sh` - Installation
```bash
#!/bin/bash
# Copies .claude/ to user's project
# Creates initial CLAUDE.md
# That's it - simple
```

### 2. `validate.sh` - Health Check  
```bash
#!/bin/bash
# Checks .claude/ exists
# Verifies commands have proper YAML
# Reports status
```

### 3. `cleanup.sh` - Maintenance
```bash
#!/bin/bash  
# Archives old logs
# Removes temp files
# Keeps project clean
```

### 4. `test-harness.sh` - Quality Assurance
```bash
#!/bin/bash
# Runs basic smoke tests
# Validates command structure
# Checks for common issues
```

### 5. `emergency-reset.sh` - Recovery
```bash
#!/bin/bash
# Backs up current state
# Resets to clean install
# Recovers from errors
```

**That's it. No more scripts needed.**

## Everything Else is Prompts

### Discovery Through Prompts
Instead of Python scripts analyzing code, Claude does it:

```markdown
# /discover-project
Claude uses Read, Glob, Grep to:
- Read package.json/requirements.txt
- Identify framework (React, Django, etc.)
- Find test patterns
- Detect conventions
- Create PROJECT-DNA.md
```

### Generation Through Prompts
Instead of Python generators, Claude creates:

```markdown
# /generate-commands
Claude uses Write, Edit to:
- Read PROJECT-DNA.md
- Select appropriate templates
- Customize based on patterns
- Write new commands to .claude/commands/generated/
```

### Validation Through Prompts
Instead of Python validators, Claude checks:

```markdown
# /validate-setup
Claude uses Read, Grep to:
- Verify generated commands exist
- Check YAML frontmatter is valid
- Test basic command execution
- Report any issues
```

## The Elegant Flow

### 1. Knowledge Access (Prompts)
```
/patterns react       → Claude reads patterns for React
/patterns testing     → Claude reads testing patterns
/antipatterns common  → Claude reads what to avoid
```

### 2. Project Analysis (Prompts)
```
/discover-project     → Claude analyzes user's code
/identify-stack      → Claude detects tech stack
/extract-conventions → Claude finds team patterns
```

### 3. Intelligent Generation (Prompts)
```
/generate-commands   → Claude creates custom commands
/generate-context    → Claude creates CLAUDE.md
/generate-agents     → Claude creates specialized agents
```

### 4. Interactive Consultation (Prompts)
```
/consult-interactive → Claude asks clarifying questions
/consult-technical   → Claude dives deep on architecture
/consult-workflow    → Claude understands team process
```

## Simple State Management

### Session State (Not Scripts!)
```json
{
  "session_id": "2025-01-09-001",
  "phase": "discovery",
  "completed": ["welcome", "project-analysis"],
  "next": "consultation",
  "checkpoint": "after-analysis"
}
```

Claude reads/writes this simple JSON. No orchestration scripts needed.

## Pattern Templates (Prompt-Accessible)

### Instead of Complex YAML
```yaml
# OLD: Complex, script-processed
generation_engine:
  pipeline:
    stages:
      - discovery_analysis:
          steps: [...]
```

### Simple Template Prompts
```markdown
# Pattern: React Component Generator
When user has React:
1. Check their component style (class/functional)
2. Check their file structure (separate/colocated)
3. Generate component command matching their style
```

## The User Journey (10-15 Minutes)

### Streamlined Experience
```
1. /welcome (1 min)
   → Orient user
   → Explain process
   
2. /discover-project (3-5 min)
   → Analyze codebase
   → Extract patterns
   → Create PROJECT-DNA.md
   
3. /consult-brief (3-5 min)
   → Ask 5-7 key questions
   → Clarify ambiguities
   → Confirm understanding
   
4. /generate-all (2-3 min)
   → Generate commands
   → Create context
   → Set up agents
   
5. /validate (1 min)
   → Check everything works
   → Show what was created
   → Ready to use!
```

## Why This Works

### Advantages
1. **Claude Native** - Uses Claude's strengths
2. **No Black Boxes** - Everything is readable markdown
3. **Debuggable** - Can see exactly what Claude does
4. **Maintainable** - No complex script dependencies
5. **Portable** - Works anywhere Claude Code works

### What We Avoid
- ❌ Script orchestration complexity
- ❌ Python dependency management
- ❌ Execution environment issues
- ❌ Black box processing
- ❌ Debugging script failures

## Implementation Priority

### Phase 1: Core Flow (Day 1)
1. Make `/discover-project` actually analyze projects
2. Make `/generate-commands` actually create commands
3. Connect them with PROJECT-DNA.md

### Phase 2: Intelligence (Day 2)
1. Add pattern recognition to discovery
2. Add template customization to generation
3. Add basic consultation questions

### Phase 3: Polish (Day 3)
1. Add session management (simple JSON)
2. Add progress indicators
3. Add validation and error handling

## The Key Insight

**We don't need scripts to orchestrate Claude. Claude IS the orchestrator.**

Every "backend process" can be a prompt that Claude executes:
- Pattern matching? Claude can do it
- Template processing? Claude can do it
- File generation? Claude can do it
- Validation? Claude can do it

## Success Metrics

### Simple Success
User runs three commands:
```
/welcome
/discover-project
/generate-commands
```

And gets:
- ✅ PROJECT-DNA.md with their patterns
- ✅ 5-10 custom commands that match their style
- ✅ Commands that actually work

### Elegant Success
The same three commands also:
- Remember session state
- Ask clarifying questions
- Provide progress updates
- Validate output
- Handle errors gracefully

## The Bottom Line

**43 scripts → 5 scripts**
**Complex backends → Simple prompts**
**Theoretical integration → Actual functionality**
**30-60 minutes → 10-15 minutes**

This is Claude Code Native: **Prompts all the way down.**