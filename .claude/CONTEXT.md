# Claude Context - Essential Information Only

## 🎯 Project: Deep Discovery Consultation System
**Vision**: 30-60 minute consultation → project-specific commands  
**Current Phase**: 6 of 8 (Command Generation)  
**Critical Gap**: Frontend commands exist, backend exists, but NOT connected

## 🏗️ Architecture (Remember This!)
```
.claude/commands/        = Frontend (what users run)
.claude-architect/       = Backend (processing logic)
                          ↓
            These must be CONNECTED for anything to work
```

## ⚠️ Five Critical Rules
1. **Hidden dirs need special handling**: `ls -la .claude*` (LS tool fails)
2. **Test before claiming complete**: Can user actually run it?
3. **Integrate, don't duplicate**: Backend exists - wire to it
4. **Structure ≠ Functionality**: YAML files don't execute
5. **Confused? STOP & ASK**: Don't assume when uncertain

## 📍 Right Now Priority
**Make ONE thing work end-to-end**:
```bash
/discover-project  →  Actually analyzes using backend  →  Creates PROJECT-DNA.md
                                    ↓
/generate-commands  →  Uses backend templates  →  Creates working commands
```

## 🔗 Need More Context?
- **🆕 New session?** → `.claude/context/00-quickstart.md`
- **🏗️ Architecture?** → `.claude/context/01-architecture.md`
- **🔧 How to work?** → `.claude/context/02-workflow.md`
- **🐛 Debugging?** → `.claude/context/04-troubleshooting.md`
- **📊 Session state?** → `.claude/session/state.json`

## 🚦 Quick Status Check
```bash
# Run these to know actual state:
ls -la .claude-architect/    # Backend exists? ✓
ls -la .claude/commands/      # Frontend exists? ✓
grep "claude-architect" .claude/commands/*.md  # Integration? ✗
```

---
*87 lines, ~400 tokens - Everything essential, nothing more*