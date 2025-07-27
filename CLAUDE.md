# Claude Code Modular Prompts

**⚠️ PRE-PRODUCTION** Claude Code native prompt engineering library with 79 slash commands. Currently undergoing validation for production readiness.

**🚨 CRITICAL: NOT READY FOR PRODUCTION USE** - See `ULTRATHINK-PROMPT-ENGINEERING-ASSESSMENT.md` and `MVP-ACTION-PLAN.md`

## 🎯 CRITICAL UNDERSTANDING: This is a PROMPT ENGINEERING Project

**THIS IS NOT A SOFTWARE DEVELOPMENT PROJECT!** This is a collection of:
- **Slash Commands**: Prompt templates that work within Claude Code conversations (e.g., `/task`, `/help`)
- **Components**: Reusable prompt fragments that get composed together
- **Context Files**: Prompt engineering patterns and best practices
- **NOT executable code** - These are prompts that guide Claude's responses

**Testing** means:
- ✅ Testing prompt effectiveness in Claude conversations
- ✅ Validating token efficiency and context management
- ✅ Checking prompt composition and chaining
- ❌ NOT testing code execution or software functionality

**Security** means:
- ✅ Prompt injection prevention
- ✅ Context boundary protection
- ✅ Safe prompt patterns
- ❌ NOT system security or code vulnerabilities

## Current Structure
```
/
├── .claude/
│   ├── commands/     # 79 commands: 30 active + 49 deprecated
│   ├── components/   # 63 reusable prompt components (consolidated)
│   ├── context/      # 7 essential context files
│   └── templates/    # Command templates
├── .main.archive/    # ARCHIVED - Original tallinn content (332 files)
└── tests/            # Testing framework implemented (structural validation)
```

## Immutable Rules
1. Maximum 3 directory levels
2. No new files in .main.archive (archived content)
3. Tests before implementation (experimental validation focus)
4. No duplicate commands (each must be unique)
5. One atomic commit per task
6. **PARANOIA MANDATE**: Triple-check everything before commits
   - Verify no sensitive data (keys, tokens, passwords)
   - Check all file paths are correct
   - Validate directory structure integrity
   - Ensure .claude is never in .gitignore
   - Scan for accidental duplicates or leftovers

## Status
| Metric | Current | Target | Progress |
|--------|---------|--------|----------|
| MD files | 148 active | <150 | ✅ Within acceptable range |
| Commands | 79 total (30 active) | 79 unique | ✅ No duplicates found |
| Components | 65 (+2 security) | ~50-70 | ✅ Enhanced with security frameworks |
| Context files | 13 | 6-8 | ⚠️ Expanded with performance contexts |
| Structural validation | 100% pass rate | 100% | ✅ All 85 commands passing |
| Functional validation | 70.6% tested | 100% | ⚠️ 60/85 commands validated |
| Real Claude Code testing | 0% | 100% | ❌ Never tested in actual environment |
| Security implementation | Framework only | Verified | ❌ Untested in production |
| Validation templates | 5 comprehensive | Complete | ✅ Templates implemented |
| Max dir depth | 3 | 3 | ✅ Achieved |

## Validation Status and Production Readiness

### Current Validation State
This project has comprehensive **validation infrastructure** but requires systematic **validation execution**:

- ✅ **Validation Templates**: 5 comprehensive templates for systematic validation
- ✅ **Research Foundation**: 15 verified Claude Code sources and best practices  
- ✅ **Architecture**: Sophisticated command and component structure
- ❌ **Functional Testing**: 0 commands functionally tested in Claude Code
- ❌ **Production Readiness**: Requires 10-week validation implementation plan

### Production Readiness Plan
See `MVP-ACTION-PLAN.md` for 8-10 week production readiness roadmap:
- **Week 1-2**: Emergency fixes - Documentation, real Claude Code testing, security verification
- **Week 3-4**: Core infrastructure - Installation, monitoring, performance optimization  
- **Week 5-6**: User experience - Onboarding flow, community building
- **Week 7-8**: Production launch - Governance, beta program with 5-10 teams

**MVP Focus**: Top 10 commands (help, auto, task, dev, query, test, validate-command, pipeline, secure-assess, quality)

### Honest Assessment
- **Architecture Quality**: Excellent - Sophisticated, well-researched design
- **Functional Reality**: Unknown - Commands never executed in Claude Code environment
- **Documentation Accuracy**: Mixed - Some claims exceed validated reality
- **Production Readiness**: Not ready - Requires systematic validation implementation

