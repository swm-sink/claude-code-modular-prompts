---
name: /consult-workflow
description: Team workflow and collaboration pattern consultation focusing on development processes and team conventions
usage: "/consult-workflow [quick|standard|comprehensive] [resume]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite]
category: consultation
version: "1.0"
---

# Workflow Pattern Consultation: Team Collaboration & Development Process Discovery

## Purpose
This command provides focused team workflow consultation (7-10 minutes) that extracts deep understanding of your team's development processes, collaboration patterns, coding standards, and quality practices. Designed as both a standalone consultation and cross-cutting analysis for the full consultation flow.

## 🎯 What This Consultation Discovers

**Development Workflow Intelligence:**
- Development lifecycle and process patterns (agile, waterfall, hybrid)
- Code review processes, approval workflows, and quality gates
- Branch strategies, deployment patterns, and release cycles
- Team collaboration tools and communication patterns

**Quality & Standards Understanding:**
- Coding standards, style guides, and formatting preferences
- Documentation requirements and knowledge sharing practices
- Testing strategies, coverage requirements, and quality metrics
- Error handling, logging, and monitoring conventions

**Team Dynamics & Preferences:**
- Team size, structure, and role responsibilities
- Decision-making processes and technical leadership patterns
- Tool preferences and workflow automation
- Learning culture and knowledge transfer approaches

## 📋 Consultation Process

### Phase 1: Development Process Discovery (2-3 minutes)
**Process Pattern Recognition:**
- Development methodology and sprint/iteration patterns
- Code review and approval workflow requirements
- Branch strategy and merge/deployment patterns
- Release cycle and deployment frequency preferences

**Intelligent Process Questioning:**
- "I see GitHub Actions workflows. Are you doing continuous deployment or scheduled releases?"
- "Multiple branch protection rules suggest team development. What's your review process?"
- "Semantic versioning in your tags. How do you handle breaking changes and migration?"

### Phase 2: Quality Standards & Conventions (3-4 minutes)
**Standards Pattern Analysis:**
- Code formatting and linting rule preferences
- Documentation standards and comment conventions
- Testing requirements and coverage expectations
- Error handling and logging pattern preferences

**Adaptive Standards Discovery:**
- For TypeScript: "Do you prefer explicit types or type inference? Strict mode enabled?"
- For Python: "PEP 8 compliance or custom style guide? Type hints required or optional?"
- For Documentation: "Inline comments, README-driven, or wiki documentation preferred?"

### Phase 3: Team Collaboration & Tool Integration (2-3 minutes)
**Collaboration Pattern Understanding:**
- Team size and distributed/co-located work patterns
- Communication preferences (async, real-time, documentation-first)
- Knowledge sharing and mentoring approaches
- Tool ecosystem and integration preferences

**Context-Aware Team Questions:**
- Small teams: "How do you handle knowledge sharing and cross-training?"
- Large teams: "What's your process for architectural decisions and standards enforcement?"
- Distributed teams: "How do you maintain code quality and communication across time zones?"

## 🚀 Three Consultation Modes

### Quick Mode (5-7 minutes)
**Essential Workflow Understanding:**
- Basic development process and review requirements
- Key coding standards and formatting preferences
- Primary collaboration tools and communication patterns
- Critical quality gates and testing requirements

### Standard Mode (7-10 minutes) - Default
**Comprehensive Workflow Profile:**
- Complete development lifecycle and process understanding
- Full coding standards and quality requirement mapping
- Team collaboration patterns and decision-making processes
- Tool integration and workflow automation preferences

### Comprehensive Mode (10-15 minutes)
**Deep Workflow Consultation:**
- Advanced process optimization and efficiency analysis
- Detailed quality metrics and continuous improvement patterns
- Leadership and mentoring workflow integration
- Long-term process evolution and scaling considerations

## 🔄 Session Management Integration

### Pause/Resume Support
- Save workflow discovery progress with `/manage-session-state pause`
- Resume workflow consultation with `/consult-workflow resume`
- Session state preserved in `.claude/consultation-state.json`
- Full context restoration including process understanding and preferences

