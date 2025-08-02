# Workflow Coordinator Component

**Purpose**: Coordinate multi-step workflow execution with dependency management and failure recovery

**Usage**: 
Accept and parse input data or parameters for workflow initialization
Define workflow step sequence and manage dependencies between steps
Execute steps in proper order while handling parallel execution opportunities
Process step failures with appropriate recovery strategies and rollback
Coordinate state management across workflow steps and components
Ensure workflow completion criteria are met before finalizing results

**Compatibility**: 
- **Works with**: task-summary, progress-indicator, error-handler, state-manager
- **Requires**: workflow_definition (object), input_data (any)
- **Conflicts**: None (designed for orchestration)

**Implementation**:
```javascript
// Define and execute multi-step workflow
const workflow = {
  steps: [
    {id: "validate", component: "input-validation", depends: []},
    {id: "process", component: "data-transformer", depends: ["validate"]},
    {id: "save", component: "file-writer", depends: ["process"]}
  ],
  recovery: "rollback_on_failure",
  parallel: true  // Allow parallel execution where possible
};

const result = await coordinate_workflow(workflow, input_data);
if (!result.success) {
  return handle_error("workflow", `Step ${result.failed_step} failed: ${result.error}`);
}

return result.final_output;
```

**Category**: atomic | **Complexity**: complex | **Time**: 30 minutes