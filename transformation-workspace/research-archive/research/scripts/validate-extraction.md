# Pattern Extraction Validation Command
---
name: validate-extraction  
description: Validate quality and completeness of extracted patterns
usage: "/validate-extraction [pattern-id] [validation-type]"
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, LS]
category: research
---

## Command Purpose
This command performs comprehensive validation of extracted patterns to ensure they meet quality standards, have sufficient evidence, and will contribute meaningfully to the deep discovery consultation system.

## Parameters
- **pattern-id** (required): Specific pattern ID to validate (e.g., "pattern-commands-component-generator-20250807")
- **validation-type** (optional): Type of validation ("quality", "evidence", "craap", "cross-ref", "all")

## Validation Framework

### Step 1: Pattern Record Location & Loading
```bash
echo "🔍 Locating Pattern Record: $1"
echo "==============================================="

# Find pattern in research database
PATTERN_FILE=$(find .claude-architect/research -name "*$1*" -type f)

if [[ -z "$PATTERN_FILE" ]]; then
    # Search in database entries
    PATTERN_ENTRY=$(grep -l "$1" .claude-architect/research/research-database-entries.yaml 2>/dev/null)
    
    if [[ -n "$PATTERN_ENTRY" ]]; then
        echo "✅ Pattern found in database: $PATTERN_ENTRY"
    else
        echo "❌ Pattern not found: $1"
        echo "Available patterns:"
        grep "pattern_id:" .claude-architect/research/research-database-entries.yaml | head -10
        exit 1
    fi
else
    echo "✅ Pattern file found: $PATTERN_FILE"
fi

# Extract pattern metadata
PATTERN_CATEGORY=$(grep "category:" "$PATTERN_FILE" | cut -d' ' -f2)
PATTERN_CONFIDENCE=$(grep "overall_confidence:" "$PATTERN_FILE" | cut -d' ' -f2)
EXTRACTION_DATE=$(grep "extraction_date:" "$PATTERN_FILE" | cut -d' ' -f2)

echo "📊 Pattern Metadata:"
echo "  Category: $PATTERN_CATEGORY"
echo "  Confidence: $PATTERN_CONFIDENCE"
echo "  Extracted: $EXTRACTION_DATE"
```

### Step 2: Evidence Strength Validation
```bash
echo ""
echo "📋 Evidence Strength Validation:"
echo "==============================================="

# Count evidence sources
SOURCE_COUNT=$(grep -c "repository:" "$PATTERN_FILE")
echo "📊 Evidence Sources: $SOURCE_COUNT"

# Minimum requirement check
if [[ $SOURCE_COUNT -lt 3 ]]; then
    echo "⚠️  WARNING: Below minimum evidence requirement (3 sources)"
    EVIDENCE_SCORE=0.3
elif [[ $SOURCE_COUNT -lt 5 ]]; then
    echo "✅ Meets minimum evidence requirement"
    EVIDENCE_SCORE=0.6
else
    echo "🌟 Exceeds evidence requirements"
    EVIDENCE_SCORE=0.9
fi

# Check source diversity
UNIQUE_REPOS=$(grep "repository:" "$PATTERN_FILE" | sort | uniq | wc -l)
DIVERSITY_RATIO=$(echo "scale=2; $UNIQUE_REPOS / $SOURCE_COUNT" | bc)

echo "🎯 Source Diversity: $DIVERSITY_RATIO (unique: $UNIQUE_REPOS / total: $SOURCE_COUNT)"

if (( $(echo "$DIVERSITY_RATIO >= 0.8" | bc -l) )); then
    echo "✅ High source diversity"
    DIVERSITY_SCORE=0.9
elif (( $(echo "$DIVERSITY_RATIO >= 0.6" | bc -l) )); then
    echo "✅ Good source diversity"  
    DIVERSITY_SCORE=0.7
else
    echo "⚠️  Low source diversity - consider additional sources"
    DIVERSITY_SCORE=0.4
fi

# Check source authority (would integrate with repository metadata)
echo "🏛️ Source Authority Analysis:"
HIGH_AUTHORITY=0
MEDIUM_AUTHORITY=0
LOW_AUTHORITY=0

# This would check actual repository statistics
grep "repository:" "$PATTERN_FILE" | while read -r repo_line; do
    REPO_NAME=$(echo "$repo_line" | cut -d' ' -f2)
    echo "  📊 Checking authority of: $REPO_NAME"
    
    # Placeholder for authority scoring
    # Would check stars, forks, maintenance activity
    echo "    ⭐ Authority: Medium (placeholder)"
done

AUTHORITY_SCORE=0.7  # Placeholder calculation
```

