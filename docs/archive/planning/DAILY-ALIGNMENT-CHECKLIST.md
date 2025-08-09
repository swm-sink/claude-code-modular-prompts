# Daily Alignment Checklist

## 🌅 Start of Session Checklist

### Step 1: Verify You Can Find Directories (1 min)
```bash
# CORRECT way to check directories exist
ls -la /Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/ | grep "\.claude"

# Should show:
# .claude
# .claude-architect
# .claude-minimal
```
✅ Verified: _________ (date/time)

### Step 2: Understand the Architecture (2 min)
```
Remember:
- .claude/commands/ = Frontend (user interface)
- .claude-architect/ = Backend (processing logic)
- They work TOGETHER, not separately
- Integration is incomplete but improving
```
✅ Understood: _________ (date/time)

### Step 3: Check Current Phase Status (1 min)
```bash
# Check what claude.todos.yaml claims
grep "current_phase" claude.todos.yaml

# Check what PROJECT-STATE-VERIFICATION.md says
head -20 PROJECT-STATE-VERIFICATION.md
```
- YAML claims Phase: _____
- Actual functionality: _____%
✅ Discrepancy noted: _________ (date/time)

### Step 4: Test Actual Functionality (5 min)
```bash
# Test what actually works
/discover-project --dry-run
# Works? Y/N: _____

/generate-commands --dry-run  
# Works? Y/N: _____

/deep-discovery status
# Works? Y/N: _____
```
✅ Functionality tested: _________ (date/time)

### Step 5: Identify Today's Focus (2 min)
Based on INTEGRATION-PLAN.md, today's priority:
- [ ] Wire `/discover-project` to backend
- [ ] Wire `/generate-commands` to backend
- [ ] Wire `/deep-discovery` orchestration
- [ ] Test end-to-end functionality
- [ ] Other: _________________

✅ Focus identified: _________ (date/time)

## 🚨 Before Making ANY Changes

### Pre-Change Checklist:
1. **Does backend logic exist for this?**
   - Check `.claude-architect/` first
   - Don't create new if it exists
   
2. **Am I integrating or duplicating?**
   - Use existing patterns
   - Wire to backend, don't reimplement
   
3. **Will this actually work for users?**
   - Not just create files
   - Actually function when run

## 📊 Before Updating Status

### Pre-Status-Update Checklist:
1. **Test the functionality**
   ```bash
   # Actually run the command
   /[command-name]
   # Does it work? Really?
   ```

2. **Verify three levels:**
   - Structure exists? ✓
   - Integration done? ✓  
   - Functionality works? ✓
   
3. **Document evidence:**
   - What command was run: _______
   - What output produced: _______
   - Does it match intent: Y/N

## 🔄 Every 2 Hours

### Alignment Check:
1. **Re-read the vision:**
   "30-60 minute deep discovery consultation that generates project-specific commands"
   
2. **Check current work:**
   - Is this moving toward the vision? Y/N
   - Am I building integration? Y/N
   - Will users be able to use this? Y/N
   
3. **Course correct if needed:**
   - Identified drift? _______
   - Correction needed? _______

## 🏁 End of Session

### Wrap-up Checklist:
1. **Update PROJECT-STATE-VERIFICATION.md**
   - What actually works now: _______
   - What's still broken: _______
   
2. **Update integration status**
   - What got integrated today: _______
   - What's next priority: _______
   
3. **Honest assessment:**
   - Real progress today: _____%
   - Blocked on anything? _______
   - Need clarification on? _______

## 🚫 Red Flags - STOP if you see these:

1. Creating new architecture when backend exists
2. Building standalone when should integrate
3. Updating status without testing
4. Adding YAMLs instead of wiring existing
5. Can't find directories (use correct method!)
6. Confused about architecture (re-read CLAUDE.md)
7. Multiple approaches for same thing
8. Integration path unclear

**If any red flag appears → STOP and ask for clarification**

## 📝 Session Log

### Session: _________ (date/time)
- Started with phase: _____
- Ended with phase: _____  
- Integrated: _______
- Actually works now: _______
- Next session priority: _______

---

**Remember**: 
- Structure ≠ Functionality
- YAML configs ≠ Working features
- Integration > New implementation
- Test everything before claiming complete