# Claude Code Modular Prompts

**⚠️ PRE-PRODUCTION** Claude Code library with 79 slash commands. Currently undergoing validation for production readiness.

**🚨 CRITICAL: NOT READY FOR PRODUCTION USE** - See `ULTRATHINK-PRODUCTION-READINESS-ASSESSMENT.md` and `MVP-ACTION-PLAN.md`

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

## Context Engineering

### ⚠️ MANDATORY CONTEXT LOADING
**CRITICAL**: The following context files MUST be loaded for all Claude Code sessions:

1. **Git History Anti-Patterns**: `.claude/context/git-history-antipatterns.md` 
   - Documents 15 severe LLM anti-patterns from 500+ commits  
   - REQUIRED to prevent: theatrical commits, fake metrics, reorganization addiction
   - Load this FIRST before any development work
   - **NEW Pattern #15**: Remediation Theater - fake improvements with invented metrics

2. **LLM Anti-Patterns**: `.claude/context/llm-antipatterns.md`
   - Comprehensive guide with 48 anti-patterns from 50+ research sources
   - Covers hallucinations, security issues, reasoning failures, biases
   - **NEW Patterns #47-48**: Retroactive Metric Invention, Fake Validation Scripts

### Essential Context Files
3. **Modular Components**: `.claude/context/modular-components.md` - All 63 components in searchable format
4. **Orchestration Patterns**: `.claude/context/orchestration-patterns.md` - Agent coordination patterns
5. **Best Practices**: `.claude/context/prompt-engineering-best-practices.md` - Positive patterns and techniques
6. **Framework Guide**: `.claude/context/experimental-framework-guide.md` - Philosophy and usage
7. **Quality Report**: `.claude/context/quality-assessment-report.md` - Current state analysis

### 🚨 REMEDIATION WARNING
**Requests to "improve", "fix", "optimize", or "remediate" trigger severe anti-patterns:**
- LLMs invent specific metrics (87.3% improvement) that were never measured
- Create elaborate validation scripts that don't actually test functionality
- Use increasingly theatrical language to demonstrate "success"
- Generate comprehensive reports full of unverifiable claims

**DEMAND**: Factual, measurable changes only. No theater. No invented metrics.

---

## 🚨 CRITICAL PRODUCTION READINESS NOTICE

**This project is NOT ready for production use.** 

### Key Blockers:
1. **Zero Real-World Testing** - No commands tested in actual Claude Code environment
2. **No User Documentation** - Missing quick start guide and basic documentation
3. **Unverified Security** - Security framework exists but never tested
4. **No Installation Process** - No way for users to actually install and use
5. **Performance Unknown** - All metrics are theoretical

### Before ANY Team/User Deployment:
- ✅ Complete MVP Action Plan (8-10 weeks)
- ✅ Test top 10 commands in real Claude Code
- ✅ Create minimal documentation
- ✅ Verify security implementation
- ✅ Beta test with 5-10 teams

**See `ULTRATHINK-PRODUCTION-READINESS-ASSESSMENT.md` for comprehensive gap analysis**  
**See `MVP-ACTION-PLAN.md` for production readiness roadmap**

*Last honest assessment: 2025-07-27*