### Step 3: CRAAP Framework Validation
```bash
echo ""
echo "🧪 CRAAP Framework Validation:"
echo "==============================================="

# Currency Assessment
CURRENCY_SCORE=$(grep "currency_score:" "$PATTERN_FILE" | cut -d' ' -f2)
echo "📅 Currency Score: $CURRENCY_SCORE"

if (( $(echo "$CURRENCY_SCORE >= 0.8" | bc -l) )); then
    echo "  ✅ Very current (recent updates)"
elif (( $(echo "$CURRENCY_SCORE >= 0.6" | bc -l) )); then
    echo "  ✅ Reasonably current"
else
    echo "  ⚠️  May be outdated - verify recent applicability"
fi

# Relevance Assessment  
RELEVANCE_SCORE=$(grep "relevance_score:" "$PATTERN_FILE" | cut -d' ' -f2)
echo "🎯 Relevance Score: $RELEVANCE_SCORE"

if (( $(echo "$RELEVANCE_SCORE >= 0.8" | bc -l) )); then
    echo "  ✅ Highly relevant to consultation system"
else
    echo "  ⚠️  Consider relevance alignment with 30-60min consultation goal"
fi

# Authority Assessment
AUTHORITY_SCORE=$(grep "authority_score:" "$PATTERN_FILE" | cut -d' ' -f2)  
echo "🏛️ Authority Score: $AUTHORITY_SCORE"

# Accuracy Assessment
ACCURACY_SCORE=$(grep "accuracy_score:" "$PATTERN_FILE" | cut -d' ' -f2)
echo "✅ Accuracy Score: $ACCURACY_SCORE"

if (( $(echo "$ACCURACY_SCORE < 0.6" | bc -l) )); then
    echo "  ❌ CRITICAL: Accuracy below threshold - pattern may be unreliable"
    ACCURACY_ISSUES=true
else
    ACCURACY_ISSUES=false
fi

# Purpose Assessment
PURPOSE_SCORE=$(grep "purpose_score:" "$PATTERN_FILE" | cut -d' ' -f2)
echo "🎪 Purpose Score: $PURPOSE_SCORE"

# Calculate CRAAP composite score
CRAAP_COMPOSITE=$(echo "scale=2; ($CURRENCY_SCORE + $RELEVANCE_SCORE + $AUTHORITY_SCORE + $ACCURACY_SCORE + $PURPOSE_SCORE) / 5" | bc)
echo "📊 CRAAP Composite Score: $CRAAP_COMPOSITE"
```

### Step 4: Implementation Quality Validation  
```bash
echo ""
echo "🔧 Implementation Quality Validation:"
echo "==============================================="

# Check for working examples
WORKING_EXAMPLES=$(grep "working_examples:" "$PATTERN_FILE" | cut -d' ' -f2)
echo "💻 Working Examples: $WORKING_EXAMPLES"

if [[ "$WORKING_EXAMPLES" == "yes" ]]; then
    echo "  ✅ Has working implementation examples"
    IMPLEMENTATION_SCORE=0.8
else
    echo "  ⚠️  Missing working examples - limits practical applicability"
    IMPLEMENTATION_SCORE=0.3
fi

# Check documentation quality
DOC_QUALITY=$(grep "documentation_quality:" "$PATTERN_FILE" | cut -d' ' -f2)
echo "📚 Documentation Quality: $DOC_QUALITY"

case $DOC_QUALITY in
    "good")
        DOC_SCORE=0.9
        echo "  ✅ Excellent documentation"
        ;;
    "fair") 
        DOC_SCORE=0.6
        echo "  ✅ Adequate documentation"
        ;;
    "poor")
        DOC_SCORE=0.3
        echo "  ⚠️  Poor documentation - may hinder adoption"
        ;;
    *)
        DOC_SCORE=0.5
        echo "  ❓ Documentation quality not assessed"
        ;;
esac

# Check community validation
COMMUNITY_VALIDATION=$(grep "community_validation:" "$PATTERN_FILE" | cut -d' ' -f2)
echo "👥 Community Validation: $COMMUNITY_VALIDATION"

IMPLEMENTATION_COMPOSITE=$(echo "scale=2; ($IMPLEMENTATION_SCORE + $DOC_SCORE) / 2" | bc)
echo "📊 Implementation Quality Score: $IMPLEMENTATION_COMPOSITE"
```

