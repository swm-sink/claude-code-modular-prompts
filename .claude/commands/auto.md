| version | last_updated | status |
|---------|--------------|--------|
| 2.3.0   | 2025-07-07   | stable |

# /auto - Smart routing for any request

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Intelligent routing with research-first approach">
  
  <delegation target="modules/patterns/intelligent-routing.md">
    Analyze request → Research deeply → Route to optimal command
  </delegation>
  
  <depends_on>
    patterns/intelligent-routing.md for request analysis and routing
    patterns/pattern-library.md for proven execution patterns
    All commands and modules for dynamic routing decisions
  </depends_on>
  
  <examples>
    /auto "Add user authentication"     → Routes to /task
    /auto "Build e-commerce platform"   → Routes to /swarm
    /auto "How does caching work?"      → Routes to /query
    /auto "Create bug report template"  → Smart prompt engineering
  </examples>
  
  <rule>ALWAYS research first, then route intelligently</rule>
  
  <pattern_usage>
    • Uses three_x_rule pattern for routing decisions
    • Implements consequence_mapping for impact analysis
    • Leverages parallel_execution for research operations
    • Applies explicit_validation pattern
    • Uses smart_memoization for cached routing decisions
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/patterns/intelligent-routing.md for full implementation
  </pattern_usage>
  
</command>
```