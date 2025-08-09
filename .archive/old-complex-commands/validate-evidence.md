---
name: validate-evidence
description: Comprehensive CRAAP framework validation for extracted patterns with confidence scoring and quality assurance
usage: "validate-evidence [pattern-id|batch-name] [--framework=craap] [--threshold=0.7] [--detailed]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite, WebFetch]
category: research
version: "1.0"
---

# Validate Evidence: Rigorous CRAAP Framework Pattern Validation

## Purpose: Evidence-Based Quality Assurance for Pattern Database

The `/validate-evidence` command applies rigorous CRAAP (Currency, Relevance, Authority, Accuracy, Purpose) framework validation to extracted patterns, ensuring only high-quality, evidence-based patterns enter the consultation system. This command is the quality gatekeeper that maintains the integrity of our research database.

**Validation Philosophy**: No pattern enters consultation without rigorous evidence validation - quality over quantity always.

## Rigorous vs Permissive: Why Strict Validation Matters

**❌ Failed Permissive Approach**:
- Accept patterns without thorough validation
- Rely on surface-level quality indicators
- Skip evidence verification steps
- Allow patterns based on popularity alone
- No systematic quality improvement process

**✅ Our Rigorous Validation Approach**:
- Comprehensive CRAAP framework assessment
- Evidence source verification with 3+ source requirement
- Technical accuracy testing with working examples
- Cross-reference validation and relationship verification
- Confidence scoring with transparent methodology
- Continuous validation improvement and calibration

## CRAAP Framework Implementation

### Currency Assessment (Weight: 15%)
**"How recent and up-to-date is this pattern?"**

```
Scoring Methodology:
├── Repository Analysis:
│   ├── Last commit within 3 months: 1.0
│   ├── Last commit within 6 months: 0.8
│   ├── Last commit within 1 year: 0.6
│   ├── Last commit within 2 years: 0.4
│   └── Last commit > 2 years ago: 0.2
├── Dependency Currency:
│   ├── All dependencies current: +0.2
│   ├── Most dependencies current: +0.1
│   ├── Some dependencies outdated: 0.0
│   └── Many dependencies outdated: -0.1
└── Community Activity:
    ├── Active issues/PRs: +0.1
    ├── Recent releases: +0.1
    └── Maintenance indicators: +0.1
```

**Validation Process**:
```bash
# Currency validation implementation
validate_currency() {
  local pattern_id=$1
  local repository_url=$2
  
  # Check repository recency
  last_commit_date=$(git log -1 --format="%ci" "$repository_url")
  months_since_commit=$(calculate_months_since "$last_commit_date")
  
  # Calculate base currency score
  if [ $months_since_commit -le 3 ]; then
    currency_base=1.0
  elif [ $months_since_commit -le 6 ]; then
    currency_base=0.8
  elif [ $months_since_commit -le 12 ]; then
    currency_base=0.6
  elif [ $months_since_commit -le 24 ]; then
    currency_base=0.4
  else
    currency_base=0.2
  fi
  
  # Check dependency currency
  dependency_score=$(check_dependency_currency "$repository_url")
  
  # Check community activity
  activity_score=$(check_community_activity "$repository_url")
  
  # Calculate final currency score
  currency_score=$(echo "$currency_base + $dependency_score + $activity_score" | bc -l)
  
  echo "Currency Score: $currency_score"
  return $currency_score
}
```

### Relevance Assessment (Weight: 25%)
**"How applicable is this pattern to our deep discovery consultation goals?"**

```
Scoring Criteria:
├── Consultation Alignment:
│   ├── Perfect fit for 30-60 min consultation: 1.0
│   ├── Strong alignment, minor adaptation: 0.8
│   ├── Good alignment, moderate adaptation: 0.6
│   ├── Limited alignment, major adaptation: 0.4
│   └── Poor alignment, minimal value: 0.2
├── Depth Philosophy Support:
│   ├── Strongly supports depth-over-speed: +0.2
│   ├── Somewhat supports depth approach: +0.1
│   ├── Neutral on depth vs speed: 0.0
│   └── Favors speed over depth: -0.2
└── Target Domain Coverage:
    ├── Covers primary target domains: +0.1
    ├── Covers secondary domains: +0.05
    └── Limited domain applicability: 0.0
```