### Integration with Full Consultation
- Workflow findings influence technical and domain consultations
- Process preferences inform context generation and command customization
- Team patterns shape Claude's communication style and suggestion approach
- Progress tracked within overall consultation workflow

### User Control Throughout Process
- **Navigation**: `skip`, `back`, `skip section` commands available
- **Pace Control**: Switch between quick/standard/comprehensive modes mid-session
- **Clarification**: `clarify`, `example`, `more detail` for deeper process understanding
- **Validation**: `review`, `summary` to confirm workflow understanding

## 💡 Interactive Dialogue Examples

### Development Process Discovery Dialogue:
```
⚙️ Workflow Analysis: Development Process Discovery

I've analyzed your repository and found process indicators:
- GitHub Actions with PR-based triggers
- Branch protection rules requiring reviews
- Semantic versioning and release tags
- Issue templates and project boards

Let me understand your specific development workflow:

1. Development Cycle: Are you using agile/scrum, feature-driven development, 
   or a custom process? How long are your typical development cycles?

2. Code Review Process: What's required for code approval? How many reviewers? 
   Any automated checks that must pass before merge?

3. Release Strategy: How often do you deploy? Is it automated after merge, 
   or do you have scheduled release windows?

[User provides workflow-specific context that builds process understanding]
```

### Quality Standards Exploration:
```
📏 Quality Standards & Conventions Analysis

Based on your configuration files, I can see:
- ESLint/Prettier for JavaScript formatting
- TypeScript strict mode enabled
- Jest testing configuration
- Husky pre-commit hooks

Let's understand your quality preferences:

1. Code Style: Are you strict about the current ESLint rules, or are there 
   areas where you're more flexible? Any team-specific conventions?

2. Documentation: What level of documentation do you expect? Inline comments, 
   JSDoc, README updates, or architectural decision records?

3. Testing Philosophy: Do you aim for high coverage, focus on critical paths, 
   or emphasize integration vs unit testing?

[Dialogue adapts based on detected tooling and project maturity]
```

### Team Collaboration Pattern Discovery:
```
👥 Team Collaboration & Communication Analysis

I want to understand how your team works together:

1. Team Structure: How many developers? Are you co-located, distributed, or 
   hybrid? Any specialized roles (frontend, backend, DevOps)?

2. Decision Making: How do architectural decisions get made? Technical lead, 
   team consensus, or formal RFC process?

3. Knowledge Sharing: How do you handle code reviews, mentoring, and 
   knowledge transfer? Pair programming, documentation, or informal discussion?

4. Communication Style: Do you prefer detailed written explanations, concise 
   summaries, or interactive discussion for technical topics?

[Builds understanding of team dynamics that inform Claude's interaction style]
```

## 🎯 Workflow Understanding Output

### Generated Workflow Context Files
After consultation completion, you'll have:

**Development Process Context** (`.claude/context/development-process.md`):
- Complete development lifecycle and methodology understanding
- Code review processes and quality gate requirements
- Branch strategy, deployment patterns, and release cycle preferences
- Process optimization opportunities and efficiency patterns

**Quality Standards Context** (`.claude/context/quality-standards.md`):
- Coding standards, formatting, and style guide preferences
- Documentation requirements and comment conventions
- Testing strategies, coverage expectations, and quality metrics
- Error handling, logging, and monitoring pattern preferences

**Team Collaboration Context** (`.claude/context/team-collaboration.md`):
- Team structure, roles, and responsibility patterns
- Communication preferences and collaboration tool integration
- Decision-making processes and technical leadership patterns
- Knowledge sharing and mentoring approach preferences

**Tool Integration Context** (`.claude/context/tool-integration.md`):
- Development tool ecosystem and workflow automation
- CI/CD pipeline preferences and deployment patterns
- Monitoring, analytics, and feedback loop integration
- Productivity tool preferences and workflow optimization

### Enhanced CLAUDE.md Integration
Workflow findings automatically enhance your project memory with:
- Process awareness for appropriate suggestion timing and scope
- Quality standard alignment for consistent code recommendations
- Team communication style matching for better interaction patterns
- Tool integration understanding for workflow-conscious suggestions

## 🔧 Usage Examples

