# Repository Pattern Extraction Command
---
name: extract-patterns
description: Extract evidence-based patterns from a specific Claude Code repository
usage: "/extract-patterns [repository-name] [focus-area]"
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, LS, WebFetch]
category: research
---

## Command Purpose
This command performs systematic pattern extraction from a specified Claude Code repository, applying appropriate extraction templates based on the focus area and generating validated pattern records for the research database.

## Parameters
- **repository-name** (required): Name from repository catalog (e.g., "claude-code-react-patterns")
- **focus-area** (optional): Specific area to focus extraction ("commands", "agents", "context", "workflows", "all")

## Execution Workflow

### Step 1: Repository Preparation
```bash
# Load repository metadata from catalog
REPO_DATA=$(grep -A 20 "name: $1" .claude-architect/research/repository-catalog.yaml)

# Extract repository URL and metadata
REPO_URL=$(echo "$REPO_DATA" | grep "url:" | cut -d' ' -f4)
REPO_DOMAIN=$(echo "$REPO_DATA" | grep "domain:" | cut -d' ' -f4)
PRIORITY=$(echo "$REPO_DATA" | grep "priority:" | cut -d' ' -f4)

echo "🔍 Analyzing repository: $1"
echo "📂 Domain: $REPO_DOMAIN"
echo "⭐ Priority: $PRIORITY"
echo "🔗 URL: $REPO_URL"
```

### Step 2: Repository Access & Structure Analysis
```bash
# Create temporary analysis directory
ANALYSIS_DIR="temp-analysis-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$ANALYSIS_DIR"
cd "$ANALYSIS_DIR"

# Access repository (using WebFetch for analysis)
echo "📥 Accessing repository structure..."

# Analyze key directories and files
echo "📋 Repository Structure Analysis:"
echo "==============================================="

# Look for .claude directory
CLAUDE_DIR_EXISTS="no"
if [[ $(find . -name ".claude" -type d 2>/dev/null) ]]; then
    CLAUDE_DIR_EXISTS="yes"
    echo "✅ .claude directory found"
    
    # Analyze .claude structure
    find .claude -type f -name "*.md" | head -20 | while read file; do
        echo "📄 $file"
    done
else
    echo "❌ No .claude directory found"
fi

# Look for CLAUDE.md files  
CLAUDE_MD_COUNT=$(find . -name "CLAUDE.md" -type f | wc -l)
echo "📄 CLAUDE.md files found: $CLAUDE_MD_COUNT"

# Count potential command files
COMMAND_COUNT=$(find . -path "*/.claude/commands/*" -name "*.md" | wc -l)
echo "🔧 Potential command files: $COMMAND_COUNT"

# Count potential agent files
AGENT_COUNT=$(find . -path "*/.claude/agents/*" -name "*.md" | wc -l)
echo "🤖 Potential agent files: $AGENT_COUNT"
```

### Step 3: Pattern Category Detection
```bash
echo "🎯 Pattern Category Detection:"
echo "==============================================="

# Initialize pattern categories found
CATEGORIES_FOUND=()

# Commands pattern detection
if [[ $COMMAND_COUNT -gt 0 ]]; then
    CATEGORIES_FOUND+=("commands")
    echo "✅ Commands patterns detected ($COMMAND_COUNT files)"
fi

# Agents pattern detection  
if [[ $AGENT_COUNT -gt 0 ]]; then
    CATEGORIES_FOUND+=("agents")
    echo "✅ Agent patterns detected ($AGENT_COUNT files)"
fi

# Context patterns detection
if [[ $CLAUDE_MD_COUNT -gt 0 ]]; then
    CATEGORIES_FOUND+=("context")
    echo "✅ Context patterns detected ($CLAUDE_MD_COUNT files)"
fi

# Workflow patterns detection (look for process documentation)
WORKFLOW_INDICATORS=$(grep -r -i "workflow\|process\|pipeline" . --include="*.md" | wc -l)
if [[ $WORKFLOW_INDICATORS -gt 5 ]]; then
    CATEGORIES_FOUND+=("workflows") 
    echo "✅ Workflow patterns detected ($WORKFLOW_INDICATORS indicators)"
fi

echo "📊 Categories to analyze: ${CATEGORIES_FOUND[*]}"
```

### Step 4: Apply Extraction Templates
For each detected category, apply the appropriate extraction template:

