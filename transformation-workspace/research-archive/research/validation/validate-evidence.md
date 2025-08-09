# Evidence Validation Command - CRAAP Test Implementation
---
name: validate-evidence
description: Apply rigorous CRAAP testing to extracted patterns with confidence scoring
usage: "/validate-evidence [pattern-id] [validation-level]"
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, LS, WebFetch]
category: research-validation
---

## Overview
This command implements the systematic CRAAP (Currency, Relevance, Authority, Accuracy, Purpose) test framework to validate extracted patterns and calculate confidence scores. It ensures only evidence-based, high-quality patterns enter our 30-60 minute consultation system.

## Command Parameters

### Required Parameters
- **pattern-id**: Unique identifier of the pattern to validate (e.g., "pattern-commands-component-generator-20250807")

### Optional Parameters  
- **validation-level**: Depth of validation to perform
  - `quick`: Basic CRAAP assessment (15 minutes)
  - `standard`: Full CRAAP with cross-reference validation (30 minutes) 
  - `comprehensive`: Complete validation with technical testing (45 minutes)
  - Default: `standard`

## Validation Process

### Phase 1: Pattern Data Loading
```bash
# Load pattern data from research database
READ pattern record from database
VERIFY pattern completeness and structure
EXTRACT evidence sources and metadata
INITIALIZE validation workspace
```

**Required Pattern Elements:**
- Pattern identification (id, name, category)
- Description and use case
- Evidence sources (minimum 3)
- Implementation examples
- Domain and context information

### Phase 2: CRAAP Test Execution

#### Currency Assessment (Weight: 0.15)
**Evaluation Criteria:**
```yaml
Currency Scoring:
  1.0: Updated within 3 months + current dependencies
  0.8: Updated within 6 months + most dependencies current  
  0.6: Updated within 1 year + key dependencies current
  0.4: Updated within 2 years + some outdated dependencies
  0.2: Updated > 2 years ago + multiple outdated dependencies
```

**Validation Steps:**
1. Check last update dates of all source repositories
2. Verify Claude Code version compatibility
3. Assess dependency currency status
4. Review recent community activity
5. Calculate weighted currency score

#### Relevance Assessment (Weight: 0.25)
**Evaluation Criteria:**
```yaml
Relevance Scoring:
  1.0: Perfect alignment with 30-60 minute consultation goals
  0.8: Strong alignment with depth-focused approach
  0.6: General alignment requiring some adaptation
  0.4: Partial alignment with significant adaptation needed
  0.2: Poor alignment with extensive modification required
```

**Validation Steps:**
1. Assess alignment with consultation system goals
2. Evaluate support for depth-over-speed philosophy
3. Check applicability to target use cases
4. Measure contribution to project understanding
5. Calculate weighted relevance score

#### Authority Assessment (Weight: 0.20)
**Evaluation Criteria:**
```yaml
Authority Scoring:
  1.0: 1000+ stars + recognized experts + enterprise adoption
  0.8: 500+ stars + experienced maintainers + good feedback
  0.6: 100+ stars + competent maintainers + positive response
  0.4: 50+ stars + basic expertise + mixed feedback
  0.2: <50 stars + unknown expertise + minimal validation
```

**Validation Steps:**
1. Collect repository metrics (stars, forks, contributors)
2. Research maintainer expertise and reputation
3. Assess community feedback and validation
4. Check enterprise or professional adoption
5. Calculate weighted authority score

#### Accuracy Assessment (Weight: 0.25)
**Evaluation Criteria:**
```yaml
Accuracy Scoring:
  1.0: Working examples + comprehensive tests + no errors
  0.8: Working examples + basic tests + minor issues
  0.6: Working examples + limited validation + some issues
  0.4: Examples with known issues + multiple problems
  0.2: Broken examples + significant errors + poor practices
```

**Validation Steps:**
1. Test all provided examples for functionality
2. Verify technical correctness and best practices
3. Check for security vulnerabilities or issues
4. Assess performance implications
5. Calculate weighted accuracy score

#### Purpose Assessment (Weight: 0.15)
**Evaluation Criteria:**
```yaml
Purpose Scoring:
  1.0: Production use + clear value + professional implementation
  0.8: Team use + good value + quality implementation
  0.6: Learning/demo + educational value + adequate implementation
  0.4: Experimental + proof-of-concept + basic implementation
  0.2: Unclear purpose + limited value + poor implementation
```

