# Frequently Asked Questions

## Installation

**Q: How long does setup take?**
A: 30 seconds. One command, no configuration required.

**Q: Do I need to customize anything?**
A: No. All commands work immediately with any programming language or framework.

**Q: What if I already have a .claude directory?**
A: The setup script will back up your existing .claude to .claude.backup before installing.

## Usage

**Q: Do these commands work with my tech stack?**
A: Yes. Commands automatically adapt to any programming language, framework, or project type.

**Q: Which command should I try first?**
A: Start with `/help` to see all commands, then try `/task "your development goal"`.

**Q: Can I modify the commands?**
A: Yes. Edit the files in `.claude/commands/` to customize them for your needs.

## Troubleshooting

**Q: Commands don't show up in Claude Code**
A: 
1. Make sure you're in the project directory where you ran setup
2. Restart Claude Code completely  
3. Try `/help` - if it doesn't work, the commands aren't loaded

**Q: Setup script says "permission denied"**
A: Run `chmod +x setup-minimal.sh` then try again.

**Q: I want more commands**
A: This repo contains 64+ additional commands, but they require manual customization. Most users find the 7 essential commands handle 90% of their needs.

## Team Usage

**Q: Can my team use this?**
A: Yes. Each team member runs the same 30-second setup command.

**Q: How do we share custom commands?**
A: Add your custom commands to `.claude/commands/` and commit them to your project repository.

**Q: What if team members have different setups?**
A: The installation is identical for everyone - 7 commands that work the same way.

## Advanced

**Q: Can I add more commands later?**
A: Yes. Copy individual `.md` files from the full template library, or write your own.

**Q: How do I update to newer versions?**
A: If you used git submodule: `cd .claude-templates && git pull`
If you used direct clone: re-run the setup script from a fresh clone.

**Q: Is this officially supported by Claude/Anthropic?**
A: No, this is a community project. It's based on real experience but not officially endorsed.

## Getting Help

**Q: Where can I get help?**
A: 
- Start with the `/help` command in Claude Code
- Check USAGE.md for detailed examples
- GitHub Issues for bugs
- GitHub Discussions for questions

**Q: How do I report problems?**
A: Create a GitHub issue with:
- What command you tried
- What happened vs. what you expected  
- Your operating system and project type

## Philosophy

**Q: Why only 7 commands?**
A: Quality over quantity. These 7 commands handle the vast majority of development tasks, work immediately, and require no setup time.

**Q: Why not use the comprehensive template library?**
A: Most users prefer commands that work immediately over extensive customization. You can always add more commands later if needed.