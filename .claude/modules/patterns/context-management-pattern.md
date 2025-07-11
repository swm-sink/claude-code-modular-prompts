| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Context Management Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="context_management_pattern" category="patterns">
  
  <purpose>
    Efficient session and memory optimization for long-running tasks, ensuring optimal context usage within Claude Code's 200K token window and 40-minute session limits.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Long-running development sessions</condition>
    <condition type="automatic">Context window approaching limits</condition>
    <condition type="explicit">Memory optimization needed</condition>
    <condition type="explicit">Session continuity required</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="assess_context_usage" order="1">
      <requirements>
        Context monitoring must be active
        Usage metrics must be available
        Session parameters must be tracked
      </requirements>
      <actions>
        Evaluate current context consumption
        Monitor token usage and remaining capacity
        Track active session duration
        Assess context relevance and importance
        Identify memory fragmentation issues
      </actions>
      <validation>
        Context usage is accurately assessed
        Token capacity is monitored
        Session duration is tracked
        Context relevance is evaluated
      </validation>
    </phase>
    
    <phase name="prioritize_information" order="2">
      <requirements>
        Context assessment must be completed
        Priority criteria must be defined
        Information categorization must be available
      </requirements>
      <actions>
        Rank context by importance and recency
        Evaluate current task relevance
        Assess future reference likelihood
        Consider information freshness
        Analyze storage cost vs benefit
      </actions>
      <validation>
        Information is properly prioritized
        Relevance is accurately assessed
        Storage efficiency is optimized
        Priority ranking is appropriate
      </validation>
    </phase>
    
    <phase name="optimize_context_structure" order="3">
      <requirements>
        Information prioritization must be completed
        Optimization techniques must be available
        Archive system must be operational
      </requirements>
      <actions>
        Reorganize context for efficiency
        Implement hierarchical information organization
        Compress redundant information
        Archive completed tasks
        Maintain essential references
      </actions>
      <validation>
        Context structure is optimized
        Information is hierarchically organized
        Redundancy is eliminated
        Essential references are maintained
      </validation>
    </phase>
    
    <phase name="implement_memory_strategies" order="4">
      <requirements>
        Context optimization must be completed
        Memory strategies must be defined
        Caching system must be available
      </requirements>
      <actions>
        Apply memory optimization techniques
        Implement lazy loading of detailed information
        Apply context compression and summarization
        Use progressive disclosure of complexity
        Enable smart caching of frequently used data
      </actions>
      <validation>
        Memory strategies are implemented
        Lazy loading is functional
        Context compression is effective
        Caching is operational
      </validation>
    </phase>
    
    <phase name="monitor_and_adjust" order="5">
      <requirements>
        Memory strategies must be implemented
        Monitoring system must be operational
        Adjustment mechanisms must be available
      </requirements>
      <actions>
        Track context efficiency and make adjustments
        Monitor context usage patterns
        Track session performance metrics
        Measure memory efficiency improvements
        Assess task completion rates
      </actions>
      <validation>
        Context efficiency is monitored
        Usage patterns are tracked
        Performance metrics are collected
        Continuous improvement is enabled
      </validation>
    </phase>
    
  </implementation>
  
  <optimization_techniques>
    <technique name="hierarchical_loading">Load context in priority order</technique>
    <technique name="compression">Summarize verbose information</technique>
    <technique name="caching">Store frequently accessed data</technique>
    <technique name="garbage_collection">Remove obsolete context</technique>
  </optimization_techniques>
  
  <session_boundaries>
    <boundary>40-minute session limits</boundary>
    <boundary>Token budget management</boundary>
    <boundary>Context window optimization</boundary>
    <boundary>Strategic session breaks</boundary>
  </session_boundaries>
  
  <integration_points>
    <provides_to>
      patterns/session-management-pattern.md for coordination
      patterns/performance-optimization-pattern.md for efficiency
    </provides_to>
    <depends_on>
      patterns/critical-thinking-pattern.md for optimization decisions
    </depends_on>
  </integration_points>
  
</module>
```