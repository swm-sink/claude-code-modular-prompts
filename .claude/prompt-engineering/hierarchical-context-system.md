# Hierarchical Context System

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-20   | production |

## Purpose

Multi-level context hierarchy system optimized for Claude 4's 200K context window with dynamic loading, @ import resolution, and intelligent prioritization for maximum token efficiency.

## Architecture Overview

```xml
<hierarchical_context_system version="1.0.0" enforcement="CRITICAL">
  <purpose>Token-optimized context hierarchy with dynamic loading and priority-based allocation</purpose>
  
  <hierarchy_levels>
    <level priority="1" allocation="5%">Project Configuration (PROJECT_CONFIG.xml, CLAUDE.md core)</level>
    <level priority="2" allocation="15%">Architecture Patterns (@modules/patterns/)</level>
    <level priority="3" allocation="25%">Command Implementations (@commands/)</level>
    <level priority="4" allocation="30%">Domain Standards (@domain/, @system/)</level>
    <level priority="5" allocation="20%">Context Templates (dynamic based on task)</level>
    <level priority="6" allocation="5%">Session Memory (preserved state)</level>
  </hierarchy_levels>
  
  <dynamic_loading_rules>
    <rule>Load level 1-2 immediately (framework core)</rule>
    <rule>Load level 3 on command invocation</rule>
    <rule>Load level 4 based on task requirements</rule>
    <rule>Load level 5-6 as needed with LRU eviction</rule>
  </dynamic_loading_rules>
  
  <import_resolution enforcement="MANDATORY">
    <pattern>@{category}/{module}.md</pattern>
    <resolution_order>
      1. Direct path resolution from .claude/
      2. Category-based lookup (commands, modules, system, domain)
      3. Fuzzy matching with suggestions
      4. Template instantiation if not found
    </resolution_order>
    <caching>15-minute TTL for resolved imports</caching>
  </import_resolution>
</hierarchical_context_system>
```

## Context Prioritization Matrix

```python
# Context Priority Allocation System
CONTEXT_PRIORITIES = {
    "critical_framework": {
        "priority": 1,
        "token_allocation": 10000,  # 5% of 200K
        "components": ["CLAUDE.md", "PROJECT_CONFIG.xml", "quality gates"]
    },
    "architectural_patterns": {
        "priority": 2, 
        "token_allocation": 30000,  # 15% of 200K
        "components": ["@modules/patterns/", "core workflows"]
    },
    "active_commands": {
        "priority": 3,
        "token_allocation": 50000,  # 25% of 200K
        "components": ["current command", "delegated modules"]
    },
    "domain_context": {
        "priority": 4,
        "token_allocation": 60000,  # 30% of 200K
        "components": ["@domain/", "@system/", "project specifics"]
    },
    "dynamic_templates": {
        "priority": 5,
        "token_allocation": 40000,  # 20% of 200K
        "components": ["task-specific templates", "user preferences"]
    },
    "session_memory": {
        "priority": 6,
        "token_allocation": 10000,  # 5% of 200K
        "components": ["conversation history", "accumulated context"]
    }
}
```

## Dynamic Context Loading

```xml
<dynamic_context_loading>
  <loading_strategies>
    <lazy_loading>
      <trigger>Command invocation or @ import reference</trigger>
      <implementation>Load module content only when specifically referenced</implementation>
      <optimization>Batch load related modules in single operation</optimization>
    </lazy_loading>
    
    <predictive_loading>
      <trigger>Command pattern recognition</trigger>
      <implementation>Pre-load likely-needed modules based on command type</implementation>
      <optimization>Background loading during thinking blocks</optimization>
    </predictive_loading>
    
    <priority_loading>
      <trigger>Token budget constraints</trigger>
      <implementation>Load highest priority content first</implementation>
      <optimization>Graceful degradation when approaching limits</optimization>
    </priority_loading>
  </loading_strategies>
  
  <eviction_policies>
    <lru_eviction>Remove least recently used content when token budget exceeded</lru_eviction>
    <priority_eviction>Remove lower priority content before higher priority</priority_eviction>
    <session_preservation>Always preserve session memory and framework core</session_preservation>
  </eviction_policies>
</dynamic_context_loading>
```

