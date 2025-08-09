---
name: /consult-technical
description: Deep technical architecture consultation focusing on frameworks, patterns, and development workflow
usage: "/consult-technical [quick|standard|comprehensive] [resume]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite]
category: consultation
version: "1.0"
---

# Technical Architecture Consultation: Deep Framework & Workflow Discovery

## Purpose
This command provides focused technical architecture consultation (7-10 minutes) that extracts comprehensive understanding of your project's frameworks, development patterns, testing strategies, and technical constraints. Designed as both a standalone consultation and Stage 2 of the full consultation flow.

## 🎯 What This Consultation Discovers

**Framework Intelligence:**
- Primary and secondary frameworks (React/Vue/Angular, Django/Flask/Rails, etc.)
- Framework-specific patterns and conventions in your codebase
- Configuration patterns and architectural decisions
- Framework integration patterns between frontend/backend/services

**Development Workflow:**
- Build processes, development environment setup
- Testing strategies (unit, integration, e2e) and tooling
- CI/CD pipelines, deployment patterns, and release processes
- Code quality standards, linting, and formatting conventions

**Technical Constraints & Requirements:**
- Performance requirements and optimization patterns
- Security considerations and implementation approaches
- Scalability patterns and infrastructure considerations
- Technical debt areas and modernization priorities

## 📋 Consultation Process

### Phase 1: Framework Analysis (2-3 minutes)
**Intelligent Framework Detection:**
- Analyze package.json, requirements.txt, and config files
- Identify primary frameworks and version patterns
- Discover framework-specific patterns in your codebase
- Validate findings through targeted questions

**Interactive Framework Exploration:**
- "I see you're using React 18 with TypeScript. Are you using any state management like Redux or Zustand?"
- "Your Django setup suggests API-first architecture. Are you building a decoupled frontend?"
- "I notice Next.js patterns. Are you using server-side rendering or static generation?"

### Phase 2: Development Workflow Discovery (3-4 minutes)
**Workflow Pattern Recognition:**
- Testing strategies and coverage approaches
- Build and deployment automation
- Development environment consistency
- Code review and quality assurance processes

**Adaptive Questioning Based on Detected Patterns:**
- For Node.js projects: "I see Jest in your dependencies. Are you using React Testing Library or Enzyme?"
- For Python projects: "pytest configuration detected. Do you use fixtures or factory patterns?"
- For CI/CD: "GitHub Actions workflows found. Are you deploying to cloud platforms or on-premises?"

### Phase 3: Technical Requirements & Constraints (2-3 minutes)
**Performance & Scale Understanding:**
- Expected traffic patterns and performance requirements
- Database patterns and data access optimization
- Caching strategies and content delivery approaches
- Infrastructure patterns and deployment constraints

**Context-Aware Deep Dives:**
- E-commerce: "What's your expected concurrent user load during peak shopping seasons?"
- Healthcare: "Are there HIPAA compliance requirements affecting your technical decisions?"
- Fintech: "What security standards are you implementing for financial data?"

## 🚀 Three Consultation Modes

### Quick Mode (5-7 minutes)
**Essential Technical Understanding:**
- Primary framework identification and key patterns
- Basic testing and deployment approach
- Critical performance or security requirements
- Major technical constraints or priorities

### Standard Mode (7-10 minutes) - Default
**Comprehensive Technical Profile:**
- Complete framework analysis with integration patterns
- Full development workflow understanding
- Performance, security, and scalability considerations
- Technical debt and modernization context

### Comprehensive Mode (10-15 minutes)
**Deep Technical Consultation:**
- Framework-specific best practice alignment
- Advanced architectural pattern discussion
- Performance optimization strategy exploration
- Long-term technical roadmap considerations

## 🔄 Session Management Integration

### Pause/Resume Support
- Save technical discovery progress with `/manage-session-state pause`
- Resume technical consultation with `/consult-technical resume`
- Session state preserved in `.claude/consultation-state.json`
- Full context restoration including framework analysis and user responses

### Integration with Full Consultation
- Can be run standalone or as part of `/begin-consultation`
- Technical findings feed into domain consultation and context generation
- Session continuity maintained across consultation phases
- Progress tracked within overall consultation workflow

### User Control Throughout Process
- **Navigation**: `skip`, `back`, `skip section` commands available
- **Pace Control**: Switch between quick/standard/comprehensive modes mid-session
- **Clarification**: `clarify`, `example`, `more detail` for deeper understanding
- **Validation**: `review`, `summary` to confirm technical understanding

