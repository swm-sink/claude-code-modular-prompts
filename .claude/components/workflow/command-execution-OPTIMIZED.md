# Command Execution Wrapper

**Purpose**: Standardized wrapper for command execution providing consistent initialization, parameter handling, progress tracking, and cleanup across all commands.

**Usage**: 
- Manages 4-phase execution (initialization, pre-execution, execution, post-execution)
- Validates environment, parameters, and prerequisites before execution
- Tracks progress with visual indicators (✅ 🔄 ⏸️ ❌)
- Handles errors with recovery options and state management
- Provides consistent user experience with standard patterns

**Compatibility**: 
- **Works with**: All commands, error-handler, progress-indicator
- **Requires**: command_parameters, execution_context, progress_tracking
- **Conflicts**: None (universal wrapper)

**Implementation**:
```xml
<include>components/workflow/command-execution.md</include>
🚀 Starting {command_name} execution...
✅ Step 1/N: Complete
🔄 Step 2/N: In Progress
✅ Completed successfully!
```

**Category**: workflow | **Complexity**: simple | **Time**: 30 minutes