# Frequently Asked Questions (FAQ)

## Table of Contents
1. [Getting Started](#getting-started)
2. [Commands](#commands)
3. [Configuration](#configuration)
4. [Quality and Testing](#quality-and-testing)
5. [Performance](#performance)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Usage](#advanced-usage)
8. [Meta-Framework](#meta-framework)
9. [Security and Privacy](#security-and-privacy)
10. [Migration and Integration](#migration-and-integration)
11. [Limitations and Workarounds](#limitations-and-workarounds)
12. [Best Practices](#best-practices)
13. [Quick Reference](#quick-reference)

**Quick answers to common questions:**
- **How do I know if the framework is working?** → Try `/auto "test framework setup"`
- **Which command should I use?** → Use `/auto` when uncertain
- **Why are responses slow?** → Check [Performance](#performance) section
- **Commands not working?** → See [Troubleshooting](#troubleshooting) section

## Getting Started

### Q: How do I know if the framework is working?
**A:** You should see structured, command-driven responses instead of generic AI responses. Try:
```bash
/auto "test framework setup"
```
If you get a generic response, check that CLAUDE.md is in your project root directory.

### Q: Do I need to install anything special?
**A:** No additional installation required. The framework works through:
1. **CLAUDE.md** file in your project root
2. **PROJECT_CONFIG.xml** for project-specific settings
3. **Claude Code CLI** (already installed if you're using this)

### Q: Can I use this with any programming language?
**A:** Yes! The framework supports all major languages. Configure your language in PROJECT_CONFIG.xml:
```xml
<tech_stack>
  <primary_language>python | javascript | typescript | go | rust | java | php</primary_language>
</tech_stack>
```

### Q: How is this different from regular Claude?
**A:** The framework provides:
- **Structured commands** instead of free-form chat
- **TDD enforcement** for all code changes
- **Quality gates** with coverage requirements
- **Project-specific adaptation** through configuration
- **Consistent workflows** across different tasks

## Commands

### Q: Which command should I use?
**A:** Use the decision tree:
- **Unsure what to do?** → `/auto "describe what you want"`
- **Need to understand code?** → `/query "what you want to understand"`
- **Single file/function change?** → `/task "specific change"`
- **Complete new feature?** → `/feature "feature description"`
- **Need documentation?** → `/docs "documentation needed"`

### Q: What happens if I use the wrong command?
**A:** The framework will often suggest the correct command or automatically route to the appropriate approach. You can also use `/auto` which intelligently selects the best command.

### Q: Can I chain commands together?
**A:** Yes! You can use commands in sequence:
```bash
1. /query "understand the authentication system"
2. /task "fix the login validation bug"
3. /protocol "prepare fix for production"
```

### Q: What's the difference between /task and /feature?
**A:** 
- **`/task`**: Single component, <50 lines, focused change
- **`/feature`**: Multiple components, complete functionality, requires PRD

## Configuration

### Q: Is PROJECT_CONFIG.xml required?
**A:** Recommended but not required. Without it, you get generic framework behavior. With it, you get:
- Tech stack-specific responses
- Project-specific quality standards
- Customized workflows
- Domain expertise

### Q: How do I customize the framework for my team?
**A:** Configure PROJECT_CONFIG.xml with your specifics:
```xml
<project_config>
  <tech_stack>
    <primary_language>python</primary_language>
    <framework>django</framework>
    <database>postgresql</database>
  </tech_stack>
  <team_preferences>
    <code_style>pep8</code_style>
    <testing_framework>pytest</testing_framework>
    <deployment>kubernetes</deployment>
  </team_preferences>
</project_config>
```

### Q: Can I disable TDD enforcement?
**A:** Not recommended, but possible:
```xml
<quality_standards>
  <test_coverage>
    <threshold>0</threshold>
    <enforcement>warning</enforcement>
  </test_coverage>
</quality_standards>
```
**Note**: This defeats the purpose of quality assurance.

## Quality and Testing

### Q: Why does the framework insist on writing tests first?
**A:** TDD (Test-Driven Development) is enforced because it:
- **Improves code quality** by thinking through requirements first
- **Reduces bugs** by catching issues early
- **Provides documentation** through test cases
- **Ensures maintainability** with comprehensive test coverage

### Q: What if my project doesn't have tests?
**A:** The framework will help you start:
1. Use `/task "add test infrastructure"` to set up testing
2. Use `/task "add tests for [specific function]"` to add coverage
3. Gradually increase coverage with each change

### Q: How do I check my test coverage?
**A:** The framework automatically runs coverage tools configured in PROJECT_CONFIG.xml:
```xml
<commands>
  <test>pytest --cov=src --cov-report=term-missing --cov-fail-under=90</test>
</commands>
```

## Performance

### Q: Why are responses slow?
**A:** Common causes:
1. **Large codebase** - Framework analyzes entire context
2. **Complex requests** - Break down into smaller tasks
3. **High token usage** - Use `/compact` to reduce context

**Solutions:**
```bash
# Analyze performance
/meta-review "analyze performance bottlenecks"

# Optimize framework
/meta-optimize "improve response time"
```

### Q: How can I reduce token usage?
**A:** 
1. **Use specific commands** instead of `/auto` for everything
2. **Break down large requests** into smaller tasks
3. **Use `/compact`** to summarize long sessions
4. **Configure context limits** in PROJECT_CONFIG.xml

### Q: Can I run multiple commands in parallel?
**A:** Yes, for independent tasks:
```bash
# Use /swarm for parallel coordination
/swarm "optimize database queries, add user authentication, and update documentation"
```

## Troubleshooting

### Q: Commands aren't working - I get generic responses
**A:** Check these in order:
1. **CLAUDE.md location** - Must be in project root
2. **File content** - Should contain framework configuration
3. **PROJECT_CONFIG.xml** - Should be customized for your project
4. **Try restart** - Close and reopen Claude Code

### Q: Framework is too strict about code quality
**A:** You can adjust quality standards in PROJECT_CONFIG.xml:
```xml
<quality_standards>
  <test_coverage>
    <threshold>75</threshold>  <!-- Reduced from 90% -->
  </test_coverage>
  <performance>
    <response_time_p95>500</response_time_p95>  <!-- Relaxed from 200ms -->
  </performance>
</quality_standards>
```

### Q: How do I reset the framework?
**A:** 
```bash
# Soft reset - restore configuration
cp CLAUDE.md.backup CLAUDE.md
cp PROJECT_CONFIG.xml.template PROJECT_CONFIG.xml

# Hard reset - remove all customizations
rm -rf .claude/
/init "reset framework to defaults"
```

## Advanced Usage

### Q: Can I create custom commands?
**A:** The framework has a fixed set of commands, but you can:
1. **Use `/auto`** for intelligent routing
2. **Customize PROJECT_CONFIG.xml** for project-specific behavior
3. **Use `/meta-evolve`** to adapt framework to your patterns

### Q: How do I integrate with my team's workflow?
**A:** Configure team-specific settings:
```xml
<team_workflow>
  <code_review>
    <required>true</required>
    <reviewers>2</reviewers>
  </code_review>
  <deployment>
    <strategy>blue-green</strategy>
    <environment>kubernetes</environment>
  </deployment>
</team_workflow>
```

### Q: Can I use this for non-coding tasks?
**A:** Yes! Commands work for various tasks:
- **`/docs`** - Documentation and README files
- **`/query`** - Research and analysis
- **`/feature`** - Process design and planning
- **`/protocol`** - Deployment and operational procedures

### Q: How do I contribute to the framework?
**A:** 
1. **Report issues** - Use GitHub issues for bugs
2. **Suggest improvements** - Use `/meta-evolve` to adapt framework
3. **Share patterns** - Document successful workflows
4. **Contribute examples** - Add real-world usage examples

## Meta-Framework

### Q: What do the /meta-* commands do?
**A:** Meta-commands manage the framework itself:
- **`/meta-review`** - Analyze framework performance and usage
- **`/meta-optimize`** - Improve framework efficiency
- **`/meta-evolve`** - Adapt framework to your patterns
- **`/meta-govern`** - Enforce compliance and governance

### Q: How does the framework learn from my usage?
**A:** The framework:
1. **Tracks usage patterns** through meta-commands
2. **Adapts to your tech stack** via PROJECT_CONFIG.xml
3. **Improves over time** with `/meta-evolve`
4. **Optimizes performance** with `/meta-optimize`

### Q: Can I see framework analytics?
**A:** Yes, use meta-review:
```bash
/meta-review "show usage analytics and performance metrics"
```

## Security and Privacy

### Q: Is my code secure?
**A:** The framework:
- **Processes code locally** through Claude Code CLI
- **Follows security best practices** in generated code
- **Enforces threat modeling** for new features
- **Validates security patterns** in reviews

### Q: What data is stored?
**A:** The framework stores:
- **Configuration** in PROJECT_CONFIG.xml
- **Usage patterns** for optimization (locally)
- **Framework state** in .claude/ directory
- **No sensitive code** is permanently stored

## Migration and Integration

### Q: How do I migrate an existing project?
**A:** 
1. **Add CLAUDE.md** to project root
2. **Create PROJECT_CONFIG.xml** with your tech stack
3. **Start with `/query`** to understand existing code
4. **Use `/task`** for incremental improvements
5. **Add tests gradually** with each change

### Q: Can I use this with existing CI/CD?
**A:** Yes! The framework integrates with:
- **Git workflows** - Commits and branches
- **Testing frameworks** - Pytest, Jest, etc.
- **Quality tools** - Linting, coverage, security scanning
- **Deployment pipelines** - Through `/protocol` command

### Q: How do I handle team onboarding?
**A:** 
1. **Share PROJECT_CONFIG.xml** with team settings
2. **Create team-specific examples** in examples/
3. **Document team workflows** in docs/
4. **Use `/docs`** to create onboarding guides

## Limitations and Workarounds

### Q: What can't the framework do?
**A:** Current limitations:
- **No custom commands** - Fixed command set
- **No GUI** - Command-line interface only
- **Language-specific** - May not support all languages equally
- **Context limits** - Large codebases may hit token limits

### Q: How do I work around context limits?
**A:** 
1. **Use specific commands** instead of broad analysis
2. **Break down large requests** into smaller tasks
3. **Use `/compact`** to summarize context
4. **Configure context limits** in PROJECT_CONFIG.xml

### Q: What if the framework makes mistakes?
**A:** 
1. **Validate all generated code** before committing
2. **Run tests** to catch issues early
3. **Use `/query`** to understand before implementing
4. **Provide feedback** for framework improvement

## Best Practices

### Q: What are the framework best practices?
**A:** 
1. **Always configure PROJECT_CONFIG.xml** for your project
2. **Use `/query` first** to understand before changing
3. **Follow TDD** - tests before implementation
4. **Use specific commands** when you know what you want
5. **Regular `/meta-review`** to optimize usage

### Q: How do I get the most value from the framework?
**A:** 
1. **Customize thoroughly** - PROJECT_CONFIG.xml is key
2. **Use regularly** - Framework learns from usage
3. **Follow quality gates** - Don't skip TDD
4. **Leverage meta-commands** - Continuous improvement
5. **Share with team** - Consistent workflows

---

## Quick Reference

### Most Common Solutions
```bash
# Framework not working
# → Check CLAUDE.md in project root

# Generic responses
# → Configure PROJECT_CONFIG.xml

# Slow performance
/meta-optimize "improve performance"

# Quality gates too strict
# → Adjust thresholds in PROJECT_CONFIG.xml

# Don't know which command
/auto "describe what you want"
```

### Emergency Commands
```bash
# Complete reset
/init "emergency framework reset"

# Performance issues
/meta-review "analyze performance problems"

# Configuration issues
/validate "check framework configuration"
```

**Still need help?** Check the [Troubleshooting Guide](troubleshooting.md) or use `/query "framework help with [specific issue]"`