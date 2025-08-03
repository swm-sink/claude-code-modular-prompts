# Claude Code Framework - 2-Minute Demo Script

**🎯 Objective**: Show empty project → fully configured Claude Code setup in under 5 minutes

## Demo Flow

### Scene 1: The Problem (30 seconds)
**Narration**: "Learning Claude Code takes months. Here's how to get 6+ months of knowledge in 5 minutes."

**Screen**: Show empty project directory
```bash
# Terminal: Show fresh project
mkdir my-awesome-project
cd my-awesome-project
ls -la
# -> Empty directory, just .git
```

### Scene 2: The Solution (60 seconds)
**Narration**: "Add our framework as a git submodule and run one script."

**Screen**: Git submodule integration
```bash
# Terminal: Add framework
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework

# Terminal: Run setup
cd .claude-framework
./setup.sh --project-name "my-awesome-project" --profile web-dev
```

**Screen**: Show setup script output with colorized progress
- ✓ Creating directory structure...
- ✓ Installing web-dev profile...
- ✓ Installing components...
- ✓ Setup Complete! 🎉

### Scene 3: The Result (30 seconds)
**Narration**: "Now you have a complete Claude Code setup with anti-patterns, commands, and components."

**Screen**: Show installed structure
```bash
# Terminal: Show what was created
cd ..
tree .claude
# Shows:
# .claude/
# ├── commands/
# │   ├── core/
# │   ├── development/
# │   └── web/
# ├── components/
# ├── context/
# └── CLAUDE.md
```

**Screen**: Show command count
```bash
find .claude/commands -name "*.md" | wc -l
# -> Shows number of commands installed
```

### Scene 4: Test It Works (30 seconds)
**Narration**: "Open Claude Code and start using the commands immediately."

**Screen**: Show Claude Code usage
```bash
# In Claude Code interface, show:
/help
# -> Framework help appears with available commands

/task "Add user authentication"
# -> Shows TDD workflow guidance
```

## Key Metrics to Highlight

**Visual Overlays**:
- ⏱️ **Time**: Live timer showing < 5 minutes total
- 📁 **Commands**: "79 battle-tested patterns"
- 🛡️ **Anti-patterns**: "48+ mistakes prevented"
- 🧠 **Knowledge**: "6+ months of learning"

## Technical Setup

### Recording Requirements
- **Resolution**: 1920x1080 minimum
- **Frame Rate**: 30fps
- **Audio**: Clear narration, no background music
- **Terminal**: Large font (16pt+), high contrast theme
- **Screen**: Clean desktop, focus on terminal

### Preparation Checklist
- [ ] Fresh Ubuntu/macOS virtual machine
- [ ] Git configured with demo credentials
- [ ] Terminal with clean theme and large fonts
- [ ] Test run of entire script (< 4 minutes to allow buffer)
- [ ] Backup plan if git submodule fails (direct clone)

## Script Variations

### Version A: Git Submodule (Primary)
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh
```

### Version B: Direct Clone (Fallback)
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./adapt.sh ../my-project
```

### Version C: Profile Demo (Extended)
Show different profiles:
```bash
./setup.sh --profile web-dev     # Web development
./setup.sh --profile data-science # Data science  
./setup.sh --profile devops      # DevOps
```

## Call to Action (End Screen)

**Text Overlay**:
```
🚀 Get Started in 5 Minutes:
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh

⭐ Star the repo: github.com/swm-sink/claude-code-modular-prompts
💬 Questions? Check our FAQ or GitHub Discussions
🤝 Contribute patterns back to help others
```

## Post-Production Notes

### Titles/Graphics
- Opening: "Claude Code Framework - 6 Months in 5 Minutes"
- Progress indicators during setup
- Command highlighting with syntax colors
- Success checkmarks for completed steps

### Editing Notes
- Speed up terminal output (1.2x-1.5x)
- Zoom in on important output (command counts, success messages)
- Add smooth transitions between scenes
- Keep narration concise and energetic

### Distribution
- **YouTube**: Main platform, optimize for search
- **GitHub README**: Embed as primary demo
- **Twitter**: Short clips highlighting key benefits
- **Documentation**: Include in SETUP.md

---

**Target Length**: 2 minutes (demo) + 30 seconds (call to action) = 2:30 total

*Ready for production - script validated against working setup.sh*