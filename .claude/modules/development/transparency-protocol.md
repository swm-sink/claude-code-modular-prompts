| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-14   | stable |

# Routing Decision Transparency Protocol v1.0.0

## Overview

Every routing decision must be transparent, explainable, and understandable to users. This protocol ensures all decisions can be clearly communicated.

## Transparency Levels

### 1. User-Facing Transparency
```yaml
user_explanation:
  format: "structured_natural_language"
  components:
    what: "Which command was selected"
    why: "Clear reasoning in plain language"
    how: "What will happen next"
    alternatives: "Other options considered"
    
  example: |
    I'll use the /feature command for this task because:
    - You're adding authentication (a complete feature)
    - This affects 6 files across 2 modules
    - It needs design decisions for the auth flow
    - Tests need to be written for the new functionality
    
    I considered /task but it's limited to 3 files.
    /swarm would be overkill for this scope.
```

### 2. Technical Transparency
```yaml
technical_details:
  format: "structured_data"
  components:
    counts: "Exact component counts"
    thresholds: "Specific limits checked"
    calculations: "How counts were derived"
    
  example:
    component_counts:
      files_to_modify: 2
      files_to_create: 4
      cross_module_deps: 1
      
    threshold_checks:
      task_max_files: "6 > 3 ❌"
      feature_range: "2 ≤ 6 ≤ 10 ✓"
      feature_design: "required ✓"
```

### 3. Debug Transparency
```yaml
debug_trace:
  format: "detailed_log"
  components:
    - Request parsing steps
    - File identification process
    - Dependency resolution
    - Threshold evaluation order
    - Decision tree traversal
    
  verbosity_levels:
    summary: "Key decisions only"
    detailed: "All major steps"
    trace: "Every calculation"
```

## Transparency Artifacts

### Decision Summary Card
```markdown
## Routing Decision Summary

**Request**: "Add user authentication to the API"
**Selected Command**: `/feature`
**Confidence**: 95%

### Why /feature?
- ✓ Feature-sized scope (6 files)
- ✓ Requires design decisions
- ✓ Clear requirements provided
- ✓ Manageable complexity

### Component Analysis
| Component | Count | /task Limit | /feature Range |
|-----------|-------|-------------|----------------|
| Files     | 6     | ≤3 ❌       | 2-10 ✓         |
| Modules   | 2     | 1 ❌        | ≤3 ✓           |
| Tests     | 6     | -           | Required ✓     |

### Alternatives Considered
- **❌ /task**: Too many files (6 > 3)
- **❌ /swarm**: Unnecessary (no parallel work needed)
- **✓ /feature**: Perfect fit for this scope
```

### Detailed Explanation Template
```yaml
explanation_template:
  header: "Routing Analysis for: ${REQUEST}"
  
  sections:
    understanding:
      title: "What I understood"
      content: "You want to ${PARSED_INTENT}"
      
    analysis:
      title: "What I found"
      content: |
        - ${FILE_COUNT} files need changes
        - ${MODULE_COUNT} modules affected
        - ${TEST_COUNT} tests required
        
    decision:
      title: "My recommendation"
      content: "Use ${COMMAND} because ${PRIMARY_REASON}"
      
    next_steps:
      title: "What happens next"
      content: "${COMMAND_WORKFLOW_DESCRIPTION}"
```

## Transparency Requirements

### Always Explain
1. Which command was selected
2. The primary reason for selection
3. What will happen when executed
4. Any risks or considerations

### Always Show
1. Component counts that drove decision
2. Threshold comparisons
3. Alternative commands considered
4. Confidence level

### Never Hide
1. Failures or errors in routing
2. Uncertainty in decision
3. Manual overrides
4. Edge cases encountered

## User Interaction Patterns

### Proactive Transparency
```yaml
before_execution:
  show_decision: true
  ask_confirmation: "when_uncertain"
  provide_options: "when_multiple_valid"
  
  example: |
    Based on my analysis, I'll use /feature to implement authentication.
    This will create 4 new files and modify 2 existing ones.
    
    Proceed with /feature? (or suggest alternative)
```

### On-Demand Details
```yaml
user_queries:
  "why not /task?": "Show specific threshold violations"
  "explain the counting": "Show how each count was derived"
  "what are my options?": "List all commands with feasibility"
  "show me the analysis": "Display full routing audit"
```

### Progressive Disclosure
```yaml
disclosure_levels:
  1_summary: "Used /feature (6 files, design needed)"
  2_reasoning: "Plus threshold comparisons"
  3_detailed: "Plus component analysis"
  4_complete: "Full audit trail"
  
  user_controls:
    - "show more"
    - "explain decision"
    - "view alternatives"
    - "see full analysis"
```

## Transparency Formats

### Console Output
```
🔄 Analyzing request...
📊 Counting components:
   - Files to modify: 2
   - Files to create: 4
   - Cross-module dependencies: 1
   
🎯 Routing decision: /feature
   ✓ Within file limits (6 files)
   ✓ Design decisions needed
   ✓ Clear requirements
   
📋 Next: Generate PRD and implementation plan
```

### Structured Response
```json
{
  "routing_decision": {
    "command": "/feature",
    "confidence": 0.95,
    "primary_reason": "Feature-scoped with design needs",
    "component_summary": {
      "total_files": 6,
      "complexity": "medium",
      "requires_design": true
    },
    "alternatives": {
      "/task": "Exceeds file limit",
      "/swarm": "Unnecessary complexity"
    }
  }
}
```

### Audit Trail Link
```yaml
decision_reference:
  message: "View complete routing analysis"
  artifact_id: "2025-07-08-routing-abc123"
  location: ".claude/context/artifacts/2025-07-08/routing/"
  query_url: "/context/artifacts/${artifact_id}"
```

## Error Transparency

### When Routing Fails
```yaml
routing_error_transparency:
  show:
    - What went wrong
    - Which step failed
    - Recovery attempt
    - Fallback decision
    
  example: |
    ⚠️ Routing analysis encountered an issue:
    - Unable to determine exact file count
    - Multiple interpretations possible
    
    Falling back to /auto for clarification.
```

### When Uncertain
```yaml
uncertainty_transparency:
  show:
    - Confidence level
    - Ambiguous factors
    - Assumptions made
    - Clarification needed
    
  example: |
    🤔 Routing confidence: 65% (below threshold)
    
    Uncertain because:
    - "Make it faster" could mean many things
    - Can't identify specific components
    
    Using /auto to clarify requirements first.
```

## Benefits

1. **User Trust**: Clear explanations build confidence
2. **Learning**: Users understand command selection
3. **Debugging**: Transparent decisions are debuggable
4. **Improvement**: Clear patterns for optimization
5. **Accountability**: Every decision is explainable