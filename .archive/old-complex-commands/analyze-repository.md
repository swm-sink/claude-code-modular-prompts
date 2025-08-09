---
name: analyze-repository
description: Deep analysis of individual repositories for evidence-based pattern extraction and consultation system integration
usage: "analyze-repository [repository-url|repository-name] [--focus=domain] [--session-id=id]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite, WebFetch, WebSearch]
category: research
version: "1.0"
---

# Analyze Repository: Deep Evidence-Based Pattern Analysis

## Purpose: Systematic Single-Repository Intelligence Extraction

The `/analyze-repository` command performs comprehensive 30-60 minute deep analysis of individual Claude Code repositories to extract evidence-based patterns, validate with CRAAP framework, and populate our research database. This is the primary research tool that transforms leading repositories into actionable intelligence for the consultation system.

**Research Philosophy**: One repository, thoroughly analyzed, provides more value than ten repositories skimmed.

## Deep vs Quick: Why Thorough Analysis Matters

**❌ Failed Quick-Scan Approach**:
- Surface-level pattern identification
- No validation of pattern effectiveness
- Missing cross-reference relationships
- Generic insights without context
- No confidence scoring

**✅ Our Deep Analysis Approach**:
- Complete repository structure mapping
- Pattern extraction with evidence collection
- CRAAP test validation for every pattern
- Cross-reference identification and documentation
- Confidence scoring and quality assessment
- Integration with research database
- Session management for 30-60 minute analysis

## Complete Analysis Process

### Phase 1: Repository Preparation (5 minutes)
```
Repository Setup:
├── Clone or access target repository
├── Verify repository accessibility and structure
├── Load repository metadata (stars, activity, contributors)
├── Initialize analysis session with progress tracking
└── Create working directory for extraction
```

### Phase 2: Structure Discovery (10 minutes)
```
Architecture Mapping:
├── .claude/ directory structure analysis
├── Command inventory and categorization
├── Agent definitions and specializations
├── Context files and hierarchy patterns
├── Workflow and orchestration documentation
└── Integration and configuration patterns
```

### Phase 3: Pattern Extraction (15-20 minutes)
```
Evidence Collection:
├── Apply command pattern templates
├── Extract agent orchestration patterns
├── Document context engineering approaches
├── Identify workflow automation strategies
├── Collect implementation examples with code
└── Note innovation and unique approaches
```

### Phase 4: CRAAP Validation (10-15 minutes)
```
Quality Assessment:
├── Currency: Repository recency and maintenance
├── Relevance: Alignment with consultation goals
├── Authority: Source credibility and community validation
├── Accuracy: Technical correctness and working examples
├── Purpose: Production-readiness and intentional design
└── Confidence scoring and threshold evaluation
```

### Phase 5: Database Integration (5-10 minutes)
```
Knowledge Capture:
├── Pattern record creation with evidence
├── Cross-reference identification and mapping
├── Research database population
├── Quality metrics calculation
├── Analysis report generation
└── Session completion and results summary
```

## Session Management System

### Session State Tracking
```yaml
session:
  id: "analysis-react-patterns-20250807-001"
  repository: "claude-code-react-patterns"
  start_time: "2025-08-07T10:00:00Z"
  estimated_duration: "45 minutes"
  current_phase: "pattern_extraction"
  progress:
    structure_discovery: "completed"
    pattern_extraction: "in_progress"
    validation: "pending"
    integration: "pending"
  findings:
    patterns_identified: 12
    high_confidence: 4
    medium_confidence: 6
    low_confidence: 2
```

### Pause/Resume Capability
- **Pause**: `/analyze-repository --pause --session-id=analysis-react-patterns-001`
- **Resume**: `/analyze-repository --resume --session-id=analysis-react-patterns-001`
- **Status**: `/analyze-repository --status --session-id=analysis-react-patterns-001`

### Progress Tracking
- Real-time progress updates with time estimates
- Quality gates at each phase transition
- Early warning for low-yield repositories
- Adaptive timeline based on findings richness

## Analysis Categories and Focus Areas

### 1. Command Pattern Analysis
**What We Extract**:
- Command structure and YAML frontmatter patterns
- Tool usage strategies and combinations
- Parameter handling and validation approaches
- Error handling and user guidance patterns
- Integration with other commands

**Evidence Collection**:
```bash
# Command structure analysis
find .claude/commands -name "*.md" | head -10 | while read cmd; do
  echo "=== Analyzing: $cmd ==="
  # Extract YAML frontmatter
  sed -n '1,/^---$/p' "$cmd"
  # Analyze command patterns
  grep -n "usage:\|allowed-tools:\|category:" "$cmd"
done
```

### 2. Agent Orchestration Analysis
**What We Extract**:
- Agent specialization and role definitions
- Inter-agent communication protocols
- Task routing and delegation patterns
- Result aggregation strategies
- Performance optimization approaches

