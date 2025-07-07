# /prompt Command Integration Example

## How the Command Works with the Framework

### 1. Command Invocation
When a user types `/prompt create "my assistant"`, the framework:

1. **Routes to Command File**: `.claude/commands/prompt.md`
2. **Reads Delegation Target**: `modules/development/prompt-engineering.md`
3. **Loads Supporting Modules**: 
   - `modules/quality/critical-thinking.md`
   - `modules/patterns/research-analysis.md`
   - `modules/patterns/session-management.md`

### 2. Delegation Pattern in Action

```xml
<!-- In commands/prompt.md -->
<delegation target="modules/development/prompt-engineering.md">
  This command delegates ALL implementation to the prompt engineering module...
</delegation>
```

The command file contains NO implementation logic, only:
- Command structure and metadata
- Delegation instructions
- Parameter definitions
- Usage examples

### 3. Module Execution

The module (`prompt-engineering.md`) contains the actual implementation:

```xml
<!-- In modules/development/prompt-engineering.md -->
<workflow name="prompt_engineering_lifecycle">
  <phase name="initialization" order="1">
    <!-- Actual implementation logic -->
  </phase>
  <phase name="create" order="2">
    <!-- Creation workflow -->
  </phase>
  <!-- More phases... -->
</workflow>
```

### 4. Integration with Other Commands

#### Example: Complex Prompt System with /swarm
```bash
# User wants to create a multi-prompt conversational system
/swarm "Create customer service bot with context-aware prompts"

# The swarm command might internally use:
# - /prompt create "greeting-prompt" --type system
# - /prompt create "query-handler" --type assistant  
# - /prompt create "escalation-prompt" --type hybrid
# - /prompt test "all-prompts/*.md" --scenarios all
```

#### Example: Tracked Improvement Session
```bash
# Start a session for prompt optimization
/session start "Q1 Prompt Optimization" --issue #23

# Use prompt commands within session
/prompt evaluate "production/*.md" --output baseline-q1.json
/prompt improve "production/*.md" --iterations 3
/prompt test "production/*.md" --scenarios all

# Session automatically tracks all operations
/session complete --summary "Improved avg effectiveness by 23%"
```

#### Example: Autonomous Prompt Development
```bash
# Let /auto intelligently handle prompt creation
/auto "I need better error handling in my API prompts"

# Auto might:
# 1. Research current error handling patterns
# 2. Evaluate existing prompts
# 3. Create improved versions
# 4. Test thoroughly
# 5. Generate comparison report
```

### 5. Framework Benefits

1. **Modularity**: Update prompt engineering logic without touching command
2. **Reusability**: Other commands can leverage prompt engineering module
3. **Consistency**: All commands follow same delegation pattern
4. **Extensibility**: Easy to add new subcommands or features
5. **Testing**: Command and module can be tested independently

### 6. Error Handling Flow

```
User Input → Command Validation → Module Routing → Implementation
     ↓              ↓                    ↓              ↓
   Error ←──────────┴────────────────────┴──────────────┘
     ↓
User-Friendly Message with Recovery Options
```

### 7. Token Optimization

The framework ensures efficient token usage:
- Command file: ~500 tokens (structure only)
- Module file: ~1800 tokens (implementation)
- Only loaded when needed
- Supporting modules loaded on-demand

### 8. Future Extensions

The modular design enables easy additions:

```xml
<!-- Easy to add new subcommands -->
<subcommand name="analyze">
  <purpose>Deep analysis of prompt patterns</purpose>
</subcommand>

<!-- Easy to add new parameters -->
<parameter name="--model" values="claude-3|gpt-4|llama">
  <purpose>Target model optimization</purpose>
</parameter>

<!-- Easy to integrate new modules -->
<supporting_modules>
  <module>modules/ai/model-specific-optimization.md</module>
</supporting_modules>
```

## Summary

The `/prompt` command exemplifies the framework's design principles:
- **Delegation**: Command delegates ALL implementation
- **Modularity**: Clean separation of concerns
- **Integration**: Works seamlessly with other commands
- **Quality**: Built-in testing and validation
- **Evolution**: Easy to extend and improve