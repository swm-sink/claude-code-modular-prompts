# Anti-Pattern Prevention Guide

## Core Anti-Patterns to Prevent in Every Command

### 1. Hallucination Prevention

**Pattern**: LLMs confidently making up information
**Prevention Built Into Commands**:
```yaml
Required in every command:
- Web search for authoritative sources
- No claims without citations  
- Explicit "I don't know" when no evidence
- Source URLs must be real and verifiable
```

**Implementation**:
```markdown
Before stating any best practice:
1. Search: "[topic] best practices site:official-docs.com"
2. Verify: URL is accessible and contains claimed information
3. Cite: "According to [Source URL], the recommended approach is..."
4. Never: Use phrases like "It's generally known that..." without source
```

### 2. Metric Invention Prevention

**Pattern**: Creating specific numbers without measurement
**Prevention Built Into Commands**:
```yaml
Forbidden patterns:
- "Improves performance by 73%"
- "Reduces bugs by 90%"  
- "85% of teams use this"

Required patterns:
- "May improve performance (source: [URL])"
- "Helps reduce bugs according to [Study URL]"
- "Commonly used pattern per [Survey URL]"
```

### 3. Outdated Information Prevention

**Pattern**: Using old practices that have been superseded
**Prevention Built Into Commands**:
```yaml
Date checking protocol:
- Prefer sources from current/previous year
- Flag sources older than 2 years
- Search for "deprecated [pattern]" 
- Check for newer alternatives
```

### 4. Context Ignorance Prevention

**Pattern**: Applying patterns without considering context
**Prevention Built Into Commands**:
```yaml
Context requirements:
- Project size consideration
- Team size adaptation
- Performance requirements
- Compliance needs
- Technical constraints
```

### 5. Authority Confusion Prevention

**Pattern**: Treating all sources as equally valid
**Prevention Built Into Commands**:
```yaml
Source hierarchy:
1. Official documentation
2. Core team members
3. Recognized experts
4. Popular community members
5. Random blog posts (usually rejected)
```

### 6. Conflict Hiding Prevention

**Pattern**: Presenting disputed practices as universal truths
**Prevention Built Into Commands**:
```yaml
Conflict handling:
- Document all viewpoints found
- Note which experts disagree
- Explain context for disagreement
- Make reasoned recommendation
- Allow user to decide
```

### 7. Completeness Illusion Prevention

**Pattern**: Pretending to have found everything
**Prevention Built Into Commands**:
```yaml
Honesty requirements:
- "Found X sources, there may be more"
- "Searched these specific queries"
- "Did not search for [out-of-scope topic]"
- "Recommend additional research on..."
```

### 8. Implementation Assumption Prevention

**Pattern**: Assuming how something should be implemented
**Prevention Built Into Commands**:
```yaml
Implementation guards:
- Show multiple implementation approaches
- Note trade-offs of each
- Avoid prescriptive "must use"
- Respect project constraints
```

### 9. Tool Bias Prevention

**Pattern**: Favoring familiar tools without research
**Prevention Built Into Commands**:
```yaml
Tool selection protocol:
- Research multiple options
- Compare based on project needs
- Note ecosystem maturity
- Consider team expertise
- Document selection criteria
```

### 10. Success Theater Prevention

**Pattern**: Overly optimistic progress reporting
**Prevention Built Into Commands**:
```yaml
Progress tracking requirements:
- Specific files created/modified
- Exact commands that can be run
- Measurable completion criteria
- Honest about limitations
- Clear about manual steps needed
```

## Implementation in Commands

Every command must include:

```markdown
## Anti-Pattern Guards

This command actively prevents:
- ❌ [Specific anti-pattern 1 relevant to this command]
- ❌ [Specific anti-pattern 2 relevant to this command]
- ❌ [Specific anti-pattern 3 relevant to this command]

By:
- ✓ [Specific prevention mechanism 1]
- ✓ [Specific prevention mechanism 2]
- ✓ [Specific prevention mechanism 3]
```

## Validation Checklist

Before command is considered complete:
- [ ] All claims have sources
- [ ] No invented metrics
- [ ] Conflicts documented
- [ ] Context requirements clear
- [ ] Authority levels noted
- [ ] Limitations acknowledged
- [ ] Implementation flexible
- [ ] Progress measurable

## Continuous Improvement

Track when anti-patterns slip through:
1. Document the failure
2. Analyze why it wasn't caught
3. Update prevention mechanism
4. Add to command template
5. Share learning with team

## The Golden Rule

**When in doubt, research more and claim less.**

Better to provide 3 well-researched patterns than 10 made-up ones.