**Evidence Collection**:
```bash
# Agent pattern identification
find . -path "*/.claude/agents/*" -name "*.md"
grep -r "agent\|orchestrat\|coordinat" .claude/ | head -20
# Document agent capabilities and boundaries
```

### 3. Context Engineering Analysis
**What We Extract**:
- CLAUDE.md structure and organization patterns
- Multi-file context system architectures
- Cross-reference and navigation strategies
- Token optimization techniques
- Context hierarchy and inheritance patterns

**Evidence Collection**:
```bash
# Context structure analysis
find . -name "CLAUDE.md" -o -name "claude.*.md" | while read file; do
  echo "Context file: $file"
  wc -l "$file"
  grep -c "^#\|^##\|^###" "$file"  # Section counting
done
```

### 4. Workflow Automation Analysis
**What We Extract**:
- Development workflow patterns
- Testing and validation strategies
- Deployment and release automation
- Team coordination mechanisms
- Quality assurance approaches

**Evidence Collection**:
```bash
# Workflow pattern identification
find . -name "*.yml" -o -name "*.yaml" | grep -E "workflow|action|pipeline"
grep -r "hook\|trigger\|automat" .claude/ | head -15
```

## CRAAP Framework Implementation

### Currency Assessment (Weight: 15%)
```
Scoring Criteria:
├── Repository last commit within 3 months: 1.0
├── Repository last commit within 6 months: 0.8
├── Repository last commit within 1 year: 0.6
├── Repository last commit within 2 years: 0.4
└── Repository last commit > 2 years ago: 0.2

Validation:
├── Check git log --oneline -n 1
├── Verify dependency currency
├── Assess community activity
└── Document maintenance status
```

### Relevance Assessment (Weight: 25%)
```
Alignment with Consultation Goals:
├── Perfect alignment with deep discovery: 1.0
├── Strong alignment with minor adaptation: 0.8
├── Moderate alignment requiring work: 0.6
├── Limited alignment, significant adaptation: 0.4
└── Poor alignment, minimal value: 0.2

Evaluation Criteria:
├── Supports 30-60 minute consultation philosophy
├── Enhances project understanding depth
├── Provides evidence-based insights
└── Applicable to target domains
```

### Authority Assessment (Weight: 20%)
```
Source Credibility:
├── 1000+ stars, recognized maintainers: 1.0
├── 500+ stars, experienced team: 0.8
├── 100+ stars, competent maintainers: 0.6
├── 50+ stars, basic expertise: 0.4
└── <50 stars, unknown authority: 0.2

Validation:
├── GitHub star count and trend
├── Maintainer background and expertise
├── Community engagement metrics
└── Enterprise adoption evidence
```

### Accuracy Assessment (Weight: 25%)
```
Technical Correctness:
├── Working examples, comprehensive tests: 1.0
├── Working examples, basic validation: 0.8
├── Mostly working, minor issues: 0.6
├── Examples with known problems: 0.4
└── Broken or non-working examples: 0.2

Validation Process:
├── Test command syntax and structure
├── Verify tool usage compliance
├── Check example code functionality
└── Assess best practice adherence
```

### Purpose Assessment (Weight: 15%)
```
Intentional Design:
├── Created for production use: 1.0
├── Created for team/community: 0.8
├── Created for learning/demo: 0.6
├── Created for experimentation: 0.4
└── Unclear or poor purpose: 0.2

Assessment:
├── README and documentation analysis
├── Issue and PR pattern review
├── Long-term maintenance evidence
└── Professional implementation quality
```

## Quality Gates and Validation

### Phase Transition Requirements
**Structure Discovery → Pattern Extraction**:
- Minimum 5 commands or 3 agents identified
- Repository structure successfully mapped
- Working directory prepared

**Pattern Extraction → CRAAP Validation**:
- Minimum 8 patterns identified across categories
- Evidence collected for each pattern
- Cross-references documented

**CRAAP Validation → Database Integration**:
- CRAAP scores calculated for all patterns
- Minimum 60% confidence threshold met
- Quality issues documented and addressed

### Quality Assurance Checkpoints
```
Evidence Validation:
├── Each pattern has 3+ code examples
├── Working examples verified where possible
├── Cross-references identified and documented
├── Confidence scores meet thresholds
└── Database schema compliance verified
```

## Usage Examples

### Basic Repository Analysis
```bash
/analyze-repository claude-code-react-patterns
# Performs complete 45-minute analysis
# Auto-detects focus areas from repository
# Populates research database
# Generates comprehensive report
```

### Focused Domain Analysis
```bash
/analyze-repository nextjs-claude-automation --focus=web-development
# Emphasizes web development patterns
# Filters patterns for domain relevance
# Applies domain-specific validation
# Generates domain-focused insights
```

