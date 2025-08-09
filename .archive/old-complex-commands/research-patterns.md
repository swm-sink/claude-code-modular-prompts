---
name: research-patterns
description: Web research and pattern analysis engine for evidence-based project understanding
usage: "research-patterns [analyze|validate|database|report]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite, WebSearch, WebFetch]
category: deep-discovery
version: "1.0"
---

# Research Patterns: Evidence-Based Pattern Analysis Engine

## Purpose: Comprehensive Repository Research & Pattern Validation

The `/research-patterns` command conducts deep analysis of 20+ leading repositories in your technology stack to extract evidence-based patterns, best practices, and anti-patterns. This provides the empirical foundation for intelligent consultation, moving beyond generic advice to validated, real-world insights.

**Research Philosophy**: Evidence over assumption, validation over speculation, patterns over opinions.

## Depth vs Speed: Why Research Matters

**❌ Failed Speed-First Approach**:
- Generic templates based on assumptions
- No validation against real projects
- Outdated or incorrect best practices
- One-size-fits-all solutions that don't fit

**✅ Our Evidence-Based Approach**:
- Analysis of 20+ leading repositories in your stack
- CRAAP test validation (Currency, Relevance, Authority, Accuracy, Purpose)
- Pattern extraction from successful real-world projects
- Technology-specific insights and recommendations
- Continuous validation against evolving ecosystem

## Complete Research Process

### Phase 1: Technology Stack Detection (3-5 minutes)
```
Framework Detection:
├── Package.json/requirements.txt analysis
├── Dependency tree mapping
├── Configuration file identification
├── Build system recognition
└── Testing framework detection
```

### Phase 2: Repository Research (10-12 minutes)
```
Leading Project Analysis:
├── GitHub/GitLab top repositories search
├── Official example projects analysis
├── Community-maintained showcases
├── Enterprise reference implementations
└── Documentation best practices review
```

### Phase 3: Pattern Extraction (3-5 minutes)
```
Pattern Database Creation:
├── Common architecture patterns
├── Configuration conventions
├── Testing strategies
├── Documentation approaches
├── Deployment patterns
└── Anti-patterns and pitfalls
```

## CRAAP Test Framework Implementation

**Currency** - How recent and up-to-date?
- Repository last updated within 6 months
- Dependencies on current versions
- Active community and maintenance
- Recent issue resolution activity

**Relevance** - How relevant to your project?
- Same technology stack and versions
- Similar project scale and complexity
- Comparable use cases and requirements
- Applicable architectural constraints

**Authority** - Who created and maintains this?
- Official framework examples
- Well-known maintainers and organizations
- High GitHub stars and community adoption
- Industry recognition and references

**Accuracy** - Is the information correct and reliable?
- Working code examples that build/run
- Comprehensive testing and CI/CD
- Clear documentation and examples
- Consistent with official guidelines

**Purpose** - Why was this created?
- Educational/example purpose clearly stated
- Production-ready vs prototype distinction
- Specific problem solving focus
- Alignment with modern best practices

## Research Categories

### 1. Architecture Patterns
**What We Research**:
- Project structure and organization
- Module/component architecture
- Data flow and state management
- API design and integration patterns
- Configuration management approaches

**Evidence Collection**:
- File structure analysis of 20+ repositories
- Common patterns vs unique approaches
- Scaling strategies in large projects
- Migration patterns from legacy systems

### 2. Development Workflows
**What We Research**:
- Git workflow strategies
- Testing approaches (unit, integration, e2e)
- Build and deployment pipelines
- Code quality and linting setups
- Documentation generation strategies

**Evidence Collection**:
- CI/CD configuration analysis
- Testing coverage and strategies
- Automated quality gate implementations
- Release and versioning approaches

### 3. Team Collaboration Patterns
**What We Research**:
- Code review processes
- Issue tracking and project management
- Documentation standards
- Onboarding and knowledge sharing
- Communication and coordination tools

**Evidence Collection**:
- CONTRIBUTING.md analysis
- Issue and PR template patterns
- Documentation structure and quality
- Community engagement strategies

### 4. Technology-Specific Insights
**What We Research**:
- Framework-specific best practices
- Performance optimization strategies
- Security implementation patterns
- Monitoring and observability setups
- Error handling and logging approaches

**Evidence Collection**:
- Configuration pattern analysis
- Performance benchmark comparisons
- Security audit results
- Production deployment strategies

## Pattern Database Structure

