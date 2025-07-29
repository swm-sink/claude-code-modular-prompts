<prompt_component>
  <step name="Intelligent Component Caching">
    <description>
      Implement intelligent caching strategy for frequently used components to optimize framework loading performance.
      
      Based on performance analysis, cache hot components (used 5+ times) with priority scoring based on usage frequency and file size.
      Implement cache invalidation, preloading strategies, and memory-efficient storage.
    </description>
    
    <caching_strategy>
      1. **Hot Component Identification**:
         - Cache components used 5+ times across commands
         - Priority scoring: usage_count / (file_size_kb)
         - Top priority: `generate-structured-report.md` (42 uses, 1KB)
         
      2. **Cache Implementation**:
         - In-memory cache for instant component access
         - LRU eviction policy for memory management
         - Cache warming during framework initialization
         - Intelligent preloading based on command patterns
         
      3. **Cache Management**:
         - 75% estimated cache hit ratio for hot components
         - Automatic cache invalidation on component updates
         - Memory usage monitoring and optimization
         - Performance metrics collection and reporting
         
      4. **Loading Optimization**:
         - Parallel loading for independent components
         - Lazy loading for single-use components (6 identified)
         - Dependency-aware loading order optimization
         - Graceful fallback to direct file loading
    </caching_strategy>
    
    <performance_targets>
      - **40-60% load time reduction** for component resolution
      - **75% cache hit ratio** for frequently used components
      - **Memory efficiency**: under 50KB cache size for optimal components
      - **Lazy loading**: 6 single-use components for memory savings
    </performance_targets>
    
    <implementation_patterns>
      ```javascript
      // Example cache implementation pattern
      const ComponentCache = {
        cache: new Map(),
        hotComponents: [
          'components/reporting/generate-structured-report.md',
          'components/interaction/request-user-confirmation.md',
          'components/context/find-relevant-code.md'
        ],
        
        async loadComponent(path) {
          if (this.cache.has(path)) {
            return this.cache.get(path); // Cache hit
          }
          
          const content = await loadComponentFromDisk(path);
          if (this.isHotComponent(path)) {
            this.cache.set(path, content); // Cache hot components
          }
          
          return content;
        },
        
        preloadHotComponents() {
          return Promise.all(
            this.hotComponents.map(path => this.loadComponent(path))
          );
        }
      };
      ```
    </implementation_patterns>
  </step>
  
  <o>
    Provide intelligent component caching:
    - **Cache Status**: [report cache hit/miss ratios and performance impact]
    - **Hot Components**: [list currently cached components with usage statistics]
    - **Memory Usage**: [current cache size and memory efficiency metrics]
    - **Performance Gains**: [measured load time improvements and optimization results]
    - **Recommendations**: [suggestions for cache tuning and further optimization]
  </o>
</prompt_component> 