### Step 5: Cross-Reference Validation
```bash
echo ""
echo "🔗 Cross-Reference Validation:"
echo "==============================================="

# Count cross-references
CROSS_REF_COUNT=$(grep -c "pattern_id:" "$PATTERN_FILE" | grep -v "^pattern_id:")
echo "🔗 Cross-References Found: $CROSS_REF_COUNT"

if [[ $CROSS_REF_COUNT -lt 2 ]]; then
    echo "⚠️  Below minimum cross-reference requirement (2 references)"
    CROSS_REF_SCORE=0.3
elif [[ $CROSS_REF_COUNT -lt 4 ]]; then
    echo "✅ Meets cross-reference requirements" 
    CROSS_REF_SCORE=0.7
else
    echo "🌟 Rich cross-reference network"
    CROSS_REF_SCORE=0.9
fi

# Validate cross-reference quality
echo "🔍 Cross-Reference Quality Analysis:"

grep "relationship:" "$PATTERN_FILE" | while read -r rel_line; do
    RELATIONSHIP=$(echo "$rel_line" | cut -d' ' -f2)
    echo "  🔗 Relationship type: $RELATIONSHIP"
    
    case $RELATIONSHIP in
        "extends"|"complements"|"requires")
            echo "    ✅ Strong relationship"
            ;;
        "conflicts")
            echo "    ⚠️  Conflict relationship - ensure properly documented"
            ;;
        *)
            echo "    ❓ Relationship type unclear"
            ;;
    esac
done
```

### Step 6: Confidence Score Validation
```bash
echo ""
echo "📊 Confidence Score Validation:"
echo "==============================================="

# Extract all confidence components
EVIDENCE_CONFIDENCE=$(echo "scale=2; ($EVIDENCE_SCORE + $DIVERSITY_SCORE + $AUTHORITY_SCORE) / 3" | bc)
VALIDATION_CONFIDENCE=$CRAAP_COMPOSITE
IMPLEMENTATION_CONFIDENCE=$IMPLEMENTATION_COMPOSITE

echo "📋 Confidence Breakdown:"
echo "  Evidence Strength: $EVIDENCE_CONFIDENCE"
echo "  CRAAP Validation: $VALIDATION_CONFIDENCE"  
echo "  Implementation Quality: $IMPLEMENTATION_CONFIDENCE"

# Calculate overall confidence
CALCULATED_CONFIDENCE=$(echo "scale=2; ($EVIDENCE_CONFIDENCE * 0.4 + $VALIDATION_CONFIDENCE * 0.4 + $IMPLEMENTATION_CONFIDENCE * 0.2)" | bc)
STORED_CONFIDENCE=$(grep "overall_confidence:" "$PATTERN_FILE" | cut -d' ' -f2)

echo "🎯 Calculated Confidence: $CALCULATED_CONFIDENCE"
echo "💾 Stored Confidence: $STORED_CONFIDENCE"

# Check for significant discrepancy
CONFIDENCE_DIFF=$(echo "scale=2; $CALCULATED_CONFIDENCE - $STORED_CONFIDENCE" | bc)
if (( $(echo "${CONFIDENCE_DIFF#-} > 0.1" | bc -l) )); then
    echo "⚠️  Confidence discrepancy detected - recommend recalculation"
fi
```

