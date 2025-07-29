# Demo Recording Quick Guide

## Pre-Recording Setup (5 minutes)

### 1. Environment Preparation
```bash
# Create clean demo environment
mkdir demo-recording
cd demo-recording

# Initialize fresh git repo
git init
git config user.name "Demo User"
git config user.email "demo@example.com"

# Create initial commit
echo "# My Awesome Project" > README.md
git add README.md
git commit -m "Initial commit"
```

### 2. Terminal Setup
- **Font Size**: 16pt minimum (18pt recommended)
- **Theme**: High contrast (dark background, bright text)
- **Window Size**: 1200x800 minimum
- **Zoom**: Ensure text is readable in 1080p video

### 3. Test Run
```bash
# Practice the complete flow:
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework
./setup.sh --project-name "my-awesome-project" --profile web-dev
cd ..
tree .claude  # or ls -la .claude
find .claude/commands -name "*.md" | wc -l
```

## Recording Checklist

### Start Recording
- [ ] Desktop is clean
- [ ] Terminal is prepared and sized correctly
- [ ] Timer/stopwatch is ready
- [ ] Audio levels are good
- [ ] Demo repo is ready

### Scene-by-Scene
- [ ] **Scene 1**: Show empty project, emphasize the problem
- [ ] **Scene 2**: Add submodule, run setup, show progress
- [ ] **Scene 3**: Display results, count commands
- [ ] **Scene 4**: Quick Claude Code test (if possible)

### Key Shots to Capture
- [ ] Empty directory (`ls -la`)
- [ ] Git submodule command execution
- [ ] Setup script colorized output
- [ ] Final `.claude` directory structure
- [ ] Command count verification
- [ ] Success message

## Backup Plans

### If Git Submodule Fails
```bash
# Use direct clone method
git clone https://github.com/swm-sink/claude-code-modular-prompts claude-framework
cd claude-framework
./adapt.sh ../my-project
```

### If Internet Issues
- Pre-download the repository
- Use local git server setup
- Have screenshots ready as fallback

### If Setup Script Issues
- Have manual command sequence ready
- Prepare explanation of what should happen
- Keep troubleshooting steps handy

## Post-Recording

### Editing Notes
- Speed up terminal output to 1.3x
- Add zoom-in for important text
- Include progress overlays:
  - Timer showing < 5 minutes
  - Step indicators (1/4, 2/4, etc.)
  - Success checkmarks

### Export Settings
- **Resolution**: 1920x1080
- **Format**: MP4 (H.264)
- **Bitrate**: 8-10 Mbps
- **Audio**: 48kHz, 256kbps

## Upload Checklist

### YouTube
- [ ] Title: "Claude Code Framework - 6 Months in 5 Minutes"
- [ ] Description with repository link
- [ ] Tags: claude-code, ai, automation, prompt-engineering
- [ ] Thumbnail with clear value proposition

### GitHub
- [ ] Add to README.md as primary demo
- [ ] Include in SETUP.md documentation
- [ ] Link from main repository description

---

**Estimated Recording Time**: 15 minutes prep + 10 minutes recording + 30 minutes editing = 1 hour total

*This guide ensures a smooth, professional demo that showcases the framework's value proposition effectively.*