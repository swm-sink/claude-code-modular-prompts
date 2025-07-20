# /meta-improve - User-Driven Prompt Improvement

**Purpose**: Improve the behavior of a command by providing feedback on its output and guiding the LLM to refine the underlying prompt.

## Usage
```bash
# Improve the last command that was run
/meta-improve

# Improve a specific command
/meta-improve --command=/task
```

## Workflow

The `/meta-improve` command initiates a conversational workflow to gather feedback and refine a command's prompt.

```xml
<improvement_workflow>
  <step name="Identify Target Command">
    <description>Identify the command to be improved. If the user doesn't specify a command, default to the last command that was run.</description>
    <interaction>
      <prompt>If the target command is not clear, ask the user: "Which command would you like to improve?"</prompt>
    </interaction>
  </step>
  
  <step name="Gather Feedback">
    <description>Engage the user in a conversation to understand what went wrong with the command's output and how it could be improved.</description>
    <interaction>
      <prompt>Ask the user to describe the issue: "What was the problem with the output of the `/task` command?"</prompt>
      <prompt>Ask for specific examples: "Can you give me an example of the incorrect output and what you would have expected instead?"</prompt>
      <prompt>Ask for suggestions: "How would you change the instructions for the `/task` command to prevent this issue in the future?"</prompt>
    </interaction>
  </step>
  
  <step name="Analyze & Generate Improvement">
    <description>Analyze the user's feedback and the target command's current prompt. Based on this analysis, generate a new, improved version of the prompt.</description>
    <tool_usage>
      <tool>Read</tool>
      <description>Read the contents of the target command's markdown file.</description>
    </tool_usage>
  </step>
  
  <step name="Propose Changes & Confirm">
    <description>Present the proposed changes to the user as a diff and ask for confirmation before applying them.</description>
    <interaction>
      <prompt>Show the user a diff of the changes: "Here are the changes I'm proposing for the `/task` command. Do you approve?"</prompt>
    </interaction>
  </step>
  
  <step name="Apply Changes">
    <description>Once the user confirms, apply the changes to the target command's markdown file.</description>
    <tool_usage>
      <tool>Write</tool>
      <description>Write the new, improved prompt to the target command's file.</description>
    </tool_usage>
  </step>
  
  <step name="Final Summary">
    <description>Provide a summary of the completed improvement and thank the user for their feedback.</description>
    <output>A confirmation message: "Thank you for your feedback! The `/task` command has been successfully improved."</output>
  </step>
</improvement_workflow>
```

This user-driven improvement mechanism is a key feature of the "Prompt Factory," allowing the framework to learn and adapt based on real-world usage. 