```bash
# Start focused workflow consultation
/consult-workflow

# Quick process overview (5-7 minutes)
/consult-workflow quick

# Comprehensive workflow deep dive
/consult-workflow comprehensive

# Resume paused workflow consultation
/consult-workflow resume

# Use as cross-cutting analysis in full consultation
/begin-consultation  # Workflow patterns inform all phases
```

## 🤖 Specialized Agent Integration

This consultation leverages specialized workflow analysis agents:

**Process Analysis Agent**: Maps development lifecycle and methodology patterns
**Quality Standards Agent**: Identifies coding standards and quality requirements
**Team Dynamics Agent**: Analyzes collaboration patterns and communication preferences
**Tool Integration Agent**: Maps workflow automation and productivity tool usage

Agents work together to build comprehensive workflow understanding that enables process-aware suggestions and team-conscious technical recommendations.

## 🎯 Success Outcomes

After workflow consultation, Claude will:
- **Match your process**: Align suggestions with your development lifecycle
- **Respect your standards**: Generate code that meets your quality requirements
- **Communicate appropriately**: Use your team's preferred communication style
- **Consider team context**: Factor team size and dynamics into recommendations

**Result**: Claude becomes a team-aware technical advisor who understands not just what to build, but HOW your team prefers to build it.

## 🏗️ Team-Specific Examples

### Small Team (2-5 developers) Workflow Understanding:
```
After workflow consultation, Claude will understand:
- Informal review processes with focus on knowledge sharing
- Direct communication preferences with less formal documentation
- Flexible standards with emphasis on consistency over strict compliance
- Rapid iteration cycles with continuous deployment preferences
- Cross-functional responsibilities and broad technical involvement
```

### Large Team (10+ developers) Workflow Understanding:
```
After workflow consultation, Claude will understand:
- Formal review processes with multiple approval requirements
- Documentation-heavy communication with standardized templates
- Strict coding standards enforcement with automated tooling
- Structured release cycles with comprehensive testing gates
- Specialized roles with clear responsibility boundaries
```

### Distributed Team Workflow Understanding:
```
After workflow consultation, Claude will understand:
- Asynchronous communication preferences with detailed written explanations
- Timezone-aware collaboration patterns and handoff processes
- Documentation-first culture with comprehensive context sharing
- Automated quality gates compensating for reduced real-time review
- Cultural sensitivity in communication style and technical explanation
```

## 📈 Process Optimization Integration

### Continuous Improvement Awareness
Claude learns your approach to:
- **Process Evolution**: How you adapt and improve development practices
- **Bottleneck Resolution**: Your strategies for identifying and addressing workflow issues
- **Team Growth**: How processes scale as team size changes
- **Technology Adoption**: Your approach to evaluating and integrating new tools

### Efficiency Pattern Recognition
Understanding of your preferences for:
- **Automation vs Manual Process**: Where you prefer human oversight vs automated execution
- **Speed vs Quality Balance**: Your team's risk tolerance and quality/velocity trade-offs
- **Innovation vs Stability**: How you balance trying new approaches with proven methods
- **Individual vs Collective**: Preference for individual ownership vs team collaboration

## Next Steps

1. **Test workflow understanding**: Ask Claude process-specific questions
2. **Continue to full consultation**: Run `/begin-consultation` for comprehensive setup
3. **Integrate with technical consultation**: Use `/consult-technical` to combine understanding
4. **Refine workflow context**: Use `/update-context workflow` for adjustments

**Time Investment**: 7-10 minutes for process intelligence that makes every interaction respect your team's development culture and workflow preferences.

## Integration with Other Consultations

### Technical Consultation Integration
- Workflow preferences inform technology stack recommendations
- Process requirements shape architectural decision suggestions
- Quality standards influence code generation and refactoring advice
- Team structure affects complexity and maintainability recommendations

### Domain Consultation Integration
- Business process understanding informs development workflow alignment
- User experience requirements shape quality and testing emphasis
- Compliance requirements influence process formality and documentation needs
- Business timeline constraints affect development cycle and release strategy recommendations

**Combined Understanding**: Creates Claude expertise that considers technical capabilities, business requirements, AND team workflow preferences for truly contextual assistance.