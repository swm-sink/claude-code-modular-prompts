# Frequently Asked Questions (FAQ)

> **Quick answers to common questions about the Claude Code Framework**

## 🚀 Getting Started

### Q: What is the Claude Code Framework?
**A:** It's a modular prompt engineering framework that enhances Claude Code with 108+ specialized modules, intelligent command routing, quality gates, and meta-prompting capabilities. Think of it as a productivity multiplier for development with Claude.

### Q: How long does setup take?
**A:** Initial setup takes 2-5 minutes. Copy three files (CLAUDE.md, PROJECT_CONFIG.xml, .claude/) to your project and you're ready to go.

### Q: Do I need to install any software?
**A:** No installation required. The framework works entirely through Claude Code's conversation interface. Just copy the framework files to your project directory.

### Q: Will this work with my tech stack?
**A:** Yes! The framework adapts to any technology stack through PROJECT_CONFIG.xml. It supports web development, mobile, data science, DevOps, and more.

## 💻 Commands

### Q: Which command should I use?
**A:** When in doubt, use `/auto`. It intelligently routes to the right command:
- **Understanding code**: `/query`
- **Small changes**: `/task`
- **New features**: `/feature`
- **Complex work**: `/swarm`
- **Documentation**: `/docs`

### Q: What's the difference between /task and /feature?
**A:** 
- `/task`: Focused work on 1-3 files, quick fixes, small enhancements
- `/feature`: Complete user-facing functionality, generates PRD, comprehensive approach

### Q: Do I need to use quotes in commands?
**A:** Yes, always use quotes for command descriptions:
- ✅ `/task "fix login bug"`
- ❌ `/task fix login bug`

### Q: Can I chain multiple commands?
**A:** Yes! Use `/chain` for complex workflows or execute commands sequentially for multi-step processes.

## 🔧 Configuration

### Q: How do I customize for my project?
**A:** Edit PROJECT_CONFIG.xml with your:
- Project name and domain
- Primary language and framework
- Directory structure
- Quality thresholds

### Q: What are the dynamic placeholders?
**A:** The framework uses `[PROJECT_CONFIG: path | DEFAULT: value]` syntax to adapt to your configuration automatically.

### Q: Can I change quality standards?
**A:** Yes, modify the `<quality_standards>` section in PROJECT_CONFIG.xml. You can adjust test coverage thresholds, performance targets, and enforcement levels.

## 🛡️ Quality Gates

### Q: Why does the framework enforce TDD?
**A:** TDD (Test-Driven Development) is proven to reduce bugs by 40-80%. The framework enforces RED→GREEN→REFACTOR to ensure reliable, maintainable code.

### Q: Can I disable quality gates?
**A:** You can change enforcement from BLOCKING to WARNING in PROJECT_CONFIG.xml, but we strongly recommend keeping quality gates active.

### Q: What does 90% test coverage mean?
**A:** It means 90% of your code lines are executed by tests. This is measured by tools like pytest-cov, jest, or language-specific coverage tools.

## 🤖 Meta-Prompting

### Q: What are meta-commands?
**A:** Meta-commands (`/meta-*`) enable the framework to self-improve:
- `/meta-review`: Audit framework health
- `/meta-evolve`: Adapt to your patterns
- `/meta-optimize`: Improve performance
- `/meta-fix`: Diagnose and fix issues

### Q: Is the framework learning from my usage?
**A:** Yes, with safety boundaries. The framework recognizes patterns and optimizes, but core functionality remains stable with human oversight.

### Q: Can I rollback framework changes?
**A:** Yes, all changes can be rolled back within 60 seconds. The framework maintains stability while evolving.

## 🐛 Troubleshooting

### Q: "Command not found" - what's wrong?
**A:** Check that:
1. You're in the project directory with CLAUDE.md
2. You're using the `/` prefix: `/task` not `task`
3. You're using quotes: `/task "description"`

### Q: "Permission denied" errors
**A:** Quick fix:
```bash
chmod +x .claude/commands/*
rm -f .claude/settings.local.json && ln -sf ~/.claude/settings.json .claude/settings.local.json
```

### Q: Framework doesn't understand my project
**A:** Update PROJECT_CONFIG.xml with your actual tech stack, domain, and primary language. The framework adapts based on this configuration.

### Q: Commands are slow to respond
**A:** Try:
1. `/meta-optimize` to improve performance
2. Use focused commands instead of broad ones
3. Check for large files that might be slowing analysis

## 📚 Advanced Usage

### Q: Can I create custom modules?
**A:** Yes! See the [Extending Framework](../advanced/extending-framework.md) guide. Custom modules integrate seamlessly with existing commands.

### Q: How do I use the 108+ modules directly?
**A:** Commands automatically orchestrate modules. For direct usage, modules are in `.claude/modules/` with documentation in each file.

### Q: Can multiple developers use the framework?
**A:** Yes! Share PROJECT_CONFIG.xml and use `/session` for tracking. The framework supports team collaboration through GitHub integration.

### Q: How does GitHub integration work?
**A:** Commands like `/swarm` and `/session` automatically create GitHub issues for tracking. Ensure you have GitHub CLI (`gh`) installed and authenticated.

## 🎯 Best Practices

### Q: What's the recommended workflow?
**A:** Research → Plan → Execute:
1. `/query` to understand
2. `/auto` or `/feature` to plan
3. Execute with appropriate command
4. `/docs` to document

### Q: Should I use /auto or specific commands?
**A:** Start with `/auto` when unsure. As you learn the framework, use specific commands for more control.

### Q: How often should I run meta-commands?
**A:** 
- `/meta-review`: Weekly or when issues arise
- `/meta-optimize`: Monthly or when performance degrades
- `/meta-evolve`: When you notice repetitive patterns

## 🔒 Security & Performance

### Q: Is my code secure with the framework?
**A:** Yes. The framework:
- Runs locally in your environment
- Doesn't send code anywhere
- Enforces security best practices
- Includes threat modeling in quality gates

### Q: How much does the framework add to token usage?
**A:** The framework is token-optimized. Initial context setup uses ~4-8K tokens, but intelligent routing and caching minimize ongoing usage.

### Q: Can I use this in production?
**A:** Yes! Use `/protocol` for production-critical operations. It enforces maximum quality gates and safety measures.

## 📞 Getting Help

### Q: Where can I find more documentation?
**A:** 
- **Quick Start**: [Getting Started Guide](../getting-started/quick-start.md)
- **Commands**: [Commands Reference](commands-reference.md)
- **Workflows**: [Common Patterns](../user-guide/workflows/common-patterns.md)
- **Troubleshooting**: [Troubleshooting Guide](troubleshooting.md)

### Q: How do I report issues?
**A:** Use `/meta-review` to diagnose issues, then `/query` to analyze specific problems. Document findings for reporting.

### Q: Is there a community or support channel?
**A:** Check the [GitHub repository](https://github.com/swm-sink/claude-code-modular-prompts) for issues and discussions.

---

**Don't see your question?** Try:
- `/query "your specific question about the framework"`
- `/auto "help me understand [topic]"`
- Check the [Troubleshooting Guide](troubleshooting.md)

**Want to contribute?** See [Contributing Guide](../advanced/contributing.md) to help improve the framework!