**Validation Process**:
```bash
# Relevance validation implementation
validate_relevance() {
  local pattern_id=$1
  local pattern_description=$2
  local pattern_category=$3
  
  # Assess consultation alignment
  consultation_alignment=$(assess_consultation_fit "$pattern_description" "$pattern_category")
  
  # Check depth philosophy support
  depth_support=$(check_depth_philosophy_alignment "$pattern_description")
  
  # Evaluate domain coverage
  domain_coverage=$(evaluate_domain_applicability "$pattern_category" "$pattern_description")
  
  # Calculate relevance score
  relevance_score=$(echo "$consultation_alignment + $depth_support + $domain_coverage" | bc -l)
  
  echo "Relevance Score: $relevance_score"
  return $relevance_score
}
```

### Authority Assessment (Weight: 20%)
**"How credible and trustworthy is the pattern source?"**

```
Credibility Indicators:
├── Repository Metrics:
│   ├── 1000+ stars: 1.0
│   ├── 500+ stars: 0.8
│   ├── 100+ stars: 0.6
│   ├── 50+ stars: 0.4
│   └── <50 stars: 0.2
├── Maintainer Expertise:
│   ├── Recognized experts in field: +0.2
│   ├── Experienced developers: +0.1
│   ├── Active contributors: +0.05
│   └── Unknown/inactive maintainers: 0.0
├── Community Validation:
│   ├── Strong community engagement: +0.1
│   ├── Regular community feedback: +0.05
│   └── Limited community interaction: 0.0
└── Enterprise Adoption:
    ├── Known enterprise usage: +0.1
    ├── Production deployment evidence: +0.05
    └── No enterprise adoption evidence: 0.0
```

**Validation Process**:
```bash
# Authority validation implementation
validate_authority() {
  local repository_url=$1
  
  # Get repository metrics
  star_count=$(get_github_stars "$repository_url")
  fork_count=$(get_github_forks "$repository_url")
  
  # Calculate base authority from stars
  if [ $star_count -ge 1000 ]; then
    authority_base=1.0
  elif [ $star_count -ge 500 ]; then
    authority_base=0.8
  elif [ $star_count -ge 100 ]; then
    authority_base=0.6
  elif [ $star_count -ge 50 ]; then
    authority_base=0.4
  else
    authority_base=0.2
  fi
  
  # Assess maintainer expertise
  maintainer_score=$(assess_maintainer_expertise "$repository_url")
  
  # Check community validation
  community_score=$(check_community_validation "$repository_url")
  
  # Look for enterprise adoption
  enterprise_score=$(check_enterprise_adoption "$repository_url")
  
  # Calculate final authority score
  authority_score=$(echo "$authority_base + $maintainer_score + $community_score + $enterprise_score" | bc -l)
  
  echo "Authority Score: $authority_score"
  return $authority_score
}
```

### Accuracy Assessment (Weight: 25%)
**"How technically correct and well-implemented is the pattern?"**

```
Technical Quality Indicators:
├── Working Examples:
│   ├── Comprehensive tests passing: 1.0
│   ├── Basic tests passing: 0.8
│   ├── Examples work without tests: 0.6
│   ├── Examples with minor issues: 0.4
│   └── Broken or non-working examples: 0.2
├── Code Quality:
│   ├── Follows best practices consistently: +0.2
│   ├── Generally good code quality: +0.1
│   ├── Mixed code quality: 0.0
│   └── Poor code quality: -0.1
├── Claude Code Compliance:
│   ├── Perfect YAML frontmatter: +0.1
│   ├── Proper tool usage: +0.1
│   ├── Follows Claude Code conventions: +0.1
│   └── Non-compliant structure: -0.2
└── Security Considerations:
    ├── Security best practices followed: +0.1
    ├── Basic security awareness: +0.05
    └── Security issues present: -0.2
```

