| version | last_updated | status |
|---------|--------------|--------|
| 2.3.0   | 2025-07-07   | stable |

# /auto - Smart routing for any request

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Intelligent routing with research-first approach and complexity scoring">
  
  <delegation target="modules/patterns/intelligent-routing.md">
    Analyze request → Calculate complexity → Research deeply → Route to optimal command
  </delegation>
  
  <thinking_pattern>
    <step>1. Parse request and identify key components</step>
    <step>2. Calculate complexity score (components×5 + integrations×4 + security×3)</step>
    <step>3. Research codebase if needed for context</step>
    <step>4. Route based on thresholds: ≤2 /query, 3-9 /task, 10-14 /feature, ≥15 /swarm</step>
    <step>5. Execute with full module capabilities</step>
  </thinking_pattern>
  
  <depends_on>
    patterns/intelligent-routing.md for request analysis and routing
    patterns/pattern-library.md for proven execution patterns
    quality/error-recovery.md for resilient execution
    All commands and modules for dynamic routing decisions
  </depends_on>
  
  <examples>
    /auto "Add user authentication"     → Score ~12 → Routes to /task
    /auto "Build e-commerce platform"   → Score 40+ → Routes to /swarm
    /auto "How does caching work?"      → Score 1 → Routes to /query
    /auto "Create API endpoints"        → Score ~10 → Routes to /feature
  </examples>
  
  <rules>
    <rule>ALWAYS calculate complexity score before routing</rule>
    <rule>ALWAYS research first for informed decisions</rule>
    <rule>NEVER skip complexity scoring algorithm</rule>
  </rules>
  
  <pattern_usage>
    • Uses three_x_rule pattern for routing decisions
    • Implements consequence_mapping for impact analysis
    • Leverages parallel_execution for research operations
    • Applies explicit_validation pattern
    • Uses smart_memoization for cached routing decisions
    • Integrates error_recovery for resilient routing
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/patterns/intelligent-routing.md for full implementation
  </pattern_usage>
  
</command>
```