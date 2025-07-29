# Source #11: ClaudeFlow

### Metadata
- **URL**: https://github.com/ceciliomichael/ClaudeFlow
- **Author/Organization**: ceciliomichael (Community)
- **Date**: 2025 (Active)
- **Type**: Community/Framework

### Verification Status
- ✅ Multi-phase workflow framework
- ✅ Command patterns defined
- ✅ Context persistence mechanism
- ✅ Planning and execution separation
- ✅ Claude integration optimized

### Rating: 5/5

### Key Patterns Observed

1. **Multi-Phase Workflow Pattern**:
   ```
   /plan → /act → /memory → [new session] → /recall → /act
   ```
   - Comprehensive planning phase
   - Iterative execution cycles
   - State persistence between sessions

2. **Command Structure**:
   - `/plan [description]`: Create project plan
   - `/act`: Execute current phase
   - `/memory`: Save project state
   - `/recall`: Load previous context
   - `/plancreate`: Single-phase planning
   - `/create`: Single-phase execution

3. **Context Management**:
   ```
   .session/
   ├── project-state.json
   ├── memory-bank.md
   └── execution-logs/
   ```

### Code Examples

```bash
# Multi-phase workflow
/plan Build a complete authentication system with JWT tokens

# Execute phase 1
/act

# Save state after phase completion
/memory

# In new session, restore context
/recall
/act  # Continue with phase 2
```

### Insights & Innovations

- Context chaining between sessions
- Structured project decomposition
- Persistent memory across restarts
- Complexity-based workflow selection
- IDE-optimized (Cursor/Claude 3.7)

### Practical Applications

- Large feature development
- Multi-day projects
- Team handoffs
- Incremental development
- Quality gate implementation

### Limitations/Caveats

- Requires manual session management
- IDE-specific optimizations
- Additional commands to learn