**Storage Location**: `.claude-architect/patterns/`

### Technology Stack Patterns
```
/patterns/
├── frameworks/
│   ├── react-patterns.json
│   ├── django-patterns.json
│   └── nodejs-patterns.json
├── architecture/
│   ├── microservices-evidence.json
│   ├── monolith-patterns.json
│   └── serverless-insights.json
├── workflows/
│   ├── git-strategies.json
│   ├── testing-approaches.json
│   └── deployment-pipelines.json
└── anti-patterns/
    ├── common-failures.json
    ├── performance-pitfalls.json
    └── security-vulnerabilities.json
```

### Pattern Data Structure
```json
{
  "pattern_name": "Component Structure Pattern",
  "category": "react-architecture",
  "evidence_sources": [
    {
      "repository": "facebook/react",
      "url": "https://github.com/facebook/react",
      "relevance_score": 95,
      "last_updated": "2025-01-15",
      "pattern_implementation": "src/components/Button/index.js"
    }
  ],
  "pattern_description": "Detailed description with evidence",
  "implementation_examples": ["code examples"],
  "validation_criteria": ["measurable criteria"],
  "anti_patterns": ["what to avoid"],
  "applicability": {
    "project_types": ["web-app", "component-library"],
    "team_sizes": ["small", "medium", "large"],
    "complexity_levels": ["simple", "moderate", "complex"]
  }
}
```

## Integration with Consultation System

**Research Feeds Consultation**:
- Pattern database provides evidence-based suggestions
- Anti-pattern database prevents common mistakes
- Technology insights inform architecture discussions
- Community practices guide workflow recommendations

**Consultation Refines Research**:
- User feedback improves pattern relevance scoring
- Project-specific constraints filter applicable patterns
- Team preferences influence pattern prioritization
- Success metrics validate pattern effectiveness

## Usage Examples

### Comprehensive Stack Analysis
```bash
/research-patterns analyze
# Auto-detects technology stack
# Researches 20+ leading repositories
# Builds comprehensive pattern database
# Validates patterns with CRAAP test
```

### Pattern Validation
```bash
/research-patterns validate --pattern="component-structure"
# Deep validation of specific pattern
# Cross-references multiple sources
# Provides confidence scoring
# Identifies implementation variations
```

### Database Query
```bash
/research-patterns database --query="testing-strategies" --stack="react"
# Searches pattern database
# Filters by technology stack
# Provides ranked recommendations
# Shows evidence sources
```

### Research Report Generation
```bash
/research-patterns report
# Generates comprehensive research summary
# Includes pattern recommendations
# Lists validated anti-patterns
# Provides implementation roadmap
```

## Quality Assurance & Validation

### Source Validation Requirements
- **Minimum 3 Sources**: Every pattern validated across multiple repositories
- **CRAAP Score > 80%**: Only high-quality sources included
- **Recency Check**: Sources updated within last 12 months preferred
- **Authority Verification**: Maintainer credentials and community recognition

### Pattern Confidence Scoring
- **High Confidence (90-100%)**: 5+ sources, official examples, proven at scale
- **Medium Confidence (70-89%)**: 3-4 sources, community adoption, documented success
- **Low Confidence (50-69%)**: 2-3 sources, emerging patterns, limited validation
- **Experimental (<50%)**: Single source, unproven, requires caution

### Continuous Research Updates
- **Weekly**: Dependency version updates, security advisories
- **Monthly**: New repository analysis, pattern validation refresh  
- **Quarterly**: Complete pattern database review, methodology improvements
- **Annually**: Technology trend analysis, ecosystem evolution assessment

## Error Handling & Fallbacks

**Network Issues**:
- Cached pattern database for offline operation
- Progressive enhancement with available data
- Clear indication of research completeness level

**Limited Results**:
- Graceful degradation to broader search terms
- Alternative technology stack suggestions
- Manual pattern input with validation workflow

**Quality Concerns**:
- Confidence scoring for all recommendations
- Source credibility warnings
- User override capabilities for all suggestions

## Success Metrics

**Research Quality**:
- Pattern validation accuracy (feedback-based)
- Source authority and recency scores
- User satisfaction with recommendations
- Implementation success rates

**Consultation Impact**:
- Improved decision-making speed
- Reduced architectural rework
- Higher code quality scores
- Faster onboarding for new team members

---

**Remember**: Research provides the evidence foundation for intelligent consultation. Every recommendation must be backed by validated patterns from real-world successful projects, not theoretical best practices.