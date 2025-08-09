# Deep Discovery Analysis Framework
## Systematic Approach for Repository Pattern Extraction

### Purpose
This framework defines the systematic, evidence-based approach for analyzing Claude Code repositories to extract valuable patterns for our 30-60 minute deep discovery consultation system. Unlike the failed "quick scan and guess" approach, this methodology ensures every pattern is validated, documented, and traceable.

---

## Phase 1: Repository Preparation

### 1.1 Initial Assessment
Before deep analysis, perform quick viability check:

```yaml
Viability Criteria:
  - Repository actively maintained (commits within 3 months)
  - Minimum 100 stars or significant community engagement
  - Clear Claude Code integration (presence of .claude/ directory)
  - Documentation exists (README, CLAUDE.md, or similar)
  - Actual working code (not just concepts or templates)
```

### 1.2 Repository Clone and Setup
```bash
# Clone for local analysis
git clone [repository-url] ./analysis/[repo-name]

# Document initial observations
- Total file count
- Primary language/framework
- Team size indicators
- Complexity assessment
```

### 1.3 Create Analysis Workspace
```
analysis/[repo-name]/
├── extracted-patterns/
├── evidence/
├── validation/
└── analysis-notes.md
```

---

## Phase 2: Systematic Pattern Extraction

### 2.1 Command Pattern Analysis

**What to Look For:**
```yaml
Command Patterns:
  Structure:
    - YAML frontmatter format
    - Parameter handling approaches
    - Tool usage patterns
    - Error handling strategies
    
  Categories:
    - Generation commands (create files/code)
    - Analysis commands (examine existing code)
    - Workflow commands (multi-step processes)
    - Utility commands (helpers and tools)
    
  Innovation Indicators:
    - Novel parameter approaches
    - Unique tool combinations
    - Creative problem solutions
    - Efficiency optimizations
```

**Extraction Process:**
1. Scan `.claude/commands/` directory
2. Categorize each command by purpose
3. Extract YAML structure patterns
4. Document unique approaches
5. Note effectiveness indicators

**Evidence Collection:**
- Screenshot command structure
- Copy relevant code snippets
- Document file paths and line numbers
- Record usage examples if available

### 2.2 Agent Pattern Analysis

**What to Look For:**
```yaml
Agent Patterns:
  Architecture:
    - Agent definition structure
    - Capability boundaries
    - Communication protocols
    - Orchestration patterns
    
  Specializations:
    - Domain expertise areas
    - Task decomposition approaches
    - Validation methodologies
    - Performance optimizations
    
  Coordination:
    - Multi-agent workflows
    - Handoff mechanisms
    - State management
    - Conflict resolution
```

**Extraction Process:**
1. Identify agent definitions (usually in `.claude/agents/`)
2. Map agent relationships and dependencies
3. Document coordination patterns
4. Extract specialization strategies
5. Note effectiveness metrics

### 2.3 Context Engineering Analysis

**What to Look For:**
```yaml
Context Patterns:
  CLAUDE.md Structure:
    - Section organization
    - Metadata usage
    - Cross-referencing approaches
    - Update strategies
    
  Multi-file Context:
    - File hierarchy patterns
    - Navigation systems
    - Inheritance models
    - Token optimization
    
  Effectiveness:
    - Context depth indicators
    - Response quality improvements
    - Token efficiency metrics
    - Maintenance patterns
```

**Extraction Process:**
1. Analyze CLAUDE.md structure and content
2. Map context file relationships
3. Document navigation patterns
4. Measure context effectiveness
5. Note maintenance approaches

### 2.4 Workflow Pattern Analysis

**What to Look For:**
```yaml
Workflow Patterns:
  Development Workflows:
    - Setup procedures
    - Development cycles
    - Testing integration
    - Deployment processes
    
  Team Workflows:
    - Collaboration patterns
    - Review processes
    - Knowledge sharing
    - Standard enforcement
    
  Automation:
    - CI/CD integration
    - Hook usage
    - Trigger patterns
    - Quality gates
```

---

## Phase 3: Evidence Validation

### 3.1 CRAAP Test Application

For each extracted pattern, apply the CRAAP test:

**Currency (0-1 score):**
- When was the pattern last updated?
- Is it compatible with current Claude Code version?
- Are dependencies up to date?

**Relevance (0-1 score):**
- Does it apply to our use cases?
- Is it appropriate for our target users?
- Does it align with 30-60 minute consultation goals?

**Authority (0-1 score):**
- Is the source repository credible?
- Does it have community validation?
- Are the authors recognized experts?

**Accuracy (0-1 score):**
- Is the pattern technically correct?
- Are there working examples?
- Has it been tested/validated?

