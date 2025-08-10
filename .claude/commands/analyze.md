---
name: analyze
description: Adaptive codebase analysis based on project size
usage: "/analyze [--depth quick|standard|deep] [--focus patterns|metrics|health]"
allowed-tools: [Read, Glob, Grep, Task]
---

# Adaptive Project Analysis

I'll analyze your codebase with appropriate depth based on its size and complexity.

## Detecting Project Scope

Quick assessment:
- File count: [checking...]
- Primary language: [detecting...]
- Project type: [identifying...]

<quick-mode>
<!-- For < 10 files or --depth quick -->

## Quick Analysis (30 seconds)

### Structure Overview
- Total files: [count]
- Main technology: [detected]
- Entry points: [identified]

### Key Patterns
- Architecture: [style detected]
- Dependencies: [count and type]
- Test coverage: [present/absent]

### Summary
[2-3 line assessment of project health]
</quick-mode>

<standard-mode>
<!-- For 10-100 files or default -->

## Standard Analysis (2 minutes)

### Project Metrics
- **Size**: [LOC, files, directories]
- **Languages**: [distribution]
- **Complexity**: [simple/moderate/complex]

### Architecture Patterns
- **Structure**: [detected pattern]
- **Dependencies**: [internal/external mapping]
- **Key modules**: [identified]

### Code Quality Indicators
- **Consistency**: [assessment]
- **Documentation**: [coverage]
- **Testing**: [framework and coverage]

### Improvement Opportunities
1. [Most impactful improvement]
2. [Second priority]
3. [Nice to have]

*Need deeper analysis? Use `/analyze --depth deep`*
</standard-mode>

<deep-mode>
<!-- For > 100 files or --depth deep -->

## Comprehensive Analysis (5 minutes)

*Large project detected. Using parallel analysis for efficiency.*

### Parallel Analysis Tasks

**Task 1**: Architecture Assessment
- Module coupling and cohesion
- Dependency graph analysis
- Pattern consistency

**Task 2**: Quality Metrics
- Complexity scores
- Technical debt indicators
- Performance bottlenecks

**Task 3**: Health Scoring
- Maintainability index
- Test coverage analysis
- Documentation completeness

### Detailed Findings

#### Architecture Health: [score]/100
- **Strengths**: [identified]
- **Weaknesses**: [identified]
- **Risks**: [identified]

#### Code Quality: [score]/100
- **Complexity hotspots**: [files]
- **Duplication**: [percentage]
- **Standards compliance**: [assessment]

#### Team Patterns
- **Hot files**: [frequently changed]
- **Conventions**: [detected]
- **Workflow**: [identified from git]

### Strategic Recommendations
1. **Immediate**: [critical fixes]
2. **Short-term**: [1-2 week improvements]
3. **Long-term**: [architectural changes]

### Interactive Exploration

Want to dive deeper into any area?
- Use `/analyze --focus patterns` for architecture details
- Use `/analyze --focus metrics` for quality metrics
- Use `/analyze --focus health` for maintainability
</deep-mode>

## Analysis Complete

[Mode-appropriate summary and next steps]

**Useful next commands**:
- `/build` - Start implementing features
- `/test` - Generate tests for uncovered code
- `/refactor` - Improve identified issues