# Research → Plan → Implement - The Foundation Workflow

> **The Professional Pattern**: Master the Query → Feature → Task workflow that underlies all sophisticated development work.

This is the most important workflow pattern in professional development. It's the systematic approach that experienced developers use when facing complex requirements, unfamiliar codebases, or sophisticated features. Master this pattern and you'll handle any development challenge with confidence.

## 🎯 The Three-Phase Foundation

### Phase 1: Research (Query) - "Understand Before Acting"
**Time**: 5-10 minutes
**Goal**: Deep understanding of context, requirements, and constraints

### Phase 2: Plan (Feature) - "Design Before Building"  
**Time**: 5-15 minutes
**Goal**: Clear architecture and implementation strategy

### Phase 3: Implement (Task) - "Execute with Quality"
**Time**: 10-30 minutes
**Goal**: Production-ready implementation with tests and documentation

## 🚀 20-Minute Complete Workflow

### Prerequisites
- ✅ Completed quick-start examples
- ✅ Framework responding consistently
- ✅ Basic understanding of command types

### Step 1: Setup Research Environment (2 minutes)

```bash
# Copy workflow-optimized configuration
cp /path/to/claude-code-modular-prompts/examples/workflows/research-plan-implement/PROJECT_CONFIG.xml .

# Create a realistic scenario - let's say you need to add user authentication
mkdir -p src/auth tests/auth docs/auth
touch src/auth/.gitkeep tests/auth/.gitkeep docs/auth/.gitkeep
```

### Step 2: RESEARCH Phase - Deep Understanding (5 minutes)

```bash
# Phase 1: Understand the domain and requirements
/query "analyze this codebase for existing authentication patterns, security requirements, and integration points for a new user authentication system"

# Follow up with specific questions based on initial analysis
/query "what are the security best practices for authentication in this type of application, and what are the potential integration challenges?"

# Research existing patterns and standards
/query "review the current project structure and recommend the best approach for adding authentication that follows existing patterns"
```

**What happens in Research**:
- 🔍 **Codebase Analysis**: Framework understands your existing patterns
- 📚 **Domain Knowledge**: Applies best practices for your technology stack
- 🎯 **Requirement Clarification**: Identifies specific needs and constraints
- ⚠️ **Risk Assessment**: Highlights potential challenges and integration points

### Step 3: PLAN Phase - Design Strategy (8 minutes)

```bash
# Phase 2: Create comprehensive feature plan based on research
/feature "design and plan a user authentication system with JWT tokens, including login/logout, password reset, and session management, following the patterns identified in research"
```

**What happens in Planning**:
- 🏗️ **Architecture Design**: Framework creates detailed implementation plan
- 📋 **Component Breakdown**: Identifies all necessary files and modules
- 🔗 **Integration Strategy**: Plans how new code fits with existing systems
- 🧪 **Test Strategy**: Defines comprehensive testing approach
- 📚 **Documentation Plan**: Outlines necessary documentation and examples

### Step 4: IMPLEMENT Phase - Quality Execution (5 minutes)

```bash
# Phase 3: Execute the planned implementation
/task "implement the core authentication service following the planned architecture"
/task "add user login and logout endpoints with proper error handling"
/task "implement password reset functionality with email verification"
/task "add session management and JWT token handling"
```

**What happens in Implementation**:
- ✅ **TDD Execution**: Each task follows RED→GREEN→REFACTOR cycle
- 🔧 **Quality Gates**: Automatic enforcement of coverage and quality standards
- 📝 **Documentation**: Auto-generated docs and usage examples
- 🧪 **Integration Testing**: Validates that components work together
- 🚀 **Production Readiness**: Code ready for real-world deployment

### Step 5: Validation and Review (2 minutes)

```bash
# Validate the complete implementation
/query "review the complete authentication implementation, validate that it follows the original research recommendations, and identify any gaps or improvements"

# Test the implementation
npm test  # or appropriate test command
```

## ✅ Workflow Success Indicators

After completing this workflow, you should have:

- [ ] **Deep Understanding**: Clear grasp of domain, requirements, and constraints
- [ ] **Comprehensive Plan**: Detailed architecture and implementation strategy
- [ ] **Production Code**: Working implementation with tests and documentation
- [ ] **Quality Validation**: Code that meets professional standards
- [ ] **Integration Confidence**: New code fits seamlessly with existing system
- [ ] **Future Maintainability**: Code structure supports future modifications

## 🔍 Why This Pattern Works

### Research Phase Benefits
- **Prevents False Starts**: Understanding before acting saves significant time
- **Identifies Hidden Requirements**: Discovers constraints and dependencies early
- **Applies Best Practices**: Leverages domain knowledge and proven patterns
- **Reduces Risk**: Identifies potential challenges before implementation

### Planning Phase Benefits
- **Clear Direction**: Detailed roadmap prevents implementation confusion
- **Component Coordination**: Ensures all pieces fit together properly
- **Quality Integration**: Plans testing and documentation from the start
- **Team Communication**: Provides clear specification for implementation

### Implementation Phase Benefits
- **Focused Execution**: Clear tasks with specific, achievable goals
- **Quality Assurance**: TDD and quality gates built into every step
- **Incremental Progress**: Small, validated steps toward complete solution
- **Production Readiness**: Professional standards applied throughout

## 🚀 Practice Scenarios

### Web Development Scenarios
```bash
# E-commerce feature
/query "analyze requirements for adding product reviews and ratings"
/feature "plan a comprehensive product review system with moderation"
/task "implement review submission and display components"

# Performance optimization
/query "analyze current performance bottlenecks and optimization opportunities"
/feature "plan a comprehensive performance improvement strategy"
/task "implement specific optimizations with measurement"
```

