---
name: welcome-simple
description: Simple, elegant welcome and quick start guide
usage: "welcome-simple"
allowed-tools: [Read]
category: core
---

# Welcome to Claude Context Architect (Elegant Edition)

## 🎯 What This Does

In **10-15 minutes**, Claude Context Architect will:
1. Analyze your project
2. Understand your patterns
3. Generate custom commands
4. Make Claude understand YOUR codebase

## 🚀 Quick Start (3 Commands)

```bash
# Step 1: Analyze your project (3-5 min)
/discover-project-simple

# Step 2: Generate custom commands (2-3 min)
/generate-commands-simple

# Step 3: Try your new commands!
/create-component MyComponent  # or whatever was generated
```

That's it. Really.

## 📊 What Happens

### When you run `/discover-project-simple`:
- Claude reads your package.json/requirements.txt
- Scans your file structure
- Identifies your patterns
- Creates PROJECT-DNA.md

### When you run `/generate-commands-simple`:
- Claude reads PROJECT-DNA.md
- Generates 5-10 commands specific to YOUR project
- Saves them to `.claude/commands/generated/`
- Ready to use immediately

### When you use generated commands:
- They create files matching YOUR patterns
- Use YOUR test framework
- Follow YOUR conventions
- Just work

## 🎨 Example Results

### For a React + TypeScript + Jest project:
```
Generated commands:
✅ /create-component - Creates components your way
✅ /add-test - Adds tests with your framework
✅ /create-hook - Creates React hooks
✅ /add-route - Adds routes to your router
✅ /create-context - Creates React contexts
```

### For a Python + Django project:
```
Generated commands:
✅ /create-model - Creates Django models
✅ /add-view - Creates views
✅ /create-api-endpoint - Creates API endpoints
✅ /add-test - Creates Python tests
✅ /create-migration - Creates migrations
```

## 💡 Philosophy

**Simple but Elegant**
- No complex backends
- No 40+ Python scripts
- No theoretical abstractions
- Just prompts that work

**Claude Native**
- Uses Claude's built-in tools
- Everything is readable markdown
- No black boxes
- You can see and modify everything

## 🛠️ Only 5 Scripts

Instead of 43 Python scripts, we have just 5 shell scripts:
1. `setup.sh` - Installation
2. `validate.sh` - Health check
3. `cleanup.sh` - Maintenance
4. `test-harness.sh` - Basic tests
5. `emergency-reset.sh` - Recovery

Everything else is done through Claude prompts.

## 📝 Session State (Optional)

If you want to pause and resume:
```json
{
  "session": "2025-01-09-001",
  "completed": ["discovery", "generation"],
  "next": "testing"
}
```

Simple JSON file. No complex orchestration.

## 🎯 Success Metrics

You'll know it worked when:
- PROJECT-DNA.md exists with your patterns
- Generated commands appear in `.claude/commands/generated/`
- Commands create files that match your style
- Everything takes less than 15 minutes

## 🚨 If Something Goes Wrong

```bash
# Check what exists
ls -la PROJECT-DNA.md
ls -la .claude/commands/generated/

# Run validation
./scripts/validate.sh

# Reset if needed
./scripts/emergency-reset.sh
```

## 🎉 Ready to Start?

Run these three commands:
```
/discover-project-simple
/generate-commands-simple
/[your-generated-command]
```

Welcome to elegant simplicity.

---
*Claude Context Architect - Elegant Edition*
*Simple. Functional. Claude Native.*