**Validation Process**:
```bash
# Accuracy validation implementation
validate_accuracy() {
  local pattern_id=$1
  local pattern_file=$2
  local repository_path=$3
  
  # Test working examples
  example_score=$(test_pattern_examples "$pattern_file" "$repository_path")
  
  # Assess code quality
  code_quality_score=$(assess_code_quality "$pattern_file")
  
  # Check Claude Code compliance
  compliance_score=$(check_claude_code_compliance "$pattern_file")
  
  # Security assessment
  security_score=$(assess_security_practices "$pattern_file" "$repository_path")
  
  # Calculate final accuracy score
  accuracy_score=$(echo "$example_score + $code_quality_score + $compliance_score + $security_score" | bc -l)
  
  echo "Accuracy Score: $accuracy_score"
  return $accuracy_score
}
```

### Purpose Assessment (Weight: 15%)
**"How well does the pattern serve intentional, production-ready purposes?"**

```
Intentionality Indicators:
├── Creation Intent:
│   ├── Built for production use: 1.0
│   ├── Built for team/community use: 0.8
│   ├── Built for learning/demonstration: 0.6
│   ├── Built for experimentation: 0.4
│   └── Unclear or poor purpose: 0.2
├── Value Proposition:
│   ├── Clear, significant business value: +0.2
│   ├── Good educational/technical value: +0.1
│   ├── Limited but clear value: +0.05
│   └── Questionable value proposition: -0.1
├── Maintenance Plan:
│   ├── Active, planned maintenance: +0.1
│   ├── Regular maintenance: +0.05
│   ├── Occasional maintenance: 0.0
│   └── No maintenance plan: -0.1
└── Problem-Solution Fit:
    ├── Solves real, significant problems: +0.1
    ├── Addresses common needs: +0.05
    └── Narrow or artificial problem: 0.0
```

**Validation Process**:
```bash
# Purpose validation implementation
validate_purpose() {
  local repository_url=$1
  local readme_content=$2
  local pattern_description=$3
  
  # Assess creation intent from documentation
  creation_intent=$(assess_creation_intent "$readme_content" "$pattern_description")
  
  # Evaluate value proposition
  value_score=$(evaluate_value_proposition "$pattern_description")
  
  # Check maintenance indicators
  maintenance_score=$(check_maintenance_plan "$repository_url")
  
  # Assess problem-solution fit
  problem_solution_score=$(assess_problem_solution_fit "$pattern_description")
  
  # Calculate final purpose score
  purpose_score=$(echo "$creation_intent + $value_score + $maintenance_score + $problem_solution_score" | bc -l)
  
  echo "Purpose Score: $purpose_score"
  return $purpose_score
}
```

## Comprehensive Validation Workflow

### Phase 1: Pre-Validation Setup (2-5 minutes)
```
Validation Preparation:
├── Load pattern(s) from research database
├── Gather evidence sources and repository data
├── Initialize CRAAP framework scoring system
├── Set up validation workspace and logging
├── Configure quality gates and thresholds
└── Prepare cross-reference validation data
```

### Phase 2: Individual CRAAP Assessment (10-20 minutes per pattern)
```
Systematic Validation:
├── Currency: Repository recency, dependency currency, activity
├── Relevance: Consultation alignment, depth philosophy, domain fit
├── Authority: Source credibility, maintainer expertise, community validation
├── Accuracy: Technical correctness, working examples, compliance
├── Purpose: Creation intent, value proposition, problem-solution fit
└── Weighted confidence score calculation
```

### Phase 3: Cross-Reference Validation (5-10 minutes)
```
Relationship Verification:
├── Verify claimed pattern relationships exist
├── Check dependency patterns meet quality thresholds
├── Validate complementary pattern compatibility
├── Identify and resolve relationship conflicts
└── Update relationship confidence scores
```

### Phase 4: Evidence Source Verification (5-15 minutes)
```
Source Quality Assessment:
├── Verify minimum 3-source requirement
├── Check source diversity (different repositories/domains)
├── Validate working examples in evidence
├── Cross-check evidence consistency
└── Document evidence quality metrics
```

### Phase 5: Final Scoring and Decision (3-5 minutes)
```
Quality Gate Assessment:
├── Calculate final weighted confidence score
├── Apply confidence threshold for acceptance/rejection
├── Generate detailed validation report
├── Update research database with validation results
└── Flag patterns requiring improvement or re-validation
```

## Validation Modes and Usage