### Session-Managed Analysis
```bash
# Start new analysis session
/analyze-repository claude-ml-workflows --session-id=ml-analysis-001

# Pause after 30 minutes
/analyze-repository --pause --session-id=ml-analysis-001

# Resume later
/analyze-repository --resume --session-id=ml-analysis-001

# Check progress
/analyze-repository --status --session-id=ml-analysis-001
```

### Integration with Research Database
```bash
# Analysis with database integration
/analyze-repository claude-devops-toolkit --database-update --cross-reference
# Automatically updates research database
# Identifies relationships with existing patterns
# Calculates aggregate confidence metrics
```

## Error Handling and Recovery

### Repository Access Issues
```
Problem: Repository not accessible
Action: 
├── Try alternative access methods
├── Check for archived versions
├── Document access limitations
└── Continue with available alternatives
```

### Low Pattern Yield
```
Problem: <8 patterns identified
Action:
├── Extend analysis time by 15 minutes
├── Broaden pattern search criteria
├── Focus on innovation and unique approaches
└── Document limited yield with reasoning
```

### Time Overrun Management
```
Maximum Analysis Time: 90 minutes
Actions at 60 minutes:
├── Prioritize high-confidence patterns
├── Focus on most relevant categories
├── Accelerate validation process
└── Generate preliminary report
```

### Quality Threshold Failures
```
Problem: Patterns below confidence threshold
Action:
├── Extend evidence collection
├── Seek additional validation sources
├── Adjust confidence scoring if justified
└── Document quality concerns
```

## Integration with Research Infrastructure

### Database Population
```yaml
# Pattern record structure
pattern_record:
  id: "pattern-commands-component-gen-20250807"
  source_repository: "claude-code-react-patterns"
  analysis_session: "analysis-react-patterns-001"
  extraction_date: "2025-08-07T14:30:00Z"
  confidence_score: 0.85
  craap_scores:
    currency: 0.9
    relevance: 0.8
    authority: 0.9
    accuracy: 0.8
    purpose: 0.9
  evidence_sources: 3
  cross_references: ["pattern-commands-test-gen", "pattern-agents-quality"]
```

### Cross-Reference System
- Automatic relationship detection
- Dependency mapping
- Conflict identification
- Complementary pattern discovery

### Research Database Integration
```bash
# Database operations during analysis
- INSERT pattern records as discovered
- UPDATE confidence scores as validation completes
- CREATE cross-reference relationships
- CALCULATE aggregate metrics for repository
```

## Output Deliverables

### Analysis Report
```markdown
# Repository Analysis Report: claude-code-react-patterns

## Executive Summary
- Repository Quality: High (Authority: 0.9, Currency: 0.9)
- Patterns Extracted: 15 (High: 7, Medium: 6, Low: 2)
- Innovation Score: 0.8 (novel component generation patterns)
- Consultation Relevance: 0.85 (strongly supports deep discovery)

## Pattern Categories
### Commands (8 patterns)
- component-generator: 0.9 confidence
- test-scaffolder: 0.8 confidence
- state-manager: 0.7 confidence
...

### Cross-Reference Analysis
- 12 relationships identified
- 3 pattern dependencies
- 2 complementary workflows
- 0 conflicts detected
```

### Research Database Updates
- 15 new pattern records
- 12 cross-reference relationships
- Repository metadata entry
- Analysis session documentation

### Quality Metrics
```yaml
analysis_quality:
  total_time: "47 minutes"
  patterns_per_minute: 0.32
  average_confidence: 0.78
  evidence_completeness: 0.92
  validation_coverage: 1.0
```

## Success Criteria

### Quantitative Targets
- **Analysis Time**: 30-60 minutes per repository
- **Pattern Yield**: 8+ patterns minimum, 15+ preferred
- **Confidence Score**: 70%+ average across patterns
- **Evidence Quality**: 3+ sources per pattern
- **Cross-References**: 2+ relationships per pattern

### Qualitative Indicators
- Patterns support 30-60 minute consultation goals
- Evidence thoroughly documented with working examples
- Innovation and unique approaches highlighted
- Clear integration path to consultation system
- Actionable insights for project-specific recommendations

## Integration with Consultation System

### Pattern Database Feeds Consultation
- Evidence-based recommendations during consultation
- Domain-specific pattern suggestions
- Anti-pattern warnings based on repository analysis
- Confidence-scored alternatives for decision making

### Analysis Informs Agent Development
- Agent specialization based on discovered patterns
- Orchestration strategies from successful repositories
- Quality assurance approaches from validated examples
- Innovation adoption from cutting-edge implementations

---

**Remember**: Each repository analysis contributes to building comprehensive evidence-based intelligence that transforms the 30-60 minute consultation from generic advice to project-specific expertise. Quality and thoroughness over speed ensure valuable, actionable insights.