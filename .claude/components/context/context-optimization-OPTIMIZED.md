# Context Optimization and Token Management

**Purpose**: Advanced context optimization system maximizing Claude's 200K token window through intelligent hierarchical loading, dynamic management, and adaptive compression.

**Usage**: 
- Manages 4-tier hierarchical loading (core, relevant, extended, comprehensive)
- Allocates 150K tokens for context with 50K working reserve
- Scores context by relevance and loads based on query complexity
- Implements semantic compression while preserving critical information
- Provides real-time adaptation and predictive loading by command type

**Compatibility**: 
- **Works with**: hierarchical-loading, session-management, intelligent-summarization, all commands
- **Requires**: token_budget, relevance_scoring, compression_strategy
- **Conflicts**: None (foundational context system)

**Implementation**:
```yaml
context_optimization:
  total_budget: 200000
  tiers: [core_30K, relevant_50K, extended_40K, comprehensive_30K]
  compression: semantic_chunking
  loading: adaptive_predictive
  efficiency_target: 90%
```

**Category**: context | **Complexity**: moderate | **Time**: 1-2 hours