### Individual Pattern Validation
```bash
# Validate single pattern with detailed analysis
/validate-evidence pattern-commands-component-gen-001 --detailed

# Quick validation with standard threshold
/validate-evidence pattern-agents-orchestrator-002

# Strict validation with high threshold
/validate-evidence pattern-context-hierarchy-003 --threshold=0.85
```

### Batch Validation
```bash
# Validate entire extraction batch
/validate-evidence --batch=priority-web-dev --threshold=0.7

# Validate patterns by category
/validate-evidence --category=commands --threshold=0.75

# Validate patterns by confidence range
/validate-evidence --confidence-range=0.6-0.8 --detailed
```

### Domain-Specific Validation
```bash
# Validate web development patterns
/validate-evidence --domain=web-development --framework=craap

# Validate data science patterns with relaxed threshold
/validate-evidence --domain=data-science --threshold=0.65

# Validate enterprise patterns with strict criteria
/validate-evidence --domain=enterprise --threshold=0.8 --detailed
```

### Re-validation and Quality Improvement
```bash
# Re-validate patterns that failed initial validation
/validate-evidence --status=failed --improve

# Validate patterns with updated evidence
/validate-evidence --recently-updated --framework=craap

# Calibration validation with known high-quality patterns
/validate-evidence --calibration-set --detailed
```

## Quality Improvement System

### Pattern Improvement Workflow
```yaml
pattern_improvement:
  low_currency:
    issue: "Repository not recently updated"
    improvement_actions:
      - "Look for forks with recent activity"
      - "Check for successor repositories"
      - "Verify pattern still applicable with newer tools"
      - "Update implementation for current versions"
    
  low_relevance:
    issue: "Pattern not well-aligned with consultation goals"
    improvement_actions:
      - "Identify adaptation strategies"
      - "Find more relevant usage examples"
      - "Document specific consultation scenarios"
      - "Create bridge patterns for integration"
    
  low_authority:
    issue: "Source lacks credibility indicators"
    improvement_actions:
      - "Seek additional high-authority sources"
      - "Validate with expert review"
      - "Look for enterprise adoption examples"
      - "Check for academic or industry references"
    
  low_accuracy:
    issue: "Technical issues or compliance problems"
    improvement_actions:
      - "Fix working examples and test thoroughly"
      - "Update to Claude Code compliance"
      - "Address security and best practice issues"
      - "Improve documentation and error handling"
    
  low_purpose:
    issue: "Unclear value proposition or intent"
    improvement_actions:
      - "Clarify problem-solution fit"
      - "Document value proposition clearly"
      - "Identify real-world usage scenarios"
      - "Connect to business or technical outcomes"
```

### Validation Calibration System
```bash
# Calibrate validation system with known patterns
calibrate_validation() {
  # Test with high-quality reference patterns
  local reference_patterns=("react-component-generator" "tdd-workflow-automation" "context-hierarchy-navigation")
  
  for pattern in "${reference_patterns[@]}"; do
    echo "Calibrating with reference pattern: $pattern"
    reference_score=$(validate_pattern "$pattern" "reference")
    expected_score=$(get_expected_score "$pattern")
    
    # Check calibration accuracy
    variance=$(echo "$reference_score - $expected_score" | bc -l)
    if (( $(echo "${variance#-} > 0.05" | bc -l) )); then
      echo "WARNING: Validation variance detected for $pattern: $variance"
      adjust_validation_parameters "$pattern" "$variance"
    fi
  done
}
```

## Cross-Reference Validation

### Relationship Verification
```yaml
relationship_validation:
  extends:
    verification: "Base pattern exists and meets quality threshold"
    action: "Verify inheritance relationship is logical"
    confidence_impact: +0.05
    
  conflicts:
    verification: "Conflict is real and documented with resolution"
    action: "Ensure conflict resolution strategy exists"
    confidence_impact: -0.10
    
  complements:
    verification: "Patterns work together effectively"
    action: "Test combined usage scenarios"
    confidence_impact: +0.03
    
  requires:
    verification: "Dependency exists and is accessible"
    action: "Validate dependency chain integrity"
    confidence_impact: 0.00
```

