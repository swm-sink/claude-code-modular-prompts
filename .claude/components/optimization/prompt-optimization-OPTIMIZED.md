# Native Prompt Optimization

**Purpose**: Advanced prompt optimization using Claude's iterative improvement and self-evaluation capabilities for native optimization without external tools.

**Usage**: 
- Implements 5-step optimization cycle (analyze, identify, modify, evaluate, iterate)
- Provides structural analysis, clarity assessment, and completeness checking
- Offers multiple optimization strategies (clarity-first, efficiency-first, multi-objective)
- Supports Chain-of-Thought and Tree-of-Thoughts optimization methods
- Enables customizable optimization settings (style, priority, constraints)

**Compatibility**: 
- **Works with**: opro-framework, textgrad-framework, dspy-framework, all prompts
- **Requires**: initial_prompt, optimization_focus, iteration_count
- **Conflicts**: None (native Claude capability)

**Implementation**:
```xml
<activate_optimization>
  <mode>prompt_optimization</mode>
  <focus>clarity|efficiency|completeness|all</focus>
  <iterations>auto|1|3|5</iterations>
  <style>conservative|balanced|aggressive</style>
</activate_optimization>
```

**Category**: optimization | **Complexity**: moderate | **Time**: 1-2 hours