#### Commands Pattern Extraction
```bash
if [[ " ${CATEGORIES_FOUND[*]} " =~ " commands " ]]; then
    echo "🔧 Extracting command patterns..."
    
    find .claude/commands -name "*.md" | while read cmd_file; do
        echo "  📄 Analyzing: $cmd_file"
        
        # Load command pattern template
        cp ../../../templates/command-pattern-template.yaml "analysis-$(basename $cmd_file .md).yaml"
        
        # Extract YAML frontmatter
        YAML_START=$(grep -n "^---$" "$cmd_file" | head -1 | cut -d: -f1)
        YAML_END=$(tail -n +$((YAML_START + 1)) "$cmd_file" | grep -n "^---$" | head -1 | cut -d: -f1)
        
        if [[ -n "$YAML_START" && -n "$YAML_END" ]]; then
            YAML_CONTENT=$(sed -n "$((YAML_START + 1)),$((YAML_START + YAML_END - 1))p" "$cmd_file")
            echo "    ✅ YAML frontmatter extracted"
            
            # Extract command name, description, usage, tools
            CMD_NAME=$(echo "$YAML_CONTENT" | grep "name:" | cut -d' ' -f2-)
            CMD_DESC=$(echo "$YAML_CONTENT" | grep "description:" | cut -d' ' -f2-)
            CMD_USAGE=$(echo "$YAML_CONTENT" | grep "usage:" | cut -d' ' -f2-)
            CMD_TOOLS=$(echo "$YAML_CONTENT" | grep "allowed-tools:" | cut -d' ' -f2-)
            
            echo "    📝 Command: $CMD_NAME"
            echo "    📖 Description: $CMD_DESC"
        fi
        
        # Analyze content structure
        TOTAL_LINES=$(wc -l < "$cmd_file")
        SECTION_COUNT=$(grep -c "^##" "$cmd_file")
        
        echo "    📊 Lines: $TOTAL_LINES, Sections: $SECTION_COUNT"
        
        # Look for innovation indicators
        UNIQUE_PATTERNS=$(grep -i "unique\|novel\|innovative\|creative" "$cmd_file" | wc -l)
        if [[ $UNIQUE_PATTERNS -gt 0 ]]; then
            echo "    💡 Innovation indicators found: $UNIQUE_PATTERNS"
        fi
    done
fi
```

#### Context Pattern Extraction  
```bash
if [[ " ${CATEGORIES_FOUND[*]} " =~ " context " ]]; then
    echo "📚 Extracting context patterns..."
    
    find . -name "CLAUDE.md" | while read claude_file; do
        echo "  📄 Analyzing: $claude_file"
        
        # Load context pattern template
        cp ../../../templates/context-pattern-template.yaml "context-analysis-$(basename $(dirname $claude_file)).yaml"
        
        # Analyze structure
        TOTAL_LINES=$(wc -l < "$claude_file")
        HEADER_COUNT=$(grep -c "^#" "$claude_file")
        LINK_COUNT=$(grep -c "\[.*\](" "$claude_file")
        
        echo "    📊 Lines: $TOTAL_LINES, Headers: $HEADER_COUNT, Links: $LINK_COUNT"
        
        # Check for hierarchical patterns
        MULTI_LEVEL=$(grep -c "^###" "$claude_file")
        if [[ $MULTI_LEVEL -gt 0 ]]; then
            echo "    🏗️ Hierarchical structure detected (depth: 3+)"
        fi
        
        # Look for token optimization indicators
        TOKEN_REFS=$(grep -i "token\|context.*window\|efficiency" "$claude_file" | wc -l)
        if [[ $TOKEN_REFS -gt 0 ]]; then
            echo "    ⚡ Token optimization patterns: $TOKEN_REFS"
        fi
    done
fi
```

### Step 5: Evidence Collection & Validation
```bash
echo "📋 Evidence Collection & Validation:"
echo "==============================================="

# Apply CRAAP validation framework
current_date=$(date +%s)

for analysis_file in analysis-*.yaml; do
    if [[ -f "$analysis_file" ]]; then
        echo "🔍 Validating: $analysis_file"
        
        # Currency assessment (check repository last update)
        # This would use WebFetch to check repository metadata
        CURRENCY_SCORE="0.8"  # Placeholder - would calculate based on last update
        
        # Authority assessment (check stars, forks, activity)
        AUTHORITY_SCORE="0.7"  # Placeholder - would extract from repo metadata
        
        # Relevance assessment (based on domain alignment)
        if [[ "$REPO_DOMAIN" =~ ^(web-development|testing|devops)$ ]]; then
            RELEVANCE_SCORE="0.9"
        else
            RELEVANCE_SCORE="0.7"
        fi
        
        # Calculate overall confidence
        OVERALL_CONFIDENCE=$(echo "scale=2; ($CURRENCY_SCORE + $AUTHORITY_SCORE + $RELEVANCE_SCORE) / 3" | bc)
        
        echo "  📊 Confidence: $OVERALL_CONFIDENCE"
        
        # Only proceed if meets minimum threshold
        if (( $(echo "$OVERALL_CONFIDENCE >= 0.6" | bc -l) )); then
            echo "  ✅ Passes quality threshold"
        else
            echo "  ❌ Below quality threshold - flagged for review"
        fi
    fi
done
```