**Purpose (0-1 score):**
- Does it serve our deep discovery goals?
- Is the intent clear and beneficial?
- Does it prioritize depth over speed?

### 3.2 Cross-Reference Validation

**Minimum 3-Source Rule:**
- Pattern must appear in at least 3 repositories
- OR have strong evidence of effectiveness
- OR solve a unique problem exceptionally well

**Correlation Analysis:**
- Which patterns commonly appear together?
- What patterns conflict with each other?
- How do patterns build upon each other?

---

## Phase 4: Pattern Documentation

### 4.1 Pattern Record Creation

For each validated pattern, create a comprehensive record:

```yaml
Pattern Record:
  identification:
    id: pattern-[category]-[timestamp]
    name: descriptive-pattern-name
    category: [commands|agents|context|workflows]
    
  description:
    summary: Brief description
    problem_solved: What issue it addresses
    implementation: How it works
    
  evidence:
    sources:
      - repository: name
        file: path
        lines: [start-end]
    validation:
      craap_score: 0.0-1.0
      confidence: high|medium|low
      
  effectiveness:
    adoption_rate: percentage
    success_indicators: metrics
    user_feedback: summary
    
  applicability:
    domains: [web, data-science, etc]
    complexity: simple|moderate|complex
    prerequisites: requirements
```

### 4.2 Quality Metrics

**Pattern Quality Indicators:**
- Clear documentation exists
- Multiple successful implementations
- Positive user feedback
- Measurable improvements
- Maintained and updated

**Red Flags to Note:**
- Overly complex solutions
- High maintenance burden
- Limited applicability
- Performance issues
- User frustration indicators

---

## Phase 5: Synthesis and Integration

### 5.1 Pattern Synthesis

After analyzing multiple repositories:

1. **Identify Common Patterns**
   - What approaches appear repeatedly?
   - Which patterns are domain-agnostic?
   - What are the core success patterns?

2. **Discover Unique Solutions**
   - What innovative approaches exist?
   - Which patterns solve unique problems?
   - What can we learn from outliers?

3. **Build Pattern Relationships**
   - How do patterns complement each other?
   - What combinations work well?
   - Which patterns conflict?

### 5.2 Integration Planning

**For Our 30-60 Minute Consultation:**
- Which patterns support deep analysis?
- What enables quality over speed?
- Which patterns encourage thoroughness?
- What supports evidence-based decisions?

---

## Quality Criteria

### Minimum Standards
Every pattern must meet these criteria:

1. **Evidence-Based**: Minimum 3 sources or exceptional validation
2. **Documented**: Clear explanation of how and why
3. **Tested**: Working examples exist
4. **Relevant**: Applies to deep discovery goals
5. **Quality-Focused**: Prioritizes depth over speed

### Preferred Standards
High-value patterns also have:

1. **Wide Adoption**: Used across multiple domains
2. **Innovation**: Novel approach to problems
3. **Efficiency**: Optimal resource usage
4. **Maintainable**: Clear update and evolution path
5. **Community Validated**: Positive user feedback

---

## Analysis Tools and Commands

### Useful Commands for Analysis

```bash
# Find all Claude commands
find . -path "*/.claude/commands/*.md" -type f

# Search for specific patterns
grep -r "allowed-tools:" .claude/

# Analyze file structure
tree .claude/ -L 3

# Check command categories
grep -h "^category:" .claude/commands/*.md | sort | uniq -c

# Find agent definitions
find . -path "*/.claude/agents/*.md" -type f
```

### Documentation Templates

Use consistent templates for findings:

```markdown
## Pattern: [Name]
**Category**: [commands|agents|context|workflows]
**Repository**: [source]
**Confidence**: [high|medium|low]

### Description
[What the pattern does]

### Evidence
- Source 1: [repo/file:lines]
- Source 2: [repo/file:lines]
- Source 3: [repo/file:lines]

### Implementation
[Code snippet or description]

### Effectiveness
- Adoption: [percentage]
- Success Rate: [metrics]
- User Feedback: [summary]

### Notes
[Additional observations]
```

---

## Continuous Improvement

This framework should evolve based on:
- Patterns discovered during analysis
- Effectiveness of extraction methods
- New Claude Code capabilities
- User feedback on consultation system

Regular reviews should assess:
- Are we finding valuable patterns?
- Is the evidence threshold appropriate?
- Are validation methods effective?
- Is the analysis time justified?

Remember: **Quality over Quantity** - Better to deeply analyze 20 repositories than superficially scan 100.

---

*This framework ensures our 30-60 minute consultation is built on real evidence, not assumptions - the key differentiator from the failed speed-focused approach.*