### Step 7: Quality Gate Assessment
```bash
echo ""
echo "🚪 Quality Gate Assessment:"
echo "==============================================="

GATES_PASSED=()
GATES_FAILED=()

# Gate 1: Minimum Evidence Sources
if [[ $SOURCE_COUNT -ge 3 ]]; then
    GATES_PASSED+=("minimum_evidence")
    echo "✅ Gate 1: Minimum Evidence Sources"
else
    GATES_FAILED+=("minimum_evidence")
    echo "❌ Gate 1: FAILED - Insufficient evidence sources"
fi

# Gate 2: Confidence Threshold
if (( $(echo "$CALCULATED_CONFIDENCE >= 0.6" | bc -l) )); then
    GATES_PASSED+=("confidence_threshold")
    echo "✅ Gate 2: Confidence Threshold"
else
    GATES_FAILED+=("confidence_threshold") 
    echo "❌ Gate 2: FAILED - Below confidence threshold"
fi

# Gate 3: CRAAP Validation Complete
if (( $(echo "$CRAAP_COMPOSITE > 0.5" | bc -l) )); then
    GATES_PASSED+=("craap_validation")
    echo "✅ Gate 3: CRAAP Validation"
else
    GATES_FAILED+=("craap_validation")
    echo "❌ Gate 3: FAILED - CRAAP validation insufficient"
fi

# Gate 4: Cross-References
if [[ $CROSS_REF_COUNT -ge 2 ]]; then
    GATES_PASSED+=("cross_references")
    echo "✅ Gate 4: Cross-References"
else
    GATES_FAILED+=("cross_references")
    echo "❌ Gate 4: FAILED - Insufficient cross-references"
fi

# Gate 5: Implementation Evidence
if [[ "$WORKING_EXAMPLES" == "yes" ]]; then
    GATES_PASSED+=("implementation_evidence")
    echo "✅ Gate 5: Implementation Evidence"
else
    GATES_FAILED+=("implementation_evidence")
    echo "⚠️  Gate 5: WARNING - Missing implementation evidence"
fi

TOTAL_GATES=${#GATES_PASSED[@]}
TOTAL_POSSIBLE=5

echo ""
echo "📊 Quality Gates Summary:"
echo "  Passed: $TOTAL_GATES / $TOTAL_POSSIBLE"
echo "  Passed Gates: ${GATES_PASSED[*]}"
if [[ ${#GATES_FAILED[@]} -gt 0 ]]; then
    echo "  Failed Gates: ${GATES_FAILED[*]}"
fi
```

### Step 8: Recommendations & Action Items
```bash
echo ""
echo "💡 Recommendations & Action Items:"
echo "==============================================="

# Generate specific recommendations based on validation results
RECOMMENDATIONS=()

if [[ $SOURCE_COUNT -lt 3 ]]; then
    RECOMMENDATIONS+=("Seek additional evidence sources to meet minimum requirement")
fi

if (( $(echo "$CALCULATED_CONFIDENCE < 0.7" | bc -l) )); then
    RECOMMENDATIONS+=("Improve evidence quality or seek higher-authority sources")
fi

if [[ "$WORKING_EXAMPLES" != "yes" ]]; then
    RECOMMENDATIONS+=("Locate or create working implementation examples")
fi

if [[ $CROSS_REF_COUNT -lt 3 ]]; then
    RECOMMENDATIONS+=("Identify additional cross-references with related patterns")
fi

if (( $(echo "$CURRENCY_SCORE < 0.6" | bc -l) )); then
    RECOMMENDATIONS+=("Verify pattern relevance with recent Claude Code developments")
fi

# Output recommendations
if [[ ${#RECOMMENDATIONS[@]} -eq 0 ]]; then
    echo "✅ No critical issues identified - pattern meets quality standards"
else
    echo "📋 Action Items:"
    for rec in "${RECOMMENDATIONS[@]}"; do
        echo "  • $rec"
    done
fi
```

