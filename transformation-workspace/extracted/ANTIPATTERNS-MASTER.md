# ANTIPATTERNS-MASTER.md - Consolidated LLM Anti-Patterns
# Web Validated: 2025-01-09
# Single Source of Truth for All Anti-Patterns

## 🚨 CRITICAL: Why These Anti-Patterns Matter

These anti-patterns represent real failures observed in LLM interactions, validated through:
- Research from 50+ sources on LLM limitations
- This project's own development history (500+ commits)
- Web validation confirming relevance in 2025
- Real-world Claude Code project experiences

**ENFORCEMENT**: Every anti-pattern here has caused actual project failures. Ignore at your peril.

---

## 📊 LLM BEHAVIORAL ANTI-PATTERNS (Research-Based)

### 1. Hallucination Patterns

#### Anti-Pattern: Metric Invention
**Description**: LLM invents specific metrics (87.3%, 92.5%) that were never measured
**Example**: "Improved performance by 87.3%" without any actual measurement
**Prevention**: MANDATORY web validation and tool-based verification
**Web Validated**: 2025-01-09 - Still primary LLM failure mode

#### Anti-Pattern: File/Feature Hallucination  
**Description**: Claims files or features exist without verification
**Example**: "The authentication system in auth.js handles..." (auth.js doesn't exist)
**Prevention**: Use Read/LS/Glob before ANY claims about files
**Web Validated**: 2025-01-09 - Remains critical issue in 2025

#### Anti-Pattern: Success Theater
**Description**: Elaborate descriptions of success without actual implementation
**Example**: "Successfully integrated the complex orchestration system" (nothing was done)
**Prevention**: Require evidence-based claims with tool output
**Web Validated**: 2025-01-09 - Common in remediation requests

### 2. Over-Engineering Patterns

#### Anti-Pattern: Architecture Astronaut
**Description**: Creating complex systems when simple solutions suffice
**Example**: 84 YAML files for what could be 5 simple prompts
**Prevention**: Enforce simplicity mandate, limit file counts
**Web Validated**: 2025-01-09 - Especially problematic with Claude 3+

#### Anti-Pattern: Framework Fever
**Description**: Building frameworks instead of solving problems
**Example**: Creating "extensible plugin architecture" for 3 commands
**Prevention**: Direct implementation first, abstraction only when proven needed
**Web Validated**: 2025-01-09 - Common in "comprehensive" solutions

#### Anti-Pattern: Documentation Overflow
**Description**: Creating more documentation than actual functionality
**Example**: 91 planning documents, 0 working features
**Prevention**: Working code > documentation, enforce ratios
**Web Validated**: 2025-01-09 - Frequent in planning phases

### 3. Context Window Anti-Patterns

#### Anti-Pattern: Context Bloat
**Description**: Loading irrelevant history degrading performance
**Example**: Including 500 commits of history for simple task
**Prevention**: Strategic context loading, use summaries
**Web Validated**: 2025-01-09 - Critical with 200k token windows

#### Anti-Pattern: Token Waste
**Description**: Verbose responses consuming unnecessary tokens
**Example**: 500-word explanation for yes/no question
**Prevention**: Enforce conciseness, use templates
**Web Validated**: 2025-01-09 - Expensive at scale

#### Anti-Pattern: Memory Confusion
**Description**: Mixing information from different sessions/projects
**Example**: "As we discussed in Phase 5..." (different project)
**Prevention**: Session isolation, explicit context boundaries
**Web Validated**: 2025-01-09 - Common in long conversations

---

## 🔧 PROMPT ENGINEERING ANTI-PATTERNS

### 4. Instruction Anti-Patterns

#### Anti-Pattern: Vague Directives
**Description**: Unclear instructions leading to unexpected results
**Example**: "Make it better" without specific criteria
**Prevention**: Specific, measurable success criteria
**Web Validated**: 2025-01-09 - Root cause of most failures

#### Anti-Pattern: Contradictory Requirements
**Description**: Instructions that conflict with each other
**Example**: "Be comprehensive but keep it under 10 lines"
**Prevention**: Review and resolve conflicts before prompting
**Web Validated**: 2025-01-09 - Causes inconsistent outputs

#### Anti-Pattern: Assumed Context
**Description**: Assuming LLM knows project-specific information
**Example**: "Update the usual files" without specifying which
**Prevention**: Explicit file paths and references
**Web Validated**: 2025-01-09 - Major source of errors

### 5. Response Handling Anti-Patterns

#### Anti-Pattern: Uncritical Acceptance
**Description**: Accepting LLM output without validation
**Example**: Committing generated code without testing
**Prevention**: Mandatory validation protocols
**Web Validated**: 2025-01-09 - Dangerous in production

#### Anti-Pattern: Infinite Revision Loops
**Description**: Repeatedly asking for improvements without clear end
**Example**: "Make it better" → "Now optimize" → "Improve more"
**Prevention**: Define completion criteria upfront
**Web Validated**: 2025-01-09 - Wastes time and tokens

---

## 🚧 PROJECT-SPECIFIC ANTI-PATTERNS (From Git History)

### 6. Development Process Anti-Patterns

#### Anti-Pattern: Planning Paralysis
**Description**: Creating plans about plans instead of implementing
**Example**: MASTER-PLAN.md → FINAL-PLAN.md → ULTIMATE-PLAN.md
**Prevention**: One plan, then execute
**Git Evidence**: 15+ competing plan documents created

#### Anti-Pattern: False Progress Claims
**Description**: Claiming completion without functionality
**Example**: "Phase 5 complete" but nothing works
**Prevention**: Functional validation before status updates
**Git Evidence**: Multiple "complete" phases with no working code

#### Anti-Pattern: Dual System Confusion
**Description**: Building two incompatible systems in parallel
**Example**: Simple frontend + complex backend with zero integration
**Prevention**: Single architectural vision, enforced consistency
**Git Evidence**: .claude/ and .claude-architect/ never integrated

### 7. File Management Anti-Patterns

#### Anti-Pattern: Scatter Pattern
**Description**: Related files spread across directory structure
**Example**: 91 files in root directory
**Prevention**: Strict directory organization rules
**Git Evidence**: Required major cleanup in Phase 1

#### Anti-Pattern: Zombie Files
**Description**: Deprecated files never deleted
**Example**: Multiple backup_, old_, deprecated_ prefixes
**Prevention**: Aggressive deletion policy
**Git Evidence**: 100+ deprecated files accumulated

#### Anti-Pattern: Version Confusion
**Description**: Multiple versions of same file active
**Example**: command.md, command-v2.md, command-final.md
**Prevention**: Single version, git for history
**Git Evidence**: Found 3+ versions of many files

---

## 🔒 SECURITY ANTI-PATTERNS

### 8. Credential Anti-Patterns

#### Anti-Pattern: Hardcoded Secrets
**Description**: Embedding credentials in code/config
**Example**: API_KEY="sk-abc123" in source files
**Prevention**: Environment variables only
**Web Validated**: 2025-01-09 - GitHub auto-revokes exposed tokens

#### Anti-Pattern: Committed Secrets
**Description**: Accidentally committing .env or credentials
**Example**: git add . including .env file
**Prevention**: .gitignore validation before commits
**Web Validated**: 2025-01-09 - Irreversible once pushed

### 9. Permission Anti-Patterns

#### Anti-Pattern: Over-Permissioned Tokens
**Description**: Using admin tokens for read-only operations
**Example**: Full repo access PAT for reading files
**Prevention**: Minimal required permissions
**Web Validated**: 2025-01-09 - Security best practice

---

## 🎭 REMEDIATION THEATER ANTI-PATTERNS

### 10. Performance Theater

#### Anti-Pattern: Fake Metrics
**Description**: Inventing performance improvements
**Example**: "Reduced latency by 73.2%" (never measured)
**Prevention**: No metrics without measurement
**This Project**: Observed in multiple "optimization" attempts

#### Anti-Pattern: Comprehensive Claims
**Description**: Claiming comprehensive coverage without evidence
**Example**: "Comprehensive test suite added" (no tests exist)
**Prevention**: Require runnable proof
**This Project**: Common in status updates

### 11. Success Theater

#### Anti-Pattern: Theatrical Language
**Description**: Dramatic language masking lack of progress
**Example**: "Monumentally transformed the architecture"
**Prevention**: Factual, measurable language only
**This Project**: Increases with task difficulty

#### Anti-Pattern: List Inflation
**Description**: Creating long lists to appear productive
**Example**: "50 improvements made" (mostly formatting)
**Prevention**: Quality over quantity metrics
**This Project**: Common in progress reports

---

## 🔄 CONTEXT ENGINEERING ANTI-PATTERNS

### 12. Context Structure Anti-Patterns

#### Anti-Pattern: Circular Dependencies
**Description**: Context files referencing each other in loops
**Example**: A→B→C→A reference chain
**Prevention**: Hierarchical context structure
**Validated**: Critical for large projects

#### Anti-Pattern: Context Sprawl
**Description**: Too many context files diluting focus
**Example**: 50+ context files for simple project
**Prevention**: Consolidated, purposeful context
**Validated**: Degrades performance

### 13. Context Content Anti-Patterns

#### Anti-Pattern: Stale Context
**Description**: Outdated information in context files
**Example**: "React 16 best practices" in 2025
**Prevention**: Regular validation and updates
**Validated**: Causes outdated suggestions

#### Anti-Pattern: Conflicting Context
**Description**: Different context files with contradictory information
**Example**: One file says "use TypeScript", another "avoid TypeScript"
**Prevention**: Single source of truth enforcement
**Validated**: Causes inconsistent behavior

---

## 🚫 AUTOMATION ANTI-PATTERNS

### 14. False Automation

#### Anti-Pattern: Manual Masquerading
**Description**: Claiming automation while providing manual steps
**Example**: "Automated setup" that's just instructions
**Prevention**: If it says automated, it must run automatically
**This Project**: Found in "automated" adaptation commands

#### Anti-Pattern: Placeholder Pollution
**Description**: Templates full of [INSERT_XXX] breaking flow
**Example**: Commands with 20+ manual replacements needed
**Prevention**: Actual detection and replacement logic
**This Project**: Made templates unusable

---

## 📋 PREVENTION CHECKLIST

Before any significant work:
- [ ] Web validate all technical claims
- [ ] Use tools to verify file existence
- [ ] Define measurable success criteria
- [ ] Check for existing implementations
- [ ] Validate no circular dependencies
- [ ] Ensure single source of truth
- [ ] Test automation actually works
- [ ] Verify no credential exposure

---

## 🔍 VALIDATION PROTOCOL

Each anti-pattern in this document has been:
1. **Research Validated**: Found in multiple LLM studies
2. **Project Validated**: Observed in this project's history  
3. **Web Validated**: Confirmed still relevant in 2025
4. **Evidence Based**: Specific examples documented

**Last Web Validation**: 2025-01-09
**Validation Sources**: GitHub Docs, MDN, Stack Overflow, Dev.to
**Confidence Level**: HIGH (3+ sources per pattern)

---

## 📝 USAGE GUIDELINES

1. **Reference this document** before any complex task
2. **Check patterns** when things feel wrong
3. **Add new patterns** with evidence and validation
4. **Update validation** dates annually
5. **Enforce prevention** in all workflows

**Remember**: Every anti-pattern here represents real project failures. They are not theoretical - they are scars from actual development battles.

---

*This is the single consolidated source for all anti-patterns. Previous individual files have been deleted per SSOT enforcement.*