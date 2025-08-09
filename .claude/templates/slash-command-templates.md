# Slash Command Templates & Best Practices
*Research-based templates from 119+ production commands and Anthropic best practices*

## 🎯 Command Categories & Templates

### 1. Discovery Commands

#### Deep Discovery Command
```markdown
---
name: deep-discovery
description: Comprehensive 30-60 minute project consultation
usage: "/deep-discovery [--type web|api|cli|library]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, WebSearch, Task]
category: discovery
model: opus
---

You are a Deep Discovery Specialist conducting a comprehensive project consultation.

## Consultation Process

### Phase 1: Technical Discovery (15 minutes)
1. **Scan Project Structure**
   - Use Glob to find all configuration files
   - Read package.json, requirements.txt, go.mod, etc.
   - Identify primary language and frameworks
   - Map directory structure and conventions

2. **Analyze Architecture**
   - Read main entry points
   - Identify architectural patterns
   - Detect testing frameworks
   - Understand build processes

3. **Pattern Recognition**
   - Search for common patterns with Grep
   - Identify naming conventions
   - Detect code style preferences
   - Find anti-patterns to avoid

### Phase 2: Domain Understanding (15 minutes)
1. **Business Logic Analysis**
   - Read domain models and entities
   - Understand business rules
   - Map data flows
   - Identify core workflows

2. **Interactive Consultation**
   Ask the user:
   - What is the primary purpose of this project?
   - What are the main pain points you face?
   - What patterns work well in your codebase?
   - What should I never change or break?

### Phase 3: Context Generation (15 minutes)
1. **Generate PROJECT-DNA.md**
   Create a comprehensive project DNA document including:
   - Technical architecture summary
   - Domain knowledge capture
   - Team conventions and patterns
   - Critical rules and anti-patterns

2. **Create Custom Commands**
   Generate 5+ project-specific commands:
   - /[project]-deploy
   - /[project]-test
   - /[project]-refactor
   - /[project]-security-check
   - /[project]-performance-audit

3. **Build Context Hierarchy**
   Create context files:
   - 00-essential.md (< 100 lines)
   - 01-architecture.md
   - 02-domain.md
   - 03-patterns.md

### Phase 4: Validation (15 minutes)
1. **Test Generated Commands**
   - Validate each command works
   - Ensure no breaking changes
   - Verify output quality

2. **Get User Approval**
   - Present findings for review
   - Incorporate feedback
   - Finalize configurations

## Success Criteria
- [ ] Completes within 30-60 minutes
- [ ] Generates comprehensive PROJECT-DNA.md
- [ ] Creates 5+ working custom commands
- [ ] Produces hierarchical context files
- [ ] Receives user approval

## Arguments
$ARGUMENTS - Optional project type specification
```

#### Project Analysis Command
```markdown
---
name: analyze-project
description: Quick project analysis and report generation
usage: "/analyze-project [--depth shallow|deep]"
allowed-tools: [Read, Glob, Grep, LS]
category: discovery
model: sonnet
---

Perform a rapid project analysis to understand structure and patterns.

## Analysis Steps

1. **Project Identification**
   \`\`\`bash
   # Detect project type
   - Check for package.json → Node.js/JavaScript
   - Check for requirements.txt → Python
   - Check for go.mod → Go
   - Check for Cargo.toml → Rust
   \`\`\`

2. **Structure Analysis**
   - Map directory tree (max depth: 3)
   - Count files by type
   - Identify main modules
   - Detect test locations

3. **Pattern Detection**
   - Common file naming patterns
   - Code organization style
   - Import/dependency patterns
   - Configuration approach

4. **Generate Report**
   Create analysis report with:
   - Project type and stack
   - Architecture overview
   - Key statistics
   - Recommendations

## Output Format
\`\`\`markdown
# Project Analysis Report

## Overview
- **Type**: [detected type]
- **Language**: [primary language]
- **Framework**: [main framework]
- **Size**: [LOC and file count]

## Structure
[Directory tree visualization]

## Patterns Detected
[List of patterns found]

## Recommendations
[Suggested improvements]
\`\`\`

Arguments: $ARGUMENTS
```

### 2. Development Commands