**Validation Steps:**
1. Analyze pattern creation intent and purpose
2. Assess business/technical value proposition
3. Evaluate implementation quality and professionalism
4. Check maintenance plan and sustainability
5. Calculate weighted purpose score

### Phase 3: Confidence Score Calculation

#### Weighted Score Formula
```
Overall Confidence = (Currency × 0.15) + (Relevance × 0.25) + (Authority × 0.20) + (Accuracy × 0.25) + (Purpose × 0.15)
```

#### Confidence Thresholds and Actions
```yaml
Confidence Levels:
  High (0.80-1.00):
    action: "Accept for immediate inclusion"
    notes: "Pattern ready for consultation system"
    
  Medium (0.60-0.79):
    action: "Accept with validation notes"  
    notes: "Include with adaptation guidance"
    
  Low (0.40-0.59):
    action: "Flag for improvement"
    notes: "Requires significant enhancement"
    
  Reject (0.00-0.39):
    action: "Reject with recommendations"
    notes: "Insufficient quality for inclusion"
```

### Phase 4: Cross-Reference Validation

#### Relationship Analysis
```bash
# Identify pattern relationships
SEARCH for related patterns in database
ANALYZE dependency requirements
CHECK for conflicts with existing patterns
VALIDATE complementary relationships
```

**Relationship Types:**
- **Extends**: Pattern builds on another (confidence +0.05)
- **Conflicts**: Pattern conflicts with another (confidence -0.10)  
- **Complements**: Pattern works well with another (confidence +0.03)
- **Requires**: Pattern depends on another (confidence neutral)

#### Cross-Reference Scoring
```yaml
Correlation Strength:
  Strong (0.8+): 5+ repositories show correlation
  Moderate (0.6+): 3+ repositories show correlation  
  Weak (0.4+): 2+ repositories show correlation
```

### Phase 5: Technical Validation

#### Structural Validation
```bash
# Validate pattern structure and syntax
CHECK YAML frontmatter format
VERIFY Claude Code compliance
VALIDATE tool usage patterns
TEST example implementations
```

#### Quality Gates
```yaml
Technical Requirements:
  - Valid YAML/Markdown structure
  - Claude Code command standards compliance
  - Appropriate tool usage
  - Error handling included
  - Clear documentation
  - Working examples
  - Prerequisites documented
```

### Phase 6: Final Assessment and Reporting

#### Validation Report Generation
```yaml
Validation Report Structure:
  pattern_identification:
    - Pattern ID, name, category
    - Source repositories and evidence
    - Validation date and assessor
    
  craap_assessment:
    - Individual CRAAP scores with rationale
    - Weighted calculation breakdown
    - Overall confidence score
    
  cross_reference_analysis:
    - Identified relationships
    - Dependency validation
    - Conflict resolution
    - Correlation strength
    
  technical_validation:
    - Structural compliance results
    - Example testing outcomes
    - Quality gate assessment
    - Technical recommendations
    
  final_decision:
    - Include/reject decision with rationale
    - Confidence level classification
    - Implementation recommendations
    - Improvement suggestions
```

## Usage Examples

### Basic Pattern Validation
```bash
/validate-evidence pattern-commands-api-generator-20250807
```

**Expected Output:**
```yaml
Validation Results:
  Pattern: API Generator Command Pattern
  Overall Confidence: 0.82 (High)
  
  CRAAP Scores:
    Currency: 0.9 (Updated 2 months ago, current dependencies)
    Relevance: 0.85 (Strong alignment with consultation goals)
    Authority: 0.8 (1200+ stars, experienced maintainers)
    Accuracy: 0.8 (Working examples, minor test gaps)
    Purpose: 0.85 (Clear production value)
  
  Decision: ACCEPT for immediate inclusion
  Notes: High-quality pattern ready for consultation system
```

### Comprehensive Validation with Cross-References
```bash
/validate-evidence pattern-agents-orchestration-20250807 comprehensive
```

