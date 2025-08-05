---
name: /begin-consultation
description: Start interactive 30+ minute consultation to transform Claude into YOUR project expert
usage: "/begin-consultation [phase] [resume]"
allowed-tools: [Read, Write, Edit, LS, Glob, Grep, TodoWrite]
category: consultation
version: "1.0"
---

# Begin Consultation: Transform Claude Into YOUR Project Expert

## Purpose
This command initiates a comprehensive 30+ minute interactive consultation that transforms generic Claude Code into a specialized expert for YOUR specific project through systematic context engineering.

## 🎯 What You'll Get
After completing this consultation, Claude will:
- **Understand your architecture** - Know your frameworks, patterns, and technical decisions
- **Speak your domain language** - Use your business terminology and understand your goals  
- **Navigate your codebase** - Know where to find files and how your project is organized
- **Follow your standards** - Respect your coding conventions and quality requirements

## 📋 Consultation Process

### Phase 1: Technical Analysis (10-15 minutes)
Deep analysis of your project's technical architecture, framework patterns, and development environment.

**Key Analysis Areas:**
- **Framework Detection**: Identify React/Vue/Angular, Django/Flask/Rails, etc.
- **Project Structure**: Understand your directory organization and file patterns
- **Development Workflow**: Testing strategies, build processes, deployment methods
- **Quality Standards**: Code style, linting rules, performance requirements

### Phase 2: Domain Intelligence (10-15 minutes)  
Extraction of business domain knowledge, terminology, and project-specific patterns.

**Intelligence Extraction:**
- **Business Domain**: E-commerce, fintech, healthcare, etc. with specific terminology
- **User Workflows**: How users interact with your application
- **Data Models**: Key entities, relationships, and business logic
- **Integration Patterns**: APIs, services, and external dependencies

### Phase 3: Context Generation (5-10 minutes)
Creation of a multi-file hierarchical context system with your approval at every step.

**Generated Artifacts:**
- **Enhanced CLAUDE.md** - Project memory with comprehensive context
- **Context Directory** - Organized context files in `.claude/context/`
- **Navigation System** - Cross-references and file hop patterns
- **Session State** - Support for future consultation updates and improvements

## 🚀 Getting Started

### Prerequisites
- Claude Code installed and active in your project
- 30+ minutes available for comprehensive consultation
- Basic understanding of your project's goals and architecture

### Starting the Consultation
```
/begin-consultation
```

### Session Management
- **Pause**: Type `PAUSE` at any prompt to save progress
- **Resume**: Run `/begin-consultation resume` to continue
- **Skip Phase**: Use `/begin-consultation phase-2` to jump to specific phase
- **Restart**: Run `/begin-consultation reset` to start over

### What to Expect
1. **Interactive Questions**: The system will ask about your project specifics
2. **Multiple Choice Options**: Choose from detected frameworks and patterns  
3. **Confirmation Steps**: Review and approve all generated content
4. **Real-time Feedback**: See context being built as you progress

## 💡 Pro Tips
- **Be Specific**: Detailed answers create better context
- **Use Examples**: Mention specific files, functions, or workflows
- **Think Long-term**: Consider how your project might evolve
- **Save Progress**: Use pause/resume for longer consultations

## 🔧 Troubleshooting
- **Command not found**: Ensure you're in a directory with `.claude/` folder
- **Session lost**: Check `.claude/consultation-state.json` for recovery
- **Context conflicts**: Review generated files before finalizing

## Next Steps
After consultation completion:
1. Test Claude with project-specific commands (`/task`, `/analyze`, `/debug`)
2. Refine context using `/update-context` command
3. Share successful patterns with your team

**Result**: Claude becomes a true expert in YOUR specific project, not just generic development tasks.