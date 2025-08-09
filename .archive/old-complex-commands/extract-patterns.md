---
name: extract-patterns
description: Systematic pattern extraction from multiple repositories with batch processing and targeted analysis
usage: "extract-patterns [pattern-type] [--domain=domain] [--batch=batch-name] [--confidence=threshold]"
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob, LS, TodoWrite, WebFetch]
category: research
version: "1.0"
---

# Extract Patterns: Systematic Multi-Repository Pattern Analysis

## Purpose: Targeted Pattern Discovery Across Repository Collections

The `/extract-patterns` command performs systematic extraction of specific pattern types from multiple repositories, enabling targeted analysis by category, domain, or confidence level. This command leverages the Phase 2 pattern extraction engine to build comprehensive pattern collections efficiently.

**Research Philosophy**: Systematic pattern extraction with rigorous validation beats random repository browsing.

## Targeted vs Scattered: Why Focused Extraction Matters

**❌ Failed Scattered Approach**:
- Random browsing of repositories without focus
- Generic pattern collection without validation
- No confidence scoring or quality assessment
- Missing cross-repository pattern relationships
- Overwhelming volume without actionable insights

**✅ Our Systematic Extraction Approach**:
- Targeted pattern type analysis across multiple repositories
- Domain-filtered extraction for relevant insights
- Batch processing with progress tracking
- Confidence threshold filtering for quality assurance
- Cross-repository correlation and relationship identification
- Evidence-based pattern validation with CRAAP scoring

## Pattern Extraction Categories

### 1. Command Patterns
**Target**: Slash command implementations and innovations
```
Extraction Focus:
├── Generation commands (create components, files, structures)
├── Analysis commands (code review, metrics, validation)
├── Workflow commands (CI/CD, deployment, testing orchestration)
├── Utility commands (helpers, converters, formatters)
└── Integration commands (external tools, APIs, services)

Validation Criteria:
├── Working YAML frontmatter structure
├── Proper tool usage and permissions
├── Clear parameter handling and validation
├── Error handling and user guidance
└── Integration with broader workflow patterns
```

### 2. Agent Patterns
**Target**: Specialized agent architectures and orchestration
```
Extraction Focus:
├── Specialized agents (domain experts, analyzers, generators)
├── Orchestration agents (coordinators, routers, aggregators)
├── Validation agents (quality, testing, compliance)
├── Research agents (discovery, analysis, synthesis)
└── Communication protocols between agents

Validation Criteria:
├── Clear role and responsibility definition
├── Capability boundaries and limitations
├── Inter-agent communication patterns
├── Task routing and delegation mechanisms
└── Performance monitoring and optimization
```

### 3. Context Patterns
**Target**: Context engineering and CLAUDE.md structures
```
Extraction Focus:
├── Project memory patterns (CLAUDE.md organization)
├── Hierarchical context systems (multi-file structures)
├── Navigation patterns (cross-references, linking)
├── Token optimization strategies (efficiency, compression)
└── Context inheritance and cascading patterns

Validation Criteria:
├── Measurable improvement in Claude responses
├── Efficient token usage with comprehensive coverage
├── Clear navigation and discoverability
├── Maintenance and updating procedures
└── Team collaboration and sharing support
```

### 4. Workflow Patterns
**Target**: End-to-end development and automation workflows
```
Extraction Focus:
├── Development workflows (coding, testing, review)
├── Testing workflows (TDD, automation, validation)
├── Deployment workflows (CI/CD, release, rollback)
├── Team workflows (collaboration, knowledge sharing)
└── Quality workflows (monitoring, metrics, improvement)

Validation Criteria:
├── Measurable efficiency improvements
├── Error reduction and quality enhancement
├── Team adoption and satisfaction metrics
├── Scalability and maintenance considerations
└── Integration with existing tools and processes
```

## Batch Processing System

### Pre-Defined Batch Collections

#### High-Priority Web Development
```yaml
batch: priority-web-dev
repositories:
  - claude-code-react-patterns
  - nextjs-claude-automation
  - claude-api-builder
  - claude-testing-framework
focus: ["commands", "workflows"]
confidence_threshold: 0.7
estimated_time: "2-3 hours"
```

#### Enterprise and Team Patterns
```yaml
batch: enterprise-patterns
repositories:
  - claude-enterprise-setup
  - claude-team-workflows
  - quality-assurance-claude
  - compliance-automation-claude
focus: ["agents", "context"]
confidence_threshold: 0.75
estimated_time: "2.5-3.5 hours"
```

