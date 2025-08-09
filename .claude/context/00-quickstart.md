# Quickstart - First 5 Minutes

## 🎯 Understand in 30 Seconds
- **What**: Building deep discovery system for Claude Code
- **Problem**: Commands exist, backend exists, but disconnected
- **Solution**: Wire them together
- **Not**: Create more plans or YAML files

## ✅ Verify Your Environment (1 min)
```bash
# 1. Check directories (use Bash, not LS!)
ls -la /Users/smenssink/conductor/repo/claude-code-modular-prompts/lisbon/.claude*

# Should see:
# .claude/          ← Frontend commands
# .claude-architect/ ← Backend logic
# .claude-minimal/   ← Ignore this
```

## 📊 Check Actual Status (1 min)
```bash
# What works?
/deep-discovery status     # Probably describes process
/discover-project          # Might analyze files
/generate-commands         # Might create something

# Key question: Do they use backend?
grep -l "claude-architect" .claude/commands/*.md | wc -l
# If 0 or low number = problem!
```

## 🎬 Your First Action (2 min)

### If starting fresh today:
1. Read `PROJECT-STATE-VERIFICATION.md` for reality check
2. Read `INTEGRATION-PLAN.md` for what needs doing
3. Pick ONE command to integrate (suggest: `/discover-project`)

### If continuing work:
1. Check `.claude/session/state.json` for last action
2. Verify claimed vs actual state
3. Continue integration, don't create new

## 🚫 Automatic Stop Triggers
**STOP if you**:
- Can't find .claude-architect/ (it exists, you're using wrong command)
- Think you need new architecture (backend already exists)
- Want to create a plan (implement instead)
- Are confused (ask for clarification)

## 🔗 Next Steps
- **Ready to work?** → Read `context/02-workflow.md`
- **Hit a problem?** → Read `context/04-troubleshooting.md`
- **Confused about design?** → Read `context/01-architecture.md`

---
*Quick, actionable, no fluff*