## @ Import Resolution Engine

```python
class ImportResolver:
    """Resolves @ imports with intelligent fallbacks and optimization"""
    
    def __init__(self, base_path=".claude/"):
        self.base_path = base_path
        self.cache = {}  # 15-minute TTL cache
        self.resolution_stats = {}
        
    def resolve_import(self, import_path: str) -> str:
        """
        Resolve @ import with multiple strategies:
        @modules/patterns/tdd-cycle-pattern.md
        @commands/auto
        @system/quality/universal-quality-gates.md
        """
        if import_path in self.cache:
            return self.cache[import_path]
            
        # Strategy 1: Direct path resolution
        direct_path = self._resolve_direct(import_path)
        if direct_path:
            self.cache[import_path] = direct_path
            return direct_path
            
        # Strategy 2: Category-based lookup
        category_path = self._resolve_category(import_path)
        if category_path:
            self.cache[import_path] = category_path
            return category_path
            
        # Strategy 3: Fuzzy matching
        fuzzy_path = self._resolve_fuzzy(import_path)
        if fuzzy_path:
            self.cache[import_path] = fuzzy_path
            return fuzzy_path
            
        # Strategy 4: Template instantiation
        template_path = self._create_from_template(import_path)
        self.cache[import_path] = template_path
        return template_path
        
    def _resolve_direct(self, import_path: str) -> Optional[str]:
        """Direct file path resolution"""
        clean_path = import_path.lstrip('@')
        full_path = f"{self.base_path}{clean_path}"
        
        if not full_path.endswith('.md'):
            full_path += '.md'
            
        return full_path if self._file_exists(full_path) else None
        
    def _resolve_category(self, import_path: str) -> Optional[str]:
        """Category-based intelligent lookup"""
        categories = {
            'commands': 'commands/',
            'modules': 'modules/',
            'system': 'system/',
            'domain': 'domain/',
            'meta': 'meta/',
            'templates': 'templates/'
        }
        
        for category, path in categories.items():
            if category in import_path:
                return self._search_in_category(import_path, path)
                
        return None
        
    def _resolve_fuzzy(self, import_path: str) -> Optional[str]:
        """Fuzzy matching with similarity scoring"""
        all_files = self._get_all_framework_files()
        matches = self._fuzzy_match(import_path, all_files)
        
        return matches[0] if matches else None
        
    def _create_from_template(self, import_path: str) -> str:
        """Create module from template when not found"""
        template_content = self._get_module_template(import_path)
        new_path = self._create_module_file(import_path, template_content)
        
        return new_path
```

## Context Switching Optimization

```xml
<context_switching_optimization>
  <principles>
    <minimize_reloads>Cache frequently accessed modules with intelligent TTL</minimize_reloads>
    <batch_operations>Load related modules in single operation to reduce overhead</batch_operations>
    <predictive_caching>Pre-load likely-needed content based on usage patterns</predictive_caching>
    <graceful_degradation>Maintain functionality even when context limits reached</graceful_degradation>
  </principles>
  
  <implementation_patterns>
    <pattern name="Command Context Preparation">
      <step>Identify required modules for command</step>
      <step>Pre-load critical dependencies</step>
      <step>Establish context hierarchy for session</step>
      <step>Reserve token budget for execution</step>
    </pattern>
    
    <pattern name="Dynamic Context Adaptation">
      <step>Monitor token usage during execution</step>
      <step>Evict low-priority content as needed</step>
      <step>Load additional context on demand</step>
      <step>Preserve session continuity</step>
    </pattern>
    
    <pattern name="Session Context Management">
      <step>Establish baseline context at session start</step>
      <step>Track context evolution throughout session</step>
      <step>Compress and archive completed context</step>
      <step>Maintain minimal session state for continuity</step>
    </pattern>
  </implementation_patterns>
</context_switching_optimization>
```