#### TDD Command
```markdown
---
name: tdd
description: Test-driven development workflow enforcement
usage: "/tdd [feature-name]"
allowed-tools: [Read, Write, Edit, Bash]
category: development
model: opus
---

You are a TDD Specialist. Follow the RED-GREEN-REFACTOR cycle strictly.

## TDD Workflow

### Step 1: RED Phase (Write Failing Test)
1. **Understand Requirement**
   - What should the feature do?
   - What are edge cases?
   - What should it NOT do?

2. **Write Test First**
   \`\`\`typescript
   describe('[Feature]', () => {
     it('should [expected behavior]', () => {
       // Arrange
       const input = setupTestData();
       
       // Act
       const result = featureUnderTest(input);
       
       // Assert
       expect(result).toBe(expected);
     });
   });
   \`\`\`

3. **Verify Test Fails**
   - Run test and confirm failure
   - Failure proves test is valid

### Step 2: GREEN Phase (Make Test Pass)
1. **Write Minimal Code**
   - Just enough to pass test
   - No extra features
   - No premature optimization

2. **Run Test**
   - Confirm test passes
   - All existing tests still pass

### Step 3: REFACTOR Phase
1. **Improve Code Quality**
   - Remove duplication
   - Improve naming
   - Simplify logic

2. **Maintain Green**
   - Run tests after each change
   - Keep all tests passing

## Enforcement Rules
- ❌ NEVER write code without test
- ❌ NEVER write more than minimal code
- ✅ ALWAYS see red before green
- ✅ ALWAYS refactor when green

## Arguments
$ARGUMENTS - Feature name to implement

## Success Metrics
- [ ] Test written first
- [ ] Test failed initially
- [ ] Test passes with minimal code
- [ ] Code refactored while green
- [ ] All tests still passing
```

#### Feature Implementation Command
```markdown
---
name: implement-feature
description: Structured feature implementation workflow
usage: "/implement-feature [feature-spec]"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Task]
category: development
model: opus
---

Implement a feature following best practices and project patterns.

## Implementation Workflow

### Phase 1: Understanding
1. **Read Specification**
   - Parse feature requirements
   - Identify acceptance criteria
   - Note edge cases

2. **Analyze Impact**
   - What files need changes?
   - What might break?
   - What tests needed?

### Phase 2: Planning
1. **Break Down Tasks**
   - Create atomic sub-tasks
   - Order by dependencies
   - Estimate complexity

2. **Use TodoWrite**
   \`\`\`typescript
   const tasks = [
     "Create data model",
     "Add API endpoint",
     "Implement business logic",
     "Add validation",
     "Write tests",
     "Update documentation"
   ];
   \`\`\`

### Phase 3: Implementation
1. **Follow Project Patterns**
   - Read existing similar code
   - Match style and structure
   - Use established patterns

2. **Incremental Development**
   - Implement one piece
   - Test it works
   - Commit atomically
   - Move to next piece

### Phase 4: Validation
1. **Testing**
   - Unit tests for logic
   - Integration tests for API
   - E2E tests for workflow

2. **Code Review Prep**
   - Self-review changes
   - Check style guide
   - Verify no breaks

## Success Criteria
- [ ] All requirements met
- [ ] Tests passing
- [ ] Documentation updated
- [ ] No regressions
- [ ] Follows patterns

Arguments: $ARGUMENTS
```

### 3. Quality Commands

#### Security Review Command
```markdown
---
name: security-review
description: Automated security vulnerability scanning
usage: "/security-review [--severity all|high|critical]"
allowed-tools: [Read, Grep, WebSearch]
category: security
model: opus
---

Conduct comprehensive security review of codebase.

## Security Checks

### 1. Vulnerability Scanning
- **SQL Injection**
  \`\`\`regex
  Pattern: (SELECT|INSERT|UPDATE|DELETE).*\\$\\{.*\\}
  Risk: Direct string interpolation in queries
  \`\`\`

- **XSS Vulnerabilities**
  \`\`\`regex
  Pattern: innerHTML\\s*=|dangerouslySetInnerHTML
  Risk: Unescaped user input in HTML
  \`\`\`

- **Command Injection**
  \`\`\`regex
  Pattern: exec\\(|system\\(|eval\\(
  Risk: Dynamic command execution
  \`\`\`

### 2. Authentication Issues
- Weak password requirements
- Missing rate limiting
- Session management flaws
- Token exposure

### 3. Data Protection
- Sensitive data in logs
- Unencrypted storage
- API key exposure
- PII handling

### 4. Dependency Audit
\`\`\`bash
# Check for known vulnerabilities
npm audit
pip check
go mod audit
\`\`\`

## Report Format
\`\`\`markdown
# Security Review Report

## Critical Issues (Immediate Action Required)
- [Issue]: [Location] - [Fix]

## High Priority Issues
- [Issue]: [Location] - [Fix]

## Medium Priority Issues
- [Issue]: [Location] - [Fix]

## Recommendations
- [Security best practice]
\`\`\`

Arguments: $ARGUMENTS
```

