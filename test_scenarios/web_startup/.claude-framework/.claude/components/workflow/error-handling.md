<prompt_component>
  <step name="Standardized Error Handling">
    <description>
      Implement consistent error handling, validation, and recovery patterns across all commands.
      Provide standardized error detection, classification, user feedback, and recovery options.
      Ensure graceful degradation and clear communication when issues arise.
    </description>
    <error_management>
      1. **Error Detection and Classification**:
         - **System Errors**: File access, network, permissions
         - **User Input Errors**: Invalid parameters, missing files
         - **Logic Errors**: Unexpected conditions, edge cases
         - **External Errors**: API failures, tool unavailability

      2. **Error Response Patterns**:
         - **Immediate**: Stop execution for critical errors
         - **Graceful**: Continue with reduced functionality
         - **Retry**: Attempt recovery with backoff strategy
         - **Fallback**: Switch to alternative approach

      3. **User Communication**:
         - Clear, actionable error messages
         - Specific problem identification
         - Suggested resolution steps
         - Context about what was being attempted

      4. **Recovery and Continuation**:
         - Suggest alternative approaches
         - Provide partial results when possible
         - Offer retry mechanisms
         - Log errors for debugging
    </error_management>
    <output>
      Use standardized error reporting format:
      
      **🚨 Error Detected**: [Clear description of what went wrong]
      
      **📍 Context**: [What was being attempted when error occurred]
      
      **🔍 Cause**: [Specific reason for the error]
      
      **🛠️ Suggested Actions**:
      - [Specific step 1 to resolve]
      - [Specific step 2 to resolve]
      - [Alternative approach if applicable]
      
      **🔄 Recovery Options**:
      - [How to retry or continue]
      - [Fallback solutions available]
      
      Always maintain helpful tone and provide actionable guidance.
      When possible, offer to continue with partial functionality.
    </output>
  </step>
</prompt_component>