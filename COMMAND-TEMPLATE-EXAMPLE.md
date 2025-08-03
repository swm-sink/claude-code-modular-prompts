# Research-Driven Command Template Example

## Example: 1_research-framework.md

```markdown
---
name: 1_research-framework
description: Research framework-specific best practices and patterns through web search
usage: |
  /1_research-framework
  
  This command will:
  1. Detect your project's frameworks
  2. Search for authoritative best practices
  3. Validate sources and resolve conflicts
  4. Create framework-specific context
allowed-tools: [Read, Write, WebSearch, Grep]
requires: [0_verify-project]
produces: [.claude/research/framework-patterns.md, .claude/context/framework-best-practices.md]
---

# Framework Pattern Research Command

## Step 1: Framework Detection
First, I'll analyze your project to identify frameworks:

<framework_detection>
- Check package.json for JavaScript frameworks
- Check requirements.txt for Python frameworks
- Check Gemfile for Ruby frameworks
- Check go.mod for Go frameworks
- Check pom.xml/build.gradle for Java frameworks
</framework_detection>

## Step 2: Web Search Queries

Based on detected framework [FRAMEWORK_NAME], I'll search for:

### Official Documentation
- "[FRAMEWORK_NAME] official best practices 2024"
- "[FRAMEWORK_NAME] architectural patterns documentation"
- "[FRAMEWORK_NAME] team guidelines"
- "site:docs.[FRAMEWORK_DOMAIN] best practices"

### Community Expertise  
- "[FRAMEWORK_NAME] Claude Code patterns site:github.com"
- "[FRAMEWORK_NAME] production patterns [CURRENT_YEAR]"
- "[FRAMEWORK_NAME] anti-patterns real world"
- "[FRAMEWORK_NAME] [EXPERT_NAME] recommendations"

### Performance & Security
- "[FRAMEWORK_NAME] performance optimization guide"
- "[FRAMEWORK_NAME] security best practices OWASP"
- "[FRAMEWORK_NAME] scalability patterns enterprise"

## Step 3: Source Validation (VERIFY Protocol)

For each source found:

### V - Validate Source Authority
- Is this an official maintainer/creator?
- Is this a recognized expert (conference speaker, core contributor)?
- Does the source have proven track record?

### E - Evidence Required
- Are claims backed by benchmarks/data?
- Are there real-world examples?
- Is there community validation (stars, adoption)?

### R - Reference Multiple Sources  
- Find at least 3 sources per pattern
- Note agreements and disagreements
- Weight by authority and recency

### I - Integrate Only Proven Patterns
- Pattern appears in multiple authoritative sources
- Has successful production usage
- No contradicting evidence from experts

### F - Fact-check Against Reality
- Test pattern in minimal example
- Check against your codebase
- Verify performance claims if possible

### Y - Yield Traceable Documentation
Create output with format:
```
Pattern: [Pattern Name]
Sources: 
  - [URL1] - [Author] - [Date] - [Authority Score]
  - [URL2] - [Author] - [Date] - [Authority Score]
Evidence: [Specific evidence for this pattern]
Conflicts: [Any disagreements between sources]
Application: [How to apply in your project]
```

## Step 4: Conflict Resolution

When sources disagree:

1. **Check Context**: Is disagreement due to different use cases?
2. **Check Dates**: Is one source outdated?
3. **Check Authority**: Who has more expertise?
4. **Document Both**: Present both views with context
5. **Recommend**: Make recommendation based on your project's needs

## Step 5: Context Generation

Create framework-specific context files:

### .claude/research/framework-patterns.md
- All researched patterns with full citations
- Conflict documentation
- Update tracking

### .claude/context/framework-best-practices.md  
- Distilled best practices for Claude to follow
- Project-specific adaptations
- Anti-patterns to avoid

### .claude/agents/framework-specialist.md
- Agent specialized in your framework
- Incorporates researched patterns
- Includes compliance checks

## Anti-Pattern Prevention

This command prevents:
- ❌ Hallucinated "best practices" without sources
- ❌ Outdated patterns from old documentation
- ❌ Conflating opinions with established practices
- ❌ Missing important framework-specific considerations
- ❌ Applying patterns out of context

## Example Output

After running this command for a React project:

```markdown
# React Framework Patterns - Research Results

## Pattern: Component Composition over Inheritance
Sources:
- https://react.dev/learn/thinking-in-react (Official React Docs, 2024, Authority: 10/10)
- https://kentcdodds.com/blog/compound-components (Kent C. Dodds, 2023, Authority: 9/10)  
- https://github.com/facebook/react/issues/13991 (React Team Discussion, Authority: 10/10)

Evidence: React team explicitly recommends composition, Facebook uses internally, 
         adopted by major projects (Airbnb, Netflix)

Application: Use component composition patterns in your project:
- Compound components for related UI elements
- Render props for behavior sharing
- Custom hooks for logic extraction

## Pattern: Strict TypeScript Configuration
Sources:
- https://react-typescript-cheatsheet.netlify.app (Community Standard, 2024, Authority: 8/10)
- https://github.com/microsoft/TypeScript-React-Starter (Microsoft, 2024, Authority: 9/10)

Conflicts: 
- Some recommend strict: true (Microsoft)
- Others suggest gradual adoption (Kent C. Dodds)
Resolution: Start with strict: true for new projects, gradual for migrations
```

## Success Metrics

- ✓ Every pattern has 3+ authoritative sources
- ✓ All conflicts are documented and resolved
- ✓ Output is immediately actionable
- ✓ Context files are optimized for Claude
- ✓ Anti-patterns are explicitly prevented
```