#### Performance Audit Command
```markdown
---
name: performance-audit
description: Analyze and optimize performance bottlenecks
usage: "/performance-audit [--focus frontend|backend|database]"
allowed-tools: [Read, Grep, Write]
category: quality
model: sonnet
---

Identify and address performance bottlenecks.

## Audit Areas

### 1. Code Analysis
- **N+1 Queries**
  - Detect ORM lazy loading
  - Find missing eager loads
  - Suggest batch queries

- **Inefficient Algorithms**
  - O(n²) or worse complexity
  - Unnecessary loops
  - Redundant calculations

- **Memory Leaks**
  - Unclosed resources
  - Circular references
  - Large object retention

### 2. Frontend Performance
- Bundle size analysis
- Lazy loading opportunities
- Image optimization needs
- Render performance

### 3. Backend Performance
- Slow endpoints
- Database query optimization
- Caching opportunities
- Async processing needs

### 4. Optimization Suggestions
\`\`\`typescript
// Before: O(n²)
const result = items.filter(item => 
  otherItems.some(other => other.id === item.id)
);

// After: O(n)
const otherIds = new Set(otherItems.map(o => o.id));
const result = items.filter(item => otherIds.has(item.id));
\`\`\`

## Output
- Performance hotspots identified
- Specific optimization recommendations
- Implementation priority order
- Expected improvement metrics

Arguments: $ARGUMENTS
```

### 4. Workflow Commands

#### Release Command
```markdown
---
name: release
description: Automated release preparation and changelog generation
usage: "/release [version] [--type major|minor|patch]"
allowed-tools: [Read, Write, Edit, Bash]
category: workflow
model: sonnet
---

Prepare a new release with changelog generation and version updates.

## Release Workflow

### 1. Version Determination
\`\`\`bash
# Analyze commits since last release
git log --oneline [last-tag]..HEAD

# Determine version bump
- Breaking changes → Major
- New features → Minor  
- Bug fixes → Patch
\`\`\`

### 2. Changelog Generation
\`\`\`markdown
# Changelog

## [Version] - [Date]

### ✨ Features
- [Feature from commit]

### 🐛 Bug Fixes
- [Fix from commit]

### 💥 Breaking Changes
- [Breaking change]

### 📚 Documentation
- [Doc updates]
\`\`\`

### 3. Version Updates
- Update package.json
- Update version constants
- Update README badges
- Update documentation

### 4. Pre-release Checks
- [ ] All tests passing
- [ ] No lint errors
- [ ] Documentation current
- [ ] Breaking changes documented
- [ ] Migration guide if needed

### 5. Release Commit
\`\`\`bash
git add -A
git commit -m "chore(release): v[version]"
git tag v[version]
\`\`\`

Arguments: $ARGUMENTS
```

### 5. Specialized Commands