#### Innovation and Research
```yaml
batch: innovation-research
repositories:
  - claude-ml-workflows
  - claude-game-dev
  - creative-coding-claude
  - claude-blockchain-tools
focus: ["all"]
confidence_threshold: 0.6
estimated_time: "3-4 hours"
```

### Custom Batch Definition
```yaml
# Create custom extraction batch
custom_batch:
  name: "data-science-focus"
  repositories: 
    - claude-ml-workflows
    - data-analysis-claude
  pattern_types: ["commands", "workflows"]
  domain_filter: "data-science"
  confidence_threshold: 0.8
  validation_level: "comprehensive"
  cross_reference: true
```

## Systematic Extraction Workflow

### Phase 1: Batch Preparation (5-10 minutes)
```
Batch Setup:
├── Load target repository list from catalog
├── Verify repository accessibility and metadata
├── Initialize extraction templates for pattern types
├── Create working directories for parallel processing
├── Set up progress tracking and session management
└── Configure quality gates and validation criteria
```

### Phase 2: Parallel Pattern Extraction (20-40 minutes)
```
Repository Processing:
├── Apply pattern templates systematically to each repository
├── Collect evidence with code examples and documentation
├── Perform initial validation and confidence scoring
├── Document cross-repository pattern relationships
├── Track extraction progress and quality metrics
└── Handle errors and low-yield repositories gracefully
```

### Phase 3: Pattern Aggregation (10-15 minutes)
```
Cross-Repository Analysis:
├── Identify common patterns across multiple repositories
├── Document pattern variations and adaptations
├── Calculate aggregate confidence scores
├── Map pattern relationships and dependencies
├── Identify innovation and unique approaches
└── Prepare patterns for CRAAP validation
```

### Phase 4: Batch Validation (15-25 minutes)
```
Comprehensive Quality Assessment:
├── Apply CRAAP framework to all extracted patterns
├── Filter patterns by confidence threshold
├── Cross-validate patterns across repositories
├── Document validation results and quality metrics
├── Flag patterns requiring additional evidence
└── Generate batch validation report
```

### Phase 5: Database Integration (10 minutes)
```
Knowledge Base Population:
├── Insert validated patterns into research database
├── Create cross-reference relationships
├── Update repository analysis metadata
├── Calculate aggregate metrics and trends
├── Generate extraction summary report
└── Update pattern catalog and indexes
```

## Pattern Extraction Templates Integration

### Command Pattern Template Application
```bash
# Systematic command extraction
for repo in $batch_repositories; do
  echo "Extracting commands from: $repo"
  find "$repo/.claude/commands" -name "*.md" | while read cmd; do
    # Apply command pattern template
    extract_command_pattern "$cmd" "$repo"
    # Validate YAML frontmatter
    validate_command_structure "$cmd"
    # Document tool usage patterns
    analyze_tool_usage "$cmd"
  done
done
```

### Agent Pattern Template Application
```bash
# Systematic agent extraction
for repo in $batch_repositories; do
  echo "Extracting agents from: $repo"
  find "$repo" -path "*/.claude/agents/*" -name "*.md" | while read agent; do
    # Apply agent pattern template
    extract_agent_pattern "$agent" "$repo"
    # Analyze specialization strategies
    analyze_agent_capabilities "$agent"
    # Document orchestration patterns
    extract_coordination_patterns "$agent"
  done
done
```

### Context Pattern Template Application
```bash
# Systematic context extraction
for repo in $batch_repositories; do
  echo "Extracting context from: $repo"
  find "$repo" -name "CLAUDE.md" -o -name "claude.*.md" | while read ctx; do
    # Apply context pattern template
    extract_context_pattern "$ctx" "$repo"
    # Analyze structure and organization
    analyze_context_hierarchy "$ctx"
    # Document navigation patterns
    extract_navigation_strategies "$ctx"
  done
done
```

## Confidence Threshold Filtering

### Threshold Configuration
```yaml
confidence_levels:
  strict: 0.85      # Only highest quality patterns
  standard: 0.70    # Good quality patterns
  inclusive: 0.60   # Medium quality patterns
  research: 0.40    # Include experimental patterns
  
filtering_strategy:
  pre_extraction: "Apply threshold during extraction"
  post_extraction: "Filter after all patterns collected"
  adaptive: "Adjust threshold based on yield"
```