### Relationship Quality Assessment
```bash
# Validate pattern relationships
validate_relationships() {
  local pattern_id=$1
  
  # Get pattern relationships from database
  relationships=$(get_pattern_relationships "$pattern_id")
  
  while IFS=',' read -r related_id relationship_type strength; do
    echo "Validating relationship: $pattern_id -> $related_id ($relationship_type)"
    
    # Verify related pattern exists and meets threshold
    related_confidence=$(get_pattern_confidence "$related_id")
    if (( $(echo "$related_confidence < 0.6" | bc -l) )); then
      echo "WARNING: Low confidence in related pattern: $related_id ($related_confidence)"
      flag_relationship_issue "$pattern_id" "$related_id" "low_confidence_dependency"
    fi
    
    # Validate relationship type logic
    case $relationship_type in
      "extends")
        validate_extension_relationship "$pattern_id" "$related_id"
        ;;
      "conflicts")
        validate_conflict_relationship "$pattern_id" "$related_id"
        ;;
      "complements")
        validate_complementary_relationship "$pattern_id" "$related_id"
        ;;
      "requires")
        validate_dependency_relationship "$pattern_id" "$related_id"
        ;;
    esac
    
  done <<< "$relationships"
}
```

## Error Handling and Quality Assurance

### Validation Error Recovery
```bash
# Handle validation errors gracefully
handle_validation_error() {
  local error_type=$1
  local pattern_id=$2
  local context=$3
  
  case $error_type in
    "missing_evidence")
      echo "ERROR: Insufficient evidence for $pattern_id"
      mark_for_evidence_collection "$pattern_id"
      set_validation_status "$pattern_id" "needs_evidence"
      ;;
    "technical_failure")
      echo "ERROR: Technical validation failed for $pattern_id"
      schedule_manual_review "$pattern_id" "technical_issues"
      set_validation_status "$pattern_id" "technical_review"
      ;;
    "threshold_failure")
      echo "INFO: Pattern $pattern_id below threshold but recoverable"
      suggest_improvements "$pattern_id"
      set_validation_status "$pattern_id" "improvement_needed"
      ;;
    "data_corruption")
      echo "CRITICAL: Data corruption detected for $pattern_id"
      quarantine_pattern "$pattern_id"
      alert_administrators "data_corruption" "$pattern_id"
      ;;
  esac
}
```

### Quality Assurance Checkpoints
```bash
# Comprehensive quality assurance
quality_assurance_check() {
  local validation_session=$1
  
  echo "Running quality assurance for session: $validation_session"
  
  # Check validation completeness
  incomplete_validations=$(find_incomplete_validations "$validation_session")
  if [ -n "$incomplete_validations" ]; then
    echo "WARNING: Incomplete validations found: $incomplete_validations"
    complete_missing_validations "$incomplete_validations"
  fi
  
  # Verify scoring consistency
  scoring_anomalies=$(detect_scoring_anomalies "$validation_session")
  if [ -n "$scoring_anomalies" ]; then
    echo "WARNING: Scoring anomalies detected: $scoring_anomalies"
    review_scoring_anomalies "$scoring_anomalies"
  fi
  
  # Check cross-reference integrity
  reference_issues=$(validate_cross_reference_integrity "$validation_session")
  if [ -n "$reference_issues" ]; then
    echo "WARNING: Cross-reference issues: $reference_issues"
    repair_cross_references "$reference_issues"
  fi
  
  # Generate QA report
  generate_qa_report "$validation_session"
}
```

## Integration with Research Database

### Validation Result Storage
```sql
-- Store CRAAP validation results
INSERT INTO pattern_validations (
  pattern_id,
  validation_date,
  currency_score,
  relevance_score,
  authority_score,
  accuracy_score,
  purpose_score,
  overall_confidence,
  validation_status,
  validator_notes
) VALUES (
  'pattern-cmd-001',
  '2025-08-07T14:30:00Z',
  0.85,
  0.80,
  0.90,
  0.88,
  0.82,
  0.84,
  'accepted',
  'High-quality pattern with excellent working examples'
);
```

### Validation History Tracking
```sql
-- Track validation history for continuous improvement
SELECT 
  pattern_id,
  validation_date,
  overall_confidence,
  validation_status,
  LAG(overall_confidence) OVER (PARTITION BY pattern_id ORDER BY validation_date) as previous_confidence
FROM pattern_validations
WHERE pattern_id = 'pattern-cmd-001'
ORDER BY validation_date DESC;
```