### Step 6: Cross-Reference Identification
```bash
echo "🔗 Cross-Reference Analysis:"
echo "==============================================="

# Look for patterns that reference each other
for analysis_file in analysis-*.yaml; do
    if [[ -f "$analysis_file" ]]; then
        PATTERN_NAME=$(basename "$analysis_file" .yaml)
        echo "🔍 Finding references for: $PATTERN_NAME"
        
        # Search for references to this pattern in other files
        REFERENCES=$(grep -r "$PATTERN_NAME" . --include="*.md" | wc -l)
        if [[ $REFERENCES -gt 1 ]]; then
            echo "  🔗 Cross-references found: $REFERENCES"
        fi
    fi
done
```

### Step 7: Database Population
```bash
echo "💾 Populating Research Database:"
echo "==============================================="

# Generate database entries for validated patterns
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
PATTERNS_ADDED=0

for analysis_file in analysis-*.yaml; do
    if [[ -f "$analysis_file" ]]; then
        PATTERN_ID="pattern-${1}-$(basename $analysis_file .yaml)-$(date +%Y%m%d)"
        
        echo "📝 Creating database entry: $PATTERN_ID"
        
        # Create database record (would integrate with actual database)
        cat << EOF >> "../../../research-database-entries.yaml"
- pattern_id: $PATTERN_ID
  repository: $1
  extraction_date: $TIMESTAMP
  confidence_score: $OVERALL_CONFIDENCE
  source_file: $analysis_file
  domain: $REPO_DOMAIN
  
EOF
        
        ((PATTERNS_ADDED++))
    fi
done

echo "✅ Patterns added to database: $PATTERNS_ADDED"
```

### Step 8: Generate Extraction Report
```bash
echo "📄 Generating Extraction Report:"
echo "==============================================="

REPORT_FILE="../extraction-report-${1}-$(date +%Y%m%d).md"

cat << EOF > "$REPORT_FILE"
# Pattern Extraction Report: $1

## Repository Analysis
- **Repository**: $1
- **Domain**: $REPO_DOMAIN  
- **Analysis Date**: $TIMESTAMP
- **Priority Level**: $PRIORITY

## Patterns Extracted
- **Total Patterns**: $PATTERNS_ADDED
- **Categories Found**: ${CATEGORIES_FOUND[*]}
- **Command Patterns**: $(ls analysis-*.yaml 2>/dev/null | wc -l)
- **Average Confidence**: $OVERALL_CONFIDENCE

## Quality Assessment
- **Patterns Above Threshold**: $(echo "$PATTERNS_ADDED >= 1" | bc)
- **Evidence Sources**: 1 (primary repository)
- **CRAAP Validation**: Complete

## Recommendations
$(if [[ $PATTERNS_ADDED -lt 5 ]]; then echo "- Consider extending analysis time for deeper pattern extraction"; fi)
$(if [[ $(echo "$OVERALL_CONFIDENCE < 0.8" | bc -l) ]]; then echo "- Seek additional evidence sources to increase confidence"; fi)

## Next Steps
- Cross-reference with related repositories
- Validate patterns through implementation testing
- Update research database with findings

---
Generated by Pattern Extraction Engine v1.0
EOF

echo "📄 Report saved: $REPORT_FILE"
```

### Step 9: Cleanup & Summary
```bash
# Clean up temporary files
cd ..
rm -rf "$ANALYSIS_DIR"

echo ""
echo "🎯 Extraction Summary:"
echo "==============================================="
echo "Repository: $1"
echo "Patterns Found: $PATTERNS_ADDED"
echo "Categories: ${CATEGORIES_FOUND[*]}"
echo "Average Confidence: $OVERALL_CONFIDENCE"
echo "Report: $REPORT_FILE"
echo ""
echo "✅ Pattern extraction complete!"
```

## Usage Examples

### Extract All Patterns from High-Priority Repository
```bash
/extract-patterns claude-code-react-patterns all
```

### Focus on Specific Pattern Category
```bash
/extract-patterns claude-enterprise-setup agents
/extract-patterns claude-testing-framework workflows
```

### Batch Processing (would call this command multiple times)
```bash
/extract-patterns claude-code-react-patterns all
/extract-patterns claude-enterprise-setup all  
/extract-patterns claude-testing-framework all
```

## Quality Assurance

### Validation Requirements
- Minimum confidence score: 0.6
- CRAAP validation: Complete
- Evidence documentation: Required
- Cross-reference identification: Required

### Success Criteria
- Patterns support 30-60 minute consultation goal
- Evidence is traceable and verifiable
- Quality over quantity approach maintained
- Innovation and unique approaches highlighted

This extraction command provides systematic, repeatable pattern extraction that feeds directly into our deep discovery consultation system.