### Quality Gate Integration
```bash
# Filter patterns by confidence threshold
filter_by_confidence() {
  local threshold=$1
  local pattern_file=$2
  
  confidence_score=$(calculate_confidence "$pattern_file")
  if (( $(echo "$confidence_score >= $threshold" | bc -l) )); then
    echo "ACCEPT: $pattern_file (confidence: $confidence_score)"
    add_to_validated_patterns "$pattern_file"
  else
    echo "REJECT: $pattern_file (confidence: $confidence_score below $threshold)"
    add_to_improvement_queue "$pattern_file"
  fi
}
```

## Usage Examples

### Extract Specific Pattern Types
```bash
# Extract command patterns from web development repositories
/extract-patterns commands --domain=web-development --confidence=0.75

# Extract agent orchestration patterns
/extract-patterns agents --confidence=0.8

# Extract context engineering patterns with cross-references
/extract-patterns context --cross-reference --confidence=0.7
```

### Batch Processing
```bash
# Process pre-defined high-priority batch
/extract-patterns --batch=priority-web-dev

# Process custom batch with specific focus
/extract-patterns --batch=enterprise-patterns --focus=agents,context

# Process all repositories with low confidence threshold for research
/extract-patterns --batch=innovation-research --confidence=0.5
```

### Domain-Filtered Extraction
```bash
# Extract patterns specific to data science domain
/extract-patterns workflows --domain=data-science --confidence=0.7

# Extract DevOps-specific patterns across all types
/extract-patterns --domain=devops --confidence=0.75

# Extract testing patterns from multiple domains
/extract-patterns commands --domain=testing,web-development --confidence=0.8
```

### Progressive Extraction with Quality Gates
```bash
# Start with high confidence, expand if needed
/extract-patterns commands --confidence=0.85
# If insufficient yield:
/extract-patterns commands --confidence=0.7 --expand-search
# Final fallback:
/extract-patterns commands --confidence=0.6 --include-experimental
```

## Cross-Repository Pattern Analysis

### Pattern Correlation Detection
```yaml
pattern_correlations:
  command_test_integration:
    pattern_1: "component-generator-command"
    pattern_2: "test-scaffolder-command"
    correlation_strength: 0.85
    repositories_showing_correlation: 7
    evidence: "85% of component generators include test scaffolding"
    
  agent_orchestration_context:
    pattern_1: "orchestration-agent"
    pattern_2: "hierarchical-context"
    correlation_strength: 0.78
    repositories_showing_correlation: 5
    evidence: "Complex agent systems typically use multi-file context"
```

### Pattern Evolution Tracking
```yaml
pattern_evolution:
  component_generation:
    early_pattern: "simple-component-creation"
    evolved_pattern: "intelligent-component-generation"
    evolution_evidence:
      - "Added TypeScript support"
      - "Integrated test generation"
      - "Added accessibility features"
      - "State management integration"
    adoption_timeline: "2023-2025"
    confidence_improvement: "+0.25"
```

### Innovation Identification
```yaml
innovation_patterns:
  ai_assisted_debugging:
    repositories: ["claude-ai-debugger", "intelligent-error-resolver"]
    innovation_level: "breakthrough"
    adoption_potential: "high"
    evidence_strength: "medium (limited sources)"
    consultation_relevance: 0.9
    
  dynamic_agent_spawning:
    repositories: ["adaptive-agent-system"]
    innovation_level: "experimental"
    adoption_potential: "uncertain"
    evidence_strength: "low (single source)"
    consultation_relevance: 0.6
```

## Error Handling and Quality Assurance

### Repository Access Issues
```bash
# Handle inaccessible repositories gracefully
handle_repository_error() {
  local repo_url=$1
  local error_type=$2
  
  case $error_type in
    "access_denied")
      echo "WARNING: Cannot access $repo_url - skipping"
      add_to_error_log "$repo_url" "access_denied"
      continue_with_next_repository
      ;;
    "not_found")
      echo "ERROR: Repository $repo_url not found"
      check_alternative_urls "$repo_url"
      ;;
    "network_timeout")
      echo "RETRY: Network timeout for $repo_url"
      retry_with_backoff "$repo_url" 3
      ;;
  esac
}
```

### Low Pattern Yield Management
```bash
# Adapt extraction strategy for low-yield repositories
handle_low_yield() {
  local repo=$1
  local current_yield=$2
  local minimum_expected=$3
  
  if [ $current_yield -lt $minimum_expected ]; then
    echo "Low yield detected in $repo: $current_yield patterns"
    # Expand search criteria
    expand_pattern_search_criteria
    # Lower confidence threshold temporarily
    adjust_confidence_threshold -0.1
    # Extend analysis time
    extend_analysis_time 15
    # Document low yield reasoning
    document_yield_analysis "$repo" "$current_yield"
  fi
}
```