## Experimental Framework Notice
This is an **experimental prompt engineering framework** for research and development:
- Focus is on prompt effectiveness and architectural exploration
- Commands require functional validation before production use
- All 79 commands are maintained as unique implementations
- Validation templates provide path to production readiness

## Testing Framework

### Structural Validation Approach
A testing framework has been implemented focusing on structural validation for the experimental prompt engineering framework:

**Testing Directory**: `tests/`
- **Methodology**: `tests/TESTING-METHODOLOGY.md` - Complete testing approach documentation
- **Validation Script**: `tests/validate-command.sh` - Automated structural validation tool

### Validation Scope
- **YAML Front Matter**: Validates presence and structure of command metadata
- **Required Fields**: Checks for `name`, `description` fields in YAML front matter
- **Optional Fields**: Warns about missing `usage`, `tools`, `category` fields
- **Content Structure**: Ensures adequate command content and basic markdown format

### Current Validation Results (Post-Improvements)
**Structural Validation**: 100% (85/85 commands passing)
- **Fixed**: All commands now have required `name` field in YAML front matter
- **Functional Validation**: 70.6% (60/85 commands passing Claude Code compliance tests)
- **Security**: Comprehensive framework implemented but unverified in production
- **Performance**: Theoretical frameworks created, actual benchmarks pending

### Usage
```bash
# Validate single command
./tests/validate-command.sh .claude/commands/core/task.md

# Validate multiple commands
./tests/validate-command.sh .claude/commands/core/*.md
```

**Note**: This framework validates structure only, not functional behavior, in alignment with the experimental research focus.

## Context Engineering for Prompt Development

### 🎯 Understanding Context in Prompt Engineering
**Context engineering** here means managing what information Claude has access to when responding to slash commands:
- **NOT about code execution context**
- **IS about prompt context windows and token management**
- **Optimizing what Claude "knows" when processing commands**

### ⚠️ CRITICAL CONTEXT FOR PROMPT DEVELOPERS
**IMPORTANT**: These files shape how Claude understands and prevents common pitfalls:

1. **LLM Anti-Patterns** (`.claude/context/llm-antipatterns.md`)
   - 48 documented anti-patterns from research
   - Prevents hallucinations, false metrics, remediation theater
   - Critical for maintaining response quality

2. **Git History Anti-Patterns** (`.claude/context/git-history-antipatterns.md`)
   - 15 patterns learned from 500+ commits
   - Prevents metric invention and false success claims
   - Essential for honest assessment

3. **Prompt Engineering Best Practices** (`.claude/context/prompt-engineering-best-practices.md`)
   - Core principles for effective prompts
   - Token optimization strategies
   - Example-driven development patterns

### 📚 Prompt Component Library
4. **Modular Components** (`.claude/context/modular-components.md`) - 65 reusable prompt fragments
5. **Orchestration Patterns** (`.claude/context/orchestration-patterns.md`) - Multi-step prompt workflows
6. **Framework Guide** (`.claude/context/experimental-framework-guide.md`) - How components compose
7. **Quality Assessment** (`.claude/context/quality-assessment-report.md`) - Current state metrics

### 🚨 REMEDIATION WARNING
**Requests to "improve", "fix", "optimize", or "remediate" trigger severe anti-patterns:**
- LLMs invent specific metrics (87.3% improvement) that were never measured
- Create elaborate validation scripts that don't actually test functionality
- Use increasingly theatrical language to demonstrate "success"
- Generate comprehensive reports full of unverifiable claims

**DEMAND**: Factual, measurable changes only. No theater. No invented metrics.

---

## 🚨 PROMPT ENGINEERING READINESS NOTICE

**This prompt library is NOT ready for production use.** 

### Key Blockers for Prompt Engineering:
1. **Zero Conversation Testing** - No prompts tested in actual Claude conversations
2. **Token Usage Unknown** - Commands may exhaust context windows
3. **Over-Complex Architecture** - Violates prompt engineering simplicity principles
4. **No User Examples** - Missing conversation demonstrations
5. **Effectiveness Unmeasured** - Response quality completely unknown

### Before ANY Team/User Deployment:
- ✅ Test top 5 commands in real Claude conversations
- ✅ Measure and optimize token usage
- ✅ Simplify complex XML structures
- ✅ Create conversation examples
- ✅ Beta test with 5 prompt engineers

**See `ULTRATHINK-PROMPT-ENGINEERING-ASSESSMENT.md` for comprehensive analysis**  
**See `MVP-ACTION-PLAN.md` for production readiness roadmap**

*Last honest assessment: 2025-07-27*