#### Multi-Agent Orchestration Command
```markdown
---
name: multi-agent-analysis
description: Orchestrate multiple specialized agents for comprehensive analysis
usage: "/multi-agent-analysis [task]"
allowed-tools: [Task]
category: advanced
model: opus
---

Orchestrate multiple specialized agents to analyze different aspects in parallel.

## Orchestration Strategy

### 1. Task Decomposition
Analyze the task and identify specialized sub-tasks:
- Technical architecture analysis
- Security vulnerability assessment
- Performance bottleneck detection
- Code quality evaluation
- Documentation completeness check

### 2. Agent Deployment
\`\`\`yaml
agents:
  - name: architecture-analyst
    task: "Analyze system architecture and identify patterns"
    model: sonnet
    
  - name: security-auditor
    task: "Scan for security vulnerabilities"
    model: sonnet
    
  - name: performance-optimizer
    task: "Identify performance bottlenecks"
    model: sonnet
    
  - name: quality-guardian
    task: "Assess code quality and test coverage"
    model: sonnet
\`\`\`

### 3. Parallel Execution
Deploy all agents simultaneously:
- Each agent works in isolated context
- No interference between agents
- Maximum parallelization

### 4. Result Synthesis
Combine findings from all agents:
- Identify common themes
- Resolve conflicts
- Prioritize recommendations
- Generate unified report

## Output Format
\`\`\`markdown
# Multi-Agent Analysis Report

## Executive Summary
[Synthesized key findings]

## Architecture Analysis
[Agent 1 findings]

## Security Assessment
[Agent 2 findings]

## Performance Analysis
[Agent 3 findings]

## Quality Metrics
[Agent 4 findings]

## Prioritized Recommendations
1. [Critical action]
2. [High priority action]
3. [Medium priority action]
\`\`\`

Arguments: $ARGUMENTS
```

## 📋 Command Best Practices

### 1. Command Structure

#### Optimal YAML Frontmatter
```yaml
---
name: command-name           # Kebab-case, descriptive
description: Brief purpose   # One-line explanation
usage: "/command [args]"     # Clear usage example
allowed-tools: [...]         # Minimal required tools
category: core|dev|quality   # Logical grouping
model: haiku|sonnet|opus    # Appropriate model selection
---
```

### 2. Tool Selection Guidelines

```yaml
Discovery Commands:
  - Read, Glob, Grep, LS     # File exploration
  - WebSearch                 # External research

Development Commands:
  - Read, Write, Edit         # Code modification
  - MultiEdit                 # Batch changes
  - Bash                      # Build/test execution

Quality Commands:
  - Read, Grep               # Code analysis
  - WebSearch                # Vulnerability databases

Workflow Commands:
  - Read, Write, Bash        # Automation
  - Task                     # Sub-agent orchestration
```

### 3. Performance Optimization

#### Token-Efficient Commands
- Keep system prompts under 500 tokens
- Use references instead of inline content
- Lazy-load context with @references
- Clear between unrelated operations

#### Batch Operations
```markdown
## Good: Parallel Operations
Execute these in parallel:
- Read(file1), Read(file2), Grep(pattern)

## Bad: Sequential Operations
Read file1
Then read file2
Then search for pattern
```

### 4. Error Handling

```markdown
## Robust Error Handling

1. **Validate Inputs**
   - Check arguments exist
   - Verify file paths valid
   - Ensure permissions adequate

2. **Graceful Failures**
   - Provide clear error messages
   - Suggest corrective actions
   - Maintain partial progress

3. **Recovery Options**
   - Offer rollback if possible
   - Save work before risky operations
   - Provide manual recovery steps
```

### 5. User Interaction

```markdown
## Interactive Patterns

### Confirmation Requests
"This will modify [N] files. Proceed? (y/n)"

### Progress Updates
"Phase 1/4: Analyzing project structure..."
"Phase 2/4: Detecting patterns... (23 files scanned)"

### Clear Output
- Use markdown formatting
- Include code blocks
- Provide summaries
- Highlight important findings
```

## 🚀 Advanced Patterns

### Chain of Thought Commands
```markdown
## Enable Deep Thinking
Include "think step by step" or "ultrathink" in critical decision points.

<thinking>
Let me analyze this problem:
1. First, I need to understand...
2. Then I should check...
3. Finally, I'll synthesize...
</thinking>
```

### Progressive Enhancement
```markdown
## Start Simple, Add Complexity
1. **Basic Version**: Core functionality
2. **Enhanced Version**: Add validation
3. **Advanced Version**: Add parallelization
4. **Expert Version**: Add AI optimization
```

### Command Composition
```markdown
## Combine Commands for Workflows
/analyze-project → /generate-tests → /implement-feature → /security-review
```

## 📊 Success Metrics

### Command Quality Checklist
- [ ] Completes in reasonable time (< 5 min for most)
- [ ] Produces actionable output
- [ ] Handles errors gracefully
- [ ] Follows project patterns
- [ ] Maintains context efficiency
- [ ] Provides clear feedback
- [ ] Documents changes made
- [ ] Enables rollback if needed

---
*Based on analysis of 119+ production commands and Anthropic best practices*