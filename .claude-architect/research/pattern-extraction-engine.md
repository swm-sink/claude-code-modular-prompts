# Pattern Extraction Engine - Deep Discovery System
---
name: extract-patterns
description: Systematically extract evidence-based patterns from Claude Code repositories
usage: "/extract-patterns [repository-name] [focus-area]"
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, LS, WebFetch]
category: research
---

## Overview
The Pattern Extraction Engine systematically analyzes Claude Code repositories to extract evidence-based patterns for the deep discovery consultation system. This engine implements rigorous validation, confidence scoring, and cross-reference identification to ensure pattern quality.

## Extraction Workflow

### Phase 1: Repository Analysis Setup
1. **Repository Preparation**
   ```bash
   # Clone target repository for analysis
   git clone [repository-url] temp-analysis/
   cd temp-analysis/
   
   # Identify key directories and files
   find . -name ".claude" -type d
   find . -name "CLAUDE.md" -type f
   find . -name "*.md" -path "*/.claude/commands/*"
   ```

2. **Structure Discovery**
   - Map directory structure
   - Identify command files
   - Locate agent definitions
   - Find context files
   - Document workflow patterns

3. **Metadata Collection**
   - Repository stars, forks, activity
   - Last commit date and frequency
   - Contributor count and diversity
   - Issue/PR patterns

### Phase 2: Pattern Identification
Using the extraction templates, systematically identify patterns in each category:

#### Command Pattern Extraction
1. **Scan command files**:
   ```bash
   find .claude/commands -name "*.md" | while read file; do
     echo "Analyzing: $file"
     # Extract YAML frontmatter
     # Analyze command structure
     # Document parameter patterns
     # Note tool usage
   done
   ```

2. **Identify innovation patterns**:
   - Unique command structures
   - Creative tool combinations  
   - Novel parameter handling
   - Effective error handling

3. **Document usage patterns**:
   - Common command sequences
   - Integration approaches
   - Team adoption strategies

#### Agent Pattern Extraction  
1. **Locate agent definitions**:
   ```bash
   find . -path "*/.claude/agents/*" -name "*.md"
   find . -name "*agent*" -type f
   grep -r "agent" .claude/
   ```

2. **Analyze specialization strategies**:
   - Agent role definitions
   - Capability boundaries
   - Communication protocols
   - Orchestration patterns

3. **Extract coordination patterns**:
   - Task routing mechanisms
   - Result aggregation approaches
   - Conflict resolution strategies
   - Performance optimization

#### Context Pattern Extraction
1. **Analyze CLAUDE.md structures**:
   ```bash
   find . -name "CLAUDE.md" | while read file; do
     echo "Structure analysis: $file"
     wc -l "$file"
     grep -n "^#" "$file"  # Section headers
     grep -n "^-" "$file"   # Lists and bullets
   done
   ```

2. **Document hierarchy patterns**:
   - Multi-file context systems
   - Cross-reference approaches
   - Navigation patterns
   - Token optimization strategies

#### Workflow Pattern Extraction
1. **Identify process flows**:
   - Development workflows
   - Testing approaches
   - Deployment patterns
   - Team coordination

2. **Extract automation patterns**:
   - Trigger mechanisms
   - State management
   - Error handling
   - Quality gates

### Phase 3: Evidence Collection
For each identified pattern:

1. **Source Documentation**:
   - File locations with line numbers
   - Code snippets with context
   - Configuration examples
   - Usage documentation

2. **Cross-Reference Identification**:
   - Related patterns within repository
   - Dependencies between patterns
   - Complementary approaches
   - Conflicting implementations

3. **Effectiveness Indicators**:
   - Adoption metrics (usage frequency)
   - Community validation (stars, forks)
   - Maintenance indicators (recent commits)
   - Documentation quality

### Phase 4: Quality Validation
Apply rigorous validation using CRAAP framework:

#### Currency Assessment (0-1 score)
- **1.0**: Updated within 3 months
- **0.8**: Updated within 6 months  
- **0.6**: Updated within 1 year
- **0.4**: Updated within 2 years
- **0.2**: Updated > 2 years ago

#### Relevance Assessment (0-1 score)  
- **1.0**: Directly applicable to consultation system
- **0.8**: Highly relevant with minor adaptation
- **0.6**: Moderately relevant
- **0.4**: Somewhat relevant
- **0.2**: Tangentially relevant

#### Authority Assessment (0-1 score)
- **1.0**: 1000+ stars, active maintainers
- **0.8**: 500+ stars, regular updates
- **0.6**: 100+ stars, occasional updates
- **0.4**: 50+ stars, some activity
- **0.2**: < 50 stars, minimal activity