### Quality Threshold Management
```bash
# Manage quality vs quantity tradeoffs
manage_quality_threshold() {
  local current_confidence=$1
  local target_pattern_count=$2
  local actual_pattern_count=$3
  
  if [ $actual_pattern_count -lt $target_pattern_count ]; then
    echo "Pattern count below target: $actual_pattern_count < $target_pattern_count"
    
    # Option 1: Lower confidence threshold
    if [ $(echo "$current_confidence > 0.6" | bc -l) -eq 1 ]; then
      new_confidence=$(echo "$current_confidence - 0.05" | bc -l)
      echo "Lowering confidence threshold to $new_confidence"
      apply_confidence_threshold $new_confidence
    fi
    
    # Option 2: Expand search scope
    expand_search_to_additional_repositories
    
    # Option 3: Accept lower yield with documentation
    document_yield_justification "quality-over-quantity"
  fi
}
```

## Integration with Research Database

### Batch Database Operations
```sql
-- Insert patterns in batch
INSERT INTO patterns (id, category, subcategory, name, confidence_score, evidence_sources, extraction_batch)
VALUES 
  ('pattern-cmd-001', 'commands', 'generation', 'component-creator', 0.85, 5, 'priority-web-dev'),
  ('pattern-cmd-002', 'commands', 'analysis', 'code-reviewer', 0.78, 4, 'priority-web-dev'),
  ('pattern-agt-001', 'agents', 'specialized', 'react-expert', 0.82, 3, 'priority-web-dev');

-- Create cross-references
INSERT INTO pattern_relationships (pattern_1_id, pattern_2_id, relationship_type, strength)
VALUES 
  ('pattern-cmd-001', 'pattern-cmd-002', 'complements', 0.75),
  ('pattern-cmd-001', 'pattern-agt-001', 'requires', 0.68);
```

### Aggregate Metrics Calculation
```sql
-- Calculate batch extraction metrics
SELECT 
  extraction_batch,
  COUNT(*) as total_patterns,
  AVG(confidence_score) as avg_confidence,
  COUNT(CASE WHEN confidence_score >= 0.8 THEN 1 END) as high_confidence,
  COUNT(CASE WHEN confidence_score >= 0.7 THEN 1 END) as medium_confidence
FROM patterns 
GROUP BY extraction_batch;
```

## Success Criteria and Quality Metrics

### Quantitative Targets
- **Pattern Yield**: 15-25 patterns per repository
- **Batch Processing Time**: 2-4 hours per 4-repository batch
- **Confidence Distribution**: 40%+ high confidence (0.8+), 70%+ medium+ confidence (0.7+)
- **Cross-References**: 60%+ patterns with 2+ relationships
- **Domain Coverage**: All major domains represented

### Qualitative Indicators
- Patterns support specific consultation scenarios
- Clear evidence trail for all accepted patterns
- Innovation and unique approaches documented
- Cross-repository trends and evolution captured
- Integration path to consultation system clear

## Output Deliverables

### Pattern Collection Report
```markdown
# Pattern Extraction Report: Priority Web Development Batch

## Executive Summary
- **Repositories Processed**: 4 (react-patterns, nextjs-automation, api-builder, testing-framework)
- **Total Patterns Extracted**: 67
- **High Confidence Patterns**: 29 (43%)
- **Cross-References Identified**: 45
- **Innovation Patterns**: 8

## Pattern Distribution
### Commands: 32 patterns
- Generation commands: 12 (avg confidence: 0.82)
- Analysis commands: 8 (avg confidence: 0.75)
- Workflow commands: 12 (avg confidence: 0.79)

### Agents: 18 patterns
- Specialized agents: 10 (avg confidence: 0.77)
- Orchestration agents: 8 (avg confidence: 0.74)

### Context: 10 patterns  
- Hierarchical context: 6 (avg confidence: 0.81)
- Navigation patterns: 4 (avg confidence: 0.73)

### Workflows: 7 patterns
- Development workflows: 4 (avg confidence: 0.76)
- Testing workflows: 3 (avg confidence: 0.80)
```

### Research Database Entries
- 67 validated pattern records
- 45 cross-reference relationships
- 4 repository analysis summaries
- Batch processing metadata

### Pattern Relationship Map
- Visual representation of pattern dependencies
- Complementary pattern clusters
- Innovation adoption pathways
- Domain-specific pattern networks

---

**Remember**: Systematic pattern extraction with rigorous validation builds the comprehensive evidence base needed for intelligent, project-specific consultation. Focus on quality patterns that directly support the 30-60 minute deep discovery goals.