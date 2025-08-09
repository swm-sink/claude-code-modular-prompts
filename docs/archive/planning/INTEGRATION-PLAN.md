# Integration Plan: Wiring Frontend to Backend

## 🎯 Goal: Make Commands Actually Use Backend Architecture

### Priority 1: Wire `/discover-project` to Backend

**Current State**: Standalone implementation
**Target State**: Uses `.claude-architect/research/` for analysis

#### Integration Steps:

```yaml
1. Make command read backend configs:
   - Read: .claude-architect/research/analysis-framework.md
   - Read: .claude-architect/research/pattern-extraction-engine.md
   - Use: Templates from .claude-architect/research/templates/

2. Execute pattern extraction:
   - Use: pattern-extraction-engine.md logic
   - Apply: CRAAP test from validation/
   - Output: To .claude-architect/project-dna.md

3. Store discoveries properly:
   - Write: .claude-architect/discoveries/project-dna.md
   - Update: .claude-architect/session-state.json
```

### Priority 2: Wire `/generate-commands` to Backend

**Current State**: Reads PROJECT-DNA.md, generates from scratch
**Target State**: Uses `.claude-architect/command-forge/` templates

#### Integration Steps:

```yaml
1. Read command-forge configs:
   - Load: command-categories.yaml
   - Load: pattern-library.yaml
   - Load: generation-engine.yaml

2. Use actual templates:
   - Read: templates/component-generator-template.md
   - Apply: Variable substitution from discoveries
   - Use: Pattern matching from pattern-library.yaml

3. Generate properly:
   - Output to: .claude/commands/generated/
   - Track in: .claude-architect/session-state.json
```

### Priority 3: Make `/deep-discovery` Orchestrate Everything

**Current State**: Describes the process
**Target State**: Actually orchestrates the consultation

#### Integration Steps:

```yaml
1. Read consultation flow:
   - Load: .claude-architect/consultation/consultation-flow.yaml
   - Execute: Stage progression
   - Track: Progress in session-state.json

2. Execute each phase:
   - Phase 1: Call integrated /discover-project
   - Phase 2: Use consultation/questions/
   - Phase 3: Call integrated /generate-commands

3. Manage session:
   - Save: .claude-architect/session-state.json
   - Allow: Pause/resume functionality
   - Track: Time and progress
```

## 🔧 Specific Code Changes Needed

### Example 1: Update `/discover-project`

```markdown
# Current (Standalone)
The command analyzes files independently

# Target (Integrated)
## Implementation
1. Load analysis framework:
   framework = Read('.claude-architect/research/analysis-framework.md')
   
2. Execute pattern extraction:
   patterns = Read('.claude-architect/research/pattern-extraction-engine.md')
   Apply patterns to discovered files
   
3. Save to backend:
   Write('.claude-architect/discoveries/project-dna.md', discoveries)
```

### Example 2: Update `/generate-commands`

```markdown
# Current (Standalone)
Reads PROJECT-DNA.md and creates commands from scratch

# Target (Integrated)
## Implementation
1. Load generation engine:
   engine = Read('.claude-architect/command-forge/generation-engine.yaml')
   categories = Read('.claude-architect/command-forge/command-categories.yaml')
   
2. Use templates:
   For each category in categories:
     template = Read('.claude-architect/command-forge/templates/{category}-template.md')
     Apply discoveries to template
     Generate command
```

## 📊 Success Metrics

### Metric 1: Integration Evidence
```bash
# Commands should reference backend
grep -r "\.claude-architect" .claude/commands/
# Should show multiple references
```

### Metric 2: Functional Test
```bash
# Run discovery
/discover-project
# Check: Creates .claude-architect/discoveries/project-dna.md

# Generate commands  
/generate-commands
# Check: Uses templates from command-forge/
# Check: Creates working commands in .claude/commands/generated/
```

### Metric 3: End-to-End Test
```bash
# Full consultation
/deep-discovery start
# Should: 
# - Start consultation
# - Ask questions
# - Analyze project
# - Generate commands
# - Take 30-60 minutes
# - Produce working output
```

## 🚨 Anti-Patterns to Avoid

### ❌ DON'T:
1. Create new standalone implementations
2. Duplicate logic that exists in backend
3. Build "simpler" versions that ignore backend
4. Add more YAML without wiring existing
5. Claim integration without testing

### ✅ DO:
1. Read backend configs in commands
2. Use existing templates and patterns
3. Save state to backend locations
4. Test integration actually works
5. Update only after functionality verified

## 📅 Integration Schedule

### Day 1: Wire `/discover-project`
- Morning: Add backend config reading
- Afternoon: Test pattern extraction works
- Evening: Verify PROJECT-DNA creation

### Day 2: Wire `/generate-commands`
- Morning: Add template loading
- Afternoon: Test command generation
- Evening: Verify generated commands work

### Day 3: Wire `/deep-discovery`
- Morning: Add orchestration logic
- Afternoon: Test full flow
- Evening: Verify 30-60 minute consultation works

### Day 4: Validation
- Test all integration points
- Fix any broken connections
- Update documentation
- Update claude.todos.yaml with ACTUAL status

## 🔄 Daily Integration Checklist

- [ ] Pick ONE command to integrate
- [ ] Find corresponding backend logic
- [ ] Update command to use backend
- [ ] Test integration works
- [ ] Commit with evidence of functionality
- [ ] Update PROJECT-STATE-VERIFICATION.md
- [ ] Only then move to next command

## 📝 Tracking Integration Progress

```yaml
integration_status:
  discover-project:
    reads_backend: false → true
    uses_templates: false → true
    saves_to_backend: false → true
    
  generate-commands:
    reads_backend: false → true
    uses_templates: false → true
    generates_working: false → true
    
  deep-discovery:
    orchestrates: false → true
    manages_session: false → true
    works_e2e: false → true
```

---

**Remember**: Integration means commands actually USE backend, not just reference it in documentation.