**Expected Output:**
```yaml
Validation Results:
  Pattern: Agent Orchestration Pattern  
  Overall Confidence: 0.67 (Medium)
  
  CRAAP Scores:
    Currency: 0.7 (Updated 8 months ago)
    Relevance: 0.8 (Good alignment, needs adaptation)
    Authority: 0.6 (300 stars, competent maintainers)
    Accuracy: 0.6 (Examples work, limited testing)
    Purpose: 0.7 (Clear team use value)
  
  Cross-References:
    Extends: pattern-commands-multi-step-20250806 (+0.05)
    Complements: pattern-context-hierarchical-20250805 (+0.03)
    Final Adjusted Score: 0.75
  
  Technical Validation:
    Structure: PASS
    Claude Code Compliance: PASS  
    Examples: 2/3 working (PARTIAL)
    
  Decision: ACCEPT with validation notes
  Notes: Include with example fixes and adaptation guidance
```

### Batch Validation Command
```bash
/validate-evidence-batch priority-patterns-week-1
```

**Process:**
1. Load all patterns from specified batch
2. Run standard validation on each pattern
3. Generate aggregate quality report
4. Identify patterns needing attention
5. Update research database with results

## Quality Requirements

### Minimum Acceptance Criteria
- **Confidence Score**: ≥ 0.60
- **Evidence Sources**: ≥ 3 different repositories
- **Technical Validation**: All quality gates passed
- **Cross-References**: No unresolved conflicts

### Excellence Criteria  
- **Confidence Score**: ≥ 0.80
- **Evidence Sources**: ≥ 5 different repositories
- **User Validation**: Community feedback incorporated
- **Implementation**: Working examples tested

### Automatic Rejection Criteria
- **Confidence Score**: < 0.40
- **Evidence Sources**: < 3 repositories
- **Technical Issues**: Major quality gate failures
- **Conflicts**: Unresolved pattern conflicts

## Success Metrics

### Validation Accuracy
- **Target**: 95%+ patterns work as expected in practice
- **Measurement**: Post-implementation success tracking
- **Review**: Monthly validation accuracy assessment

### Processing Efficiency
- **Quick Validation**: 15 minutes average
- **Standard Validation**: 30 minutes average  
- **Comprehensive Validation**: 45 minutes average
- **Quality**: No reduction in thoroughness for speed

### Pattern Quality Distribution
- **Target**: 40%+ high confidence (≥0.80)
- **Target**: 80%+ medium+ confidence (≥0.60)
- **Target**: <10% rejection rate after initial screening

## Error Handling

### Common Issues and Solutions

#### Insufficient Evidence
```yaml
Error: "Pattern has only 2 evidence sources (minimum 3 required)"
Solution: 
  - Search for additional repositories with similar patterns
  - Consider exceptional case review if pattern is uniquely valuable
  - Document search efforts and rationale
```

#### Cross-Reference Conflicts
```yaml
Error: "Pattern conflicts with pattern-X but conflict unresolved"
Solution:
  - Analyze conflict nature and severity
  - Document resolution strategy
  - Consider pattern modification or rejection
  - Update relationship documentation
```

#### Technical Validation Failures
```yaml
Error: "Example implementation fails with error Y"  
Solution:
  - Debug and fix example if possible
  - Document known limitations
  - Reduce accuracy score appropriately
  - Consider rejection if critical failures
```

### Escalation Procedures
- **Borderline Cases**: Independent dual review (0.55-0.65 scores)
- **High-Impact Patterns**: Mandatory peer review
- **Technical Disputes**: Technical committee review
- **Appeals**: Formal appeals process with documentation

## Integration Points

### Research Database Updates
```bash
# Update pattern record with validation results
UPDATE pattern SET 
  validation_status = 'completed',
  confidence_score = calculated_score,
  craap_scores = individual_scores,
  validation_notes = assessment_details,
  last_validated = current_timestamp
```

### Consultation System Integration
```bash
# Patterns meeting acceptance criteria automatically available
IF confidence_score >= 0.60 THEN
  ADD pattern to consultation system catalog
  GENERATE usage documentation
  UPDATE pattern recommendations
```

This command provides the rigorous, evidence-based validation system needed to ensure our 30-60 minute consultation is built on REAL QUALITY PATTERNS, not assumptions or hopes.