## 💡 Interactive Dialogue Examples

### Framework Discovery Dialogue:
```
🔧 Technical Analysis: Framework Discovery

I've analyzed your project structure and found:
- React 18 with TypeScript (frontend)
- Express.js with Node.js (backend) 
- PostgreSQL (database)
- Docker containers (deployment)

Let me understand your specific patterns:

1. State Management: I notice Redux Toolkit in your dependencies. Are you using 
   RTK Query for API integration, or do you have a separate data fetching strategy?

2. Component Architecture: I see a components/ and pages/ structure. Are you 
   following any specific design system or component library patterns?

3. API Design: Your Express routes suggest REST patterns. Are you considering 
   GraphQL, or is REST working well for your use cases?

[User provides context-specific responses that build technical understanding]
```

### Development Workflow Exploration:
```
⚙️ Development Workflow Analysis

Based on your GitHub Actions and package.json scripts, I can see you have:
- Automated testing with Jest and React Testing Library
- ESLint/Prettier for code quality
- Docker-based deployment pipeline

Let's explore your specific workflow:

1. Testing Strategy: What's your approach to testing? Are you focusing on unit 
   tests, integration tests, or do you have end-to-end testing with Cypress/Playwright?

2. Code Review Process: How does your team handle code reviews? Any specific 
   quality gates or automated checks that are critical?

3. Deployment Frequency: Are you doing continuous deployment, or do you have 
   scheduled release cycles? Any rollback strategies?

[Dialogue adapts based on project scale and team size]
```

## 🎯 Technical Understanding Output

### Generated Technical Profile
After consultation completion, you'll have:

**Framework Context File** (`.claude/context/technical-architecture.md`):
- Complete framework inventory with version patterns
- Framework-specific patterns found in your codebase
- Integration patterns between different technology layers
- Framework best practices relevant to your implementation

**Development Workflow Context** (`.claude/context/development-workflow.md`):
- Testing strategies and tooling preferences  
- Build/deployment pipeline understanding
- Code quality standards and automation
- Team collaboration patterns and processes

**Technical Requirements Context** (`.claude/context/technical-requirements.md`):
- Performance requirements and constraints
- Security considerations and implementation patterns
- Scalability patterns and infrastructure understanding
- Technical debt areas and modernization priorities

### Enhanced CLAUDE.md Integration
Technical findings automatically enhance your project memory with:
- Framework-specific context for better code suggestions
- Development workflow awareness for process recommendations
- Technical constraint awareness for solution appropriateness
- Pattern recognition for consistent technical advice

## 🔧 Usage Examples

```bash
# Start focused technical consultation
/consult-technical

# Quick technical overview (5-7 minutes)
/consult-technical quick

# Comprehensive technical deep dive
/consult-technical comprehensive  

# Resume paused technical consultation
/consult-technical resume

# Use within full consultation flow
/begin-consultation stage-2  # Equivalent to /consult-technical standard
```

## 🤖 Specialized Agent Integration

This consultation leverages specialized technical analysis agents:

**Framework Detection Agent**: Analyzes dependencies and configuration files
**Pattern Recognition Agent**: Identifies code patterns and architectural decisions  
**Workflow Analysis Agent**: Maps development processes and tooling integration
**Technical Validation Agent**: Validates technical understanding and identifies gaps

Agents work together to build comprehensive technical understanding that goes far beyond surface-level framework detection.

## 🎯 Success Outcomes

After technical consultation, Claude will:
- **Speak your tech stack**: Use framework-specific terminology and concepts
- **Understand your patterns**: Recognize your architectural decisions and conventions
- **Respect your workflow**: Align suggestions with your development processes
- **Consider your constraints**: Factor in performance, security, and technical requirements

**Result**: Claude becomes a technical expert in YOUR specific technology choices and development patterns, not just generic programming advice.

## Next Steps

1. **Test technical understanding**: Ask Claude framework-specific questions
2. **Continue to domain consultation**: Run `/consult-domain` for business understanding
3. **Complete full consultation**: Use `/begin-consultation` for comprehensive setup
4. **Refine technical context**: Use `/update-context technical` for adjustments

**Time Investment**: 7-10 minutes for technical expertise that transforms every subsequent interaction with Claude.