## Token Budget Management

```python
class TokenBudgetManager:
    """Manages token allocation across context hierarchy"""
    
    def __init__(self, total_budget=200000, work_reserve=50000):
        self.total_budget = total_budget
        self.work_reserve = work_reserve
        self.available_budget = total_budget - work_reserve
        self.allocations = {}
        self.usage_tracking = {}
        
    def allocate_budget(self, priority_levels: dict) -> dict:
        """Allocate token budget across priority levels"""
        allocations = {}
        
        for level, config in priority_levels.items():
            allocation = int(self.available_budget * config['allocation_percentage'])
            allocations[level] = {
                'budget': allocation,
                'used': 0,
                'remaining': allocation
            }
            
        return allocations
        
    def request_tokens(self, level: str, amount: int) -> bool:
        """Request token allocation for specific level"""
        if level not in self.allocations:
            return False
            
        if self.allocations[level]['remaining'] >= amount:
            self.allocations[level]['used'] += amount
            self.allocations[level]['remaining'] -= amount
            return True
            
        # Try to borrow from lower priority levels
        return self._borrow_tokens(level, amount)
        
    def _borrow_tokens(self, requesting_level: str, amount: int) -> bool:
        """Borrow tokens from lower priority levels"""
        priority_order = ['session_memory', 'dynamic_templates', 'domain_context', 
                         'active_commands', 'architectural_patterns', 'critical_framework']
        
        requesting_priority = priority_order.index(requesting_level)
        
        for i in range(requesting_priority + 1, len(priority_order)):
            lender_level = priority_order[i]
            if self.allocations[lender_level]['remaining'] >= amount:
                self.allocations[lender_level]['remaining'] -= amount
                self.allocations[requesting_level]['remaining'] += amount
                return True
                
        return False
```

## Context Quality Gates

```xml
<context_quality_gates enforcement="BLOCKING">
  <validation_rules>
    <rule name="Token Budget Compliance">
      <check>Total context must not exceed available budget</check>
      <action>Trigger eviction or degradation if exceeded</action>
      <priority>CRITICAL</priority>
    </rule>
    
    <rule name="Import Resolution Validation">
      <check>All @ imports must resolve to valid modules or templates</check>
      <action>Create missing modules from templates or suggest alternatives</action>
      <priority>HIGH</priority>
    </rule>
    
    <rule name="Context Coherence Validation">
      <check>Context must maintain logical coherence across hierarchy</check>
      <action>Flag contradictions and inconsistencies</action>
      <priority>MEDIUM</priority>
    </rule>
    
    <rule name="Performance Threshold Validation">
      <check>Context loading must complete within 10 seconds</check>
      <action>Optimize loading strategy or reduce context scope</action>
      <priority>HIGH</priority>
    </rule>
  </validation_rules>
  
  <monitoring_metrics>
    <metric>Context loading time per hierarchy level</metric>
    <metric>Token usage efficiency across priority levels</metric>
    <metric>Import resolution success rate</metric>
    <metric>Cache hit ratio for resolved imports</metric>
    <metric>Context switching frequency and overhead</metric>
  </monitoring_metrics>
</context_quality_gates>
```

## Integration Points

```xml
<integration_points>
  <claude_code_integration>
    <memory_system>Integrates with Claude Code's hierarchical memory (project/user/imported)</memory_system>
    <import_syntax>Uses @import syntax for module references</import_syntax>
    <session_management>Coordinates with Claude Code session limits and context preservation</session_management>
  </claude_code_integration>
  
  <framework_integration>
    <command_loading>Commands automatically load required context hierarchy</command_loading>
    <module_composition>Modules reference other modules through @ import system</module_composition>
    <quality_enforcement>Context quality gates integrate with universal quality system</quality_enforcement>
  </framework_integration>
  
  <performance_integration>
    <parallel_loading>Leverage Claude 4's parallel execution for context loading</parallel_loading>
    <thinking_optimization>Use thinking blocks for context preparation and optimization</thinking_optimization>
    <token_optimization>Coordinate with token optimization patterns throughout framework</token_optimization>
  </performance_integration>
</integration_points>
```