### Aggregate Quality Metrics
```sql
-- Calculate validation success rates and trends
SELECT 
  DATE(validation_date) as validation_day,
  COUNT(*) as patterns_validated,
  AVG(overall_confidence) as avg_confidence,
  COUNT(CASE WHEN validation_status = 'accepted' THEN 1 END) as accepted,
  COUNT(CASE WHEN validation_status = 'rejected' THEN 1 END) as rejected,
  COUNT(CASE WHEN validation_status = 'improvement_needed' THEN 1 END) as needs_improvement
FROM pattern_validations
GROUP BY DATE(validation_date)
ORDER BY validation_day DESC;
```

## Output Deliverables

### Individual Pattern Validation Report
```markdown
# Pattern Validation Report: component-generator-command

## CRAAP Assessment Summary
- **Overall Confidence**: 0.84 (High Confidence)
- **Validation Status**: ACCEPTED
- **Validation Date**: 2025-08-07T14:30:00Z

## Detailed Scores
### Currency: 0.85 (Excellent)
- Repository updated 2 months ago
- All dependencies current
- Active community engagement

### Relevance: 0.80 (Strong)
- Perfect alignment with consultation goals
- Strongly supports depth-over-speed philosophy
- Applicable to web development domain

### Authority: 0.90 (Excellent)
- 2,500+ GitHub stars
- Recognized React experts as maintainers
- Strong community validation

### Accuracy: 0.88 (Excellent)
- Working examples with comprehensive tests
- Follows Claude Code best practices
- Security considerations addressed

### Purpose: 0.82 (Strong)
- Built for production use
- Clear business value proposition
- Active maintenance plan

## Cross-Reference Validation
- 3 relationships validated successfully
- No dependency conflicts detected
- Strong complementary patterns identified

## Recommendations
- **Action**: Include in consultation system immediately
- **Priority**: High (supports core web development scenarios)
- **Integration**: Recommend for component generation workflows
```

### Batch Validation Summary
```markdown
# Batch Validation Report: Priority Web Development

## Executive Summary
- **Patterns Validated**: 67
- **Accepted**: 52 (78%)
- **Needs Improvement**: 12 (18%)
- **Rejected**: 3 (4%)
- **Average Confidence**: 0.76

## Quality Distribution
### High Confidence (0.8+): 29 patterns (43%)
- Ready for immediate consultation use
- Strong evidence base and validation scores

### Medium Confidence (0.7-0.8): 23 patterns (34%)
- Suitable for consultation with notes
- Minor improvements recommended

### Low Confidence (0.6-0.7): 12 patterns (18%)
- Require improvement before use
- Evidence collection or technical fixes needed

### Below Threshold (<0.6): 3 patterns (4%)
- Rejected from consultation system
- Major issues requiring resolution

## Validation Issues Summary
### Most Common Issues:
1. **Currency**: 8 patterns with outdated dependencies
2. **Accuracy**: 5 patterns with technical compliance issues
3. **Evidence**: 4 patterns with insufficient source diversity
4. **Authority**: 2 patterns from low-credibility sources

## Recommendations
- **Immediate Use**: 52 accepted patterns ready for integration
- **Improvement Queue**: 12 patterns flagged for enhancement
- **Re-validation**: Schedule quarterly validation updates
```

## Success Criteria and Quality Metrics

### Quantitative Targets
- **Validation Accuracy**: 95%+ patterns meeting stated confidence levels in practice
- **Acceptance Rate**: 75%+ patterns meeting minimum threshold (0.7)
- **High Confidence Rate**: 40%+ patterns achieving high confidence (0.8+)
- **False Positive Rate**: <5% accepted patterns failing in consultation
- **False Negative Rate**: <3% rejected patterns that would succeed

### Qualitative Indicators
- Patterns consistently support consultation goals
- Evidence validation prevents low-quality pattern inclusion
- Cross-reference validation maintains relationship integrity
- Continuous improvement increases validation accuracy over time
- Stakeholder confidence in pattern quality and selection

---

**Remember**: Rigorous validation is the foundation of reliable consultation. Every pattern that passes CRAAP validation has earned its place through evidence, not assumption. Quality assurance at this stage prevents consultation failures later.