| version | last_updated | status |
|---------|--------------|--------|
| 2.0.0   | 2025-07-07   | minimal |

# /docs - Instant documentation access

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Navigate, search, and generate documentation">
  
  <delegation target="modules/development/documentation.md">
    Parse request → Search/Navigate → Display or Generate
  </delegation>
  
  <examples>
    /docs "permission guide"        # Find specific topic
    /docs "list all"                # Browse documentation
    /docs "explain AWARE"           # Topic explanation
    /docs "create contributor guide" # Generate new docs
  </examples>
  
  <capabilities>Smart search • Auto-generation • Consistency checks</capabilities>
  
</command>
```