| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Prompt Construction Visualization Module

────────────────────────────────────────────────────────────────────────────────

## Purpose
Provides transparent visualization of how Claude 4 assembles and executes modular prompts, making the "lego block" composition process visible and predictable.

## Interface Contract

```xml
<interface_contract>
  <inputs>
    <required>command_structure, module_dependencies, execution_context</required>
    <optional>token_budget_limits, visualization_depth, performance_metrics</optional>
  </inputs>
  <outputs>
    <success>assembly_preview, workflow_diagram, context_budget_analysis, execution_forecast</success>
    <failure>visualization_errors, dependency_conflicts, budget_overflow_warnings</failure>
  </outputs>
</interface_contract>
```

## Execution Pattern

```xml
<execution_pattern>
  <claude_4_behavior>
    WHEN invoked:
    1. Parse command structure to identify assembly components
    2. Map module dependencies and execution order
    3. Generate visual workflow representation
    4. Calculate context budget requirements
    5. Provide execution time estimates and optimization suggestions
  </claude_4_behavior>
</execution_pattern>
```

## Core Visualization Functions

### Assembly Preview Generation

```xml
<assembly_preview_generator>
  <workflow_visualization>
    Creates ASCII flow diagrams showing:
    - Command checkpoints in sequence
    - Module composition hierarchy
    - Dependency relationships
    - Parallel execution opportunities
    - Error recovery paths
  </workflow_visualization>
  
  <visual_format>
    ┌─────────────────┐
    │ 1. Checkpoint   │ → Brief description
    │    Name         │
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │ 2. Module       │ → Core functionality
    │    Execution    │
    └─────────────────┘
  </visual_format>
</assembly_preview_generator>
```

### Context Budget Analysis

```xml
<context_budget_analyzer>
  <token_estimation>
    - Analyzes command complexity
    - Estimates module execution overhead
    - Calculates parallel optimization savings
    - Provides budget breakdown by phase
    - Warns of potential context overflow
  </token_estimation>
  
  <optimization_suggestions>
    - Identifies parallel execution opportunities
    - Suggests context window management
    - Recommends checkpoint consolidation
    - Provides module batching strategies
  </optimization_suggestions>
</context_budget_analyzer>
```

### Runtime Execution Preview

```xml
<runtime_execution_previewer>
  <execution_trace_generator>
    Creates realistic execution timelines:
    - Timestamp-based progress indicators
    - Module state transitions
    - Checkpoint completion markers
    - Error boundary visualizations
    - Performance milestone tracking
  </execution_trace_generator>
  
  <progress_indicators>
    Uses standardized symbols:
    ▶️ START, ✓ CHECKPOINT, 🔴 RED, ✅ GREEN, 🔧 REFACTOR
    🎯 DECISION, 📝 WRITING, 🔍 ANALYSIS, ⚡ OPTIMIZATION
  </progress_indicators>
</runtime_execution_previewer>
```

## Claude 4 Integration Patterns

### Prompt Assembly Process

```xml
<prompt_assembly_integration>
  <step_1_parsing>
    - Extract command thinking pattern structure
    - Identify required modules and dependencies
    - Map execution checkpoints to module calls
    - Validate interface contracts
  </step_1_parsing>
  
  <step_2_optimization>
    - Identify parallel execution opportunities
    - Calculate optimal tool batching strategies
    - Optimize context window usage
    - Plan error recovery boundaries
  </step_2_optimization>
  
  <step_3_visualization>
    - Generate assembly preview diagrams
    - Create context budget analysis
    - Build execution trace templates
    - Provide Claude 4 interpretation guides
  </step_3_visualization>
</prompt_assembly_integration>
```

### Execution Transparency

```xml
<execution_transparency>
  <real_time_tracking>
    - Monitor checkpoint progression
    - Track module state transitions
    - Display context usage metrics
    - Show parallel execution efficiency
  </real_time_tracking>
  
  <debug_information>
    - Module input/output visibility
    - Decision reasoning transparency
    - Error boundary identification
    - Performance bottleneck detection
  </debug_information>
</execution_transparency>
```

## Performance Optimization

### Context Window Management

```xml
<context_optimization>
  <token_efficiency>
    - Batch tool calls for 70% improvement
    - Optimize module composition order
    - Minimize redundant information
    - Use smart caching strategies
  </token_efficiency>
  
  <predictive_analysis>
    - Forecast context usage patterns
    - Identify optimization opportunities
    - Suggest execution path alternatives
    - Provide resource allocation guidance
  </predictive_analysis>
</context_optimization>
```

### Parallel Execution Coordination

```xml
<parallel_coordination>
  <execution_scheduling>
    - Identify independent operations
    - Coordinate dependent module execution
    - Optimize resource allocation
    - Manage execution timeouts
  </execution_scheduling>
  
  <performance_monitoring>
    - Track parallel execution efficiency
    - Monitor resource utilization
    - Measure throughput improvements
    - Identify optimization bottlenecks
  </performance_monitoring>
</parallel_coordination>
```

## Integration Points

### Module Runtime Engine Integration

```xml
<runtime_engine_integration>
  <module_composition>
    - Leverages existing composition framework
    - Extends with visualization capabilities
    - Maintains backward compatibility
    - Enhances execution transparency
  </module_composition>
  
  <quality_gates_integration>
    - Visualizes quality gate enforcement
    - Shows TDD cycle progression
    - Displays security validation steps
    - Tracks compliance requirements
  </quality_gates_integration>
</runtime_engine_integration>
```

### Command Enhancement Support

```xml
<command_enhancement_support>
  <standardized_sections>
    - Provides template structures for commands
    - Ensures consistent visualization formats
    - Maintains interface contract compliance
    - Supports extensible enhancement patterns
  </standardized_sections>
  
  <validation_support>
    - Validates command structure compliance
    - Checks interface contract adherence
    - Verifies visualization completeness
    - Ensures performance optimization
  </validation_support>
</command_enhancement_support>
```

## Usage Examples

### Basic Command Visualization

```xml
<basic_usage>
  Input: command="/task", parameters="Add email validation"
  Output: 
    - Assembly preview with 5 checkpoints
    - Context budget: ~12,000 tokens
    - Execution trace with TDD cycle
    - Claude 4 interpretation guide
</basic_usage>
```

### Complex Multi-Agent Visualization

```xml
<complex_usage>
  Input: command="/swarm", parameters="E-commerce platform"
  Output:
    - Multi-agent assembly preview
    - Context budget: ~25,000 tokens
    - Parallel execution coordination
    - Worktree isolation visualization
</complex_usage>
```

## Error Handling

### Visualization Failures

```xml
<error_handling>
  <dependency_conflicts>
    - Detect circular dependencies
    - Identify missing modules
    - Report interface mismatches
    - Suggest resolution strategies
  </dependency_conflicts>
  
  <context_overflow>
    - Monitor token usage limits
    - Warn of potential overflow
    - Suggest optimization strategies
    - Provide degraded functionality
  </context_overflow>
</error_handling>
```

## Future Enhancements

### Interactive Visualization

```xml
<future_capabilities>
  <interactive_preview>
    - Real-time execution monitoring
    - Interactive checkpoint navigation
    - Dynamic optimization suggestions
    - Performance profiling integration
  </interactive_preview>
  
  <adaptive_optimization>
    - Learning from execution patterns
    - Automatic optimization recommendations
    - Context-aware budget management
    - Predictive performance analysis
  </adaptive_optimization>
</future_capabilities>
```

────────────────────────────────────────────────────────────────────────────────

**Dependencies**: patterns/module-composition-framework.md, quality/universal-quality-gates.md, development/task-management.md