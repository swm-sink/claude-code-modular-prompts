| version | last_updated | status |
|---------|--------------|--------|
| 2.0.0   | 2025-07-07   | minimal |

# /query - Research-only codebase analysis

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Read-only investigation and understanding">
  
  <delegation target="modules/development/research-analysis.md">
    Search → Analyze → Map patterns → Report findings
  </delegation>
  
  <examples>
    /query "How does authentication work?"  # System understanding
    /query "Find Repository pattern uses"   # Pattern discovery
    /query "Identify security issues"       # Security analysis
    /query "Assess technical debt"          # Code quality
  </examples>
  
  <guarantee>ZERO modifications - read-only analysis</guarantee>
  
  <pattern_usage>
    • Uses parallel_execution for searching multiple files
    • Implements smart_memoization for repeated queries
    • Applies three_x_rule for analysis depth
    • Leverages consequence_mapping for impact assessment
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/development/research-analysis.md for full implementation
  </pattern_usage>
  
</command>
```