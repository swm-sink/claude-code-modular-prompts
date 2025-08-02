# Setup Guide

## Quick Setup

### Method 1: Git Submodule (Recommended)
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh
```

### Method 2: Direct Integration
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../your-project
```

### Method 3: Selective Copy
Choose specific commands/components to copy manually.

## Result

After setup, you'll have:
- Customized `.claude/` directory with comprehensive command templates
- Working copy of extensive reusable components
- Guide commands for customization assistance

## Next Steps

1. Use `/adapt-to-project` for customization checklist
2. Manual Find & Replace of placeholders in your editor
3. Use `/validate-adaptation` to verify setup

## Customization Timeline

- **Hour 1**: Install templates, get customization guide
- **Hours 2-3**: Manual Find & Replace work  
- **Hour 4**: Test and verify customizations
- **Ongoing**: Manual updates when needed

*See CLAUDE.md for complete project context and USAGE.md for command examples.*