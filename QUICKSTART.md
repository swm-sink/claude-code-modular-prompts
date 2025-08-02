# Quick Start Guide

## 30-Second Installation

```bash
# Clone the repository
git clone https://github.com/swm-sink/claude-code-modular-prompts.git
cd claude-code-modular-prompts

# Run setup script
./setup.sh /path/to/your/project

# Start using in Claude Code
cd /path/to/your/project
claude
```

## First Commands

Once installed, try these commands in Claude Code:

```
/help                           # See all available commands
/task "implement user login"    # Execute a development task
/analyze-code                   # Analyze your codebase
/quick-command search "TODO"    # Create a custom search command
```

## What Happens During Setup

1. **Copies template files** to your project's `.claude/` directory
2. **Preserves reference copy** in `.claude-framework/` for updates
3. **Creates guide commands** to help with customization

## Next Steps

- Run `/adapt-to-project` for a customization checklist
- Run `/replace-placeholders` to see what needs manual updates
- Read [SETUP.md](SETUP.md) for detailed installation options
- Check [EXAMPLES.md](EXAMPLES.md) for usage examples

## Common Issues

**Templates have placeholders:**
- This is by design - templates need customization for your project
- Use `/replace-placeholders` to get a complete list
- Manual Find & Replace in your editor is the fastest method

**Commands not working:**
- Ensure you're in a Claude Code session
- Check that `.claude/` directory exists in your project
- Verify YAML frontmatter is correct with `/validate-adaptation`

## Support

- GitHub Issues: [Report problems](https://github.com/swm-sink/claude-code-modular-prompts/issues)
- Documentation: See `/help` command for comprehensive guide