# Claude Code Modular Prompts

**Experimental** Claude Code library with 67 slash commands and comprehensive agent orchestration for prompt engineering research.

## Current Structure
```
/
├── .claude/
│   ├── commands/     # 67 commands (all unique, no duplicates)
│   ├── components/   # 63 reusable prompt components (consolidated)
│   ├── context/      # 7 essential context files
│   └── templates/    # Command templates
├── .main.archive/    # ARCHIVED - Original tallinn content (332 files)
└── tests/            # MISSING - Target: 90% coverage (currently: 0%)
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
| Commands | 67 | 67 unique | ✅ No duplicates found |
| Components | 63 | ~50-70 | ✅ Consolidated from 85 |
| Context files | 7 | 6-8 | ✅ Essential contexts only |
| Test coverage | 0% | 90% | ❌ Experimental validation needed |
| Max dir depth | 3 | 3 | ✅ Achieved |

## Experimental Framework Notice
This is an **experimental prompt engineering framework** for research and development:
- Performance benchmarks are not required
- Focus is on prompt effectiveness, not execution speed
- Commands are tested for correctness, not performance
- All 67 commands are maintained as unique implementations

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