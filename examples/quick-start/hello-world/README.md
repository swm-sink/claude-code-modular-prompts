# Hello World - 2-Minute Framework Success

> **Guarantee**: Framework working and responding to commands in exactly 2 minutes.

This is your first contact with the Claude Code framework. Follow these copy-paste steps and you'll have a working framework installation with successful command execution in under 2 minutes.

## 🚀 2-Minute Execution Plan

### Step 1: Copy Framework Files (30 seconds)

```bash
# Navigate to your project directory (replace 'your-project' with actual path)
cd /path/to/your-project

# Copy framework files (adjust source path as needed)
cp -r /path/to/claude-code-modular-prompts/.claude .
cp /path/to/claude-code-modular-prompts/CLAUDE.md .
cp /path/to/claude-code-modular-prompts/examples/quick-start/hello-world/PROJECT_CONFIG.xml .

# Verify files copied correctly
ls -la CLAUDE.md PROJECT_CONFIG.xml .claude/
```

**Expected output**: You should see `CLAUDE.md`, `PROJECT_CONFIG.xml`, and `.claude/` directory.

### Step 2: Test Framework Installation (30 seconds)

```bash
# Test framework responsiveness with simplest possible command
/query "what is the current directory structure?"
```

**Expected result**: Framework analyzes your project and provides a structured response about your directory layout.

### Step 3: Customize Project Settings (30 seconds)

Open `PROJECT_CONFIG.xml` and update these three lines:

```xml
<name>Your Actual Project Name</name>
<primary_language>your_main_language</primary_language>  <!-- javascript, python, go, etc. -->
<framework_stack>your_tech_stack</framework_stack>       <!-- react, django, express, etc. -->
```

**Quick customization**: Just change the name and language - everything else works with defaults.

### Step 4: Execute Your First Real Command (30 seconds)

```bash
# Let the framework intelligently analyze and suggest next steps
/auto "help me understand this project and suggest improvements"
```

**Expected result**: Framework provides intelligent analysis of your codebase with specific, actionable suggestions.

## ✅ Success Validation

If successful, you should see:

- [ ] **No error messages**: All commands execute cleanly
- [ ] **Project analysis**: Framework describes your actual project structure
- [ ] **Intelligent suggestions**: Recommendations specific to your codebase
- [ ] **Confident responses**: Framework "understands" your project context

## 🎉 Congratulations - You Did It!

You now have a working Claude Code framework installation! Here's what just happened:

### What the Framework Learned About Your Project
- **Structure**: Analyzed your directory layout and file organization
- **Technology**: Detected your programming languages and frameworks
- **Context**: Understood your project type and development patterns
- **Opportunities**: Identified specific areas for improvement

### What You Can Do Next (Choose One)

#### Option A: Explore More Commands (2 minutes)
```bash
# Try different command types
/query "find all TODO comments in the codebase"
/task "add a simple utility function"
/docs "create a basic README"
```

#### Option B: Move to Real Development (5 minutes)
Continue to [first-task/](../first-task/) for hands-on code modification.

#### Option C: Understand Workflows (10 minutes)
Explore [workflows/](../../workflows/) for real-world development patterns.

## 🔧 Quick Customization

### For Different Project Types

**Web Applications**:
```xml
<primary_language>typescript</primary_language>
<framework_stack>react+nextjs</framework_stack>
```

**API Services**:
```xml
<primary_language>go</primary_language>
<framework_stack>gin+postgres</framework_stack>
```

**Data Science**:
```xml
<primary_language>python</primary_language>
<framework_stack>pandas+scikit-learn</framework_stack>
```

**Mobile Apps**:
```xml
<primary_language>typescript</primary_language>
<framework_stack>react-native</framework_stack>
```

### For Different Quality Standards

**High-Quality Production**:
```xml
<threshold>95</threshold>
<enforcement>BLOCKING</enforcement>
```

**Rapid Prototyping**:
```xml
<threshold>70</threshold>
<enforcement>ADVISORY</enforcement>
```

## 🚨 Troubleshooting (If Things Don't Work)

### "Command not found" error?
```bash
# Check if you're in the right directory
pwd
ls CLAUDE.md

# If CLAUDE.md missing, copy framework files again
```

### "Permission denied" error?
```bash
# Fix permissions on macOS/Linux
chmod +x .claude/commands/*
```

### Framework responses seem generic?
```bash
# Update PROJECT_CONFIG.xml with more specific details
# Then try commands again - framework will adapt
```

### Still having issues?
1. **Try a different project**: Test in a simpler directory first
2. **Check framework source**: Ensure you copied from the correct location
3. **Restart fresh**: Delete copied files and try again with careful copy-paste
4. **Get help**: See [troubleshooting guide](../../../docs/reference/troubleshooting.md)

## 💡 Pro Tips for Maximum Success

1. **Trust the copy-paste**: Don't modify commands until you see success
2. **Start in a test directory**: Try in a simple project first if your main project is complex
3. **Read the responses**: Framework provides detailed, project-specific insights
4. **Experiment fearlessly**: Commands are read-only until you explicitly make changes
5. **Progress gradually**: Master hello-world before moving to more complex examples

## 📚 What You Just Learned

- ✅ **Framework Installation**: How to copy and configure framework files
- ✅ **Command Execution**: Basic syntax and immediate feedback
- ✅ **Project Integration**: How framework adapts to your specific codebase
- ✅ **Intelligent Routing**: Framework automatically understands context and provides relevant assistance
- ✅ **Configuration**: Basic PROJECT_CONFIG.xml customization

## 🎯 Next Steps

### Immediate (Right Now)
- **Try more commands**: Experiment with `/query`, `/task`, `/docs`
- **Explore responses**: Read framework suggestions carefully
- **Build confidence**: Every successful command increases framework trust

### Next 5 Minutes
- **Move to [first-task/](../first-task/)**: Make your first actual code change
- **Try intelligent routing**: Use `/auto` for complex requests
- **Learn command selection**: Understand when to use which command

### Next 30 Minutes
- **Explore [workflows/](../../workflows/)**: Real-world development patterns
- **Customize configuration**: Fine-tune PROJECT_CONFIG.xml for your needs
- **Share success**: Show teammates what you just accomplished

---

**Success checkpoint**: You now have a working framework installation! 🎉

**Ready for real development?** Continue to [first-task/](../first-task/) to make your first code change via the framework.

**Want to understand patterns?** Explore [workflows/](../../workflows/) to see how professionals use the framework daily.