## Usage Examples

### Basic Context Hierarchy

```xml
<!-- Session context establishment -->
<context_session>
  <level_1>CLAUDE.md + PROJECT_CONFIG.xml (10K tokens)</level_1>
  <level_2>@modules/patterns/intelligent-routing.md (5K tokens)</level_2>
  <level_3>@commands/auto.md (8K tokens)</level_3>
  <level_4>@system/quality/universal-quality-gates.md (12K tokens)</level_4>
  <level_5>@templates/task-specific-context.md (15K tokens)</level_5>
  <level_6>session_memory.json (5K tokens)</level_6>
  <total>55K tokens (27.5% of budget, 50K reserved for work)</total>
</context_session>
```

### Dynamic Context Loading

```python
# Example: /auto command with dynamic context loading
async def auto_command_context_loading():
    # Level 1: Framework core (immediate)
    await load_framework_core()
    
    # Level 2: Routing patterns (immediate)
    await load_module("@modules/patterns/intelligent-routing.md")
    
    # Level 3: Commands (on-demand based on routing decision)
    command_choice = await intelligent_routing()
    await load_module(f"@commands/{command_choice}.md")
    
    # Level 4: Domain context (predictive based on command)
    domain_modules = predict_domain_needs(command_choice)
    await batch_load_modules(domain_modules)
    
    # Level 5: Templates (lazy loading)
    template = await lazy_load_template(task_type)
    
    # Level 6: Session memory (preserved)
    session_context = load_session_memory()
    
    return construct_optimal_context()
```

### Context Optimization Patterns

```xml
<optimization_patterns>
  <pattern name="Progressive Context Loading">
    <description>Load context progressively based on task complexity</description>
    <implementation>Start with minimal context, expand as needed</implementation>
    <use_case>Unknown task complexity, exploratory analysis</use_case>
  </pattern>
  
  <pattern name="Predictive Context Preparation">
    <description>Pre-load context based on historical patterns</description>
    <implementation>Analyze usage patterns, pre-load likely modules</implementation>
    <use_case>Repetitive workflows, known task patterns</use_case>
  </pattern>
  
  <pattern name="Adaptive Context Switching">
    <description>Dynamically adjust context based on real-time needs</description>
    <implementation>Monitor execution, adapt context hierarchy</implementation>
    <use_case>Long-running sessions, evolving requirements</use_case>
  </pattern>
</optimization_patterns>
```

## Performance Targets

- **Context Loading**: <10 seconds for full hierarchy
- **Import Resolution**: <1 second per @ import
- **Token Efficiency**: >90% of allocated budget utilized
- **Cache Hit Ratio**: >80% for frequently accessed modules
- **Context Switching**: <2 seconds between major context changes
- **Memory Overhead**: <5% of total token budget for management

## Recovery Procedures

```xml
<recovery_procedures>
  <context_corruption>
    <detect>Validation failures, import resolution errors</detect>
    <recover>Clear cache, reload from framework files</recover>
    <fallback>Use minimal context with degraded functionality</fallback>
  </context_corruption>
  
  <token_budget_exceeded>
    <detect>Budget monitoring alerts</detect>
    <recover>Trigger eviction policies, compress context</recover>
    <fallback>Essential context only, request additional budget</fallback>
  </token_budget_exceeded>
  
  <import_resolution_failure>
    <detect>404 module not found errors</detect>
    <recover>Create from template, suggest alternatives</recover>
    <fallback>Skip optional imports, continue with available context</fallback>
  </import_resolution_failure>
</recovery_procedures>
```