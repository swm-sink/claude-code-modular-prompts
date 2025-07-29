<prompt_component>
  <step name="Command Execution Wrapper">
    <description>
      Standardized wrapper for command execution that provides consistent initialization,
      parameter handling, progress tracking, and cleanup across all commands.
    </description>
    <execution_phases>
      1. **Initialization Phase**:
         - Validate environment and prerequisites
         - Parse and validate input parameters
         - Initialize progress tracking
         - Set up error handling context
      
      2. **Pre-Execution Phase**:
         - Check required tools availability
         - Verify file/directory permissions
         - Load any required configurations
         - Display execution plan to user
      
      3. **Execution Phase**:
         - Execute command steps sequentially
         - Track progress after each step
         - Handle errors with recovery options
         - Maintain execution state
      
      4. **Post-Execution Phase**:
         - Generate execution summary
         - Clean up temporary resources
         - Save state if needed
         - Provide next steps guidance
    </execution_phases>
    <standard_patterns>
      ```
      # Command Initialization
      🚀 Starting {command_name} execution...
      📋 Parameters: {parameters}
      
      # Progress Tracking
      ✅ Step 1/N: {step_description} - Complete
      🔄 Step 2/N: {step_description} - In Progress
      ⏸️  Step 3/N: {step_description} - Pending
      
      # Error Handling
      ❌ Error in Step X: {error_description}
      🔧 Recovery options:
        1. {recovery_option_1}
        2. {recovery_option_2}
      
      # Completion
      ✅ {command_name} completed successfully!
      📊 Summary: {execution_summary}
      🎯 Next steps: {next_steps}
      ```
    </standard_patterns>
    <integration_example>
      ```xml
      <include>components/workflow/command-execution.md</include>
      
      <steps>
        <step name="Initialize">
          <action>Apply command execution wrapper initialization</action>
        </step>
        
        <!-- Command-specific steps here -->
        
        <step name="Complete">
          <action>Apply command execution wrapper completion</action>
        </step>
      </steps>
      ```
    </integration_example>
    <benefits>
      - Consistent user experience across all commands
      - Built-in error handling and recovery
      - Automatic progress tracking
      - Standardized parameter validation
      - Clean resource management
    </benefits>
    <output>
      When using this component:
      - Include at the beginning of command execution
      - Wrap all command logic within execution phases
      - Use standard progress indicators
      - Implement recovery options for all errors
      - Always provide clear completion status
    </output>
  </step>
</prompt_component>