### Step 9: Validation Report Generation
```bash
echo ""
echo "📄 Generating Validation Report:"
echo "==============================================="

VALIDATION_REPORT="validation-report-$1-$(date +%Y%m%d).md"

cat << EOF > ".claude-architect/research/$VALIDATION_REPORT"
# Pattern Validation Report: $1

## Validation Summary
- **Pattern ID**: $1
- **Category**: $PATTERN_CATEGORY
- **Validation Date**: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
- **Overall Status**: $(if [[ ${#GATES_FAILED[@]} -eq 0 ]]; then echo "PASSED"; else echo "NEEDS IMPROVEMENT"; fi)

## Evidence Assessment
- **Source Count**: $SOURCE_COUNT (requirement: ≥3)
- **Source Diversity**: $DIVERSITY_RATIO
- **Evidence Score**: $EVIDENCE_CONFIDENCE

## CRAAP Framework Results
- **Currency**: $CURRENCY_SCORE
- **Relevance**: $RELEVANCE_SCORE  
- **Authority**: $AUTHORITY_SCORE
- **Accuracy**: $ACCURACY_SCORE
- **Purpose**: $PURPOSE_SCORE
- **Composite**: $CRAAP_COMPOSITE

## Quality Gates
- **Passed**: $TOTAL_GATES / $TOTAL_POSSIBLE
- **Passed Gates**: ${GATES_PASSED[*]}
$(if [[ ${#GATES_FAILED[@]} -gt 0 ]]; then echo "- **Failed Gates**: ${GATES_FAILED[*]}"; fi)

## Confidence Analysis
- **Calculated**: $CALCULATED_CONFIDENCE
- **Stored**: $STORED_CONFIDENCE
- **Assessment**: $(if (( $(echo "$CALCULATED_CONFIDENCE >= 0.8" | bc -l) )); then echo "High confidence"; elif (( $(echo "$CALCULATED_CONFIDENCE >= 0.6" | bc -l) )); then echo "Acceptable confidence"; else echo "Below threshold"; fi)

$(if [[ ${#RECOMMENDATIONS[@]} -gt 0 ]]; then
echo "## Recommendations"
for rec in "${RECOMMENDATIONS[@]}"; do
    echo "- $rec"
done
fi)

## Next Steps
$(if [[ ${#GATES_FAILED[@]} -eq 0 ]]; then
echo "- Pattern approved for inclusion in consultation system"
echo "- Consider for high-priority pattern database"
else
echo "- Address failed quality gates before approval"  
echo "- Revalidate after improvements"
fi)

---
Generated by Pattern Validation Engine v1.0
EOF

echo "📄 Validation report saved: $VALIDATION_REPORT"
```

### Step 10: Validation Summary
```bash
echo ""
echo "🎯 Validation Summary:"
echo "==============================================="
echo "Pattern: $1"
echo "Status: $(if [[ ${#GATES_FAILED[@]} -eq 0 ]]; then echo "✅ APPROVED"; else echo "⚠️  NEEDS IMPROVEMENT"; fi)"
echo "Quality Gates: $TOTAL_GATES / $TOTAL_POSSIBLE"
echo "Confidence: $CALCULATED_CONFIDENCE"
echo "Report: $VALIDATION_REPORT"
echo ""
if [[ ${#GATES_FAILED[@]} -eq 0 ]]; then
    echo "✅ Pattern validation complete - ready for consultation system!"
else
    echo "⚠️  Pattern requires improvement before approval"
fi
```

## Usage Examples

### Comprehensive Validation
```bash
/validate-extraction pattern-commands-component-generator-20250807 all
```

### Specific Validation Types
```bash
/validate-extraction pattern-agents-orchestrator-20250807 quality
/validate-extraction pattern-context-hierarchy-20250807 evidence  
/validate-extraction pattern-workflows-tdd-20250807 craap
```

## Quality Standards

### Minimum Requirements
- Evidence sources: ≥3
- Confidence score: ≥0.6
- CRAAP validation: Complete
- Cross-references: ≥2

### Excellence Thresholds  
- Evidence sources: ≥5
- Confidence score: ≥0.8
- Implementation examples: Required
- Community validation: Positive

This validation command ensures only high-quality, evidence-based patterns enter our deep discovery consultation system.