### API Development Scenarios
```bash
# API versioning
/query "research best practices for API versioning in this codebase"
/feature "plan migration to versioned API endpoints"
/task "implement v2 endpoints with backward compatibility"

# Rate limiting
/query "analyze current API usage patterns and rate limiting needs"
/feature "plan comprehensive rate limiting and throttling system"
/task "implement rate limiting middleware with monitoring"
```

### Data Processing Scenarios
```bash
# Data pipeline
/query "analyze current data processing workflows and improvement opportunities"
/feature "plan optimized data processing pipeline with error handling"
/task "implement pipeline components with validation and monitoring"

# Analytics integration
/query "research analytics requirements and integration patterns"
/feature "plan analytics data collection and reporting system"
/task "implement analytics tracking with privacy compliance"
```

## 🔧 Pattern Customization

### For Different Project Phases

**Greenfield Projects** (New Development):
```xml
<domain_specific_rules>
  <rule>Research emerging best practices and modern patterns</rule>
  <rule>Plan for scalability and future requirements</rule>
  <rule>Implement with comprehensive testing and documentation</rule>
</domain_specific_rules>
```

**Legacy Integration** (Existing Systems):
```xml
<domain_specific_rules>
  <rule>Research existing patterns and constraints thoroughly</rule>
  <rule>Plan minimal disruption integration strategies</rule>
  <rule>Implement with backward compatibility and migration paths</rule>
</domain_specific_rules>
```

**Rapid Prototyping** (Quick Validation):
```xml
<domain_specific_rules>
  <rule>Research minimum viable feature requirements</rule>
  <rule>Plan for quick iteration and validation</rule>
  <rule>Implement with focus on functionality over perfection</rule>
</domain_specific_rules>
```

### For Different Team Sizes

**Solo Development**:
```bash
# Research with personal context
/query "analyze this from my perspective as solo developer with these constraints"

# Plan with individual capacity
/feature "plan implementation considering my available time and skills"
```

**Team Development**:
```bash
# Research with team context
/query "analyze this considering team skills, existing patterns, and collaboration needs"

# Plan with team coordination
/feature "plan implementation with clear team roles and integration points"
```

## 🚨 Common Pattern Challenges

### Research Phase Too Shallow?
```bash
# Dig deeper with specific questions
/query "what specific security vulnerabilities should I consider for this feature?"
/query "what are the performance implications of this approach?"
/query "how does this integrate with existing team workflows?"
```

### Planning Phase Too Vague?
```bash
# Ask for more specific details
/feature "break down the previous plan into specific, actionable components with clear interfaces"
```

### Implementation Getting Stuck?
```bash
# Break down further or get help
/query "analyze why this implementation is challenging and suggest alternative approaches"
/task "implement just the core functionality first, then extend"
```

### Quality Gates Blocking?
```bash
# Adjust or understand requirements
/query "explain why quality gates are failing and suggest specific improvements"
```

## 💡 Advanced Pattern Techniques

### Research Depth Scaling
```bash
# Light research for familiar domains
/query "quick analysis of requirements and implementation approach"

# Deep research for unfamiliar domains
/query "comprehensive domain analysis including security, performance, and maintainability considerations"
/query "research industry best practices and common pitfalls for this type of feature"
/query "analyze integration requirements and potential architectural impacts"
```

### Planning Sophistication
```bash
# Simple planning for straightforward features
/feature "plan basic implementation following existing patterns"

# Complex planning for architectural features
/feature "plan comprehensive solution including architecture, migration strategy, testing approach, and rollout plan"
```

### Implementation Coordination
```bash
# Sequential implementation for simple features
/task "implement component A" && /task "implement component B"

# Parallel implementation for complex features  
/swarm "coordinate parallel implementation of multiple components"
```

## 🎯 Mastery Development

### Beginner Mastery
- **Pattern Recognition**: Automatically think Research → Plan → Implement
- **Phase Discipline**: Complete each phase before moving to next
- **Quality Integration**: TDD and quality gates feel natural
- **Context Preservation**: Maintain understanding across phases

### Intermediate Mastery
- **Depth Scaling**: Adjust research depth based on complexity and familiarity
- **Planning Sophistication**: Create comprehensive plans for complex features
- **Implementation Coordination**: Manage multi-task implementation effectively
- **Pattern Adaptation**: Customize pattern for different domains and constraints

### Advanced Mastery
- **Pattern Innovation**: Create variations for unique challenges
- **Team Leadership**: Guide others in pattern application
- **Quality Mentoring**: Help others understand when and how to apply pattern
- **Framework Evolution**: Contribute improvements to pattern effectiveness

## 📚 Related Patterns and Concepts

- **Multi-Agent Development**: [examples/workflows/multi-agent-development/](../multi-agent-development/)
- **Long-Running Sessions**: [examples/workflows/long-running-session/](../long-running-session/)
- **Command Chaining**: [examples/advanced/command-chaining/](../../advanced/command-chaining/)
- **Quality Gates**: [docs/quality/universal-quality-gates.md](../../../.claude/system/quality/universal-quality-gates.md)

---

**Pattern Mastery Achieved**: You now understand the foundation of professional development workflow! 🎉

**Ready for parallel coordination?** Explore [multi-agent-development/](../multi-agent-development/) to master sophisticated multi-agent workflows.

**Want extended session management?** Try [long-running-session/](../long-running-session/) for complex, multi-day development projects.