# /query - Research & Analysis Command

**Purpose**: Research and analyze codebases without making changes. Perfect for understanding before modifying.

## When to Use

Use `/query` for:
- Understanding existing code
- Analyzing architecture
- Finding implementation patterns
- Researching dependencies
- Investigating bugs (before fixing)
- Security audits (read-only)

## Core Features

### Read-Only Guarantee
- Never modifies files
- No commits or changes
- Safe for production analysis
- Perfect for code reviews

### Comprehensive Search
- Code pattern matching
- Dependency analysis
- Architecture mapping
- Performance profiling
- Security scanning

## Analysis Types

### Code Understanding
```bash
/query "How does the authentication system work?"
```
- Maps auth flow
- Identifies components
- Documents patterns
- Shows examples

### Architecture Analysis
```bash
/query "What is the current microservice architecture?"
```
- Service boundaries
- Communication patterns
- Data flow
- Dependency graph

### Pattern Discovery
```bash
/query "Find all uses of the Repository pattern"
```
- Pattern instances
- Implementation variations
- Best practices used
- Improvement opportunities

### Bug Investigation
```bash
/query "Why do users get logged out randomly?"
```
- Traces code paths
- Identifies causes
- Suggests fixes (not implemented)
- Documents findings

## Search Strategies

### 1. Broad Discovery
- Start with Glob patterns
- Search file names
- Map directory structure
- Identify key modules

### 2. Deep Analysis
- Grep for patterns
- Read specific files
- Trace call chains
- Map dependencies

### 3. Synthesis
- Combine findings
- Create mental model
- Document understanding
- Present insights

## Output Formats

### Executive Summary
- Key findings
- Critical insights
- Recommendations
- Next steps

### Technical Deep-Dive
- Code examples
- Call graphs
- Dependency maps
- Performance metrics

### Visual Representations
```
Authentication Flow:
┌─────────┐     ┌─────────┐     ┌─────────┐
│ User    │────▶│ Auth    │────▶│ Token   │
│ Login   │     │ Service │     │ Store   │
└─────────┘     └─────────┘     └─────────┘
```

## Common Queries

### Security Analysis
```bash
/query "Identify potential security vulnerabilities"
```
- SQL injection risks
- XSS possibilities  
- Authentication gaps
- Data exposure

### Performance Review
```bash
/query "Find performance bottlenecks in API"
```
- Slow queries
- N+1 problems
- Missing indexes
- Cache opportunities

### Technical Debt
```bash
/query "Assess technical debt in codebase"
```
- Code duplication
- Outdated patterns
- Missing tests
- Documentation gaps

## Integration Points

### Before Development
```bash
# First understand
/query "How is user management implemented?"

# Then modify
/task "Add user roles feature"
```

### Code Review
```bash
/query "Review the changes in PR #123"
```
- Analyzes diff
- Checks patterns
- Identifies risks
- Suggests improvements

## Best Practices

1. **Query first** before any task
2. **Be specific** in questions
3. **Save findings** for reference
4. **Share insights** with team

## Advanced Features

### Multi-File Analysis
- Correlates information across files
- Builds complete understanding
- Identifies hidden dependencies

### Historical Analysis
```bash
/query "How has the auth system evolved?"
```
- Git history analysis
- Pattern evolution
- Decision rationale

### Comparative Analysis
```bash
/query "Compare our auth with best practices"
```
- Industry standards
- Security guidelines
- Performance benchmarks

## Examples

### Simple Query
```bash
/query "What testing framework do we use?"
# Searches for test files, configs, and patterns
```

### Complex Investigation  
```bash
/query "Trace the complete order processing flow"
# Maps entire business process across services
```

### Optimization Research
```bash
/query "Find all database queries that could be optimized"
# Identifies N+1, missing indexes, slow queries
```

## Token Optimization
- Concise summaries
- Focused analysis
- No implementation details
- Max 8k tokens per response