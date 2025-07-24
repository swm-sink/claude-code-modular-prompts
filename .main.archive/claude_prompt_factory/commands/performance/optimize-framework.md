---
description: Advanced framework optimization with intelligent performance tuning, bottleneck analysis, and scalability enhancement
argument-hint: "[optimization_scope] [performance_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /optimize framework - Advanced Framework Optimization

Sophisticated framework optimization system with intelligent performance tuning, bottleneck analysis, and comprehensive scalability enhancement.

## Usage
```bash
/optimize framework performance              # Performance optimization focus
/optimize framework --scalability            # Scalability enhancement
/optimize framework --bottlenecks            # Bottleneck analysis and resolution
/optimize framework --comprehensive          # Comprehensive framework optimization
```

<command_file>
  <metadata>
    <n>/optimize framework</n>
    <purpose>Advanced framework optimization with intelligent performance tuning, bottleneck analysis, and scalability enhancement</purpose>
    <usage>
      <![CDATA[
      /optimize framework [target] --scope [scope]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="target" type="string" required="false" default="comprehensive">
      <description>The optimization target (e.g., execution, tokens, memory, loading, comprehensive)</description>
    </argument>
    <argument name="scope" type="string" required="false" default="system">
      <description>The scope of the optimization (e.g., commands, components, system)</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Optimize the entire system for execution performance</description>
      <usage>/optimize framework execution --scope system</usage>
    </example>
    <example>
      <description>Optimize command token usage</description>
      <usage>/optimize framework tokens --scope commands</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/performance/framework-optimization.md</include>
      <include>components/constitutional/constitutional-framework.md</include>
      <include>components/quality/framework-validation.md</include>
      <include>components/performance/bottleneck-analysis.md</include>
      <include>components/performance/caching-strategies.md</include>
      
You are an advanced framework optimization specialist. The user wants to analyze and optimize the framework's performance.

**Optimization Process:**
1. **Performance Baseline and Analysis**: Measure the current performance across all dimensions and identify bottlenecks.
2. **Optimization Strategy Development**: Develop a detailed optimization roadmap with clear targets and methods.
3. **Systematic Optimization Implementation**: Apply optimizations in measured steps, continuously monitoring for improvements.
4. **Validation and Continuous Improvement**: Validate the effectiveness of optimizations and establish ongoing performance monitoring.

**Implementation Strategy:**
- Use profiling and benchmarking tools to get a clear picture of the framework's current performance.
- Analyze the data to identify performance hotspots and areas for improvement.
- Apply a variety of optimization techniques, including algorithmic improvements, caching, parallel processing, and memory management.
- Rigorously test all changes to ensure that they do not introduce regressions.
- Provide a detailed report of the optimizations applied and the resulting performance improvements.
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/performance/framework-optimization.md</component>
      <component>components/constitutional/constitutional-framework.md</component>
      <component>components/quality/framework-validation.md</component>
    </includes_components>
    <uses_config_values>
      <value>optimization.default_target</value>
      <value>optimization.default_scope</value>
    </uses_config_values>
  </dependencies>
</command_file>

## Command

`/optimize-framework`

## Purpose

Analyze and optimize the Claude Code Prompt Factory's performance across multiple dimensions using systematic optimization frameworks that target loading speed, execution efficiency, memory usage, and token consumption.

## Usage

```bash
/optimize-framework --target=execution --scope=system
/optimize-framework --target=tokens --scope=commands  
/optimize-framework --target=memory --scope=components
/optimize-framework --target=loading "Optimize command discovery and initialization"
```

## Parameters

```xml
<command>optimize-framework</command>
<params>
  <!-- Framework Component Reference -->
  <framework_component>@components/performance/framework-optimization</framework_component>
  <constitutional_compliance>true</constitutional_compliance>
  
  <!-- Optimization Configuration -->
  <target>execution</target> <!-- loading, execution, memory, tokens, comprehensive -->
  <scope>system</scope> <!-- commands, components, system, user_specified -->
  <optimization_level>standard</optimization_level> <!-- conservative, standard, aggressive -->
  <measurement_baseline>current_performance</measurement_baseline>
  
  <!-- Analysis Parameters -->
  <profiling_depth>comprehensive</profiling_depth>
  <bottleneck_identification>automatic</bottleneck_identification>
  <performance_benchmarking>enabled</performance_benchmarking>
  <comparative_analysis>enabled</comparative_analysis>
  
  <!-- Optimization Strategy -->
  <optimization_methods>
    <algorithmic_improvements>true</algorithmic_improvements>
    <caching_optimization>true</caching_optimization>
    <resource_allocation>true</resource_allocation>
    <parallel_processing>true</parallel_processing>
    <memory_management>true</memory_management>
  </optimization_methods>
  
  <!-- Safety and Validation -->
  <preserve_functionality>strict</preserve_functionality>
  <rollback_capability>enabled</rollback_capability>
  <testing_validation>comprehensive</testing_validation>
  <performance_monitoring>continuous</performance_monitoring>
</params>
</command>
```

## Optimization Targets

### 1. **Execution Performance**
Optimize runtime performance and response times:
```bash
/optimize-framework --target=execution --scope=system
# Analyzes command execution patterns and optimizes critical paths
# Identifies bottlenecks in reasoning, processing, and output generation
# Best for: Improving user experience, reducing latency, system responsiveness
```

### 2. **Token Efficiency**
Optimize context window usage and token consumption:
```bash
/optimize-framework --target=tokens --scope=commands
# Analyzes prompt structure and reduces token overhead
# Optimizes component integration and reference patterns
# Best for: Cost reduction, context window management, scalability
```

### 3. **Memory Optimization**
Optimize memory usage and resource allocation:
```bash
/optimize-framework --target=memory --scope=components
# Analyzes memory patterns and optimizes component loading
# Implements efficient caching and garbage collection strategies
# Best for: Resource-constrained environments, multi-agent scenarios
```

### 4. **Loading Performance**
Optimize system initialization and command discovery:
```bash
/optimize-framework --target=loading --scope=system
# Optimizes component loading order and dependency resolution
# Implements lazy loading and selective initialization
# Best for: Startup time, first-use experience, development workflow
```

### 5. **Comprehensive Optimization**
Full-spectrum optimization across all dimensions:
```bash
/optimize-framework --target=comprehensive --scope=system
# Performs holistic optimization considering all performance aspects
# Balances trade-offs between different optimization objectives
# Best for: Production deployment, maximum efficiency, long-term performance
```

## Optimization Process

### Phase 1: Performance Baseline and Analysis
1. **Current State Assessment**: Measure existing performance across all dimensions
2. **Bottleneck Identification**: Identify performance limiting factors
3. **Resource Profiling**: Analyze resource usage patterns and inefficiencies
4. **User Impact Analysis**: Assess performance impact on user experience

### Phase 2: Optimization Strategy Development
1. **Target Prioritization**: Rank optimization targets by impact and feasibility
2. **Method Selection**: Choose optimal optimization techniques for each target
3. **Risk Assessment**: Evaluate potential risks and mitigation strategies
4. **Implementation Planning**: Create detailed optimization roadmap

### Phase 3: Systematic Optimization Implementation
1. **Incremental Optimization**: Apply optimizations in measured steps
2. **Performance Monitoring**: Continuously monitor performance improvements
3. **Validation Testing**: Ensure functionality preservation throughout process
4. **Rollback Preparation**: Maintain ability to revert changes if needed

### Phase 4: Validation and Continuous Improvement
1. **Performance Validation**: Verify optimization effectiveness
2. **Regression Testing**: Ensure no functionality degradation
3. **Monitoring Setup**: Establish ongoing performance monitoring
4. **Optimization Maintenance**: Plan for continued optimization as system evolves

## Examples

### System-Wide Execution Optimization
```bash
/optimize-framework --target=execution --scope=system

# Performance Analysis:
# Current baseline: 2.3s average command execution
# Bottlenecks identified: Component loading (40%), reasoning cycles (35%), output generation (25%)
# 
# Optimization Results:
# Component loading: 2.1s → 0.8s (-62% improvement)
# Reasoning cycles: 1.2s → 0.9s (-25% improvement)  
# Output generation: 0.7s → 0.5s (-29% improvement)
# Total execution time: 2.3s → 1.4s (-39% improvement)
```

### Token Usage Optimization
```bash
/optimize-framework --target=tokens --scope=commands

# Token Analysis:
# Current usage: ~4,200 tokens per complex command
# Optimization opportunities: Redundant context (23%), verbose references (18%), inefficient prompts (12%)
# 
# Token Optimization Results:
# Redundant context removal: -965 tokens (-23%)
# Reference streamlining: -756 tokens (-18%)
# Prompt optimization: -504 tokens (-12%)
# Total reduction: 2,225 tokens (-53% improvement)
# Cost impact: $0.089 → $0.042 per command (-53% cost reduction)
```

### Memory Usage Optimization
```bash
/optimize-framework --target=memory --scope=components

# Memory Profiling:
# Peak memory usage: 1.2GB during complex multi-agent tasks
# Memory hotspots: Component caching (45%), agent state (30%), framework loading (25%)
# 
# Memory Optimization:
# Intelligent component caching: 540MB → 216MB (-60%)
# Agent state optimization: 360MB → 252MB (-30%)
# Lazy framework loading: 300MB → 180MB (-40%)
# Total memory reduction: 1.2GB → 648MB (-46% improvement)
```

### Loading Performance Optimization
```bash
/optimize-framework --target=loading --scope=system

# Loading Analysis:
# Cold start time: 8.7 seconds
# Component discovery: 3.2s, dependency resolution: 2.1s, initialization: 3.4s
# 
# Loading Optimization:
# Parallel component discovery: 3.2s → 1.1s (-66%)
# Optimized dependency resolution: 2.1s → 0.8s (-62%)
# Lazy initialization: 3.4s → 1.3s (-62%)
# Total loading time: 8.7s → 3.2s (-63% improvement)
```

## Framework Integration

This command leverages:
- **Framework Optimization Component**: Comprehensive performance optimization strategies
- **Constitutional AI**: Ethical optimization that preserves system safety and integrity
- **Quality Assurance**: Rigorous testing and validation of optimization changes
- **Performance Monitoring**: Continuous tracking of optimization effectiveness

## Output Format

```markdown
## Optimization Summary
**Target**: [Optimization focus area]
**Scope**: [System scope of optimization]
**Optimization Level**: [Conservative/Standard/Aggressive]
**Duration**: [Time taken for optimization process]

## Performance Baseline
| Metric | Before | After | Improvement |
|--------|---------|-------|-------------|
| Execution Time | 2.3s | 1.4s | -39% |
| Token Usage | 4,200 | 1,975 | -53% |
| Memory Usage | 1.2GB | 648MB | -46% |
| Loading Time | 8.7s | 3.2s | -63% |

## Optimization Breakdown
### Execution Performance
- **Component Loading**: 2.1s → 0.8s (-62%)
- **Reasoning Cycles**: 1.2s → 0.9s (-25%)
- **Output Generation**: 0.7s → 0.5s (-29%)

### Resource Optimization
- **Token Efficiency**: 4,200 → 1,975 tokens (-53%)
- **Memory Footprint**: 1.2GB → 648MB (-46%)
- **CPU Utilization**: 78% → 54% (-31%)

## Optimization Techniques Applied
- ✅ **Algorithmic Improvements**: Optimized critical path algorithms
- ✅ **Caching Optimization**: Intelligent component and result caching
- ✅ **Resource Allocation**: Dynamic resource management
- ✅ **Parallel Processing**: Concurrent execution where safe
- ✅ **Memory Management**: Efficient memory usage patterns

## Validation Results
- **Functionality Tests**: 2,847 tests passed (100% success rate)
- **Regression Tests**: No functionality degradation detected
- **Performance Tests**: All performance targets exceeded
- **Safety Validation**: Constitutional compliance maintained

## Monitoring and Maintenance
- **Performance Monitoring**: Real-time performance tracking enabled
- **Alert Thresholds**: Performance degradation alerts configured
- **Optimization Maintenance**: Monthly optimization review scheduled
- **Rollback Capability**: Full rollback available if needed

## Cost Impact Analysis
**Daily Usage**: 1,000 commands
**Before Optimization**: $89.00/day (4,200 tokens × $0.021)
**After Optimization**: $41.48/day (1,975 tokens × $0.021)
**Monthly Savings**: $1,425.60 (-53% cost reduction)

## Recommendations
- Deploy optimizations to production environment
- Monitor performance for 48 hours post-deployment
- Schedule quarterly optimization reviews
- Consider additional optimizations in [specific areas]
```

## Benefits

- **Dramatic Performance Improvements**: Significant gains across all performance dimensions
- **Cost Optimization**: Substantial reduction in token usage and operational costs
- **User Experience Enhancement**: Faster response times and improved system responsiveness
- **Resource Efficiency**: Optimal utilization of computational and memory resources
- **Scalability Preparation**: Performance foundation for increased usage and complexity
- **Continuous Improvement**: Ongoing optimization and performance monitoring

This command transforms the Claude Code Prompt Factory into a highly optimized, efficient system that delivers exceptional performance while maintaining full functionality and safety. 