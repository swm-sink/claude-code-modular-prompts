---
description: Intelligent cache clearing with automated invalidation, performance optimization, and comprehensive state management
argument-hint: "[cache_type] [invalidation_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /cache clear - Intelligent Cache Clearing

Advanced cache clearing system with automated invalidation, intelligent performance optimization, and comprehensive state management.

## Usage
```bash
/cache clear all                           # Clear all application caches
/cache clear --selective                   # Selectively clear specific caches
/cache clear --automated                   # Automated cache invalidation
/cache clear --performance                 # Performance-optimized clearing
```

<command_file>
  <metadata>
    <n>/cache clear</n>
    <purpose>Intelligent cache clearing with automated invalidation, performance optimization, and comprehensive state management</purpose>
    <usage>
      <![CDATA[
      /cache clear [cache_type]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="cache_type" type="string" required="false" default="all">
      <description>Type of cache to clear</description>
    </argument>
    <argument name="invalidation_strategy" type="string" required="false" default="automated">
      <description>Strategy for cache invalidation and clearing</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Clear all application caches</description>
      <usage>/cache clear all</usage>
    </example>
    <example>
      <description>Selectively clear specific caches</description>
      <usage>/cache clear --selective</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
You are an advanced cache management specialist. The user wants to implement intelligent cache clearing with automated invalidation and performance optimization.

**Clearing Process:**
1. **Cache Analysis**: Analyze current cache structure and usage patterns
2. **Invalidation Strategy**: Design intelligent cache invalidation strategies
3. **Automated Clearing**: Implement automated cache clearing mechanisms
4. **Performance Optimization**: Optimize cache performance and efficiency
5. **State Management**: Ensure comprehensive state consistency and management

**Implementation Strategy:**
- Analyze cache usage to identify optimization opportunities
- Implement intelligent cache invalidation strategies (e.g., TTL, event-based)
- Create automated cache clearing with safety checks and validation
- Optimize cache performance with efficient data structures and algorithms
- Establish comprehensive state management to prevent inconsistencies

<include component="components/performance/cost-optimization.md" />
<include component="components/reliability/circuit-breaker.md" />
<include component="components/quality/framework-validation.md" />
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/performance/cost-optimization.md</component>
      <component>components/reliability/circuit-breaker.md</component>
      <component>components/quality/framework-validation.md</component>
    </includes_components>
    <uses_config_values>
      <value>cache.invalidation.auto_enabled</value>
      <value>performance.optimization.strategy</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Workflow

The `/cache clear` command follows a systematic process to safely clear caches.

```xml
<cache_clear_workflow>
  <step name="Analyze Caches">
    <description>Analyze all relevant cache types (memory, file, build, dependency, and application) to determine their size and contents. This includes language-specific caches for Python, Node.js, Java, Go, and Docker.</description>
    <tool_usage>
      <tool>Parallel Bash</tool>
      <description>Run commands to analyze the size of various cache directories.</description>
    </tool_usage>
  </step>
  
  <step name="Clear Caches">
    <description>Clear the specified cache types. By default, it will clear all identified caches. The user can specify a type (e.g., `build`, `deps`) to clear only a specific cache.</description>
    <tool_usage>
      <tool>Parallel Bash</tool>
      <description>Run commands to delete the contents of various cache directories.</description>
    </tool_usage>
  </step>
  
  <step name="Verify & Report">
    <description>Verify that the caches have been cleared successfully and generate a report detailing the cleared caches and the amount of space freed.</description>
    <output>A summary report of the cache clearing operation.</output>
  </step>
</cache_clear_workflow>
```

### Language-Specific Caches
- **Python**: pip cache, __pycache__, .pyc files, pytest cache
- **Node.js**: npm/yarn cache, node_modules/.cache, .next cache
- **Java**: Maven/Gradle cache, target directories, .class files
- **Go**: Module cache, build cache, test cache
- **Docker**: Image cache, build cache, volume cache