#### Accuracy Assessment (0-1 score)
- **1.0**: Working examples, comprehensive tests
- **0.8**: Working examples, basic tests
- **0.6**: Working examples, limited validation
- **0.4**: Examples with minor issues
- **0.2**: Examples with significant issues

#### Purpose Assessment (0-1 score)
- **1.0**: Created for production use
- **0.8**: Created for team/community use
- **0.6**: Created for learning/demonstration
- **0.4**: Created for experimentation
- **0.2**: Created for other purposes

### Phase 5: Database Population
Store validated patterns in structured format:

1. **Pattern Record Creation**:
   ```yaml
   pattern:
     id: pattern-commands-component-generator-20250807
     category: commands
     subcategory: generation_commands
     name: component-generator
     description: "React component generation with test scaffolding"
     
     evidence:
       sources:
         - repository: claude-code-react-patterns
           url: https://github.com/example/claude-code-react-patterns
           file_path: .claude/commands/component.md
           line_numbers: [1, 45]
           extracted_date: 2025-08-07T00:00:00Z
     
     confidence:
       evidence_strength: 0.8
       validation_confidence: 0.85
       implementation_confidence: 0.9
       overall_confidence: 0.85
   ```

2. **Cross-Reference Documentation**:
   - Link related patterns
   - Identify dependencies
   - Note complementary approaches
   - Flag conflicts

3. **Quality Metrics Calculation**:
   - Confidence scores
   - Adoption indicators
   - Effectiveness measures

## Implementation Commands

### Primary Extraction Command
```bash
/extract-patterns claude-code-react-patterns web-development
```

**Process Flow**:
1. Load repository from catalog
2. Apply appropriate extraction templates  
3. Collect evidence systematically
4. Validate using CRAAP framework
5. Populate research database
6. Generate extraction report

### Validation Command
```bash
/validate-extraction pattern-commands-123
```

**Validation Steps**:
1. Check evidence completeness
2. Verify CRAAP scores
3. Validate cross-references
4. Calculate confidence scores
5. Flag quality issues

### Batch Processing Command
```bash
/extract-patterns-batch priority-week-1
```

**Batch Process**:
1. Load priority target list
2. Process repositories in sequence
3. Aggregate findings
4. Generate comprehensive report
5. Update research database

## Quality Requirements

### Minimum Standards
- **Evidence Sources**: 3+ different repositories
- **Confidence Score**: 0.6+ (60%)  
- **CRAAP Validation**: Complete for all patterns
- **Cross-References**: 2+ identified relationships

### Excellence Standards  
- **Evidence Sources**: 5+ different repositories
- **Confidence Score**: 0.8+ (80%)
- **User Validation**: Community feedback incorporated
- **Implementation Testing**: Working examples validated

### Rejection Criteria
- **Evidence Sources**: < 3 repositories
- **Confidence Score**: < 0.6 (60%)
- **CRAAP Validation**: Incomplete
- **Implementation**: Non-working examples

## Success Metrics

### Quantitative Targets
- **Patterns Extracted**: 75+ high-quality patterns
- **Domain Coverage**: 7+ domains represented
- **Confidence Distribution**: 40%+ high-confidence patterns
- **Cross-Reference Coverage**: 60%+ patterns cross-referenced

### Qualitative Indicators
- Patterns support 30-60 minute consultation
- Evidence thoroughly documented
- Conflicts and anti-patterns identified
- Innovation and unique approaches highlighted

## Output Deliverables

### Per-Repository Analysis
1. **Extraction Report**: Comprehensive pattern analysis
2. **Pattern Database Entries**: Structured pattern records
3. **Quality Assessment**: CRAAP validation results  
4. **Cross-Reference Map**: Relationship documentation

### Aggregate Deliverables
1. **Master Pattern Database**: All validated patterns
2. **Pattern Relationship Map**: Cross-references and dependencies
3. **Domain Analysis**: Patterns by domain and use case
4. **Innovation Catalog**: Novel approaches and techniques

## Risk Mitigation

### Repository Access Issues
- **Action**: Use cached/archived versions
- **Backup**: Move to next priority target
- **Documentation**: Note access limitations

### Low Pattern Yield
- **Threshold**: < 5 patterns per repository
- **Action**: Extend analysis time or add repositories
- **Quality Gate**: Maintain confidence standards

### Time Overrun
- **Maximum**: 5 hours per repository
- **Action**: Focus on highest-priority patterns
- **Escalation**: Adjust scope or timeline

### Quality Issues
- **Minimum Confidence**: 0.6 threshold
- **Action**: Increase validation rigor
- **Quality Assurance**: Peer review for borderline patterns

This extraction engine provides the systematic, evidence-based approach needed to build a valuable pattern database for the 30-60 minute deep discovery consultation system.